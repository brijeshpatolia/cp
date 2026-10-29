"use client";

import confetti from "canvas-confetti";
import { useEffect, useRef, useState, type ReactNode } from "react";
import { fmt, formatClock, useLocalPref, useOrigin, usePoll, useTicker, useWakeLock } from "@/lib/client";
import { readableOn } from "@/lib/color";
import { LEVELS_SENIOR_FIRST } from "@/lib/levels";
import { rankTeams } from "@/lib/ranking";
import type { LotView, PublicState, TeamView } from "@/lib/types";
import { Diya, DiyaRow, Rangoli, Toran } from "../festive";
import { QrCode } from "../QrCode";
import { TeamDot } from "../ui";
import { sounds } from "./sound";

type Theme = "light" | "dark";

const FESTIVE_COLORS = ["#fbbf24", "#f59e0b", "#ea580c", "#db2777", "#fde68a"];

export function Board() {
  const poll = usePoll<PublicState>("/api/state", 500);
  const [theme, setTheme] = useLocalPref<Theme>("board-theme", "light");
  const [soundOn, setSoundOn] = useState(false);
  const joinUrl = useOrigin();
  useWakeLock();

  // A projector on a whiteboard washes out dark backgrounds, so the light
  // "festive day" theme is the default; "Diwali night" suits a TV.
  useEffect(() => {
    const root = document.documentElement;
    root.classList.toggle("dark", theme === "dark");
    root.classList.toggle("light", theme === "light");
    return () => root.classList.remove("dark", "light");
  }, [theme]);

  const s = poll.data;
  useBoardEffects(s, soundOn);

  return (
    <div className="relative flex h-dvh w-full flex-col overflow-hidden text-ink">
      <Toran className="h-[5.5vh]" />
      <div className="flex min-h-0 flex-1 flex-col px-[3vw] pt-[1.5vh] pb-[3vh]">
        <header className="flex items-center justify-between gap-4 text-[2.2vh] font-semibold text-muted">
          <span className="flex items-center gap-[0.6vw] font-festive text-[2.8vh] text-ink">
            <Diya className="h-[3.6vh] w-[3.6vh]" />
            {s?.eventName ?? "Diwali Perks Auction"}
          </span>
          <span className="flex items-center gap-3">
            <span className={poll.offline ? "font-bold text-bad" : ""}>
              {poll.offline ? "Reconnecting…" : s && s.phase === "checkin" ? `${s.stats.registered} checked in` : ""}
            </span>
            <span className="flex gap-2 opacity-25 transition hover:opacity-100">
              <SmallButton
                label={soundOn ? "Mute" : "Sound on"}
                onClick={() => {
                  if (!soundOn) sounds.unlock();
                  setSoundOn(!soundOn);
                }}
              >
                {soundOn ? "🔊" : "🔇"}
              </SmallButton>
              <SmallButton label={theme === "light" ? "Diwali night theme" : "Festive day theme"} onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
                {theme === "light" ? "☾" : "☀"}
              </SmallButton>
              <SmallButton
                label="Full screen"
                onClick={() => (document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen())}
              >
                ⛶
              </SmallButton>
            </span>
          </span>
        </header>
        <main className="relative min-h-0 flex-1">
          {!s ? (
            <Center>
              <DiyaRow count={3} />
              <p className="text-[4vh] text-muted">Lighting the diyas…</p>
            </Center>
          ) : s.board.scene === "checkin" ? (
            <CheckinScene s={s} joinUrl={joinUrl} />
          ) : s.board.scene === "reveal" ? (
            <RevealScene s={s} />
          ) : s.board.scene === "lot" ? (
            <LotScene s={s} serverNow={poll.serverNow} />
          ) : s.board.scene === "leaderboard" ? (
            <LeaderboardScene s={s} />
          ) : (
            <Center>
              <CornerRangoli />
              <p className="max-w-[80vw] text-center font-festive text-[10vh] leading-tight">{s.board.message || "…"}</p>
              <DiyaRow count={5} className="h-[8vh] w-[8vh]" />
            </Center>
          )}
        </main>
      </div>
    </div>
  );
}

function SmallButton({ label, onClick, children }: { label: string; onClick: () => void; children: ReactNode }) {
  return (
    <button
      aria-label={label}
      title={label}
      onClick={onClick}
      className="grid h-[4vh] w-[4vh] place-items-center rounded-full border border-line bg-surface text-[2vh]"
    >
      {children}
    </button>
  );
}

// canvas-confetti works in CSS pixels; scale it so a 4K TV gets the same show as a laptop.
const screenScale = () => Math.max(1, window.innerHeight / 900);

// Bursts of fireworks across the top half of the screen.
function fireworks(colors: string[], durationMs: number) {
  const k = screenScale();
  const end = Date.now() + durationMs;
  const timer = setInterval(() => {
    if (Date.now() > end) return clearInterval(timer);
    for (const x of [0.08 + Math.random() * 0.34, 0.58 + Math.random() * 0.34]) {
      confetti({
        particleCount: 50,
        spread: 360,
        startVelocity: 26 * k,
        ticks: 75,
        gravity: 0.7 * k,
        scalar: 0.95 * k,
        shapes: ["star", "circle"],
        origin: { x, y: 0.12 + Math.random() * 0.3 },
        colors,
        disableForReducedMotion: true,
      });
    }
  }, 300);
}

// Sounds and fireworks, fired once per event (new bid, perk sold, final results).
function useBoardEffects(s: PublicState | null | undefined, soundOn: boolean) {
  const seen = useRef<{ lotId?: number; topBid?: number; status?: string; phase?: string } | null>(null);
  const lot = s?.lot;
  const key = `${s?.phase}:${lot ? `${lot.id}:${lot.status}:${lot.top?.amount ?? 0}` : "none"}`;

  useEffect(() => {
    const prev = seen.current;
    seen.current = { lotId: lot?.id, topBid: lot?.top?.amount, status: lot?.status, phase: s?.phase };
    if (!prev || !s) return; // first load: don't replay what already happened
    if (s.phase === "results" && prev.phase !== "results") {
      if (soundOn) sounds.bell();
      fireworks(FESTIVE_COLORS, 6000);
      return;
    }
    if (!lot || prev.lotId !== lot.id) return;
    if (lot.top && lot.top.amount !== prev.topBid && soundOn) sounds.bid();
    if (lot.status === "sold" && prev.status !== "sold") {
      if (soundOn) sounds.gavel();
      const color = s.teams.find((t) => t.id === lot.winnerTeamId)?.color ?? "#9f1d45";
      const k = screenScale();
      confetti({
        particleCount: 160,
        spread: 100,
        startVelocity: 50 * k,
        gravity: k,
        scalar: k,
        origin: { x: 0.35, y: 0.75 },
        colors: [color, ...FESTIVE_COLORS],
        shapes: ["star", "circle"],
        disableForReducedMotion: true,
      });
      fireworks([color, ...FESTIVE_COLORS], 2500);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps -- `key` captures every change that matters
  }, [key, soundOn]);
}

function Center({ children }: { children: ReactNode }) {
  return <div className="relative flex h-full flex-col items-center justify-center gap-[2.4vh]">{children}</div>;
}

function CornerRangoli() {
  return (
    <>
      <Rangoli className="animate-spin-slow pointer-events-none absolute -bottom-[18vh] -left-[14vh] h-[56vh] w-[56vh]" />
      <Rangoli className="animate-spin-slow pointer-events-none absolute -right-[14vh] -bottom-[18vh] h-[56vh] w-[56vh]" />
    </>
  );
}

function CheckinScene({ s, joinUrl }: { s: PublicState; joinUrl: string }) {
  return (
    <div className="relative grid h-full grid-cols-[auto_1fr] items-center gap-[5vw]">
      <Rangoli className="animate-spin-slow pointer-events-none absolute -right-[12vh] -bottom-[20vh] h-[62vh] w-[62vh]" />
      <div className="relative flex flex-col items-center gap-[1.8vh]">
        <p className="font-festive text-[5.5vh] leading-none">Scan to join</p>
        <div className="rounded-[2.6vh] bg-gradient-to-br from-[#f59e0b] via-[#fbbf24] to-[#db2777] p-[0.9vh] shadow-xl">
          <QrCode value={joinUrl} className="h-[52vh]" />
        </div>
        <p className="text-[2.6vh] font-semibold text-muted">{joinUrl.replace(/^https?:\/\//, "")}</p>
      </div>
      <div className="relative flex min-w-0 flex-col gap-[2.6vh]">
        <p className="font-festive text-[4.6vh] leading-tight text-accent">शुभ दीपावली · Happy Diwali</p>
        <div>
          <p className="tabular text-[20vh] leading-none font-black">{s.stats.registered}</p>
          <p className="text-[4vh] font-bold text-muted">checked in{!s.checkinOpen && " · check-in closed"}</p>
        </div>
        <div className="flex flex-wrap gap-[1vw] text-[2.6vh]">
          {LEVELS_SENIOR_FIRST.map((l) => (
            <span key={l} className="rounded-full border border-line bg-surface px-[1.2vw] py-[0.6vh] font-semibold">
              {l} <span className="tabular text-muted">{s.stats.byLevel[l]}</span>
            </span>
          ))}
        </div>
        <ul className="flex flex-wrap gap-[0.8vw] text-[2.6vh]">
          {s.stats.recent.map((p) => (
            <li key={p.id} className="animate-slide-up rounded-xl border border-line bg-surface px-[1vw] py-[0.6vh]">
              ✨ {p.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

function RevealScene({ s }: { s: PublicState }) {
  const revealed = [...s.teams].sort((a, b) => a.revealOrder - b.revealOrder);
  const latest = revealed.at(-1);
  if (!latest) {
    return (
      <Center>
        <CornerRangoli />
        <p className="text-[3.6vh] font-bold tracking-[0.3em] text-muted uppercase">{s.teamCount} teams</p>
        <p className="text-center font-festive text-[12vh] leading-none">Who&apos;s on your team?</p>
        <DiyaRow count={7} className="h-[8vh] w-[8vh]" />
        <p className="text-[3.2vh] text-muted">Watch this screen, and your phone.</p>
      </Center>
    );
  }
  const ink = readableOn(latest.color);
  return (
    <div className="grid h-full grid-cols-[1fr_auto] gap-[2.5vw] pt-[1.5vh]">
      <div key={latest.id} className="animate-pop-in flex min-h-0 flex-col overflow-hidden rounded-[2vh] border border-line bg-surface shadow-xl">
        <div
          className="relative flex items-end justify-between gap-[2vw] overflow-hidden px-[2.5vw] py-[3vh]"
          style={{ background: latest.color, color: ink }}
        >
          <Rangoli opacity="0.28" className="animate-spin-slow pointer-events-none absolute -top-[10vh] right-[18vw] h-[34vh] w-[34vh]" />
          <div className="relative min-w-0">
            <p className="text-[2.4vh] font-bold tracking-[0.25em] uppercase opacity-90">
              Team {latest.revealOrder} of {s.teamCount}
            </p>
            <p className="truncate font-festive text-[min(10vh,6vw)] leading-[1.2]">{latest.name}</p>
          </div>
          <div className="relative shrink-0 text-right">
            <p className="text-[2.4vh] font-bold tracking-[0.25em] uppercase opacity-90">Table</p>
            <p className="tabular text-[9vh] leading-none font-black">{latest.tableNo}</p>
          </div>
        </div>
        <ul className="grid min-h-0 flex-1 grid-cols-2 content-start gap-x-[3vw] gap-y-[2.4vh] px-[2.5vw] py-[3.5vh] text-[min(4.2vh,2.7vw)]">
          {latest.members.map((m, i) => (
            <li key={m.id} className="animate-slide-up flex items-baseline justify-between gap-3" style={{ animationDelay: `${i * 90}ms` }}>
              <span className="truncate font-bold">
                {latest.leader?.id === m.id && "👑 "}
                {m.name}
              </span>
              <span className="shrink-0 text-[min(2.6vh,1.6vw)] font-semibold text-muted">{m.level}</span>
            </li>
          ))}
        </ul>
      </div>
      <div className="flex w-[22vw] flex-col gap-[1.2vh] overflow-hidden [@media(max-aspect-ratio:3/2)]:w-[27vw]">
        <p className="text-[2.4vh] font-bold text-muted">
          {revealed.length} of {s.teamCount} revealed
        </p>
        {revealed
          .slice(0, -1)
          .reverse()
          .map((t) => (
            <div key={t.id} className="flex items-center gap-3 rounded-xl border border-line bg-surface px-4 py-[1.2vh] text-[min(2.6vh,1.9vw)]">
              <TeamDot color={t.color} className="h-[2vh] w-[2vh]" />
              <span className="flex-1 truncate font-bold">{t.name}</span>
              <span className="text-muted">T{t.tableNo}</span>
            </div>
          ))}
      </div>
    </div>
  );
}

function LotScene({ s, serverNow }: { s: PublicState; serverNow: () => number }) {
  const lot = s.lot;
  if (!lot) {
    return (
      <Center>
        <CornerRangoli />
        <p className="text-[3.6vh] font-bold tracking-[0.3em] text-muted uppercase">{s.nextLot ? "First up" : "The auction"}</p>
        {s.nextLot ? (
          <>
            <p className="text-[16vh] leading-none">{s.nextLot.emoji}</p>
            <p className="text-center font-festive text-[9vh] leading-none">{s.nextLot.title}</p>
          </>
        ) : (
          <p className="font-festive text-[9vh]">Starting soon</p>
        )}
        <DiyaRow count={5} />
      </Center>
    );
  }
  return (
    <div className="grid h-full grid-cols-[1fr_32vw] gap-[3vw] pt-[1.5vh]">
      <LotHero s={s} lot={lot} serverNow={serverNow} />
      <div className="flex min-h-0 flex-col gap-[2.5vh]">
        <BidTicker s={s} lot={lot} />
        <CoinTable s={s} lot={lot} />
      </div>
    </div>
  );
}

// Approximate width of a number or clock in em at the board's black, tabular weight
// (measured: digits 0.66em, comma 0.26em, colon 0.32em), with a little slack.
function emWidth(text: string) {
  let em = 0.08;
  for (const ch of text) em += ch === "," ? 0.27 : ch === ":" ? 0.33 : 0.66;
  return Math.round(em * 100) / 100;
}

function teamById(s: PublicState, id: number | null | undefined): TeamView | undefined {
  return s.teams.find((t) => t.id === id);
}

function LotHero({ s, lot, serverNow }: { s: PublicState; lot: LotView; serverNow: () => number }) {
  useTicker(200);
  const top = teamById(s, lot.top?.teamId);
  const winner = teamById(s, lot.winnerTeamId);
  const left = lot.status === "live" && lot.endsAt ? Math.max(0, lot.endsAt - serverNow()) : (lot.pausedMsLeft ?? 0);
  const running = lot.status === "live" || lot.status === "paused";
  const amount = lot.status === "sold" ? (lot.price ?? 0) : (lot.top?.amount ?? lot.startPrice);
  const amountTeam = lot.status === "sold" ? winner : top;
  const callout = lot.status === "live" && left > 0 && left <= 5000 ? (left > 2500 ? "Going once…" : "Going twice…") : null;

  return (
    <div className="@container relative flex min-h-0 flex-col">
      <div className="flex items-start gap-[2vw]">
        <span className="text-[16vh] leading-none">{lot.emoji}</span>
        <div className="min-w-0 pt-[1vh]">
          <p className="font-festive text-[min(8vh,5.4vw)] leading-[1.1]">{lot.title}</p>
          {lot.description && <p className="mt-[1vh] text-[3vh] text-muted">{lot.description}</p>}
        </div>
      </div>

      <div className="mt-auto flex items-end justify-between gap-[3vw]">
        <div className="min-w-0">
          <p className="text-[3vh] font-bold tracking-[0.2em] text-muted uppercase">
            {lot.status === "sold" ? "Sold for" : lot.status === "unsold" ? "Opened at" : lot.top ? "Top bid" : "Opening bid"}
          </p>
          <p
            key={amount}
            className="tabular animate-bump leading-[0.95] font-black"
            // Fill the space beside the countdown ring, but never run into it: 30vh ring + 3vw gap.
            style={{ color: amountTeam?.color, fontSize: `min(24vh, calc((100cqw - 30vh - 3vw) / ${emWidth(fmt(amount))}))` }}
          >
            {fmt(amount)}
          </p>
          <p className="h-[6vh] font-festive text-[4.5vh]" style={{ color: amountTeam?.color }}>
            {amountTeam ? amountTeam.name : running ? `+${fmt(lot.step)} per bid` : ""}
          </p>
        </div>
        {running && <CountdownRing left={left} total={lot.durationS * 1000} paused={lot.status === "paused"} />}
      </div>

      {callout && (
        <div className="pointer-events-none absolute inset-0 grid place-items-center">
          <p key={callout} className="animate-pop-in rounded-[2vh] bg-ink px-[3vw] py-[2vh] font-festive text-[11vh] text-bg shadow-2xl">
            {callout}
          </p>
        </div>
      )}
      {lot.status === "sold" && winner && (
        <div className="pointer-events-none absolute inset-0 grid place-items-center">
          <div
            className="animate-stamp rounded-[2vh] border-[1vh] px-[3.5vw] py-[1.5vh] text-center shadow-2xl"
            style={{ borderColor: "#fbbf24", background: winner.color, color: readableOn(winner.color) }}
          >
            <p className="font-festive text-[16vh] leading-none">SOLD!</p>
            <p className="font-festive text-[5vh]">to {winner.name}</p>
          </div>
        </div>
      )}
      {lot.status === "unsold" && (
        <div className="pointer-events-none absolute inset-0 grid place-items-center">
          <p className="animate-stamp rounded-[2vh] border-[1vh] border-muted bg-surface px-[3vw] py-[1vh] font-festive text-[12vh] text-muted">
            No bids
          </p>
        </div>
      )}
    </div>
  );
}

function CountdownRing({ left, total, paused }: { left: number; total: number; paused: boolean }) {
  const r = 45;
  const circumference = 2 * Math.PI * r;
  const fraction = Math.min(1, left / Math.max(total, 1));
  const urgent = !paused && left <= 10_000;
  return (
    <div className="relative h-[30vh] w-[30vh] shrink-0">
      <svg viewBox="0 0 100 100" className="h-full w-full -rotate-90">
        <circle cx="50" cy="50" r={r} fill="none" stroke="var(--border)" strokeWidth="7" />
        <circle
          cx="50"
          cy="50"
          r={r}
          fill="none"
          stroke={urgent ? "var(--bad)" : "#f59e0b"}
          strokeWidth="7"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={circumference * (1 - fraction)}
          style={{ transition: "stroke-dashoffset 0.25s linear" }}
        />
      </svg>
      <div className="absolute inset-0 grid place-items-center">
        {paused ? (
          <p className="font-festive text-[5vh]">Paused</p>
        ) : (
          <p
            className={`tabular font-black ${urgent ? "animate-urgent text-bad" : ""}`}
            style={{ fontSize: `${Math.min(11, 23 / emWidth(formatClock(left)))}vh` }}
          >
            {formatClock(left)}
          </p>
        )}
      </div>
    </div>
  );
}

function BidTicker({ s, lot }: { s: PublicState; lot: LotView }) {
  return (
    <div className="min-h-0">
      <p className="mb-[1vh] text-[2.4vh] font-bold tracking-[0.2em] text-muted uppercase">Bids</p>
      {lot.bids.length === 0 ? (
        <p className="text-[3vh] text-muted">No bids yet</p>
      ) : (
        <ul className="flex flex-col gap-[0.8vh]">
          {lot.bids.slice(0, 4).map((b, i) => {
            const team = teamById(s, b.teamId);
            return (
              <li
                key={b.id}
                className={`flex items-center gap-3 rounded-xl px-4 py-[1vh] text-[3vh] ${
                  i === 0 ? "animate-slide-up border border-line bg-surface font-extrabold" : "text-muted"
                }`}
              >
                <TeamDot color={team?.color ?? "#999"} className="h-[2.2vh] w-[2.2vh]" />
                <span className="flex-1 truncate">{team?.name ?? "?"}</span>
                <span className="tabular">{fmt(b.amount)}</span>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
}

function CoinTable({ s, lot }: { s: PublicState; lot: LotView }) {
  const teams = [...s.teams].sort((a, b) => b.coinsLeft - a.coinsLeft);
  const max = Math.max(1, ...s.teams.map((t) => t.coins));
  return (
    <div className="mt-auto">
      <p className="mb-[1vh] text-[2.4vh] font-bold tracking-[0.2em] text-muted uppercase">{s.currency} left</p>
      <ul className="flex flex-col gap-[0.7vh]">
        {teams.map((t) => {
          // While bidding is open, fade teams that can't afford the next bid (but not the top bidder).
          const open = lot.status === "live" || lot.status === "paused";
          const short = open && t.id !== lot.top?.teamId && t.coinsLeft < lot.minNext;
          return (
            <li
              key={t.id}
              className={`grid grid-cols-[minmax(0,3fr)_minmax(0,2fr)_auto] items-center gap-3 text-[2.3vh] ${short ? "opacity-40" : ""}`}
            >
              <span className="truncate font-semibold">{t.name}</span>
              <span className="h-[1.4vh] overflow-hidden rounded-full bg-surface-2">
                <span className="block h-full rounded-full" style={{ width: `${(t.coinsLeft / max) * 100}%`, background: t.color }} />
              </span>
              <span className="tabular text-right font-bold">{fmt(t.coinsLeft)}</span>
            </li>
          );
        })}
      </ul>
    </div>
  );
}

function LeaderboardScene({ s }: { s: PublicState }) {
  const ranked = rankTeams(s.teams);
  const final = s.phase === "results";
  return (
    <div className="relative flex h-full flex-col pt-[1.5vh]">
      {final && <Rangoli className="animate-spin-slow pointer-events-none absolute -top-[16vh] -right-[12vh] h-[48vh] w-[48vh]" />}
      <div className="relative flex items-end gap-[1.5vw]">
        <p className="font-festive text-[8vh] leading-none">{final ? "🏆 Final results" : "Standings"}</p>
        {final && <p className="pb-[0.8vh] font-festive text-[4vh] text-accent">Happy Diwali! शुभ दीपावली</p>}
      </div>
      <ol className="relative mt-[3vh] grid min-h-0 flex-1 auto-rows-fr gap-[1.2vh]">
        {ranked.map((t, i) => (
          <li
            key={t.id}
            className={`animate-slide-up flex items-center gap-[1.5vw] rounded-[1.5vh] px-[1.5vw] text-[3vh] ${
              i === 0 && final ? "shadow-xl" : "border border-line bg-surface"
            }`}
            style={{ animationDelay: `${i * 70}ms`, ...(i === 0 && final ? { background: t.color, color: readableOn(t.color) } : {}) }}
          >
            <span className="tabular w-[3vw] text-center font-black">{i === 0 && final ? "👑" : i + 1}</span>
            {!(i === 0 && final) && <TeamDot color={t.color} className="h-[2.4vh] w-[2.4vh]" />}
            <span className="w-[20vw] truncate font-festive">{t.name}</span>
            <span className="flex min-w-0 flex-1 gap-[0.6vw] overflow-hidden">
              {t.perks.length === 0 ? (
                <span className="opacity-60">No perks yet</span>
              ) : (
                t.perks.map((p) => (
                  <span key={p.lotId} className="truncate rounded-full bg-surface-2 px-[0.8vw] text-ink">
                    {p.emoji} {p.title}
                  </span>
                ))
              )}
            </span>
            <span className="tabular font-bold">
              {fmt(t.coinsLeft)} <span className="text-[2.2vh] opacity-70">{s.currency}</span>
            </span>
          </li>
        ))}
      </ol>
    </div>
  );
}
