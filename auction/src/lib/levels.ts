// Positions, junior → senior. Shared by server and client code.
export const LEVELS = ["Analyst", "Associate", "VP", "Director", "MD"] as const;
export type Level = (typeof LEVELS)[number];

export const LEVEL_RANK: Record<Level, number> = {
  Analyst: 0,
  Associate: 1,
  VP: 2,
  Director: 3,
  MD: 4,
};

export const LEVELS_SENIOR_FIRST: Level[] = [...LEVELS].reverse();

export function isLevel(value: unknown): value is Level {
  return typeof value === "string" && (LEVELS as readonly string[]).includes(value);
}
