// The app's database settings against a pooler that behaves like Supabase's
// (tests/wireProxy.ts): no query may be sent on a connection that still owes a reply,
// and a database that stops answering must cost a quick error, not a hung app.
// Uses TEST_DATABASE_URL, which it wipes; skipped when unset.
import { readFileSync } from "node:fs";
import { join } from "node:path";
import postgres from "postgres";
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { startWireProxy, type WireProxy } from "./wireProxy";

const url = process.env.TEST_DATABASE_URL;
process.env.ADMIN_PASSWORD ??= "test";

describe.skipIf(!url)("database connections through a Supabase-like pooler", () => {
  let proxy: WireProxy;

  beforeAll(async () => {
    const raw = postgres(url!, { onnotice: () => {} });
    await raw.unsafe("drop schema public cascade; create schema public;");
    await raw.unsafe(readFileSync(join(__dirname, "..", "db", "schema.sql"), "utf8"));
    await raw.end();
    proxy = await startWireProxy(url!, { supavisor: true });
    process.env.DATABASE_URL = proxy.url;
  });

  afterAll(async () => {
    (await import("@/lib/db")).resetDb();
    await proxy.close();
  });

  it("never sends a query on a connection that is still waiting for a reply", async () => {
    const { withTimeout } = await import("@/lib/db");
    const { runAdminAction: admin } = await import("@/lib/admin");
    const { register, placeBid } = await import("@/lib/participant");
    const state = await import("@/lib/state");
    const levels = ["Analyst", "Associate", "VP", "Director", "MD"] as const;
    const checkIn = (name: string, i: number) =>
      register(undefined, { name, department: "Ops", level: levels[i % levels.length] }).then((r) => r.token!);

    async function eventInMiniature() {
      const tokens = await Promise.all(Array.from({ length: 40 }, (_, i) => checkIn(`Person ${i}`, i)));
      await admin({ action: "teams.generate", teamCount: 5 });
      await admin({ action: "reveal.all" });
      const lot = (await admin({ action: "lot.create", title: "Unlimited WFH", startPrice: 100, step: 10, durationS: 60 })) as { id: number };
      await admin({ action: "lot.start", id: lot.id });

      // Every phone bids (only leaders may) and polls, the board and admin poll, and late
      // arrivals check in, all at once: far more queries than the pool has connections.
      await Promise.all([
        ...tokens.map((t) => placeBid({ participant: t }, { lotId: lot.id, amount: 100 }).catch(() => null)),
        ...tokens.map((t) => state.getMeState({ participant: t })),
        ...Array.from({ length: 20 }, () => state.getPublicState()),
        ...Array.from({ length: 5 }, () => state.getAdminOverview()),
        ...Array.from({ length: 5 }, (_, i) => checkIn(`Late ${i}`, i)),
      ]);
    }

    const outcome = await withTimeout(eventInMiniature(), 10_000).then(
      () => "finished",
      (err) => String(err),
    );
    expect(proxy.stats).toMatchObject({ pipelined: 0, stalled: 0 });
    expect(outcome).toBe("finished");
    expect((await state.getPublicState()).lot?.top?.amount).toBe(100);
  });

  it("catches a client that does pipeline, which then stalls as it would on Supabase", async () => {
    const pipelined = proxy.stats.pipelined;
    const client = postgres(proxy.url, { max: 1, onnotice: () => {} }); // postgres.js defaults
    const burst = Promise.all([client`select 1`, client`select 2`, client`select 3`, client`select 4`]);
    const outcome = await Promise.race([
      burst.then(
        () => "finished",
        () => "failed",
      ),
      new Promise((resolve) => setTimeout(resolve, 2000, "stuck")),
    ]);
    await client.end({ timeout: 0 });
    expect(outcome).toBe("stuck");
    expect(proxy.stats.pipelined).toBeGreaterThan(pipelined);
  });

  it("answers a slow request with a 503 but keeps a pool that is only busy", async () => {
    const { db } = await import("@/lib/db");
    const { handle } = await import("@/lib/http");
    const slow = handle(async () => Response.json((await db()`select pg_sleep(1)`)[0]), 300);
    const quick = handle(async () => Response.json((await db()`select 1 as ok`)[0]), 300);
    const pool = db();
    const slowAnswer = slow();
    await new Promise((resolve) => setTimeout(resolve, 100));
    expect((await quick()).status).toBe(200);
    expect((await slowAnswer).status).toBe(503);
    expect(db()).toBe(pool);
  });

  it("answers quickly with a 503 when the database stops answering, then recovers", async () => {
    const { db, resetDb } = await import("@/lib/db");
    const { handle } = await import("@/lib/http");
    resetDb(); // start from a fresh pool, whatever the tests above left behind
    const ping = handle(async () => Response.json((await db()`select 1 as ok`)[0]), 500);
    expect((await ping()).status).toBe(200);

    proxy.stallAll(); // e.g. sockets that died while Vercel had the function paused
    const started = performance.now();
    expect((await ping()).status).toBe(503);
    expect(performance.now() - started).toBeLessThan(2000);
    expect((await ping()).status).toBe(200);
  });
});
