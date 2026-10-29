"use client";

import { useCallback, useEffect, useState, type FormEvent } from "react";
import type { AdminAction } from "@/lib/admin";
import { api, ApiError, usePoll } from "@/lib/client";
import type { AdminOverview } from "@/lib/types";
import { Button, Card, ErrorText, inputClass, Label } from "../ui";
import { LiveTab } from "./LiveTab";
import { PeopleTab } from "./PeopleTab";
import { PerksTab } from "./PerksTab";
import { SettingsTab } from "./SettingsTab";
import { TeamsTab } from "./TeamsTab";

export type Act = (action: AdminAction, confirmText?: string) => Promise<Record<string, unknown> | null>;

export interface TabProps {
  o: AdminOverview;
  act: Act;
  serverNow: () => number;
}

const TABS = [
  ["live", "Live"],
  ["people", "People"],
  ["teams", "Teams"],
  ["perks", "Perks"],
  ["settings", "Settings"],
] as const;
type Tab = (typeof TABS)[number][0];

export function AdminApp() {
  const [authed, setAuthed] = useState<boolean | null>(null);
  useEffect(() => {
    api<{ admin: boolean }>("/api/admin/session")
      .then((r) => setAuthed(r.admin))
      .catch(() => setAuthed(false));
  }, []);

  if (authed === null) return <p className="py-20 text-center text-muted">Loading…</p>;
  if (!authed) return <Login onDone={() => setAuthed(true)} />;
  return <Console onLoggedOut={() => setAuthed(false)} />;
}

function Login({ onDone }: { onDone: () => void }) {
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(e: FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);
    try {
      await api("/api/admin/session", { password });
      onDone();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="mx-auto max-w-sm px-4 pt-24">
      <Card>
        <form onSubmit={submit} className="flex flex-col gap-3">
          <p className="text-xl font-extrabold">🔨 Organizer login</p>
          <div>
            <Label htmlFor="password">Admin password</Label>
            <input
              id="password"
              type="password"
              className={inputClass}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              autoComplete="current-password"
              autoFocus
            />
          </div>
          <ErrorText>{error}</ErrorText>
          <Button type="submit" disabled={busy || !password}>
            {busy ? "Checking…" : "Log in"}
          </Button>
        </form>
      </Card>
    </main>
  );
}

function Console({ onLoggedOut }: { onLoggedOut: () => void }) {
  const poll = usePoll<AdminOverview>("/api/admin", 1000);
  const [tab, setTab] = useState<Tab>("live");
  const [toast, setToast] = useState<{ ok: boolean; text: string } | null>(null);
  const { replace } = poll;

  useEffect(() => {
    if (poll.error?.status === 401) onLoggedOut();
  }, [poll.error, onLoggedOut]);

  useEffect(() => {
    if (!toast) return;
    const id = setTimeout(() => setToast(null), toast.ok ? 2500 : 6000);
    return () => clearTimeout(id);
  }, [toast]);

  const act: Act = useCallback(
    async (action, confirmText) => {
      if (confirmText && !window.confirm(confirmText)) return null;
      try {
        const res = await api<Record<string, unknown> & { overview: AdminOverview }>("/api/admin", action);
        replace(res.overview);
        return res;
      } catch (err) {
        if (err instanceof ApiError && err.status === 401) onLoggedOut();
        setToast({ ok: false, text: err instanceof Error ? err.message : "That didn't work" });
        return null;
      }
    },
    [replace, onLoggedOut],
  );

  const o = poll.data;
  return (
    <div className="mx-auto max-w-6xl px-4 pt-4 pb-24">
      <header className="flex flex-wrap items-center justify-between gap-3">
        <h1 className="text-xl font-extrabold">🔨 {o?.settings.eventName ?? "Office Auction"} · Admin</h1>
        <div className="flex items-center gap-3 text-sm">
          {poll.offline && <span className="font-semibold text-bad">Reconnecting…</span>}
          <a href="/board" target="_blank" rel="noreferrer" className="font-semibold text-accent underline">
            Open big screen ↗
          </a>
        </div>
      </header>
      <nav className="sticky top-0 z-10 -mx-4 mt-3 flex gap-1 overflow-x-auto border-b border-line bg-bg px-4 py-2">
        {TABS.map(([key, label]) => (
          <button
            key={key}
            onClick={() => setTab(key)}
            className={`rounded-lg px-3 py-1.5 text-sm font-semibold whitespace-nowrap ${tab === key ? "bg-ink text-bg" : "text-muted"}`}
          >
            {label}
            {key === "people" && o ? ` (${o.participants.length})` : ""}
            {key === "perks" && o ? ` (${o.lots.length})` : ""}
          </button>
        ))}
      </nav>
      <div className="mt-4">
        {!o ? (
          <p className="py-20 text-center text-muted">Loading…</p>
        ) : tab === "live" ? (
          <LiveTab o={o} act={act} serverNow={poll.serverNow} />
        ) : tab === "people" ? (
          <PeopleTab o={o} act={act} serverNow={poll.serverNow} />
        ) : tab === "teams" ? (
          <TeamsTab o={o} act={act} serverNow={poll.serverNow} />
        ) : tab === "perks" ? (
          <PerksTab o={o} act={act} serverNow={poll.serverNow} />
        ) : (
          <SettingsTab o={o} act={act} serverNow={poll.serverNow} onLoggedOut={onLoggedOut} />
        )}
      </div>
      {toast && (
        <div
          role="status"
          className={`fixed inset-x-4 bottom-4 z-20 mx-auto max-w-md rounded-xl px-4 py-3 font-semibold shadow-lg ${
            toast.ok ? "bg-good text-white" : "bg-bad text-white"
          }`}
        >
          {toast.text}
        </div>
      )}
    </div>
  );
}
