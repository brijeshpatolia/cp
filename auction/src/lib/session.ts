import { createHash, createHmac, randomBytes, timingSafeEqual } from "node:crypto";
import type { NextRequest } from "next/server";

export const PARTICIPANT_COOKIE = "auc_p";
export const PADDLE_COOKIE = "auc_paddle";
export const ADMIN_COOKIE = "auc_admin";

const ADMIN_SESSION_MS = 12 * 60 * 60 * 1000;

export const newToken = () => randomBytes(24).toString("base64url");
export const hashToken = (token: string) => createHash("sha256").update(token).digest("hex");

export function cookieOptions(req: NextRequest, maxAgeSeconds: number) {
  return {
    httpOnly: true,
    sameSite: "lax" as const,
    secure: req.nextUrl.protocol === "https:",
    path: "/",
    maxAge: maxAgeSeconds,
  };
}

function adminPassword(): string {
  const password = process.env.ADMIN_PASSWORD;
  if (!password) throw new Error("ADMIN_PASSWORD is not set");
  return password;
}

// Falls back to a secret derived from the admin password, so a deploy with only
// ADMIN_PASSWORD still works (changing the password then logs everyone out).
function sessionSecret(): string {
  return process.env.SESSION_SECRET || `derived:${hashToken(`auction-session:${adminPassword()}`)}`;
}

function safeEqual(a: string, b: string) {
  const ha = createHash("sha256").update(a).digest();
  const hb = createHash("sha256").update(b).digest();
  return timingSafeEqual(ha, hb);
}

export function checkAdminPassword(candidate: string): boolean {
  return safeEqual(candidate, adminPassword());
}

const sign = (payload: string) => createHmac("sha256", sessionSecret()).update(payload).digest("base64url");

export function createAdminSession(): { value: string; maxAge: number } {
  const expires = Date.now() + ADMIN_SESSION_MS;
  return { value: `${expires}.${sign(String(expires))}`, maxAge: ADMIN_SESSION_MS / 1000 };
}

export function isAdmin(req: NextRequest): boolean {
  const value = req.cookies.get(ADMIN_COOKIE)?.value;
  if (!value) return false;
  const [expires, signature] = value.split(".");
  if (!expires || !signature || Number(expires) < Date.now()) return false;
  return safeEqual(signature, sign(expires));
}
