import { describe, expect, it } from "vitest";
import { balanceTeams, pickLeader, pickTeamFor, type Person } from "@/lib/balance";
import { LEVELS, type Level } from "@/lib/levels";

const DEPTS = ["M&A", "ECM", "DCM", "Coverage", "Research", "Ops", "Risk"];

// Deterministic PRNG so failures are reproducible.
function rng(seed: number) {
  return () => {
    seed = (seed * 1664525 + 1013904223) % 4294967296;
    return seed / 4294967296;
  };
}

function office(n: number, random: () => number): Person[] {
  const weights = [40, 30, 20, 8, 2]; // Analyst … MD
  return Array.from({ length: n }, (_, id) => {
    let r = random() * 100;
    let i = 0;
    while (r >= weights[i]) r -= weights[i++];
    return { id, level: LEVELS[Math.min(i, 4)], department: DEPTS[Math.floor(random() * DEPTS.length)] };
  });
}

const spread = (counts: number[]) => Math.max(...counts) - Math.min(...counts);

describe("balanceTeams", () => {
  it("keeps team sizes and every position within one of each other", () => {
    const random = rng(42);
    for (let run = 0; run < 2000; run++) {
      const n = 20 + Math.floor(random() * 61); // 20–80 people
      const teamCount = 2 + Math.floor(random() * 9); // 2–10 teams
      const people = office(n, random);
      const teams = balanceTeams(people, teamCount, random);

      expect(teams.flat().map((p) => p.id).sort((a, b) => a - b)).toEqual(people.map((p) => p.id));
      expect(spread(teams.map((t) => t.length))).toBeLessThanOrEqual(1);
      for (const level of LEVELS) {
        expect(spread(teams.map((t) => t.filter((p) => p.level === level).length))).toBeLessThanOrEqual(1);
      }
    }
  });

  it("spreads departments across teams", () => {
    const people: Person[] = Array.from({ length: 40 }, (_, id) => ({
      id,
      level: "Analyst",
      department: id < 10 ? "M&A" : DEPTS[id % DEPTS.length],
    }));
    const teams = balanceTeams(people, 10, rng(7));
    // Ten people from M&A over ten teams: one each.
    for (const team of teams) expect(team.filter((p) => p.department === "M&A").length).toBeLessThanOrEqual(2);
  });

  it("80 people into 10 teams gives teams of 8", () => {
    const teams = balanceTeams(office(80, rng(1)), 10, rng(2));
    expect(teams.map((t) => t.length)).toEqual(Array(10).fill(8));
  });
});

describe("pickTeamFor (late arrivals)", () => {
  it("joins the team with fewest of that position, then the smallest", () => {
    const p = (id: number, level: Level): Person => ({ id, level, department: "" });
    const teams = [[p(1, "VP"), p(2, "Analyst")], [p(3, "Analyst")], [p(4, "VP")]];
    expect(pickTeamFor(p(9, "VP"), teams, () => 0)).toBe(1);
    expect(pickTeamFor(p(9, "Analyst"), teams, () => 0)).toBe(2);
  });
});

describe("pickLeader", () => {
  const members: Person[] = [
    { id: 1, level: "Analyst", department: "" },
    { id: 2, level: "MD", department: "" },
    { id: 3, level: "VP", department: "" },
  ];
  it("follows the rule", () => {
    expect(pickLeader(members, "junior")?.id).toBe(1);
    expect(pickLeader(members, "senior")?.id).toBe(2);
    expect(members.map((m) => m.id)).toContain(pickLeader(members, "random")?.id);
    expect(pickLeader([], "random")).toBeNull();
  });
});
