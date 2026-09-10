# BFRE ANCHOR MAP — level by level

Game-master reference for **THE RISK DESK** (`prompt/RISK_DESK.md`). One job: let the GM obey the
rule *"Every analogy must end by naming which page, which factor, which equation, and what it changes
about a real risk number"* — without guessing.

**Source of truth for this file:** `notes/` only (the page-indexed transcription of all 65 PDF pages).
Nothing here is cited that was not read in `notes/`. Where the paper contains no anchor for a level,
the gap is stated as a gap. **An invented citation is the worst possible failure; an honest gap is
required.**

---

## 0. How to read the citations

| Convention | Meaning |
|---|---|
| `p.24` | PDF page 24. For pages 2–65 the PDF index equals the printed footer number — verified in every chunk header. p.1 (title/contents) carries no printed number. |
| `(1.8)` | The paper's own numbered equation. Equations run **(1.1)–(1.55)**, continuously, no gaps, no duplicates. |
| **PAPER** | The paper says this. Quote or close paraphrase from `notes/`. |
| **INFER** | The GM's inference from things the paper says. Say "this follows from" — never "the paper says". |
| **GAP** | The paper does not contain this. Say so out loud at the table. |
| `[UNREADABLE]` / `[APPROX]` | The scan could not resolve it. Carry the uncertainty forward verbatim. Never round it into a confident figure. |

**Two structural facts to keep straight, because levels 4, 8 and 11 all trip on them:**

1. **Figure 1.3 (p.11) is not F.** It is the correlation of *exposures* — the columns of `X`.
   Table 1.2's last-but-one column (p.10) is the correlation of *factor returns* with the market
   factor return — that lives in `F`. Different object, same word "correlation".
2. **The portfolio-beta formula on p.4 is handwritten.** `notes/` records
   `beta_{p,b} = (X_p^T F X_b)/(X_b^T F X_b)` as a **reader's pen annotation in the margin**, not
   printed text. The printed sentence only says beta "can instead be computed via the risk factor
   exposures of the portfolio and market index, together with the factor covariance matrix". **Never
   attribute that formula to BlackRock.**

---

## 1. One-glance anchor table

| # | Level | Primary pages | Primary anchor | Anchor strength |
|---|---|---|---|---|
| 0 | The Miss | p.24, p.8, p.7, p.32 | `u` in (1.7); average squared t-statistic (p.8) | Strong for the *object*; **GAP** on why squares |
| 1 | The Dial | p.24, p.4, p.25 | `f` in (1.7); market factor return = weighted cross-sectional average (p.4 fn 2); √-cap weights (p.25) | Strong |
| 2 | The Balance | p.26 | (1.10) — restrictions imposed by hand | **GAP** on `Σx·e = 0`; the paper's balance is a *different* balance |
| 3 | The Second Dial | p.25, p.5, p.7 | (1.9) four blocks at once; country factors "neutral with respect to market, style and industry" (p.5) | Strong |
| 4 | The Collision | p.32, p.26, p.11, p.17, p.20 | VIFs + footnote 16 (p.32); three intercepts (p.26); Size–Liquidity 0.74 (p.11) | Strong — **graduate-level** |
| 5 | The Intercept | p.26, p.10, p.39, p.42 | "three intercept terms" (p.26); standardisation to weighted mean zero (p.10, p.39); `alpha_i` in (1.12) | Strong for centering; **GAP** on Cov/Var algebra |
| 6 | The Verdict | p.8, p.32, p.12, p.14, p.15 | \|t\| > 2 (p.8); 10% threshold (p.14, p.32); 10–15% stopping rule (p.12); Figure 1.8 (p.15) | Strong for *use*; **GAP** on where a standard error comes from |
| 7 | The Timeline | p.24, p.3, p.14, p.18, p.20, p.10 | "a series of cross-sectional regressions" (p.24); Table 1.2 (p.10); Figures 1.7 / 1.12 / 1.14 | Strong |
| 8 | The Weather Map | p.24, p.27, p.3, p.36 | `F` in (1.8); WKL 104 weeks / 26-week half-life (p.27) | Medium — **large GAP**, see §L8 |
| 9 | The Private Drama | p.24, p.27, p.28, p.30, Table 1.3 | `Δ` "a diagonal matrix" (p.24); p.27 says it isn't; p.28 gives the direction of the error | Very strong |
| 10 | The Assembly | p.24 | (1.7) and (1.8), one line apart | Very strong |
| 11 | The Desk | p.34, p.35 | Figure 1.18 EDR report; "Contrib. (% of Act. Risk)" | Medium — **GAP** on the formula |
| 12 | The Critique | p.8, p.27, p.32, p.33, p.36, p.55, p.56, p.5, p.6 | Unstated thresholds; deferred documents; two-day evidence base; 200+ substyles with a Random Substyle | Very strong |
| ★ | THE REBUILD | p.24, p.25, p.26, p.27, p.28 | (1.7)–(1.11) + Table 1.3 | Very strong |

---

## 2. Jargon-unlock ledger

The rules say *"Jargon is locked until the player has built the thing."* This table says which level
buys which word. Terms appear in this file freely — the GM must not leak them early **at the table**.

| Term | Unlocked at | First BFRE appearance |
|---|---|---|
| residual, the miss | L0 | `u` (1.7) p.24; `u`/`ū` (1.1)–(1.2) p.7–8; `ε` (1.3) p.10; `η` (1.5) p.12 |
| specific return, idiosyncratic return | L0 (name), L9 (machinery) | p.24, text under (1.7) |
| factor return | L1 | `f` (1.7) p.24 |
| regression weight | L1 | p.25 (√-market-cap), p.4 fn 2 |
| exposure, loading | L1–L3 | `X` (1.7) p.24; Table 1.1 p.9 |
| design matrix | L3 | not the paper's term — **GAP**, it is `X` throughout |
| orthogonal / neutral | L4 | word "neutral" p.5; the *word* "orthogonal" never appears in the paper |
| multicollinearity | L4 | p.32 |
| variance inflation factor | L4 | p.32 |
| intercept | L5 | p.26 ("three intercept terms"); `alpha_i` (1.12) p.42 |
| z-score, standardisation | L5 | p.10; p.39 ("standardised values are referred to as exposures") |
| t-statistic | L6 | p.8 |
| statistically significant | L6 | p.8 (\|t\| > 2) |
| cross-sectional regression | L7 | p.24; also pp.3, 8, 30, 32 |
| in-sample / out-of-sample | L7 or L12 | p.30 ("Out-of-sample model back-testing") |
| factor covariance matrix, `F` | L8 | (1.8) p.24; p.27 |
| half-life, exponential decay | L8 | p.27; Table 1.3 p.28 |
| shrinkage / Bayesian prior | L8 | p.36 (thinness correction); p.8 (LASSO/LARS/Ridge, **not adopted**) |
| specific risk, `Δ` | L9 | (1.8) p.24; p.27 |
| diagonal | L9 | p.24 (word used of `Δ`); p.27 (walked back) |
| asset covariance matrix, `Σ` | L10 | (1.8) p.24 |
| active risk | L11 | p.34, p.35 banner |
| marginal contribution to risk | L11 | **GAP** — see §L11 |
| bias statistic | L12 | p.32, p.38 |
| tracking error | never, from this paper | **GAP** — the paper says "Active Risk", not "tracking error" |
| eigenvalue / eigenvector | never, from this paper | **GAP** — zero occurrences in 65 pages |

---

## 3. LEVEL 0 — THE MISS

**(a) Pages.** p.24 (the object itself); p.7–8 and p.10–12 (the residual as a working tool); p.8 (why
size, not sign, is what gets scored); p.32 (`R²`); p.13 (a residual mattering in money).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| Equation (1.7) `r = X f + u` | p.24 | `u` is the miss. Text: "`X f` is termed the common factor return and `u` is the asset specific, or idiosyncratic, return." |
| Equations (1.1)/(1.2), symbols p.8 | p.7–8 | `u` = "Residual returns from the first step regression"; `ū` = residual from the second step. The paper runs a whole selection procedure *on residuals*. |
| Equations (1.3)/(1.4) → (1.5)/(1.6) | p.10, p.12 | Same shape with `ε`, `ε̃ᵢ`, then `η`, `η̃ᵢ`. Four different letters, one idea. |
| "average squared t-statistic" | p.8 | The paper's own reason for squaring: computed "to distinguish between factors with t-statistics close to +/- 2 and those that are significantly higher". |
| `R²`, in words | p.32 | "the proportion of cross-sectional variation in asset returns explained by the set of common factors". **No formula is printed.** |
| Historical Sigma | p.42 | "An equally-weighted standard deviation of the residuals in regression (1.12)" — a residual spread that becomes a *factor exposure*. |

**(c) What breaks.** If the miss is scored by its raw sum instead of its size, nothing downstream
exists: `Δ` in (1.8) (p.24) is built out of the spread of these misses, and the report on p.35 books
**50% of that portfolio's Active Risk** as Specific. A model that cannot tell a big miss from a
cancelling pair of misses sets that half of the risk number arbitrarily. **INFER** on the magnitude
of the consequence; **PAPER** on the 50% (p.35 pie, read directly, unambiguous).

**(d) Landing sentence.**
> "The thing you have been calling *the miss* is the letter `u` on page 24, equation (1.7) — and page 8
> shows the authors reaching for your exact trick on their own diagnostics: they average the **square**
> of the t-statistic, precisely so a factor scoring 6 counts more than one scoring 2 instead of letting
> big and small cancel."

**GAP — say it out loud.** The paper **never derives or defends squared loss**, never writes "least
squares", never writes a sum-of-squares. `notes/` contains zero hits for "least squares", "normal
equation", "sum of squares". Level 0's argument is *ours*; the paper only inherits its result.

---

## 4. LEVEL 1 — THE DIAL

**(a) Pages.** p.24 (what the dial is called); **p.4** (the first dial BFRE ever turns); p.25 (the
weights on the dial, with the paper's own justification); p.10 Table 1.2 (real dial settings).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| `f` in (1.7) | p.24 | "`f` : return to each factor" — one number per column per period. |
| Market factor, footnote 2 | p.4 | "all equity assets have a **unit exposure** to this factor"; market factor return = "the cross-sectional average return across all assets in the model estimation", footnote 2: "Average return based on **regression weights**, i.e. square-root of market capitalisation". |
| √-market-cap weighting | p.25 | "a good compromise between a weighting scheme that places equal weight on all assets, and one that is weighted by market capitalisation … More technically, square-root of market capitalisation **adjusts for heteroskedasticity** based on the observation that higher residual (specific) risk is typically correlated with smaller market capitalisation assets." |
| Footnote 14 | p.25 | The textbook alternative — weights = 1/residual variance — is named and dismissed: "in practice these provide similar results". |
| Table 1.2 | p.10 | Annualised factor returns for NAMR, Mar 1996–Dec 2013: Market **7.0%**, Reversal **−5.1%**, Momentum **5.4%**, Value **3.3%**, Growth **−2.0%**. These are `f`, annualised. |

**Best single use of p.4 at this level (INFER, flag it):** the market column of `X` is all ones
(p.4, PAPER) and the regression is weighted by √-market-cap (p.25, PAPER). Put those together and
`b = Σ w·x·r / Σ w·x²` collapses to `Σ w·r / Σ w` — a weighted average return. Footnote 2 on p.4
says the market factor return **is** exactly that weighted average. So the player's Level-1 formula,
applied to a column of ones, reproduces the paper's very first factor by hand. Say "this follows
from two things the paper states" — the paper does not print the collapse.

**(c) What breaks.** Get the dial wrong and **every** factor return in Table 1.2 is wrong, therefore
every entry of `F` in (1.8) is wrong, therefore the whole common-factor half of the risk number is
wrong. Direction, in the paper's own words (p.25): equal weighting gives "a poor fit for mega-cap and
large-cap securities"; pure cap weighting gives "poorer forecasts for mid-cap and small-cap
securities". So the error has a **known address** — it lands on a size segment, not uniformly.

**(d) Landing sentence.**
> "That single number you dialled in is `f` in equation (1.7) on page 24 — and page 4, footnote 2,
> tells you the very first one BFRE computes: run your calculation with a column of ones and
> square-root-of-market-cap weights and you get the market factor return, which is where the 7.0% in
> Table 1.2 on page 10 comes from."

---

## 5. LEVEL 2 — THE BALANCE

**(a) Pages.** p.26 — and only p.26.

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| Equation (1.10) | p.26 | Two identifying restrictions, shown here in their **intended** form: `Σ_j ω_CInd,j · f_CInd,j = 0` and `Σ_k ω_CCty,k · f_CCty,k = 0`. `ω` = "the average (square-root of capitalisation) weight". (What is actually *printed* is in the typo row below.) |
| Footnote 15 | p.26 | "The average return is a square-root of market capitalisation weighted return." |
| The consequence sentence | p.26 | "if asset returns across EMEA are mostly positive on a given day and UK assets are also up but by **less than the average** return over the region, then the UK factor return will be **negative**." |
| Single-country models | p.26 | Japan: no country factors, "In this instance only **one** linear restriction is required". |
| Source typo | p.26 | Both sums in (1.10) are printed with index `j`; the second summand is subscripted `k`. **This is the paper's error**, re-verified at 6×. Do not silently fix it — it is a free Level-12 exhibit. |

**(c) What breaks.** **PAPER (p.26):** without the restrictions the specification "is not uniquely
identified as there are an infinite number of possible solutions" — the regression does not return a
wrong answer, it returns *any* answer. **PAPER (p.26):** the restrictions also fix the *meaning* of
every industry and country number: "the industry and country factors are **net of** the market factor
return, which impacts their interpretation." Read a country factor as a raw country return and you
will call a rising market a falling country.

**(d) Landing sentence.**
> "Your balance came out of the arithmetic for free, and you could not have stopped it. Page 26,
> equation (1.10), shows a balance of the opposite kind — the authors force the weighted average
> industry return and the weighted average country return to zero **by hand**, because without it the
> problem has infinitely many answers. Hold on to that difference: something the arithmetic guarantees
> versus something a human imposes. Level 9 is entirely that distinction."

**GAP — say it out loud.** The orthogonality condition `Σ x·e = 0` **is not in this paper**. Not
stated, not derived, not named. `notes/` has zero hits for "orthogonal" outside a transcriber's note
and zero for "normal equation". The condition is real and the player will prove it; it just does not
have a page number. Do not manufacture one.

---

## 6. LEVEL 3 — THE SECOND DIAL

**(a) Pages.** p.25 (the full simultaneous system); p.7 (the earlier two-block version); p.5 (why
simultaneity is the point); p.11 and p.26 (the "where" glossaries — one of which is broken).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| Equation (1.9) | p.25 | `r = X_Mkt f_Mkt + Σ_{i∈Sty} X_Sty,i f_Sty,i + Σ_{j∈CInd} X_CInd,j f_CInd,j + Σ_{k∈CCty} X_CCty,k f_CCty,k + u`. Four blocks, one regression, one pass. Verified at 5×; the market term carries no sum. |
| Equation (1.1) | p.7 | The three-block ancestor: market + core country + industry-at-level-`n`. |
| Country neutrality | p.5 | "Country factor returns are estimated in a **multivariate regression together with other common factors**, and are therefore **adjusted to be neutral with respect to market, style and industry effects**." Justification given: a country with a large concentration in a single industry. |
| Equation (1.11) | p.26 | The second pass: extended industries and extended countries fitted to the first pass's residuals `u`. |
| Source typo | p.26 | The (1.9) "where"-list has **five** rows and no Style row at all — `X_Mkt f_Mkt` is printed against the description "Style Exposures and Factor Returns". Re-verified at 4×. **Paper's error.** |

**(c) What breaks.** **PAPER (p.5):** solve one column at a time and the country number stops being
neutral to industry — a country whose index is 40% banks reports a "country" return that is partly a
bank return. **PAPER (p.25/p.26):** because the second pass fits Extended Country and Extended
Industry factors to first-pass residuals, an error in the first pass's joint solve propagates into
every emerging-market and frontier factor return, which are then never re-estimated.

**(d) Landing sentence.**
> "Two dials that have to be solved together is equation (1.9) on page 25, where BFRE turns market,
> style, core-industry and core-country dials in one solve — and page 5 gives the reason in one line:
> the country number is *'neutral with respect to market, style and industry effects'* only **because**
> it was solved jointly, never one at a time."

---

## 7. LEVEL 4 — THE COLLISION

> **DIFFICULTY: graduate-level.** Multicollinearity is a genuine graduate topic and the
> regress-on-residuals move the paper uses is the Frisch–Waugh–Lovell theorem in disguise. **The paper
> never names Frisch–Waugh.** Zero hits in `notes/`. Say "this is the mechanism behind a theorem you
> will meet later called Frisch–Waugh–Lovell" — do not cite a page for the name.

**(a) Pages.** p.32 (the diagnostic and the failure mode); p.26 (the exact-collision case); p.11
(a real collision, measured); p.17 and p.44 (a collision the authors designed *out*); p.20 (a
collision they surrendered to); p.7, p.10, p.12, p.52 (partialling by regressing on residuals).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| Variance inflation factors | p.32 | "If style exposures are too closely correlated then the regression procedure will encounter problems in **apportioning the factor return between them**. This can result in **significant instability in the factor return estimates through time**." |
| Footnote 16 | p.32 | "In the most extreme case, where factor exposures are **perfectly correlated**, identification issues will exist causing the estimation process to **fail**." — this is the determinant going to zero, in the paper's own words. |
| Three intercepts | p.26 | Market + industry + country all carry unit exposure for every asset — a built-in exact collinearity, fixed only by (1.10). |
| Figure 1.3 | p.11 | Measured collisions, NAMR Dec 2013: **Size–Liquidity 0.74** (highest off-diagonal), Earnings Yield–Profitability **0.64**, Volatility–Dividend Yield **−0.46**, Size–Volatility **−0.36**. All 144 cells re-read in audit. |
| Momentum's one-month lag | p.17, p.44 | Momentum = previous **11 months with a one-month lag**, the lag explicitly "to **exclude the reversal effect**"; Reversal (1.18) is exactly the excluded month. Two columns engineered not to overlap. |
| EMEA yield merger | p.20 | Earnings Yield and Dividend Yield "were found to be highly correlated over the research history and so were **combined into a single factor**, referred to as yield." The surrender option. |
| Two-step regressions | p.7, p.10, p.12 | (1.1)/(1.2), (1.3)/(1.4), (1.5)/(1.6): a candidate is judged by regressing it on **the residuals of the model without it** — i.e. on what nothing else already explained. |
| Macro betas | p.52 | (1.49) is fitted to the residuals of (1.12), not to raw returns. |
| Volatility ↔ Size | p.14 | "portfolios which are positively exposed to size are commonly negatively exposed to volatility, and vice versa. This negative relationship is fairly stable over time." |

**(c) What breaks.** **PAPER (p.32):** the coefficients do not merely get noisy — the *apportionment*
between two collided factors becomes unstable through time, so a risk report attributes the same risk
to Size this month and to Liquidity next month with no change in the portfolio. **PAPER (footnote 16,
p.32):** at perfect correlation, estimation fails outright. **PAPER (p.13), the money version:** AOL
in 1999 scored large on market-cap and small on sales; "A measure of size based on market
capitalisation alone would confer large-size status on AOL, and **reduce its risk forecast
accordingly**." Direction: **too low**, on exactly the name where it hurt.

**(d) Landing sentence.**
> "What you just built is why page 17 stops the momentum window one month early — *'to exclude the
> reversal effect'* — because two columns that overlap end up fighting over the same return; page 32
> is the alarm the desk actually runs for it, the variance inflation factor, and its footnote 16 says
> that when two columns agree **perfectly**, the estimation does not go wrong, it stops."

---

## 8. LEVEL 5 — THE INTERCEPT

**(a) Pages.** p.26 (intercepts, counted); p.10 and p.39 (where BFRE does the centering, and the
odd way it does it); p.42 (an intercept that becomes a factor); p.16/p.51 (a column of ones,
smoothed).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| "three intercept terms" | p.26 | "for each asset, there exist three intercept terms – the market factor, an industry factor, and a country factor. **Every asset has unit exposure to these three factors.**" A column of ones *is* an intercept — the paper says so in as many words. |
| The standardisation rule | p.10 | "The **mean** is defined as the **square-root of market capitalisation weighted** average value so that the transformed substyles (and styles) have the property that their **weighted average is zero**. Additionally, these values are divided by their **equally-weighted standard deviation** so that a value of +1 … is one standard deviation above the market average. An exposure of zero indicates that a security has the market average value." |
| Huberisation | p.39 | Exposures "take values between **+/- 3** and are standardised to a square-root capitalisation **mean of zero**, with an **equal-weighted standard deviation of one**". Applied again after aggregation. |
| `alpha_i` in (1.12) | p.42 | The intercept of the beta regression is itself harvested as the **Historical Alpha** substyle (p.44). |
| Small-Cap / Mid-Cap | p.16, p.51 | (1.47)/(1.48) are smoothed dummy variables — "A smooth function is used in preference to 0/1 indicators **to mitigate instability in exposures for assets on the decile boundaries**." |

**(c) What breaks.** **PAPER (p.10):** exposures are defined so that zero means "market average". Skip
the centering and every exposure carries a level, so the market factor and the style factor both try
to explain the same common level — the collision of L4, manufactured on purpose. **PAPER (p.26):**
the pivot problem is real and unavoidable in BFRE because three columns of ones exist at once;
equation (1.10) is the fix. **Flag the asymmetry as a Level-12 seed:** mean weighted by √-cap,
standard deviation equal-weighted (p.10 and p.39, both) — the paper states it and never justifies it.

**(d) Landing sentence.**
> "Your pivot moving to the average is exactly what page 10 does to every characteristic before it ever
> reaches a regression — the mean is subtracted so that *zero means market-average* — and page 26
> shows the cost when you have too many pivots: every asset in BFRE carries **three** columns of ones,
> market, industry and country, and equation (1.10) is how they knock three back down to one."

**GAP.** The paper never derives `Cov/Var`, never writes the centering algebra, never uses the word
"covariance" in the estimator sense (only "factor covariance matrix"). The proof that the fitted line
passes through `(x̄, r̄)` is ours.

---

## 9. LEVEL 6 — THE VERDICT

**(a) Pages.** p.8 (the threshold and the squared version); p.32 (the same threshold in the official
diagnostics); p.12 (a stopping rule built from it); p.14 (the inclusion threshold, stated); p.15
Figure 1.8 and p.16 Figure 1.10 (the evidence); p.30 (why the tests are monthly).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| The threshold | p.8 | "We consider an absolute t-statistics in excess of **2** as statistically significant." (Grammar error is the source's.) |
| The squared version | p.8 | "the **average squared t-statistic**, computed specifically to distinguish between factors with t-statistics close to +/- 2 and those that are significantly higher." |
| Persistence proxy | p.8, p.32 | The **proportion** of significant t-statistics "serves as a good proxy for the persistence of individual factor effects." |
| The 10% bar | p.14 | "A value in excess of **10%** indicates a statistically significant style effect, and would be considered for inclusion in the models." |
| The stopping rule | p.12 | Recursion stops "until the largest proportion of t-statistics from the second step univariate regression is no larger than **10% - 15%**." |
| Figure 1.8 | p.15 | NAMR styles ranked by proportion of significant t-stats, Mar 1996–Jun 2013. Measured, no printed labels: Volatility ≈63%, Momentum ≈50%, Size ≈42%, Reversal ≈37%, Value ≈34%, Liquidity ≈32%, Dividend Yield ≈23%, MidCap ≈20%, Growth ≈18%, Profitability ≈14%, Sentiment ≈7%, Earnings Yield ≈4–5%. **[APPROX — pixel-measured, not printed. Say so.]** |
| Figure 1.10 | p.16 | The clean before/after: decile 10 falls from **21.1% → 3.4%** and decile 9 from **10.8% → 2.1%** once a small-cap factor is added. Also **[APPROX]**, ±0.5pp. |
| Footnotes 11, 12 | p.14, p.16 | "t-statistics are based on **monthly cross-sectional regressions**." |
| Sample | p.8 | Regressions monthly over the **15-year research history**; results summarised over the full sample **and five-year sub-samples**. |

**Boss round ammunition (big coefficient, small t).** Table 1.2 (p.10) has it printed: **Volatility**
has an annualised return of **−0.6%** with volatility **7.5%** — Sharpe **−0.08**, i.e. no reliable
return at all — yet Figure 1.8 (p.15) ranks it the **most** significant style in NAMR at ≈63%, and
p.14 says its significance is "larger than the other style factors, and incidentally **most industry
and country factors**." A risk model keeps it because it explains *co-movement*, not because it pays.
That is the argument-against-dropping, straight from two exhibits.

**(c) What breaks.** **PAPER (p.12, p.14):** the whole style-factor list is *selected* by this
statistic. Set the bar wrong and the model has the wrong columns — too low and you admit Sentiment
(≈7%, below the stated 10% bar per Figure 1.8) and Earnings Yield (≈4–5%), inflating `F` with junk
columns; too high and you drop real common variation into `Δ`, understating factor risk and
overstating specific risk. Direction claim is **INFER**; the thresholds and rankings are **PAPER**.

**(d) Landing sentence.**
> "That ratio you just built — the size of the answer divided by how much it wobbles — is what page 8
> calls a **t-statistic**, and BFRE's whole style list is chosen with it: keep a factor if the ratio
> beats 2 often enough, stop adding factors once the best candidate left clears that bar less than
> 10–15% of the time (page 12), and Figure 1.8 on page 15 is the entire North America style list
> sorted by nothing else."

**GAP — a big one, say it clearly.** The paper **never shows where a standard error comes from**,
never mentions degrees of freedom, never prints a t-statistic formula. `notes/` has zero hits for
"standard error" and "degrees of freedom" in the paper's own text. The only inference machinery named
anywhere is **Newey–West [26]** (p.27, p.28, p.38, bibliography p.65) — used to correct for serial
correlation in the *risk* estimates, not presented as the source of the t-stats. Level 6 is the level
where the game gives the player something the paper assumes.

---

## 10. LEVEL 7 — THE TIMELINE

**(a) Pages.** p.24 (the design); p.3 (the cadence, executive-summary version); p.10 Table 1.2 and
Figures 1.7 (p.14), 1.12 (p.18), 1.14 (p.20) (the output); p.14 and p.42 (the contrast case — the one
place BFRE *does* run a time-series regression); p.2 (the rival design).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| The design | p.24 | Estimation is "a series of **cross-sectional** regressions of asset returns against asset factor exposures, which provides estimates of factor returns and asset specific returns." |
| The cadence | p.24 | "These regressions are performed **daily** for country and regional models and **weekly** for the World model." (No justification given for the weekly choice — Level 12.) |
| Executive summary | p.3 | "Model estimation is performed in cross-section **in two-passes**"; daily factor returns for all models **from March 1996 onwards**. |
| The output, summarised | p.10 | Table 1.2, NAMR, Mar 1996–Dec 2013: annualised return, annualised volatility, Sharpe, correlation with market, first-order autocorrelation, for Market + 12 styles. Every number here is computed **from the time series L7 produces**. |
| The output, plotted | p.14, p.18, p.20 | Figure 1.7 (NAMR Size vs negated Fama–French SMB), Figure 1.12 (EMEA momentum), Figure 1.14 (NAMR Value vs HML) — cumulative sums of the monthly/daily `f`. |
| The contrast | p.14, p.42 | Historical beta **is** a time-series regression: (1.12), weekly excess returns, 5 years, exponentially weighted with a **52-week half-life**, against the cap-weighted Estimation Universe. But it enters BFRE as an **input substyle to Volatility**, never as the exposure mechanism. |
| The rival | p.2 | STORM: "asset-by-asset covariance matrix estimated from **asset returns alone**, each asset effectively its own factor." BFRE "imposes far more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of factors." |
| What the choice buys | p.2 | Fundamentals-based exposures react "immediately" to a change in operating activities, capital structure or corporate actions, where a returns-only model incorporates them "only gradually". |
| What the choice costs | p.13 | Same mechanism, the other way: AOL's *market-cap* substyle exposure ran ≈2.0 while its *sales* substyle sat near 0 — the exposure moves with the price, which is what the model is trying to forecast. **[APPROX — Figure 1.6 values are pixel-measured against warped gridlines.]** |

**(c) What breaks.** **PAPER (p.2, p.13):** the cross-sectional choice is what lets an exposure update
the day a company issues stock or sells a division. Its cost is that the exposure is measured with
error every single period, and errors in `X` at time `t` push straight into `f` at time `t`, then into
`F` (L8) and into every risk number thereafter. **PAPER (p.30):** the horizon is **1 month**, and the
whole selection apparatus is monthly — a factor selected on monthly cross-sections is being asked to
forecast a monthly risk number, which is self-consistent but circular. **PAPER (p.24, INFER on the
consequence):** the World model estimates weekly rather than daily, so its factor returns are a
coarser series feeding the same `F`.

**(d) Landing sentence.**
> "Run your one-day calculation again tomorrow, and again the day after, and the row of numbers you
> build is what page 14, page 18 and page 20 have been plotting all along — Figure 1.7, Figure 1.12,
> Figure 1.14 are just those numbers added up — and Table 1.2 on page 10 is the average and the spread
> of that row, from March 1996; page 24 says it is done **daily** for regional models and **weekly**
> for the World model."

---

## 11. LEVEL 8 — THE WEATHER MAP

> **DIFFICULTY: this level is the game's largest gap between what the player must build and what the
> paper contains.** Be honest about it early. The player must build an eigen-decomposition and a
> shrinkage story that **do not appear anywhere in the 65 pages**.

**(a) Pages.** p.24 (`F`'s name and place); **p.27** (everything the paper actually says about how `F`
is built, and where it stops saying); p.3 (executive summary); p.30 (one concrete pre-treatment);
p.36 (the paper's only actual shrinkage); p.10 (a real slice of `F`).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| `F` | p.24 | Equation (1.8) `Σ = X F Xᵀ + Δ`; "`F` : factor covariance matrix". |
| Construction | p.27 | "The BFRE factor covariance matrices use a history of **daily** factor return series starting in **March 1996**. Observations are weighted using an **exponential decay** that places more emphasis on recent factor returns to give more responsive risk forecasts." |
| The default recipe | p.27 | "The default factor covariance matrix calculation for all BFRE models is **WKL (weekly long-term)**, which uses **104 weeks** of factor returns with a **half-life of 26 weeks**." |
| The trade-off, stated | p.27 | "forecasts … should be **responsive** to changes in the market environment whilst not being unduly **noisy** so as to render them unstable and unusable." |
| Serial correlation | p.3, p.27 | Factor covariance matrices built "correcting for serial correlations"; PRT lets users "control for serial correlations and asynchronicity in the factor return series". Newey–West [26] is named for the specific-risk side (p.27–28). |
| Outlier pre-treatment | p.30 | Currency factor returns truncated before covariance estimation: **±8%** daily, **±20%** weekly. |
| The paper's one shrinkage | p.36 | Thin country/industry correction: "adding a **Bayesian prior**, which in essence **diverts the estimated country/industry return away from the sample factor return and towards a theoretical prior**." Note: this shrinks a **factor return**, not `F`. |
| Shrinkage, considered and not adopted | p.8 | LASSO (Tibshirani [7]), LARS (Efron [8]), Group Lasso/LARS (Yuan and Lin [9]), Ridge, Bayesian (Kadane and Lazar [6]) — named as alternatives to BFRE's stepwise selection, then rejected as "purely statistical in nature and rely heavily on historical data". |
| A readable slice of `F` | p.10 | Table 1.2 column "Correlation with Market Factor": Volatility **0.84**, Liquidity **0.69**, Reversal **−0.32**, Size **0.23**, Momentum **−0.02**. These are correlations **between factor returns** — genuine `F` content. |
| **Not** `F` | p.11 | Figure 1.3 is exposure correlation (columns of `X`). Do not let the player conflate them. |

**(c) What breaks.** **PAPER (p.27):** `F`'s responsiveness is a single knob — the half-life. Too
short and forecasts are "unduly noisy … unstable and unusable"; too long and they stop responding to
the regime. **PAPER (p.30, INFER on direction):** untruncated currency outliers would enter the
covariance estimate; the paper truncates specifically "to remove outliers", which lowers estimated
currency factor volatility relative to the raw series. **INFER (structural, and the heart of the boss
round):** with 104 weekly observations (p.27) and a factor count in the dozens-to-hundreds — NAMR's
industry schema runs to **54 rows** in Table 1.5 (p.57; *count derived by the transcriber — the page
prints no total*) alongside 12 styles in Table 1.2 (p.10) plus market, country and currency blocks —
the sample covariance matrix is **rank-deficient**: there exist portfolios the
matrix scores at exactly zero risk. The paper never states this. Say plainly that this is the game's
argument, not BlackRock's.

**(d) Landing sentence.**
> "The grid you just built is the `F` in equation (1.8) on page 24, and page 27 tells you exactly how
> BFRE fills it — daily factor returns going back to March 1996, weighted so recent weeks count more,
> the default recipe being 104 weeks with a 26-week half-life. Page 27 also tells you where the paper
> stops: the rest of the method is handed off to a separate BRS document you do not have."

**GAPS — all four must be said out loud.**
1. **No eigenvalue, no eigenvector, no principal component anywhere in the paper.** Zero hits across
   all 65 pages of `notes/`. The "direction with the most wobble" construction is entirely ours.
2. **No shrinkage of `F`.** The only shrinkage in the paper is the p.36 Bayesian prior on thin
   country/industry **returns**, and its "form, strength and shrinkage parameter are **not**
   specified" (p.36).
3. **No factor count, no observation-to-factor ratio, no rank discussion.** The paper never confronts
   "fewer months than factors".
4. **The method is explicitly deferred (p.27):** "Model users are referred to the **BRS Covariance
   Matrix Estimation documentation** for technical details on the factor covariance matrix
   methodology." This is Level 12's single best exhibit — the most important matrix in the model is
   documented elsewhere.

---

## 12. LEVEL 9 — THE PRIVATE DRAMA

**(a) Pages.** p.24 (the claim); **p.27** (the claim retracted); **p.28** (the direction of the error,
in the paper's own words, plus Table 1.3); p.30 (the assumptions, listed as assumptions); p.16 (what
happens when a common effect is left in `Δ`).

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| The claim | p.24 | "`Δ` : specific risk matrix (**a diagonal matrix** of asset specific risk forecasts)". |
| The retraction | p.27 | "The asset specific covariance matrix is made up of **two** components: a vector of asset specific risk forecasts **and a sparsely populated unit diagonal matrix containing non-zero, off-diagonal specific return correlations.**" `Δ` is **not** diagonal. Three pages apart. |
| **The direction** | p.28 | "these specific returns may be positively correlated, and so **ignoring this correlation would lead to under (or over) prediction of specific risk in a long-only (long-short) portfolio context.**" ← the paper hands the GM the boss-round answer. |
| The assumptions, as assumptions | p.30 | "Factor returns have **zero correlation** with asset specific returns, and specific returns from different issuers are **unrelated and have zero correlation**." Also p.28: correlations "only estimated between assets **in the same company**. Specific return correlations between assets in different companies are **assumed to be zero** in-line with standard modelling practice." — the justification is literally "standard modelling practice". |
| The override | p.28 | Linkages captured "either **imposed via a constant override of 1**, or where data availability permits, **estimated using asset specific returns**." |
| Structural vs empirical | p.28, p.29 | Structural: related listings get identical specific risk (cloned from primary listing) and correlation forced to **1**. Empirical: estimated separately. p.29: structural suits **active managers** over "many months"; empirical suits **index trackers**. |
| Table 1.3 | p.28 | Specific-risk parameters. Daily model: half-life **125 days**, **375** observations, Newey–West lag **10 days**. Weekly (WRLD and EMKT): **26 weeks**, **104 weeks**, **2 weeks**. Verified digit-for-digit at 4×. |
| The cross-sectional overlay | p.28 | For IPOs and short histories, specific risk is inferred from assets with "similar market capitalisation, in the same industry and country", then blended: "a **weighted sum** of its time-series forecast (if it exists) and its cross-sectional forecast … In the limit this weight is set to **1**." **The functional form of the weighting function is not given.** |
| The other failure mode | p.16 | Before a small-cap factor existed, deciles 9 and 10 still showed significant residual structure (**10.8%** and **21.1%**, above the 10% line) — common variation sitting inside `u`. |
| Named acknowledged failure | p.30 | The model "does **not** adequately capture all relationships between different listings of companies, which have more than one share class with derived securities linked to those share classes, e.g. Chinese MMA securities. This will be addressed in a forthcoming model release." |

**(c) What breaks.** This is the level with the sharpest, best-documented direction of error in the
whole paper.

| If you get this wrong | Which number moves | Direction | Source |
|---|---|---|---|
| Ignore same-company specific correlation, long-only book | Portfolio specific risk | **Too low** | PAPER, p.28 |
| Ignore same-company specific correlation, long-short book | Portfolio specific risk | **Too high** | PAPER, p.28 |
| Leave a real common factor inside `u` (e.g. no small-cap factor) | `Δ` too big, `F` too small; total risk roughly preserved but the **decomposition** lies, and it collapses for a diversified portfolio where the specific part is supposed to net away | INFER, evidenced by p.16 |
| Assume `Δ` truly diagonal in a portfolio holding an ADR and its root | Specific risk | **Too low** | PAPER, p.28 |

The size of the stake is printed: on the p.35 example report, **Specific is 50%** of Active Risk.

**(d) Landing sentence.**
> "The list of leftover-sizes you just built is the `Δ` in equation (1.8) on page 24, where the paper
> calls it *'a diagonal matrix'* — then on page 27 admits it keeps off-diagonal entries after all, and
> on page 28 states your conclusion in its own words: ignoring the link between two listings of one
> company *'would lead to under (or over) prediction of specific risk in a long-only (long-short)
> portfolio context.'*"

---

## 13. LEVEL 10 — THE ASSEMBLY

**(a) Pages.** p.24, essentially alone. Supporting: p.4 (what a portfolio exposure means), p.34
(what the assembled number is used for).

**(b) Point at.**

| Anchor | Page | Sentence version |
|---|---|---|
| Equation (1.7) `r = X f + u` | p.24 | "Each asset's return is its characteristics times the payoff to those characteristics, plus what nobody else can reach." |
| Equation (1.8) `Σ = X F Xᵀ + Δ` | p.24 | `Xᵀ` reads the portfolio's characteristics; `F` says how those characteristics move together; `X` carries the answer back to assets; `Δ` adds each stock's private wobble. |
| The lead-in line | p.24 | "In general a multi-factor model decomposes asset returns as follows:" — the paper introduces (1.7) as the general form, not as BFRE-specific. |
| The ingredient list | p.24 | Portfolio risk is computed from: portfolio holdings, portfolio-level factor exposures "aggregated from the asset level", a factor covariance matrix, and asset specific risk forecasts. |
| Market exposure = position, not sensitivity | p.4 | "The market factor **exposure** of a portfolio should not be confused with its market **beta**." Market factor exposure = "the fraction of portfolio %NAV invested in equities" (footnote 3: plus delta-adjusted derivative exposure). |
| Lineage | p.24, footnote 13 | Rudd and Clasing [24], Grinold and Kahn [25], Connor et al. [17]. The approach is justified by literature precedent, not by an empirical comparison. |

**(c) What breaks.** Every multiplication in (1.8) has a job, and a slip in any one gives a
recognisable wrong answer: drop `Δ` and a single-stock portfolio's risk equals its factor risk (which
is why the p.35 report would show 100% Style/Industry/Country and 0% Specific); drop `F`'s
off-diagonals and two offsetting factor bets stop cancelling, inflating risk; forget that `X` must be
the **portfolio's** exposures (p.24: "aggregated from the asset level") and you price the wrong book.
**PAPER (p.4):** confuse market **exposure** with market **beta** and you will report a fully invested
portfolio as beta 1.00 when the report on p.35 puts its Portfolio Beta at **1.02** with a separate
Market factor exposure entirely.

**(d) Landing sentence.**
> "What you just assembled is printed on page 24 as equation (1.8), `Σ = X F Xᵀ + Δ`, one line below
> equation (1.7), `r = X f + u` — those two lines are the entire model, and the other sixty-four pages
> exist only to say what goes in `X`, what goes in `F`, and what goes in `Δ`."

---

## 14. LEVEL 11 — THE DESK

**(a) Pages.** p.34 (the prose walkthrough of a real risk report) and **p.35** (the report itself,
Figure 1.18). Nothing else in the paper is about using the number.

**(b) Point at.**

| Anchor | Page | What it is |
|---|---|---|
| Figure 1.18 | p.35 | "a sample **Equity Daily Risk (EDR)** report in Aladdin", European Equity portfolio, EMEA model, produced with PRT. |
| The banner | p.35 | **Active Risk 2.99%**, **Portfolio Beta 1.02**, **Portfolio Risk 15.62%**, **Benchmark Risk 14.98%**, Base Currency EUR. *(Residual doubt recorded in the audit: the middle digit of 2.99 is blobby — 2.89 not fully excluded; the last digit of 15.62 is soft — 15.67 not fully excluded. 14.98 and 1.02 are clean.)* |
| The pie | p.35 | "Risk Contributions by Block": Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec **1%** `[INFERRED — the glyph reads 1 or 2; 1% is recorded only because the six then sum to exactly 100]`. The five other values are read directly and are unambiguous. |
| The decomposition claim | p.34 | "Active Risk is then **decomposed** along the different factor blocks in the model … The report shows that the Active Risk is **split equally between common factors and stock specific sources**. Style and industry factors account for most of the common factor risks." |
| The two-axis panels | p.35 | Every block panel plots **"Contrib. (% of Act. Risk)"** as bars against **"Act. Exp."** as dots on a second axis — i.e. contribution and exposure are deliberately shown as different things. |
| The worked tilt | p.34, p.35 | p.34 prose: tilts towards "high volatility, momentum driven, low-yielding, smaller stocks". p.35 panel confirms it factor by factor: Volatility ≈ **+0.42 sd**, Momentum ≈ **+0.38**, Yield ≈ **−0.30**, Size ≈ **−0.20**. **[APPROX — all bar and dot magnitudes on p.35 are pixel measurements, ±10%. The axis tick labels are read directly and are reliable.]** |
| Contribution ≠ exposure, demonstrated | p.35 | Style panel: Emerging carries exposure ≈ **−0.10 sd** and contributes ≈ **0%** of active risk; Market carries exposure ≈ **0.0** and contributes ≈ 0. Country panel: **United Kingdom** has the largest active exposure in the block at roughly **−10% of NAV** *and* the largest risk contribution ≈2.4%. |

**The "diversified" boss round, entirely from p.35.** The PM points at 15 names in the Top Asset
Contributions panel. The model's own answer: 50% of Active Risk is Specific despite 15 holdings, and
the FX panel shows a single currency pair contributing ≈+2.55% of active risk on an exposure dot of
≈+9% of NAV while another pair sits at roughly **−10% of NAV** with a *positive* risk contribution —
a short position adding risk. Diversification across names does not diversify across a shared factor
tilt of +0.42 sd Volatility.

**(c) What breaks.** **PAPER (p.34/35, structure):** if contribution is computed as though it were
exposure, the report ranks positions by size instead of by risk added — and p.35 shows those two
orderings disagreeing (Emerging has exposure and no contribution; Media's ≈+4.5% of NAV exposure sits
third in the industry panel while Integrated Oil's ≈−6% sits first). **INFER:** getting the sign
convention wrong on a short position flips a risk-adding hedge into a risk-reducing one, which is
exactly the mistake the FX panel's negative-exposure/positive-contribution pair is proof against.

**(d) Landing sentence.**
> "The numbers you just computed are the bars in Figure 1.18 on page 35, labelled *'Contrib. (% of
> Act. Risk)'*, plotted deliberately against a second axis of plain exposure so you can see them
> disagree — and the pie in the same figure is how a PM who says *'I hold fifteen names'* gets
> answered: half of that portfolio's 2.99% Active Risk is specific, and most of the other half is one
> style tilt."

**GAP — say it out loud.** The paper contains **no formula for marginal contribution to risk**, no
derivation of risk decomposition, and does not use the term "marginal contribution" or "tracking
error" anywhere. `notes/` has zero hits for both. "Contribution" appears only as a chart axis label on
p.35 and as prose on p.34. Level 11's mathematics is entirely ours; only its *output format* is
citable.

---

## 15. LEVEL 12 — THE CRITIQUE

Every item below is a page the GM can put a finger on. Grouped by the four charges in the level brief.

### 15.1 Unstated parameters and thresholds

| Missing | Page | The paper's exact hedge |
|---|---|---|
| Industry-factor eligibility thresholds | p.8 | "a large proportion of significant t-statistics", "a high number of average squared t-statistics", "a large market capitalization weight", "a large effective number of assets" — **no number for any of the four**. |
| VIF thresholds and values | p.32 | "variance inflation factors were reviewed over the research history and **were found to be well within suitable thresholds**" — no value, no threshold. |
| The specific-risk blend | p.28 | "a weighted sum of its time-series forecast … and its cross-sectional forecast. The weighting function places more weight on the time-series forecast as more data becomes available." **Functional form not given.** |
| The thinness prior | p.36 | "adding a Bayesian prior … diverts the estimated country/industry return … towards a theoretical prior." **Form, strength and shrinkage parameter not specified.** |
| The whole factor-covariance method | p.27 | Deferred to "the **BRS Covariance Matrix Estimation documentation**". |
| Small-Cap / Mid-Cap constants | p.51 | `α₁=0.95, α₂=0.75, α₃=0.2` and `α₁=0.60, α₂=0.54, α₃=0.7` are printed with **no empirical justification** beyond the stated intent to hit deciles 8/9/10 and 6/7. |
| "sufficient market data" | p.31 | Coverage universe "restricted to assets with sufficient market data" — not quantified. |
| Beta window | p.42 | 52-week half-life, 5 years of weeklies — asserted, unjustified. |
| Escalation trigger | p.38 | "Signs of **persistently** poor model performance over **many periods**" — neither quantified. |

### 15.2 Single-anchor-month / thin evidence

| Claim | Evidence offered | Page |
|---|---|---|
| The market factor dominates in a stressed market | **one trading day**, 8 August 2011, Figure 1.1 | p.5 |
| Country factors dominate on a calm day | **one trading day**, 16 August 2011, Figure 1.2 | p.6 |
| Style exposure persistence | one snapshot month, Dec 2013, looking back 24 months, Figure 1.11 | p.17 |
| Style exposure correlations | one date, Dec 2013, Figure 1.3 | p.11 |
| Emerging-market factor is interpretable | ten hand-picked companies, one month (Sept 2013), Figure 1.16 | p.22 |
| All model testing | **no values printed at all** — bias statistics "generated and reviewed", results in reference **[27]**, "**available on request**" and listed in the bibliography as "**forthcoming**" | p.32, p.33, p.65 |

Extra force: neither Figure 1.1 nor Figure 1.2 prints data labels, so the reader cannot check the
magnitudes at all. `notes/` records the bar heights as **[APPROX, read off gridlines only]** and
refuses to firm them up. The GM must do the same.

### 15.3 Unjustified window lengths (a full set, all on one slide)

| Quantity | Window / parameter | Page |
|---|---|---|
| Factor covariance, default | 104 weeks, 26-week half-life | p.27 |
| Specific risk, daily model | 125-day half-life, 375 obs, NW lag 10 | Table 1.3, p.28 |
| Specific risk, weekly model | 26-week half-life, 104 weeks, NW lag 2 | Table 1.3, p.28 |
| Historical beta | 5y weekly, 52-week half-life | p.42 |
| Standard Deviation – 1Y | **daily total** returns, 180-day half-life, 360 obs | p.42 |
| Emerging-market / oil betas | 5y weekly, 52-week emphasis | p.21, p.22 |
| Assets/Sales averaging | 5 years | p.43, p.49 |
| Return on Equity | 2-year average book equity | p.50 |
| Variation in Capital Structure | 4 years of 1-year changes | p.50 |
| Bias statistic | rolling 12 months, 95% CI | p.38 |
| VaR back-test | 99%, 252 days | p.38 (this one **is** justified — UCITS + Kupiec 1995) |

**Internal inconsistencies to hand the player as free ammunition:**
- **p.10 and p.39:** the standardisation mean is **√-cap-weighted** while the standard deviation is
  **equal-weighted**. Stated twice, justified never.
- **p.42:** Historical Sigma is an **equally-weighted** standard deviation of residuals from an
  **exponentially weighted** regression.
- **p.44:** "one month" is **22 working days** for momentum and reversal (footnotes 20, 21) but a
  **calendar** month for Proportion of Active Trade Days.
- **p.45 / p.44:** Return-to-Turnover and Amihud use "the last 360 days with non-missing volume" while
  their neighbours use 3/6/12 calendar months.
- **p.47:** the `s ≤ t` no-look-ahead line is printed under (1.28) and (1.32) only, though (1.29),
  (1.30) and (1.31) mix the same dated numerator with an undated denominator.
- **p.49:** (1.38) is described as a change "over the previous **two years**" but the formula
  `ln A_t − ln A_{t−1}` is a one-year change.
- **p.50 and p.53:** Return on Capital Employed, Return on Assets and Debt-to-Assets are **vendor
  fields from Worldscope with no formula printed at all**, sitting beside descriptors defined to the
  symbol.
- **p.54:** `FS` denotes foreign **sales** in (1.54) and foreign **assets** in (1.55), and (1.54)'s
  where-clause calls `S_{i,t}` "the total assets" when it means total sales.
- **p.26:** the (1.9) where-list pairs `X_Mkt f_Mkt` with the description "Style Exposures and Factor
  Returns" and omits the Style row entirely; both sums in (1.10) are indexed `j` while the second
  summand is subscripted `k`. Both re-verified as **the source's typos**, not transcription errors.
- **p.31:** industry classification switched from GICS to TRBC in **February 2018** with no stated
  reason — meaning the factor history spans two different industry definitions.

### 15.4 Unfalsifiable behavioural stories

| Story | Page |
|---|---|
| Reversal exists because of "market investors **overreacting** to stock information in the near-term" | p.16 |
| Momentum exists because of "market investors systematically **underreacting** to newly available company information" | p.17 |
| Same paper, same section, **opposite** psychology at two adjacent horizons, and the two are deliberately made non-overlapping (11 months with a 1-month lag, p.17/p.44) so that neither story can be tested against the other. |
| Sentiment: the VIX is used "as a **first approximation** to the 'risk-on/risk-off' paradigm" — the proxy is conceded and never defended | p.23 |
| Oil: prices move on "wars, or even **the fear of wars**" | p.22 |
| Industry schema: after statistics, the schema is "**peer reviewed** by other investment and risk professionals at BlackRock … an opportunity to impose **forward-looking views** of industry behaviour into the schema" — the example given is splitting out Alcohol, Tobacco, Casinos & Gaming "due to the increasing investor focus on ESG issues" | p.8 |
| "Throughout the whole selection process, **qualitative judgement** and statistical analysis are combined" — no criterion for the qualitative half | p.12 |

### 15.5 The multiple-testing charge (the strongest single attack)

**PAPER, p.10:** "for i = 1, 2, …, N (where **N ≥ 200** is the number of candidate substyles)".
**PAPER, p.55:** "a subset of the full list of **200+**", with each horizon variant counted separately.
**PAPER, p.56, Table 1.4:** the printed inventory runs to 18 styles and 108 substyles (*both counts
derived by the transcriber from the printed rows — the page prints no totals*) — **and it contains a
style called "Random", whose single substyle is "Random Substyle".**
**PAPER, p.8:** significance is judged at |t| > 2.
**PAPER, p.55:** "**no** information about the selection procedure — no criterion, statistic, or
threshold by which substyles were kept or discarded, and **no multiple-testing correction is
mentioned** despite 200+ candidates being tested."

The authors put a placebo in the candidate set — which shows they understood the problem — and then
report no correction for having tested 200+ candidates at a fixed 2-sigma bar. **Have the player
defend that** (the recursive procedure conditions each test on the model built so far; the 10–15%
stopping rule on p.12 is a persistence requirement, not a one-shot p-value; sub-sample checks on p.8
guard against period-specific flukes) **and then attack it** (none of that is a multiple-comparison
correction, and the paper never says what the Random Substyle scored).

**(d) Landing sentence for L12.**
> "You now know enough to notice three things at once: page 32 says the multicollinearity diagnostics
> 'were found to be well within suitable thresholds' without printing a single number; page 33 sends
> you for the actual test results to reference [27], which the bibliography on page 65 lists as
> *forthcoming*; and pages 5 and 6 rest the whole country-versus-market story on two individual
> trading days in August 2011."

---

## 16. ★ THE REBUILD

**(a) Pages.** p.24, p.25, p.26, p.27, p.28. Five pages contain the entire buildable model. Everything
else is what goes into `X` (pp.4–23, 39–56) or what the output looks like (pp.34–37).

**(b) The five-page checklist — hand this to the player only after they have finished.**

| Step | Anchor | Page | The parameter the paper actually prints |
|---|---|---|---|
| 1. Build `X` | Table 1.1 (18 style descriptions); (1.12)–(1.55) for substyle formulas; pp.40–41 for the substyle→style weights per region; p.39 for the five transformations | p.9; pp.42–54; pp.40–41; p.39 | Exposures standardised to √-cap mean 0, equal-weighted sd 1, capped at **±3** (p.39) |
| 2. Estimate `f`, pass 1 | Equation (1.9) | p.25 | Weights = **√ market capitalisation** (p.25); blocks = Market, Style, Core Industry, Core Country |
| 3. Identify the solution | Equation (1.10) | p.26 | Weighted average Core Industry return = 0; weighted average Core Country return = 0. One restriction only for single-country models |
| 4. Estimate `f`, pass 2 | Equation (1.11) | p.26 | Extended Industry and Extended Country factors fitted to pass-1 residuals `u` |
| 5. Build `F` | (1.8); construction on p.27 | p.24, p.27 | Daily factor returns from **March 1996**; default **WKL**: **104 weeks**, **26-week half-life**; serial-correlation correction |
| 6. Build `Δ` | p.27–28; Table 1.3 | p.27, p.28 | Daily: half-life **125 days**, **375** obs, NW lag **10 days**. Weekly (WRLD, EMKT): **26 weeks**, **104 weeks**, NW lag **2 weeks**. Plus same-company specific correlations (override **1** or estimated) |
| 7. Assemble | Equation (1.8) `Σ = X F Xᵀ + Δ` | p.24 | — |
| 8. Price a portfolio | p.24 ingredient list; Figure 1.18 for the output shape | p.24, p.35 | Holdings + portfolio exposures aggregated from asset level + `F` + specific risk forecasts |

**(c) What breaks.** All of it. The rebuild is where every earlier direction-of-error claim becomes
simultaneously live. The single highest-leverage check to run on a rebuilt model, and the one the
paper itself corroborates: compute the split between common-factor risk and specific risk. For the
paper's own worked example on p.35 it is **50/50**, with Style **25%** and Industry **14%** of the
total. A rebuild returning 95% specific has an `X` that explains nothing; one returning 95% common has
factors that have absorbed idiosyncratic noise. Neither will be flagged by any diagnostic the paper
prints, because — see §15 — the paper prints no diagnostic values at all.

**(d) Landing sentence.**
> "Everything you built is on five pages. Page 24 has the model, equations (1.7) and (1.8). Page 25
> has the regression, equation (1.9). Page 26 has the two restrictions that make it solvable,
> equation (1.10), and the second pass, equation (1.11). Pages 27 and 28 have the six numbers —
> March 1996, 104 weeks, 26 weeks, 125 days, 375 days, 10 days. The other sixty pages tell you what to
> put in `X` and what the answer is supposed to look like when you print it."

---

## 17. NEVER CITE — things that are not in this paper

The audit of `notes/` caught a fabricated cross-reference. These are the invitations to repeat that
mistake. If the GM needs any of them, the honest move is *"the paper assumes this and never builds
it — so we are going to build it."*

**Absent from all 65 pages (zero hits in `notes/`):**
- eigenvalue, eigenvector, principal component, eigen-decomposition
- "least squares", normal equations, `Σx·e = 0`, any derivation of a regression coefficient
- standard error (as a formula or a concept the paper explains), degrees of freedom
- an `R²` **formula** (p.32 defines it in words only)
- marginal contribution to risk, risk decomposition mathematics
- "tracking error" (p.35's banner says **Active Risk**)
- "orthogonal" (the paper says "**neutral**", p.5)
- Frisch–Waugh–Lovell (the mechanism is used on pp.7, 10, 12, 52; the name never appears)
- shrinkage of `F` (the only shrinkage is the p.36 Bayesian prior on thin country/industry **returns**;
  LASSO/LARS/Ridge appear on p.8 only as **rejected alternatives**)
- any statement of how many factors a model has in total, or of the observation-to-factor ratio

**Present but must never be firmed up:**

| Item | Page | The exact caveat that must travel with it |
|---|---|---|
| The portfolio-beta formula `βₚ,b = (Xₚᵀ F X_b)/(X_bᵀ F X_b)` | p.4 | **A reader's handwritten margin annotation.** Not the paper's text. |
| Figures 1.1 / 1.2 bar heights | p.5, p.6 | **[APPROX, read off gridlines only, no data labels printed.]** Market bars roughly −4.5% to −6.5%; POL ≈ +3.5%, GRC ≈ +2.8%, HUN ≈ −3.0%, DNK ≈ −2.3% on 16 Aug. Eyeball estimates. |
| Figure 1.4 / 1.5 / 1.8 / 1.10 bar percentages | pp.12, 15, 16 | Pixel-measured against the calibrated axis, **not printed**. |
| Figure 1.5's top y-axis label | p.12 | **[UNREADABLE: 45.0% vs 45.5% cannot be settled from the ink alone.]** Label pitch forces 45.0%; the glyph does not. |
| Figure 1.6, 1.7, 1.12, 1.14 levels | pp.13, 14, 18, 20 | Measured, ±3pp on Fig 1.14; Fig 1.6's page is **warped** (gridlines drift ~0.15 units), so late-sample readings are worse. |
| Figure 1.9 cell **signs** | p.15 | **[UNREADABLE]** — the greyscale ramp is **diverging**, so darkness encodes magnitude, not sign. No cell's sign is recoverable. |
| Figure 1.11 trace → legend mapping | p.17 | **[UNREADABLE]** — dash patterns are not separable. Never say "the reversal line": say "one series collapses to ≈0 by lag 1, which a one-month-return exposure would do." |
| Figure 1.17 sector bar values | p.23 | Pixel-measured (Energy ≈ +0.55, Materials ≈ +0.61); the source **prints no digits at all** for this figure. |
| Figure 1.18 bar and dot magnitudes | p.35 | **Every one is a pixel measurement, ±10%.** Axis tick labels are reliable; bar values are not. |
| Figure 1.18 "Act Sec 1%" | p.35 | **[INFERRED]** — the glyph reads 1 or 2; 1% is chosen only because the six slices then sum to 100. |
| Figure 1.18 banner digits | p.35 | 2.99% (**2.89 not fully excluded**), 15.62% (**15.67 not fully excluded**). 14.98% and 1.02 are clean. |
| CAND Foreign Sensitivity weight | p.40 | **[UNREADABLE]** — one `0.5` glyph sits between the Foreign Sales and Foreign Assets rows. **Do not assume 0.5/0.5.** Taken literally the column sums to 0.5, not 1.00. |
| Tables on pp.58, 62, 63 | pp.58, 62, 63 | Captions cropped out of the photographs. **Do not cite "Table 1.12" or "Table 1.13"** — the numbers are not visible. p.58's first table's region is unknown. |
| The `lê_{i,s}` symbol in (1.49) | p.52 | Legible at 14×; **meaning ambiguous** — the paper never defines it, describing it in prose only as "the residuals in regression (1.12)". |
| The Mid-Cap rank symbol `r_{i,t}` in (1.48) | p.51 | Same glyph the paper uses for returns; the page says it is "defined below" and **no definition appears**. |
| Small-Cap rank direction | p.51 | The page **never states whether rank 1 is the largest or smallest company.** Reading the flat top as "the smallest ~5%" is an inference from stated purpose. |
| Table 1.2's NAMR row set | p.10 | 13 rows: Market + **12** styles. Small-Cap, Leverage, Quality, Foreign Sensitivity, Oil, Emerging Market do **not** appear in this table. Do not quote a NAMR number for a factor that is not in it. |

---

## 18. Fastest lookups at the table

| The GM needs… | Go to |
|---|---|
| The model in two lines | p.24, (1.7) and (1.8) |
| The regression that produces every factor return | p.25, (1.9) |
| Why the regression needs help to be solvable | p.26, (1.10) + the "three intercept terms" paragraph |
| A real factor return, with its Sharpe and its market correlation | p.10, Table 1.2 |
| A real exposure correlation | p.11, Figure 1.3 |
| Every parameter of the specific-risk model | p.28, Table 1.3 |
| The only parameters of the factor covariance model the paper prints | p.27 (WKL, 104 weeks, 26-week half-life, March 1996) |
| The direction a risk number moves when `Δ` is wrong | p.28, the "under (or over) prediction" sentence |
| A risk report to argue with a PM about | p.35, Figure 1.18 |
| The list of every style and what it means | p.9, Table 1.1 |
| The formula for any substyle | pp.42–54, equations (1.12)–(1.55) |
| Which substyles go into which style, per region | pp.40–41 |
| The complete candidate inventory (including the placebo) | p.56, Table 1.4 |
| Something to attack | p.8, p.27, p.32, p.33, p.36, p.55 |
