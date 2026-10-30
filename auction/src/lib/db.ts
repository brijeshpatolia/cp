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
// with single statements, even many at once. Other databases use one URL for both.
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

// Reuse one pool per server instance (and across dev hot reloads).
const globalForDb = globalThis as unknown as { auctionSql?: Pool };

export function db(): Pool {
  globalForDb.auctionSql ??= connect(databaseUrl(), { max: 5, idle_timeout: 20 });
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

// Throws the pool away: its connections close at once, failing whatever was waiting on
// them, and the next db() opens a new one. postgres.js has no query timeout, so this is
// the way out when the database stops answering, e.g. on a socket that died while Vercel
// had the function paused.
export function resetDb() {
  const old = globalForDb.auctionSql;
  globalForDb.auctionSql = undefined;
  old?.end({ timeout: 0 }).catch(() => {});
}

// A transaction is milliseconds of work; one still going after this long is on a
// connection that stopped answering.
const TRANSACTION_TIMEOUT_MS = 10_000;

// Runs `fn` in a transaction on a connection of its own, closed straight after. On
// Supabase it is a session-mode connection (see transactionUrl), and each open one
// holds one of the project's ~15 pooled database connections. A pool of them didn't
// work: Vercel pauses idle functions with their connections still open, and those stay
// taken. If they're all taken anyway, the transaction uses the transaction-mode pooler,
// which copes with one transaction at a time. (Not db().begin(): max_pipeline 0 stops
// it reserving its connection, porsager/postgres#1189.)
export async function transaction<T>(fn: (tx: postgres.Sql) => Promise<T>): Promise<T> {
  try {
    return await transactionOn(transactionUrl(), fn);
  } catch (err) {
    // The pooler refuses the connection before anything runs, so trying again is safe.
    const sessionsFull = err instanceof Error && err.message.includes("EMAXCONNSESSION");
    if (!sessionsFull || transactionUrl() === databaseUrl()) throw err;
    return transactionOn(databaseUrl(), fn);
  }
}

async function transactionOn<T>(url: string | undefined, fn: (tx: postgres.Sql) => Promise<T>): Promise<T> {
  const sql = connect(url, { max: 1, idle_timeout: 10 });
  let committed = false;
  try {
    const run = async () => {
      await sql`begin`; // fine without reserving: this connection is the pool's only one
      const result = await fn(sql);
      await sql`commit`;
      return result;
    };
    const result = await withTimeout(run(), TRANSACTION_TIMEOUT_MS);
    committed = true;
    return result;
  } finally {
    // Closing the connection rolls back anything that didn't commit.
    await sql.end({ timeout: committed ? 1 : 0 });
  }
}
