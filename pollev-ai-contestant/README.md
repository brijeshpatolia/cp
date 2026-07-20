# PollEv AI Contestant 🤖⚡

A headless **human-vs-AI quiz race** bot for [Poll Everywhere](https://pollev.com) sessions.

It opens a PollEv participant page in headless Chromium (Playwright), registers
itself with a screen name (default **"AI Claude"**), then watches the DOM for live
multiple-choice questions. The instant a new question appears, it sends the
question + options to Claude (`claude-sonnet-4-6`), logs the pick, confidence,
one-line reason, and end-to-end latency — and (optionally) clicks the answer in
the page. Target: **under 4 seconds** from question detection to answer.

Every Q&A event is also appended as a JSON line to `results.jsonl`, so the
event organizer can build a leaderboard afterwards.

Word clouds, open-text prompts, and "waiting for presenter" screens are simply
ignored — the bot idles until an MCQ shows up, and every polling tick is wrapped
in try/catch so nothing crashes the loop.

## Quickstart — GitHub Codespaces (works from a phone!)

1. Open this repo on github.com (mobile browser is fine).
2. Tap **Code → Codespaces → Create codespace on main**.
   The devcontainer auto-installs Node deps and Chromium (takes ~2 min).
3. In the Codespace terminal:

   ```bash
   cp .env.example .env
   # edit .env and paste your ANTHROPIC_API_KEY (nano .env or the editor)
   npm start
   ```

4. Watch the log. When the presenter pushes a multiple-choice question you'll see:

   ```
   🆕 [2026-07-20T12:00:01.000Z] New question: "What year was..."
   🤖 [2026-07-20T12:00:02.400Z] Pick: [2] "1969" (confidence 0.97) — Apollo 11 landed in 1969. [api 1350ms, total 1402ms]
   ```

## Quickstart — local (headed mode, for debugging selectors)

```bash
git clone <this repo> && cd pollev-ai-contestant
npm install
npx playwright install --with-deps chromium
cp .env.example .env   # add your ANTHROPIC_API_KEY
HEADLESS=false npm start
```

With `HEADLESS=false` a real Chromium window opens so you can watch what the
bot sees and inspect PollEv's markup.

## Auto-submitting answers

By default the bot only *logs* its pick. To make it actually click the answer
button in the page:

```bash
npm run start:click        # equivalent to AUTO_CLICK=true npm start
```

> **Etiquette:** only enable auto-submit with the session organizer's
> permission. It's their poll — the fun is racing the humans openly, not
> stuffing the ballot.

## Configuration

All via environment variables / `.env`:

| Var | Default | Meaning |
|---|---|---|
| `POLLEV_URL` | `https://pollev.com/mmsapac` | participant page to watch |
| `SCREEN_NAME` | `AI Claude` | name used at registration |
| `AUTO_CLICK` | `false` | actually submit the answer |
| `POLL_INTERVAL` | `750` | ms between DOM checks |
| `HEADLESS` | `true` | set `false` for local debugging |
| `FILL_EMAIL` | `false` | auto-fill a placeholder email if PollEv requires one |
| `ANTHROPIC_API_KEY` | — | **required** |

Registration cookies/localStorage persist in `./pollev-profile`, so the bot
stays registered across restarts.

## Troubleshooting

**Selectors not matching (questions never detected).** PollEv's markup varies.
Run locally with `HEADLESS=false`, open DevTools on the participant page, and
inspect the question title and option buttons. Then adjust the selector lists
at the top of `src/extract.js` (`TITLE_SELECTORS` / `OPTION_SELECTORS`).

**"This poll requires org login".** Some polls sit behind Google/Microsoft
SSO. Run once locally with `HEADLESS=false`, log in manually in the opened
browser — the session is saved to `./pollev-profile` — then restart headless.
(Note: the profile directory is gitignored and won't follow you into a
Codespace; do the SSO dance wherever the bot actually runs.)

**Registration wants an email.** Set `FILL_EMAIL=true` to auto-fill
`<screenname>@example.com`, or handle it once in headed mode.

**API key errors.** `❌ ANTHROPIC_API_KEY is not set` → copy `.env.example` to
`.env` and paste your key. A 401 from the API means the key is wrong/revoked; a
429 means you're rate-limited — the bot falls back to option 0 with confidence
0 rather than crashing.

**Nothing happens on word clouds / open text.** That's by design — the bot
only answers multiple choice and idles otherwise (`⏳ Waiting (screen: ...)`).

## How it works

```
src/index.js     main loop: persistent Chromium context, registration, 750ms watcher
src/extract.js   layered DOM selectors: find question, options, describe screen
src/claude.js    Claude API call (15s timeout, 1 retry, JSON-only prompt, safe fallback)
src/register.js  auto-fill screen name / join flow, SSO + email edge cases
```

Dedupe is by question text: each unique question is answered exactly once per
process lifetime.
