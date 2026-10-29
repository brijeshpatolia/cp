import type { NextRequest } from "next/server";
import { handle, json } from "@/lib/http";
import { getPublicState } from "@/lib/state";

// Polled by every screen. `?cdn=1` lets Vercel's CDN serve it for 2 s, which is
// what the ~70 non-leader phones use, so they barely touch the database.
export const GET = handle(async (req: NextRequest) => {
  const cdn = req.nextUrl.searchParams.has("cdn");
  const state = await getPublicState();
  return json(state, { headers: { "Cache-Control": cdn ? "public, max-age=0, s-maxage=2" : "no-store" } });
});
