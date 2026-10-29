import { NextResponse, type NextRequest } from "next/server";
import { db } from "@/lib/db";
import { handle } from "@/lib/http";
import { cookieOptions, hashToken, PADDLE_COOKIE } from "@/lib/session";

// Opened by scanning a team's paddle QR: this phone may now bid for that team.
export const GET = handle(async (req: NextRequest, ctx: RouteContext<"/paddle/[token]">) => {
  const { token } = await ctx.params;
  const [paddle] = await db()<{ team_id: number }[]>`select team_id from paddles where token_hash = ${hashToken(token)}`;
  const res = NextResponse.redirect(new URL(paddle ? "/" : "/?paddle=invalid", req.url));
  if (paddle) res.cookies.set(PADDLE_COOKIE, token, cookieOptions(req, 24 * 60 * 60));
  return res;
});
