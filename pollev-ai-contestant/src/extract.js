// DOM extraction for Poll Everywhere participant pages.
// PollEv markup varies between deployments, so every lookup is a layered list
// of selector strategies plus text heuristics. All functions run in the page
// context via page.evaluate.

const TITLE_SELECTORS = [
  '[class*="activity-title"]',
  '[class*="component-title"]',
  '[data-testid*="title"]',
  'h1',
  'h2',
];

const OPTION_SELECTORS = [
  'button[class*="multiple-choice"]',
  'button[class*="option"]',
  '[role="radio"]',
];

/**
 * Extract the current multiple-choice question, if one is on screen.
 * Returns { question, options: string[] } or null when no valid MCQ
 * (needs a non-empty question and >= 2 non-empty options).
 */
async function extractMcq(page) {
  return page.evaluate(
    ({ titleSelectors, optionSelectors }) => {
      const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();

      let question = '';
      for (const sel of titleSelectors) {
        const el = document.querySelector(sel);
        const text = el ? clean(el.innerText) : '';
        if (text) {
          question = text;
          break;
        }
      }

      let options = [];
      for (const sel of optionSelectors) {
        const els = Array.from(document.querySelectorAll(sel)).filter(
          (el) => clean(el.innerText)
        );
        if (els.length >= 2) {
          options = els.map((el) => clean(el.innerText));
          break;
        }
      }

      if (!question || options.length < 2) return null;
      return { question, options };
    },
    { titleSelectors: TITLE_SELECTORS, optionSelectors: OPTION_SELECTORS }
  );
}

/**
 * Click the option button at the given index, using the same selector
 * strategy as extractMcq so indexes line up. Returns true if clicked.
 */
async function clickOption(page, index) {
  return page.evaluate(
    ({ optionSelectors, idx }) => {
      const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();

      let els = [];
      for (const sel of optionSelectors) {
        const found = Array.from(document.querySelectorAll(sel)).filter(
          (el) => clean(el.innerText)
        );
        if (found.length >= 2) {
          els = found;
          break;
        }
      }

      const target = els[idx];
      if (!target) return false;
      target.click();
      return true;
    },
    { optionSelectors: OPTION_SELECTORS, idx: index }
  );
}

/**
 * Short human-readable description of what's currently on screen,
 * for logging: 'registration' | 'waiting' | 'mcq' | 'unknown'.
 */
async function describeScreen(page) {
  return page.evaluate(
    ({ optionSelectors }) => {
      const clean = (s) => (s || '').replace(/\s+/g, ' ').trim();
      const bodyText = clean(document.body ? document.body.innerText : '').toLowerCase();

      const nameInput = Array.from(
        document.querySelectorAll('input[type="text"], input:not([type])')
      ).find((el) => {
        const hints = [
          el.placeholder,
          el.name,
          el.id,
          el.getAttribute('aria-label'),
          el.labels && el.labels[0] ? el.labels[0].innerText : '',
        ]
          .join(' ')
          .toLowerCase();
        return hints.includes('name');
      });
      if (nameInput) return 'registration';

      for (const sel of optionSelectors) {
        const els = Array.from(document.querySelectorAll(sel)).filter(
          (el) => clean(el.innerText)
        );
        if (els.length >= 2) return 'mcq';
      }

      if (
        bodyText.includes('waiting for') ||
        bodyText.includes("hasn't asked") ||
        bodyText.includes('no active') ||
        bodyText.includes('will appear here')
      ) {
        return 'waiting';
      }

      return 'unknown';
    },
    { optionSelectors: OPTION_SELECTORS }
  );
}

module.exports = { extractMcq, clickOption, describeScreen };
