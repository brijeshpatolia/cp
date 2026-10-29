"use client";

import { useCallback, useEffect, useRef, useState, useSyncExternalStore } from "react";

export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public data: Record<string, unknown> = {},
  ) {
    super(message);
  }
}

export async function api<T>(path: string, body?: unknown, method = body === undefined ? "GET" : "POST"): Promise<T> {
  const res = await fetch(path, {
    method,
    headers: body === undefined ? undefined : { "Content-Type": "application/json" },
    body: body === undefined ? undefined : JSON.stringify(body),
    cache: "no-store",
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new ApiError(res.status, data.error ?? `Request failed (${res.status})`, data);
  return data as T;
}

interface Timed {
  serverTime: number;
}

// Polls a JSON endpoint on a timer. Keeps the last good data while offline, refreshes
// at once when the screen wakes up, and tracks the server's clock so countdowns agree.
export function usePoll<T extends Timed>(url: string | null, intervalMs: number) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<ApiError | null>(null);
  const [offline, setOffline] = useState(false);
  const offset = useRef(0);
  const timer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  const seq = useRef(0);

  const accept = useCallback((next: T, sentAt: number) => {
    const now = Date.now();
    offset.current = next.serverTime - (sentAt + now) / 2;
    setData(next);
    setError(null);
    setOffline(false);
  }, []);

  const refresh = useCallback(async () => {
    if (!url) return;
    clearTimeout(timer.current);
    const mine = ++seq.current;
    const sentAt = Date.now();
    try {
      const next = await api<T>(url);
      if (mine === seq.current) accept(next, sentAt);
    } catch (err) {
      if (mine !== seq.current) return;
      if (err instanceof ApiError && err.status < 500) setError(err);
      else setOffline(true);
    } finally {
      if (mine === seq.current && !document.hidden) timer.current = setTimeout(refresh, intervalMs);
    }
  }, [url, intervalMs, accept]);

  useEffect(() => {
    // Polling is a subscription to the server: start it once mounted (and on URL change).
    refresh();
    const onVisible = () => {
      if (!document.hidden) refresh();
    };
    document.addEventListener("visibilitychange", onVisible);
    window.addEventListener("online", onVisible);
    const requests = seq;
    return () => {
      requests.current++; // ignore responses still in flight
      clearTimeout(timer.current);
      document.removeEventListener("visibilitychange", onVisible);
      window.removeEventListener("online", onVisible);
    };
  }, [refresh]);

  // Lets a mutation's response (e.g. after a bid) replace the polled data immediately.
  const replace = useCallback((next: T) => accept(next, Date.now()), [accept]);
  const serverNow = useCallback(() => Date.now() + offset.current, []);

  return { data, error, offline, refresh, replace, serverNow };
}

// Re-renders every `ms` milliseconds (for countdowns).
export function useTicker(ms = 250) {
  const [, setTick] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setTick((t) => t + 1), ms);
    return () => clearInterval(id);
  }, [ms]);
}

export function formatClock(msLeft: number) {
  const total = Math.max(0, Math.ceil(msLeft / 1000));
  const m = Math.floor(total / 60);
  const s = total % 60;
  return m > 0 ? `${m}:${String(s).padStart(2, "0")}` : String(s);
}

export const fmt = (n: number) => n.toLocaleString("en-US");

// Keeps the phone screen on while mounted (leaders bidding, the big screen).
export function useWakeLock(active = true) {
  useEffect(() => {
    if (!active || !("wakeLock" in navigator)) return;
    let lock: WakeLockSentinel | null = null;
    const acquire = async () => {
      try {
        if (!document.hidden) lock = await navigator.wakeLock.request("screen");
      } catch {
        // Not allowed (battery saver, unsupported): the screen may sleep; polling catches up on wake.
      }
    };
    acquire();
    document.addEventListener("visibilitychange", acquire);
    return () => {
      document.removeEventListener("visibilitychange", acquire);
      lock?.release().catch(() => {});
    };
  }, [active]);
}

const prefListeners = new Set<() => void>();

function subscribePrefs(listener: () => void) {
  prefListeners.add(listener);
  window.addEventListener("storage", listener);
  return () => {
    prefListeners.delete(listener);
    window.removeEventListener("storage", listener);
  };
}

function readPref(key: string): string | null {
  try {
    return localStorage.getItem(key);
  } catch {
    return null; // storage blocked (private mode etc.)
  }
}

// A per-browser preference in localStorage (e.g. the big screen's theme).
export function useLocalPref<T extends string>(key: string, fallback: T): [T, (value: T) => void] {
  const value = useSyncExternalStore(
    subscribePrefs,
    () => (readPref(key) as T | null) ?? fallback,
    () => fallback,
  );
  const set = useCallback(
    (next: T) => {
      try {
        localStorage.setItem(key, next);
      } catch {
        // The preference just won't stick.
      }
      prefListeners.forEach((l) => l());
    },
    [key],
  );
  return [value, set];
}

const noSubscribe = () => () => {};

// This site's origin (for QR codes); empty during server prerendering.
export function useOrigin() {
  return useSyncExternalStore(noSubscribe, () => window.location.origin, () => "");
}

// Vibrates the phone, but only once the user has interacted with the page
// (browsers block vibration before that and log a console error).
export function buzz(pattern: number | number[]) {
  if (navigator.userActivation?.hasBeenActive) navigator.vibrate?.(pattern);
}
