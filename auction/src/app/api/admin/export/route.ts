import type { NextRequest } from "next/server";
import { handle, HttpError } from "@/lib/http";
import { isAdmin } from "@/lib/session";
import { getAdminOverview } from "@/lib/state";

const cell = (value: unknown) => {
  const text = value === null || value === undefined ? "" : String(value);
  return /[",\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
};
const csv = (rows: unknown[][]) => rows.map((r) => r.map(cell).join(",")).join("\n") + "\n";

export const GET = handle(async (req: NextRequest) => {
  if (!isAdmin(req)) throw new HttpError(401, "Please log in again");
  const type = req.nextUrl.searchParams.get("type") === "results" ? "results" : "people";
  const o = await getAdminOverview();
  const teamName = (id: number | null) => o.teams.find((t) => t.id === id)?.name ?? "";

  let body: string;
  if (type === "people") {
    body = csv([
      ["Name", "Department", "Position", "Team", "Table", "Leader"],
      ...o.participants.map((p) => {
        const team = o.teams.find((t) => t.id === p.teamId);
        return [p.name, p.department, p.level, team?.name ?? "", team?.tableNo ?? "", team?.leaderId === p.id ? "yes" : ""];
      }),
    ]);
  } else {
    body = csv([
      ["Perk", "Status", "Winner", `Price (${o.settings.currency})`],
      ...o.lots.map((l) => [l.title, l.status, teamName(l.winnerTeamId), l.price ?? ""]),
      [],
      ["Team", "Budget", "Spent", "Left", "Perks won"],
      ...o.teams.map((t) => [
        t.name,
        t.coins,
        t.coins - t.coinsLeft,
        t.coinsLeft,
        o.lots.filter((l) => l.status === "sold" && l.winnerTeamId === t.id).map((l) => l.title).join("; "),
      ]),
    ]);
  }
  return new Response(body, {
    headers: {
      "Content-Type": "text/csv; charset=utf-8",
      "Content-Disposition": `attachment; filename="auction-${type}.csv"`,
      "Cache-Control": "no-store",
    },
  });
});
