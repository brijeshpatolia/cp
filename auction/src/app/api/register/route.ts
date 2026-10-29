import type { NextRequest } from "next/server";
import { handle, json, readJson } from "@/lib/http";
import { register } from "@/lib/participant";
import { cookieOptions, PADDLE_COOKIE, PARTICIPANT_COOKIE } from "@/lib/session";
import { getMeState } from "@/lib/state";

const WEEK = 7 * 24 * 60 * 60;

export const POST = handle(async (req: NextRequest) => {
  const existing = req.cookies.get(PARTICIPANT_COOKIE)?.value;
  const { token } = await register(existing, await readJson(req));
  const me = await getMeState({ participant: token ?? existing, paddle: req.cookies.get(PADDLE_COOKIE)?.value });
  const res = json(me);
  if (token) res.cookies.set(PARTICIPANT_COOKIE, token, cookieOptions(req, WEEK));
  return res;
});
