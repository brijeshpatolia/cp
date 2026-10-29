import { z } from "zod";

export const LEADER_RULES = ["random", "junior", "senior"] as const;
export type LeaderRule = (typeof LEADER_RULES)[number];

export const settingsSchema = z.object({
  eventName: z.string().trim().min(1).max(60),
  teamCount: z.number().int().min(2).max(12),
  startingCoins: z.number().int().min(1).max(1_000_000),
  currency: z.string().trim().min(1).max(20),
  leaderRule: z.enum(LEADER_RULES),
  antiSnipeSeconds: z.number().int().min(0).max(60),
  defaultStartPrice: z.number().int().min(1),
  defaultStep: z.number().int().min(1),
  defaultDuration: z.number().int().min(5).max(3600),
  maxPerksPerTeam: z.number().int().min(0).max(50), // 0 = no limit
  departments: z.array(z.string().trim().min(1).max(40)).max(40), // empty = free text
});

export type Settings = z.infer<typeof settingsSchema>;

export const DEFAULT_SETTINGS: Settings = {
  eventName: "Diwali Perks Auction",
  teamCount: 10,
  startingCoins: 1000,
  currency: "coins",
  leaderRule: "random",
  antiSnipeSeconds: 10,
  defaultStartPrice: 50,
  defaultStep: 10,
  defaultDuration: 45,
  maxPerksPerTeam: 0,
  departments: [],
};

// Stored settings are merged over the defaults, so new settings get sensible values
// without a migration and a bad stored value never breaks the app.
export function withDefaults(stored: unknown): Settings {
  const merged = { ...DEFAULT_SETTINGS, ...(typeof stored === "object" && stored ? stored : {}) };
  const parsed = settingsSchema.safeParse(merged);
  return parsed.success ? parsed.data : DEFAULT_SETTINGS;
}
