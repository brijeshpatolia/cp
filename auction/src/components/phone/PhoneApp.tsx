"use client";

import confetti from "canvas-confetti";
import { useCallback, useEffect, useRef, useState, useSyncExternalStore, type FormEvent, type ReactNode } from "react";
import { api, buzz, fmt, formatClock, usePoll, useTicker, useWakeLock } from "@/lib/client";
import { readableOn } from "@/lib/color";
import { LEVELS, type Level } from "@/lib/levels";
import { rankTeams } from "@/lib/ranking";
import type { LotView, MeState, PublicState, TeamView } from "@/lib/types";
import { Diya, Rangoli, Toran } from "../festive";
import { Button, Card, ErrorText, inputClass, Label, LevelBadge, TeamDot } from "../ui";

const noSubscribe = () => () => {};

export function PhoneApp() {
  const [me, setMe] = useState<MeState | null>(null);
  const [loadFailed, setLoadFailed] = useState(false);
  const [editing, setEditing] = useState(false);
  const badPaddle = useSyncExternalStore(
    noSubscribe,
    () => new URLSearchParams(window.location.search).get("paddle") === "invalid",
    () => false,
  );
  const notice = badPaddle ? "That paddle QR code is no longer valid. Ask an organizer for a new one." : null;

  const loadMe = useCallback(
    () =>
      api<MeState>("/api/me").then(
        (next) => {
          setMe(next);
          setLoadFailed(false);
        },
        () => setLoadFailed(true),
      ),
    [],
  );

  useEffect(() => {
    loadMe();
  }, [loadMe]);

  const bidder = Boolean(me?.bidTeam);
  const joined = Boolean(me?.participant || me?.bidTeam);
  // Leaders poll fresh state every second; everyone else reads the CDN-cached copy.
  const poll = usePoll<PublicState>(joined ? (bidder ? "/api/state" : "/api/state?cdn=1") : null, bidder ? 1000 : 3000);

  // Teams and leaders change rarely; refetch this phone's own view when they do.
  const peopleVersion = poll.data?.peopleVersion;
  useEffect(() => {
    if (peopleVersion !== undefined && me && peopleVersion > me.peopleVersion) loadMe();
  }, [peopleVersion, me, loadMe]);

  useWinCelebration(poll.data?.lot ?? null, me?.bidTeam?.id ?? me?.team?.id);

  if (!me) {
    return (
      <Shell>
        {loadFailed ? (
          <Card>
            <p className="font-semibold">Can&apos;t reach the auction right now.</p>
            <Button className="mt-3" onClick={loadMe}>
              Try again
            </Button>
          </Card>
        ) : (
          <p className="py-20 text-center text-muted">Loading…</p>
        )}
      </Shell>
    );
  }

  if (!joined || editing) {
    return (
      <Shell eventName={me.eventName}>
        {notice && <Card className="border-bad text-bad">{notice}</Card>}
        <CheckinForm
          me={me}
          onDone={(next) => {
            setMe(next);
            setEditing(false);
          }}
          onCancel={editing ? () => setEditing(false) : undefined}
        />
      </Shell>
    );
  }

  const state = poll.data;
  // Prefer the freshly polled copy of a team (coins, perks); fall back to /api/me's.
  const fresh = (team: TeamView | null) => (team ? (state?.teams.find((t) => t.id === team.id) ?? team) : null);
  const team = fresh(me.team);
  const bidTeam = fresh(me.bidTeam);
  const auctionOn = state && (state.phase === "auction" || state.phase === "results");

  return (
    <Shell eventName={me.eventName} offline={poll.offline}>
      {notice && <Card className="border-bad text-bad">{notice}</Card>}
      {me.participant && !team && <WaitingCard me={me} onEdit={() => setEditing(true)} />}
      {/* During the auction the live perk comes first; CSS order keeps the card mounted. */}
      {team && (
        <div className={auctionOn ? "order-2" : ""}>
          <TeamCard team={team} me={me} defaultOpen={!auctionOn} />
        </div>
      )}
      {bidTeam && !auctionOn && (
        <Card>
          <p className="font-semibold">👑 This phone is the bidding paddle for {bidTeam.name}.</p>
          <p className="mt-1 text-muted">Bidding opens here when the auction starts.</p>
        </Card>
      )}
      {auctionOn && state.phase === "results" && <Standings state={state} myTeamId={team?.id ?? bidTeam?.id} />}
      {auctionOn &&
        state.phase === "auction" &&
        (bidTeam ? (
          <BidPanel state={state} team={bidTeam} serverNow={poll.serverNow} onState={poll.replace} />
        ) : (
          <LotCard state={state} myTeamId={team?.id} serverNow={poll.serverNow} />
        ))}
      {team && auctionOn && !bidTeam && <TeamWallet team={team} currency={state.currency} />}
    </Shell>
  );
}

// A burst of confetti on this phone when its team wins a perk.
function useWinCelebration(lot: LotView | null, myTeamId: number | undefined) {
  const seen = useRef<string | null>(null);
  const key = lot ? `${lot.id}:${lot.status}` : null;
  useEffect(() => {
    const prev = seen.current;
    seen.current = key;
    if (!lot || lot.status !== "sold" || lot.winnerTeamId !== myTeamId) return;
    if (prev !== `${lot.id}:live` && prev !== `${lot.id}:paused`) return; // only on the moment it sells
    buzz([80, 40, 80, 40, 200]);
    confetti({
      particleCount: 120,
      spread: 90,
      origin: { y: 0.6 },
      colors: ["#fbbf24", "#f59e0b", "#db2777", "#ea580c"],
      shapes: ["star", "circle"],
      disableForReducedMotion: true,
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps -- `key` captures the transition
  }, [key, myTeamId]);
}

function Shell({ eventName, offline, children }: { eventName?: string; offline?: boolean; children: ReactNode }) {
  return (
    <>
      <Toran className="h-7" />
      <main className="mx-auto flex max-w-md flex-col gap-4 px-4 pt-2 pb-16">
        <header className="flex items-center justify-between">
          <h1 className="flex items-center gap-1.5 font-festive text-xl">
            <Diya className="h-8 w-8" />
            {eventName ?? "Diwali Perks Auction"}
          </h1>
          {offline && <span className="text-sm font-medium text-bad">Reconnecting…</span>}
        </header>
        {children}
      </main>
    </>
  );
}

function CheckinForm({ me, onDone, onCancel }: { me: MeState; onDone: (me: MeState) => void; onCancel?: () => void }) {
  const p = me.participant;
  const [name, setName] = useState(p?.name ?? "");
  const [department, setDepartment] = useState(p?.department ?? "");
  const [level, setLevel] = useState<Level | null>(p?.level ?? null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const listed = me.departments.length > 0;

  if (!p && !me.checkinOpen) {
    return (
      <Card>
        <p className="font-festive text-2xl">Check-in is closed</p>
        <p className="mt-1 text-muted">Please find an organizer and they&apos;ll add you.</p>
      </Card>
    );
  }

  async function submit(e: FormEvent) {
    e.preventDefault();
    if (!level) return setError("Please pick your position");
    setBusy(true);
    setError(null);
    try {
      onDone(await api<MeState>("/api/register", { name, department, level }));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setBusy(false);
    }
  }

  return (
    <form onSubmit={submit} className="flex flex-col gap-4">
      <div>
        {p ? (
          <p className="font-festive text-3xl leading-tight">Edit your details</p>
        ) : (
          <>
            <p className="font-festive text-4xl leading-tight text-accent">Happy Diwali!</p>
            <p className="mt-1 text-lg font-semibold">Check in to join the auction.</p>
            <p className="text-muted">Takes ten seconds. Then watch the big screen.</p>
          </>
        )}
      </div>
      <div>
        <Label htmlFor="name">Your name</Label>
        <input
          id="name"
          className={inputClass}
          value={name}
          onChange={(e) => setName(e.target.value)}
          autoComplete="name"
          maxLength={40}
          required
        />
      </div>
      <div>
        <Label htmlFor="department">Team / department</Label>
        {listed ? (
          <select id="department" className={inputClass} value={department} onChange={(e) => setDepartment(e.target.value)} required>
            <option value="" disabled>
              Choose…
            </option>
            {[...me.departments, ...(department && !me.departments.includes(department) ? [department] : [])].map((d) => (
              <option key={d}>{d}</option>
            ))}
          </select>
        ) : (
          <input
            id="department"
            className={inputClass}
            value={department}
            onChange={(e) => setDepartment(e.target.value)}
            placeholder="e.g. M&A, Risk, Operations"
            maxLength={40}
          />
        )}
      </div>
      <fieldset>
        <legend className="mb-1 block text-sm font-medium text-muted">Position</legend>
        <div className="grid grid-cols-3 gap-2">
          {LEVELS.map((l) => (
            <button
              key={l}
              type="button"
              disabled={Boolean(p) && !me.canChangeLevel}
              onClick={() => setLevel(l)}
              aria-pressed={level === l}
              className={`rounded-xl border px-2 py-3 text-sm font-semibold transition disabled:opacity-50 ${
                level === l ? "border-accent bg-accent text-accent-ink" : "border-line bg-surface"
              }`}
            >
              {l}
            </button>
          ))}
        </div>
        {p && !me.canChangeLevel && <p className="mt-1 text-xs text-muted">You&apos;re already on a team, so your position is locked.</p>}
      </fieldset>
      <ErrorText>{error}</ErrorText>
      <Button type="submit" size="lg" disabled={busy}>
        {busy ? "Saving…" : p ? "Save" : "Check in ✨"}
      </Button>
      {onCancel && (
        <Button variant="ghost" onClick={onCancel}>
          Cancel
        </Button>
      )}
    </form>
  );
}

function WaitingCard({ me, onEdit }: { me: MeState; onEdit: () => void }) {
  const p = me.participant!;
  return (
    <Card className="animate-slide-up">
      <p className="font-festive text-3xl">You&apos;re in! ✨</p>
      <div className="mt-3 flex flex-wrap items-center gap-2">
        <span className="font-semibold">{p.name}</span>
        {p.department && <span className="text-muted">· {p.department}</span>}
        <LevelBadge level={p.level} />
      </div>
      <p className="mt-3 text-muted">
        Teams will be revealed on the big screen. Keep this page open: your team will show up here.
      </p>
      <Button variant="secondary" size="sm" className="mt-4" onClick={onEdit}>
        Edit my details
      </Button>
    </Card>
  );
}

function TeamCard({ team, me, defaultOpen }: { team: TeamView; me: MeState; defaultOpen: boolean }) {
  const [toggled, setToggled] = useState<boolean | null>(null);
  const open = toggled ?? defaultOpen;
  useEffect(() => {
    buzz(200); // when this phone's team is revealed
  }, [team.id]);
  const ink = readableOn(team.color);
  return (
    <div className="animate-pop-in overflow-hidden rounded-2xl border border-line bg-surface">
      <div className="relative overflow-hidden p-5" style={{ background: team.color, color: ink }}>
        <Rangoli opacity="0.3" className="animate-spin-slow pointer-events-none absolute -top-10 -right-10 h-40 w-40" />
        <p className="relative text-xs font-bold uppercase tracking-[0.2em] opacity-90">Your team</p>
        <p className="relative font-festive text-4xl leading-tight">{team.name}</p>
        <p className="relative mt-1 text-lg font-semibold">Sit at table {team.tableNo}</p>
      </div>
      <div className="p-4">
        {me.isLeader ? (
          <p className="font-semibold">👑 You&apos;re the team leader! Your phone is the team&apos;s bidding paddle.</p>
        ) : (
          team.leader && (
            <p>
              👑 Leader: <b>{team.leader.name}</b>
            </p>
          )
        )}
        <button className="mt-3 text-sm font-semibold text-muted" onClick={() => setToggled(!open)}>
          {open ? "Hide" : "Show"} {team.members.length} members
        </button>
        {open && (
          <ul className="mt-1 divide-y divide-line">
            {team.members.map((m) => (
              <li key={m.id} className="flex items-center justify-between gap-2 py-2">
                <span className="truncate">
                  {m.name}
                  {m.id === me.participant?.id && <span className="text-muted"> (you)</span>}
                  {team.leader?.id === m.id && " 👑"}
                </span>
                <LevelBadge level={m.level} />
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

function teamOf(state: PublicState, id: number | null | undefined) {
  return state.teams.find((t) => t.id === id) ?? null;
}

function LotStatus({ state, lot, myTeamId, serverNow }: { state: PublicState; lot: LotView; myTeamId?: number; serverNow: () => number }) {
  useTicker(250);
  const top = teamOf(state, lot.top?.teamId);
  const winner = teamOf(state, lot.winnerTeamId);
  const left = lot.endsAt ? lot.endsAt - serverNow() : 0;

  return (
    <div>
      <div className="flex items-start gap-3">
        <span className="text-5xl leading-none">{lot.emoji}</span>
        <div className="min-w-0">
          <p className="font-festive text-2xl leading-tight">{lot.title}</p>
          {lot.description && <p className="mt-0.5 text-sm text-muted">{lot.description}</p>}
        </div>
      </div>

      {lot.status === "sold" && winner && (
        <p className="mt-4 rounded-xl p-3 text-center text-lg font-bold" style={{ background: winner.color, color: readableOn(winner.color) }}>
          {winner.id === myTeamId ? "🎉 Your team won it" : `SOLD to ${winner.name}`} for {fmt(lot.price ?? 0)} {state.currency}
        </p>
      )}
      {lot.status === "unsold" && <p className="mt-4 text-center font-semibold text-muted">No bids. Unsold.</p>}

      {(lot.status === "live" || lot.status === "paused") && (
        <div className="mt-4 flex items-end justify-between gap-3">
          <div>
            <p className="text-sm text-muted">{lot.top ? "Top bid" : "Opens at"}</p>
            <p className="tabular text-4xl font-extrabold">{fmt(lot.top?.amount ?? lot.startPrice)}</p>
            {top && (
              <p className="mt-1 flex items-center gap-1.5 font-semibold">
                <TeamDot color={top.color} />
                {top.id === myTeamId ? "Your team" : top.name}
              </p>
            )}
          </div>
          <div className="text-right">
            {lot.status === "paused" ? (
              <p className="text-xl font-bold">⏸ Paused</p>
            ) : (
              <>
                <p className={`tabular text-4xl font-extrabold ${left < 10_000 ? "animate-urgent text-bad" : ""}`}>{formatClock(left)}</p>
                <p className="text-sm text-muted">{left >= 60_000 ? "left" : "seconds left"}</p>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

function LotCard({ state, myTeamId, serverNow }: { state: PublicState; myTeamId?: number; serverNow: () => number }) {
  if (!state.lot) {
    return (
      <Card>
        <p className="font-festive text-2xl">The auction is about to start</p>
        {state.nextLot && (
          <p className="mt-1 text-muted">
            First up: {state.nextLot.emoji} {state.nextLot.title}
          </p>
        )}
        <p className="mt-2 text-muted">Watch the big screen!</p>
      </Card>
    );
  }
  return (
    <Card>
      <LotStatus state={state} lot={state.lot} myTeamId={myTeamId} serverNow={serverNow} />
    </Card>
  );
}

function TeamWallet({ team, currency }: { team: TeamView; currency: string }) {
  return (
    <Card>
      <div className="flex items-baseline justify-between">
        <p className="font-semibold">{team.name} has</p>
        <p className="tabular text-2xl font-extrabold">
          {fmt(team.coinsLeft)} <span className="text-base font-semibold text-muted">{currency}</span>
        </p>
      </div>
      {team.perks.length > 0 && (
        <ul className="mt-2 flex flex-wrap gap-2">
          {team.perks.map((p) => (
            <li key={p.lotId} className="rounded-full bg-surface-2 px-3 py-1 text-sm font-medium">
              {p.emoji} {p.title}
            </li>
          ))}
        </ul>
      )}
    </Card>
  );
}

function BidPanel({
  state,
  team,
  serverNow,
  onState,
}: {
  state: PublicState;
  team: TeamView;
  serverNow: () => number;
  onState: (s: PublicState) => void;
}) {
  useWakeLock();
  useTicker(250);
  const [busy, setBusy] = useState(false);
  const [feedback, setFeedback] = useState<{ lotId: number; amount: number; ok: boolean; text: string } | null>(null);
  const [custom, setCustom] = useState("");
  const lot = state.lot;
  const running = lot?.status === "live" && (lot.endsAt ?? 0) > serverNow();
  const winning = Boolean(lot && lot.top?.teamId === team.id && (lot.status === "live" || lot.status === "paused"));

  // Buzz when this team loses the top spot.
  const wasWinning = useRef(false);
  useEffect(() => {
    if (wasWinning.current && !winning && lot?.status === "live") buzz([120, 60, 120]);
    wasWinning.current = winning;
  }, [winning, lot?.status]);

  async function bid(amount: number) {
    if (!lot) return;
    setBusy(true);
    setFeedback(null);
    try {
      const res = await api<{ state: PublicState }>("/api/bid", { lotId: lot.id, amount });
      onState(res.state);
      setFeedback({ lotId: lot.id, amount, ok: true, text: `You bid ${fmt(amount)} ${state.currency}` });
      setCustom("");
    } catch (err) {
      setFeedback({ lotId: lot.id, amount, ok: false, text: err instanceof Error ? err.message : "That bid didn't go through" });
    } finally {
      setBusy(false);
    }
  }

  const quick = lot ? [...new Set([lot.minNext, lot.minNext + lot.step, lot.minNext + lot.step * 4])] : [];
  const affordable = quick.filter((a) => a <= team.coinsLeft);
  const customAmount = Number(custom);

  return (
    <>
      <div
        className="flex items-center justify-between rounded-2xl p-4"
        style={{ background: team.color, color: readableOn(team.color) }}
      >
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.2em] opacity-90">Bidding for</p>
          <p className="font-festive text-2xl leading-tight">{team.name}</p>
        </div>
        <div className="text-right">
          <p className="tabular text-3xl font-extrabold">{fmt(team.coinsLeft)}</p>
          <p className="text-sm font-semibold opacity-90">{state.currency} left</p>
        </div>
      </div>

      <Card>
        {lot ? (
          <LotStatus state={state} lot={lot} myTeamId={team.id} serverNow={serverNow} />
        ) : (
          <p className="font-festive text-xl">Waiting for the first perk…</p>
        )}
      </Card>

      {lot && (lot.status === "live" || lot.status === "paused") && (
        <Card className={winning ? "border-good" : ""}>
          <p className={`text-center text-lg font-extrabold ${winning ? "text-good" : lot.top ? "text-bad" : ""}`}>
            {winning ? "You're winning 🎉" : lot.top ? "You're not winning. Bid!" : "No bids yet. Open the bidding!"}
          </p>
          <div className="mt-3 grid grid-cols-1 gap-2">
            {affordable.map((amount, i) => (
              <Button
                key={amount}
                size="lg"
                variant={i === 0 ? "primary" : "secondary"}
                disabled={!running || winning || busy}
                onClick={() => bid(amount)}
              >
                Bid {fmt(amount)}
              </Button>
            ))}
          </div>
          {affordable.length === 0 && (
            <p className="mt-2 text-center font-semibold text-bad">
              Not enough {state.currency} left for the minimum bid of {fmt(lot.minNext)}.
            </p>
          )}
          <form
            className="mt-3 flex gap-2"
            onSubmit={(e) => {
              e.preventDefault();
              if (customAmount > 0) bid(customAmount);
            }}
          >
            <input
              className={inputClass}
              type="number"
              inputMode="numeric"
              min={lot.minNext}
              max={team.coinsLeft}
              step={1}
              placeholder={`${fmt(lot.minNext)} or more`}
              value={custom}
              onChange={(e) => setCustom(e.target.value)}
              disabled={!running || winning}
            />
            <Button type="submit" variant="secondary" disabled={!running || winning || busy || !(customAmount > 0)}>
              Bid
            </Button>
          </form>
          {/* A success message goes stale once someone outbids it. */}
          {feedback?.lotId === lot.id && (!feedback.ok || lot.top?.amount === feedback.amount) && (
            <p className={`mt-3 text-center font-semibold ${feedback.ok ? "text-good" : "text-bad"}`}>{feedback.text}</p>
          )}
        </Card>
      )}

      {team.perks.length > 0 && <TeamWallet team={team} currency={state.currency} />}
    </>
  );
}

function Standings({ state, myTeamId }: { state: PublicState; myTeamId?: number }) {
  return (
    <Card>
      <p className="font-festive text-3xl">Final standings</p>
      <p className="font-festive text-lg text-accent">Happy Diwali! शुभ दीपावली</p>
      <ol className="mt-3 flex flex-col gap-2">
        {rankTeams(state.teams).map((t, i) => (
          <li key={t.id} className={`flex items-center gap-3 rounded-xl p-2 ${t.id === myTeamId ? "bg-surface-2" : ""}`}>
            <span className="tabular w-6 text-center font-bold">{i === 0 ? "🏆" : i + 1}</span>
            <TeamDot color={t.color} />
            <span className="min-w-0 flex-1">
              <span className="block truncate font-semibold">{t.name}</span>
              <span className="block text-sm text-muted">
                {t.perks.length} perk{t.perks.length === 1 ? "" : "s"} · {fmt(t.coinsLeft)} {state.currency} left
              </span>
            </span>
          </li>
        ))}
      </ol>
    </Card>
  );
}
