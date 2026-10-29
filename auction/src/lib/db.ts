import postgres from "postgres";

// Provider-specific query params (e.g. Supabase's `supa=`) would be sent to Postgres
// as unknown settings and rejected, so only sslmode is kept.
function cleanUrl(raw: string | undefined): string | undefined {
  if (!raw) return undefined;
  const url = new URL(raw);
  const sslmode = url.searchParams.get("sslmode");
  url.search = "";
  if (sslmode) url.searchParams.set("sslmode", sslmode);
  return url.toString();
}

// The app's (pooled) connection: DATABASE_URL, or POSTGRES_URL as set by Vercel's
// Supabase integration. Neon's integration sets DATABASE_URL.
export function databaseUrl(): string | undefined {
  return cleanUrl(process.env.DATABASE_URL || process.env.POSTGRES_URL);
}

// Migrations prefer the integration's non-pooled (direct or session-mode) connection
// from the same provider, which is the safest place to run DDL.
export function migrationUrl(): string | undefined {
  const env = process.env;
  const direct = env.MIGRATION_DATABASE_URL || (env.DATABASE_URL ? env.DATABASE_URL_UNPOOLED : env.POSTGRES_URL_NON_POOLING);
  return cleanUrl(direct) ?? databaseUrl();
}

export function isLocal(url: string) {
  const host = new URL(url).hostname;
  return host === "localhost" || host === "127.0.0.1";
}

// postgres.js's max_pipeline option: real, though missing from its types.
// tests/pooler.db.test.ts checks that it does its job.
const noPipelining = { max_pipeline: 0 };

function connect() {
  const url = databaseUrl();
  if (!url) throw new Error("DATABASE_URL (or POSTGRES_URL) is not set");
  return postgres(url, {
    // Transaction-mode poolers (Supabase port 6543, Neon) don't support prepared statements,
    prepare: false,
    // nor, in Supabase's case, a query sent on a connection that still owes an earlier
    // reply: the pooler then stops answering that connection, or hands it another query's
    // rows (supabase/supavisor#1239). postgres.js sends queries that way whenever more are
    // waiting than it has connections, unless max_pipeline is 0. That setting also stops
    // sql.begin() from reserving its connection, so transactions use transaction() below.
    ...noPipelining,
    max: 5,
    idle_timeout: 20,
    connect_timeout: 10,
    ssl: isLocal(url) ? false : "require",
    onnotice: () => {},
  });
}

type Pool = ReturnType<typeof connect>;

// Anything that can run a query: the pool or a transaction from `transaction()`.
export type Sql = postgres.ISql;

// Reuse one pool per server instance (and across dev hot reloads).
const globalForDb = globalThis as unknown as { auctionSql?: Pool };

export function db(): Pool {
  globalForDb.auctionSql ??= connect();
  return globalForDb.auctionSql;
}

// Settles like `work`, or rejects with a TimeoutError once `ms` have passed.
export class TimeoutError extends Error {}
export async function withTimeout<T>(work: Promise<T>, ms: number): Promise<T> {
  let timer: ReturnType<typeof setTimeout> | undefined;
  try {
    return await Promise.race([
      work,
      new Promise<never>((_, reject) => {
        timer = setTimeout(() => reject(new TimeoutError(`No answer within ${ms / 1000} s`)), ms);
      }),
    ]);
  } finally {
    clearTimeout(timer);
  }
}

// Throws a pool away: its connections close at once, failing whatever was waiting on
// them, and the next db() opens a new one. postgres.js has no query timeout, so this is
// the way out when the database stops answering, e.g. on a socket that died while Vercel
// had the function paused. Defaults to the current pool.
export function resetDb(pool = globalForDb.auctionSql) {
  if (pool === globalForDb.auctionSql) globalForDb.auctionSql = undefined;
  pool?.end({ timeout: 0 }).catch(() => {});
}

// Runs `fn` in a transaction on a connection reserved for it (instead of db().begin(),
// which max_pipeline 0 breaks: porsager/postgres#1189).
export async function transaction<T>(fn: (tx: postgres.ReservedSql) => Promise<T>): Promise<T> {
  const pool = db();
  const tx = await pool.reserve();
  let result: T;
  try {
    await tx`begin`;
    result = await fn(tx);
    await tx`commit`;
  } catch (err) {
    // A connection that can't roll back promptly is broken (a query sent on a closed
    // reserved connection never settles): drop its pool rather than reuse it.
    const rolledBack = await withTimeout(tx`rollback`, 2000).then(
      () => true,
      () => false,
    );
    if (rolledBack) tx.release();
    else resetDb(pool);
    throw err;
  }
  tx.release();
  return result;
}
