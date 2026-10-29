// Integration tests against a real Postgres (TEST_DATABASE_URL). Skipped when unset.
import { readFileSync } from "node:fs";
import { join } from "node:path";
import postgres from "postgres";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

const url = process.env.TEST_DATABASE_URL;
process.env.DATABASE_URL = url;
process.env.ADMIN_PASSWORD ??= "test";

type Admin = typeof import("@/lib/admin");
type Participant = typeof import("@/lib/participant");
type State = typeof import("@/lib/state");

describe.skipIf(!url)("auction (database)", () => {
  let admin: Admin["runAdminAction"];
  let register: Participant["register"];
  let placeBid: Participant["placeBid"];
  let state: State;
  let raw: postgres.Sql;
  const tokens = new Map<number, string>(); // participant id → device token

  const levels = ["Analyst", "Analyst", "Analyst", "Associate", "Associate", "VP", "VP", "Director"] as const;

  async function checkIn(i: number) {
    const { token } = await register(undefined, {
      name: `Person ${i}`,
      department: ["M&A", "ECM", "Risk", "Ops"][i % 4],
      level: i % 37 === 0 ? "MD" : levels[i % levels.length],
    });
    const me = await state.getMeState({ participant: token! });
    tokens.set(me.participant!.id, token!);
    return { token: token!, id: me.participant!.id };
  }

  async function leaders() {
    const rows = await raw<{ id: number; leader_id: number }[]>`select id, leader_id from teams order by id`;
    return rows.map((t) => ({ teamId: t.id, token: tokens.get(t.leader_id)! }));
  }

  const bid = (token: string, lotId: number, amount: number) => placeBid({ participant: token }, { lotId, amount });
  const bidError = (token: string, lotId: number, amount: number) =>
    bid(token, lotId, amount).then(
      () => null,
      (e: { message: string; status: number }) => e,
    );

  beforeAll(async () => {
    raw = postgres(url!, { onnotice: () => {} });
    await raw.unsafe("drop schema public cascade; create schema public;");
    await raw.unsafe(readFileSync(join(__dirname, "..", "db", "schema.sql"), "utf8"));
    ({ runAdminAction: admin } = await import("@/lib/admin"));
    ({ register, placeBid } = await import("@/lib/participant"));
    state = await import("@/lib/state");
  });

  afterAll(async () => {
    await raw.end();
    await (await import("@/lib/db")).db().end();
  });

  it("checks in 80 people concurrently and deals them into 10 balanced teams with leaders", async () => {
    await Promise.all(Array.from({ length: 80 }, (_, i) => checkIn(i + 1)));
    await admin({ action: "teams.generate", teamCount: 10 });

    const teams = await raw<{ id: number; leader_id: number | null; size: number }[]>`
      select t.id, t.leader_id, count(p.id)::int as size
      from teams t join participants p on p.team_id = t.id group by t.id`;
    expect(teams).toHaveLength(10);
    expect(teams.every((t) => t.size === 8 && t.leader_id !== null)).toBe(true);

    const spread = await raw<{ level: string; spread: number }[]>`
      select level, max(n) - min(n) as spread from (
        select l.level, t.id, count(p.id) as n
        from teams t cross join (select distinct level from participants) l
        left join participants p on p.team_id = t.id and p.level = l.level
        group by l.level, t.id) x group by level`;
    expect(spread.every((s) => s.spread <= 1)).toBe(true);
  });

  it("hides teams until revealed, then shows a phone its own team", async () => {
    const [someone] = [...tokens.values()];
    expect((await state.getMeState({ participant: someone })).team).toBeNull();
    expect((await state.getPublicState()).teams).toHaveLength(0);

    await admin({ action: "reveal.next" });
    expect((await state.getPublicState()).teams).toHaveLength(1);
    await admin({ action: "reveal.all" });
    const me = await state.getMeState({ participant: someone });
    expect(me.team?.members.length).toBe(8);
    expect((await state.getPublicState()).teams).toHaveLength(10);
  });

  it("places a late arrival without breaking the balance", async () => {
    const late = await checkIn(81);
    const [row] = await raw<{ team_id: number | null }[]>`select team_id from participants where id = ${late.id}`;
    expect(row.team_id).not.toBeNull();
    const sizes = await raw<{ n: number }[]>`select count(*)::int as n from participants group by team_id`;
    expect(Math.max(...sizes.map((s) => s.n)) - Math.min(...sizes.map((s) => s.n))).toBeLessThanOrEqual(1);
  });

  it("enforces the bidding rules", async () => {
    const { id: lotId } = (await admin({ action: "lot.create", title: "Unlimited WFH", startPrice: 100, step: 10, durationS: 60 })) as { id: number };
    expect(await bidError((await leaders())[0].token, lotId, 100)).toMatchObject({ message: "Bidding on this perk has closed" });
    await admin({ action: "lot.start", id: lotId });

    const [a, b] = await leaders();
    const [notLeader] = await raw<{ id: number }[]>`
      select p.id from participants p join teams t on t.id = p.team_id where p.id <> t.leader_id limit 1`;
    expect(await bidError(tokens.get(notLeader.id)!, lotId, 200)).toMatchObject({ status: 403 });

    expect(await bidError(a.token, lotId, 90)).toMatchObject({ message: expect.stringContaining("minimum bid is now 100") });
    await bid(a.token, lotId, 100);
    expect(await bidError(a.token, lotId, 150)).toMatchObject({ message: "You already have the top bid" });
    expect(await bidError(b.token, lotId, 105)).toMatchObject({ message: expect.stringContaining("now 110") });
    expect(await bidError(b.token, lotId, 5000)).toMatchObject({ message: expect.stringContaining("Not enough coins") });
    await bid(b.token, lotId, 110);
    // Team A bid moments ago: a second bid within 400 ms is rejected as a double tap.
    expect(await bidError(a.token, lotId, 120)).toMatchObject({ status: 429 });
  });

  it("serializes simultaneous bids: amounts strictly climb and no team outbids itself", async () => {
    await new Promise((r) => setTimeout(r, 450));
    const [{ id: lotId }] = await raw<{ id: number }[]>`select id from lots where status = 'live'`;
    const all = await leaders();
    // Every leader fires 5 bids at once, each trying to beat the current top by one step.
    await Promise.all(
      all.flatMap((l, i) =>
        Array.from({ length: 5 }, async (_, k) => {
          await new Promise((r) => setTimeout(r, k * 450 + (i % 3)));
          const s = await state.getPublicState();
          await bid(l.token, lotId, s.lot!.minNext).catch(() => {});
        }),
      ),
    );
    const bids = await raw<{ team_id: number; amount: number }[]>`
      select team_id, amount from bids where lot_id = ${lotId} and not voided order by id`;
    expect(bids.length).toBeGreaterThan(5);
    for (let i = 1; i < bids.length; i++) {
      expect(bids[i].amount).toBeGreaterThanOrEqual(bids[i - 1].amount + 10);
      expect(bids[i].team_id).not.toBe(bids[i - 1].team_id);
    }
  });

  it("extends the clock on a last-second bid (anti-snipe)", async () => {
    const [{ id: lotId }] = await raw<{ id: number }[]>`select id from lots where status = 'live'`;
    await raw`update lots set ends_at = clock_timestamp() + interval '3 seconds' where id = ${lotId}`;
    const s = await state.getPublicState();
    const bidder = (await leaders()).find((l) => l.teamId !== s.lot!.top!.teamId)!;
    await bid(bidder.token, lotId, s.lot!.minNext);
    const [{ left }] = await raw<{ left: number }[]>`
      select extract(epoch from ends_at - clock_timestamp()) as left from lots where id = ${lotId}`;
    expect(Number(left)).toBeGreaterThan(9);
  });

  it("pauses, resumes, adds time and undoes a bid", async () => {
    const [{ id }] = await raw<{ id: number }[]>`select id from lots where status = 'live'`;
    await admin({ action: "lot.pause", id });
    let s = await state.getPublicState();
    expect(s.lot!.status).toBe("paused");
    const top = s.lot!.top!;
    expect(await bidError((await leaders()).find((l) => l.teamId !== top.teamId)!.token, id, s.lot!.minNext)).toMatchObject({
      message: "Bidding on this perk has closed",
    });
    await admin({ action: "lot.addTime", id, seconds: 15 });
    await admin({ action: "lot.resume", id });
    await admin({ action: "lot.undo", id });
    s = await state.getPublicState();
    expect(s.lot!.status).toBe("live");
    expect(s.lot!.top!.amount).toBeLessThan(top.amount);
  });

  it("sells to the top bid when the timer runs out and charges the winner", async () => {
    const [{ id }] = await raw<{ id: number }[]>`select id from lots where status = 'live'`;
    const before = await state.getPublicState();
    const top = before.lot!.top!;
    await raw`update lots set ends_at = clock_timestamp() - interval '1 second' where id = ${id}`;
    const after = await state.getPublicState();
    expect(after.lot).toMatchObject({ id, status: "sold", winnerTeamId: top.teamId, price: top.amount });
    const winner = after.teams.find((t) => t.id === top.teamId)!;
    expect(winner.coinsLeft).toBe(winner.coins - top.amount);
    expect(winner.perks.map((p) => p.title)).toEqual(["Unlimited WFH"]);
  });

  it("runs only one perk at a time, hides mystery perks, and re-auctions", async () => {
    const one = (await admin({ action: "lot.create", title: "Leave early Friday", mystery: true })) as { id: number };
    const two = (await admin({ action: "lot.create", title: "Pick the team lunch" })) as { id: number };
    await admin({ action: "lot.start", id: one.id });
    await expect(admin({ action: "lot.start", id: two.id })).rejects.toMatchObject({ status: 409 });

    let s = await state.getPublicState();
    expect(s.lot).toMatchObject({ id: one.id, title: "Mystery perk" });
    await admin({ action: "lot.close", id: one.id });
    s = await state.getPublicState();
    expect(s.lot).toMatchObject({ id: one.id, status: "unsold", title: "Leave early Friday" });

    await admin({ action: "lot.reopen", id: one.id });
    s = await state.getPublicState();
    expect(s.lots.find((l) => l.id === one.id)?.status).toBe("queued");
  });

  it("enforces the max-perks rule", async () => {
    await admin({ action: "settings.update", settings: { maxPerksPerTeam: 1 } });
    const [{ winner }] = await raw<{ winner: number }[]>`select winner_team_id as winner from lots where status = 'sold'`;
    const [{ id }] = await raw<{ id: number }[]>`select id from lots where status = 'queued' order by sort_order limit 1`;
    await admin({ action: "lot.start", id });
    const team = (await leaders()).find((l) => l.teamId === winner)!;
    const minNext = (await state.getPublicState()).lot!.minNext;
    expect(await bidError(team.token, id, minNext)).toMatchObject({ message: expect.stringContaining("maximum number of perks") });
    await admin({ action: "lot.close", id });
    await admin({ action: "settings.update", settings: { maxPerksPerTeam: 0 } });
  });

  it("lets a phone with a paddle QR bid for that team", async () => {
    const [team] = await raw<{ id: number }[]>`select id from teams order by id limit 1`;
    const { paddlePath } = (await admin({ action: "team.paddle", teamId: team.id })) as { paddlePath: string };
    const token = paddlePath.split("/").pop()!;
    const me = await state.getMeState({ paddle: token });
    expect(me.participant).toBeNull();
    expect(me.bidTeam?.id).toBe(team.id);

    const { id } = (await admin({ action: "lot.create", title: "Paddle test", startPrice: 5 })) as { id: number };
    await admin({ action: "lot.start", id });
    await placeBid({ paddle: token }, { lotId: id, amount: 5 });
    expect((await state.getPublicState()).lot?.top).toEqual({ teamId: team.id, amount: 5 });
    await admin({ action: "lot.close", id });

    await admin({ action: "team.revokePaddles", teamId: team.id });
    expect((await state.getMeState({ paddle: token })).bidTeam).toBeNull();
  });

  it("resets the auction but keeps people and teams", async () => {
    await admin({ action: "reset", scope: "auction" });
    const [counts] = await raw<{ bids: number; open: number; people: number; teams: number }[]>`
      select (select count(*) from bids)::int as bids,
             (select count(*) from lots where status <> 'queued')::int as open,
             (select count(*) from participants)::int as people,
             (select count(*) from teams)::int as teams`;
    expect(counts).toEqual({ bids: 0, open: 0, people: 81, teams: 10 });
  });
});
