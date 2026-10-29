import postgres from "postgres";

// Accepts DATABASE_URL, or POSTGRES_URL as set by the Vercel ↔ Supabase/Neon
// integrations. Provider-specific query params (e.g. Supabase's `supa=`) would be
// sent to Postgres as unknown settings and rejected, so only sslmode is kept.
export function databaseUrl(): string | undefined {
  const raw = process.env.DATABASE_URL || process.env.POSTGRES_URL;
  if (!raw) return undefined;
  const url = new URL(raw);
  const sslmode = url.searchParams.get("sslmode");
  url.search = "";
  if (sslmode) url.searchParams.set("sslmode", sslmode);
  return url.toString();
}

function isLocal(url: string) {
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
