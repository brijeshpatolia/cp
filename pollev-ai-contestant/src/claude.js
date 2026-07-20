// Anthropic API call + strict-JSON answer parsing.

const Anthropic = require('@anthropic-ai/sdk');

const MODEL = process.env.CLAUDE_MODEL || 'claude-sonnet-4-6';

const SYSTEM_PROMPT = [
  'You are a lightning-fast quiz contestant. You are given a multiple-choice',
  'question and its options. Respond with JSON ONLY — no prose, no markdown',
  'fences, nothing else. Exact shape:',
  '{"choiceIndex": <0-based integer index of the best option>,',
  ' "confidence": <number between 0 and 1>,',
  ' "reason": "<one short sentence>"}',
].join(' ');

let client = null;
function getClient() {
  if (!client) {
    // timeout is in ms for the JS SDK; we do our own single retry, so
    // disable the SDK's built-in retries to keep total latency bounded.
    client = new Anthropic({ timeout: 15000, maxRetries: 0 });
  }
  return client;
}

function stripFences(text) {
  return text
    .trim()
    .replace(/^```(?:json)?\s*/i, '')
    .replace(/\s*```$/, '')
    .trim();
}

function fallbackAnswer(reason) {
  return { choiceIndex: 0, confidence: 0, reason };
}

function parseAnswer(rawText, numOptions) {
  try {
    const parsed = JSON.parse(stripFences(rawText));
    let choiceIndex = Number(parsed.choiceIndex);
    if (!Number.isInteger(choiceIndex)) return fallbackAnswer('unparseable choiceIndex');
    choiceIndex = Math.min(Math.max(choiceIndex, 0), numOptions - 1);
    let confidence = Number(parsed.confidence);
    if (!Number.isFinite(confidence)) confidence = 0;
    confidence = Math.min(Math.max(confidence, 0), 1);
    return {
      choiceIndex,
      confidence,
      reason: typeof parsed.reason === 'string' ? parsed.reason : '',
    };
  } catch (err) {
    return fallbackAnswer(`JSON parse failed: ${err.message}`);
  }
}

async function requestOnce(question, options) {
  const userPrompt = [
    `Question: ${question}`,
    'Options:',
    ...options.map((opt, i) => `${i}. ${opt}`),
  ].join('\n');

  const response = await getClient().messages.create({
    model: MODEL,
    max_tokens: 300,
    system: SYSTEM_PROMPT,
    messages: [{ role: 'user', content: userPrompt }],
  });

  const textBlock = response.content.find((b) => b.type === 'text');
  return textBlock ? textBlock.text : '';
}

/**
 * Ask Claude which option to pick. One retry on failure; guaranteed to
 * resolve with { choiceIndex, confidence, reason, apiLatencyMs } — falls back
 * to choiceIndex 0 / confidence 0 if both attempts fail.
 */
async function askClaude(question, options) {
  const started = Date.now();
  let answer;
  try {
    answer = parseAnswer(await requestOnce(question, options), options.length);
  } catch (firstErr) {
    try {
      answer = parseAnswer(await requestOnce(question, options), options.length);
    } catch (secondErr) {
      answer = fallbackAnswer(`API failed twice: ${secondErr.message}`);
    }
  }
  answer.apiLatencyMs = Date.now() - started;
  return answer;
}

module.exports = { askClaude, MODEL };
