"use client";

import { useState, type FormEvent } from "react";
import { api } from "@/lib/client";
import { LEADER_RULES, type LeaderRule, type Settings } from "@/lib/settings";
import { Button, Card, inputClass, Label } from "../ui";
import type { TabProps } from "./AdminApp";

const RULE_LABELS: Record<LeaderRule, string> = {
  random: "Random member",
  junior: "Most junior (the analyst spends the MD's money!)",
  senior: "Most senior",
};

export function SettingsTab({ o, act, onLoggedOut }: TabProps & { onLoggedOut: () => void }) {
  const [draft, setDraft] = useState<Settings>(o.settings);
  const [departments, setDepartments] = useState(o.settings.departments.join("\n"));
  const set = <K extends keyof Settings>(key: K, value: Settings[K]) => setDraft((d) => ({ ...d, [key]: value }));
  const num = (key: keyof Settings) => (e: React.ChangeEvent<HTMLInputElement>) => set(key, Number(e.target.value) as never);

  async function save(e: FormEvent) {
    e.preventDefault();
    const list = departments
      .split("\n")
      .map((d) => d.trim())
      .filter(Boolean);
    await act({ action: "settings.update", settings: { ...draft, departments: list } });
  }

  return (
    <div className="grid gap-4 lg:grid-cols-2">
      <Card>
        <form onSubmit={save} className="grid gap-3 sm:grid-cols-2">
          <p className="font-bold sm:col-span-2">Event settings</p>
          <div className="sm:col-span-2">
            <Label htmlFor="eventName">Event name</Label>
            <input id="eventName" className={inputClass} value={draft.eventName} onChange={(e) => set("eventName", e.target.value)} maxLength={60} />
          </div>
          <div>
            <Label htmlFor="currency">Currency name</Label>
            <input id="currency" className={inputClass} value={draft.currency} onChange={(e) => set("currency", e.target.value)} maxLength={20} />
          </div>
          <div>
            <Label htmlFor="coins">Starting {draft.currency} per team</Label>
            <input id="coins" type="number" min={1} className={inputClass} value={draft.startingCoins} onChange={num("startingCoins")} />
          </div>
          <div>
            <Label htmlFor="teamCount">Default number of teams</Label>
            <input id="teamCount" type="number" min={2} max={12} className={inputClass} value={draft.teamCount} onChange={num("teamCount")} />
          </div>
          <div>
            <Label htmlFor="leaderRule">Leader is</Label>
            <select id="leaderRule" className={inputClass} value={draft.leaderRule} onChange={(e) => set("leaderRule", e.target.value as LeaderRule)}>
              {LEADER_RULES.map((r) => (
                <option key={r} value={r}>
                  {RULE_LABELS[r]}
                </option>
              ))}
            </select>
          </div>
          <div>
            <Label htmlFor="antiSnipe">Anti-snipe (seconds)</Label>
            <input id="antiSnipe" type="number" min={0} max={60} className={inputClass} value={draft.antiSnipeSeconds} onChange={num("antiSnipeSeconds")} />
          </div>
          <div>
            <Label htmlFor="maxPerks">Max perks per team (0 = no limit)</Label>
            <input id="maxPerks" type="number" min={0} max={50} className={inputClass} value={draft.maxPerksPerTeam} onChange={num("maxPerksPerTeam")} />
          </div>
          <div>
            <Label htmlFor="defStart">Default opening bid</Label>
            <input id="defStart" type="number" min={1} className={inputClass} value={draft.defaultStartPrice} onChange={num("defaultStartPrice")} />
          </div>
          <div>
            <Label htmlFor="defStep">Default min raise</Label>
            <input id="defStep" type="number" min={1} className={inputClass} value={draft.defaultStep} onChange={num("defaultStep")} />
          </div>
          <div>
            <Label htmlFor="defDuration">Default timer (seconds)</Label>
            <input id="defDuration" type="number" min={5} max={3600} className={inputClass} value={draft.defaultDuration} onChange={num("defaultDuration")} />
          </div>
          <div className="sm:col-span-2">
            <Label htmlFor="departments">Departments for the check-in form, one per line (leave empty for free text)</Label>
            <textarea id="departments" rows={4} className={inputClass} value={departments} onChange={(e) => setDepartments(e.target.value)} />
          </div>
          <p className="text-xs text-muted sm:col-span-2">
            A bid in the last {draft.antiSnipeSeconds} s resets the clock to {draft.antiSnipeSeconds} s. Changing starting {draft.currency} only
            affects teams made after saving; use the button on the right to update existing teams.
          </p>
          <Button type="submit" className="sm:col-span-2">
            Save settings
          </Button>
        </form>
      </Card>

      <div className="flex flex-col gap-4">
        <Card>
          <p className="font-bold">Coins</p>
          <p className="text-sm text-muted">Give every existing team exactly {draft.startingCoins} {draft.currency}.</p>
          <Button
            className="mt-3"
            variant="secondary"
            disabled={o.teams.length === 0}
            onClick={() =>
              act(
                { action: "teams.setCoins", coins: draft.startingCoins },
                `Set every team's budget to ${draft.startingCoins} ${draft.currency}? Perks already won still count against it.`,
              )
            }
          >
            Apply to all teams
          </Button>
        </Card>

        <Card>
          <p className="font-bold">Export</p>
          <div className="mt-3 flex flex-wrap gap-2">
            <a className="rounded-xl border border-line px-4 py-2.5 font-semibold" href="/api/admin/export?type=people">
              People & teams (CSV)
            </a>
            <a className="rounded-xl border border-line px-4 py-2.5 font-semibold" href="/api/admin/export?type=results">
              Auction results (CSV)
            </a>
          </div>
        </Card>

        <Card className="border-bad">
          <p className="font-bold text-bad">Reset</p>
          <p className="text-sm text-muted">For rehearsals and after the event. These can&apos;t be undone.</p>
          <div className="mt-3 flex flex-col gap-2">
            <Button variant="secondary" onClick={() => act({ action: "reset", scope: "auction" }, "Clear all bids and results? Teams and people stay.")}>
              Reset the auction (keep teams)
            </Button>
            <Button variant="secondary" onClick={() => act({ action: "reset", scope: "teams" }, "Delete all teams and results? People stay checked in.")}>
              Reset teams and auction (keep people)
            </Button>
            <Button
              variant="danger"
              onClick={() => act({ action: "reset", scope: "everything" }, "Delete EVERYONE, all teams and all results? Perks and settings stay.")}
            >
              Reset everything
            </Button>
          </div>
        </Card>

        <Button
          variant="ghost"
          onClick={async () => {
            await api("/api/admin/session", undefined, "DELETE").catch(() => {});
            onLoggedOut();
          }}
        >
          Log out
        </Button>
      </div>
    </div>
  );
}
