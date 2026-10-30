// Phone-side actions: checking in and bidding.
import { z } from "zod";
import { bumpPeople, ensureLeader, placeLateArrival } from "./admin";
import { db, transaction } from "./db";
import { HttpError } from "./http";
import { LEVELS } from "./levels";
import { hashToken, newToken } from "./session";
import { loadApp, resolveDevice, type DeviceTokens } from "./state";

export const registerSchema = z.object({
  name: z.string().trim().min(1, "Please enter your name").max(40),
  department: z.string().trim().max(40).default(""),
  level: z.enum(LEVELS, { message: "Please pick your position" }),
});

type CheckIn = { ok: true; added: boolean } | { ok: false; error: "closed" | "late" };

// Checks a phone in, or updates the details of a phone that already checked in.
// Returns a new device token when one was created (the caller sets the cookie).
export async function register(existingToken: string | undefined, input: unknown): Promise<{ token: string | null }> {
  const data = registerSchema.parse(input);
  const token = newToken();
  // One statement rather than a transaction, as everyone checks in at once (see
  // check_in in db/schema.sql).
  const [{ r }] = await db()<{ r: CheckIn }[]>`
    select check_in(${existingToken ? hashToken(existingToken) : null}, ${hashToken(token)},
                    ${data.name}, ${data.department}, ${data.level}) as r`;
  if (r.ok) return { token: r.added ? token : null };
  if (r.error === "closed") throw new HttpError(403, "Check-in is closed. Please find an organizer.");
  return checkInLate(token, data);
}

// Someone checking in after the teams were made joins the team that keeps the balance best.
function checkInLate(token: string, data: z.infer<typeof registerSchema>): Promise<{ token: string }> {
  return transaction(async (tx) => {
    const app = await loadApp(tx, { lock: true });
    if (!app.checkinOpen) throw new HttpError(403, "Check-in is closed. Please find an organizer.");

    const [person] = await tx<{ id: number }[]>`
      insert into participants (name, department, level, token_hash)
      values (${data.name}, ${data.department}, ${data.level}, ${hashToken(token)})
      returning id`;
    const teamId = await placeLateArrival(tx, { id: person.id, level: data.level, department: data.department });
    if (teamId) {
      await tx`update participants set team_id = ${teamId} where id = ${person.id}`;
      await ensureLeader(tx, teamId, app.settings.leaderRule);
      await bumpPeople(tx);
    }
    return { token };
  });
}

export const bidSchema = z.object({
  lotId: z.number().int().positive(),
  amount: z.number().int().positive("Enter a whole number"),
});

type BidResult =
  | { ok: true; amount: number }
  | { ok: false; error: string; min?: number; left?: number };

// Minimum gap between two bids from the same team on the same lot (absorbs double taps).
const MIN_GAP_MS = 400;

export async function placeBid(tokens: DeviceTokens, input: unknown) {
  const { lotId, amount } = bidSchema.parse(input);
  const sql = db();
  const [device, app] = await Promise.all([resolveDevice(sql, tokens), loadApp(sql)]);
  if (!device.bidTeamId) throw new HttpError(403, "Only your team's leader can bid");

  const [{ r }] = await sql<{ r: BidResult }[]>`
    select place_bid(${lotId}, ${device.bidTeamId}, ${device.participant?.id ?? null}, ${amount},
                     ${app.settings.antiSnipeSeconds}, ${app.settings.maxPerksPerTeam}, ${MIN_GAP_MS}) as r`;
  if (r.ok) return r;

  const currency = app.settings.currency;
  switch (r.error) {
    case "too_low":
      throw new HttpError(409, `Too low: the minimum bid is now ${r.min} ${currency}`, { min: r.min });
    case "no_coins":
      throw new HttpError(409, `Not enough ${currency}: your team has ${r.left} left`, { left: r.left });
    case "already_top":
      throw new HttpError(409, "You already have the top bid");
    case "closed":
      throw new HttpError(409, "Bidding on this perk has closed");
    case "max_perks":
      throw new HttpError(409, "Your team already has the maximum number of perks");
    case "slow_down":
      throw new HttpError(429, "One bid at a time, please");
    default:
      throw new HttpError(409, "That bid couldn't be placed");
  }
}
