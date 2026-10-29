import { connection } from "next/server";
import { databaseUrl, db } from "@/lib/db";
import { handle, json } from "@/lib/http";

// Deployment check: open /api/health after deploying. Says what's missing, if anything.
export const GET = handle(async () => {
  await connection();
  const checks = {
    databaseUrl: Boolean(databaseUrl()),
    databaseReachable: false,
    tablesCreated: false,
    adminPassword: Boolean(process.env.ADMIN_PASSWORD),
    sessionSecret: Boolean(process.env.SESSION_SECRET),
  };
  let problem: string | null = null;
  let dbLatencyMs: number | null = null;

  if (!checks.databaseUrl) {
    problem = "No database: connect Supabase in the Vercel project's Storage tab (or set DATABASE_URL), then redeploy.";
  } else {
    try {
      const started = performance.now();
      await db()`select 1`;
      dbLatencyMs = Math.round(performance.now() - started);
      checks.databaseReachable = true;
      const [row] = await db()<{ ok: boolean }[]>`select to_regclass('public.app_state') is not null as ok`;
      checks.tablesCreated = row.ok;
      if (!row.ok) problem = "The database has no tables yet: redeploy, and the build will create them.";
    } catch (err) {
      problem = `Can't reach the database: ${err instanceof Error ? err.message : String(err)}`;
    }
  }
  if (!problem && !checks.adminPassword) problem = "ADMIN_PASSWORD is not set, so nobody can log in to /admin.";

  const ok = checks.databaseReachable && checks.tablesCreated && checks.adminPassword;
  return json(
    {
      ok,
      problem,
      checks,
      dbLatencyMs, // a few ms when the app and database share a region; 100+ means they don't
      region: process.env.VERCEL_REGION ?? null,
    },
    { status: ok ? 200 : 503 },
  );
});
