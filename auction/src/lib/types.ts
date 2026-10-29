// JSON shapes returned by the API, shared by server and client code.
import type { Level } from "./levels";
import type { Settings } from "./settings";

export const PHASES = ["checkin", "teams", "auction", "results"] as const;
export type Phase = (typeof PHASES)[number];

export const BOARD_SCENES = ["checkin", "reveal", "lot", "leaderboard", "message"] as const;
export type BoardScene = (typeof BOARD_SCENES)[number];

export type LotStatus = "queued" | "live" | "paused" | "sold" | "unsold";

export interface MemberView {
  id: number;
  name: string;
  level: Level;
}

export interface PerkView {
  lotId: number;
  title: string;
  emoji: string;
  price: number;
}

export interface TeamView {
  id: number;
  name: string;
  color: string;
  tableNo: number;
  revealOrder: number;
  coins: number;
  coinsLeft: number;
  leader: MemberView | null;
  members: MemberView[];
  perks: PerkView[];
}

export interface BidView {
  id: number;
  teamId: number;
  amount: number;
  at: number;
}

export interface LotView {
  id: number;
  title: string;
  emoji: string;
  description: string;
  mystery: boolean;
  status: LotStatus;
  startPrice: number;
  step: number;
  durationS: number;
  endsAt: number | null;
  pausedMsLeft: number | null;
  minNext: number;
  top: { teamId: number; amount: number } | null;
  bids: BidView[];
  winnerTeamId: number | null;
  price: number | null;
}

export interface LotSummary {
  id: number;
  title: string;
  emoji: string;
  status: LotStatus;
  winnerTeamId: number | null;
  price: number | null;
}

export interface PublicState {
  serverTime: number;
  eventName: string;
  currency: string;
  phase: Phase;
  checkinOpen: boolean;
  board: { scene: BoardScene; message: string };
  revealCount: number;
  teamCount: number;
  peopleVersion: number;
  antiSnipeSeconds: number;
  stats: {
    registered: number;
    byLevel: Record<Level, number>;
    recent: { id: number; name: string; level: Level }[];
  };
  teams: TeamView[]; // only teams that have been revealed
  lot: LotView | null; // the live/paused lot, else the most recently closed one
  nextLot: LotSummary | null;
  lots: LotSummary[];
}

export interface MeState {
  serverTime: number;
  eventName: string;
  currency: string;
  participant: { id: number; name: string; department: string; level: Level } | null;
  team: TeamView | null; // null until the participant's team is revealed
  isLeader: boolean;
  bidTeam: TeamView | null; // team this device bids for (as leader or via paddle QR)
  checkinOpen: boolean;
  canChangeLevel: boolean;
  departments: string[];
  peopleVersion: number;
}

export interface AdminParticipant {
  id: number;
  name: string;
  department: string;
  level: Level;
  teamId: number | null;
  hasDevice: boolean;
  createdAt: number;
}

export interface AdminTeam {
  id: number;
  name: string;
  color: string;
  tableNo: number;
  revealOrder: number;
  coins: number;
  coinsLeft: number;
  leaderId: number | null;
  paddles: number;
}

export interface AdminLot extends LotView {
  sortOrder: number;
  bidCount: number;
}

export interface AdminBid {
  id: number;
  teamId: number;
  amount: number;
  at: number;
  voided: boolean;
  by: string | null;
}

export interface AdminOverview {
  serverTime: number;
  settings: Settings;
  phase: Phase;
  checkinOpen: boolean;
  board: { scene: BoardScene; message: string };
  revealCount: number;
  participants: AdminParticipant[];
  teams: AdminTeam[];
  lots: AdminLot[];
  currentLotId: number | null;
  bids: AdminBid[]; // all bids on the current lot, newest first, including undone ones
}
