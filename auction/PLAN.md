# Office Auction: Plan

A phone-first web app for an office event of up to 80 people. Everyone checks in by
scanning a QR code, the app deals them into balanced teams, each team gets the
same number of coins, and teams bid live for perks ("Unlimited work from home",
…) from their leader's phone while the big screen shows the action.

**Status:** built, with a Diwali theme (marigold toran, diyas, rangoli, fireworks,
Diwali team names). See [README.md](README.md) for running the event and deploying.
Decisions so far and the remaining open questions are at the end.

---

## 1. The event, start to finish

| Phase | Big screen (`/board`) | Everyone's phone | Organizers (`/admin`) |
|---|---|---|---|
| 0. Setup (before the day) | | | Add perks, set coins per team, number of teams, list of departments |
| 1. Check-in | Large QR code, live count ("73 checked in"), names appearing as they join | Scan QR → name, department, position → "You're in! Teams soon" | Watch the list, fix typos, add people who have no phone |
| 2. Teams | Reveal one team at a time: name, colour, table, members, 👑 leader | "You're on **The Bulls**: Table 4, leader Priya" | Generate → check balance → reshuffle/edit → lock → Announce |
| 3. Auction | Current perk, top bid and team, countdown, recent bids, every team's coins left | Leader: bidding paddle. Everyone else: what's on the block and the team's coins | Start lot, pause, +15 s, undo bid, close, next |
| 4. Results | Who won what, coins left, overall winner | Team's winnings | Export CSV, reset |

## 2. Screens

### Check-in (`/join`, opened from the QR code)
- Fields: **name**, **department** (dropdown the organizers set, plus "Other"),
  **position** (Analyst, Associate, VP, Director, MD).
- The phone remembers the person through a secure cookie, so a refresh or a
  second scan doesn't create a duplicate. People can fix their details until
  the teams are locked.
- People who arrive after teams are made go into the team that keeps the
  balance best, and their phone shows that team straight away.

### Phone after the teams are announced
- Team card: team name and colour, table number, members with positions, leader marked.
- During the auction: the perk on the block, the top bid and who holds it, the
  team's coins left, and the perks won so far ("Watch the big screen!").

### Leader's phone = the team's bidding paddle
- Same as above, plus big bid buttons: **+1 step**, **+2 steps**, **+5 steps**,
  and a custom amount.
- Clear status: **You're winning** (green), **Outbid!** (red, phone vibrates),
  **Not enough coins**.
- The screen stays awake while bidding (Wake Lock API).
- If the leader's phone dies, the admin shows a **paddle QR** for that team, and
  any phone that scans it becomes the team's paddle. The admin can also switch the leader.

### Big screen (`/board`)
Full screen, 16:9, readable from the back of the room. The admin picks which scene is showing:
1. **Check-in:** QR code, URL, live counter, recent names, count per position.
2. **Team reveal:** one team at a time (admin taps Next) with a short animation, then a grid of all teams.
3. **Live lot:** perk title, emoji and description; the top bid in large type in the
   leading team's colour; countdown ring with "Going once… going twice…" in the
   final seconds; recent bids; a coin bar for every team; **SOLD!** with confetti
   and a gavel sound.
4. **Leaderboard / results:** perks per team, coins left.
5. **Message:** any text the admin types ("Break, back in 10").

### Admin (`/admin`, password)
- **Dashboard:** phase controls, counts by position and department, board scene picker.
- **People:** search, edit, delete, add manually, move to another team, make leader.
- **Teams:** generate (choose the number of teams), balance table (positions × teams),
  reshuffle, rename, change colour or table, adjust coins (bonus or penalty for
  fun challenges), lock, announce.
- **Perks (lots):** add, edit, reorder: title, emoji/image, description, starting bid, step, timer.
- **Auction console:** start lot, pause/resume, +15 s, undo last bid, close now,
  re-run an unsold lot, live bid log.
- **Export:** CSV of people, teams and results. **Reset** for rehearsals and after the event.

## 3. Balanced teams

Goal: every team gets a fair spread of seniority, teams are the same size (±1),
and departments are mixed.

1. Organizers pick the number of teams (up to 10 by default; 80 people → 10 teams of 8).
2. Go through people from most senior to most junior (MD → Director → VP →
   Associate → Analyst), in random order within each position.
3. Put each person in the team that has, in this order of priority:
   1. the fewest people of that position,
   2. the fewest people overall,
   3. the fewest people from the same department,

   with ties broken at random.

What this guarantees:
- For each position, team counts differ by at most 1.
- Team sizes differ by at most 1.
- Departments are spread out.
- Teams that don't get one of the few MDs get Directors first, because they are
  smaller at that point. Senior weight evens out on its own.

Before announcing, the admin sees a positions × teams table and can reshuffle or move people by hand.

**Leader:** picked automatically for each team using a rule the organizers
choose (random, most junior or most senior; default random). It can be re-rolled per
team or set by hand. With up to 10 teams there are up to 10 leaders.

**Team names:** assigned from a Diwali list (Diya Squad, Rangoli Rebels, Laddoo
Legends, Anaar Army, Kandil Crew, Chakri Champs, Phuljhadi Force, Toran Titans, Rocket
Riders, Kaju Katli Kings, …), each with a colour and table number. All of them are
editable.

## 4. Auction rules (defaults; all adjustable)

- Every team starts with the same coins (default 1,000). The admin can give
  bonuses or penalties.
- One perk at a time. The opening bid must be at least the starting price; each
  later bid must be at least the top bid plus the step.
- Only the team's paddle (the leader's phone) can bid. A team can't outbid itself
  and can't bid more than the coins it has left.
- Timer per lot (default 45 s). **Anti-snipe:** a bid in the last 10 s resets the
  clock to 10 s, so a last-second bid can't steal a lot.
- When the timer reaches zero the lot goes to the top bid (or stays unsold if
  there were no bids), and the price comes off that team's coins. The admin can
  pause, add time, undo a mistaken bid, close early or re-run a lot.
- Optional twists for the organizers to choose from: a mystery lot (perk hidden
  until sold), a maximum number of perks per team, bonus coins for
  mini-challenges, power-up cards.

## 5. Architecture (built for Vercel)

```
 phones / big screen / admin ──HTTPS──▶ Next.js on Vercel (pages + API routes)
                                                  │
                                                  ▼
                                    Supabase Postgres (free plan)
                                    tables + one place_bid() function
```

- **Next.js (App Router, TypeScript) on Vercel** serves every page and the API.
- **Supabase Postgres** holds participants, teams, lots, bids and settings. Its
  table editor also works as an emergency admin tool on the day.
- **Every bid goes through one Postgres function** (`place_bid`). In a single
  transaction it locks the lot row, checks every rule, records the bid and
  extends the timer. If two leaders tap at the same instant, the bids are
  processed one after the other and the second one gets "Outbid: the minimum is
  now X". No team can overspend and no bid is lost.
- **Time** comes only from the database clock. Every refresh carries the server
  time, and each screen corrects for its own clock drift, so all countdowns show
  the same value.

### How screens stay live (and why not websockets)

Vercel Functions can't keep websocket connections open, so live updates need
either a separate realtime service or polling. Supabase Realtime's free plan
allows **100 messages per second** and counts one message **per receiving
screen**. One bid pushed to ~85 screens is ~86 messages, so two bids in the same second
are over the cap, and connections over the cap get dropped. Paid plans raise the limit,
but at this size polling is simpler, works through corporate firewalls and costs nothing:

| Screen | Refreshes | Delay |
|---|---|---|
| Big screen | every 0.5 s | ≤ 0.5 s |
| Admin console, up to 10 leader phones | every 1 s | ≤ 1 s (a leader's own bid shows instantly) |
| ~70 other phones | every 3 s, from Vercel's CDN cache (2 s) | ≤ 5 s (they're watching the big screen anyway) |

Each refresh is a small JSON response (< 2 KB) that includes a `version`
number. A phone fetches its personal data (team, leader status) again only when
`version` changes. Phones also refresh straight away when they wake from sleep.

If the big screen feels slow in rehearsal, Supabase Realtime can be added for
the big screen alone. That's only a handful of listeners, far inside the free cap.

### Load math for 80 people

- Check-in burst: ~80 inserts over a few minutes, which is trivial (the simulation
  checks in 80 phones in the same second).
- ~70 phones refreshing every 3 s ≈ 23 requests/s. Vercel's CDN cache answers
  almost all of them, so the function behind it runs about once every 2 s.
- Big screen, admin and leaders ≈ 13 requests/s to functions, each a single indexed query.
- A 3-hour event ≈ 150k function calls. Vercel Hobby includes 1,000,000 a month
  and 4 hours of active CPU, and each call uses a few milliseconds.
- Supabase Realtime isn't used, so none of its message caps apply. The database
  handles a few queries per second.

### Security

- **Participants** have no passwords. An unguessable token in an httpOnly cookie
  identifies each phone. Bidding needs the token of the team's paddle, so a
  non-leader can't bid even by calling the API directly.
- **Admin** uses one organizer password (a Vercel environment variable), a signed
  session cookie and rate-limited login attempts.
- The Supabase service key stays on the server; browsers never talk to the database directly.
- The API keeps team assignments hidden until the admin announces them, so nobody can spoil the reveal.
- Each paddle is rate-limited (for example one bid per 0.5 s) to absorb double taps.

## 6. Data model (Postgres)

```
event         phase, board_scene, version, settings (team count, coins, timers, step,
              leader rule, currency name, departments)
participants  id, name, department, level, device_token_hash, team_id, created_at
teams         id, name, colour, table_no, coins, leader_id
paddles       token_hash, team_id, created_at        -- devices allowed to bid for a team
lots          id, sort_order, title, emoji, description, start_price, step, duration_s,
              status (queued | live | paused | sold | unsold), ends_at, paused_ms_left,
              winner_team_id, price
bids          id, lot_id, team_id, participant_id, amount, created_at, voided
```

Coins left = team coins − total price of lots won.

## 7. Build steps (each ends in something to try on a phone)

1. **Skeleton and check-in:** Next.js app in `auction/`, Supabase schema, Vercel
   deploy, QR check-in, admin login, people list.
2. **Teams:** balancing algorithm (unit-tested); preview, reshuffle, edit and lock;
   announce, with the reveal on the big screen and a "your team" phone screen;
   leader selection; paddle QR.
3. **Auction:** lot editor, `place_bid` and the lot lifecycle, leader paddle,
   live big-screen scene, admin console.
4. **Polish and proof:** animations, sounds, confetti, results, CSV export, and a
   load-test script run against the deployed site (80 fake phones checking in,
   10 bots bidding as fast as the rules allow) that checks no team ever
   overspends and the top bid always wins.

## 8. Accounts and setup

- A free **Supabase** project in the region nearest the office. Run the SQL file
  from this repo in its SQL editor.
- A **Vercel** project linked to this GitHub repo, with **Root Directory =
  `auction`** and these environment variables: Supabase URL and service key,
  `ADMIN_PASSWORD`, `SESSION_SECRET`.
- Put Vercel Functions in the same region as Supabase.
- Vercel's free Hobby plan is for non-commercial personal use. If the company
  wants the app on a company account, that needs Pro.

## 9. Event-day checklist

- **A week before:** full rehearsal with 5–10 organizers' phones on the office
  Wi-Fi (corporate networks sometimes block new sites, so check early); a
  load-test run; reset the data.
- **Day before:** open the Supabase dashboard (free projects pause after a week
  without activity); enter the final perks and coins; print QR posters for the
  entrance and each table.
- **On the day:** big-screen laptop on mains power with sleep turned off and the
  browser full screen on `/board`; admin on a second device; a few spare phones
  for paddle QRs; an organizer at the door to add people who have no phone.
- **After:** export the CSV, then reset to delete everyone's data.

## 10. Decisions

Decided:
- Up to 80 people and at most 10 teams, so up to 10 leaders (default 10 teams of 8).
- Defaults, all changeable in **Settings**: leader picked at random; 1,000 coins per
  team; "team" on the check-in form means the person's department, and the new teams
  mix departments; overall winner = most perks, then most coins left.

Still open (each one is a setting, so the app doesn't wait on them):
1. How is the overall winner decided: most perks won, best value, or a judges'
   "most fun" vote? Do you want fun twists (mystery perks are built in; bonus coins
   can be given by editing a team's coins)?
2. Leader rule: random, most junior or most senior?
3. Coins per team, currency name, list of perks, default timer and step.
4. Event date, which sets the rehearsal timeline.
