# VOCABULARY UNDER FIRE — GM ammunition for Round Type F

Reference material for the Game Master of THE RISK DESK. Not for the player's eyes.

**What Round F is** (`prompt/RISK_DESK.md` §6F): you say a sentence a real quant would say. The
player translates it to plain English, then uses the term correctly in a **new** sentence,
unprompted. Nothing else counts.

**What it is actually testing:** Victory Condition 2, the Passing Test. Not "can they define the
word" — every definition is one search away. It is: *does the word behave correctly in their mouth
when they are not being asked about it.* A person with no background gets the definition right and
the **usage** wrong in a specific, repeatable way. Those failure modes are the **TELL** rows below.
Hunt the tell, not the definition.

**The locking rule** (§6, §8 — NO JARGON BEFORE THE MECHANISM): every term below carries the level
that unlocks it. Do not let the name out of your mouth before the player has built the thing. If
you need to talk about the mechanism earlier, describe it — "the balance condition", "the leftover",
"the dial" — and hand over the real word only at the unlock.

**Source discipline.** Every page reference in this document was checked against
`notes/` before being written down. `notes/` is a page-indexed transcription of a **scan**; where it
says `[UNREADABLE]`, `[APPROX]`, `[INFERRED]` or `[TENTATIVE]`, that uncertainty is carried forward
here and must be carried forward to the table. Anything that is my reading rather than the paper's
statement is marked **[GM INFERENCE]**. Do not upgrade those at the table.

---

## 0. HOW TO RUN A ROUND F — 60 seconds

1. **Fire the sentence.** Deadpan, at speed, as an aside inside a desk task. Never "here is a
   vocabulary question."
2. **Demand the translation.** Plain English, no jargon substitution. "Cross-sectional means
   we do it in the cross-section" is a fail — dock bps for a circular translation.
3. **Demand a new sentence.** It must be about a *different situation* from yours. A player who
   re-skins your sentence has memorised, not understood.
4. **Fire the follow-up.** This is where the round is actually decided. The translations are easy
   to fake; the follow-ups are not.
5. **Score on the ladder** (§7 of the rules). Correct translation + correct new sentence = tier 2.
   Surviving the follow-up = tier 4. Nothing below tier 4 closes a level.

**Docking rules specific to Round F:** a right answer with a wrong reason scores zero (§8 —
this is the rule that Victory Condition 2 lives or dies on). Using a term correctly *by accident*
in the new sentence, without being able to say why, is also zero.

---

## 1. THE UNLOCK LADDER

Do not use the word before the level in column 2. Column 3 is what the paper does with it.

| # | Term | Unlocks at | Status in the BFRE paper |
|---|---|---|---|
| 1 | cross-sectional regression | **L7** (name); machinery from L1 | **Used, repeatedly, as the paper's core method** (pp. 7, 24, 30, 32) |
| 2 | orthogonal | **L2** (one column); deepens **L4** | **Word never appears** in the 65 pages. Mechanism is everywhere |
| 3 | residual | **L0** | **Used constantly** — `u`, `ū`, `ε`, `ε̃` (pp. 7, 8, 11, 24, 26, 27, 42, 52) |
| 4 | specific risk | **L9** (the forecast); *specific return* from **L0** | **Used constantly** — it is a named section (pp. 24, 27, 28, 30, 35) |
| 5 | exposure | **L1** (name); BFRE's meaning needs **L5** | **The paper's house word.** Defined outright on p. 39 |
| 6 | loading | **L1**, alongside exposure | **Word never appears.** Synonym the house does not use |
| 7 | design matrix | **L3** | **Phrase never appears.** `X` is called "factor exposures" (p. 24) |
| 8 | degrees of freedom | **L6** | **Phrase never appears.** Machinery present (t-stats, obs counts) |
| 9 | standard error | **L6** | **Phrase never appears in the paper.** Presupposed by every t-statistic |
| 10 | covariance matrix | **L8**; *covariance* itself at **L5** | **Used constantly** — `F`, `Σ`, `Δ` (pp. 2, 24, 27, 28) |
| 11 | shrinkage | **L8** boss | **Word appears only in a bibliography title** ([7], p. 64). Mechanism on p. 36 |
| 12 | eigenvalue | **L8** | **Word never appears. No eigen-decomposition, no PCA anywhere in the paper** |
| 13 | tracking error | **L10** (once `V` exists); used at **L11** | **Phrase never appears.** The paper's word is **Active Risk** (pp. 34, 35) |
| 14 | marginal contribution | **L11** | **Phrase never appears.** The paper reports "contribution to active risk" (pp. 34, 35) |
| 15 | multicollinearity | **L4** | **Used, once, precisely** (p. 32, with footnote 16) |
| 16 | in-sample vs out-of-sample | **L12** | "Out-of-sample" appears **once** (p. 30). "In-sample" **never** |

**Read that column 4 carefully before every round.** Six of the sixteen terms are words the player
will hear from real quants but will never find in the paper. If you cite a page for one of those,
you have broken rule §8 (NO NUMBER WITHOUT ITS ORIGIN) in its most damaging form.

---

## 2. HOUSE STYLE — where the paper's word differs from the textbook's

The player will talk to people who use the paper's convention. Drill these six.

| Textbook / street | BFRE says | Where | Why it matters at the table |
|---|---|---|---|
| factor **loading** | factor **exposure** | p. 39: "The standardised values are **referred to as exposures**" | In BFRE, `X` is an *observed, standardised characteristic*, not a fitted time-series beta. Calling it a loading imports the wrong origin story |
| **design matrix** | "factor exposures", `X` | p. 24, where-list under (1.7) | Nobody at this desk says design matrix. Saying it is harmless; failing to recognise it is not |
| **tracking error** | **Active Risk** | p. 34 top-line list; p. 35 banner | The EDR report the player will be shown says *Active Risk*. Hearing "tracking error" and not mapping it instantly is a tell |
| **D** (specific risk matrix) | **Δ** (Delta) | p. 24, eq. (1.8): `Σ = X F Xᵀ + Δ` | The game's own rules write `V = XFXᵀ + D`. The paper writes `Σ` and `Δ`. Flag the letter swap explicitly at L10 or the player will think they have found an error |
| **shrinkage** | "adding a **Bayesian prior**" | p. 36 | Applied to *thin country/industry factor returns*, not to the covariance matrix. See §3.11 |
| **least squares / OLS / estimator** | *(never named)* | — | The paper describes regressions with square-root-of-market-cap weights (p. 25) but **never names the estimator**, never writes normal equations, never says "least squares", "unbiased" or "standard error". Verified by grep over all 65 pages of `notes/` |

**A seventh, subtler one.** The paper prints an italic *R²* on p. 32 and defines it only in words —
"the proportion of cross-sectional variation in asset returns explained by the set of common factors
in the model". The phrase *coefficient of determination* is the **transcriber's gloss in `notes/`,
not printed text**. No formula for R² appears anywhere in the paper.

---

## 3. THE SIXTEEN

---

### 1. CROSS-SECTIONAL REGRESSION — unlocks at **L7** (The Timeline)

**Fire this**
> "We're running the cross-sectional regression daily for the regionals and weekly for World, so the
> World factor returns are going to be a lot lumpier than the NAMR ones."

**Plain English**
On one single day, line up every stock in the universe. Each stock has a set of characteristics and
one return that day. Find the numbers that best turn characteristics into that day's returns —
across the stocks, all at once, with time held still. Do it again tomorrow. Each run produces one
factor return per factor, for that day. Repeat, and you have a time series.

**Mechanism required before the word**
- **L1** — `b = Σxr/Σx²` from nudging (one column, one date).
- **L3** — two columns, two balance conditions.
- **L7** — the same regression run month after month, producing a *series* of `f`.
The word is only earned at L7, because "cross-sectional" is a *contrast* word: it means nothing
until the player can state the alternative (a time-series regression of one stock's history) and say
what it would have given instead. That contrast is L7's boss round.

**In the paper**
- p. 24 — the estimation phase is "a series of **cross-sectional regressions** of asset returns
  against asset factor exposures, which provides estimates of factor returns and asset specific
  returns." Frequency: "**daily** for country and regional models and **weekly** for the World model"
  (no justification given for the weekly choice — good L12 ammunition).
- p. 7 — eqs (1.1)–(1.2): the industry-selection two-step cross-sectional regression, "run for
  n = 1, 2, …". p. 8 confirms these use **monthly** returns over the 15-year research history.
- p. 30 — "Style and industry factors are selected by assessing explanatory power using **monthly
  cross-sectional regressions**."
- p. 32 — R² is "the proportion of **cross-sectional** variation in asset returns explained by the
  set of common factors in the model."
- Note the frequency zoo, all in the paper's own words: **monthly** for factor *selection* (pp. 8,
  30), **daily/weekly** for factor *return estimation* (p. 24). A player who says "the regression is
  monthly" full stop is half right and will be caught.

**THE TELL**
Three, in order of how badly they give the game away.
1. **They describe a time-series regression and call it cross-sectional.** "We take the stock's
   returns over the last five years and regress them on its Value score." That is not this. It is,
   however, exactly what the paper does for *Historical Beta* on p. 42, eq. (1.12) — so the confusion
   is live in this very document and the player must be able to separate the two.
2. **They put it backwards.** "We regress the exposures on the returns." Returns are the left-hand
   side. Nothing marks a non-quant faster.
3. **They think `f` is one fixed number.** They speak of "the Value factor return" as a constant,
   rather than one number per date, of which BFRE has a series running from **March 1996** (p. 27).

**Follow-up (separates understanding from memory)**
> "Same data, two ways. (a) 3,000 stocks, one month, regress this month's returns on this month's
> Value exposures. (b) One stock, 200 months, regress its returns on its Value exposures. Both are
> regressions. What have I got at the end of each, how many numbers is it, and which one is BFRE?"

Pass looks like: (a) one number per factor for that month, a *factor return*, and BFRE repeats it —
daily for regionals, weekly for World (p. 24); (b) one number for that stock, a *beta* / sensitivity,
which is what p. 42 eq. (1.12) does to *build an exposure*, not to estimate a factor return. Bonus
tier-4 answer: BFRE uses the time-series form **inside** the cross-sectional form — historical beta
is a time-series output that becomes a column of `X`.

**Difficulty:** moderate. The idea is easy; the *contrast* is where players slip.

---

### 2. ORTHOGONAL — unlocks at **L2** (The Balance), deepens at **L4** (The Collision)

**Fire this**
> "By construction the residuals are orthogonal to every column of X in that cross-section — so if
> your specific returns are showing a Value tilt, your exposures aren't what you think they are."

**Plain English**
Two lists of numbers are orthogonal when you multiply them pairwise and the total comes to zero.
That is all it means. It says the two carry no overlapping information *in the linear sense*: one
cannot be used to predict any part of the other by a straight-line rule.

**Mechanism required before the word**
- **L2** — `Σ x·e = 0` derived as a turning-force condition and proved by the nudge/contradiction
  argument. Once the player has *forced* that sum to zero themselves, the word is a label for
  something they own.
- **L4** — the multi-column meaning: "a coefficient is what this column explains that no other
  column already explained." That is the sense a quant uses in conversation.

**In the paper**
> **The word "orthogonal" does not appear anywhere in the 65 transcribed pages.** Checked by grep
> over all of `notes/`. There is exactly one occurrence in `notes/` and it is the **transcriber's own
> commentary** on p. 52 ("the macro betas are estimated on the residuals of (1.12) … so they are
> orthogonal to whatever (1.12) already explains"), explicitly followed by "this design choice is
> stated without justification". Do not quote that as the paper's word.

The **mechanism**, however, is load-bearing throughout:
- p. 7, eqs (1.1)–(1.2) — industries at level n+1 are fitted to the **residual** `u` of the level-n
  fit, so each granularity level only gets credit for what the coarser one missed.
- pp. 10, 12 — eqs (1.3)–(1.6): candidate substyles are regressed against the residual `ε` of a
  market + core-country + core-industry model; accepted factors are then folded into the first stage
  and the whole thing re-run recursively.
- p. 52, eq. (1.49) — macro-economic betas are the slope of a regression **of the residuals of
  (1.12)**, not of raw returns.
- p. 30, as a stated **assumption**: "Factor returns have **zero correlation** with asset specific
  returns, and specific returns from different issuers are unrelated and have **zero correlation**."

**[GM INFERENCE] — and it is a good one to hand the player at L9.** Within a *single* fitted
cross-section, the weighted sum `Σ w·x·u = 0` for every column of `X` is *forced by the arithmetic
of the fit* — it is not an assumption, it is what the fit means. The p. 30 bullet is a *different
and much stronger* claim: that the factor-return **time series** and the specific-return **time
series** are uncorrelated **over time**. Nothing in the fitting procedure delivers that. The paper
lists it under "Assumptions & Limitations" and offers no evidence. This is the cleanest available
example of the L9 distinction between *what least squares guarantees* and *what BFRE assumes*. The
paper never writes the normal equations, so the "forced by arithmetic" half is standard algebra the
player builds at L2, not a paper claim.

**THE TELL**
1. **Boardroom usage.** "That's orthogonal to what we're discussing" — meaning irrelevant, a
   tangent. Extremely common, and instantly fatal in a quant conversation because it reveals the
   word arrived from management-speak rather than from a dot product.
2. **Claiming BFRE's factors are orthogonal.** They are conspicuously not. p. 11, Figure 1.3
   (NAMR, Dec 2013): **Size–Liquidity exposure correlation = 0.74**, Earnings Yield–Profitability
   **0.64**, Volatility–Dividend Yield **−0.46**, Size–Volatility **−0.36**. A player who says "the
   factors are orthogonal by construction" has just contradicted the paper's own figure.
3. **Collapsing two different orthogonalities.** Residuals ⟂ columns of `X` is *forced*. Column ⟂
   column is *not*, and in BFRE is false. Different statements. A player who cannot keep them apart
   will fail the L4 boss round.

**Follow-up**
> "In the cold-open five stocks, `Σe = 2` but `Σx·e = 0`. One of those is orthogonality. Which, and
> why is the other one not zero — is that a bug?"

Pass: `Σx·e = 0` is the orthogonality (residuals ⟂ the `x` column). `Σe = 2 ≠ 0` because there is no
constant column in that fit — orthogonality is forced only against columns actually *in* `X`, and a
column of ones is not in this one. Not a bug; it is the whole content of L5.
(Numbers: `datasets/level0.md`, verified in exact rationals by `tools/verify_coldopen.py`.)

**Second follow-up if they sail through**
> "Size and Liquidity exposures correlate at 0.74. Are the Size and Liquidity **factor returns**
> orthogonal? Are the residuals orthogonal to *both* columns?"

Answers: factor returns — no, nothing forces that, and the paper doesn't claim it. Residuals —
yes, to both, always, by construction.

**Difficulty:** L2 sense is easy. The L4 sense ("what this column explains that no other column
already explained") is where **Frisch–Waugh** lives and is **honestly graduate-level** — say so.

---

### 3. RESIDUAL — unlocks at **L0** (The Miss)

**Fire this**
> "Don't read the residual as noise — in the industry step it's literally the input to the next
> regression. Anything you leave in the level-one residual is what the level-two industries get to
> explain."

**Plain English**
What is left of a stock's return after the model has said its piece. Actual minus predicted, one
number per stock per date. Not an error in the sense of a mistake — it is the part of the move the
model was never built to reach.

**Mechanism required before the word**
**L0.** The player must have (a) computed misses, (b) argued for squaring rather than summing raw,
(c) argued for squares over absolute values. `datasets/level0.md` runs the whole thing: at `b = 2`
the residuals are `+1, −1, +0.5, +2, −0.5`. Three desks with identical `Σe = 0` and `Σe²` of 1, 144
and 0 make the point that cancellation is not smallness.

**In the paper — used everywhere, under four different symbols**

| Symbol | Meaning | Page |
|---|---|---|
| `u` | residual of the first-step industry regression, eq. (1.1) | pp. 7, 8 |
| `ū` | residual of the second-step (finer industry) regression, eq. (1.2) | pp. 7, 8 |
| `ε`, `ε̃ᵢ` | residual of the style-selection two-step, eqs (1.3)–(1.4) | pp. 10, 11 |
| `η`, `η̃ᵢ` | same, one recursion later with size folded in, eqs (1.5)–(1.6) | p. 12 |
| `u` | **asset specific return** in the model equation `r = Xf + u`, eq. (1.7) | p. 24 |
| `u` | first-pass residual, eq. (1.9); `ε` = second-pass residual, eq. (1.11) | pp. 25–27 |
| `ε_{i,s}` | residual of the historical-beta regression, eq. (1.12) | p. 42 |

Two things worth saying out loud at the table:
- p. 24 — "`X f` is termed the common factor return and `u` is the asset specific, or idiosyncratic,
  return." **In BFRE, "residual" and "specific return" are the same object wearing two names**, and
  which name it gets depends on whether you are talking about the fit or about risk.
- p. 42 — "Historical Sigma" is "an **equally-weighted** standard deviation of the residuals in
  regression (1.12)", even though (1.12) itself is exponentially weighted. `notes/` flags this as an
  explicit, unjustified inconsistency. Good L12 material.

**THE TELL**
1. **"The residuals should be zero."** No. You minimise their sum of squares; the individual
   residuals are neither zero nor supposed to be. If they were zero you would have fitted noise.
2. **Calling them errors and treating them as failure.** In a *risk* model the residual is not the
   waste product, it is **half the answer** — the EDR example on p. 35 shows Specific at **50%** of
   Active Risk. The player who is embarrassed by residuals has not understood what `Δ` is for.
3. **Confusing residual with forecast error.** A residual is in-sample, computed after the fit, on
   the data the fit used. A forecast error is out-of-sample. Different objects; see §3.16.
4. **Asserting `Σe = 0` unconditionally.** True with an intercept, false without. The cold-open
   dataset has `Σe = 2`.

**Follow-up**
> "I fitted with no intercept and my residuals don't sum to zero. Is my code broken?"

Pass: no — `Σe = 0` is forced only when a column of ones is in `X`. Tier-4 extra: "and my `Σx·e`
*is* zero, which is the check that would actually catch a bug."

**Difficulty:** easy — this is the L0 term and the one they should own coldest.

---

### 4. SPECIFIC RISK — unlocks at **L9** (The Private Drama); *specific return* from **L0**

**Fire this**
> "Half the active risk in that book is specific, and it's not a data error — they've got six names
> at three per cent of NAV each."

**Plain English**
Two different objects, and the player must keep them apart:
- **specific return** — the leftover for one stock on one date. A *realised* number. `u` in
  `r = Xf + u`.
- **specific risk** — a *forecast* of how big those leftovers are likely to be for that stock going
  forward. A volatility, not a return. This is what sits on the diagonal of `Δ`.

**Mechanism required before the word**
- **L0** — the CHR trap. In the cold open, CHR has `x = 0.0` and `r = +0.5%`. No value of `b` can
  ever predict it. That is not a flaw to be fixed; it is the definition of the thing.
- **L9** — building `Δ` and separating what least squares *guarantees* from what BFRE *assumes*.
- Do not say "specific risk" before L9. Before that, it is "the private part" / "the leftover".

**In the paper**
- p. 24, eq. (1.7)–(1.8): `r = X f + u`; `Σ = X F Xᵀ + Δ`, with `Δ` described in the where-list as
  "specific risk matrix (**a diagonal matrix** of asset specific risk forecasts)".
- p. 27 — and this **contradicts the p. 24 gloss, in the paper's own words**: "The asset specific
  covariance matrix is made up of two components: a vector of asset specific risk forecasts **and a
  sparsely populated unit diagonal matrix containing non-zero, off-diagonal specific return
  correlations**." So BFRE's `Δ` is *not* purely diagonal.
- p. 27 — specific risk is "primarily estimated using a **time-series of specific returns**",
  cleansed with robust methods, exponentially weighted, Newey–West adjusted.
- p. 28, Table 1.3 — the parameters, verified digit for digit: Daily model half-life **125 days**,
  **375** observations, Newey–West lag **10 days**; Weekly (WRLD and EMKT) half-life **26 weeks**,
  **104** observations, lag **2 weeks**.
- p. 28 — the **cross-sectional overlay**: assets with little or no history (IPOs) get a forecast
  inferred from assets of "similar market capitalisation, in the same industry and country", blended
  with the time-series forecast by a weighting function whose **functional form the paper never
  gives**. In the limit the weight goes to 1.
- p. 28, p. 30 — specific return correlations are estimated **only between assets in the same
  company**; across companies they are "**assumed to be zero** in-line with standard modelling
  practice". That phrase is the whole justification offered.
- p. 35 — the EDR pie: **Specific 50%**, Style 25%, Industry 14%, Country 6%, FX 4%, Act Sec 1%
  `[INFERRED — the glyph reads 1 or 2; only the sum-to-100 argument selects 1]`. Corroborates p. 34's
  "Active Risk is split equally between common factors and stock specific sources."

**THE TELL**
1. **"Specific risk is the risk of that specific stock."** No — that is the stock's *total*
   volatility. Specific risk is what is left after the factors have taken their share. A very
   volatile stock can have modest specific risk if its volatility is all factor-driven.
2. **"Specific risk diversifies away, so it doesn't matter."** True in a textbook 500-name equal
   weight book; false in the report on p. 35, where it is 50% of active risk. The player must be able
   to say *what has to be true about a portfolio* for that to happen (few names, big active weights).
3. **Confusing the return with the risk.** Saying "the stock had 2% of specific risk yesterday" —
   yesterday it had a specific *return*. Risk is forward-looking.
4. **Assuming independence across all stocks.** BFRE explicitly does not (pp. 27, 28: cross-listings,
   ADRs and root assets, A/B shares in Sweden, Registered/Bearer in Switzerland).

**Follow-up**
> "The EDR report says specific is 50% of active risk on a real European equity book. Diversification
> is supposed to kill specific risk. What has to be true about that portfolio for the number to be
> 50 rather than 5?"

Pass: concentration — a small number of large active positions. Tier-4 extra: they point at the
paper's own corroboration, the Top Asset Contributions panel on p. 35, where active exposures run
to roughly **+1.3 to +3.0% of NAV** — but they must flag that those magnitudes are `notes/`
**pixel measurements (±10%), not printed values**. If they quote them as printed figures, dock.

**Difficulty:** the concept is L0-easy. `Δ` being *nearly* diagonal, and why, is L9 and hard.

---

### 5. EXPOSURE — unlocks at **L1** (name); BFRE's *meaning* needs **L5**

**Fire this**
> "It's a plus-nought-point-four standard deviation exposure to Volatility, not a forty basis point
> position — you're reading off the wrong axis."

**Plain English**
The number that says how much of a characteristic a stock has. It is the input column of the model:
one number per stock per factor per date. In BFRE most of them are unitless scores, not amounts of
money.

**Mechanism required before the word**
- **L1** — `x` in `predicted return = b × x`. The player has already built this; "exposure" is just
  the desk's name for their `x`.
- **L5** — required for BFRE's *actual* exposures, which are z-scores: subtract a mean, divide by a
  spread. Until the pivot has moved to `x̄` at L5 and the player has seen `Σxr/Σx²` become `Cov/Var`,
  "an exposure of +1 means one standard deviation above the market average" is a sentence they can
  repeat but not derive.

**In the paper — this is the paper's house word, and it is defined outright**
- p. 39, Huberisation: "**The standardised values are referred to as exposures** and take values
  between **+/− 3** and are standardised to a **square-root capitalisation mean of zero**, with an
  **equal-weighted standard deviation of one**." (Footnote 19: the standardisation universe is
  "similar to" the core estimation universe.) Note the asymmetry — mean cap-weighted, standard
  deviation equal-weighted — which `notes/` flags as unjustified in the source.
- p. 10 — "Conceptually, the standardisation process is similar to forming a **z-score** … a value of
  +1 for a substyle or style can be interpreted as a security having an exposure of one standard
  deviation above the market average. An exposure of zero indicates that a security has the market
  average value."
- **Three different unit systems live in the same `X`, and the player must know all three:**

| Block | What an exposure is | Units | Page |
|---|---|---|---|
| Market | every equity asset has **unit exposure**; for a portfolio it is "the fraction of portfolio %NAV invested in equities" (fn 3: delta-adjusted for derivatives) | %NAV / 1 | p. 4 |
| Style | Huberised z-score, bounded ±3 | standard deviations | pp. 10, 39 |
| Industry, Country, Currency | "assigned using **dummy variables**" | 0 / 1 | p. 30 |
| Small-Cap, Mid-Cap | "**smoothed versions of dummy variables**" indicating decile membership — smooth "to mitigate instability in exposures for assets on the decile boundaries" | smoothed 0–1 | p. 16 |

- p. 4, and this is the one the paper shouts about: "**The market factor exposure of a portfolio
  should not be confused with its market beta.**" The scanned copy carries a previous reader's
  **handwritten margin note** — "Market factor exp =/= beta" — plus a handwritten formula
  `β_{p,b} = (X_pᵀ F X_b)/(X_bᵀ F X_b)`. **That formula is a reader's pen annotation, not printed
  text.** Cite it as such or not at all.

**THE TELL**
1. **Wrong units.** "We've got a 3% exposure to Value." A style exposure is in standard deviations
   and lives in [−3, +3]. Percent-of-NAV is what an *industry* or *country* exposure is reported in
   on the EDR (p. 35 right-hand axes). Mixing them is the single most audible unit error available.
2. **Exposure = beta.** The paper pre-empts this on p. 4 because everyone does it. Market factor
   exposure is how much of the book is in equities; beta is a covariance ratio computed *from* `X`
   and `F`.
3. **Thinking exposures are estimated.** They are *measured* — off balance sheets, analyst
   estimates and price history — then standardised. Nothing is fitted to get them. (Historical Beta,
   p. 42, is a partial exception: a fitted number that then *becomes* a raw substyle before
   standardisation. That nuance is tier-5.)
4. **Forgetting they are re-standardised twice.** p. 39: substyles are Huberised, aggregated to
   styles, then "passed through the Huberisation procedure **once more**".

**Follow-up**
> "Give me the units of three things for the same portfolio: its market factor exposure, its Value
> exposure, its Airlines exposure. I want three different answers."

Pass: %NAV; standard deviations (bounded ±3); 0/1 dummy (aggregated to a portfolio, a weight).
Anyone who gives one answer three times has not read `X` as a real object.

**Difficulty:** the name is L1-easy; the z-score construction is L5; the three-unit-systems fact is
where a real quant would notice a fake.

---

### 6. LOADING — unlocks at **L1**, immediately after exposure

**Fire this**
> "People say loading, we say exposure — and in this model the exposure isn't a fitted beta, it's a
> Huberised z-score off the balance sheet."

**Plain English**
Same object as an exposure: the number multiplying a factor return in the model equation. A synonym,
imported from the academic and US-shop dialect.

**Mechanism required before the word**
**L1**, same as exposure. There is no separate mechanism. What must be built before you *use* the
word in a sentence about BFRE is the L7 contrast — see the tell.

**In the paper**
> **The word "loading" does not appear anywhere in the 65 transcribed pages.** Checked by grep over
> all of `notes/`. Every occurrence of the concept is "exposure" (defined p. 39; used from p. 4
> onward).

Teach it anyway. The player will hear it constantly, and the *register mismatch* is the point: at a
BlackRock desk, "exposure" is the house word, and reaching for "loading" marks you as coming from
somewhere else. That is not an error — but not recognising it instantly is.

**THE TELL**
1. **Loading applied to the wrong side.** Saying "the Value loading was 30 basis points last month"
   — that is the factor *return* `f`, not the loading `X`. Getting which side of `X f` is which is
   the most common single mistake among people who half-know the vocabulary.
2. **Importing the CAPM origin story.** In "factor loading" as most textbooks use it, the loading is
   a **slope estimated from a time-series regression** of a stock on a factor. In BFRE `X` is an
   *observed characteristic*, standardised, known before any regression is run — and it is the
   regression's *input*, not its output. This is exactly what L7's boss round is about ("why BFRE
   estimates cross-sectionally rather than by time-series betas, and what that choice costs").
3. **Using it while quoting the paper.** "The paper says the Volatility loading is…" — the paper says
   no such thing and never uses the word. Dock for a fabricated attribution; that is precisely the
   failure mode `notes/`'s own audit caught.

**Follow-up**
> "In a textbook factor model the loading is estimated from a regression. In BFRE, `X` is not
> estimated. So where does `X` come from — and what breaks in the standard-error story if you pretend
> a measured characteristic is a fitted coefficient?"

Pass: `X` comes from fundamentals, analyst estimates and price history, standardised to z-scores
(pp. 9, 10, 39). Tier-4 extra: if `X` were itself estimated it would carry its own uncertainty, which
would have to propagate into the uncertainty of `f`; BFRE treats `X` as **known**, so all the
uncertainty in a t-statistic is uncertainty about `f` alone. **[GM INFERENCE]** — the paper does not
discuss errors-in-variables anywhere; do not attribute this to the paper.

**Difficulty:** trivially easy as a synonym; the L7 contrast underneath it is the hard part.

---

### 7. DESIGN MATRIX — unlocks at **L3** (The Second Dial)

**Fire this**
> "You can't put the market, a full set of industry dummies and a full set of country dummies in the
> same design matrix and expect it to invert. That's three intercepts."

**Plain English**
The table of inputs. One row per stock, one column per factor, filled with that stock's exposures.
It is the whole left-hand side of the regression laid out as a grid — everything the model is allowed
to use to explain returns. In BFRE it is `X`.

**Mechanism required before the word**
**L3.** With one column there is no matrix and no reason for the word. At L3 the player has two
columns and two simultaneous balance conditions, and has solved a 2×2 normal-equation system by hand
in fractions. That is the moment "a grid of columns" becomes an object worth naming.

**In the paper**
> **The phrase "design matrix" does not appear anywhere in the 65 transcribed pages.** Checked by
> grep. `X` is called "**factor exposures**" — p. 24, where-list under (1.7): "`X` : set of factor
> exposures based on asset characteristics".

The **structure** of `X` is described in detail and is unusually interesting:
- p. 30 — "Industry, country and currency factor exposures are assigned using **dummy variables**,
  e.g. all assets with exposure to the same industry factor receive the same risk from that
  exposure." **`notes/` audit finding #6 is important here: styles are explicitly NOT in that list.**
  An earlier draft of the digest wrongly implied style exposures were dummies; it was corrected. Do
  not reintroduce the error.
- p. 4 — every equity asset has **unit exposure** to the market factor. So `X` has a column of ones.
- p. 6 — "Every asset is assigned a unit exposure to [a] single currency factor at any point in
  time", via a one-to-one country→currency mapping.
- p. 26 — **the identification problem, in the paper's own words:** "This specification is not
  uniquely identified as there are an infinite number of possible solutions. The reason for this lies
  in the fact that, for each asset, there exist **three intercept terms** – the market factor, an
  industry factor, and a country factor. Every asset has unit exposure to these three factors. This
  can be resolved by adding **two linear restrictions** … which reduces the intercept terms from
  three to one. This identification simply represents a **rotation** of the factor returns. It does
  not impact the efficacy of the risk model."
- p. 26, eq. (1.10) — the two restrictions: the square-root-cap-weighted average industry factor
  return is zero, and likewise for countries. Consequence, in the paper's words: "the industry and
  country factors are **net of the market factor return**, which impacts their interpretation … if
  asset returns across EMEA are mostly positive on a given day and UK assets are also up but by less
  than the average return over the region, then the **UK factor return will be negative**."
  **Transcription caveat:** both summation indices in (1.10) are printed as `j` while the second
  summand is subscripted `k` — `notes/` re-verified at 6× and calls it a **source typo**, not a
  reading error. Carry that forward; don't silently fix it.
- p. 26 — single-country models (Japan) have no country factors, so **only one** restriction is
  needed.
- p. 26 — a second printed inconsistency to carry forward: in the where-list for (1.9) the symbol
  `X_Mkt f_Mkt` is paired with the description "**Style** Exposures and Factor Returns", and the
  Style row is simply **absent**. `notes/` re-verified at 4×; it is an error in the source.

**THE TELL**
1. **Thinking it holds the returns.** It holds only the predictors. `r` is separate.
2. **Thinking "design" means it was optimised.** It is an old experimental-design word — the design
   is the *arrangement of the experiment*, i.e. which inputs each observation got.
3. **Not seeing the dependency.** This is the tell that matters: a player who cannot look at
   [market column of ones] + [complete set of industry dummies] + [complete set of country dummies]
   and see that the industry columns sum to the market column, and so do the country columns, has not
   internalised L4 either. Two exact linear dependencies ⇒ infinitely many solutions ⇒ the paper's
   two restrictions.
4. **Calling the fix "dropping a factor".** It isn't. p. 26: it is a **rotation** and it "does not
   impact the efficacy of the risk model" — the fitted values are identical, only the *labels on the
   split* change.

**Follow-up**
> "BFRE's `X` has a market column of all ones, a complete set of industry dummies and a complete set
> of country dummies. Add the industry columns up. Now add the country columns up. What have you got,
> what does it do to the model, and what did BFRE do about it?"

Pass: both sums equal the market column; three intercepts; infinitely many solutions; two linear
restrictions on the factor *returns* (p. 26, eq. 1.10) — not on the exposures. Tier-4 extra: they
volunteer that the restriction changes what a country factor return *means* (net of market), and
give the UK/EMEA example.

**Difficulty:** L3 for the object, L4 for the dependency. The identification argument is the
hardest thing on this page and is worth an entire session.

---

### 8. DEGREES OF FREEDOM — unlocks at **L6** (The Verdict)

**Fire this**
> "A hundred and four weekly observations and seventy-odd factors — you've got almost no degrees of
> freedom left, which is why those correlations move around so much."

**Plain English**
How many independent pieces of information you still have *after* the fit has spent some of them.
Fitting `k` numbers to `n` data points uses up `k` of them: `n − k` remain to say anything about how
big the leftovers really are. It is the honest denominator.

**Mechanism required before the word**
**L6.** The player must have derived a standard error from scratch and be able to say **why the
denominator is `n − k` and not `n`** — the same nudge argument as L1, applied to the question "how
much of the miss did I manufacture by fitting?". Do not hand over the phrase before that; before
L6 it is "how much information is left over".

**In the paper**
> **The phrase "degrees of freedom" does not appear anywhere in the 65 transcribed pages.** Checked
> by grep.

The machinery is present and countable:
- p. 8 — t-statistics used as the factor-selection criterion; "We consider an absolute t-statistics
  in excess of **2** as statistically significant" (grammatical error is in the original). A t-stat
  is meaningless without a df, and the paper never states one.
- p. 32 — factor efficacy from "the proportion of significant t-statistics"; "the majority of factors
  are significant more than **10%** of time over the research history".
- p. 27, p. 28, Table 1.3 — the observation counts that *are* stated: factor covariance default WKL
  uses **104 weeks** with a **26-week** half-life; specific risk daily uses **375 days**, weekly
  **104 weeks**.
- p. 57 — Table 1.5, NAMR industry schema: **54 industry factors** (`notes/`: "my count" — the total
  is **not printed**). p. 61 — Table 1.11, WRLD: **49 industry factors**, again the transcriber's
  count.
- p. 10, Table 1.2 — the NAMR model shows the market factor plus **12** style factors.

**[GM INFERENCE], and you must present it as one.** The paper never prints a total factor count for
any model. Adding the counts above for NAMR — 1 market + 12 styles + 54 industries + a small number
of core countries + currency factors — gives something on the order of **70**, against **104** weekly
observations for the default factor covariance matrix. That is a legitimate, arithmetic-traceable
setup for the L8 boss round, but the "≈70" is *your* addition of `notes/`'s own hand counts, not a
figure from the paper. Say that out loud at the table.

**THE TELL**
1. **"It's the number of data points."** That is `n`, not the degrees of freedom.
2. **`n − 1` with no explanation.** They know the formula from a school variance and cannot say what
   the 1 paid for. Ask "what did you spend it on?" — the answer is the mean you estimated.
3. **Treating it as a vague quality ("the model has more freedom")** rather than a count.
4. **Applying it to the wrong regression.** The cross-section has thousands of stocks and ~70
   factors — degrees of freedom are not the binding constraint there. The **time-series** covariance
   estimate has 104 observations. A player who says "we don't have enough degrees of freedom in the
   cross-sectional regression" has aimed the worry at the wrong place.

**Follow-up**
> "Two estimates. One: a daily cross-section, three thousand stocks, seventy factors. Two: a factor
> covariance matrix, one hundred and four weekly observations, seventy factors. Which one is in
> trouble, and why is it not the other one?"

Pass: the second. 3000 − 70 leaves plenty; 104 observations to pin down a 70×70 object does not.
Tier-4 extra: they notice that a covariance matrix needs `70×71/2 = 2,485` distinct numbers, and that
104 observations cannot possibly determine 2,485 quantities — so the matrix is **structurally**
rank-deficient or nearly so, which is L8's boss round and §3.12's follow-up.

**Difficulty:** the count is easy; *why the subtraction* is the L6 origin question and is where most
textbooks skip a step. Victory Condition 3 names this one explicitly.

---

### 9. STANDARD ERROR — unlocks at **L6** (The Verdict)

**Fire this**
> "The coefficient's fine, it's the standard error that blew out. `t` went from six to under one and
> nothing changed in the exposures."

**Plain English**
How much your *estimate* would jump around if you re-ran the same procedure on a fresh sample of the
same size. It is a standard deviation — but of the estimate, not of the data. It shrinks as you get
more data, roughly like `1/√n`. A t-statistic is just "estimate ÷ its own standard error": how many
of its own wobbles away from zero the answer sits.

**Mechanism required before the word**
**L6**, and only L6. The player must be able to derive it, not quote it — Victory Condition 3 calls
this out by name ("where a standard error comes from"). They should also be able to show
`t² = (S²/Q)/σ²` and recognise `R²` and `t²` as the same fact twice (L6 boss + §8 CALL BACK).

**In the paper**
> **The phrase "standard error" does not appear anywhere in the 65 transcribed pages.** Checked by
> grep. The one occurrence in `notes/` is the **transcriber's own comment** on the bibliography page
> (p. 65): "[26] Newey–West is the only estimation-technique citation on this page — consistent with
> HAC standard errors." That is a `notes/` inference about a reference list, not paper text.

What the paper does instead:
- Uses t-statistics everywhere without ever printing the formula (pp. 8, 14, 32).
- p. 8 — the threshold `|t| > 2`; and, tellingly, the **average squared t-statistic**, computed
  specifically "to distinguish between factors with t-statistics close to +/− 2 and those that are
  significantly higher."
- p. 14 — inclusion threshold: a style needs its **proportion of significant t-stats above 10%**.
- p. 25 — the weighting choice is *about* the standard error without ever saying so: assets are
  weighted by **square-root of market capitalisation** because "square-root of market capitalisation
  **adjusts for heteroskedasticity** based on the observation that higher residual (specific) risk is
  typically correlated with smaller market capitalisation assets" (footnote 14: schemes using the
  reciprocal of each asset's residual variance "provide similar results").
- p. 27, p. 28 — **Newey–West [26]** is used to aggregate daily returns into forecasts "that account
  for serial correlations in the daily data". Reference [26] (p. 65) is "A Simple, Positive
  Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix".
- p. 56, **Table 1.4 "Inventory of all substyles investigated"** contains a style called **Random**
  with one substyle, **"Random Substyle"** — printed, in the table, verbatim. The page carries **no prose
  at all**, so the paper never says what it is for. `notes/` glosses it as "the classic placebo/control
  descriptor for a factor-selection procedure" — **that reading is the transcriber's, not the paper's**,
  and you must say so. But the object itself is real and printed, and it is the single best teaching
  artefact in 65 pages for what a t-statistic is actually protecting you against: run a selection
  procedure over 108 candidate substyles at a 5%-ish significance bar and roughly five of them will clear
  it by luck. A deliberately meaningless column tells you whether yours is one of them.
  (Counts: **18 styles, 108 substyles** — `notes/`'s count from the printed rows; **no totals are printed**.)
- **The best line in the paper for this term is on p. 6, footnote 8.** Currency factor returns are
  "**calculated**" from exchange rates and risk-free rates rather than "estimated", and the footnote
  says why: "Note the use of the term 'calculated' here, as opposed to 'estimated' — **no uncertainty
  is involved in their construction**." A quantity that is calculated has no standard error. That
  single footnote is the cleanest illustration in 65 pages of what a standard error is *for*.

**THE TELL**
1. **Confusing it with standard deviation.** "The standard error of the returns is 20%." No — that
   is a standard deviation of data. Standard error attaches to an *estimate*. This is the single most
   common misuse of the word in the English language and it is instantly audible.
2. **No `√n`.** They cannot say what makes a standard error small. Twice the data, roughly `1/√2`
   the standard error — and they should recognise `√n` as an old friend from L6's derivation.
3. **"t > 2 means the factor is important."** It means the estimate is large relative to *its own*
   noise. A microscopic effect measured very precisely clears `t = 2` easily. The paper's own
   average-squared-t metric (p. 8) exists because "significant" is too blunt.
4. **Quoting a standard error from the paper.** There isn't one. Not a single standard error, VIF
   value, bias statistic or R² *number* is printed anywhere in the document. Only thresholds.

**Follow-up**
> "BFRE calls currency factor returns *calculated*, not *estimated*, and the footnote says no
> uncertainty is involved. What is the standard error of a calculated factor return, and what does
> that tell you about what a standard error actually measures?"

Pass: zero — there is nothing to be uncertain about; it is arithmetic on observed exchange rates. So
a standard error measures uncertainty *about the estimate*, not variability *of the thing*. Currency
factor returns are extremely variable and have no standard error at all.

**Second follow-up**
> "Two factors, both estimated at +0.20% this month. One has `t = 6`, the other `t = 0.4`. Nothing
> differs in the exposures. Which number in the arithmetic carries the difference, and where does it
> come from?"

**Difficulty:** deriving it from scratch is genuinely the hardest thing at L6 and one of the four
things Victory Condition 3 singles out. Say so.

---

### 10. COVARIANCE MATRIX — unlocks at **L8** (The Weather Map); *covariance* itself at **L5**

**Fire this**
> "We're re-estimating the factor covariance matrix off a twenty-six-week half-life, so don't be
> surprised if the correlations move after a vol spike."

**Plain English**
A square table. Down the diagonal, how much each thing wobbles (variance). Off the diagonal, how much
each pair wobbles *together*. It is the object that lets you turn a set of positions into one risk
number, because risk does not add — it adds with the cross-terms.

**Mechanism required before the word**
- **L5** — covariance itself arrives here, when centering turns `Σxr/Σx²` into `Cov/Var`. That is the
  player's first covariance and it should be called back explicitly at L8 (§8 CALL BACK).
- **L8** — building `F` from a factor-return time series.
- Do not say "matrix" before L3, and do not say "covariance matrix" before L8.

**In the paper — three different matrices, and mixing them up is fatal**

| Symbol | What | Size | Page |
|---|---|---|---|
| `F` | **factor** covariance matrix | number of factors squared — small | p. 24, eq. (1.8) |
| `Σ` | **asset** covariance matrix | number of assets squared — enormous | p. 24, eq. (1.8) |
| `Δ` | specific risk matrix, "a diagonal matrix of asset specific risk forecasts" *(but see p. 27)* | assets squared, near-diagonal | p. 24 |

- p. 24, eq. (1.8): `Σ = X F Xᵀ + Δ`. **The game's rules write this as `V = XFXᵀ + D`. The paper
  writes `Σ` and `Δ`.** Tell the player at L10, or they will think they've caught an error.
- p. 2 — the reason the whole model exists, in the paper's words: BFRE "imposes far more structure on
  the asset covariance matrix, reducing the modelling problem to a smaller set of factors, which
  capture the most important sources of asset return commonality."
- p. 27 — `F` is built from **daily factor returns starting March 1996**, exponentially weighted.
  Default for all BFRE models is **WKL (weekly long-term): 104 weeks of factor returns, 26-week
  half-life**. Technical details are **deferred to an external document** ("BRS Covariance Matrix
  Estimation documentation") that is not in this paper — a real gap for L12.
- p. 27, p. 28 — Newey–West [26] serial-correlation adjustment; Table 1.3 gives the specific-risk
  parameters.
- p. 11 — Figure 1.3 is a **correlation** matrix (12×12, unit diagonal), not a covariance matrix.
  Useful for drilling the difference.

**THE TELL**
1. **Saying "correlation matrix" for "covariance matrix" and vice versa.** A correlation matrix has
   ones on the diagonal and is unitless; a covariance matrix has variances on the diagonal and
   carries squared units. If the player cannot say what is on the diagonal of `F` **and in what
   units** (percent-squared, or variance per period), they are guessing.
2. **Confusing `F` with `Σ`.** `F` is dozens across. `Σ` is tens of thousands across. Nobody ever
   builds `Σ` — the entire point of the factor model is that you never have to. A player who talks
   about "estimating the asset covariance matrix" in BFRE has missed the thesis on p. 2.
3. **Treating it as just a table of numbers.** A covariance matrix must be positive semi-definite —
   every portfolio you can form out of it must come back with non-negative variance. That constraint
   is why the Newey–West paper's title (ref [26], p. 65) leads with "**A Simple, Positive
   Semi-Definite**…". A player who does not know a covariance matrix can be *invalid* has not built
   one.
4. **Ignoring the decay.** "The covariance matrix" is not a fact about history; it is a weighted
   opinion about it. 26-week half-life means data from a year ago counts about a quarter as much.

**Follow-up**
> "`F` for the NAMR model. How many rows, roughly, and what is on the diagonal in what units? Now
> `Σ = XFXᵀ + Δ` — how many rows does `Σ` have, and why does nobody ever build it?"

Pass: `F` is roughly the factor count square (their own count from the paper's tables, flagged as a
count and not a printed figure); diagonal = factor variances, in squared return units. `Σ` is the
asset count square — thousands — and it is never built because `X F Xᵀ` reproduces it on demand from
a much smaller object. Tier-4 extra: portfolio risk only ever needs `wᵀΣw`, which you compute as
`(Xᵀw)ᵀ F (Xᵀw) + wᵀΔw` — aggregate to factor exposures first, and `Σ` never appears.

**Difficulty:** L8. Moderate — but the positive-semi-definite requirement is the doorway to
eigenvalues and is graduate-level.

---

### 11. SHRINKAGE — unlocks at **L8 boss round**. **GRADUATE-LEVEL — say so.**

**Fire this**
> "Thin countries get shrunk toward the prior, otherwise a five-stock country factor return is just
> five stocks' specific returns wearing a hat."

**Plain English**
Deliberately pulling a noisy estimate part-way toward something steadier — a prior, an average, a
theoretical value — and accepting that you are now slightly wrong on purpose, because the alternative
was being wildly wrong at random. You trade a little bias for a lot of variance.

**Mechanism required before the word**
**L8 boss round**, which is stated in the rules as: "Show why a covariance matrix estimated from
fewer months than factors is structurally broken, and what shrinkage does about it." The player must
first *feel* the instability — they cannot appreciate a cure for a disease they have not seen.
Prerequisites: L6 (standard error, so they know what "noisy" means quantitatively) and L8 (`F`).

**In the paper**
> **The word "shrinkage" appears in the 65 pages only inside a bibliography title:** reference **[7]**
> on p. 64 — R. Tibshirani, "Regression **shrinkage** and selection via the lasso", *J. R. Statist.
> Soc. B*, 1996. Checked by grep over all of `notes/`.

The paper's actual shrinkage-shaped device, and it is not where a textbook would put it:
- p. 36 — "The estimation procedure uses **thinness corrections for country and industry factors**
  where limited, or no data exists to reliably estimate those factor returns. We impose the thin
  country/industry correction by **adding a Bayesian prior**, which in essence **diverts the estimated
  country/industry return away from the sample factor return and towards a theoretical prior**. In
  its purest sense this can be understood as capturing a **true** country/industry return rather than
  **asset-specific** returns."
- **`notes/` flags the gap and you must carry it:** "the prior's form, strength and shrinkage
  parameter are **not** specified anywhere on this page." There is no number to trace. Under §8 (NO
  NUMBER WITHOUT ITS ORIGIN) you cannot teach a figure here; teach the mechanism with clearly-labelled
  invented numbers, per §8 FLAG UNREADABLE SOURCE.
- p. 8 — the paper explicitly **names shrinkage-family alternatives it did not adopt** for factor
  selection: Bayesian priors (Kadane and Lazar [6]), **LASSO** (Tibshirani [7]), **LARS** (Efron [8]),
  **Group Lasso / Group LARS** (Yuan and Lin [9]), and **Ridge**. Its stated reason: those "are purely
  statistical in nature and rely heavily on historical data", whereas BFRE "starts with a economically
  intuitive industry definition, and blends this with sophisticated statistical analysis as well as
  up-to-date market insights and forward-looking views" (*sic* on the grammar).
- p. 28 — a second, different smoothing device that is *not* called shrinkage but behaves like one:
  the specific-risk **cross-sectional overlay**, where a young asset's forecast is "a **weighted sum**
  of its time-series forecast (if it exists) and its cross-sectional forecast", the weight moving to
  the time-series forecast as data accumulates, and in the limit to 1. **The weighting function's
  form is not given.**

**A discrepancy inside `notes/` that you must not repeat.** The commentary on the bibliography page
(p. 64) says the reference list "confirms the model-selection machinery used in the body: classical
subset selection *plus* lasso / LARS / group-lasso **shrinkage**". That is the transcriber's gloss and
it **contradicts p. 8**, where the paper names those same methods explicitly as approaches it did *not*
take. Trust p. 8 — it is body text and it is quoted verbatim in `notes/`. Treat the p. 64 line as an
over-read of a reference list.

**The honest headline for the table:** BFRE does **not** state anywhere that it shrinks the factor
covariance matrix. Textbook shrinkage (Ledoit–Wolf and relatives) shrinks `F` or `Σ` toward a
structured target. BFRE's one stated Bayesian prior shrinks *thin country and industry factor
returns*. Different object, different stage of the pipeline. A player who says "BFRE shrinks the
covariance matrix" is inventing a claim the paper does not make.

**THE TELL**
1. **"Shrinkage means making the numbers smaller."** It means moving them *toward a target*. If the
   raw estimate is below the target, shrinkage raises it. This is the definitional tell and it catches
   nearly everyone.
2. **Cannot name what is being traded.** Shrinkage buys a reduction in variance by paying in bias.
   A player who says shrinkage "makes the estimate better" without naming the price has memorised.
3. **Cannot say where the target comes from.** "Toward a theoretical prior" (p. 36) is the paper's own
   phrase and the paper never says what the prior is. A player who invents one is doing exactly what
   `notes/`'s audit exists to catch.
4. **Assuming it is applied to `F`.** See above.

**Follow-up**
> "BFRE shrinks a thin country's factor return toward a prior. Suppose the prior is the region's
> average, which is +1%, and the raw estimate for that country this week is −4%. Does shrinkage make
> the number smaller?"

Pass: no — it moves it *up*, toward +1%. Tier-4 extra: and the reason the paper gives for doing it at
all is on p. 36 — with only a handful of assets, the "country factor return" is mostly a few stocks'
specific returns misattributed, so the prior is there to stop specific risk from leaking into the
common-factor block.

**Difficulty:** **graduate-level.** Bias–variance trade-off, Bayesian priors, Stein-type shrinkage.
Announce that before you start (§8 BE HONEST ABOUT DIFFICULTY). Do not let the player conclude they
are slow.

---

### 12. EIGENVALUE — unlocks at **L8**. **GRADUATE-LEVEL — say so.**

**Fire this**
> "The first eigenvalue is eating about half the variance — that's just the market showing up in the
> factor block again."

**Plain English**
Take a cloud of data with a covariance matrix. There is one direction in which the cloud is most
stretched. The **eigenvector** is that direction; the **eigenvalue** is how much variance lives along
it. Do the direction with the second-most stretch, at right angles to the first, and so on. The
eigenvalues are the variances of those directions, and they add up to the total variance in the
matrix.

**Mechanism required before the word**
**L8**, exactly as the rules frame it: "explain what an eigenvalue is by building it from *the
direction with the most wobble*." Build the direction first, numerically, on a 2×2. The name arrives
only after the player has found a most-wobbly direction by hand.

**In the paper**
> **The word "eigenvalue" does not appear anywhere in the 65 transcribed pages. Neither does
> "eigenvector", "eigen-" anything, "principal component", or "PCA".** Checked by grep over all of
> `notes/`.

**This matters, and you must say it plainly at the table.** BFRE is a **fundamental** factor model:
the factors are named, economically interpretable characteristics chosen on four stated criteria
(p. 4: Interpretability, Explanatory Power, Consistency, Efficacy). It is the *opposite design choice*
from a statistical model that extracts unnamed factors as the leading eigenvectors of a return
covariance matrix. The paper's whole first page of methodology is an argument for interpretability
over statistical extraction, and p. 8 makes the same argument again against LASSO/LARS/Ridge.

So: teach eigenvalues at L8 because they are the only honest way to explain **why a covariance matrix
estimated from too few observations is structurally broken** — but tell the player they are learning
a diagnostic lens the paper never picks up, not a BFRE mechanism. The closest the paper comes is
reference [26] (p. 65), Newey–West, whose title begins "A Simple, **Positive Semi-Definite** …" —
positive semi-definite is precisely the statement "no eigenvalue is negative", though the paper never
unpacks it.

**THE TELL**
1. **"The eigenvalue is the direction."** No. The eigen**vector** is the direction; the
   eigen**value** is the amount of variance along it. Swapping them is the classic.
2. **Assuming the model does PCA.** A player who says "BFRE extracts the factors from the covariance
   matrix" has described a different family of model entirely and would be corrected in the first
   thirty seconds of a real conversation.
3. **Not knowing what a zero or negative eigenvalue means.** A zero eigenvalue means there is a
   portfolio the matrix says has **exactly zero risk** — which you could lever without limit. A
   negative one means a portfolio with negative variance, which is nonsense and means the matrix is
   invalid. This is the concrete content of L8's boss round.
4. **Thinking they are a property of the data rather than of the matrix.** Different weighting
   schemes on the same history give different matrices and different eigenvalues — which is exactly
   why the 26-week half-life on p. 27 is a modelling choice, not a fact.

**Follow-up**
> "You estimate a `K × K` covariance matrix from `T` observations, and `T < K`. How many eigenvalues
> are exactly zero, and what portfolio does a zero eigenvalue hand you?"

Pass: at least `K − T` of them are zero. A zero eigenvalue is a direction — a portfolio — the matrix
claims has zero variance. Lever it up and the model reports no risk at all. That is not conservatism,
it is a hole. Tier-4 extra: and this is why a covariance matrix estimated from fewer periods than
factors is *structurally* broken rather than merely imprecise — no amount of care in the estimation
fixes a rank deficiency; only structure (shrinkage, a factor model, a target) does.

**Difficulty:** **graduate-level.** Announce it. The 2×2-by-hand construction is doable at 12th
standard with strong algebra; the general theory is not, and does not need to be.

---

### 13. TRACKING ERROR — unlocks at **L10** (The Assembly); used at **L11** (The Desk)

**Fire this**
> "Two-ninety-nine of tracking error against a benchmark running at fifteen — that's a
> benchmark-hugging book with one big style tilt in it."

**Plain English**
The volatility of the *difference* between your portfolio's return and the benchmark's return. Not
how far behind you are on average — how much the gap jumps around. A fund that beats its benchmark by
exactly 3% every single month has enormous outperformance and almost **zero** tracking error.

**Mechanism required before the word**
**L10.** `V = XFXᵀ + Δ` must exist and the player must be able to compute `wᵀVw` for a weight vector.
Tracking error is then just that computation run on the **active weights** `w_P − w_B`. Not before —
otherwise it is a word for a thing they cannot compute.

**In the paper**
> **The phrase "tracking error" does not appear anywhere in the 65 transcribed pages.** Checked by
> grep. **The paper's word is "Active Risk."**

- p. 34 — "Top-line risk numbers are shown along the top of the report: **Active Risk, Portfolio Beta,
  Portfolio Risk and Benchmark Risk**. **Active Risk is then decomposed along the different factor
  blocks** … The report shows that the Active Risk is **split equally between common factors and stock
  specific sources**."
- p. 35 — the EDR banner, re-verified at 9× during `notes/`'s audit: **Active Risk 2.99% | Portfolio
  Beta 1.02 | Portfolio Risk 15.62% | Benchmark Risk 14.98%**, base currency EUR. **Carry the
  caveats:** `notes/` records residual doubt on the middle digit of 2.99 (2.89 not fully excluded) and
  the last digit of 15.62 (15.67 not fully excluded). 14.98 and 1.02 are clean.
- p. 29 — "active portfolio managers" vs "index tracking portfolios" is the paper's only use of
  "tracking", and it is about *which specific-risk methodology suits which client*, nothing to do with
  tracking error.

**The arithmetic hook — the best single number in the paper for this term.**
`15.62 − 14.98 = 0.64`. Active Risk is **2.99**. If active risk were "the difference between the two
risks", it would be 0.64 and it is not — it is about **4.7 times** larger. That is because risks do
not subtract; variances combine with a cross-term. Working backwards from
`σ_A² = σ_P² + σ_B² − 2ρ σ_P σ_B` gives an implied portfolio–benchmark correlation of
**ρ ≈ 0.982**, and that value is stable at ≈ 0.982–0.983 across every combination of the digits
`notes/` could not fully exclude (15.62/15.67 and 2.99/2.89). Arithmetic verified in exact rationals.
**[GM INFERENCE]:** the paper does not print ρ and does not print this relationship; the derivation is
yours. Present it as a check you ran, not as a paper claim.

**THE TELL**
1. **Thinking it is a mean, not a spread.** "We're tracking 3% behind." That is a return shortfall.
   Tracking error is a standard deviation.
2. **Thinking it is the difference of the two volatilities.** The 0.64 vs 2.99 arithmetic above kills
   this on the spot, using the paper's own banner.
3. **Not knowing the house word.** In a BFRE conversation the report says **Active Risk**. A player
   who does not map the two instantly, in both directions, fails the register half of Victory
   Condition 2.
4. **Thinking low tracking error means low risk.** The book on p. 35 has 2.99% active risk and
   15.62% total risk. Tracking error says nothing about the risk you inherited from the benchmark.

**Follow-up**
> "Portfolio risk 15.62. Benchmark risk 14.98. Active risk 2.99. Why isn't active risk 0.64?"

Pass: because risk is a standard deviation and standard deviations do not subtract — variances add
with a `−2ρσ_Pσ_B` cross-term, and with `ρ` near one the two large risks cancel almost entirely,
leaving a small residual that is nonetheless much larger than the difference of the two numbers.
Tier-4 extra: they invert it and produce ρ ≈ 0.98 themselves, and then say what a ρ of 0.98 means about
the manager's behaviour (they are hugging).

**Difficulty:** the concept is L10-easy once `V` exists. The variance-cross-term intuition is exactly
the L10 "explain every matrix multiplication as a sentence" skill.

---

### 14. MARGINAL CONTRIBUTION — unlocks at **L11** (The Desk)

**Fire this**
> "Its weight is small but the marginal contribution is the biggest in the book — it's correlated with
> everything else you own."

**Plain English**
How much total portfolio risk would change if you nudged this one position up a little. Not how risky
the position is on its own — how much risk it *adds to this particular portfolio*, which depends
entirely on what else is in there. A position that hedges the rest of the book can have a marginal
contribution near zero or below it.

**Mechanism required before the word**
**L11.** The player must already have `V` (L10) and must have computed portfolio risk by hand for a
3-stock book. Marginal contribution is then the nudge argument from **L1**, applied one last time — and
you should say so explicitly (§8 CALL BACK): at L1 they nudged `b` and watched `SS` move; here they
nudge `w_i` and watch `σ_P` move. Same tool, new clothes.

**In the paper**
> **The phrase "marginal contribution" does not appear anywhere in the 65 transcribed pages.** Checked
> by grep. The word "marginal" occurs three times, and only one is relevant: p. 7, where residuals of a
> coarse industry fit are regressed on a finer schema level "to compute the **marginal benefit** of
> increasing granularity" — a different idea entirely.

What the paper reports is **contribution**, which is the closely related object marginal contribution
is used to build:
- p. 34 — each factor block's bar chart "displays the **active exposure** together with the
  **contribution to active risk**."
- p. 35 — the axes are literally labelled "**Contrib. (% of Act. Risk)**" (style, industry, country,
  FX panels) and "**Contribution (%)**" (asset panel); the legend series are "Contrib. to Act. Risk"
  and "Contrib. to Spec. Risk".
- p. 35 — the pie "Risk Contributions by Block": **Specific 50 / Style 25 / Industry 14 / Country 6 /
  FX 4 / Act Sec 1**, and **these sum to exactly 100**. `notes/` marks the 1% as `[INFERRED]` — the
  glyph reads 1 or 2, and only the sum-to-100 argument selects 1. **Carry that.**
- p. 35 — Top Style Contributions: Volatility ≈ 11% of active risk with an exposure of ≈ +0.42
  standard deviations; Momentum ≈ 6; Size ≈ 3.5; Yield ≈ 3; Reversal ≈ 1. **All bar and dot magnitudes
  on p. 35 are `notes/` pixel measurements, ±10%, not printed values.** Say so every time you use them.

**The key structural fact, and it is [GM INFERENCE] as to mechanism:** contributions that sum to
exactly the total are what you get when you take each position's marginal contribution and multiply it
by that position's weight (an Euler decomposition, which works because risk is homogeneous of degree
one in the weights). The paper reports the *result* — a decomposition summing to 100% — and never
describes the machinery. Attribute the 100% to p. 35; attribute the mechanism to your own derivation
at L11.

**THE TELL**
1. **"It's how much risk that position has."** That is standalone volatility × weight, and it is a
   different number. Marginal contribution depends on the position's correlation with **the rest of the
   book**, which standalone risk cannot see. This is the whole point of L11's boss round — the PM who
   insists their portfolio is diversified.
2. **Not knowing contributions sum to the total.** If they think it is just a ranking, they will not
   understand why the EDR pie is a pie.
3. **Thinking contributions must be positive.** A genuine hedge has a negative marginal contribution
   — adding more of it *reduces* total risk. Note the paper's own FX panel on p. 35 shows a bar at
   ≈ **−0.05%** of active risk, i.e. a small negative contribution (`notes/` pixel reading, ±10%).
4. **Confusing it with exposure.** The EDR panels deliberately plot both on the same chart with two
   different axes precisely because they are different (p. 35). A large exposure with a small
   contribution is normal and interesting.

**Follow-up**
> "Name me a position whose marginal contribution to risk is negative. What has to be true about it,
> and what happens to the total if I double it?"

Pass: a position that moves against the rest of the book — a short in something the portfolio is long,
a hedge, a low-or-negatively-correlated diversifier. Doubling it reduces total risk *at first*, and
they should say "at first", because as it grows it stops hedging and starts dominating, and the
marginal contribution crosses zero. Tier-5: the crossing point is the risk-minimising weight.

**Difficulty:** L11. The Euler/homogeneity argument for why the contributions add to exactly the total
is graduate-adjacent — you can get there with the nudge argument and no calculus, but say plainly that
the general theorem is beyond scope.

---

### 15. MULTICOLLINEARITY — unlocks at **L4** (The Collision). **GRADUATE-LEVEL — say so.**

**Fire this**
> "Size and Liquidity run at nought-point-seven-four in the exposure correlations, so the split between
> those two factor returns is going to be unstable. Look at the VIFs before you read anything into one
> month of Liquidity."

**Plain English**
Two or more input columns carry nearly the same information. The model can still predict fine — the
fitted values are solid — but it cannot *decide* how to divide the credit between them. So the
individual coefficients swing around wildly from period to period even though nothing real has changed.
Take it to the extreme, where two columns are identical, and there are infinitely many answers, all
equally good.

**Mechanism required before the word**
**L4**, exactly as the rules frame it: "Show that a coefficient means *what this column explains that
no other column already explained*; explain the determinant going to zero." Boss round: "Build a
dataset where the naive one-at-a-time answer is catastrophically wrong, and quantify how wrong."
The player must have *seen* the swing before they get the word.

**In the paper — and here the paper's own sentence is nearly perfect, so use it verbatim**
- p. 32 — "The final set of diagnostics are **variance inflation factors**. These help diagnose issues
  relating to **multicollinearity between the style factors**. **If style exposures are too closely
  correlated then the regression procedure will encounter problems in apportioning the factor return
  between them. This can result in significant instability in the factor return estimates through
  time**¹⁶. In order to guard against these effects, variance inflation factors were reviewed over the
  research history and **were found to be well within suitable thresholds**."
  - Note precisely what the paper says the damage is: **apportioning** and **instability**. It does
    *not* say bias. That is correct, and it is the discriminating fact — see the tell.
  - **`notes/` flags: no numeric VIF values and no thresholds are reported anywhere.** "Well within
    suitable thresholds" is the entire evidence. Prime L12 material.
- p. 32, **footnote 16** — the extreme case: "In the most extreme case, where factor exposures are
  perfectly correlated, **identification issues will exist causing the estimation process to fail**."
  That is the determinant going to zero, in the paper's own words.
- p. 11, **Figure 1.3** (NAMR, Dec 2013) — the live evidence, and the numbers are verified:
  **Size–Liquidity 0.74** (highest off-diagonal), Earnings Yield–Profitability **0.64**,
  Volatility–Dividend Yield **−0.46**, Size–Volatility **−0.36**.
- p. 14 — the paper discusses the Size/Volatility relationship in prose: "Large volatility exposures
  tend to be associated with small-cap stocks through time … Consequently, portfolios which are
  positively exposed to size are commonly negatively exposed to volatility, and vice versa."
- p. 26 — the *perfect* collinearity case is not hypothetical in BFRE: market + full industry dummies
  + full country dummies are exactly linearly dependent, and the paper fixes it with two restrictions.
  **Different problem, same disease.** Multicollinearity is the near case; identification failure is
  the exact case; they sit on one continuum and the player should be able to say so.

**THE TELL**
1. **"Multicollinearity means the factors are correlated, so drop one."** Two errors in one sentence.
   Correlated predictors are normal and not per se a problem; and dropping one does not recover the
   split, it just imposes a different (and now hidden) answer. BFRE **keeps** Size and Liquidity
   despite 0.74.
2. **"It biases the estimates."** It does **not**. It inflates their variance. The estimates remain
   correct on average; they are just noisy and unstable. The paper agrees with this (p. 32:
   "apportioning", "instability" — never "bias"), which makes it a nice place to show the player that
   the source is on their side.
3. **Confusing collinearity among the *columns* with correlation among the *residuals*.** Different
   problems, different fixes.
4. **Confusing it with correlated factor returns.** Style exposures being correlated (p. 11) and style
   factor *returns* being correlated (Table 1.2, p. 10, e.g. Volatility's 0.84 correlation with the
   market) are different facts about different objects.
5. **Quoting a VIF number from the paper.** There isn't one.

**Follow-up**
> "Size and Liquidity exposures correlate at 0.74. Does that make the Size factor return wrong? If
> not, what exactly does it do to it — and why did they keep both factors?"

Pass: not wrong, just unstable — the *split* between them swings while the combined fit is fine. They
kept both because each has independent explanatory power and the VIFs, per p. 32, stayed within
(unstated) thresholds. Tier-4 extra: they volunteer that "the paper reports no VIF numbers at all,
so I'd want the actual values before I believed it" — that is the L12 instinct arriving early and is
worth bps.

**Second follow-up**
> "What is the difference between the Size/Liquidity situation and the market-plus-industries-plus-
> countries situation on p. 26?"

Pass: degree. 0.74 is *near*-collinearity — solvable but unstable. The intercept problem is *exact*
collinearity — not solvable at all until you add restrictions (footnote 16: the estimation "fails").

**Difficulty:** **graduate-level**, and the rules name it as such. **Frisch–Waugh** — the theorem
underneath "what this column explains that no other column already explained" — is also graduate-level.
Announce both. A 12th-standard player with strong algebra can absolutely build the 2×2 determinant
version by hand; they should not feel slow for finding the general statement hard.

---

### 16. IN-SAMPLE vs OUT-OF-SAMPLE — unlocks at **L12** (The Critique)

**Fire this**
> "R-squared is an in-sample number. The only thing I actually care about is the out-of-sample bias
> statistic on the real books."

**Plain English**
**In-sample**: measured on the very data used to build the model. Always flattering, because the model
was tuned to fit exactly those points. **Out-of-sample**: measured on data the model never saw. The
only kind that is evidence. The gap between the two is how much of your apparent skill was memorisation.

**Mechanism required before the word**
**L12.** The player must be able to name the paper's real weaknesses. Prerequisites: L6 (they must
know that adding parameters *always* raises in-sample fit, which is the same fact as degrees of freedom
being consumed) and L8 (they must have felt an estimate be unstable).

**In the paper**
> **"In-sample" appears nowhere in the 65 transcribed pages. "Out-of-sample" appears exactly once.**
> Checked by grep over all of `notes/`.

- p. 30, the single occurrence, in the Assumptions & Limitations bullet list: "The model should be used
  with care on portfolios covering assets not well represented in the estimation universe.
  **Out-of-sample model back-testing is conducted on a subset of such portfolios** as part of the
  **Quarterly Aladdin Risk Model conference calls**."
- p. 32 — the in-sample diagnostics: R² ("the proportion of cross-sectional variation in asset returns
  explained by the set of common factors"), proportion of significant t-statistics (threshold 10%),
  and VIFs. All computed on the estimation universe over 1996–2013.
- p. 32 — the out-of-sample idea, under its own name in the paper: "One way of testing the accuracy of
  the risk forecasts is to compare the volatility of **realised** returns to **forecast** risks. This
  forms the basis of the **bias statistic**."
- p. 38 — the bias statistic's actual construction: "a rolling window standard deviation of **12
  monthly standardised returns**, and exceptions are flagged using a **95% confidence interval**".
  `notes/` records that the 12 months and the 95% are asserted, not justified. Also p. 38: tail risk
  via proportion of violations of **99% 1-day VaR over the previous 252 days** (footnote 18: consistent
  with UCITS guidelines, following Kupiec (1995)), and benchmarking against **STORM**.
- p. 56 — **Table 1.4** is titled "Inventory of all substyles **investigated**", not "used": it is the
  candidate pool that was screened, and `notes/` records that the page gives **no indication of which
  survived**. It lists **108 substyles** across 18 candidate styles (`notes/`'s count; no totals printed),
  one of which is literally called **"Random Substyle"**. Search that many candidates and some will look
  significant purely in-sample. This is the multiple-testing half of the in-sample problem, and the paper
  hands you the evidence without ever naming the issue.
- **pp. 32–33, and this is the L12 kill shot:** the Model Testing chapter lists an "exhaustive set" of
  test portfolios (pure factor portfolios, cap-weighted estimation universes and carve-outs, cap
  terciles, individual stocks, minimum variance portfolios, active portfolios, "a significant number of
  genuine portfolios") and then **prints not one bias statistic, not one pass/fail criterion, and not
  one summary result.** "More details of the testing are provided by **[27] available on request**."
  `notes/` records this explicitly as a methodological gap.

**THE TELL**
1. **"High R², so it forecasts well."** The deepest confusion available here. R² is a statement about
   how much of *last month's* cross-sectional return spread the factors accounted for. A risk model's
   job is to forecast *volatility*, next month. Those are different quantities, and the paper knows it
   — which is why the bias statistic exists as a separate test on p. 32.
2. **Thinking out-of-sample only means "different stocks".** It primarily means **later in time**. A
   model tuned on 1996–2013 and tested on 1996–2013 is in-sample no matter which stocks you pick.
3. **Not knowing what a risk model is even scored on.** For a return model you score forecast returns;
   for a **risk** model you score forecast *volatility* against realised volatility. If the player
   cannot name the bias statistic as the scoring rule, they have not read pp. 32/38.
4. **Accepting "were found to be well within suitable thresholds" and "available on request".** Both
   phrases appear in the paper (pp. 32, 33). Under §8 (NO NUMBER WITHOUT ITS ORIGIN) a player who
   accepts either without objecting has failed the L12 instinct — and, per the rules, should lose bps
   for accepting a number whose origin they cannot trace, even when the number is absent.

**Follow-up**
> "Name me a model that would score a very high R² on the estimation cross-section and still be
> completely useless for forecasting next month's risk."

Pass: anything with enough free parameters — one dummy per stock is the limiting case, R² = 1 by
construction, zero forecasting content. Tier-4 extra: they connect it to degrees of freedom (L6) —
R² rises mechanically with every column added, so R² alone can never justify adding a factor, which is
exactly why the paper uses *t-statistic persistence over time* (pp. 8, 32) rather than R² to select
factors.

**Second follow-up (the L12 attack)**
> "The Model Testing chapter is two pages, lists nine kinds of test portfolio, and reports zero
> numbers. Defend that as a BlackRock author. Now attack it as a rival."

**Difficulty:** conceptually the easiest term on this list; it is placed at L12 because its *use* is
critical, not because it is hard.

---

## 4. DIFFICULTY HONESTY CARD

Read this out when the relevant term comes up. §2 of the rules: *never soften the difficulty of
genuinely hard material — say plainly when something is graduate-level so the player can calibrate
their own frustration correctly.*

| Material | Level | Say this |
|---|---|---|
| **Multicollinearity** | L4 | "This is a graduate econometrics topic. You will build the 2×2 version by hand and it will be genuinely clear. The general theory is a course." |
| **Frisch–Waugh** (the "what this column explains that no other explains" theorem) | L4 | "Graduate-level. You are getting the mechanism without the theorem, which is the right trade." |
| **Standard error from scratch** | L6 | "Most textbooks skip this derivation. We are not skipping it. It is Victory Condition 3." |
| **Eigen-decomposition** | L8 | "Graduate-level, and the paper never uses it. We are borrowing a lens to see why a covariance matrix can be broken." |
| **Shrinkage / bias–variance** | L8 boss | "Graduate-level. Also: the paper's version is not the textbook's version, and we will do both." |
| **Euler decomposition of risk** | L11 | "The theorem behind contributions summing to the total is beyond scope. The nudge argument gets you there without it." |

---

## 5. PAGE-ANCHOR INDEX

Every page below was read in `notes/` before being cited in this document. Use it to check a claim
mid-round without re-reading the whole file.

| Page | What is there | Terms it serves |
|---|---|---|
| p. 2 | STORM contrast; "imposes far more structure on the asset covariance matrix" | covariance matrix |
| p. 3 | two-pass cross-sectional estimation; daily factor returns from March 1996; specific risk from daily specific returns | cross-sectional regression, specific risk |
| p. 4 | four factor-selection criteria; unit market exposure; market factor return = cross-sectional average (sqrt-cap weights, fn 2); "market factor exposure ≠ market beta"; S&P 500 on NAMR market: β = 0.99, R² = 91%. **Handwritten reader annotations in the margin — not printed text** | exposure, eigenvalue (why not PCA) |
| p. 6 | country exposures; currency factor returns **"calculated", not "estimated"** (fn 8: "no uncertainty is involved") | standard error, exposure |
| p. 7 | eqs (1.1)–(1.2), two-step cross-sectional industry regression; residual `u`, `ū`; "marginal benefit of increasing granularity" | cross-sectional regression, orthogonal, residual, marginal contribution (contrast) |
| p. 8 | symbol list; monthly returns, 15-year history; **\|t\| > 2**; average squared t-statistic; LASSO/LARS/Ridge/Bayesian named as **not** adopted | standard error, degrees of freedom, shrinkage |
| p. 9 | Table 1.1, 18 style factors; styles "**typically**" equal-weighted substyle combinations | exposure |
| p. 10 | Table 1.2 NAMR summary stats; standardisation "similar to forming a z-score", sqrt-cap mean / equal-weight sd; eqs (1.3)–(1.4); N ≥ 200 substyles | exposure, multicollinearity |
| p. 11 | **Figure 1.3**, 12×12 style exposure correlations: Size–Liquidity **0.74**, EY–Profitability **0.64**, Vol–DivYield **−0.46**, Size–Vol **−0.36** | multicollinearity, orthogonal |
| p. 12 | eqs (1.5)–(1.6), recursive re-run with size folded in | orthogonal, residual |
| p. 14 | 10% significant-t threshold; fn 11 (t-stats from monthly cross-sectional regressions); Size/Volatility prose | standard error, multicollinearity |
| p. 16 | reversal = one month, behavioural overreaction; decile **0/1 dummies**; small/mid-cap as **smoothed** dummies; Figure 1.10 | exposure, design matrix |
| p. 24 | **eq. (1.7) `r = Xf + u`; eq. (1.8) `Σ = XFXᵀ + Δ`**; daily/weekly estimation; `X` = "set of factor exposures" | all of them |
| p. 25 | eq. (1.9); **sqrt-market-cap weights** + heteroskedasticity justification; fn 14; two-pass; Core Country/Industry | standard error, cross-sectional regression |
| p. 26 | **eq. (1.10) two identifying restrictions; "three intercept terms"; "a rotation … does not impact the efficacy"**; eq. (1.11); UK/EMEA interpretation example; **two printed source typos, both re-verified** | design matrix, multicollinearity, orthogonal |
| p. 27 | `F` from daily factor returns since **March 1996**; **WKL = 104 weeks, 26-week half-life**; specific covariance = risk vector **+ non-zero off-diagonal correlations**; Newey–West [26] | covariance matrix, specific risk |
| p. 28 | **Table 1.3** (Daily: 125d / 375 obs / NW 10d; Weekly WRLD-EMKT: 26w / 104 obs / NW 2w); **cross-sectional overlay** for IPOs; structural vs empirical | specific risk, shrinkage, degrees of freedom |
| p. 30 | Assumptions: **dummy variables for industry/country/currency (not styles)**; "factor returns have **zero correlation** with asset specific returns"; 1-month horizon; **the only "out-of-sample" in the paper** | orthogonal, design matrix, in/out-of-sample |
| p. 32 | R² defined **in words only**; 10% t-stat threshold; **VIFs / multicollinearity, fn 16**; bias statistic introduced. **No numeric values anywhere** | multicollinearity, in/out-of-sample, standard error |
| p. 33 | test-portfolio list completed; **no results printed**; "[27] available on request" | in/out-of-sample |
| p. 34 | **Active Risk / Portfolio Beta / Portfolio Risk / Benchmark Risk**; "Active Risk split equally between common factors and stock specific"; "contribution to active risk" | tracking error, marginal contribution |
| p. 35 | EDR banner **2.99 / 1.02 / 15.62 / 14.98**; pie **Specific 50 / Style 25 / Industry 14 / Country 6 / FX 4 / Act Sec 1 [INFERRED]**; all bar magnitudes are **pixel readings ±10%** | tracking error, marginal contribution, specific risk |
| p. 36 | **thinness corrections via a Bayesian prior**; prior's form/strength **not specified** | shrinkage |
| p. 38 | bias statistic = rolling **12** monthly standardised returns, **95%** CI; 99% 1-day VaR over **252** days; benchmarking vs STORM | in/out-of-sample |
| p. 39 | **Huberisation: "the standardised values are referred to as exposures", ±3, sqrt-cap mean 0, equal-weight sd 1**; Cloning; Fill-Miss | exposure, loading |
| p. 42 | **eq. (1.12) historical beta** (weekly, 52-week half-life, 5 years); Historical Sigma = **equally**-weighted sd of exponentially-weighted residuals | residual, loading, cross-sectional regression |
| p. 52 | eq. (1.49): macro betas fitted **to the residuals of (1.12)**. The word "orthogonal" here is **`notes/`'s gloss, not the paper's** | orthogonal |
| p. 56 | **Table 1.4, "Inventory of all substyles investigated"** — 18 candidate styles / **108** substyles (`notes/`'s count, **not printed**), including a style **Random** whose one substyle is **"Random Substyle"**. No prose on the page at all | standard error, in/out-of-sample |
| p. 57 | Table 1.5, NAMR industry schema — **54** industries (`notes/`'s count, **not printed**) | degrees of freedom |
| p. 61 | Table 1.11, WRLD industry schema — **49** industries (`notes/`'s count, **not printed**) | degrees of freedom |
| p. 64 | ref **[7] Tibshirani**, "Regression **shrinkage** and selection via the lasso" — the only occurrence of the word in printed text. **`notes/`'s commentary on this page claims BFRE *uses* lasso/LARS shrinkage; p. 8 says the opposite. Trust p. 8** | shrinkage |
| p. 65 | ref **[26] Newey–West**, "A Simple, **Positive Semi-Definite**, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix" | covariance matrix, eigenvalue |

---

## 6. THINGS YOU MUST NOT SAY AT THE TABLE

Failure modes for the GM, not the player. `notes/`'s own audit caught a fabricated cross-reference;
this is the list that stops the next one.

1. **Do not cite a page for a word the paper does not use.** Six terms here have no paper occurrence:
   loading, design matrix, degrees of freedom, standard error, eigenvalue, tracking error. Plus
   "orthogonal" and "in-sample". Cite the *mechanism's* page and name the word as outside vocabulary.
2. **Do not quote `notes/`'s commentary as the paper's text.** The traps, all four checked:
   "orthogonal" (p. 52) and "HAC standard errors" (p. 65) are the transcriber's words; so is
   "coefficient of determination" (p. 32), the "placebo/control" reading of the Random Substyle
   (p. 56), and every "(my count)" total — 54 and 49 industries, 18 styles, 108 substyles. And one
   outright internal contradiction: the p. 64 commentary says BFRE's selection machinery includes
   lasso/LARS/group-lasso **shrinkage**; **p. 8 body text says those methods were the alternatives
   BFRE did not take.** Trust the body text.
3. **Do not launder a pixel measurement into a printed figure.** Every bar height, dot position and
   axis reading on p. 35 (and Figures 1.1, 1.2, 1.6, 1.7, 1.9, 1.10, 1.12) is a measurement off a
   photograph with a stated tolerance. Say "measured off the chart, roughly" every single time.
4. **Do not resolve `[INFERRED]` or `[TENTATIVE]` markers.** The p. 35 pie's "Act Sec 1%" is inferred
   from the sum-to-100 argument only; the FX currency codes are tentative; "2.99" and "15.62" have soft
   digits. Carry all four.
5. **Do not silently correct the paper's typos.** Eq. (1.10)'s doubled `j` index and the p. 26
   where-list pairing `X_Mkt` with "Style Exposures" are **source errors**, re-verified at high zoom.
   Showing the player a real published document containing real errors is worth more than a clean one.
6. **Do not invent a number the paper withholds.** There is no VIF value, no bias statistic, no R²
   figure, no total factor count, no specific-risk weighting function, and no Bayesian prior parameter
   anywhere in the document. When the player asks — and they should — the correct answer is "the paper
   does not say, and that is a finding."
