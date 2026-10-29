import type { NextRequest } from "next/server";
import { z } from "zod";
import { handle, HttpError, json, readJson } from "@/lib/http";
import { ADMIN_COOKIE, checkAdminPassword, cookieOptions, createAdminSession, isAdmin } from "@/lib/session";

export const GET = handle(async (req: NextRequest) => json({ admin: isAdmin(req) }));

export const POST = handle(async (req: NextRequest) => {
  const { password } = z.object({ password: z.string().max(200) }).parse(await readJson(req));
  if (!checkAdminPassword(password)) {
    await new Promise((r) => setTimeout(r, 700)); // slow down guessing
    throw new HttpError(401, "Wrong password");
  }
  const session = createAdminSession();
  const res = json({ admin: true });
  res.cookies.set(ADMIN_COOKIE, session.value, cookieOptions(req, session.maxAge));
  return res;
});

export const DELETE = handle(async (req: NextRequest) => {
  const res = json({ admin: false });
  res.cookies.set(ADMIN_COOKIE, "", cookieOptions(req, 0));
  return res;
});
