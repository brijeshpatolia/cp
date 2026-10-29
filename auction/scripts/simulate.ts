// Load + correctness simulation against a running deployment.
//
//   ADMIN_PASSWORD=... npm run simulate -- --url https://your-app.vercel.app --yes
//
// It WIPES the event (reset everything), checks in N fake people, makes teams,
// runs one perk with every leader bidding as fast as the rules allow while the
// other phones poll like real ones, then checks the results and resets again
// (pass --keep to leave the data for a look in /admin and /board).
import { parseArgs } from "node:util";
import { LEVELS } from "../src/lib/levels";
import type { AdminOverview, MeState, PublicState } from "../src/lib/types";

const { values: args } = parseArgs({
  options: {
    url: { type: "string", default: "http://localhost:3000" },
    people: { type: "string", default: "80" },
    teams: { type: "string", default: "10" },
    seconds: { type: "string", default: "25" },
    yes: { type: "boolean", default: false },
    keep: { type: "boolean", default: false },
  },
});

const BASE = args.url!.replace(/\/$/, "");
const PEOPLE = Number(args.people);
const TEAMS = Number(args.teams);
const SECONDS = Number(args.seconds);
const PASSWORD = process.env.ADMIN_PASSWORD;

interface Stat {
  ms: number[];
  errors: number;
}
const stats: Record<string, Stat> = {};

// A tiny cookie-keeping client, one per simulated phone.
class Phone {
  cookies = new Map<string, string>();

  async call<T>(label: string, path: string, body?: unknown, method?: string): Promise<{ status: number; data: T }> {
    const started = performance.now();
    const res = await fetch(BASE + path, {
      method: method ?? (body === undefined ? "GET" : "POST"),
      headers: {
        ...(body === undefined ? {} : { "Content-Type": "application/json" }),
        Cookie: [...this.cookies].map(([k, v]) => `${k}=${v}`).join("; "),
      },
      body: body === undefined ? undefined : JSON.stringify(body),
      redirect: "manual",
    });
    for (const c of res.headers.getSetCookie()) {
      const [pair] = c.split(";");
      const i = pair.indexOf("=");
      this.cookies.set(pair.slice(0, i), pair.slice(i + 1));
    }
    const data = (await res.json().catch(() => ({}))) as T;
    const stat = (stats[label] ??= { ms: [], errors: 0 });
    stat.ms.push(performance.now() - started);
    if (res.status >= 500) stat.errors++;
    return { status: res.status, data };
  }
}

const admin = new Phone();
async function adminAction(action: Record<string, unknown>) {
  const res = await admin.call<{ error?: string; overview: AdminOverview }>("admin", "/api/admin", action);
  if (res.status !== 200) throw new Error(`${action.action}: ${res.data.error}`);
  return res.data;
}

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const pick = <T>(items: readonly T[]) => items[Math.floor(Math.random() * items.length)];

function percentile(values: number[], p: number) {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.min(sorted.length - 1, Math.floor((p / 100) * sorted.length))] ?? 0;
}

async function main() {
  if (!PASSWORD) throw new Error("Set ADMIN_PASSWORD");
  if (!args.yes) throw new Error(`This wipes all event data at ${BASE}. Re-run with --yes if that's OK.`);

  const login = await admin.call<{ error?: string }>("admin", "/api/admin/session", { password: PASSWORD });
  if (login.status !== 200) throw new Error(`Admin login failed: ${login.data.error}`);
  await adminAction({ action: "reset", scope: "everything" });
  await adminAction({ action: "checkin.set", open: true });

  console.log(`Checking in ${PEOPLE} phones at once…`);
  const weights = [35, 30, 20, 10, 5];
  const phones = await Promise.all(
    Array.from({ length: PEOPLE }, async (_, i) => {
      const phone = new Phone();
      let r = Math.random() * 100;
      let level = 0;
      while (r >= weights[level]) r -= weights[level++];
      const res = await phone.call<MeState>("register", "/api/register", {
        name: `Sim ${String(i + 1).padStart(2, "0")}`,
        department: pick(["M&A", "ECM", "DCM", "Coverage", "Risk", "Operations"]),
        level: LEVELS[level],
      });
      if (res.status !== 200) throw new Error(`Check-in failed: ${JSON.stringify(res.data)}`);
      return { phone, id: res.data.participant!.id };
    }),
  );

  await adminAction({ action: "teams.generate", teamCount: TEAMS });
  await adminAction({ action: "reveal.all" });
  const { id: lotId } = (await adminAction({
    action: "lot.create",
    title: "Simulation perk",
    emoji: "🤖",
    startPrice: 10,
    step: 10,
    durationS: SECONDS + 5,
  })) as unknown as { id: number };
  const { overview } = await adminAction({ action: "lot.start", id: lotId });

  const leaders = overview.teams.map((t) => ({ team: t, phone: phones.find((p) => p.id === t.leaderId)!.phone }));
  const others = phones.filter((p) => !overview.teams.some((t) => t.leaderId === p.id));
  console.log(`${overview.teams.length} teams; ${leaders.length} leaders bidding, ${others.length} phones watching, for ${SECONDS}s…`);

  const until = Date.now() + SECONDS * 1000;
  let placed = 0;
  let rejected = 0;

  const watchers = others.map(async ({ phone }) => {
    await sleep(Math.random() * 3000);
    while (Date.now() < until) {
      await phone.call("state (cached)", "/api/state?cdn=1");
      await sleep(3000);
    }
  });

  const bidders = leaders.map(async ({ team, phone }) => {
    while (Date.now() < until) {
      const { data: s } = await phone.call<PublicState>("state (leader)", "/api/state");
      const lot = s.lot;
      const coins = s.teams.find((t) => t.id === team.id)?.coinsLeft ?? 0;
      if (lot?.status === "live" && lot.top?.teamId !== team.id && lot.minNext <= coins) {
        const amount = Math.min(coins, lot.minNext + lot.step * Math.floor(Math.random() * 3));
        const res = await phone.call("bid", "/api/bid", { lotId: lot.id, amount });
        if (res.status === 200) placed++;
        else rejected++;
      }
      await sleep(300 + Math.random() * 700);
    }
  });

  await Promise.all([...watchers, ...bidders]);
  const { overview: final } = await adminAction({ action: "lot.close", id: lotId });

  // Every accepted bid beat the previous one by a full step, and no team outbid itself.
  const bids = [...final.bids].filter((b) => !b.voided).reverse();
  const problems: string[] = [];
  for (let i = 1; i < bids.length; i++) {
    if (bids[i].amount < bids[i - 1].amount + 10) problems.push(`bid ${bids[i].id} too small`);
    if (bids[i].teamId === bids[i - 1].teamId) problems.push(`team ${bids[i].teamId} outbid itself`);
  }
  const lot = final.lots.find((l) => l.id === lotId)!;
  const top = bids.at(-1);
  if (top && (lot.winnerTeamId !== top.teamId || lot.price !== top.amount)) problems.push("winner is not the top bid");
  for (const t of final.teams) if (t.coinsLeft < 0) problems.push(`${t.name} overspent`);

  console.log(`\nBids accepted: ${placed}, rejected by the rules (outbid in the meantime etc.): ${rejected}`);
  if (top) console.log(`Sold to ${final.teams.find((t) => t.id === lot.winnerTeamId)?.name} for ${lot.price}`);
  console.log("\nRequest            count   p50 ms   p95 ms   5xx");
  for (const [label, s] of Object.entries(stats)) {
    console.log(
      `${label.padEnd(18)} ${String(s.ms.length).padStart(5)} ${percentile(s.ms, 50).toFixed(0).padStart(8)} ${percentile(s.ms, 95).toFixed(0).padStart(8)} ${String(s.errors).padStart(5)}`,
    );
  }
  const serverErrors = Object.values(stats).reduce((n, s) => n + s.errors, 0);

  if (!args.keep) await adminAction({ action: "reset", scope: "everything" });
  if (problems.length || serverErrors) {
    console.error(`\nFAILED: ${[...problems, serverErrors ? `${serverErrors} server errors` : ""].filter(Boolean).join("; ")}`);
    process.exit(1);
  }
  console.log(`\nPASSED${args.keep ? " (data kept: see /admin and /board)" : " (event data reset)"}`);
}

main().catch((err) => {
  console.error(err instanceof Error ? err.message : err);
  process.exit(1);
});
