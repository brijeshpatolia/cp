// Applies db/schema.sql (idempotent). Runs before `next build`, so every Vercel
// deploy brings the database up to date. Skips quietly when no database is configured.
import { readFileSync } from "node:fs";
import { join } from "node:path";
import postgres from "postgres";
import { isLocal, migrationUrl } from "../src/lib/db";

async function main() {
  const url = migrationUrl();
  if (!url) {
    console.warn("migrate: DATABASE_URL / POSTGRES_URL not set, skipping database migration");
    return;
  }
  const sql = postgres(url, { prepare: false, max: 1, ssl: isLocal(url) ? false : "require", onnotice: () => {} });
  try {
    await sql.unsafe(readFileSync(join(__dirname, "..", "db", "schema.sql"), "utf8"));
    console.log("migrate: schema is up to date");
  } finally {
    await sql.end();
  }
}

main().catch((err) => {
  console.error("migrate: failed", err);
  process.exit(1);
});
