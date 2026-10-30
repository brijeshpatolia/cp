import { afterEach, describe, expect, it } from "vitest";
import { databaseUrl, migrationUrl, poolerMode, transactionUrl } from "@/lib/db";

const saved = { ...process.env };
afterEach(() => {
  process.env = { ...saved };
});

function setEnv(vars: Record<string, string | undefined>) {
  for (const key of ["DATABASE_URL", "DATABASE_URL_UNPOOLED", "POSTGRES_URL", "POSTGRES_URL_NON_POOLING", "MIGRATION_DATABASE_URL"]) {
    delete process.env[key];
  }
  Object.assign(process.env, vars);
}

describe("database URLs", () => {
  it("queries go through Supabase's pooler in transaction mode, transactions in session mode", () => {
    setEnv({ POSTGRES_URL: "postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require&supa=base-pooler.x" });
    expect(databaseUrl()).toBe("postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require");
    expect(transactionUrl()).toBe("postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require");
    expect([poolerMode(databaseUrl()!), poolerMode(transactionUrl()!)]).toEqual(["transaction", "session"]);
  });

  it("prefers DATABASE_URL, with the same split when it is Supabase's pooler", () => {
    setEnv({
      DATABASE_URL: "postgres://postgres.abc:pw@aws-1-eu-west-1.pooler.supabase.com:6543/postgres",
      POSTGRES_URL: "postgres://other@db.example.com:5432/x",
    });
    expect(transactionUrl()).toBe("postgres://postgres.abc:pw@aws-1-eu-west-1.pooler.supabase.com:5432/postgres");
  });

  it("uses one URL for everything with other databases", () => {
    setEnv({ DATABASE_URL: "postgres://u:p@ep-cool-1234-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require" });
    expect(transactionUrl()).toBe(databaseUrl());
    expect(poolerMode(databaseUrl()!)).toBeNull();
  });

  it("migrates over the integration's non-pooled connection", () => {
    setEnv({
      POSTGRES_URL: "postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:6543/postgres",
      POSTGRES_URL_NON_POOLING: "postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require",
    });
    expect(migrationUrl()).toBe("postgres://postgres.abc:pw@aws-0-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require");
  });
});
