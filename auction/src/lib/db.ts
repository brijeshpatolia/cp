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

function isSupabasePooler(url: URL) {
  return url.hostname.endsWith(".pooler.supabase.com");
}

// "session" or "transaction" for Supabase's pooler, else null (for /api/health).
export function poolerMode(raw: string): "session" | "transaction" | null {
  const url = new URL(raw);
  if (!isSupabasePooler(url)) return null;
  return url.port === "6543" ? "transaction" : "session";
}

// The app's (pooled) connection: DATABASE_URL, or POSTGRES_URL as set by Vercel's
// Supabase integration. Neon's integration sets DATABASE_URL.
export function databaseUrl(): string | undefined {
  return cleanUrl(process.env.DATABASE_URL || process.env.POSTGRES_URL);
}

// Transactions take Supabase's pooler in session mode instead: port 5432 on the same
// host, which passes each connection straight through to a database connection. In
// transaction mode (6543) the pooler loses or mixes up replies when a few transactions
// run at once (3 to 5 simultaneous check-ins did it in production), though it copes
// with single statements. Other databases use the same URL for both.
export function transactionUrl(): string | undefined {
  const raw = databaseUrl();
  if (!raw) return undefined;
  const url = new URL(raw);
  if (isSupabasePooler(url) && url.port === "6543") url.port = "5432";
  return url.toString();
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

function connect(url: string | undefined, { max, idle_timeout }: { max: number; idle_timeout: number }) {
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
    max,
    idle_timeout,
    connect_timeout: 10,
    ssl: isLocal(url) ? false : "require",
    onnotice: () => {},
  });
}

type Pool = ReturnType<typeof connect>;

// Anything that can run a query: the pool or a transaction from `transaction()`.
export type Sql = postgres.ISql;

// Reuse the pools per server instance (and across dev hot reloads).
const globalForDb = globalThis as unknown as { auctionSql?: Pool; auctionTxSql?: Pool };

export function db(): Pool {
  globalForDb.auctionSql ??= connect(databaseUrl(), { max: 5, idle_timeout: 20 });
  return globalForDb.auctionSql;
}

// Connections for transaction(). In session mode each one holds one of the project's
// pooled database connections (about 15 on Supabase's free plan, shared by every
// function instance) while it is open, so there are only two, closed soon after use.
// Transactions all lock app_state first, so more wouldn't run any faster.
function transactionPool(): Pool {
  if (transactionUrl() === databaseUrl()) return db();
  globalForDb.auctionTxSql ??= connect(transactionUrl(), { max: 2, idle_timeout: 10 });
  return globalForDb.auctionTxSql;
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

// Throws pools away: their connections close at once, failing whatever was waiting on
// them, and the next query opens new ones. postgres.js has no query timeout, so this is
// the way out when the database stops answering, e.g. on a socket that died while Vercel
// had the function paused. Defaults to all of the instance's pools.
export function resetDb(pool?: Pool) {
  for (const old of pool ? [pool] : [globalForDb.auctionSql, globalForDb.auctionTxSql]) {
    if (!old) continue;
    if (globalForDb.auctionSql === old) globalForDb.auctionSql = undefined;
    if (globalForDb.auctionTxSql === old) globalForDb.auctionTxSql = undefined;
    old.end({ timeout: 0 }).catch(() => {});
  }
}

// A transaction is milliseconds of work; one still going after this long is on a
// connection that stopped answering.
const TRANSACTION_TIMEOUT_MS = 10_000;

// Runs `fn` in a transaction on a connection reserved for it (instead of db().begin(),
// which max_pipeline 0 breaks: porsager/postgres#1189).
export async function transaction<T>(fn: (tx: postgres.ReservedSql) => Promise<T>): Promise<T> {
  const pool = transactionPool();
  const tx = await pool.reserve();
  const work = (async () => {
    await tx`begin`;
    const result = await fn(tx);
    await tx`commit`;
    return result;
  })();
  try {
    const result = await withTimeout(work, TRANSACTION_TIMEOUT_MS);
    tx.release();
    return result;
  } catch (err) {
    // A stuck connection, or one that can't roll back promptly (a query sent on a closed
    // reserved connection never settles), goes with its pool rather than being reused.
    // Closing it makes the database roll the transaction back.
    const rolledBack =
      !(err instanceof TimeoutError) &&
      (await withTimeout(tx`rollback`, 2000).then(
        () => true,
        () => false,
      ));
    if (rolledBack) tx.release();
    else resetDb(pool);
    throw err;
  }
}
