-- Office Auction schema.
-- Idempotent: scripts/migrate.ts runs it on every build/deploy, so every
-- statement must be safe to repeat (if not exists / or replace / guarded DO).

-- One row of global state: event phase, what the big screen shows, settings.
create table if not exists app_state (
  id             int primary key default 1 check (id = 1),
  phase          text not null default 'checkin'
                 check (phase in ('checkin', 'teams', 'auction', 'results')),
  checkin_open   boolean not null default true,
  board_scene    text not null default 'checkin'
                 check (board_scene in ('checkin', 'reveal', 'lot', 'leaderboard', 'message')),
  board_message  text not null default '',
  reveal_count   int not null default 0,
  -- Bumped whenever teams or memberships change, so phones know to refetch /api/me.
  people_version int not null default 1,
  settings       jsonb not null default '{}'::jsonb
);
insert into app_state (id) values (1) on conflict (id) do nothing;

create table if not exists teams (
  id           int generated always as identity primary key,
  name         text not null,
  color        text not null,
  table_no     int not null,
  reveal_order int not null,
  coins        int not null check (coins >= 0),
  leader_id    int
);

create table if not exists participants (
  id          int generated always as identity primary key,
  name        text not null,
  department  text not null default '',
  level       text not null check (level in ('Analyst', 'Associate', 'VP', 'Director', 'MD')),
  token_hash  text unique, -- sha256 of the phone's cookie token; null when added by an organizer
  team_id     int references teams (id) on delete set null,
  created_at  timestamptz not null default now()
);
create index if not exists participants_team_idx on participants (team_id);

do $$
begin
  alter table teams add constraint teams_leader_fk
    foreign key (leader_id) references participants (id) on delete set null;
exception when duplicate_object then null;
end $$;

-- Extra devices allowed to bid for a team (the "paddle QR" fallback).
create table if not exists paddles (
  token_hash text primary key,
  team_id    int not null references teams (id) on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists lots (
  id             int generated always as identity primary key,
  sort_order     int not null default 0,
  title          text not null,
  emoji          text not null default '🎁',
  description    text not null default '',
  mystery        boolean not null default false, -- title hidden from everyone until sold
  start_price    int not null check (start_price > 0),
  step           int not null check (step > 0),
  duration_s     int not null check (duration_s between 5 and 3600),
  status         text not null default 'queued'
                 check (status in ('queued', 'live', 'paused', 'sold', 'unsold')),
  ends_at        timestamptz,
  paused_ms_left int,
  winner_team_id int references teams (id) on delete set null,
  price          int,
  closed_at      timestamptz,
  created_at     timestamptz not null default now()
);
-- At most one lot can be live or paused at any moment.
create unique index if not exists lots_one_active on lots ((true)) where status in ('live', 'paused');

create table if not exists bids (
  id             int generated always as identity primary key,
  lot_id         int not null references lots (id) on delete cascade,
  team_id        int not null references teams (id) on delete cascade,
  participant_id int references participants (id) on delete set null,
  amount         int not null check (amount > 0),
  voided         boolean not null default false,
  created_at     timestamptz not null default clock_timestamp()
);
create index if not exists bids_lot_idx on bids (lot_id, id desc);

-- Coins a team can still spend: its budget minus what it paid for lots it won.
create or replace function team_coins_left(p_team int) returns int
language sql stable as $$
  select t.coins - coalesce((select sum(l.price) from lots l
                             where l.winner_team_id = t.id and l.status = 'sold'), 0)::int
  from teams t where t.id = p_team
$$;

-- Every bid goes through here. The lot row lock serializes simultaneous bids,
-- so each one is checked against the true current top bid.
create or replace function place_bid(
  p_lot int, p_team int, p_participant int, p_amount int,
  p_anti_snipe_s int, p_max_perks int, p_min_gap_ms int
) returns jsonb
language plpgsql as $$
declare
  l          lots%rowtype;
  top_team   int;
  top_amount int;
  min_bid    int;
  left_coins int;
  won        int;
begin
  select * into l from lots where id = p_lot for update;
  if not found then
    return jsonb_build_object('ok', false, 'error', 'not_found');
  end if;
  if l.status <> 'live' or clock_timestamp() >= l.ends_at then
    return jsonb_build_object('ok', false, 'error', 'closed');
  end if;

  select team_id, amount into top_team, top_amount
  from bids where lot_id = p_lot and not voided order by id desc limit 1;

  if top_team = p_team then
    return jsonb_build_object('ok', false, 'error', 'already_top');
  end if;

  if p_min_gap_ms > 0 and exists (
    select 1 from bids where lot_id = p_lot and team_id = p_team
      and created_at > clock_timestamp() - make_interval(secs => p_min_gap_ms / 1000.0)
  ) then
    return jsonb_build_object('ok', false, 'error', 'slow_down');
  end if;

  min_bid := coalesce(top_amount + l.step, l.start_price);
  if p_amount < min_bid then
    return jsonb_build_object('ok', false, 'error', 'too_low', 'min', min_bid);
  end if;

  left_coins := team_coins_left(p_team);
  if left_coins is null then
    return jsonb_build_object('ok', false, 'error', 'no_team');
  end if;
  if p_amount > left_coins then
    return jsonb_build_object('ok', false, 'error', 'no_coins', 'left', left_coins);
  end if;

  if p_max_perks > 0 then
    select count(*) into won from lots where winner_team_id = p_team and status = 'sold';
    if won >= p_max_perks then
      return jsonb_build_object('ok', false, 'error', 'max_perks');
    end if;
  end if;

  insert into bids (lot_id, team_id, participant_id, amount)
  values (p_lot, p_team, p_participant, p_amount);

  -- Anti-snipe: a bid in the final seconds pushes the close out again.
  if l.ends_at - clock_timestamp() < make_interval(secs => p_anti_snipe_s) then
    update lots set ends_at = clock_timestamp() + make_interval(secs => p_anti_snipe_s)
    where id = p_lot;
  end if;

  return jsonb_build_object('ok', true, 'amount', p_amount);
end $$;

-- Closes live lots whose timer has run out (or, with p_force_lot, that lot
-- right now). Called on every state read, so no background job is needed.
-- Lots locked by an in-flight bid are skipped and settled on the next read.
create or replace function settle_lots(p_force_lot int default null) returns int
language plpgsql as $$
declare
  r          record;
  top_team   int;
  top_amount int;
  n          int := 0;
begin
  for r in
    select id from lots
    where (status = 'live' and ends_at <= clock_timestamp())
       or (id = p_force_lot and status in ('live', 'paused'))
    for update skip locked
  loop
    top_team := null;
    select team_id, amount into top_team, top_amount
    from bids where lot_id = r.id and not voided order by id desc limit 1;

    update lots set
      status         = case when top_team is null then 'unsold' else 'sold' end,
      winner_team_id = top_team,
      price          = case when top_team is null then null else top_amount end,
      ends_at        = least(coalesce(ends_at, clock_timestamp()), clock_timestamp()),
      paused_ms_left = null,
      closed_at      = clock_timestamp()
    where id = r.id;
    n := n + 1;
  end loop;
  return n;
end $$;
