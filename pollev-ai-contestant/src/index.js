// PollEv AI Contestant — main loop.
// Opens the participant page in headless Chromium, handles registration,
// then polls the DOM for new multiple-choice questions and answers them
// with Claude. Every Q&A event is appended to results.jsonl.

require('dotenv').config();

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { extractMcq, clickOption, describeScreen } = require('./extract');
const { askClaude, MODEL } = require('./claude');
const { handleRegistration } = require('./register');

const config = {
  pollevUrl: process.env.POLLEV_URL || 'https://pollev.com/mmsapac',
  screenName: process.env.SCREEN_NAME || 'AI Claude',
  autoClick: process.env.AUTO_CLICK === 'true',
  pollInterval: parseInt(process.env.POLL_INTERVAL || '750', 10),
  headless: process.env.HEADLESS !== 'false',
  fillEmail: process.env.FILL_EMAIL === 'true',
};

const PROFILE_DIR = path.resolve(__dirname, '..', 'pollev-profile');
const RESULTS_FILE = path.resolve(__dirname, '..', 'results.jsonl');

function log(emoji, message) {
  console.log(`${emoji} [${new Date().toISOString()}] ${message}`);
}

function recordResult(event) {
  try {
    fs.appendFileSync(RESULTS_FILE, JSON.stringify(event) + '\n');
  } catch (err) {
    log('⚠️', `Could not write results.jsonl: ${err.message}`);
  }
}

const seenQuestions = new Set();
let lastScreen = null;
let lastWaitingLog = 0;

async function handleMcq(page, mcq) {
  const detectedAt = Date.now();
  log('🆕', `New question: "${mcq.question}"`);
  mcq.options.forEach((opt, i) => log('  ', `   ${i}. ${opt}`));

  const answer = await askClaude(mcq.question, mcq.options);
  const totalLatencyMs = Date.now() - detectedAt;

  log(
    '🤖',
    `Pick: [${answer.choiceIndex}] "${mcq.options[answer.choiceIndex]}" ` +
      `(confidence ${answer.confidence.toFixed(2)}) — ${answer.reason} ` +
      `[api ${answer.apiLatencyMs}ms, total ${totalLatencyMs}ms]`
  );

  let submitted = false;
  if (config.autoClick) {
    submitted = await clickOption(page, answer.choiceIndex);
    if (submitted) {
      log('✅', `Submitted option ${answer.choiceIndex}`);
    } else {
      log('⚠️', 'AUTO_CLICK is on but the option button could not be clicked');
    }
  }

  recordResult({
    timestamp: new Date().toISOString(),
    question: mcq.question,
    options: mcq.options,
    pick: answer.choiceIndex,
    pickText: mcq.options[answer.choiceIndex],
    confidence: answer.confidence,
    reason: answer.reason,
    apiLatencyMs: answer.apiLatencyMs,
    totalLatencyMs,
    submitted,
    model: MODEL,
  });
}

async function tick(page) {
  const mcq = await extractMcq(page);

  if (mcq) {
    if (!seenQuestions.has(mcq.question)) {
      seenQuestions.add(mcq.question);
      await handleMcq(page, mcq);
    }
    lastScreen = 'mcq';
    return;
  }

  const screen = await describeScreen(page);

  if (screen === 'registration') {
    await handleRegistration(
      page,
      { screenName: config.screenName, fillEmail: config.fillEmail },
      log
    );
  } else if (screen !== lastScreen || Date.now() - lastWaitingLog > 15000) {
    log('⏳', `Waiting (screen: ${screen})...`);
    lastWaitingLog = Date.now();
  }
  lastScreen = screen;
}

async function main() {
  if (!process.env.ANTHROPIC_API_KEY) {
    log('❌', 'ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key.');
    process.exit(1);
  }

  log('🚀', `Starting PollEv AI Contestant`);
  log('  ', `   url=${config.pollevUrl} name="${config.screenName}" ` +
    `autoClick=${config.autoClick} interval=${config.pollInterval}ms ` +
    `headless=${config.headless} model=${MODEL}`);

  const context = await chromium.launchPersistentContext(PROFILE_DIR, {
    headless: config.headless,
  });
  const page = context.pages()[0] || (await context.newPage());

  await page.goto(config.pollevUrl, { waitUntil: 'domcontentloaded' });
  log('🌐', `Loaded ${config.pollevUrl}`);

  await handleRegistration(
    page,
    { screenName: config.screenName, fillEmail: config.fillEmail },
    log
  ).catch((err) => log('⚠️', `Registration handler error: ${err.message}`));

  let busy = false;
  setInterval(async () => {
    if (busy) return;
    busy = true;
    try {
      await tick(page);
    } catch (err) {
      // Never crash the loop — page navigations, detached frames, API
      // hiccups etc. all land here and we just try again next tick.
      log('⚠️', `Tick error (ignored): ${err.message}`);
    } finally {
      busy = false;
    }
  }, config.pollInterval);

  const shutdown = async () => {
    log('👋', 'Shutting down');
    await context.close().catch(() => {});
    process.exit(0);
  };
  process.on('SIGINT', shutdown);
  process.on('SIGTERM', shutdown);
}

main().catch((err) => {
  log('❌', `Fatal: ${err.stack || err.message}`);
  process.exit(1);
});
