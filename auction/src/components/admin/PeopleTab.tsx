"use client";

import { useRef, useState, type FormEvent } from "react";
import { LEVELS, LEVELS_SENIOR_FIRST, type Level } from "@/lib/levels";
import { Button, Card, inputClass, TeamDot } from "../ui";
import type { TabProps } from "./AdminApp";

export function PeopleTab({ o, act }: TabProps) {
  const [query, setQuery] = useState("");
  const [name, setName] = useState("");
  const [department, setDepartment] = useState("");
  const [level, setLevel] = useState<Level>("Analyst");

  const q = query.trim().toLowerCase();
  const people = o.participants.filter(
    (p) => !q || p.name.toLowerCase().includes(q) || p.department.toLowerCase().includes(q),
  );
  const unassigned = o.participants.filter((p) => !p.teamId).length;

  async function add(e: FormEvent) {
    e.preventDefault();
    const res = await act({ action: "participant.add", name, department, level });
    if (res) {
      setName("");
      setDepartment("");
    }
  }

  return (
    <div className="flex flex-col gap-4">
      <Card>
        <div className="flex flex-wrap gap-2 text-sm">
          <span className="rounded-full bg-ink px-3 py-1 font-bold text-bg">{o.participants.length} people</span>
          {LEVELS_SENIOR_FIRST.map((l) => (
            <span key={l} className="rounded-full bg-surface-2 px-3 py-1 font-semibold">
              {l} {o.participants.filter((p) => p.level === l).length}
            </span>
          ))}
          {o.teams.length > 0 && unassigned > 0 && (
            <span className="rounded-full bg-bad px-3 py-1 font-semibold text-white">{unassigned} without a team</span>
          )}
        </div>
      </Card>

      <Card>
        <p className="mb-2 font-bold">Add someone (no phone, or on their behalf)</p>
        <form onSubmit={add} className="grid gap-2 sm:grid-cols-[1fr_1fr_auto_auto]">
          <input className={inputClass} placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} required maxLength={40} />
          <input className={inputClass} placeholder="Department" value={department} onChange={(e) => setDepartment(e.target.value)} maxLength={40} />
          <select className={inputClass} value={level} onChange={(e) => setLevel(e.target.value as Level)}>
            {LEVELS.map((l) => (
              <option key={l}>{l}</option>
            ))}
          </select>
          <Button type="submit">Add</Button>
        </form>
        {o.teams.length > 0 && <p className="mt-1 text-xs text-muted">Teams exist, so they&apos;ll be placed in the best-balanced team.</p>}
      </Card>

      <Card className="overflow-x-auto">
        <input className={`${inputClass} mb-3`} placeholder="Search name or department" value={query} onChange={(e) => setQuery(e.target.value)} />
        <table className="w-full min-w-[640px] text-sm">
          <thead className="text-left text-muted">
            <tr>
              <th className="py-1 font-medium">Name</th>
              <th className="py-1 font-medium">Department</th>
              <th className="py-1 font-medium">Position</th>
              <th className="py-1 font-medium">Team</th>
              <th className="py-1" />
            </tr>
          </thead>
          <tbody>
            {people.map((p) => {
              const team = o.teams.find((t) => t.id === p.teamId);
              return (
                <tr key={p.id} className="border-t border-line">
                  <td className="py-1.5 pr-2">
                    <EditableText value={p.name} onSave={(v) => act({ action: "participant.update", id: p.id, name: v })} />
                    <span className="ml-1 text-xs text-muted">
                      {team?.leaderId === p.id && "👑"}
                      {!p.hasDevice && " (added by organizer)"}
                    </span>
                  </td>
                  <td className="py-1.5 pr-2">
                    <EditableText
                      value={p.department}
                      allowEmpty
                      onSave={(v) => act({ action: "participant.update", id: p.id, department: v })}
                    />
                  </td>
                  <td className="py-1.5 pr-2">
                    <select
                      className="rounded-lg border border-line bg-bg px-2 py-1"
                      value={p.level}
                      onChange={(e) => act({ action: "participant.update", id: p.id, level: e.target.value as Level })}
                    >
                      {LEVELS.map((l) => (
                        <option key={l}>{l}</option>
                      ))}
                    </select>
                  </td>
                  <td className="py-1.5 pr-2">
                    <span className="flex items-center gap-1.5">
                      {team && <TeamDot color={team.color} />}
                      <select
                        className="rounded-lg border border-line bg-bg px-2 py-1"
                        value={p.teamId ?? ""}
                        onChange={(e) =>
                          act({ action: "participant.update", id: p.id, teamId: e.target.value ? Number(e.target.value) : null })
                        }
                      >
                        <option value="">— none —</option>
                        {o.teams.map((t) => (
                          <option key={t.id} value={t.id}>
                            {t.name}
                          </option>
                        ))}
                      </select>
                    </span>
                  </td>
                  <td className="py-1.5 text-right">
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={() => act({ action: "participant.delete", id: p.id }, `Remove ${p.name}? Their phone will need to check in again.`)}
                    >
                      Remove
                    </Button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
        {people.length === 0 && <p className="py-6 text-center text-muted">Nobody yet. Show the check-in QR on the big screen.</p>}
      </Card>
    </div>
  );
}

// Text that saves when you leave the field (or press Enter), and only if it changed.
// Escape cancels the edit.
export function EditableText({
  value,
  onSave,
  allowEmpty = false,
  className = "",
}: {
  value: string;
  onSave: (v: string) => void;
  allowEmpty?: boolean;
  className?: string;
}) {
  const [draft, setDraft] = useState(value);
  const [focused, setFocused] = useState(false);
  const cancelled = useRef(false);
  return (
    <input
      className={`w-full min-w-0 rounded-lg border border-transparent bg-transparent px-1 py-0.5 hover:border-line focus:border-accent focus:outline-none ${className}`}
      value={focused ? draft : value}
      onFocus={() => {
        cancelled.current = false;
        setDraft(value);
        setFocused(true);
      }}
      onChange={(e) => setDraft(e.target.value)}
      onBlur={() => {
        setFocused(false);
        const next = draft.trim();
        if (!cancelled.current && next !== value && (next || allowEmpty)) onSave(next);
      }}
      onKeyDown={(e) => {
        if (e.key === "Escape") cancelled.current = true;
        if (e.key === "Enter" || e.key === "Escape") e.currentTarget.blur();
      }}
    />
  );
}
