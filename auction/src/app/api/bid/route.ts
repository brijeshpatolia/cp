import type { NextRequest } from "next/server";
import { handle, json, readJson } from "@/lib/http";
import { placeBid } from "@/lib/participant";
import { PADDLE_COOKIE, PARTICIPANT_COOKIE } from "@/lib/session";
import { getPublicState } from "@/lib/state";

export const POST = handle(async (req: NextRequest) => {
  const result = await placeBid(
    { participant: req.cookies.get(PARTICIPANT_COOKIE)?.value, paddle: req.cookies.get(PADDLE_COOKIE)?.value },
    await readJson(req),
  );
  // Send back fresh state so the leader's phone updates without waiting for the next poll.
  return json({ ...result, state: await getPublicState() });
});
