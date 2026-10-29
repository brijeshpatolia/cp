import { unstable_rethrow } from "next/navigation";
import { NextResponse } from "next/server";
import { ZodError } from "zod";
import { resetDb, TimeoutError, withTimeout } from "./db";

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
      console.error(err);
      return json({ error: "Something went wrong, please try again" }, { status: 500 });
    }
  };
}

export async function readJson(req: Request): Promise<unknown> {
  try {
    return await req.json();
  } catch {
    throw new HttpError(400, "Invalid JSON body");
  }
}
