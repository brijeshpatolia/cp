"use client";

import { useState, type FormEvent } from "react";
import { fmt } from "@/lib/client";
import { Button, Card, inputClass, Label, TeamDot } from "../ui";
import type { TabProps } from "./AdminApp";
import { EditableText } from "./PeopleTab";

const IDEAS = [
  { emoji: "🏠", title: "Unlimited work from home", description: "For one month" },
  { emoji: "🪔", title: "Half day before Diwali", description: "Head home early for the festivities" },
  { emoji: "🍬", title: "Mithai box for your team", description: "Kaju katli, laddoos, the works" },
  { emoji: "🏖️", title: "Leave early on Fridays", description: "For a month of Fridays" },
  { emoji: "🍕", title: "Pick the team lunch", description: "Your choice, team pays" },
  { emoji: "☕", title: "Boss brings the coffee", description: "Every morning for a week" },
  { emoji: "🙅", title: "Skip one meeting", description: "No questions asked" },
  { emoji: "🌴", title: "An extra day off", description: "Use it this quarter" },
  { emoji: "👕", title: "Casual dress week", description: "Hoodies welcome" },
  { emoji: "🎧", title: "Music control", description: "Office playlist for a week" },
];

export function PerksTab({ o, act }: TabProps) {
  const s = o.settings;
  const [emoji, setEmoji] = useState("🎁");
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [startPrice, setStartPrice] = useState(s.defaultStartPrice);
  const [step, setStep] = useState(s.defaultStep);
  const [durationS, setDurationS] = useState(s.defaultDuration);
  const [mystery, setMystery] = useState(false);
  const active = o.lots.find((l) => l.status === "live" || l.status === "paused");
  const team = (id: number | null) => o.teams.find((t) => t.id === id);

  async function add(e: FormEvent) {
    e.preventDefault();
    const res = await act({ action: "lot.create", emoji, title, description, startPrice, step, durationS, mystery });
    if (res) {
      setTitle("");
      setDescription("");
      setEmoji("🎁");
      setMystery(false);
    }
  }

  return (
    <div className="flex flex-col gap-4">
      <Card>
        <p className="mb-3 font-bold">Add a perk</p>
        <form onSubmit={add} className="grid gap-3 sm:grid-cols-6">
          <div className="sm:col-span-1">
            <Label htmlFor="emoji">Emoji</Label>
            <input id="emoji" className={inputClass} value={emoji} onChange={(e) => setEmoji(e.target.value)} maxLength={16} required />
          </div>
          <div className="sm:col-span-5">
            <Label htmlFor="title">Perk</Label>
            <input id="title" className={inputClass} value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Unlimited work from home" maxLength={80} required />
          </div>
          <div className="sm:col-span-6">
            <Label htmlFor="description">Details (optional)</Label>
            <input id="description" className={inputClass} value={description} onChange={(e) => setDescription(e.target.value)} placeholder="For one month" maxLength={300} />
          </div>
          <div className="sm:col-span-2">
            <Label htmlFor="start">Opening bid</Label>
            <input id="start" type="number" min={1} className={inputClass} value={startPrice} onChange={(e) => setStartPrice(Number(e.target.value))} />
          </div>
          <div className="sm:col-span-2">
            <Label htmlFor="step">Min raise</Label>
            <input id="step" type="number" min={1} className={inputClass} value={step} onChange={(e) => setStep(Number(e.target.value))} />
          </div>
          <div className="sm:col-span-2">
            <Label htmlFor="duration">Timer (seconds)</Label>
            <input id="duration" type="number" min={5} max={3600} className={inputClass} value={durationS} onChange={(e) => setDurationS(Number(e.target.value))} />
          </div>
          <label className="flex items-center gap-2 text-sm sm:col-span-4">
            <input type="checkbox" checked={mystery} onChange={(e) => setMystery(e.target.checked)} />
            Mystery perk: hidden from everyone until it&apos;s sold
          </label>
          <Button type="submit" className="sm:col-span-2">
            Add perk
          </Button>
        </form>
        <div className="mt-3 flex flex-wrap gap-2">
          <span className="text-sm text-muted">Ideas:</span>
          {IDEAS.filter((idea) => !o.lots.some((l) => l.title === idea.title)).map((idea) => (
            <button
              key={idea.title}
              className="rounded-full border border-line px-3 py-1 text-sm hover:border-accent"
              onClick={() => {
                setEmoji(idea.emoji);
                setTitle(idea.title);
                setDescription(idea.description);
              }}
            >
              {idea.emoji} {idea.title}
            </button>
          ))}
        </div>
      </Card>

      <Card>
        <p className="mb-2 font-bold">Running order</p>
        {o.lots.length === 0 && <p className="py-4 text-center text-muted">No perks yet.</p>}
        <ol className="flex flex-col">
          {o.lots.map((l, i) => {
            const winner = team(l.winnerTeamId);
            const queued = l.status === "queued";
            return (
              <li key={l.id} className="flex flex-wrap items-center gap-2 border-t border-line py-2">
                <span className="flex flex-col">
                  <button className="px-1 text-muted disabled:opacity-20" disabled={i === 0} onClick={() => act({ action: "lot.move", id: l.id, direction: "up" })} aria-label="Move up">
                    ▲
                  </button>
                  <button className="px-1 text-muted disabled:opacity-20" disabled={i === o.lots.length - 1} onClick={() => act({ action: "lot.move", id: l.id, direction: "down" })} aria-label="Move down">
                    ▼
                  </button>
                </span>
                <span className="w-10">
                  <EditableText value={l.emoji} className="text-2xl" onSave={(v) => act({ action: "lot.update", id: l.id, emoji: v })} />
                </span>
                <div className="min-w-48 flex-1">
                  <EditableText value={l.title} className="font-bold" onSave={(v) => act({ action: "lot.update", id: l.id, title: v })} />
                  <EditableText
                    value={l.description}
                    allowEmpty
                    className="text-sm text-muted"
                    onSave={(v) => act({ action: "lot.update", id: l.id, description: v })}
                  />
                </div>
                <span className="text-xs text-muted">
                  opens {fmt(l.startPrice)} · +{fmt(l.step)} · {l.durationS}s{l.mystery && " · mystery"}
                </span>
                <span className="rounded-full bg-surface-2 px-2 py-0.5 text-xs font-bold uppercase">{l.status}</span>
                {winner && (
                  <span className="flex items-center gap-1 text-sm font-semibold">
                    <TeamDot color={winner.color} /> {winner.name} · {fmt(l.price ?? 0)}
                  </span>
                )}
                {queued && (
                  <Button size="sm" disabled={Boolean(active) || o.teams.length === 0} onClick={() => act({ action: "lot.start", id: l.id })}>
                    Start
                  </Button>
                )}
                {(l.status === "sold" || l.status === "unsold") && (
                  <Button size="sm" variant="ghost" onClick={() => act({ action: "lot.reopen", id: l.id }, "Cancel this result and put the perk back in the queue?")}>
                    Re-auction
                  </Button>
                )}
                {l.status !== "live" && l.status !== "paused" && (
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={() =>
                      act(
                        { action: "lot.delete", id: l.id },
                        l.status === "sold" ? `Delete "${l.title}"? ${winner?.name ?? "The winner"} gets its ${fmt(l.price ?? 0)} back.` : `Delete "${l.title}"?`,
                      )
                    }
                  >
                    Delete
                  </Button>
                )}
              </li>
            );
          })}
        </ol>
      </Card>
    </div>
  );
}
