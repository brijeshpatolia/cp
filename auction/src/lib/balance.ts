import { LEVEL_RANK, LEVELS_SENIOR_FIRST, type Level } from "./levels";
import type { LeaderRule } from "./settings";

export interface Person {
  id: number;
  level: Level;
  department: string;
}

type Random = () => number;

const deptKey = (department: string) => department.trim().toLowerCase();

export function shuffle<T>(items: T[], random: Random = Math.random): T[] {
  const a = [...items];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Index of the team `person` should join: fewest people of their position, then
// fewest people overall, then fewest from their department; ties broken at random.
export function pickTeamFor(person: Person, teams: Person[][], random: Random = Math.random): number {
  let best: number[] = [];
  let bestKey: number[] | null = null;
  teams.forEach((members, index) => {
    const key = [
      members.filter((m) => m.level === person.level).length,
      members.length,
      members.filter((m) => deptKey(m.department) === deptKey(person.department)).length,
    ];
    const cmp = bestKey ? key[0] - bestKey[0] || key[1] - bestKey[1] || key[2] - bestKey[2] : -1;
    if (cmp < 0) {
      bestKey = key;
      best = [index];
    } else if (cmp === 0) {
      best.push(index);
    }
  });
  return best[Math.floor(random() * best.length)];
}

// Deals people into `teamCount` teams, most senior first. Guarantees that team
// sizes differ by at most one and so do the counts of each position, and spreads
// departments. Teams that miss out on the scarce senior people fill up first on
// the next level down, which evens out seniority.
export function balanceTeams(people: Person[], teamCount: number, random: Random = Math.random): Person[][] {
  const teams: Person[][] = Array.from({ length: teamCount }, () => []);
  for (const level of LEVELS_SENIOR_FIRST) {
    for (const person of shuffle(people.filter((p) => p.level === level), random)) {
      teams[pickTeamFor(person, teams, random)].push(person);
    }
  }
  return teams;
}

export function pickLeader(members: Person[], rule: LeaderRule, random: Random = Math.random): Person | null {
  if (members.length === 0) return null;
  let pool = members;
  if (rule !== "random") {
    const ranks = members.map((m) => LEVEL_RANK[m.level]);
    const target = rule === "junior" ? Math.min(...ranks) : Math.max(...ranks);
    pool = members.filter((m) => LEVEL_RANK[m.level] === target);
  }
  return pool[Math.floor(random() * pool.length)];
}
