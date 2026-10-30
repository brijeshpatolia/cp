# Office Auction

A phone-first web app for an office event of up to ~80 people. Everyone checks in by
scanning a QR code, the app deals them into balanced teams (mixing Analysts, Associates,
VPs, Directors and MDs, and departments), each team gets the same coins, and team leaders
bid for perks ("Unlimited work from home", …) from their phones while the big screen
shows the action.

| Page | Who | What |
| --- | --- | --- |
| `/` | Everyone (the QR code points here) | Check in, see your team, follow the auction. Leaders get the bid buttons. |
| `/board` | The projector / TV | Check-in QR and counter, team reveal, live perk with countdown, SOLD!, standings |
| `/admin` | Organizers (password) | People, teams, perks, the live auction console, settings, CSV export, reset |

It's dressed for Diwali: a marigold toran across the top, flickering diyas, rangoli,
शुभ दीपावली lettering, Diwali team names (Diya Squad, Rangoli Rebels, Anaar Army…),
fireworks on every SOLD and at the final results, and a temple-bell chime. The big screen
has a light **festive day** theme (default, best on a projector) and a **Diwali night**
theme (the ☾ button, best on a TV); phones follow their own light/dark setting.

The design and the reasoning behind it are in [PLAN.md](PLAN.md).

## Running the event

**Before the day** (in `/admin`)
1. **Perks** tab: add the perks in running order (there are one-click ideas). Tick
   *Mystery perk* to hide a perk's name until it's sold.
2. **Settings** tab: event name, coins per team (rename the currency too, e.g. "laddoos"),
   who becomes leader (random, most junior or most senior), timer defaults, and optionally
   a fixed list of departments for the check-in form.
3. Rehearse with a few phones on the office Wi-Fi, then **Settings → Reset everything**.

**On the day**
1. **Check-in:** open `/board` on the projector laptop, click ⛶ for full screen and 🔇 to
   turn sound on (the buttons sit faintly in the top-right corner). People scan the QR and check in; the counter climbs. Anyone without a
   phone: **People → Add**.
2. **Teams:** **Teams → Generate teams** (default 10), check the balance table, reshuffle
   if you like. Then **Live → 2. Teams** and press **Reveal next team** once per team: each
   team appears on the big screen and on its members' phones at the same moment.
3. **Auction:** **Live → Start next**. Leaders bid from their phones; the big screen shows
   the top bid, countdown and every team's coins. A bid in the last 10 s puts the clock
   back to 10 s. At zero the perk is sold automatically. You can **Pause**, add **+15 s**,
   **Undo last bid**, or **Sell now**.
4. **Results:** **Live → 4. Results** shows the final standings (most perks, then most
   coins left). **Settings → Export** gives CSVs.

**The big screen**
- The board scales to any screen. It has been checked at 1080p and 4K TVs, a 16:10 laptop
  mirrored to a screen, a 4:3 projector and an ultrawide, with prices up to 10,000.
- Open `/board` in Chrome on the laptop connected to the screen. If the laptop *extends*
  its display, drag the window onto the big screen first, then click ⛶ (or press F11).
- Projector on a whiteboard: keep the default light theme. TV: the ☾ "Diwali night"
  theme looks best.
- Keep the laptop on mains power. The board asks the browser to keep the screen awake,
  but turn off the laptop's own sleep timer too.

**If something goes wrong**
- *A leader's phone dies:* **Teams → Paddle QR** for that team, and scan it with any
  phone; that phone can now bid for the team. Or pick a different leader in the dropdown.
- *A mistaken bid:* **Live → Undo last bid** (while the perk is running), or
  **Re-auction** afterwards.
- *Someone checked in twice:* **People → Remove** one of them.
- *The big screen shows the wrong thing:* **Live → Big screen shows** switches scenes, or
  shows any message you type.

## Deploying (Vercel + Supabase, about 15 minutes)

Vercel builds from GitHub, and its production site (the URL everyone uses) is built from
`main`. Preview deployments of other branches ask visitors to log in to Vercel, so they
won't work for phones at the event. Make sure this code is on `main` before you start.

1. **Import the project.** On [vercel.com](https://vercel.com) (sign up with GitHub),
   choose **Add New → Project** and import this repository.
   - **Root Directory:** click **Edit** and choose `auction`. The framework shows as
     Next.js; leave the build settings alone.
   - **Environment Variables:** add `ADMIN_PASSWORD` (the organizers' password) and
     `SESSION_SECRET` (any long random string, e.g. from `openssl rand -hex 32`).
   - Click **Deploy**. The first build succeeds without a database. The site isn't usable
     yet; the next steps add the database.
2. **Add the database.** In the new project, open **Storage → Create Database → Supabase**
   (free plan). Pick the region nearest the office (for India: Mumbai), leave the
   environment-variable prefix empty, and connect it to the project. This sets
   `POSTGRES_URL` and friends for you; the app reads them as they are.
3. **Match the regions.** In **Settings → Functions → Function Region**, choose the same
   region as the database (Mumbai is `bom1`). Every request talks to the database
   several times, so this matters.
4. **Redeploy.** In **Deployments**, open the latest one, choose **⋯ → Redeploy**. This
   build creates the database tables (`scripts/migrate.ts` runs before `next build`), and
   every later deploy keeps them up to date.
5. **Check it.** Open `https://<your-project>.vercel.app/api/health`. It should say
   `"ok": true`, with `dbLatencyMs` in single or low double digits. Otherwise `problem`
   says what's missing, and `hint` says which Function Region to pick if the app and
   the database are in different regions. Then log in at `/admin`.
6. **Load test** before setting up for real (it wipes the event data):

   ```bash
   cd auction && npm install
   ADMIN_PASSWORD=... npm run simulate -- --url https://<your-project>.vercel.app --yes
   ```

   This checks in 80 fake phones at once, makes 10 teams, has every leader bid as fast as
   the rules allow while the other phones poll like real ones, checks that the results
   are consistent, prints latencies, and resets. Add `--keep` to look at the result in
   `/admin` and `/board` first.

You can also skip the Storage tab: create the project at [supabase.com](https://supabase.com),
open **Connect**, copy the **Transaction pooler** connection string (port 6543) and add it
as `DATABASE_URL`. A [Neon](https://neon.tech) database from the Storage tab works too.

Free Supabase projects pause after about a week without activity, so open the dashboard
the day before the event. Vercel's free Hobby plan is meant for non-commercial personal
use; if the company wants this on a company account, that's the Pro plan.

## How it copes with 80 phones

Vercel Functions can't hold open websocket connections, and a hosted realtime service's
free tier counts every message delivered to every phone, so screens poll instead:

| Screen | Polls | Notes |
| --- | --- | --- |
| Big screen | every 0.5 s | |
| Leaders' phones, admin | every 1 s | a leader's own bid shows instantly |
| Everyone else | every 3 s | `/api/state?cdn=1` is cached by Vercel's CDN for 2 s, so these barely reach the database |

Every bid runs through one Postgres function (`place_bid` in `db/schema.sql`) that locks
the perk's row, checks all the rules and records the bid in one transaction, so
simultaneous bids are handled one after another and no team can overspend. The clock is
the database's; perks are sold by whichever request first notices the timer ran out, so
no background job is needed.

Supabase's connection pooler needs some care. Reads and bids, single statements, go
through its transaction mode (port 6543), one query at a time per connection, because it
stops answering a connection that sends a query before the previous one has answered
([supavisor#1239](https://github.com/supabase/supavisor/issues/1239)). Check-ins and
admin actions run several statements in a transaction, and transaction mode lost or mixed
up their replies once a few ran at the same moment, so they go through the same pooler's
session mode (port 5432) instead, which passes each connection straight through. Session
mode has room for about 15 connections per project, so each server instance keeps at
most two, closed after 10 idle seconds. No request waits on the database for more than
10 seconds (30 for admin actions): it gets a "busy, try again" answer, and if nothing at
all is getting through, the app reconnects.

## Developing

Needs Node 20+ and Postgres.

```bash
cp .env.example .env.local      # then edit it
createdb auction_dev && createdb auction_test
npm install
npm run db:migrate
npm run dev                     # http://localhost:3000, /board, /admin
```

| Command | |
| --- | --- |
| `npm test` | Unit tests (team balancing) and database tests (bidding rules, concurrent bids, anti-snipe, settling, and the connection settings through a proxy that behaves like Supabase's pooler). The database tests use `TEST_DATABASE_URL`, which they wipe, and are skipped if it isn't set. |
| `npm run lint` / `npm run typecheck` | ESLint / TypeScript |
| `npm run simulate -- --url http://localhost:3000 --yes` | The 80-phone simulation, locally |

Code map: `db/schema.sql` (tables + bidding SQL), `src/lib/` (state, admin actions,
team balancing, sessions), `src/app/api/` (route handlers), `src/components/` (phone,
board and admin UIs).
