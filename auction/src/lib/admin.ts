// Organizer actions. Each runs in one transaction that locks app_state first, so
// concurrent admin actions and check-ins serialize in a consistent lock order.
import { z } from "zod";
import { balanceTeams, pickLeader, pickTeamFor, shuffle, type Person } from "./balance";
import { transaction, type Sql } from "./db";
import { HttpError } from "./http";
import { LEVELS } from "./levels";
import { hashToken, newToken } from "./session";
import { settingsSchema, type LeaderRule } from "./settings";
import { loadApp, type AppState, type MemberRow } from "./state";
import { TEAM_STYLES } from "./teamStyles";
import { BOARD_SCENES, PHASES } from "./types";

const id = z.number().int().positive();
const name = z.string().trim().min(1).max(40);
const department = z.string().trim().max(40);
const lotFields = {
  title: z.string().trim().min(1).max(80),
  emoji: z.string().trim().min(1).max(16),
  description: z.string().trim().max(300),
  mystery: z.boolean(),
  startPrice: z.number().int().min(1),
  step: z.number().int().min(1),
  durationS: z.number().int().min(5).max(3600),
};

export const actionSchema = z.discriminatedUnion("action", [
  z.object({ action: z.literal("settings.update"), settings: settingsSchema.partial() }),
  z.object({ action: z.literal("phase.set"), phase: z.enum(PHASES) }),
  z.object({ action: z.literal("checkin.set"), open: z.boolean() }),
  z.object({ action: z.literal("board.set"), scene: z.enum(BOARD_SCENES), message: z.string().max(200).optional() }),
  z.object({ action: z.literal("reveal.next") }),
  z.object({ action: z.literal("reveal.all") }),
  z.object({ action: z.literal("reveal.reset") }),
  z.object({
    action: z.literal("participant.add"),
    name,
    department: department.default(""),
    level: z.enum(LEVELS),
    teamId: id.nullable().optional(),
  }),
  z.object({
    action: z.literal("participant.update"),
    id,
    name: name.optional(),
    department: department.optional(),
    level: z.enum(LEVELS).optional(),
    teamId: id.nullable().optional(),
  }),
  z.object({ action: z.literal("participant.delete"), id }),
  z.object({ action: z.literal("teams.generate"), teamCount: z.number().int().min(2).max(12) }),
  z.object({ action: z.literal("teams.clear") }),
  z.object({ action: z.literal("teams.setCoins"), coins: z.number().int().min(0).max(1_000_000) }),
  z.object({
    action: z.literal("team.update"),
    id,
    name: z.string().trim().min(1).max(30).optional(),
    color: z.string().regex(/^#[0-9a-fA-F]{6}$/).optional(),
    tableNo: z.number().int().min(1).max(99).optional(),
    coins: z.number().int().min(0).max(1_000_000).optional(),
  }),
  z.object({ action: z.literal("team.setLeader"), teamId: id, participantId: id }),
  z.object({ action: z.literal("team.rerollLeader"), teamId: id }),
  z.object({ action: z.literal("team.paddle"), teamId: id }),
  z.object({ action: z.literal("team.revokePaddles"), teamId: id }),
  z.object({
    action: z.literal("lot.create"),
    title: lotFields.title,
    emoji: lotFields.emoji.optional(),
    description: lotFields.description.optional(),
    mystery: lotFields.mystery.optional(),
    startPrice: lotFields.startPrice.optional(),
    step: lotFields.step.optional(),
    durationS: lotFields.durationS.optional(),
  }),
  z.object({
    action: z.literal("lot.update"),
    id,
    title: lotFields.title.optional(),
    emoji: lotFields.emoji.optional(),
    description: lotFields.description.optional(),
    mystery: lotFields.mystery.optional(),
    startPrice: lotFields.startPrice.optional(),
    step: lotFields.step.optional(),
    durationS: lotFields.durationS.optional(),
  }),
  z.object({ action: z.literal("lot.delete"), id }),
  z.object({ action: z.literal("lot.move"), id, direction: z.enum(["up", "down"]) }),
  z.object({ action: z.literal("lot.start"), id }),
  z.object({ action: z.literal("lot.pause"), id }),
  z.object({ action: z.literal("lot.resume"), id }),
  z.object({ action: z.literal("lot.addTime"), id, seconds: z.number().int().min(1).max(600) }),
  z.object({ action: z.literal("lot.close"), id }),
  z.object({ action: z.literal("lot.undo"), id }),
  z.object({ action: z.literal("lot.reopen"), id }),
  z.object({ action: z.literal("reset"), scope: z.enum(["auction", "teams", "everything"]) }),
]);

export type AdminAction = z.infer<typeof actionSchema>;

export const bumpPeople = (tx: Sql) => tx`update app_state set people_version = people_version + 1 where id = 1`;

async function teamMembers(tx: Sql, teamId: number) {
  return tx<MemberRow[]>`select id, name, department, level, team_id from participants where team_id = ${teamId}`;
}

// Gives the team a leader by the configured rule when it has none (or the
// current one left the team). `force` re-rolls, avoiding the current leader if possible.
export async function ensureLeader(tx: Sql, teamId: number, rule: LeaderRule, force = false) {
  const [team] = await tx<{ leader_id: number | null }[]>`select leader_id from teams where id = ${teamId}`;
  if (!team) return;
  const members = await teamMembers(tx, teamId);
  const current = members.find((m) => m.id === team.leader_id);
  if (current && !force) return;
  const pool = force && members.length > 1 ? members.filter((m) => m.id !== team.leader_id) : members;
  const leader = pickLeader(pool, rule);
  await tx`update teams set leader_id = ${leader?.id ?? null} where id = ${teamId}`;
}

// Puts a participant who arrives after the teams were made into the team that keeps
// the balance best. Returns the chosen team id, or null when there are no teams yet.
export async function placeLateArrival(tx: Sql, person: Person): Promise<number | null> {
  const teams = await tx<{ id: number }[]>`select id from teams order by table_no, id`;
  if (teams.length === 0) return null;
  const members = await tx<MemberRow[]>`
    select id, name, department, level, team_id from participants where team_id is not null and id <> ${person.id}`;
  const grouped = teams.map((t) => members.filter((m) => m.team_id === t.id));
  return teams[pickTeamFor(person, grouped)].id;
}

async function assertNoAuctionActivity(tx: Sql) {
  const [row] = await tx<{ n: number }[]>`
    select (select count(*) from bids)::int + (select count(*) from lots where status <> 'queued')::int as n`;
  if (row.n > 0) {
    throw new HttpError(409, "The auction has already started. Reset the auction (Settings) before changing teams this way.");
  }
}

async function lockLot(tx: Sql, lotId: number) {
  const [lot] = await tx<{ id: number; status: string; ends_at: Date | null; paused_ms_left: number | null }[]>`
    select id, status, ends_at, paused_ms_left from lots where id = ${lotId} for update`;
  if (!lot) throw new HttpError(404, "Perk not found");
  return lot;
}

async function setPhase(tx: Sql, app: AppState, phase: AppState["phase"]) {
  const [{ n: teamCount }] = await tx<{ n: number }[]>`select count(*)::int as n from teams`;
  if ((phase === "teams" || phase === "auction") && teamCount === 0) {
    throw new HttpError(409, "Generate the teams first");
  }
  if (phase === "checkin") {
    await tx`update app_state set phase = 'checkin', board_scene = 'checkin', reveal_count = 0 where id = 1`;
  } else if (phase === "teams") {
    const revealCount = app.phase === "checkin" ? 0 : app.revealCount;
    await tx`update app_state set phase = 'teams', board_scene = 'reveal', reveal_count = ${revealCount} where id = 1`;
  } else if (phase === "auction") {
    await tx`update app_state set phase = 'auction', board_scene = 'lot', reveal_count = ${teamCount} where id = 1`;
  } else {
    await tx`update app_state set phase = 'results', board_scene = 'leaderboard', reveal_count = ${teamCount} where id = 1`;
  }
  await bumpPeople(tx);
}

export async function runAdminAction(input: unknown): Promise<Record<string, unknown>> {
  const action = actionSchema.parse(input);
  return transaction(async (tx) => {
    const app = await loadApp(tx, { lock: true });
    const rule = app.settings.leaderRule;

    switch (action.action) {
      case "settings.update": {
        const settings = settingsSchema.parse({ ...app.settings, ...action.settings });
        await tx`update app_state set settings = ${tx.json(settings)} where id = 1`;
        return {};
      }

      case "phase.set":
        await setPhase(tx, app, action.phase);
        return {};

      case "checkin.set":
        await tx`update app_state set checkin_open = ${action.open} where id = 1`;
        return {};

      case "board.set":
        await tx`
          update app_state set board_scene = ${action.scene},
            board_message = ${action.message ?? app.boardMessage} where id = 1`;
        return {};

      case "reveal.next":
      case "reveal.all":
      case "reveal.reset": {
        const [{ n: teamCount }] = await tx<{ n: number }[]>`select count(*)::int as n from teams`;
        if (teamCount === 0) throw new HttpError(409, "Generate the teams first");
        const current = app.phase === "checkin" ? 0 : app.revealCount;
        const next =
          action.action === "reveal.all" ? teamCount : action.action === "reveal.reset" ? 0 : Math.min(current + 1, teamCount);
        const phase = app.phase === "checkin" ? "teams" : app.phase;
        await tx`update app_state set phase = ${phase}, board_scene = 'reveal', reveal_count = ${next} where id = 1`;
        await bumpPeople(tx);
        return { revealCount: next, teamCount };
      }

      case "participant.add": {
        const [person] = await tx<{ id: number }[]>`
          insert into participants (name, department, level, team_id)
          values (${action.name}, ${action.department}, ${action.level}, ${action.teamId ?? null}) returning id`;
        if (action.teamId === undefined) {
          const teamId = await placeLateArrival(tx, { id: person.id, level: action.level, department: action.department });
          if (teamId) await tx`update participants set team_id = ${teamId} where id = ${person.id}`;
        }
        const [row] = await tx<{ team_id: number | null }[]>`select team_id from participants where id = ${person.id}`;
        if (row.team_id) await ensureLeader(tx, row.team_id, rule);
        await bumpPeople(tx);
        return { id: person.id };
      }

      case "participant.update": {
        const [before] = await tx<MemberRow[]>`
          select id, name, department, level, team_id from participants where id = ${action.id} for update`;
        if (!before) throw new HttpError(404, "Person not found");
        await tx`
          update participants set
            name = ${action.name ?? before.name},
            department = ${action.department ?? before.department},
            level = ${action.level ?? before.level},
            team_id = ${action.teamId === undefined ? before.team_id : action.teamId}
          where id = ${action.id}`;
        if (action.teamId !== undefined && action.teamId !== before.team_id) {
          if (before.team_id) {
            await tx`update teams set leader_id = null where id = ${before.team_id} and leader_id = ${action.id}`;
            await ensureLeader(tx, before.team_id, rule);
          }
          if (action.teamId) await ensureLeader(tx, action.teamId, rule);
        }
        await bumpPeople(tx);
        return {};
      }

      case "participant.delete": {
        const [gone] = await tx<{ team_id: number | null }[]>`
          delete from participants where id = ${action.id} returning team_id`;
        if (!gone) throw new HttpError(404, "Person not found");
        if (gone.team_id) await ensureLeader(tx, gone.team_id, rule);
        await bumpPeople(tx);
        return {};
      }

      case "teams.generate": {
        await assertNoAuctionActivity(tx);
        const people = await tx<MemberRow[]>`select id, name, department, level, team_id from participants`;
        if (people.length < action.teamCount) {
          throw new HttpError(409, `Only ${people.length} people have checked in; that's not enough for ${action.teamCount} teams`);
        }
        await tx`delete from teams`;
        const groups = balanceTeams(people, action.teamCount);
        // Teams are revealed on the big screen in a random order, for suspense.
        const revealOrder = shuffle(groups.map((_, i) => i));
        for (const [index, members] of groups.entries()) {
          const style = TEAM_STYLES[index % TEAM_STYLES.length];
          const [team] = await tx<{ id: number }[]>`
            insert into teams (name, color, table_no, reveal_order, coins)
            values (${style.name}, ${style.color}, ${index + 1}, ${revealOrder.indexOf(index) + 1}, ${app.settings.startingCoins})
            returning id`;
          const ids = members.map((m) => m.id);
          await tx`update participants set team_id = ${team.id} where id in ${tx(ids)}`;
          const leader = pickLeader(members, rule);
          await tx`update teams set leader_id = ${leader?.id ?? null} where id = ${team.id}`;
        }
        await tx`
          update app_state set
            settings = jsonb_set(settings, '{teamCount}', ${tx.json(action.teamCount)}::jsonb),
            reveal_count = 0,
            phase = case when phase = 'checkin' then 'checkin' else 'teams' end,
            board_scene = case when phase = 'checkin' then board_scene else 'reveal' end
          where id = 1`;
        await bumpPeople(tx);
        return { teams: groups.length };
      }

      case "teams.clear": {
        await assertNoAuctionActivity(tx);
        await tx`delete from teams`;
        await tx`update app_state set phase = 'checkin', board_scene = 'checkin', reveal_count = 0 where id = 1`;
        await bumpPeople(tx);
        return {};
      }

      case "teams.setCoins":
        await tx`update teams set coins = ${action.coins}`;
        await tx`
          update app_state set settings = jsonb_set(settings, '{startingCoins}', ${tx.json(action.coins)}::jsonb) where id = 1`;
        await bumpPeople(tx);
        return {};

      case "team.update": {
        const [team] = await tx<{ name: string; color: string; table_no: number; coins: number }[]>`
          select name, color, table_no, coins from teams where id = ${action.id} for update`;
        if (!team) throw new HttpError(404, "Team not found");
        await tx`
          update teams set
            name = ${action.name ?? team.name},
            color = ${action.color ?? team.color},
            table_no = ${action.tableNo ?? team.table_no},
            coins = ${action.coins ?? team.coins}
          where id = ${action.id}`;
        await bumpPeople(tx);
        return {};
      }

      case "team.setLeader": {
        const [member] = await tx<{ id: number }[]>`
          select id from participants where id = ${action.participantId} and team_id = ${action.teamId}`;
        if (!member) throw new HttpError(409, "That person is not on this team");
        await tx`update teams set leader_id = ${action.participantId} where id = ${action.teamId}`;
        await bumpPeople(tx);
        return {};
      }

      case "team.rerollLeader":
        await ensureLeader(tx, action.teamId, rule, true);
        await bumpPeople(tx);
        return {};

      case "team.paddle": {
        const token = newToken();
        await tx`insert into paddles (token_hash, team_id) values (${hashToken(token)}, ${action.teamId})`;
        return { paddlePath: `/paddle/${token}` };
      }

      case "team.revokePaddles":
        await tx`delete from paddles where team_id = ${action.teamId}`;
        return {};

      case "lot.create": {
        const s = app.settings;
        const [lot] = await tx<{ id: number }[]>`
          insert into lots (sort_order, title, emoji, description, mystery, start_price, step, duration_s)
          values (
            (select coalesce(max(sort_order), 0) + 1 from lots),
            ${action.title}, ${action.emoji ?? "🎁"}, ${action.description ?? ""}, ${action.mystery ?? false},
            ${action.startPrice ?? s.defaultStartPrice}, ${action.step ?? s.defaultStep},
            ${action.durationS ?? s.defaultDuration})
          returning id`;
        return { id: lot.id };
      }

      case "lot.update": {
        const [lot] = await tx<
          {
            status: string;
            title: string;
            emoji: string;
            description: string;
            mystery: boolean;
            start_price: number;
            step: number;
            duration_s: number;
          }[]
        >`
          select status, title, emoji, description, mystery, start_price, step, duration_s
          from lots where id = ${action.id} for update`;
        if (!lot) throw new HttpError(404, "Perk not found");
        const pricing = action.startPrice !== undefined || action.step !== undefined || action.durationS !== undefined;
        if (pricing && lot.status !== "queued") {
          throw new HttpError(409, "Prices and timer can only be changed before the perk goes up for auction");
        }
        await tx`
          update lots set
            title = ${action.title ?? lot.title},
            emoji = ${action.emoji ?? lot.emoji},
            description = ${action.description ?? lot.description},
            mystery = ${action.mystery ?? lot.mystery},
            start_price = ${action.startPrice ?? lot.start_price},
            step = ${action.step ?? lot.step},
            duration_s = ${action.durationS ?? lot.duration_s}
          where id = ${action.id}`;
        return {};
      }

      case "lot.delete": {
        const lot = await lockLot(tx, action.id);
        if (lot.status === "live" || lot.status === "paused") throw new HttpError(409, "Close this perk before deleting it");
        await tx`delete from lots where id = ${action.id}`;
        return {};
      }

      case "lot.move": {
        const lots = await tx<{ id: number; sort_order: number }[]>`select id, sort_order from lots order by sort_order, id`;
        const i = lots.findIndex((l) => l.id === action.id);
        const j = action.direction === "up" ? i - 1 : i + 1;
        if (i < 0 || j < 0 || j >= lots.length) return {};
        [lots[i], lots[j]] = [lots[j], lots[i]];
        for (const [index, lot] of lots.entries()) {
          await tx`update lots set sort_order = ${index + 1} where id = ${lot.id}`;
        }
        return {};
      }

      case "lot.start": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "queued") throw new HttpError(409, "Only perks that haven't been auctioned yet can be started");
        const [active] = await tx<{ title: string }[]>`select title from lots where status in ('live', 'paused')`;
        if (active) throw new HttpError(409, `"${active.title}" is still running. Close it first.`);
        if (app.phase !== "auction") await setPhase(tx, app, "auction");
        await tx`
          update lots set status = 'live', ends_at = clock_timestamp() + make_interval(secs => duration_s)
          where id = ${action.id}`;
        await tx`update app_state set board_scene = 'lot' where id = 1`;
        return {};
      }

      case "lot.pause": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "live") throw new HttpError(409, "This perk isn't running");
        await tx`
          update lots set status = 'paused', ends_at = null,
            paused_ms_left = greatest(0, (extract(epoch from (ends_at - clock_timestamp())) * 1000)::int)
          where id = ${action.id}`;
        return {};
      }

      case "lot.resume": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "paused") throw new HttpError(409, "This perk isn't paused");
        // Never resume into a near-instant close; give the room a few seconds.
        await tx`
          update lots set status = 'live', paused_ms_left = null,
            ends_at = clock_timestamp() + make_interval(secs => greatest(coalesce(paused_ms_left, 0), 5000) / 1000.0)
          where id = ${action.id}`;
        return {};
      }

      case "lot.addTime": {
        const lot = await lockLot(tx, action.id);
        if (lot.status === "live") {
          await tx`update lots set ends_at = ends_at + make_interval(secs => ${action.seconds}) where id = ${action.id}`;
        } else if (lot.status === "paused") {
          await tx`update lots set paused_ms_left = paused_ms_left + ${action.seconds * 1000} where id = ${action.id}`;
        } else {
          throw new HttpError(409, "This perk isn't running");
        }
        return {};
      }

      case "lot.close": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "live" && lot.status !== "paused") throw new HttpError(409, "This perk isn't running");
        await tx`select settle_lots(${action.id})`;
        return {};
      }

      case "lot.undo": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "live" && lot.status !== "paused") {
          throw new HttpError(409, "Bids can only be undone while the perk is running. Use Re-auction instead.");
        }
        const [undone] = await tx<{ id: number }[]>`
          update bids set voided = true
          where id = (select id from bids where lot_id = ${action.id} and not voided order by id desc limit 1)
          returning id`;
        if (!undone) throw new HttpError(409, "There are no bids to undo");
        return {};
      }

      case "lot.reopen": {
        const lot = await lockLot(tx, action.id);
        if (lot.status !== "sold" && lot.status !== "unsold") throw new HttpError(409, "Only finished perks can be re-auctioned");
        await tx`update bids set voided = true where lot_id = ${action.id}`;
        await tx`
          update lots set status = 'queued', ends_at = null, paused_ms_left = null,
            winner_team_id = null, price = null, closed_at = null
          where id = ${action.id}`;
        await bumpPeople(tx);
        return {};
      }

      case "reset": {
        await tx`delete from bids`;
        await tx`
          update lots set status = 'queued', ends_at = null, paused_ms_left = null,
            winner_team_id = null, price = null, closed_at = null`;
        if (action.scope === "teams" || action.scope === "everything") {
          await tx`delete from teams`;
          await tx`update app_state set phase = 'checkin', board_scene = 'checkin', reveal_count = 0 where id = 1`;
        }
        if (action.scope === "everything") {
          await tx`delete from participants`;
          await tx`update app_state set checkin_open = true, board_message = '' where id = 1`;
        }
        if (action.scope === "auction" && (app.phase === "auction" || app.phase === "results")) {
          await tx`update app_state set phase = 'teams', board_scene = 'reveal' where id = 1`;
        }
        await bumpPeople(tx);
        return {};
      }
    }
  });
}
