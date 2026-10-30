import { connection } from "next/server";
import { databaseUrl, db, poolerMode, TimeoutError, transaction, transactionUrl, withTimeout } from "@/lib/db";
import { handle, json, replacePoolIfStuck } from "@/lib/http";

// The Vercel region next to each cloud region a Supabase (or Neon) database can be in.
const NEAREST_VERCEL_REGION: Record<string, string> = {
  "ap-south-1": "bom1",
  "ap-southeast-1": "sin1",
  "ap-southeast-2": "syd1",
  "ap-northeast-1": "hnd1",
  "ap-northeast-2": "icn1",
  "eu-central-1": "fra1",
  "eu-west-1": "dub1",
  "eu-west-2": "lhr1",
  "eu-west-3": "cdg1",
  "eu-north-1": "arn1",
  "us-east-1": "iad1",
  "us-east-2": "cle1",
  "us-west-1": "sfo1",
  "us-west-2": "pdx1",
  "ca-central-1": "yul1",
  "sa-east-1": "gru1",
};

// e.g. aws-0-ap-south-1.pooler.supabase.com → ap-south-1
function databaseRegion(url: string | undefined) {
  if (!url) return null;
  return new URL(url).hostname.match(/(?:^|[.-])((?:us|eu|ap|sa|ca|me|af)-[a-z]+-\d)(?=\.)/)?.[1] ?? null;
}

const message = (err: unknown) => (err instanceof Error ? err.message : String(err));

// Deployment check: open /api/health after deploying. Says what's missing, if anything.
export const GET = handle(async () => {
  await connection();
  const started = performance.now();
  const url = databaseUrl();
  const checks = {
    databaseUrl: Boolean(url),
    databaseReachable: false,
    tablesCreated: false,
    transactionsWork: false,
    adminPassword: Boolean(process.env.ADMIN_PASSWORD),
    sessionSecret: Boolean(process.env.SESSION_SECRET),
  };
  let problem: string | null = null;
  let dbLatencyMs: number | null = null;

  if (!url) {
    problem = "No database: connect Supabase in the Vercel project's Storage tab (or set DATABASE_URL), then redeploy.";
  } else {
    // Three checks of at most 3 s each, inside the request's 10 s limit.
    try {
      const pinged = performance.now();
      await withTimeout(db()`select 1`, 3000);
      dbLatencyMs = Math.round(performance.now() - pinged);
      checks.databaseReachable = true;
      const [row] = await withTimeout(db()<{ ok: boolean }[]>`select to_regclass('public.app_state') is not null as ok`, 3000);
      checks.tablesCreated = row.ok;
      if (!row.ok) problem = "The database has no tables yet: redeploy, and the build will create them.";
    } catch (err) {
      if (err instanceof TimeoutError) replacePoolIfStuck(started);
      problem = `Can't reach the database: ${message(err)}`;
    }
    if (checks.databaseReachable) {
      try {
        await withTimeout(transaction((tx) => tx`select 1`), 3000);
        checks.transactionsWork = true;
      } catch (err) {
        if (err instanceof TimeoutError) replacePoolIfStuck(started);
        problem ??= `Transactions (check-ins, admin actions) fail: ${message(err)}`;
      }
    }
  }
  if (!problem && !checks.adminPassword) problem = "ADMIN_PASSWORD is not set, so nobody can log in to /admin.";

  const region = process.env.VERCEL_REGION ?? null;
  const dbRegion = databaseRegion(url);
  const nearest = dbRegion ? NEAREST_VERCEL_REGION[dbRegion] : undefined;
  const hint =
    region && nearest && region !== nearest
      ? `The app runs in ${region} but the database is in ${dbRegion}, so every request waits on long round trips. ` +
        `In the Vercel project, set Settings → Functions → Function Region to ${nearest}, then redeploy.`
      : null;

  const ok = checks.databaseReachable && checks.tablesCreated && checks.transactionsWork && checks.adminPassword;
  return json(
    {
      ok,
      problem,
      hint,
      checks,
      dbLatencyMs, // a few ms when the app and database share a region; 100+ means they don't
      region,
      dbRegion,
      // Supabase's pooler: "transaction" mode for queries, "session" mode for transactions
      dbPooler: url ? { queries: poolerMode(url), transactions: poolerMode(transactionUrl()!) } : null,
    },
    { status: ok ? 200 : 503 },
  );
});
