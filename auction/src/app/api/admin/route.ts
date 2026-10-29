import type { NextRequest } from "next/server";
import { runAdminAction } from "@/lib/admin";
import { handle, HttpError, json, readJson } from "@/lib/http";
import { isAdmin } from "@/lib/session";
import { getAdminOverview } from "@/lib/state";

function requireAdmin(req: NextRequest) {
  if (!isAdmin(req)) throw new HttpError(401, "Please log in again");
}

export const GET = handle(async (req: NextRequest) => {
  requireAdmin(req);
  return json(await getAdminOverview());
});

// Making the teams takes a few dozen statements: slow if the database is far away.
export const POST = handle(async (req: NextRequest) => {
  requireAdmin(req);
  const result = await runAdminAction(await readJson(req));
  return json({ ...result, overview: await getAdminOverview() });
}, 30_000);
