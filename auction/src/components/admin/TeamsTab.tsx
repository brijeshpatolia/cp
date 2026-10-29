"use client";

import { useState } from "react";
import { fmt } from "@/lib/client";
import { LEVELS_SENIOR_FIRST } from "@/lib/levels";
import type { AdminTeam } from "@/lib/types";
import { QrCode } from "../QrCode";
import { Button, Card, LevelBadge } from "../ui";
import type { TabProps } from "./AdminApp";
import { EditableText } from "./PeopleTab";

export function TeamsTab({ o, act }: TabProps) {
  const [count, setCount] = useState(o.settings.teamCount);
  const [paddle, setPaddle] = useState<{ team: AdminTeam; url: string } | null>(null);
  const hasTeams = o.teams.length > 0;
  const perTeam = count > 0 ? (o.participants.length / count).toFixed(1) : "–";

  async function makePaddle(team: AdminTeam) {
    const res = await act({ action: "team.paddle", teamId: team.id });
    if (res?.paddlePath) setPaddle({ team, url: `${window.location.origin}${res.paddlePath}` });
  }

  return (
    <div className="flex flex-col gap-4">
      <Card>
        <p className="font-bold">{hasTeams ? "Reshuffle teams" : "Make teams"}</p>
        <p className="text-sm text-muted">
          Balances positions (MD → Analyst), team sizes and departments. Leaders are picked by the rule in Settings (
          {o.settings.leaderRule}).
        </p>
        <div className="mt-3 flex flex-wrap items-center gap-2">
          <input
            type="number"
            min={2}
            max={12}
            className="w-24 rounded-xl border border-line bg-bg px-3 py-2.5 text-ink outline-none focus:border-accent"
            value={count}
            onChange={(e) => setCount(Number(e.target.value))}
            aria-label="Number of teams"
          />
          <span className="text-sm text-muted">
            teams for {o.participants.length} people (≈{perTeam} each)
          </span>
          <Button
            onClick={() =>
              act(
                { action: "teams.generate", teamCount: count },
                hasTeams ? "Reshuffle everyone into new teams? Names, colours and leaders are reassigned." : undefined,
              )
            }
            disabled={count < 2 || count > 12 || o.participants.length < count}
          >
            {hasTeams ? "Reshuffle" : "Generate teams"}
          </Button>
          {hasTeams && (
            <Button variant="ghost" onClick={() => act({ action: "teams.clear" }, "Delete all teams? People stay checked in.")}>
              Delete teams
            </Button>
          )}
        </div>
      </Card>

      {hasTeams && (
        <Card className="overflow-x-auto">
          <p className="mb-2 font-bold">Balance check</p>
          <table className="w-full min-w-[560px] text-sm">
            <thead className="text-left text-muted">
              <tr>
                <th className="py-1 font-medium">Team</th>
                {LEVELS_SENIOR_FIRST.map((l) => (
                  <th key={l} className="py-1 text-center font-medium">
                    {l}
                  </th>
                ))}
                <th className="py-1 text-center font-medium">Total</th>
                <th className="py-1 text-center font-medium">Depts</th>
              </tr>
            </thead>
            <tbody>
              {o.teams.map((t) => {
                const members = o.participants.filter((p) => p.teamId === t.id);
                return (
                  <tr key={t.id} className="border-t border-line">
                    <td className="py-1.5 font-semibold" style={{ color: t.color }}>
                      {t.name}
                    </td>
                    {LEVELS_SENIOR_FIRST.map((l) => (
                      <td key={l} className="tabular py-1.5 text-center">
                        {members.filter((m) => m.level === l).length || "·"}
                      </td>
                    ))}
                    <td className="tabular py-1.5 text-center font-bold">{members.length}</td>
                    <td className="tabular py-1.5 text-center">
                      {new Set(members.map((m) => m.department.trim().toLowerCase()).filter(Boolean)).size}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </Card>
      )}

      <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        {o.teams.map((t) => {
          const members = o.participants.filter((p) => p.teamId === t.id);
          return (
            <Card key={t.id} className="flex flex-col gap-2">
              <div className="flex items-center gap-2">
                <input
                  type="color"
                  value={t.color}
                  onChange={(e) => act({ action: "team.update", id: t.id, color: e.target.value })}
                  className="h-8 w-8 shrink-0 cursor-pointer rounded border border-line"
                  aria-label="Team colour"
                />
                <EditableText value={t.name} className="text-lg font-extrabold" onSave={(v) => act({ action: "team.update", id: t.id, name: v })} />
              </div>
              <div className="grid grid-cols-2 gap-2 text-sm">
                <label className="flex items-center gap-2">
                  Table
                  <EditableText value={String(t.tableNo)} onSave={(v) => act({ action: "team.update", id: t.id, tableNo: Number(v) })} />
                </label>
                <label className="flex items-center gap-2">
                  {o.settings.currency}
                  <EditableText value={String(t.coins)} onSave={(v) => act({ action: "team.update", id: t.id, coins: Number(v) })} />
                </label>
              </div>
              {t.coinsLeft !== t.coins && (
                <p className="text-xs text-muted">
                  {fmt(t.coinsLeft)} left after {fmt(t.coins - t.coinsLeft)} spent
                </p>
              )}
              <div className="flex items-center gap-2 text-sm">
                <span>👑</span>
                <select
                  className="min-w-0 flex-1 rounded-lg border border-line bg-bg px-2 py-1"
                  value={t.leaderId ?? ""}
                  onChange={(e) => act({ action: "team.setLeader", teamId: t.id, participantId: Number(e.target.value) })}
                >
                  {t.leaderId === null && <option value="">No leader</option>}
                  {members.map((m) => (
                    <option key={m.id} value={m.id}>
                      {m.name} ({m.level})
                    </option>
                  ))}
                </select>
                <Button size="sm" variant="secondary" onClick={() => act({ action: "team.rerollLeader", teamId: t.id })}>
                  🎲 Re-roll
                </Button>
              </div>
              <div className="flex flex-wrap items-center gap-2 text-sm">
                <Button size="sm" variant="secondary" onClick={() => makePaddle(t)}>
                  Paddle QR
                </Button>
                {t.paddles > 0 && (
                  <Button size="sm" variant="ghost" onClick={() => act({ action: "team.revokePaddles", teamId: t.id }, "Stop all extra paddle phones for this team?")}>
                    Revoke {t.paddles} paddle{t.paddles === 1 ? "" : "s"}
                  </Button>
                )}
              </div>
              <ul className="divide-y divide-line text-sm">
                {members.map((m) => (
                  <li key={m.id} className="flex items-center justify-between gap-2 py-1">
                    <span className="truncate">
                      {t.leaderId === m.id && "👑 "}
                      {m.name}
                      {m.department && <span className="text-muted"> · {m.department}</span>}
                    </span>
                    <LevelBadge level={m.level} />
                  </li>
                ))}
              </ul>
            </Card>
          );
        })}
      </div>

      {paddle && (
        <div className="fixed inset-0 z-30 grid place-items-center bg-black/60 p-4" onClick={() => setPaddle(null)}>
          <div className="w-full max-w-sm rounded-2xl bg-surface p-5 text-center" onClick={(e) => e.stopPropagation()}>
            <p className="text-lg font-extrabold">Paddle for {paddle.team.name}</p>
            <p className="mt-1 text-sm text-muted">Scan with the phone that should bid for this team (works for 24 hours).</p>
            <QrCode value={paddle.url} className="mx-auto mt-4 w-64" />
            <p className="mt-3 text-xs break-all text-muted">{paddle.url}</p>
            <Button className="mt-4 w-full" onClick={() => setPaddle(null)}>
              Done
            </Button>
          </div>
        </div>
      )}
    </div>
  );
}
