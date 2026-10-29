"use client";

// Tiny synthesized sound effects for the big screen (no audio files to host).
// Browsers only allow audio after a click, so the board starts muted.
let ctx: AudioContext | null = null;

function audio() {
  ctx ??= new AudioContext();
  if (ctx.state === "suspended") void ctx.resume();
  return ctx;
}

function tone(freq: number, start: number, duration: number, gain: number, type: OscillatorType = "sine") {
  const a = audio();
  const osc = a.createOscillator();
  const env = a.createGain();
  osc.type = type;
  osc.frequency.setValueAtTime(freq, a.currentTime + start);
  env.gain.setValueAtTime(0.0001, a.currentTime + start);
  env.gain.exponentialRampToValueAtTime(gain, a.currentTime + start + 0.01);
  env.gain.exponentialRampToValueAtTime(0.0001, a.currentTime + start + duration);
  osc.connect(env).connect(a.destination);
  osc.start(a.currentTime + start);
  osc.stop(a.currentTime + start + duration + 0.05);
}

export const sounds = {
  unlock: () => audio(),
  bid: () => {
    tone(880, 0, 0.12, 0.25, "triangle");
    tone(1320, 0.06, 0.12, 0.18, "triangle");
  },
  tick: () => tone(1000, 0, 0.05, 0.12, "square"),
  gavel: () => {
    tone(110, 0, 0.25, 0.9, "triangle");
    tone(90, 0.28, 0.35, 0.9, "triangle");
    bell(0.45);
  },
  bell: () => bell(0),
};

// A temple-bell (ghanti) chime: a few inharmonic partials with a long ring.
function bell(start: number) {
  for (const [freq, gain] of [
    [659, 0.22],
    [1319, 0.12],
    [1760, 0.08],
    [2489, 0.05],
  ] as const) {
    tone(freq, start, 2.2, gain, "sine");
  }
}
