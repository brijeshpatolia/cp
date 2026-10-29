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

function connect() {
  const url = databaseUrl();
  if (!url) throw new Error("DATABASE_URL (or POSTGRES_URL) is not set");
  return postgres(url, {
    // Transaction-mode poolers (Supabase port 6543, Neon) don't support prepared statements.
    prepare: false,
    max: 5,
    idle_timeout: 20,
    connect_timeout: 10,
    ssl: isLocal(url) ? false : "require",
    onnotice: () => {},
  });
}

type Pool = ReturnType<typeof connect>;

// Anything that can run a query: the pool or a transaction inside `db().begin()`.
export type Sql = postgres.ISql;

// Reuse one pool per server instance (and across dev hot reloads).
const globalForDb = globalThis as unknown as { auctionSql?: Pool };

export function db(): Pool {
  globalForDb.auctionSql ??= connect();
  return globalForDb.auctionSql;
}
