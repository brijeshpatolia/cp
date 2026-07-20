// Auto-fill PollEv's participant registration ("What's your name?") screen.

async function findInputByHint(page, keyword) {
  const inputs = await page.$$('input');
  for (const input of inputs) {
    const matches = await input.evaluate((el, kw) => {
      const type = (el.getAttribute('type') || 'text').toLowerCase();
      if (['hidden', 'checkbox', 'radio', 'submit', 'button'].includes(type)) {
        return false;
      }
      const hints = [
        el.placeholder,
        el.name,
        el.id,
        el.getAttribute('aria-label'),
        el.labels && el.labels[0] ? el.labels[0].innerText : '',
      ]
        .join(' ')
        .toLowerCase();
      return hints.includes(kw);
    }, keyword);
    if (matches) return input;
  }
  return null;
}

async function clickPrimaryButton(page) {
  const submit = await page.$('button[type="submit"]');
  if (submit) {
    await submit.click();
    return true;
  }
  const buttons = await page.$$('button, [role="button"]');
  for (const button of buttons) {
    const text = ((await button.innerText().catch(() => '')) || '')
      .trim()
      .toLowerCase();
    if (/^(continue|join|submit|next|start|go)\b/.test(text)) {
      await button.click();
      return true;
    }
  }
  return false;
}

async function detectSso(page) {
  return page.evaluate(() => {
    const text = (document.body ? document.body.innerText : '').toLowerCase();
    const hasSso =
      text.includes('sign in with google') ||
      text.includes('sign in with microsoft') ||
      text.includes('continue with google') ||
      text.includes('continue with microsoft') ||
      text.includes('log in with');
    return hasSso;
  });
}

/**
 * Handle whatever registration screen is showing. Safe to call repeatedly.
 * Returns one of: 'registered' | 'sso' | 'email-blocked' | 'none'.
 */
async function handleRegistration(page, { screenName, fillEmail }, log) {
  const nameInput = await findInputByHint(page, 'name');

  if (!nameInput) {
    if (await detectSso(page)) {
      log(
        '🔒',
        'This poll requires org login — run once locally with HEADLESS=false ' +
          'to establish the session in ./pollev-profile'
      );
      return 'sso';
    }
    return 'none';
  }

  await nameInput.fill(screenName);
  log('✍️', `Filled screen name "${screenName}"`);

  const emailInput = await findInputByHint(page, 'email');
  if (emailInput) {
    const required = await emailInput.evaluate(
      (el) => el.required || el.getAttribute('aria-required') === 'true'
    );
    if (required) {
      if (fillEmail) {
        const email =
          screenName.replace(/\s/g, '').toLowerCase() + '@example.com';
        await emailInput.fill(email);
        log('✍️', `Filled required email ${email}`);
      } else {
        log(
          '⚠️',
          'Registration requires an email. Set FILL_EMAIL=true to auto-fill ' +
            'a placeholder, or handle it once via HEADLESS=false. Waiting...'
        );
        return 'email-blocked';
      }
    }
  }

  const clicked = await clickPrimaryButton(page);
  if (clicked) {
    log('✅', 'Submitted registration');
    await page.waitForTimeout(1500);
    return 'registered';
  }

  log('⚠️', 'Filled name but found no submit button — will retry next tick');
  return 'none';
}

module.exports = { handleRegistration };
