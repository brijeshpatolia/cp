"use client";

import { useState } from "react";
import { fmt, formatClock, useTicker } from "@/lib/client";
import type { BoardScene, Phase } from "@/lib/types";
import { Button, Card, inputClass, TeamDot } from "../ui";
import type { TabProps } from "./AdminApp";

const PHASE_STEPS: [Phase, string, string][] = [
  ["checkin", "1. Check-in", "QR on the big screen, people join"],
  ["teams", "2. Teams", "Reveal teams one by one"],
  ["auction", "3. Auction", "Run the perks"],
  ["results", "4. Results", "Final standings"],
];

const SCENES: [BoardScene, string][] = [
  ["checkin", "Check-in QR"],
  ["reveal", "Team reveal"],
  ["lot", "Live perk"],
  ["leaderboard", "Standings"],
  ["message", "Message"],
];

export function LiveTab({ o, act, serverNow }: TabProps) {
  useTicker(250);
  const [message, setMessage] = useState(o.board.message);
  const phaseIndex = PHASE_STEPS.findIndex(([p]) => p === o.phase);
  const team = (id: number | null) => o.teams.find((t) => t.id === id);
  const current = o.lots.find((l) => l.id === o.currentLotId) ?? null;
  const active = current && (current.status === "live" || current.status === "paused") ? current : null;
  const next = o.lots.find((l) => l.status === "queued");
  const left = active?.status === "live" && active.endsAt ? active.endsAt - serverNow() : (active?.pausedMsLeft ?? 0);
  const top = team(current?.top?.teamId ?? null);
  const winner = team(current?.winnerTeamId ?? null);

  return (
    <div className="grid gap-4 lg:grid-cols-[1.4fr_1fr]">
      <div className="flex flex-col gap-4">
        <Card>
          <p className="mb-3 font-bold">Event phase</p>
          <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
            {PHASE_STEPS.map(([phase, label, hint], i) => (
              <button
                key={phase}
                onClick={() =>
                  act({ action: "phase.set", phase }, i < phaseIndex ? `Go back to "${label}"? Phones and the big screen will switch too.` : undefined)
                }
                className={`rounded-xl border p-3 text-left ${phase === o.phase ? "border-accent bg-accent text-accent-ink" : "border-line"}`}
              >
                <p className="font-bold">{label}</p>
                <p className="text-xs opacity-80">{hint}</p>
              </button>
            ))}
          </div>
          <label className="mt-3 flex items-center gap-2 text-sm font-medium">
            <input type="checkbox" checked={o.checkinOpen} onChange={(e) => act({ action: "checkin.set", open: e.target.checked })} />
            Check-in open ({o.participants.length} checked in)
          </label>
        </Card>

        {(o.phase === "teams" || (o.phase === "checkin" && o.teams.length > 0)) && (
          <Card>
            <p className="font-bold">Team reveal</p>
            <p className="text-sm text-muted">
              {o.phase === "checkin" ? 0 : o.revealCount} of {o.teams.length} teams revealed. Phones show each person&apos;s team as
              it&apos;s revealed.
            </p>
            <div className="mt-3 flex flex-wrap gap-2">
              <Button size="lg" onClick={() => act({ action: "reveal.next" })} disabled={o.phase !== "checkin" && o.revealCount >= o.teams.length}>
                Reveal next team
              </Button>
              <Button variant="secondary" onClick={() => act({ action: "reveal.all" })}>
                Reveal all
              </Button>
              <Button variant="ghost" onClick={() => act({ action: "reveal.reset" }, "Hide all teams again and restart the reveal?")}>
                Start over
              </Button>
            </div>
          </Card>
        )}

        <Card>
          <div className="flex items-center justify-between">
            <p className="font-bold">Auction</p>
            {next && !active && (
              <Button onClick={() => act({ action: "lot.start", id: next.id })} disabled={o.teams.length === 0}>
                Start next: {next.emoji} {next.title}
              </Button>
            )}
          </div>
          {o.teams.length === 0 && <p className="mt-2 text-sm text-muted">Generate teams (Teams tab) before the auction.</p>}
          {!current && o.teams.length > 0 && (
            <p className="mt-2 text-sm text-muted">{next ? "Ready when you are." : "Add perks in the Perks tab."}</p>
          )}
          {current && (
            <div className="mt-3 rounded-xl border border-line p-3">
              <div className="flex items-start justify-between gap-3">
                <p className="text-lg font-extrabold">
                  {current.emoji} {current.title}
                  {current.mystery && <span className="ml-2 text-xs font-semibold text-muted">(mystery)</span>}
                </p>
                <span className="rounded-full bg-surface-2 px-2 py-0.5 text-xs font-bold uppercase">{current.status}</span>
              </div>
              <div className="mt-2 flex flex-wrap items-end justify-between gap-3">
                <div>
                  <p className="text-sm text-muted">
                    {current.status === "sold" ? "Sold for" : current.top ? "Top bid" : "Opening bid"}
                  </p>
                  <p className="tabular text-3xl font-extrabold">{fmt(current.price ?? current.top?.amount ?? current.startPrice)}</p>
                  {(winner ?? top) && (
                    <p className="flex items-center gap-1.5 font-semibold">
                      <TeamDot color={(winner ?? top)!.color} /> {(winner ?? top)!.name}
                    </p>
                  )}
                </div>
                {active && (
                  <p className={`tabular text-4xl font-extrabold ${left < 10_000 ? "text-bad" : ""}`}>
                    {active.status === "paused" ? `Paused · ${formatClock(left)}` : formatClock(left)}
                  </p>
                )}
              </div>
              <div className="mt-3 flex flex-wrap gap-2">
                {active?.status === "live" && (
                  <Button variant="secondary" onClick={() => act({ action: "lot.pause", id: active.id })}>
                    Pause
                  </Button>
                )}
                {active?.status === "paused" && <Button onClick={() => act({ action: "lot.resume", id: active.id })}>Resume</Button>}
                {active && (
                  <>
                    <Button variant="secondary" onClick={() => act({ action: "lot.addTime", id: active.id, seconds: 15 })}>
                      +15 s
                    </Button>
                    <Button
                      variant="secondary"
                      disabled={!active.top}
                      onClick={() => act({ action: "lot.undo", id: active.id }, "Undo the latest bid?")}
                    >
                      ↩ Undo last bid
                    </Button>
                    <Button
                      variant="danger"
                      onClick={() =>
                        act({ action: "lot.close", id: active.id }, active.top ? "Bang the gavel now and sell to the top bid?" : "Close this perk with no bids?")
                      }
                    >
                      🔨 {active.top ? "Sell now" : "Close"}
                    </Button>
                  </>
                )}
                {!active && (current.status === "sold" || current.status === "unsold") && (
                  <Button
                    variant="ghost"
                    onClick={() => act({ action: "lot.reopen", id: current.id }, "Cancel this result and put the perk back in the queue?")}
                  >
                    Re-auction
                  </Button>
                )}
              </div>
            </div>
          )}
          {o.bids.length > 0 && (
            <ul className="mt-3 max-h-64 overflow-y-auto text-sm">
              {o.bids.map((b) => (
                <li key={b.id} className={`flex items-center gap-2 border-t border-line py-1.5 ${b.voided ? "text-muted line-through" : ""}`}>
                  <span className="tabular w-[4.5rem] text-muted">
                    {new Date(b.at).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false })}
                  </span>
                  <TeamDot color={team(b.teamId)?.color ?? "#999"} />
                  <span className="flex-1 truncate">
                    {team(b.teamId)?.name}
                    {b.by && <span className="text-muted"> · {b.by}</span>}
                  </span>
                  <span className="tabular font-bold">{fmt(b.amount)}</span>
                </li>
              ))}
            </ul>
          )}
        </Card>
      </div>

      <div className="flex flex-col gap-4">
        <Card>
          <p className="mb-3 font-bold">Big screen shows</p>
          <div className="flex flex-wrap gap-2">
            {SCENES.map(([scene, label]) => (
              <Button
                key={scene}
                size="sm"
                variant={o.board.scene === scene ? "primary" : "secondary"}
                onClick={() => act({ action: "board.set", scene, message })}
              >
                {label}
              </Button>
            ))}
          </div>
          <form
            className="mt-3 flex gap-2"
            onSubmit={(e) => {
              e.preventDefault();
              act({ action: "board.set", scene: "message", message });
            }}
          >
            <input className={inputClass} value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Message, e.g. Break: back in 10" maxLength={200} />
            <Button type="submit" variant="secondary">
              Show
            </Button>
          </form>
        </Card>

        <Card>
          <p className="mb-2 font-bold">Teams</p>
          {o.teams.length === 0 ? (
            <p className="text-sm text-muted">No teams yet.</p>
          ) : (
            <table className="w-full text-sm">
              <thead className="text-left text-muted">
                <tr>
                  <th className="py-1 font-medium">Team</th>
                  <th className="py-1 font-medium">Leader</th>
                  <th className="py-1 text-right font-medium">Perks</th>
                  <th className="py-1 text-right font-medium">{o.settings.currency}</th>
                </tr>
              </thead>
              <tbody>
                {o.teams.map((t) => (
                  <tr key={t.id} className="border-t border-line">
                    <td className="py-1.5">
                      <span className="flex items-center gap-1.5 font-semibold">
                        <TeamDot color={t.color} /> {t.name}
                      </span>
                    </td>
                    <td className="max-w-28 truncate py-1.5">{o.participants.find((p) => p.id === t.leaderId)?.name ?? "—"}</td>
                    <td className="tabular py-1.5 text-right">{o.lots.filter((l) => l.status === "sold" && l.winnerTeamId === t.id).length}</td>
                    <td className="tabular py-1.5 text-right font-bold">{fmt(t.coinsLeft)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </Card>
      </div>
    </div>
  );
}
