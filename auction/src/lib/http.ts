import { unstable_rethrow } from "next/navigation";
import { NextResponse, type NextRequest } from "next/server";
import postgres from "postgres";
import { ZodError } from "zod";
import { resetDb, TimeoutError, withTimeout } from "./db";
import { isAdmin } from "./session";

export class HttpError extends Error {
  constructor(
    public status: number,
    message: string,
    public extra: Record<string, unknown> = {},
  ) {
    super(message);
  }
}

export function json(data: unknown, init: ResponseInit = {}) {
  const headers = new Headers(init.headers);
  if (!headers.has("Cache-Control")) headers.set("Cache-Control", "no-store");
  return NextResponse.json(data, { ...init, headers });
}

// When a request last got a successful answer. If none has since a timed-out request
// began, nothing is getting through: the database pool is stuck, not just busy, and is
// replaced so that its dead connections can't hold up every request after them.
let lastAnswered = 0;

export function replacePoolIfStuck(since: number) {
  const stuck = lastAnswered <= since;
  if (stuck) resetDb();
  return stuck;
}

// Wraps a route handler so thrown HttpErrors and validation errors become JSON responses,
// and so a request the database doesn't answer fails after `timeoutMs` instead of hanging
// until Vercel's 300 s limit.
export function handle<A extends unknown[]>(fn: (...args: A) => Promise<Response>, timeoutMs = 10_000) {
  return async (...args: A): Promise<Response> => {
    const started = performance.now();
    try {
      const res = await withTimeout(fn(...args), timeoutMs);
      if (res.status < 400) lastAnswered = performance.now();
      return res;
    } catch (err) {
      unstable_rethrow(err); // let Next.js's own control-flow errors (e.g. "stop prerendering") through
      if (err instanceof TimeoutError) {
        const replaced = replacePoolIfStuck(started);
        console.error(replaced ? `${err.message}, nor to any other request: replacing the database pool` : err.message);
        return json({ error: "The server is busy, please try again" }, { status: 503 });
      }
      if (err instanceof HttpError) return json({ error: err.message, ...err.extra }, { status: err.status });
      if (err instanceof ZodError) {
        const issue = err.issues[0];
        const where = issue?.path.length ? `${issue.path.join(".")}: ` : "";
        return json({ error: `${where}${issue?.message ?? "Invalid input"}` }, { status: 400 });
      }
      // A reference to something that is gone, or a clash with a change made a moment
      // earlier, e.g. by another organizer: usually fixed by looking again.
      if (err instanceof postgres.PostgresError && (err.code === "23503" || err.code === "23505")) {
        return json({ error: "That has just changed: refresh and try again" }, { status: 409 });
      }
      console.error(err);
      return json({ error: "Something went wrong, please try again", ...detailForAdmins(args[0], err) }, { status: 500 });
    }
  };
}

// An organizer sees what actually went wrong (e.g. a database error), to tell the cause
// on the day; phones only get the generic message.
function detailForAdmins(req: unknown, err: unknown) {
  if (!(req instanceof Request) || !("cookies" in req) || !isAdmin(req as NextRequest)) return {};
  const e = err as { message?: string; code?: string };
  return { detail: `${e?.message ?? String(err)}${e?.code ? ` (${e.code})` : ""}` };
}

export async function readJson(req: Request): Promise<unknown> {
  try {
    return await req.json();
  } catch {
    throw new HttpError(400, "Invalid JSON body");
  }
}
