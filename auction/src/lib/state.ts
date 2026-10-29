// Loads rows from Postgres and shapes them into the views the screens poll.
import { db, type Sql } from "./db";
import { LEVELS, type Level } from "./levels";
import { hashToken } from "./session";
import { withDefaults, type Settings } from "./settings";
import type {
  AdminOverview,
  BoardScene,
  BidView,
  LotStatus,
  LotSummary,
  LotView,
  MeState,
  MemberView,
  Phase,
  PublicState,
  TeamView,
} from "./types";

export interface AppState {
  phase: Phase;
  checkinOpen: boolean;
  boardScene: BoardScene;
  boardMessage: string;
  revealCount: number;
  peopleVersion: number;
  settings: Settings;
}

interface AppRow {
  phase: Phase;
  checkin_open: boolean;
  board_scene: BoardScene;
  board_message: string;
  reveal_count: number;
  people_version: number;
  settings: unknown;
}

export interface TeamRow {
  id: number;
  name: string;
  color: string;
  table_no: number;
  reveal_order: number;
  coins: number;
  leader_id: number | null;
}

export interface MemberRow {
  id: number;
  name: string;
  department: string;
  level: Level;
  team_id: number | null;
}

export interface LotRow {
  id: number;
  sort_order: number;
  title: string;
  emoji: string;
  description: string;
  mystery: boolean;
  start_price: number;
  step: number;
  duration_s: number;
  status: LotStatus;
  ends_at: Date | null;
  paused_ms_left: number | null;
  winner_team_id: number | null;
  price: number | null;
  closed_at: Date | null;
}

interface BidRow {
  id: number;
  team_id: number;
  amount: number;
  voided: boolean;
  created_at: Date;
  by: string | null;
}

const ms = (d: Date | null) => (d ? d.getTime() : null);

export async function loadApp(sql: Sql, { lock = false } = {}): Promise<AppState> {
  const [row] = await sql<AppRow[]>`
    select phase, checkin_open, board_scene, board_message, reveal_count, people_version, settings
    from app_state where id = 1 ${lock ? sql`for update` : sql``}`;
  return {
    phase: row.phase,
    checkinOpen: row.checkin_open,
    boardScene: row.board_scene,
    boardMessage: row.board_message,
    revealCount: row.reveal_count,
    peopleVersion: row.people_version,
    settings: withDefaults(row.settings),
  };
}

export const loadTeams = (sql: Sql) => sql<TeamRow[]>`
  select id, name, color, table_no, reveal_order, coins, leader_id from teams order by table_no, id`;

export const loadMembers = (sql: Sql) => sql<MemberRow[]>`
  select id, name, department, level, team_id from participants order by name, id`;

export const loadLots = (sql: Sql) => sql<LotRow[]>`
  select id, sort_order, title, emoji, description, mystery, start_price, step, duration_s, status,
         ends_at, paused_ms_left, winner_team_id, price, closed_at
  from lots order by sort_order, id`;

export function teamVisible(app: Pick<AppState, "phase" | "revealCount">, team: Pick<TeamRow, "reveal_order">) {
  if (app.phase === "checkin") return false;
  if (app.phase === "teams") return team.reveal_order <= app.revealCount;
  return true;
}

// The lot the room is looking at: the running one, else the one that closed last.
export function currentLot(lots: LotRow[]): LotRow | null {
  const active = lots.find((l) => l.status === "live" || l.status === "paused");
  if (active) return active;
  const closed = lots.filter((l) => l.closed_at && (l.status === "sold" || l.status === "unsold"));
  closed.sort((a, b) => ms(b.closed_at)! - ms(a.closed_at)!);
  return closed[0] ?? null;
}

const isClosed = (status: LotStatus) => status === "sold" || status === "unsold";

// Mystery lots stay hidden from the room until the hammer falls.
function publicFace(lot: LotRow) {
  if (lot.mystery && !isClosed(lot.status)) {
    return { title: "Mystery perk", emoji: "❓", description: "Revealed when the hammer falls" };
  }
  return { title: lot.title, emoji: lot.emoji, description: lot.description };
}

export function toLotSummary(lot: LotRow, reveal: boolean): LotSummary {
  const face = reveal ? lot : publicFace(lot);
  return {
    id: lot.id,
    title: face.title,
    emoji: face.emoji,
    status: lot.status,
    winnerTeamId: lot.winner_team_id,
    price: lot.price,
  };
}

export function toLotView(lot: LotRow, bids: BidRow[], reveal: boolean): LotView {
  const live = bids.filter((b) => !b.voided);
  const top = live[0] ?? null; // newest valid bid is always the highest
  const face = reveal ? lot : publicFace(lot);
  return {
    id: lot.id,
    title: face.title,
    emoji: face.emoji,
    description: face.description,
    mystery: lot.mystery,
    status: lot.status,
    startPrice: lot.start_price,
    step: lot.step,
    durationS: lot.duration_s,
    endsAt: ms(lot.ends_at),
    pausedMsLeft: lot.paused_ms_left,
    minNext: top ? top.amount + lot.step : lot.start_price,
    top: top ? { teamId: top.team_id, amount: top.amount } : null,
    bids: live.slice(0, 8).map((b): BidView => ({ id: b.id, teamId: b.team_id, amount: b.amount, at: b.created_at.getTime() })),
    winnerTeamId: lot.winner_team_id,
    price: lot.price,
  };
}

export function coinsLeft(team: TeamRow, lots: LotRow[]) {
  const spent = lots
    .filter((l) => l.status === "sold" && l.winner_team_id === team.id)
    .reduce((sum, l) => sum + (l.price ?? 0), 0);
  return team.coins - spent;
}

export function buildTeamView(team: TeamRow, members: MemberRow[], lots: LotRow[]): TeamView {
  const own = members.filter((m) => m.team_id === team.id);
  const view = (m: MemberRow): MemberView => ({ id: m.id, name: m.name, level: m.level });
  const leader = own.find((m) => m.id === team.leader_id);
  return {
    id: team.id,
    name: team.name,
    color: team.color,
    tableNo: team.table_no,
    revealOrder: team.reveal_order,
    coins: team.coins,
    coinsLeft: coinsLeft(team, lots),
    leader: leader ? view(leader) : null,
    members: own.map(view),
    perks: lots
      .filter((l) => l.status === "sold" && l.winner_team_id === team.id)
      .map((l) => ({ lotId: l.id, title: l.title, emoji: l.emoji, price: l.price ?? 0 })),
  };
}

async function loadBids(sql: Sql, lotId: number, limit: number) {
  return sql<BidRow[]>`
    select b.id, b.team_id, b.amount, b.voided, b.created_at, p.name as by
    from bids b left join participants p on p.id = b.participant_id
    where b.lot_id = ${lotId} order by b.id desc limit ${limit}`;
}

export async function getPublicState(): Promise<PublicState> {
  const sql = db();
  await sql`select settle_lots()`;
  const [app, teams, members, lots, levelCounts, recent] = await Promise.all([
    loadApp(sql),
    loadTeams(sql),
    loadMembers(sql),
    loadLots(sql),
    sql<{ level: Level; n: number }[]>`select level, count(*)::int as n from participants group by level`,
    sql<{ id: number; name: string; level: Level }[]>`
      select id, name, level from participants order by id desc limit 12`,
  ]);
  const lot = currentLot(lots);
  const bids = lot ? await loadBids(sql, lot.id, 30) : [];
  const byLevel = Object.fromEntries(LEVELS.map((l) => [l, 0])) as Record<Level, number>;
  for (const row of levelCounts) byLevel[row.level] = row.n;

  return {
    serverTime: Date.now(),
    eventName: app.settings.eventName,
    currency: app.settings.currency,
    phase: app.phase,
    checkinOpen: app.checkinOpen,
    board: { scene: app.boardScene, message: app.boardMessage },
    revealCount: app.revealCount,
    teamCount: teams.length,
    peopleVersion: app.peopleVersion,
    antiSnipeSeconds: app.settings.antiSnipeSeconds,
    stats: { registered: Object.values(byLevel).reduce((a, b) => a + b, 0), byLevel, recent },
    teams: teams.filter((t) => teamVisible(app, t)).map((t) => buildTeamView(t, members, lots)),
    lot: lot ? toLotView(lot, bids, false) : null,
    nextLot: (() => {
      const next = lots.find((l) => l.status === "queued");
      return next ? toLotSummary(next, false) : null;
    })(),
    lots: lots.map((l) => toLotSummary(l, false)),
  };
}

export interface DeviceTokens {
  participant?: string;
  paddle?: string;
}

// Who this device is: the participant behind its cookie, and the team it may bid for.
export async function resolveDevice(sql: Sql, tokens: DeviceTokens) {
  const [participant] = tokens.participant
    ? await sql<(MemberRow & { is_leader: boolean })[]>`
        select p.id, p.name, p.department, p.level, p.team_id, coalesce(t.leader_id = p.id, false) as is_leader
        from participants p left join teams t on t.id = p.team_id
        where p.token_hash = ${hashToken(tokens.participant)}`
    : [];
  const [paddle] = tokens.paddle
    ? await sql<{ team_id: number }[]>`select team_id from paddles where token_hash = ${hashToken(tokens.paddle)}`
    : [];
  const bidTeamId = paddle?.team_id ?? (participant?.is_leader ? participant.team_id : null);
  return { participant: participant ?? null, bidTeamId: bidTeamId ?? null, viaPaddle: Boolean(paddle) };
}

export async function getMeState(tokens: DeviceTokens): Promise<MeState> {
  const sql = db();
  const [app, device, teams, members, lots] = await Promise.all([
    loadApp(sql),
    resolveDevice(sql, tokens),
    loadTeams(sql),
    loadMembers(sql),
    loadLots(sql),
  ]);
  const teamView = (id: number | null, revealed = true) => {
    const team = teams.find((t) => t.id === id);
    return team && (revealed || teamVisible(app, team)) ? buildTeamView(team, members, lots) : null;
  };
  const visibleTeam = (id: number | null) => teamView(id, false);
  const { participant } = device;
  const team = visibleTeam(participant?.team_id ?? null);
  return {
    serverTime: Date.now(),
    eventName: app.settings.eventName,
    currency: app.settings.currency,
    participant: participant
      ? { id: participant.id, name: participant.name, department: participant.department, level: participant.level }
      : null,
    team,
    isLeader: Boolean(team && participant?.is_leader),
    // A paddle QR comes from an organizer, so that phone may see its team before the reveal.
    bidTeam: device.viaPaddle ? teamView(device.bidTeamId) : visibleTeam(device.bidTeamId),
    checkinOpen: app.checkinOpen,
    canChangeLevel: !participant?.team_id,
    departments: app.settings.departments,
    peopleVersion: app.peopleVersion,
  };
}

export async function getAdminOverview(): Promise<AdminOverview> {
  const sql = db();
  await sql`select settle_lots()`;
  const [app, teams, lots, participants, paddles, bidCounts] = await Promise.all([
    loadApp(sql),
    loadTeams(sql),
    loadLots(sql),
    sql<(MemberRow & { has_device: boolean; created_at: Date })[]>`
      select id, name, department, level, team_id, token_hash is not null as has_device, created_at
      from participants order by id`,
    sql<{ team_id: number; n: number }[]>`select team_id, count(*)::int as n from paddles group by team_id`,
    sql<{ lot_id: number; n: number }[]>`select lot_id, count(*)::int as n from bids where not voided group by lot_id`,
  ]);
  const lot = currentLot(lots);
  const bids = lot ? await loadBids(sql, lot.id, 200) : [];
  return {
    serverTime: Date.now(),
    settings: app.settings,
    phase: app.phase,
    checkinOpen: app.checkinOpen,
    board: { scene: app.boardScene, message: app.boardMessage },
    revealCount: app.revealCount,
    participants: participants.map((p) => ({
      id: p.id,
      name: p.name,
      department: p.department,
      level: p.level,
      teamId: p.team_id,
      hasDevice: p.has_device,
      createdAt: p.created_at.getTime(),
    })),
    teams: teams.map((t) => ({
      id: t.id,
      name: t.name,
      color: t.color,
      tableNo: t.table_no,
      revealOrder: t.reveal_order,
      coins: t.coins,
      coinsLeft: coinsLeft(t, lots),
      leaderId: t.leader_id,
      paddles: paddles.find((p) => p.team_id === t.id)?.n ?? 0,
    })),
    lots: lots.map((l) => ({
      ...toLotView(l, l.id === lot?.id ? bids : [], true),
      sortOrder: l.sort_order,
      bidCount: bidCounts.find((b) => b.lot_id === l.id)?.n ?? 0,
    })),
    currentLotId: lot?.id ?? null,
    bids: bids.map((b) => ({ id: b.id, teamId: b.team_id, amount: b.amount, at: b.created_at.getTime(), voided: b.voided, by: b.by })),
  };
}
