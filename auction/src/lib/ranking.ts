import type { TeamView } from "./types";

// Overall standings: most perks won, then most coins left, then name.
export function rankTeams(teams: TeamView[]): TeamView[] {
  return [...teams].sort(
    (a, b) => b.perks.length - a.perks.length || b.coinsLeft - a.coinsLeft || a.name.localeCompare(b.name),
  );
}
