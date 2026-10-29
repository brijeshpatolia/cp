import type { NextRequest } from "next/server";
import { handle, json } from "@/lib/http";
import { PADDLE_COOKIE, PARTICIPANT_COOKIE } from "@/lib/session";
import { getMeState } from "@/lib/state";

export const GET = handle(async (req: NextRequest) => {
  const me = await getMeState({
    participant: req.cookies.get(PARTICIPANT_COOKIE)?.value,
    paddle: req.cookies.get(PADDLE_COOKIE)?.value,
  });
  return json(me);
});
