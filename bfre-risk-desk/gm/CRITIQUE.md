# LEVEL 12 — THE CRITIQUE: attack & defence dossier

Game-master reference for **THE RISK DESK** (`prompt/RISK_DESK.md`), Level 12 boss round:
*"Defend the paper's choices as a BlackRock author, then attack them as a rival. Both convincingly."*

Companion to `gm/LEVEL_ANCHORS.md`. That file says **where things are**; this one says **what is wrong
with them, what is not wrong with them, and how each side wins the exchange**.

**Source of truth: `notes/` only** — the page-indexed transcription of all 65 PDF pages. Every page
reference below was read in `notes/` before being written down. The transcription audit caught one
fabricated cross-reference; the standard here is therefore: *quote or paraphrase something actually
read*. Anything that is the GM's own reasoning is marked **INFER** and must be spoken as "this
follows from…", never as "the paper says…".

---

## 0. HOW TO RUN THIS LEVEL

The level fails in two directions, and the second is the common one.

| Failure mode | What it looks like | What it means |
|---|---|---|
| **Can't attack** | Player says "it's BlackRock, it's probably fine" | They are reading, not auditing. Send them to §5. |
| **Can only attack** | Player machine-guns every unstated number | Worse. A rival who attacks everything is attacking nothing. Send them to §6. |
| **Attacks a cheap shot** | Player leads with √-cap weighting, or a typo | Instant credibility loss. This is the thing the level exists to teach. |

**The order of play.** Defence first, attack second. A player who attacks first will straw-man
themselves — they will build a weak version of the paper and then knock it down, and they will not
notice. Making them argue the BlackRock side *first*, with no warning that an attack is coming, forces
them to find the real arguments before they need to beat them.

**The pass bar.** Tier 4 on the five-tier ladder — *Defend: can survive an expert attacking it*. In
practice: the player must be able to take **any three items from §5**, give claim / page / attack /
defence for each, and then say which of the three they would actually lead with in a real meeting and
why. Naming weaknesses is Tier 2. Ranking them is Tier 4.

**Currency.** Award bps for a **correctly ranked** attack. Dock bps for any attack from §6 delivered
without the qualification that goes with it.

---

## 1. CONVENTIONS AND THE THREE BINDING RULES

| Mark | Meaning |
|---|---|
| **PAPER** | The paper says this. Quote or close paraphrase from `notes/`. |
| **INFER** | The GM's or the rival's reasoning *from* things the paper says. Never attribute to BlackRock. |
| **GAP** | The paper does not contain this at all. Say so out loud. |
| `[APPROX]` | Read off a chart's gridlines or pixel-measured. **Not a printed number.** |
| `[UNREADABLE]` | The scan could not resolve it. Carry the uncertainty forward verbatim. |
| `p.24` | PDF page 24. For pp.2–65 the PDF index equals the printed footer number. |

**Rule 1 — no laundering.** Several of the sharpest attacks rest on figure values that the paper
**does not print**. Figure 1.8's ≈7% for Sentiment is a pixel measurement, not a transcribed number.
An attack built on it must be delivered as *"the bar is visibly the second-shortest and sits below the
printed 10% line; the paper prints no value, which is itself part of the complaint."* A player who
says "Sentiment scores 7%" has invented a number and loses the point.

**Rule 2 — separate the scan from the paper.** "I can't read this figure" is a criticism of a phone
photograph. "**This figure has no data labels**" is a criticism of the paper — and it is true of every
bar and line chart in it (see §6, "CS-10, done properly"). Only the second is admissible.

**Rule 3 — absence claims are claims.** "The paper never justifies X" is checkable and is used
throughout this file. "The paper never does X anywhere in 65 pages" is stronger and is used only where
`notes/` supports it. Do not upgrade the first into the second at the table.

---

## 2. JARGON-UNLOCK LEDGER FOR THIS FILE

Terms appear freely below. **The GM must not leak a name at the table before the level that buys it.**

| Term | Unlocked at | First BFRE appearance |
|---|---|---|
| residual / the miss | L0 | `u` in (1.7), p.24 |
| exposure, factor return | L1 | `X`, `f` in (1.7), p.24 |
| neutral (the paper's word for orthogonal) | L4 | p.5 |
| multicollinearity, variance inflation factor | L4 | p.32 |
| intercept | L5 | p.26 ("three intercept terms") |
| z-score / standardisation | L5 | p.10; p.39 |
| t-statistic, statistically significant | L6 | p.8 (\|t\| > 2) |
| cross-sectional regression | L7 | p.24 |
| in-sample / out-of-sample | L7 or L12 | p.30 ("Out-of-sample model back-testing") |
| factor covariance matrix `F`, half-life | L8 | (1.8) p.24; p.27 |
| shrinkage / Bayesian prior | L8 | p.36 (thinness prior); p.8 (LASSO/Ridge, **rejected**) |
| specific risk `Δ`, diagonal | L9 | (1.8) p.24; p.27 walks "diagonal" back |
| active risk | L11 | p.34, p.35 banner |
| **bias statistic** | **L12** | p.32, p.38 |
| **sensitivity analysis** | **L12** | **GAP — never appears** |
| **multiple testing / data mining** | **L12** | **GAP — never named**; the *problem* is visible at p.10, p.55, p.56 |
| **placebo / control descriptor** | **L12** | p.56 Table 1.4 "Random Substyle" (the paper offers no prose) |
| **falsifiable** | **L12** | **GAP — the GM's word, not the paper's** |
| **post hoc** | **L12** | **GAP** |
| **look-ahead bias** | **L12** | **GAP — the mechanism is on p.47 as `s ≤ t`; the name never appears** |
| heteroskedasticity | L12 (graduate) | p.25 |
| Newey–West / serial correlation | L12 (graduate) | p.27, p.28, p.38, ref [26] p.65 |
| tracking error | **never, from this paper** | **GAP — p.35's banner says "Active Risk"** |
| eigenvalue / principal component | **never, from this paper** | **GAP — zero occurrences in 65 pages** |

---

## 3. DIFFICULTY FLAGS — say these out loud

The rules require honesty about difficulty. Five items below are genuinely graduate-level. If the
player struggles on these, that is calibration, not failure.

| Item | Where in this file | Why it's hard |
|---|---|---|
| **Multicollinearity / VIF** | G-2 | The diagnostic itself is a graduate topic; the paper reports it as an adjective. |
| **Shrinkage / Bayesian priors** | A-4, F-2 defence | LASSO, Ridge, group lasso — a whole literature the paper names and declines. |
| **Multiple-testing correction** | F-2 | The single strongest attack in the dossier and the hardest to state precisely. |
| **Heteroskedasticity** | §6 CS-1 | The paper's own justification for √-cap weights (p.25). Needed to *not* attack it. |
| **Invariance of `XFXᵀ` to rescaling a column of `X`** | §5.1 DEFENCE 3 | Derivable once L10 exists, but it is a real algebraic argument and it is the best defence in the whole file. |

Not graduate, and the player should get these unaided: single-date evidence, unstated thresholds,
unfalsifiable stories, deferred documents, internal inconsistencies.

---

## 4. THE SCOREBOARD — one glance, ranked

Ranked by **how much a rival gains by raising it**, not by how wrong the paper is.

| Rank | Item | § | Page(s) | Attack strength | Defence strength |
|---|---|---|---|---|---|
| 1 | Testing evidence deferred to a **forthcoming** document | G-3 | 32, 33, 65 | ★★★★★ | ★★★☆☆ |
| 2 | 200+ candidates, no multiple-testing correction, **a placebo in the set whose score is never reported** | F-2 | 10, 55, 56 | ★★★★★ | ★★★★☆ |
| 3 | Stated 10% inclusion bar vs factors shipped below it | F-1 | 14, 15, 10, 32 | ★★★★☆ | ★★★★☆ |
| 4 | No diagnostic value printed anywhere — VIFs "well within suitable thresholds", `R²` with no number | G-1, G-2 | 32 | ★★★★☆ | ★★★☆☆ |
| 5 | Whole factor-covariance method deferred to internal documentation | A-6 | 27 | ★★★★☆ | ★★★☆☆ |
| 6 | Every window and half-life asserted; **no sensitivity analysis anywhere** | D | 27, 28, 42, 38 | ★★★★☆ | ★★★☆☆ |
| 7 | Reversal = overreaction, momentum = underreaction, built non-overlapping | E-1 | 16, 17, 44 | ★★★★☆ | ★★★★☆ |
| 8 | Four different data frequencies for one 1-month forecast | B-1 | 8, 24, 27, 30 | ★★★★☆ | ★★★★☆ |
| 9 | **Standardisation asymmetry** — √-cap mean, equal-weighted sd | 5.1 | 10, 39 | ★★★☆☆ | ★★★★★ |
| 10 | Industry eligibility rule stated in four adjectives, no numbers | A-1 | 8 | ★★★☆☆ | ★★★☆☆ |
| 11 | Two adjacent trading days carry the country-vs-market argument | C-1 | 5, 6 | ★★★☆☆ | ★★★★☆ |
| 12 | Small-Cap / Mid-Cap constants printed bare | A-5 | 51 | ★★★☆☆ | ★★☆☆☆ |
| 13 | Specific-risk blending function form never given | A-3 | 28 | ★★★☆☆ | ★★★☆☆ |
| 14 | Thinness Bayesian prior — form, strength, parameter all absent | A-4 | 36 | ★★★☆☆ | ★★★☆☆ |
| 15 | EMEA yield merge on "highly correlated" where the printed correlations are 0.28–0.50 | C-4 | 20 | ★★★☆☆ | ★★☆☆☆ |
| 16 | Historical Sigma: equal-weighted sd of exponentially-weighted residuals | B-2 | 42 | ★★★☆☆ | ★★☆☆☆ |
| 17 | Industry classification switched GICS→TRBC in Feb 2018, after the tested history ended | H-1 | 31, 32 | ★★★☆☆ | ★★★☆☆ |
| 18 | Quality "only APXJ" in prose, APXJ **and** EMKT in the weight tables | H-2 | 21, 41 | ★★☆☆☆ | ★☆☆☆☆ |
| 19 | Structural-vs-empirical choice pushed to the user with no accuracy evidence | E-4 | 28, 29 | ★★☆☆☆ | ★★★★☆ |
| 20 | Prose/formula mismatches, symbol reuse, typo'd where-lists | H-3…H-5 | 26, 45, 49, 54 | ★★☆☆☆ | ★★☆☆☆ |

**If the player may raise only one thing:** rank 1. It is short, checkable in two page-turns, and it
converts every accuracy claim in the document into an assertion.
**If the player may raise only one thing and must survive the answer:** rank 2. The defence is strong,
which is what makes it a real exchange rather than a gotcha.

---

# 5. THE DOSSIER

## 5.1 THE WORKED EXAMPLE — the standardisation asymmetry

*This is the calibration item. It is a real weakness with an unusually good defence, and the full
three-move exchange is written out so the GM can see the standard the rest of the file is held to.*

**CLAIM (PAPER, p.10, verified word-for-word in `notes/`):**
> "The **mean** is defined as the square-root of market capitalisation weighted average value so that
> the transformed substyles (and styles) have the property that their weighted average is zero.
> Additionally, these values are divided by their **equally-weighted standard deviation** so that a
> value of +1 for a substyle or style can be interpreted as a security having an exposure of one
> standard deviation above the market average."

**Restated (PAPER, p.39, Huberisation):** exposures "take values between **+/- 3** and are
standardised to a **square-root capitalisation mean of zero**, with an **equal-weighted standard
deviation of one**."

**WHY IT'S WEAK.** Two moments of the same distribution, computed on two different weighting schemes,
stated twice in one document, justified neither time. `notes/` records the asymmetry on both pages and
records that no reason is given on either. The paper is fluent about weighting elsewhere — p.25 spends
a full paragraph defending √-cap regression weights and footnote 14 even names and dismisses the
textbook alternative — so the silence here is conspicuous rather than merely brief.

**ATTACK (rival quant).**
> "You have told me what zero means and what one means, and you have used two different populations to
> define them. The centre is the market's centre — a few hundred mega-caps decide it. The unit is the
> equal-weighted crowd's unit — five thousand small caps decide it. So an exposure of +1.0 is not 'one
> standard deviation above the market average' in any single population; it is a distance measured
> with one ruler from an origin placed by another. Worse, the two move differently through time:
> in a concentrated market the √-cap mean drifts toward a handful of names while the equal-weighted
> spread barely moves, so the same company on the same fundamentals gets a different exposure — and a
> different risk number — for reasons that have nothing to do with the company. If it doesn't matter,
> say so and use one scheme. If it does matter, tell me which one and why."

**DEFENCE (BlackRock author) — three moves, all genuine.**

1. **The two moments answer two different questions.** The mean answers *"what is average?"* and the
   answer has to be true of a **portfolio**, because the model's output is portfolio risk. A √-cap
   weighted centre makes "zero exposure" mean "the exposure of the market", which is what makes p.4's
   market factor coherent: footnote 2 defines the market factor return as the cross-sectional average
   return **using regression weights, i.e. √-market-cap**. Centre the exposures equal-weighted and the
   market factor and the style factors would be centred on two different markets. The standard
   deviation answers *"what is a unit?"*, and a unit should describe the **opportunity set** — the
   names a manager can actually pick from. Equal-weighting is the right choice for a scale precisely
   because it is not dominated by twenty names.
2. **It protects comparability, which is the stated purpose.** p.10 says standardisation exists "to
   facilitate comparison of securities across different regions". A √-cap-weighted standard deviation
   would be set by each region's largest handful of companies — so "one standard deviation" would mean
   something different in Latin America than in North America, and something different in 2013 than
   in 1999. The equal-weighted spread is far more stable across regions and through time, which is
   exactly what a common scale requires.
3. **(INFER — the strongest move, and it is ours, not the paper's.)** *A constant rescaling of a
   column of `X` cannot change the risk number at all.* Scale a style column by `c`. Least squares
   returns `f̂/c` for that factor; its variance in `F` scales by `1/c²`; the contribution to
   `X F Xᵀ` is `(cx)(1/c²·Var f)(cx) = x·Var(f)·x` — unchanged. So the choice of scale is a choice
   about **interpretation**, not about risk. Given that, the sensible criterion is precisely the one
   BlackRock used: pick the mean that makes the market factor interpretable and the scale that makes
   cross-region comparison interpretable. **Say plainly at the table:** the paper never prints this
   argument; it is the defence a BlackRock author *should* give and the player should be able to
   construct it from Level 10's `V = XFXᵀ + D`.

**COMEBACK (the rival is not finished — this is what makes it a Tier-4 exchange).**
> "Your invariance argument holds for a **constant** rescaling. Yours is not constant. The
> standard deviation is re-estimated every period from a changing universe, so the scale factor is a
> time series, and a time-varying rescaling does not pass through cleanly — it goes into the estimated
> factor-return series, and therefore into `F`. And it is not even a pure rescaling: p.39 caps every
> exposure at ±3 **after** the division. A cap is a nonlinear transform. Rescale first and clip
> second, and you clip a different set of companies than if you had clipped first — so the scale
> choice decides *who gets truncated*, and truncation is not invariant to anything."

**Verdict for the GM.** A real weakness — genuinely unjustified — but a *low-yield* one. The invariance
argument means the harm is bounded and interpretive rather than numerical, until the cap and the
time-variation are brought in. A player who raises it as their **opening** attack has misjudged;
a player who raises it as a *"and while I'm here, why two weightings?"* has judged well.

**Callbacks:** L5 (centering, the pivot at `x̄`), L8 (`F`), L10 (`V = XFXᵀ + D`, which the invariance
argument needs).

---

## 5.2 CLASS A — PARAMETERS AND THRESHOLDS STATED WITHOUT JUSTIFICATION

### A-1 · The industry-eligibility rule is four adjectives
**CLAIM (PAPER, p.8).** An industry becomes a candidate factor on four criteria: "a large proportion
of significant t-statistics", "a high number of average squared t-statistics", "a large market
capitalization weight", "a large effective number of assets".
**WHY WEAK.** No number for any of the four. "Effective number of assets" is used as a criterion and
**never defined anywhere in the paper**. And there is no stated rule for combining them — a candidate
that is large on two and small on two has no determinate fate.
**ATTACK.** "Four criteria, four adjectives, zero numbers, and one of them — *effective* number of
assets — is a technical quantity you never define. Then p.58 shows a UK industry factor with **2
assets** and another with **3**, and p.60 shows an Asia-Pacific health-care factor carrying **440**.
Both passed the same rule. That rule cannot have existed as a rule."
**DEFENCE.** The criteria are a *screen* feeding a documented procedure, not the procedure itself.
p.8 states what actually decides: a frequentist stepwise search up the schema hierarchy, cluster
analysis where a level's industries are not all eligible, then peer review by investment
professionals. The four criteria exist to stop the search producing statistically-significant
industries that no one can trade — an industry factor needs *enough assets and enough capitalisation
to be estimable and investable*, and the right threshold for that genuinely differs between a market
with ~2,200 names (NAMR, p.57) and one with ~440 (p.62) *(both sums derived by the transcriber; neither page prints a total)*. Hard-coding a number would produce worse
schemas, not better ones. The 2-asset UK factor is not an oversight: UKIN carries the **whole UK
market** in 28 factors and dropping a distinct industry because it has few listings would push its
returns into the residual and inflate specific risk for exactly those names.
**COMEBACK.** "Then publish the *range*, or the trade-off, or one worked case. You published the
asset counts (pp.57–63) — you had the data to show where the line fell and you chose not to."
**Callback:** L6 (the t-statistic and its threshold), L9 (what falls into `Δ` when a factor is dropped).

### A-2 · VIFs reported as an adjective
**CLAIM (PAPER, p.32).** "variance inflation factors were reviewed over the research history and
**were found to be well within suitable thresholds**."
**WHY WEAK.** No value, no threshold, no distribution, no worst case, no factor named. Same page
explains exactly what goes wrong when it fails — "significant instability in the factor return
estimates through time" — so the paper knows the stake and still prints no number. And Figure 1.3
(p.11) prints **Size–Liquidity at 0.74** in NAMR, which is the highest off-diagonal exposure
correlation in the model and precisely the case a VIF exists to police.
**ATTACK.** "You printed a 0.74 correlation between two style columns on page 11 and on page 32 you
tell me the collinearity diagnostic was 'well within suitable thresholds'. Which threshold? Whose?
What was the number for Size and Liquidity? You have given me a pass mark for an exam whose questions
and pass line are both unpublished." **(Graduate-level: flag VIF as such.)**
**DEFENCE.** A VIF number without its context is close to meaningless anyway — the conventional bars
(5, 10) are folklore, not theory, and the quantity that actually matters is whether the *apportionment
between two collided factors is stable through time*, which is what p.32 says was reviewed and is a
qualitatively different check from a single cross-sectional VIF. More to the point, the paper does not
merely assert the check — it shows the **design responses** to collinearity throughout: momentum is
defined over 11 months with a one-month lag explicitly "to exclude the reversal effect" (p.17, p.44);
EMEA's Earnings Yield and Dividend Yield were **merged** into a single yield factor when they proved
too close (p.20); the entire style-selection procedure judges a candidate on the *residuals* of the
model without it ((1.3)–(1.6), pp.10–12), which is a collinearity control by construction. Those are
better evidence of collinearity discipline than a table of VIFs would be.
**COMEBACK.** "All three of those are decisions taken *before* the model shipped. The VIF is the
ongoing monitor. You have shown me the design and withheld the monitor."
**Callback:** L4 (the collision, and the determinant going to zero — footnote 16 on p.32 is that fact
in the paper's own words).

### A-3 · The specific-risk blending function has no form
**CLAIM (PAPER, p.28).** For assets with little history (IPOs), a cross-sectional overlay infers
specific risk from assets of "similar market capitalisation, in the same industry and country". The
final forecast is "a **weighted sum** of its time-series forecast (if it exists) and its
cross-sectional forecast. The weighting function places more weight on the time-series forecast as
more data becomes available. In the limit this weight is set to 1."
**WHY WEAK.** Everything about the function except its endpoints is missing: no functional form, no
rate, no "sufficient history" threshold, no statement of how "similar market capitalisation" is
binned. Two implementations obeying every word on p.28 could give a new listing materially different
specific risk.
**ATTACK.** "This is a shrinkage rule with the shrinkage parameter left blank. For an IPO — the single
case where specific risk matters most and is least known — you have documented the two endpoints of a
curve and nothing in between."
**DEFENCE.** The *direction* is what a user needs and it is fully stated: more data ⇒ more weight on
the asset's own history, converging to pure time-series. The shape between endpoints is a smoothing
choice with second-order consequences for a forecast that is, for a genuinely new listing, dominated
by the cross-sectional prior no matter what curve is used. And the cross-sectional prior itself **is**
specified — same industry, same country, similar size — which is the part that determines the number.
**COMEBACK.** "Then it costs you nothing to print the curve."
**Callback:** L9 (`Δ`), L8 (shrinkage — graduate).

### A-4 · The thinness prior
**CLAIM (PAPER, p.36).** "We impose the thin country/industry correction by **adding a Bayesian
prior**, which in essence diverts the estimated country/industry return away from the sample factor
return and towards a **theoretical prior**."
**WHY WEAK.** "Theoretical prior" is not a specification. Form, strength and shrinkage parameter are
all absent — `notes/` states this explicitly for p.36. This is the one place in the model where an
estimate is *deliberately moved away from the data*, and the amount of the move is unpublished.
**ATTACK.** "Every thin country and thin industry factor return in this model is a blend of the data
and a prior you have not written down. That is not a modelling detail — it means a Frontier-market
factor return is partly an assumption, and I cannot tell how much."
**DEFENCE.** This is exactly the right thing to do and the paper says why: for markets where "limited,
or no data exists to reliably estimate those factor returns", the unshrunk estimate is worse than
useless — it is noise that will be reported as a country return and will propagate into `F`. The
alternative designs are worse: drop the factor (its returns land in `Δ` and specific risk absorbs
country risk, understating diversification benefits) or estimate it unshrunk (a two-asset country
factor with a wild return). The paper also does not hide this: the correction is named in the
production process and its purpose stated — "capturing a true country/industry return rather than
asset-specific returns". And this is the second pass, which by construction handles only Extended
Countries — Secondary Emerging, Frontier and Watch markets (p.25) — never a Core market.
**COMEBACK.** "Naming a technique is not documenting a parameter. And it interacts with the two-pass
design: extended factors are fitted to first-pass residuals (1.11, p.26) and never re-estimated, so
whatever the prior does, it does permanently."
**Callback:** L8 (shrinkage — graduate), L3 (the second pass).

### A-5 · Small-Cap and Mid-Cap constants, printed bare
**CLAIM (PAPER, p.51).** Small-Cap (1.47): `α₁ = 0.95, α₂ = 0.75, α₃ = 0.2`. Mid-Cap (1.48):
`α₁ = 0.60, α₂ = 0.54, α₃ = 0.7`. Stated intent: the functional form "is designed to give exposure to
smaller companies which reside in capitalisation **deciles 8, 9 and 10**"; Mid-Cap "assigns an exposure
to companies in **deciles 6 and 7**".
**WHY WEAK.** Six numbers, no derivation, no sensitivity. `σ_t` is calibrated so the Gaussian takes
value `α₃` at rank `α₂ · M_t` — so the authors pin the curve through a chosen point, and the point is
chosen, not fitted. Two further defects on the same page: Small-Cap ranks against the **Estimation
Universe** while Mid-Cap ranks against the **standardisation universe**, unexplained; and the page
**never states whether rank 1 is the largest or the smallest company** — reading the flat top as
"the smallest ~5%" is an inference from stated purpose, not something printed.
**ATTACK.** "Six constants, no justification, two different universes for two versions of the same
idea, and a rank variable whose direction you never state. `α₃ = 0.2` versus `α₃ = 0.7` is a
threefold difference in how fast exposure decays away from the target deciles, and you have given me
no reason for either."
**DEFENCE.** The constants are not free parameters fitted to returns — they are **targeting
constants**, and the target is stated and evidenced. p.16 shows *why* the factor exists at all
(Figure 1.10: before a small-cap factor, deciles 9 and 10 carry significant explanatory power above
the printed 10% line; after, they do not `[APPROX — bar values pixel-measured, not printed]`), and
p.15 says the research was decile-by-decile. Given the target deciles, the constants are just the
algebra that puts a smooth bump there. Smoothing itself is justified in the paper's own words: a
smooth function is used in preference to 0/1 indicators "to mitigate instability in exposures for
assets on the decile boundaries" (p.16) — i.e. these constants exist to *stop* a stock's exposure
flipping when it crosses a rank boundary, which is a stability argument, not a fitting exercise.
**COMEBACK.** "Then show me the exposure profile against decile — one chart — and I'll agree.
And I still need to know which end rank 1 is."
**Callback:** L5 (a smoothed column of ones), L6 (the decile test on p.16).

### A-6 · The factor covariance method is not in the paper
**CLAIM (PAPER, p.27).** The default is WKL (weekly long-term), 104 weeks of factor returns,
26-week half-life, daily history from March 1996, exponential decay, serial-correlation correction.
Then: "Model users are referred to the **BRS Covariance Matrix Estimation documentation** for
technical details on the factor covariance matrix methodology."
**WHY WEAK.** `F` is one of the two matrices in the model. Four numbers and a pointer is the whole
public specification. p.30 compounds it: "All the standard assumptions of BRS' Covariance Matrix
Estimation methodology apply" — assumptions inherited wholesale from a document not supplied.
**ATTACK.** "Equation (1.8) has two objects in it. You have documented `Δ` to the parameter — Table
1.3, page 28, half-lives, observation counts, Newey–West lags. And for `F` you have given me four
numbers and a cross-reference to an internal document. Half of my risk number is specified by
reference."
**DEFENCE.** This is deliberate architecture, not omission. The covariance estimator is **shared
infrastructure at the BRS level, not a BFRE component** — p.30 says "All the standard assumptions of
**BRS' Covariance Matrix Estimation methodology** apply", i.e. it is a house methodology BFRE consumes,
versioned and released on its own cycle. *(That it is shared with STORM specifically is **INFER** — the
paper does not say so.)* Documenting it inside a BFRE
paper would guarantee the two drift out of sync, which is a worse failure than a cross-reference. And
the parts that are *BFRE-specific* are all here: which factor returns go in, from when (March 1996),
at what frequency, with what default half-life and window — and p.27 tells the user they can change
the half-life, control for serial correlation and asynchronicity, and re-estimate the whole matrix
themselves in PRT. A user who wants a different `F` is not blocked; they are handed the tool.
**COMEBACK.** "The cross-reference is to a document the reader does not have. And the flexibility
argument cuts the other way: if a user can change the half-life, a user needs to know what changing it
does — which is a sensitivity analysis, and there isn't one (see §5.5)."
**Callback:** L8 (`F`), L10 (assembly).

### A-7 · The small unquantified words
Individually minor, collectively a pattern the rival should name once and move on from.

| Word | Page | The gap |
|---|---|---|
| "restricted to assets with **sufficient** market data" | 31 | Coverage universe boundary, unquantified |
| "**small** jurisdictions, e.g. Panama → USA" | 6, 31 | No size criterion for reassigning a country |
| "Eligible exchanges … were **defined by BFRE research**" | 37 | No criteria at all; the flowchart's first gate |
| "**persistently** poor model performance over **many** periods" | 38 | The escalation trigger — the thing that decides whether a broken model gets fixed |
| daily currency returns bounded ±8%, weekly ±20% | 30 | Truncation bounds asserted; `notes/` records no justification on the page |
| exposures capped at ±3 | 39 | A hard nonlinear clip, no stated basis |

**ATTACK.** "Page 38 is the important one. The escalation trigger for a failing model is
'persistently poor performance over many periods'. That is the sentence that decides whether anyone
does anything, and it contains no number."
**DEFENCE.** p.38 is a *surveillance* description, and surveillance escalation is deliberately
judgement-led in every model-risk framework — a hard trip-wire produces either alarm fatigue or
silence, and the paper puts the judgement where it belongs, with the model research team, inside a
process that logs exceptions **monthly** against a **95% confidence interval** on a rolling
**12-month** bias statistic and reports to clients **quarterly**. Those *are* numbers. And the tail
test on the same page is fully specified and externally anchored: 99% 1-day VaR, 252-day window,
"consistent with current UCITS guidelines … and follows the approach in Kupiec (1995)". So the page
that supposedly has no numbers has four, plus a regulatory reference.
**GM note.** That last defence is genuinely strong and the player must be able to make it. The Kupiec
citation is the paper's proof that it justifies parameters **when it has an external standard to point
at** — which sharpens the attack everywhere else (see §5.5).

---

## 5.3 CLASS B — ASYMMETRIES STATED BUT NEVER EXPLAINED

*These are the items where the paper does two different things to two similar objects, says so, and
does not say why. They are cheap to raise and hard to dismiss.*

### B-1 · Four frequencies for one horizon ⚑ strongest in class
**CLAIM (all PAPER).**

| Stage | Frequency | Page |
|---|---|---|
| Style and industry factors are **selected** | **monthly** cross-sectional regressions | p.8 ("Monthly local asset returns"), p.11, fn 11 p.14, p.30 |
| Factor returns are **estimated** | **daily** (country + regional models); **weekly** (World model) | p.24 |
| `F` is **built** | **weekly** — WKL, 104 weeks, 26-week half-life, from a **daily** history | p.27 |
| Risk is **forecast** | **1-month** horizon | p.30 |

**WHY WEAK.** A factor is admitted to the model on evidence at one frequency, estimated at a second,
aggregated at a third, and used to forecast at a fourth. The paper never argues that a factor which
explains monthly cross-sections is the right factor for daily estimation, and never gives a reason for
the World model's weekly estimation (`notes/` records this explicitly for p.24).
**ATTACK.** "Reversal is chosen because it explains **monthly** cross-sectional returns. It is then
estimated **daily**, and its variance goes into a matrix built on **weekly** data with a 26-week
half-life, to forecast **one month**. Which of those four frequencies is the model about? And why does
the World model estimate weekly when every regional model estimates daily — same assets, same factors,
different frequency, no reason given."
**DEFENCE.** The frequencies are not arbitrary; each is chosen for the job it does, and p.30 states the
organising principle: the **forecast horizon is 1 month**, and it "is reflected in different aspects
of the model construction" — selection is done monthly *because* the horizon is monthly, which is the
attack's own point running the other way. Estimation is daily because factor returns need enough
observations to estimate a covariance matrix at all; a monthly `F` would need decades. Weekly
aggregation for the World model is the standard response to **asynchronous trading** — a global
universe spans time zones, and daily returns across Tokyo, London and New York are not contemporaneous.
The paper is not silent about asynchronicity: p.27 names it as something PRT lets users control for,
and the serial-correlation correction (Newey–West, [26]) exists precisely to reconcile daily
estimation with a monthly horizon — p.30 says risk estimates are computed at a 1-month horizon
"taking into account **daily serial correlations** in factor returns and asset specific returns".
So the frequency ladder is not a mess; it is a documented chain with an explicit reconciliation step.
**COMEBACK.** "The asynchronicity argument for the World model is a good one — and it is *mine*, not
yours. Page 24 gives no reason. Write it down."
**GM note.** This is the best item in Class B because the defence is excellent *and* the specific gap
(p.24) survives it intact. Ideal boss-round material.
**Callback:** L7 (why cross-sectional, and what the choice costs), L8 (`F`).

### B-2 · Historical Sigma — equal-weighted spread of exponentially-weighted residuals
**CLAIM (PAPER, p.42).** Historical Beta comes from an exponentially weighted regression (1.12) with a
52-week half-life over 5 years of weeklies. Historical Sigma is "**An equally-weighted standard
deviation of the residuals in regression (1.12)**."
**WHY WEAK.** The residuals were produced by a fit that deliberately down-weighted old observations;
their spread is then measured as if every observation counted equally. `notes/` records this as "an
explicit inconsistency, unjustified".
**ATTACK.** "You told the regression that a return from four years ago is worth about an eighth of
last week's. Then you measured the scatter around that fit and told it they are worth the same. One of
those two statements is wrong. Which?"
**DEFENCE.** They are answering different questions and the mismatch is deliberate, not accidental.
The *beta* is a forward-looking sensitivity, so recent behaviour should dominate — hence the decay.
The *sigma* is being used as a cross-sectional **descriptor**, a company characteristic that ranks
this company against every other company; a descriptor wants a stable, well-estimated number over the
full available window, because a decayed sigma is a noisier sigma and noisier descriptors produce
unstable exposures — the exact instability the standardisation and the ±3 cap exist to control.
Note also that Historical Sigma never appears alone: it is one of five Volatility substyles (p.40–41),
weighted 0.2–0.4, and Volatility itself is the *most* significant style in NAMR (Figure 1.8, p.15).
The style is robust to any one substyle's weighting convention by construction — which is the paper's
stated reason for using multiple substyles at all (p.10: it "leads a more robust definition").
**COMEBACK.** "Then Beta × Sigma is a product of two numbers estimated under contradictory weighting
assumptions, and it is a substyle in its own right in EMEA, UKIN, JAPN and EMKT (pp.40–41)."
**Callback:** L1 (weights), L8 (half-life).

### B-3 · Two definitions of "one month" in one appendix
**CLAIM (PAPER, p.44).** Footnotes 20 and 21: "One month is measured as **22 working days**" — for
Relative Strength–11M and for Reversal. But (1.19) Proportion of Active Trade Days uses
"T = number of days in the previous 3, 6 or 12 **calendar** months", and (1.24) Share Turnover the
same (p.45).
**WHY WEAK.** Same word, two operationalisations, three pages apart, no remark. And a third convention
sits alongside: Return-to-Turnover (1.20, p.44) and Amihud (1.21, p.45) use "the last **360 days with
non-missing volume**" — neither working days nor calendar months.
**ATTACK.** "Three definitions of a look-back window in two pages of the same appendix, and the
document never notices. That is not a modelling choice, it is an absence of one."
**DEFENCE.** Each convention fits its measurement. A *return* window should be trading days, because
returns only exist on trading days — 22 working days is the right month for momentum and reversal.
An *activity* window must be calendar, because the whole point of Proportion of Active Trade Days is
the ratio of days traded to days available, and you cannot compute that on a window defined by trading.
A *liquidity average* over non-missing volume must skip missing observations or it silently averages
in zeros and mis-ranks thinly-covered names — which matters most in exactly the emerging markets the
model covers. Three conventions because three quantities.
**COMEBACK.** "That is a good answer and it took me ten seconds to construct. It should be a
footnote."

### B-4 · Standard Deviation – 1Y is a different animal from everything around it
**CLAIM (PAPER, p.42).** Historical Beta: **weekly**, **excess** returns, 52-week half-life, 5 years.
Standard Deviation – 1Y: "An exponentially-weighted estimate of the standard deviation of **daily
total returns**", half-life **180 days**, **360 observations**.
**WHY WEAK.** Different frequency, different return definition (total vs excess), different half-life,
different sample — for two substyles inside the **same style** (Volatility), aggregated together at
weights that vary by region (pp.40–41). `notes/` records: "again with no stated rationale".
**ATTACK.** "Volatility in the LATC model is 0.1 beta + 0.1 cumulative range + 0.4 historical sigma +
0.4 standard-deviation-1Y. You are averaging a weekly-excess-return quantity with a daily-total-return
quantity and calling the result one standard deviation of a style. What are the units of that sum?"
**DEFENCE.** The units question answers itself: **every substyle is standardised to mean 0, sd 1
before aggregation** (p.10, p.39). After Huberisation the inputs are pure z-scores, so aggregating
them is aggregating ranks-in-standard-units, not raw quantities — the frequency and return definition
affect *how each substyle orders companies*, which is exactly what you want to differ, because
different measurement conventions capture different aspects of volatility and averaging them is the
robustness argument on p.10. The substyle correlation exhibits (Figures 1.13, 1.15 on pp.19–20) show
this working in the neighbouring styles: correlated-but-not-identical measures, combined.
**COMEBACK.** "Then the weights matter enormously and you never justify a single one of them
(pp.40–41: 'No justification is offered anywhere on pp.40–41 for why particular substyles enter
particular regional models')."
**GM note.** This comeback is where Class B meets Class D. The weight tables are the largest
unjustified parameter block in the document — roughly 250 numbers.

### B-5 · Three descriptors are vendor fields with no formula
**CLAIM (PAPER, pp.50, 53).** Return on Capital Employed: "The latest Return on Capital Employed
provided by Worldscope." Return on Assets: same. Debt-to-Assets (p.53): "The latest Debt-to-Assets
ratio provided by Worldscope."
**WHY WEAK.** Appendix C defines 30 numbered equations to the symbol — and then three descriptors are
outsourced without so much as a definition of what the vendor means. ROCE and ROA carry real weight
(USAM Profitability: ROCE 0.33; EMEA Profitability: ROCE 0.25, ROA 0.25 — pp.40–41).
**ATTACK.** "You define Funds From Operations to the share count and then take Return on Assets on
faith. If Worldscope changes its definition, a style factor in your model changes and nothing in this
document would tell anyone."
**DEFENCE.** Vendor-standard fields are *more* reproducible than a bespoke formula, not less: every
client, every competitor and every analyst uses the same Worldscope field, so the descriptor is
comparable across the industry and immune to BlackRock-specific definitional drift. p.31 documents the
data layer precisely so this is auditable — source, QC procedure and limitation for every input,
including that fundamental price ratios are normalised by Worldscope prices. Re-deriving ROA in-house
would introduce a divergence from the number every user already has on their screen.
**COMEBACK.** "Then say that. One sentence: 'we use the vendor field for comparability'. You wrote
that sentence for the Amihud FX conversion — page 45, 'to ensure comparability across all values' —
so you know how."

### B-6 · Regional variation, asserted throughout, argued nowhere
**CLAIM (PAPER, pp.40–41).** ~250 substyle weights across 11 regional models. Growth uses a
forward-looking analyst measure "in EMEA and NAMR models only" (p.21). JAPN Value is 0.67/0.33 and
omits Cash-Flow-to-Price. WRLD Liquidity splits six ways at 0.17/0.17/0.17/0.16/0.16/0.17. WRLD
Leverage nets Balance Sheet Cash at **−0.5** against Debt-to-Assets at **+0.5**. EMKT's
Emerging/Developed decoupling beta carries **−1.00**.
**WHY WEAK.** `notes/` for p.41: "**No justification is offered anywhere on pp.40–41** for why
particular substyles enter particular regional models." For p.21: "No justification given for why only
those two regions use forward-looking estimates."
**ATTACK.** "Two hundred and fifty numbers, no reasons. And some of them are not rounding choices —
a negative weight inside a style is a design decision. WRLD Leverage is debt minus cash. JAPN Value
drops cash-flow-to-price entirely. EMKT flips the sign of the emerging-markets beta. Each of those is
a claim about how a market works and none is argued."
**DEFENCE.** Three of the four examples explain themselves from the model's own logic and one is
stated. (i) WRLD Leverage as debt-minus-cash is *net* leverage, which is the economically correct
measure and is why the absolute weights still sum to 1. (ii) EMKT's −1.00 on the decoupling beta is
mechanically necessary: the substyle is the beta to (EM minus S&P 500); in a developed-market model a
positive loading identifies developed companies with EM revenue exposure (p.21, the stated purpose,
with Figure 1.16's BHP/Carlsberg/Volkswagen example on p.22), and inside an *emerging-market* model
the same substyle must be flipped to identify EM companies dependent on developed markets — which is
precisely the Developed Market factor the paper defines on p.22 as "analogous to the emerging market
factor definition". (iii) Analyst estimates in EMEA and NAMR only is a data-coverage constraint: I/B/E/S
FY1/FY2 sales coverage is deep in North America and Europe and thin elsewhere, and p.31's Limitations
column flags coverage gaps as a live issue with roll-forward logic applied to stale estimates. (iv)
Regional variation is the paper's *thesis*, stated on p.3: style and industry factors "vary somewhat
by region reflecting local variation in the importance of different factors."
**COMEBACK.** "You just gave me four reasons. The document gives none. And (iii) is your inference,
not a printed statement — I checked."
**GM note.** Correct: (i)–(iii) are **INFER**. Only (iv) is PAPER. Do not let the player assert them
as the paper's arguments.

---

## 5.4 CLASS C — EVIDENCE RESTING ON A SINGLE DATE OR A SINGLE ANCHOR MONTH

| # | Claim | Evidence actually offered | Page |
|---|---|---|---|
| C-1 | The market factor dominates in a stressed market | **one trading day** — 8 Aug 2011, Fig 1.1 | 5 |
| C-2 | Country factors dominate on a calm day | **one trading day** — 16 Aug 2011, Fig 1.2 | 6 |
| C-3 | Style exposure correlations — the model's only published look at style-column overlap *(that framing is **INFER**; p.11 presents the figure without tying it to the p.32 VIF discussion)* | **one date** — Dec 2013, Fig 1.3 | 11 |
| C-4 | EMEA's earnings and dividend yields are "highly correlated" | **one matrix** — Fig 1.15, Mar 1996–Dec 2010 | 20 |
| C-5 | Style exposures persist through time | **one anchor month** — Dec 2013 vs the prior 24, Fig 1.11 | 17 |
| C-6 | The emerging-market factor is interpretable | **ten hand-picked companies, one month** — Sept 2013, Fig 1.16 | 22 |
| C-7 | Oil exposure lands where economics says it should | **one date** — Dec 2013, Fig 1.17 | 23 |
| C-8 | The model produces useful, interpretable reports | **one sample portfolio** — Fig 1.18 | 35 |
| C-9 | Industry schemas are appropriately granular | **one snapshot** — asset counts and caps "as of December 2013" | 57–63 |

### C-1/C-2 · The two-day evidence base
**CLAIM (PAPER, p.5).** On 8 Aug 2011 the largest contribution to return is the market factor, which
"captures the average (negative) return across stocks on this day"; the magnitude is uniform across
19 country indices because all are fully invested and so carry unit market exposure. **(PAPER, p.6):**
on 16 Aug 2011 the market contribution "is no longer the largest source of return, reflecting a
comparatively benign trading day", and large index returns are attributed to the **country** factor,
clearest for DNK and POL.
**WHY WEAK.** The entire "the decomposition responds to the regime" argument rests on two trading days
eight days apart in one region. And **neither figure prints a single data label** — `notes/` records
the bar heights as `[APPROX, read off gridlines only]` and refuses to firm them up.
**ATTACK.** "Your case that the block structure means something is two Mondays in August 2011.
Not a distribution, not an average across regimes, not a count of how often the market block leads —
two days, chosen after the fact, in one region, with no numbers printed on either chart. I cannot even
check the magnitudes you are describing."
**DEFENCE — and this one is strong.** These figures are not evidence *for* the model; they are
**illustrations of what the output looks like**, and the claim they illustrate does not need a large
sample because it is a mechanical consequence of the specification, not an empirical finding. p.4
states that all equity assets carry **unit** exposure to the market factor. Given that, a day on
which everything falls together *must* load on the market factor — the uniformity of the bars is the
specification made visible, which is exactly what p.5's text says ("magnitude uniform across indices
because all are fully invested"). Choosing two adjacent days with opposite character is a *better*
rhetorical design than an average, because an average would hide the thing being shown: that the
attribution changes when the regime changes rather than always reporting the same story. The claims
that *do* require statistical support — accuracy of the forecasts — are supported elsewhere: bias
statistics over the full 1996–2013 history, on an "exhaustive set" of portfolios (pp.32–33).
**COMEBACK — and this one lands.** "Then do not place them in the section headed **Model Structure**
between the market-factor and country-factor specifications, where a reader takes them as evidence.
And the tests you point me to for the real evidence are the ones you did not publish (§G-3)."
**Callback:** L10 (what each block of `X f` contributes), L11 (reading a risk report).

### C-4 · "Highly correlated" against printed correlations of 0.28–0.50
**CLAIM (PAPER, p.20).** Earnings yield and dividend yield are separate factors in every model
**except EMEA**, where they "were found to be highly correlated over the research history and so were
combined into a single factor, referred to as yield." The evidence offered is Figure 1.15.
**WHY WEAK.** Figure 1.15's printed cells: Earnings-to-Price vs Normalised E-to-P **0.85** — but those
are two *earnings* substyles. Dividend Yield's correlations to the three earnings substyles are
**0.50, 0.28 and 0.48**. So the exhibit cited to justify merging dividend yield into earnings yield
shows dividend yield to be the *least* correlated element in the matrix.
**ATTACK.** "You merged two factors because they were 'highly correlated' and printed the correlation
matrix on the same page. Dividend yield's highest correlation to any earnings substyle is 0.50. The
0.85 in that matrix is between two earnings measures — it is not evidence for the merge, it is
evidence that your earnings substyles are redundant with each other."
**DEFENCE.** The merge decision is about the **factor returns**, not the exposure correlations —
whether two *factors* fight over the same return is a question about `f`, and Figure 1.15 shows
exposures. The exposure matrix is offered as context, not proof. And the operative evidence is the one
the whole selection procedure uses: the marginal significance of the second factor once the first is
in the model ((1.3)–(1.6)) — a factor that adds nothing marginally is merged, and merging is the
*conservative* response to collinearity, strictly better than leaving two unstable columns to fight
(p.32's stated failure mode). Note the paper does not merge them anywhere else — this is a
region-specific, evidence-driven exception, which is the opposite of a blanket assumption.
**COMEBACK.** "Then the sentence should say which evidence. You cited a figure that does not support
the sentence it is attached to, and this is the one place in the document where I can check."
**GM note.** Genuinely the paper's weakest single evidential move — a citation that undercuts its own
sentence, checkable in one page-turn. Excellent boss-round bait because the defence requires the
player to know the difference between exposure correlation (Figure 1.3, 1.13, 1.15) and factor-return
correlation (Table 1.2's market-correlation column). That distinction is exactly LEVEL_ANCHORS §0's
"two structural facts". A player who confuses them fails.

### C-5/C-6 · Anchored snapshots
**CLAIM (PAPER, p.17).** Figure 1.11 plots "the cross-sectional exposure correlations of each style in
**December 2013** against its previous values for every month in the previous two years".
**(PAPER, p.22):** Figure 1.16 gives emerging-market exposures for **ten** headline EMEA companies in
**September 2013**.
**WHY WEAK.** Both are one anchor point. Persistence measured from a single month cannot show whether
persistence itself varies — the interesting question is whether momentum exposures are less persistent
in crises, and this design cannot answer it. The ten companies in Figure 1.16 are selected, and the
paper says so ("headline companies"). Additionally `[UNREADABLE]`: the mapping of individual traces to
legend entries in Figure 1.11 cannot be resolved at scan resolution — so *at the table the GM must
never say "the reversal line"*, only "one series collapses to ≈0 by lag 1, which a one-month-return
exposure would do."
**ATTACK.** "Persistence anchored on one month, from a two-year window that contains no crisis.
Interpretability demonstrated on ten names you chose."
**DEFENCE.** Figure 1.16 is explicitly a *reading aid*, introduced with "To aid with interpretation,
it is useful to consider which stocks are highly exposed" — a face-validity check, and face validity
is a legitimate criterion the paper lists first among its four on p.4 ("**Interpretability**: factors
should be easily interpretable, and have a strong economic rationale"). A ten-name table is the right
size for that job. Figure 1.11's claim is also modest and structural: reversal and momentum exposures
turn over faster than everything else, which follows from their definitions — a one-month return
exposure *must* decorrelate in one month. Nothing statistical is being claimed.
**COMEBACK.** "Face validity is a criterion you can pass with any factor, given ten well-chosen names.
That is what makes it a weak criterion, and it is the first of your four."

---

## 5.5 CLASS D — WINDOWS AND HALF-LIVES WITH NO SENSITIVITY ANALYSIS

**The class-level attack, delivered once.**
> "Here are two dozen window lengths, half-lives and lag counts from this document. Exactly **one** of
> them is justified — the 99%/252-day VaR test on page 38, which cites UCITS guidelines and Kupiec
> (1995). Every other one is asserted. And nowhere in sixty-five pages is there a single sensitivity
> analysis: not one 'we also tried 52 weeks and here is what changed'. The document proves it knows
> how to justify a parameter, on page 38, and then does not do it anywhere else."

| Quantity | Parameter | Page | Justified? |
|---|---|---|---|
| Factor covariance, default WKL | 104 weeks, 26-week half-life | 27 | No — "primarily driven by the target horizon" |
| Factor return history start | March 1996 | 27 | No |
| Specific risk, daily | 125-day half-life, 375 obs, Newey–West lag 10 | 28 (Table 1.3) | No |
| Specific risk, weekly (WRLD, EMKT) | 26-week half-life, 104 weeks, NW lag 2 | 28 | No |
| Historical Beta (1.12) | 5y weekly, 52-week half-life | 42 | No |
| Standard Deviation – 1Y | daily **total** returns, 180-day half-life, 360 obs | 42 | No |
| Cumulative Range | 12 months | 42 | No |
| Macro-economic betas (1.49) | inherits (1.12)'s window — **no half-life printed on the page** | 52 | No |
| Emerging-market / oil betas | 5y weekly, 52-week emphasis | 21, 22 | No |
| Momentum (1.17) | 11 months, 1-month lag, 22 working days | 44 | **Partly** — the lag is justified ("to exclude the reversal effect", p.17) |
| Reversal (1.18) | previous month = 22 working days | 44 | No |
| Active Trade Days (1.19) | 3 / 6 / 12 calendar months | 44 | No |
| Return-to-Turnover (1.20), Amihud (1.21) | last **360 days with non-missing volume** | 44, 45 | No |
| Growth of Trading Volume (1.22) | 12 & 36 months | 45 | No |
| Share Turnover (1.24) | 3 / 6 / 12 calendar months | 45 | No |
| Price Pressure (1.25) | 1 & 3 months | 45 | No |
| Assets / Sales averaging (1.14, 1.16, 1.36, 1.40) | 5 years | 43, 49 | No |
| Normalised EPS regression (1.31) | 5 years of EPS | 47 | No |
| Return on Equity (1.43) | 2-year average book equity | 50 | No |
| Cash Flow to Liabilities (1.45) | 5-year average FFO | 50 | No |
| Variation in Capital Structure (1.42) | 4 years of 1-year changes | 50 | No |
| Equity Dilution (1.53) | 1 year | 53 | No |
| Bias statistic | rolling 12 months, 95% CI | 38 | No |
| **VaR back-test** | **99%, 252 days** | **38** | **YES — UCITS + Kupiec (1995), fn 18** |

**THE DEFENCE (a BlackRock author's best case, and it is not weak).**

1. **The horizon does the work, and it is stated.** p.30: "The forecast horizon of the model is
   **1-month**. This is reflected in different aspects of the model construction" — and then lists
   three. p.27 makes the same link for `F`: "The value of the half-life is primarily driven by the
   target horizon." So the half-lives are not free; they are downstream of a single published choice.
2. **The trade-off is stated in words, twice, correctly.** p.27: forecasts "should be responsive to
   changes in the market environment whilst not being unduly noisy so as to render them unstable and
   unusable"; p.28 repeats it for specific risk — "balancing the conflicting demands of having
   accurate and responsive forecasts against having stable ones." That is the exact objective function
   a sensitivity analysis would be optimising, named in the document.
3. **The user can run the sensitivity themselves.** p.27: PRT "allows users to change the half-life of
   the exponential decay, control for serial correlations and asynchronicity in the factor return
   series, and apply different assumptions to factor volatilities and factor correlations." A shipped
   parameter is a **default**, not a constraint, and the paper says so.
4. **Some windows are conventions, and convention has value.** 5-year fundamental averaging, 12-month
   cumulative range, 3/6/12-month liquidity windows and 11-months-plus-a-lag momentum are the
   literature's standard constructions — Jegadeesh–Titman [14] for momentum, Amihud [19] for the
   illiquidity ratio. Re-justifying a standard from scratch in a client document adds pages, not
   information.
5. **Robustness is designed in rather than argued.** Every style is a weighted blend of substyles with
   *deliberately different* windows (Volatility carries a 52-week-half-life beta, a 12-month range and
   a 180-day-half-life standard deviation, pp.40–42), and p.10 gives the reason: combining substyles
   "leads a more robust definition of style factor returns and typically increases the explanatory
   power of the factor." Window sensitivity is diversified away at the style level by construction.

**THE COMEBACK — and it is the one the player must land.**
> "Point 5 is a claim about robustness, which is exactly the kind of claim a sensitivity analysis
> tests, and you did not run one — or did not publish it. Point 3 is worse than it looks: if I can
> change the half-life, I need to know what changes when I do, and you have not told me. And point 1
> does not survive arithmetic — the horizon is **one month**, and the default `F` half-life is
> **26 weeks**, six times the horizon, on a 104-week window. 'Driven by the target horizon' does not
> explain a memory six times longer than the thing being forecast. Give me one chart."

**GM note (INFER, flag it).** The 26-week-vs-1-month observation is the GM's arithmetic on two printed
numbers (p.27, p.30), not a statement the paper makes. It is legitimate and sharp; it must be spoken
as *"put those two pages together and…"*.
**Callback:** L8 (half-life), L0 (a diagnostic that reports cancellation instead of size — same
species of failure as a parameter reported without its sensitivity).

---

## 5.6 CLASS E — STORIES NO RESULT COULD FALSIFY

### E-1 · Overreaction at one month, underreaction at eleven ⚑ flagship of the class
**CLAIM (PAPER, p.16).** Reversal is justified by "market investors **overreacting** to stock
information in the near-term."
**CLAIM (PAPER, p.17).** Momentum is justified by "market investors systematically **underreacting** to
newly available company information, and failing to adjust their expectations in the medium-term."
**CONSTRUCTION (PAPER, p.17, p.44).** Momentum is measured over "the previous **11 months with a one
month lag** to exclude the reversal effect"; Reversal (1.18) is exactly that excluded month.
**WHY WEAK.** Two opposite psychological claims about the same investors and the same information,
made three pages apart, and the two measurements are constructed to be **disjoint** — so no dataset
can put them in competition. Any pattern of short-term reversal and medium-term drift is consistent
with the pair; no pattern is inconsistent with it. It explains everything, which is the definition of
explaining nothing.
**ATTACK.** "Page 16: investors overreact. Page 17: investors underreact. Same investors, same
information, adjacent horizons, and you have built the windows so they never overlap — which means
there is no observation that could ever embarrass either story. What result would make you withdraw
one of these sentences?"
**DEFENCE — and this is a good one, the player must be able to give it.**
1. **It is one story, not two.** The claim is not that investors both over- and under-react to the
   same thing; it is that the market's response to news has a **shape in time**: an initial overshoot
   that partially retraces within a month, followed by a slow drift as information is fully
   incorporated. That is a single coherent dynamic and it is the standard reading of the literature
   the paper cites — Jegadeesh [11], Jacobs and Levy [12], Subrahmanyam [13] on the short horizon;
   Jegadeesh and Titman [14] on the medium horizon.
2. **The non-overlap is a discipline, not an evasion.** If the two windows overlapped, the same return
   would be counted twice and the two factors would fight over it — the exact instability p.32 warns
   about. The one-month lag is a **collinearity control**, and the paper says so in as many words.
3. **BFRE does not need the story to be true.** It is a **risk** model. Factors earn their place on
   the four criteria on p.4 and on the statistical evidence, not on their narrative. Figure 1.8 (p.15)
   ranks Momentum second and Reversal fourth among NAMR styles by proportion of significant
   t-statistics `[APPROX — pixel-measured; the *ranking* is what to cite, not the heights]`, and
   Table 1.2 (p.10) prints their factor returns: Reversal **−5.1%** annualised at **3.2%** volatility
   (Sharpe **−1.59**), Momentum **+5.4%** at **3.8%** (Sharpe **1.43**) — the two largest Sharpe
   magnitudes among NAMR styles — with first-order autocorrelations of **0.17** and **0.22**. Those
   are printed numbers over 1996–2013, and they are what the inclusion decision rests on.
4. **The behavioural sentence is doing interpretive work for a PM, not inferential work for the
   model.** p.4's first criterion is Interpretability. A portfolio manager needs a sentence that says
   what the factor *is*.
**COMEBACK.** "Then delete the sentence, or mark it as colour. You have put it in a section that reads
as justification, in a document clients use to explain their risk. And point 3 is the same defence
you would have available for the **Random Substyle** in Table 1.4 if it happened to score well — which
brings me to what the placebo scored, a number you never print."
**GM note.** That comeback is the hinge of the whole level: it links the unfalsifiable-story class to
the multiple-testing class. If the player finds that link unprompted, promote.
**Callback:** L4 (momentum's lag as an engineered non-collision), L6 (Sharpe and t-statistics).

### E-2 · The conceded proxy
**CLAIM (PAPER, p.23).** "A regression analysis between asset returns and changes in the level of the
VIX index (**as a first approximation** to the 'risk-on/risk-off' paradigm) captures this sensitivity."
**WHY WEAK.** The paper concedes the proxy is approximate and never defends it, never tests an
alternative, and never says what a better approximation would be. The style being proxied — investor
risk appetite — is not directly observable, so no result could show the proxy failed *as a proxy*;
it could only show the VIX beta was insignificant, which is a different claim.
**ATTACK.** "'First approximation' to what? You cannot validate a proxy against an unobservable. And
Sentiment is the weakest style in your own Figure 1.8 — the second-shortest bar, visibly below the
10% line you print on page 14 — and you shipped it anyway."
**DEFENCE.** The concession is a *virtue*: the paper flags the limitation rather than dressing the VIX
up as the thing itself. And the descriptor is not validated as a proxy for a mood — it is validated
the same way every other substyle is, by whether the beta explains cross-sectional return commonality
in the recursive procedure. The VIX is the most liquid, longest-history, most widely-understood measure
of market-implied risk appetite available at daily frequency across the whole 1996–2013 sample; any
alternative would be less available, less standard, or both. And Sentiment is a **regime** factor,
which a full-sample proportion-of-significance statistic systematically understates: a factor that
matters intensely in a handful of stressed quarters and not at all otherwise will score low on a
metric that counts months.
**COMEBACK.** "That last argument is unfalsifiable too — 'it matters in the periods where it matters'.
Show me the sub-sample. Page 8 says you computed five-year sub-samples."

### E-3 · The rest of the class
| Story | Page | The attack in one line | The defence in one line |
|---|---|---|---|
| Oil moves on "wars, or even **the fear of wars**" | 22 | Unfalsifiable by construction — an absent war can be a feared war | It is scene-setting; the exposure is an estimated beta (p.22), and Fig 1.17 shows Energy and Materials loading positive as economics predicts |
| Peer review imposes "**forward-looking views** of industry behaviour"; Alcohol/Tobacco/Casinos split "due to the increasing investor focus on **ESG**" | 8 | A discretionary override of a statistical procedure, with no criterion and no record of what was overridden | Statistical selection on past data cannot anticipate a structural change in investor behaviour; the paper is *transparent* that judgement enters and where, which is better than hiding it in the model |
| "Throughout the whole selection process, **qualitative judgement** and statistical analysis are combined" | 12 | The escape hatch: any factor can be kept or dropped and the sentence covers it | An honest description of how every real model is built; the alternative is to pretend otherwise |
| Size: "Large companies are typically more immune to difficult economic conditions" | 12 | An economic story with no test reported in the paper | The *test* is elsewhere and is real: p.13 prints a **0.67** correlation between the NAMR size factor and the (negated) Fama-French SMB series "over the entire history", plotted as Fig 1.7 on p.14; and Fig 1.10 (p.16) shows the decile evidence |
| Liquidity: liquid stocks "react more quickly to general economic news flow" | 19 | Consistent with the 0.69 market correlation, and so is every other story | The paper does not rest on the story: it gives five substyles, their correlation matrix (Fig 1.13, p.19) and a stated reason for multiple measures — "there is no single, widely-accepted metric" (p.18) |
| Exposure cloning justified by arbitrage convergence, "**Assuming that no barriers exist**" | 39 | The assumption carries the argument, and barriers demonstrably exist (that is why Royal Dutch Shell needs its own bullet on p.30) | The convergence argument is correct over the stated horizon ("longer horizons"), and the paper carves out the case where it fails — different share classes "are in no way fungible" and stay empirical (p.28) |

### E-4 · The choice pushed to the user
**CLAIM (PAPER, pp.28–29).** Two methodologies for the specific covariance matrix — **structural**
(related listings get cloned specific risk, correlation forced to 1) and **empirical** (estimated
separately). "The model user is free to choose the approach that best applies to their investment
process and horizon": structural for active managers who see related listings as fungible over "many
months"; empirical for index trackers where day-to-day differences matter.
**WHY WEAK.** No evidence is offered that either approach forecasts better for either user type. The
recommendation is derived from a story about investor horizon, and the story is untestable as stated —
whichever a user picks, the paper's advice is unfalsified.
**ATTACK.** "You have two models of the same quantity and you are letting the client pick by
self-description. Which one produced better bias statistics for a long-only European equity fund? You
ran the tests — page 33 says the suite included 'a significant number of genuine portfolios'."
**DEFENCE — strong.** This is not indecision; it is the correct answer to a question that genuinely has
two answers. The two approaches encode two different **definitions of what a specific return is**, and
which definition is right depends on the user's horizon, which the model cannot know. For a manager
holding an ADR and its ordinary line as one economic position over months, treating their specific
returns as independent would materially *understate* concentration risk — the paper states the
direction of the error explicitly (p.28: ignoring the correlation "would lead to under (or over)
prediction of specific risk in a long-only (long-short) portfolio context"). For an index tracker, the
day-to-day basis between the two lines *is* the tracking risk, and forcing correlation to 1 would
declare it zero. A single default would be wrong for one of them by construction. And the paper does
not leave everything to taste: different share classes stay empirical **under both approaches**,
because they "confer different rights to the owner and are in no way fungible."
**COMEBACK.** "Agreed on the design. Not on the silence: you know the horizon at which they cross
over, or you could. Publish it."
**Callback:** L9 (`Δ`'s diagonal assumption and where it fails).

---

## 5.7 CLASS F — SIGNIFICANCE THRESHOLDS AND THE MULTIPLE-TESTING CHARGE

### F-1 · The bar, and the factors that ship below it
**THE THRESHOLDS, all PAPER:**

| Threshold | Where it appears | Exact words |
|---|---|---|
| \|t\| > 2 | p.8 | "We consider an absolute t-statistics in excess of 2 as statistically significant" |
| 10% of months | p.14 | "A value in excess of 10% indicates a statistically significant style effect, and **would be considered for inclusion** in the models" |
| 10% of months | p.16 | "the 10% threshold **used to determine whether styles are eligible for inclusion** in the model" |
| 10%–15% | p.12 | recursion stops "until the largest proportion of t-statistics from the second step univariate regression is no larger than **10% - 15%**" |
| 10% | p.32 | "**The majority of factors** are significant more than 10% of time over the research history, with most well in excess of this threshold" |

**WHY WEAK.**
- The same bar is described three ways — "would be considered for inclusion" (a screen), "used to
  determine whether styles are eligible" (a rule), and a **band**, 10–15%, for the stopping rule. A
  band is not a criterion; it is a range within which the analyst decides.
- p.32 says "**the majority** of factors" clear 10%. That word concedes that some shipped factors do
  not, and the paper never says which or why.
- Figure 1.8 (p.15) shows which. Against the printed 10% line, **Sentiment** is the second-shortest bar
  and **Earnings Yield** the shortest — both visibly below it `[APPROX: pixel-measured at ≈7% and
  ≈4–5%; the paper prints no data labels, so cite the *position relative to the line*, never the
  numbers]`. Both are NAMR style factors in Table 1.2 (p.10).
- The bar first appears on p.14, mid-discussion of Volatility — i.e. it is introduced after the
  results it is used to judge already exist in the document.
- **INFER, flag it:** at |t| > 2 you would expect roughly 5% of monthly cross-sections to clear the
  bar by chance alone. A 10% requirement is therefore about twice the null rate. The paper never
  computes a null rate, so this is the rival's arithmetic, not the paper's.

**ATTACK.** "Your stated inclusion rule is on page 14: above 10% of months, a style is significant and
would be considered. Your own Figure 1.8 on page 15 shows two NAMR styles below that line, and both of
them are in your NAMR model in Table 1.2 on page 10. Either the rule is not the rule, or the model
does not follow it. And page 32 quietly says so — '**the majority** of factors'."
**DEFENCE — genuinely good, and it needs three parts.**
1. **The 10% is a screen, and the paper says so.** p.14's verb is "**would be considered** for
   inclusion", not "shall be included". p.12 is explicit that qualitative judgement and statistics are
   combined. p.4 lists **four** criteria — Interpretability, Explanatory Power, Consistency, Efficacy
   — of which the proportion statistic addresses two.
2. **A low marginal significance rate is evidence of redundancy, not irrelevance — and the procedure
   is built to produce exactly that.** Styles are added **recursively**, each candidate judged on the
   *residuals of the model built so far* ((1.3)–(1.6), pp.10–12). Earnings Yield enters late, after
   Value; Figure 1.15 (p.20) shows Earnings-to-Price and Normalised Earnings-to-Price at **0.85**, and
   Figure 1.3 (p.11) shows Earnings Yield–Profitability at **0.64** and Earnings Yield–Value at
   **0.40**. A factor that overlaps that heavily with included factors *must* score low marginally —
   that is the procedure working, not failing. Dropping it would not remove the risk; it would push
   valuation risk into other factors' loadings and into `Δ`.
3. **The stopping rule is a band because it governs a search, not a verdict.** 10–15% is where you
   stop looking for the *next* factor; it is not a pass mark for a specific factor.
**COMEBACK.** "Then say which factors were retained below the bar and on which of the four criteria.
You have twelve NAMR styles and one page — it is a sentence. As written, the four criteria are jointly
unfalsifiable: any factor that fails one can be kept on another, and none of the four carries a number."
**Callback:** L6 (the whole level — big coefficient, small t, argue both sides).

### F-2 · 200+ candidates, no correction, and a placebo whose score is never reported ⚑ THE BIG ONE
**THE FACTS, all PAPER:**
- p.10: "for i = 1, 2, …, N (where **N ≥ 200** is the number of candidate substyles) we run the
  following two-step regression".
- p.55: the printed inventory "is a **subset of the full list of 200+**", with each horizon variant
  counted separately — relative strength alone counts as 5.
- p.56, Table 1.4: the printed inventory contains **18 styles and 108 substyles** *(both counts derived
  by the transcriber from the printed rows — the page prints no totals)*, and it contains a style
  called **"Random"** whose single substyle is **"Random Substyle"**.
- p.8: significance is |t| > 2.
- p.55: `notes/` records — "no information about the selection procedure … and **no multiple-testing
  correction is mentioned** despite 200+ candidates being tested."
- p.8: LASSO [7], LARS [8], Group Lasso/Group LARS [9], Ridge and Bayesian priors [6] are **named and
  declined**, on the stated ground that they "are purely statistical in nature and rely heavily on
  historical data."

**WHY WEAK.** Two hundred candidates tested at a fixed two-sigma bar, with no family-wise correction,
no false-discovery control, and no reported null benchmark — while a **placebo descriptor sits in the
candidate set**. The authors clearly understood the problem: you do not put a Random Substyle in an
inventory unless you are worried about exactly this. Having built the control, the paper never reports
what it scored. **(Graduate-level. Say so.)**

**ATTACK.**
> "You tested more than two hundred candidates at |t| > 2 with no correction for having tested two
> hundred. You knew that was the risk — you put a **Random Substyle** in the candidate list, which is
> the classic control, and it is printed in your own Table 1.4 on page 56. So there is exactly one
> number that would settle whether your 10%-of-months bar is above chance, and it is the one number
> you did not publish. What did the random substyle score?"

**DEFENCE — the strongest defence in the dossier. All six parts are needed.**
1. **The statistic is not a p-value; it is a persistence rate.** A candidate is not judged on one
   t-statistic. It is judged on the **proportion of monthly cross-sectional t-statistics exceeding 2
   over a 15-year history** (p.8, p.11, footnotes 11 and 12 on pp.14 and 16) — roughly 180 monthly
   tests per candidate. A lucky month cannot carry a candidate; a candidate has to be significant in
   one month in eight, for fifteen years.
2. **The tests are conditional, not parallel.** Each round regresses candidates on the **residuals of
   the model built so far** ((1.3)–(1.6), pp.10–12). This is not 200 independent lottery tickets — a
   candidate that merely re-expresses an accepted factor is structurally prevented from re-entering,
   and each accepted factor shrinks the field for everything after it.
3. **Sub-samples.** p.8: results are summarised over the full sample **and five-year sub-samples**,
   with p.11 adding "special emphasis … in the last five years." A period-specific fluke fails.
4. **The alternatives were considered and declined on the record.** p.8 names LASSO, LARS, Group
   Lasso, Ridge and Bayesian priors, with citations, and states the reason for not using them. That is
   a documented methodological choice by people who knew the literature — not an oversight.
5. **The economic prior does real work.** The candidate set is not 200 random data series; it is drawn
   "from the academic literature and current investment risk practice" (p.10), and the four criteria
   on p.4 lead with Interpretability and economic rationale. A data-mined factor with no story fails
   criterion one regardless of its t-statistics.
6. **The final schema is peer-reviewed** by investment and risk professionals (p.8) — a human check
   against statistical artefacts surviving the screen.

**COMEBACK — and the player must be able to deliver it after that defence, not before.**
> "Not one of those six is a multiple-comparison correction, and you are the ones who named the
> literature that contains them. (1) 180 monthly tests is a bigger family, not a smaller one. (3)
> Three five-year sub-samples is three more chances to pass, not a correction. (4) You cited Tibshirani
> and declined him — fine, but then you owe me the alternative control, and there isn't one. (5) The
> economic prior is a filter you apply *by hand*, which is judgement, which is page 12's escape hatch.
> And all of it collapses to one question you can answer in a single line and did not: **what did the
> Random Substyle score?** If it scored under 10%, print it — it would be the best evidence in the
> document. If you never looked, then the control was decoration."

**GM note.** This is the level's centrepiece. Run it as a full Round E interrogation. The player passes
only if they can deliver **all six defence points before hearing the comeback** and then concede the
comeback's force without abandoning the defence. Abandoning the defence under pressure is a fail; so is
refusing to concede.
**Callback:** L6 (t-statistics), L8 (shrinkage — the paper names it and declines it, which is the whole
point), L0 (a diagnostic that cannot distinguish good from bad).

---

## 5.8 CLASS G — DIAGNOSTICS THAT CANNOT TELL A GOOD MODEL FROM A BAD ONE

*This is the class the level brief singles out, and it is the direct descendant of **Level 0's boss
round**: three desks with identical `Σe = 0` and wildly different models. Make the callback explicit.*

### G-1 · `R²` with no formula, no value, and no null
**CLAIM (PAPER, p.32).** "The *R²* quantifies the proportion of cross-sectional variation in asset
returns explained by the set of common factors in the model. This is a standard measure of any factor
model's overall explanatory power." Printed as italic *R²* inline. **No displayed formula. No value,
anywhere in 65 pages.**
**WHY WEAK.** A cross-sectional `R²` rises mechanically as columns are added, and BFRE adds a lot of
columns — NAMR alone carries **54 industry factors** *(p.57 — count derived by the transcriber from
the printed rows; the page prints no total)* plus countries, currencies, a market and
twelve styles. Without a value, an adjusted value, a per-period distribution, or a comparison against
a randomly-loaded design matrix, the statistic cannot distinguish a model that explains from a model
that interpolates.
**ATTACK.** "You name `R²` as your measure of overall explanatory power and never print one. If you
had, I would still ask what it is being compared against, because with fifty-four industry columns and
a country column and a currency column I can get a respectable cross-sectional `R²` out of noise.
This is Level Zero's problem in a suit: a diagnostic that reports something other than what you care
about."
**DEFENCE.** `R²` is listed as one of **three** estimation diagnostics on p.32, alongside factor-level
t-statistic histories and VIFs, precisely because no single one discriminates — the paper calls them
"several standard diagnostics … appraised during this process". And crucially, **BFRE does not claim
accuracy from `R²`**. In-sample fit is not the model's claim; the model's claim is forecast accuracy,
and the section immediately following (ASSESSMENT OF VOLATILITY FORECASTS, p.32) makes it against
**realised** returns via bias statistics, and p.38 adds a 99%/252-day VaR violation count. Those are
out-of-sample tests. Attacking an in-sample statistic that the paper does not lean on is attacking the
wrong thing.
**COMEBACK.** "It would be attacking the wrong thing if the out-of-sample tests were published.
They are not (G-3). Strike those and `R²` is the only explanatory-power evidence left in the document,
and it is a word."
**Callback:** L0 (boss round — `Σe = 0` for a perfect model and a catastrophic one alike).

### G-2 · The VIF pass mark — see A-2
Same species: a diagnostic reported as an adjective. Worth raising **only in combination** with G-1 and
G-3 — three unnumbered diagnostics is a pattern; one is an oversight.

### G-3 · The tests are real, exhaustive, and unpublished ⚑ RANK 1 ATTACK
**THE CHAIN, all PAPER:**
- p.32: "A well-calibrated model should provide risk forecasts that are stable and accurate… This
  forms the basis of the **bias statistic** used to evaluate the BFRE models. An **exhaustive set** of
  bias statistics was generated and reviewed over the entire research history."
- p.32–33: the test portfolios are listed in full — pure factor portfolios for markets, styles,
  industries, countries and currencies; cap-weighted estimation universes and their industry and
  country carve-outs; cap-weighted large/mid/small terciles; individual stocks; minimum variance
  portfolios; active portfolios; "a significant number of **genuine portfolios**".
- p.33: "More details of the testing are provided by **[27] available on request**."
- p.65: **[27]** = "FMG, *BFRE Model Testing white paper*, Aladdin Model Documentation, **forthcoming**."
- `notes/` for p.33: "**no bias-statistic values, no pass/fail criteria and no summary results are
  printed anywhere in the Model Testing chapter**."
- p.30: "Out-of-sample model back-testing is conducted on a subset of such portfolios as part of the
  **Quarterly Aladdin Risk Model conference calls**" — also unpublished here.

**WHY WEAK.** Every accuracy claim in a sixty-five-page model document is deferred to a companion
document that the bibliography lists as **not yet existing**. "Available on request" and "forthcoming"
are not compatible statements about the same object.
**ATTACK — three sentences, and it is the best three sentences the rival has.**
> "Page 32 tells me an exhaustive set of bias statistics was generated and reviewed. Page 33 sends me
> to reference [27] for the results, 'available on request'. Page 65 lists [27] as **forthcoming**.
> So at the moment this document was published, the evidence for every accuracy claim in it did not
> exist in a form anyone could read — and there is not one bias-statistic value, one pass criterion or
> one back-test result printed in the entire paper."
**DEFENCE — and a player who cannot make this defence has not understood the genre.**
1. **This is client model documentation, not a research paper.** Its job is to specify the model —
   structure, parameters, assumptions, limitations, data lineage — so a user can audit their own risk
   numbers and satisfy their own model-risk function. That job is done thoroughly: two equations for
   the model (1.7, 1.8), the full estimation specification (1.9)–(1.11), Table 1.3's specific-risk
   parameters to the lag, equations (1.12)–(1.55) for every substyle, the complete data-source table on p.31, an explicit
   Assumptions & Limitations section (p.30), and a production/QC flowchart (Figure 1.19, p.37).
2. **Test results and model specification move on different cycles.** The specification changes
   rarely; surveillance is continuous — p.38: exceptions logged **monthly**, bias statistics on a
   rolling 12-month window against a 95% confidence interval, VaR violations over 252 days, and results
   presented to clients **quarterly**. A point-in-time bias statistic printed in a specification
   document is stale the month after it ships, and worse than stale — it invites users to rely on a
   number that has been superseded.
3. **The tests are specified precisely enough to reproduce.** The reader is told the statistic (bias
   statistic on standardised returns), the window (rolling 12 months), the flag (95% CI), the tail test
   (99% 1-day VaR over 252 days) with an external standard (UCITS, Kupiec 1995) and the exact portfolio
   set. A user can run every one of these on their own holdings.
4. **The surveillance is not self-marked.** p.38 benchmarks BFRE against **STORM**, Aladdin's
   independent equity risk model, and p.30 puts out-of-sample back-testing in front of clients
   quarterly. That is external exposure on a recurring cadence, not a one-off self-assessment.
**COMEBACK.** "Points 2 and 3 are good and I accept them. They argue for publishing a **history** of
bias statistics, or a distribution, or a single worst case — not for publishing none. And point 4 is
benchmarking against your own other model. Comparing BFRE to STORM tells me they agree; it does not
tell me either is right."
**GM note.** This is the item to hand a player who is floundering. It requires no statistics at all —
just three page-turns — and it is the strongest attack in the file. It is also the fastest way to show
a player that "rigour" and "unreadable maths" are different things.
**Callback:** L0 (the diagnostic that cannot discriminate), L12 itself.

### G-4 · What the paper *does* show — the concession the player must make
**PAPER, p.16, Figure 1.10.** For each market-cap decile, model residuals were regressed on 0/1 decile
dummies, before and after adding a small-cap factor. Before: deciles 9 and 10 sit above the printed
10% line. After: both fall far below it. `[APPROX — measured heights 10.8%→2.1% and 21.1%→3.4%; the
paper prints no data labels, so cite the *crossing of the printed line*, not the numbers.]`
**WHY THIS MATTERS TO BOTH SIDES.** This is the one place in the document where a diagnostic is shown
**with a visible failure state**: a specific way the model could be wrong, evidence that it was, a fix,
and evidence the fix worked. It is exactly what the rival is demanding everywhere else — which makes it
the defence's best exhibit and the attack's best proof that publishing such a thing was possible.
**DEFENCE USE.** "You asked for a diagnostic that can distinguish a good model from a bad one. Page 16
is one, and we published it, and it shows our model failing before we fixed it."
**ATTACK USE.** "One diagnostic, one factor, one region, ending December 2010, with no printed values.
You proved you can do this. Then you did it once."

### G-5 · Two more, briefly (both partly INFER — flag them)
| Diagnostic | Page | The limitation |
|---|---|---|
| Bias statistic on a **rolling 12-month** window at **95%** | 38 | **INFER:** twelve standardised observations is a small sample for a variance test; a model can be materially mis-calibrated and clear a 95% band routinely. The window and the band are both asserted (see §5.5). |
| "Proportion of significant t-statistics" as the efficacy metric | 8, 14, 15, 32 | **INFER:** it measures how often a factor's return is *detectable*, which is not the same as whether the factor improves a *risk forecast*. p.4's fourth criterion, Efficacy, explicitly asks for the second — improving "forecasts of portfolio beta and portfolio risk" — and no evidence for it is printed anywhere. |

The second is worth raising: the paper sets itself four criteria on p.4 and publishes evidence bearing
on roughly one and a half of them.

---

## 5.9 CLASS H — INTERNAL INCONSISTENCIES (free ammunition, low glory)

*Use these as **corroboration**, never as an opening. Each is cheap to verify and none of them changes
a risk number. Their value is cumulative: they establish that the document was not carefully read
before it shipped, which softens the ground for Classes F and G.*

### H-1 · The model in production is not the model that was tested
**PAPER, p.31:** industry classification is "Current: **TRBC** … Historical\*\*\*: **GICS**", where
`***` = "**before February 2018**". **PAPER, p.32:** "All models were tested extensively using a
history of data spanning several different market environments from **1996 to 2013**."
**ATTACK.** "Your tested history ends in 2013. Your industry classification changed in February 2018,
with no reason given. Industry factors are defined *from* that schema (p.7), so the industry block of
the model in production today is built on a taxonomy that did not exist during any test you describe —
and the factor return history spans two different definitions of what an industry is."
**DEFENCE.** Vendor schema changes are exogenous and unavoidable; a model that refused to follow its
data vendor would be worse, not better. p.31 documents the change, its date, and the override logic
applied around it ("overrides applied to separate composite assets into multi-sector sub-industry, and
expand coverage"), plus cloning logic to force consistency across listings within an issuer. The
alternative — freezing an obsolete taxonomy — would degrade every industry factor going forward.
**COMEBACK.** "Documenting a change is not testing it. One sentence on the effect on the factor return
series would close this."
**GM note.** The "not the model that was tested" framing is **INFER** built on two printed dates.
Say so.

### H-2 · The prose and the tables disagree about Quality
**PAPER, p.21:** "only equity dilution was found to have significant cross-sectional explanatory power
in the **Asia Pacific ex Japan (APXJ)** model." **PAPER, p.41 (Table D):** Quality / Equity Dilution
carries weight **1.00 in APXJ *and* in EMKT**.
**ATTACK.** "Page 21 says the quality factor survives in one model. Page 41 loads it in two."
**DEFENCE.** Thin. The honest answer is that p.21's sentence is about where the *research* found
significance and p.41 reflects the *shipped* models, which may have diverged — but the paper never says
that, so this is a straightforward internal inconsistency.
**GM note.** Rare case where the defence should concede. A player who tries to defend this one is
learning the wrong lesson; a good author says "that's an error, thank you."

### H-3 · Prose says one thing, formula says another
| Where | Prose | Formula | Page |
|---|---|---|---|
| (1.38) Change in Assets | "the difference … over the previous **two years**" | `ln A_t − ln A_{t−1}` — a **one-year** change | 49 |
| (1.22) Growth of Trading Volume | slope divided by "the average **Total Assets** over the last T months" | denominator is `(1/T)·Σ V_{i,s}` — average **traded volume** | 45 |
| (1.22)/(1.23) | — | regression runs `s = t−T … t` (**T+1** observations) while the normaliser averages over **T** | 45 |
| (1.54) Foreign Sales | "`S_{i,t}` the **total assets** of company i" | `S` is total **sales** | 54 |
| (1.54) vs (1.55) | — | `FS` denotes foreign **sales** in one and foreign **assets** in the other | 54 |
| (1.37) vs (1.41) | "where **β_i** is estimated" | matching line above (1.41) reads **β̂_i** — same quantity, two notations | 49 |

**ATTACK.** "Six defects in an appendix that is supposed to be the reproducible part of the document.
If I implement (1.38) from your prose I get a two-year change; from your formula I get a one-year
change. Those are different exposures and therefore different risk numbers."
**DEFENCE.** In each case the **formula is the more specific statement** and any implementer follows
the formula; the prose is a gloss. Appendix C's job is to be unambiguous where it matters, and the
equations are internally consistent even where the surrounding sentences are loose.
**COMEBACK.** "Then the gloss is wrong and should be corrected. And (1.22) is the awkward one — there
the *prose* names a quantity the formula does not contain at all, so 'follow the formula' means the
sentence is simply false."

### H-4 · The where-list that lost its Style row
**PAPER, p.26.** The symbol list for (1.9) has **five** rows, and `X_Mkt f_Mkt` is printed against the
description "**Style** Exposures and Factor Returns". There is no Market row and no Style row.
Re-verified at 4× in the audit — this is the source's error, not the transcription's.
**PAPER, p.26, (1.10).** Both summation indices are printed `j`; the second summand is subscripted `k`.
Also the source's error, re-verified at 6×.
**ATTACK.** "Equation (1.9) is the equation that produces every factor return in the model. Its
symbol list omits the style block and mislabels the market block. Equation (1.10) — the pair of
restrictions without which (1.9) has infinitely many solutions — has a summation index that does not
match its summand."
**DEFENCE.** Both are typesetting defects with zero ambiguity: (1.9) itself is printed correctly with
all four blocks and matching sub-indices (verified at 5×), and (1.10)'s intent is unmistakable from its
own where-list, which defines `w_CCty,k` and `f_CCty,k` with the `k` index. No implementer is misled.
**GM note.** True, and this is why H-4 is a **corroborating** item, not a leading one.

### H-5 · The rest, at a glance
| Defect | Page | Class |
|---|---|---|
| `s ≤ t` (the no-look-ahead line) printed under (1.28) and (1.32) only, though (1.29)–(1.31) mix a dated numerator with an undated price denominator; same on p.53 where it appears under (1.50) but not (1.52) | 47, 53 | Convention stated once, left implicit |
| "Share Turnover" in Appendix C vs "Stock Turnover" in the weight tables — never reconciled | 40–41, 45 | Naming |
| `V/N` enters (1.20) un-logged and (1.24) logged — the same quantity as two substyles | 44, 45 | Construction |
| Balance Sheet Cash filed under **Leverage**, no rationale | 53 | Taxonomy |
| Mid-Cap's rank symbol `r_{i,t}` is the same glyph the paper uses for returns; the page says it is "defined below" and **no definition appears** | 51 | Undefined symbol |
| The dependent variable of (1.49) is printed `lê_{i,s}` and **never defined** — described in prose only as "the residuals in regression (1.12)" `[AMBIGUOUS: meaning, not shape]` | 52 | Undefined symbol |
| "effective number of assets" used as an eligibility criterion, never defined | 8 | Undefined quantity |
| EMEA EarnYield weights sum to **0.75** unless Dividend Yield's 0.25 is counted inside it; the table does not say | 40 | Table defect |
| CAND Foreign Sensitivity: exactly **one** `0.5` glyph between the Foreign Sales and Foreign Assets rows. `[UNREADABLE: row attribution.]` **Do not assume 0.5/0.5** — taken literally the column sums to 0.5 | 40 | Table defect + unreadable |
| The Industry **Name** column is displaced by one row against the **Code** column for rows 6–12, producing the printed pairing "FINBANKS = Health Care, 10 assets, \$363bn" | 62 | Printed table error. `[UNREADABLE: the caption and region are cropped out of the photograph — never name the region]` |
| Non-trading returns are replaced by a compounded **market** return (1.26)/(1.27); `notes/` records "no justification, back-test, or sensitivity analysis for this proxying rule is given" | 46 | Unjustified imputation |
| Fill-Miss imputes a missing substyle by regressing it on log market cap plus market, country and industry factors — so an exposure can be manufactured entirely from a stock's size, sector and country, then enters the regression as data | 39 | Grey zone, see §7 |
| Two known defects shipped with "This will be addressed in a **forthcoming model release**" — the 1–2 day vendor coverage lag, and the multi-share-class specific-correlation gap | 30 | Honest, but shipped |

---

# 6. CHEAP SHOTS — DO NOT ATTACK THESE

*The point of this section. A rival who leads with one of these has told the room they are reading for
ammunition rather than for the model, and everything they say afterwards is discounted. Make the player
name at least three of these unprompted before the level is passed.*

| # | The cheap shot | Why it loses | The one-line kill |
|---|---|---|---|
| **CS-1** | "√-market-cap weighting is arbitrary." | It is the **best-justified choice in the paper**. p.25 gives three arguments: the compromise between equal and cap weighting; the named failure mode of each extreme (equal ⇒ "a poor fit for mega-cap and large-cap securities"; cap ⇒ "poorer forecasts for mid-cap and small-cap"); and heteroskedasticity — "higher residual (specific) risk is typically correlated with smaller market capitalisation assets". **Footnote 14 even names the textbook alternative** (1/residual variance) and says it gives similar results in practice. | "Page 25 answers that in a paragraph and footnote 14 answers the follow-up." |
| **CS-2** | "The market factor isn't the S&P 500 — beta 0.99, R² 91% is a poor fit." | p.4 pre-empts this exactly: the fit "is not expected to be a perfect fit as the NAMR market covers a broader universe of assets, **including Canadian stocks**, and uses √-cap weights, which assigns greater weight to the mid-cap and small-cap segments". It also warns separately that market factor exposure "should not be confused with its market beta". | "The paper says why on the same page, twice." |
| **CS-3** | "(1.8) calls `Δ` diagonal but page 27 says it isn't — a contradiction." | Not hidden and not a contradiction: p.27 states plainly that the specific covariance matrix is "a vector of asset specific risk forecasts and a **sparsely populated** unit diagonal matrix containing non-zero, off-diagonal specific return correlations", and p.28 gives a whole subsection to it with examples, the two methodologies, and the **direction of the error** if it were ignored. Attack the **scope** instead (correlations only *within* a company; across companies "assumed to be zero **in-line with standard modelling practice**", p.28) — that is a real, narrow, defensible criticism. | "They devote a subsection to it. What you want to attack is the across-company zero." |
| **CS-4** | "Currency factor returns are 'calculated' not 'estimated' — sloppy wording." | Footnote 8 on p.6 exists *precisely* to flag the distinction: "Note the use of the term 'calculated' here, as opposed to 'estimated' — **no uncertainty is involved in their construction**." That is unusual care, not sloppiness. | "That footnote is the paper being careful. You just cited its best sentence against it." |
| **CS-5** | Typos: "Reginal", "stadardisation", "Agriculturl", "EQYEQEXP", "FNNREAL", "dailybasis", "– empirical–", "preferences shares", "an absolute t-statistics", "can used". | Proofreading, not modelling. A rival who opens here has nothing. **Exception:** the p.62 row displacement (H-5) is a *content* defect, not a typo, and the missing Style row on p.26 is worth one sentence as corroboration. | Say nothing. Raising it is the mistake. |
| **CS-6** | "No eigen-decomposition, no principal components, no statistical factors." | The paper never claims them — zero occurrences in 65 pages — and it **argues for the fundamental approach on p.2**: returns-only models "can quickly become misleading if a company undergoes changes in its operating activities, or is subject to corporate actions, or experiences changes to its capital structure", which a fundamental model reflects "immediately". BFRE is also positioned as "entirely complementary" to STORM, the returns-only model, not as a replacement. | "They chose a fundamental model on page 2 and gave the reason. Attacking the absence of a method they never claimed is a category error." |
| **CS-7** | "The regression is not uniquely identified — three intercepts!" | The paper **finds this itself** on p.26, names it ("there are an infinite number of possible solutions"), explains the cause (market, industry and country all carry unit exposure), fixes it with (1.10), and states the consequence honestly — "the industry and country factors are **net of** the market factor return", with a worked UK example. | "They diagnose it, fix it and warn you about the fix's side-effect, all on page 26. What is left to attack?" |
| **CS-8** | "Factors are selected on monthly data but estimated daily — incoherent." | Half a cheap shot. p.30 states the organising principle explicitly — the 1-month forecast horizon drives monthly selection. The *real* version of this attack is B-1, which is about **four** frequencies and about the **unexplained** weekly World-model choice on p.24. Deliver B-1, not this. | "Page 30 explains monthly selection. Ask about the World model instead." |
| **CS-9** | "Huberisation is unjustified." | Overstated: p.39 gives two reasons versus Winsorisation — it "mitigates issues of **clustering** and **destroyed rank information** in the tails". No *empirical* evidence is offered, which is the honest version of the complaint. | "They give two reasons. Say 'no evidence is offered for them', which is true, instead of 'unjustified', which isn't." |
| **CS-10** | "I can't read the figure values." | That is the scan. The admissible version is below, immediately after this table: **the paper prints no data labels on any chart**. | "Attack the document, not the photocopy." |
| **CS-11** | "Country factor returns are negative when the country was up — that's broken." | p.26 states and explains it: the restrictions make industry and country factors net of the market, "which impacts their interpretation", with the exact worked example ("UK assets are also up but by less than the average return over the region, then the UK factor return will be negative"). | "That's the documented consequence of the identifying restriction, not a bug." |
| **CS-12** | "±3 exposure cap is arbitrary." | Grey. It *is* a number without a stated basis (p.39), but the case for capping is obvious and universal. Worth half a sentence inside the Class-A list, never on its own. | — |

### CS-10, done properly · the one figure complaint that IS admissible
**THE FACT, derived by the GM from `notes/` — say that it is derived, then use it.** The paper has
**twenty** numbered figures, 1.1 to 1.20. Of those:

| Group | Figures | Do they print values? |
|---|---|---|
| Correlation / exposure matrices | **1.3** (p.11), **1.13** (p.19), **1.15** (p.20), **1.16** (p.22) | **Yes** — every cell, all 144 of Fig 1.3 included |
| Process flowcharts (no data) | 1.19, 1.20 (p.37) | n/a |
| **Bar, line and heat charts** | **1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.14, 1.17, 1.18** | **No — not one data label, anywhere** |

`notes/` puts it flatly for p.23: "the source **prints no digits at all** for this figure"; and for
p.35: "**No individual bar values are printed anywhere in the figure**."
**ATTACK.** "Fourteen charts, not one data label between them. The 10% inclusion threshold is a dashed
line on page 16 and a sentence on page 14 — and I cannot read a single bar against it. Every
quantitative argument you make from a chart is unauditable by design."
**DEFENCE.** House style for a document read by portfolio managers, where shape and rank are the
message and a labelled bar chart with twelve categories is unreadable. The exhibits where **values**
are the message — the four correlation matrices — do print every cell, all 144 of Figure 1.3 included.
The choice tracks the content.
**COMEBACK.** "Then Figure 1.8 has values as its message. It is your published inclusion evidence and
it is twelve unlabelled bars against a threshold you state in prose three pages earlier."

---

# 7. GREY ZONE — defensible either way

*Raise these as questions, not accusations. A rival who frames a grey-zone item as a scandal loses the
same credibility as one who leads with a cheap shot.*

| Item | Page | The question, correctly framed | The paper's answer |
|---|---|---|---|
| **Two-pass estimation** — the first pass excludes lower-development markets, which therefore "have **no impact** on the factor returns estimated in the first-pass" | 25, 26 | "Frontier and Watch-market assets are priced by factors fitted without them, then given their own factors on the residuals (1.11), which are never re-estimated. What does that cost them?" | Stated rationale: those markets have "considerably poorer" data quality and coverage, and the estimation universe deliberately excludes stale-priced illiquid assets and "'tiny' companies whose economic relevance is questionable". Letting bad data set global factor returns is the worse error. |
| **Fill-Miss** | 39 | "A missing exposure is imputed from log market cap plus market, country and industry factors — so a manufactured exposure enters the regression indistinguishable from a measured one. How many, and does anything flag them?" | It is disclosed, it is targeted ("typically employed to handle listings of new companies"), and the alternative — dropping the asset — loses coverage exactly where a client most needs a number. |
| **Style exposure cloning / dual-listed fundamentals** | 30, 39 | "Royal Dutch Shell's two lines get identical fundamental exposures by construction. When does the convergence assumption fail?" | Justified by an arbitrage-convergence argument over "longer horizons"; the paper carves out the case where it demonstrably fails — different share classes "confer different rights … and are in no way fungible" and stay empirical (p.28). |
| **Price Pressure's counterfactual return** | 45, 46 | "(1.27) replaces a non-traded asset's return with a compounded market return. What does that do to the liquidity exposure of a stock that stopped trading for a week?" | The paper gives the rule and no justification. `notes/` for p.46: "No justification, back-test, or sensitivity analysis for this proxying rule is given." Genuinely thin — but low-salience, since Price Pressure loads only in EMKT (p.41). |
| **The 26-week half-life against a 1-month horizon** | 27, 30 | "Six times the forecast horizon. Why?" | The paper's answer is the responsiveness-vs-stability trade-off (p.27) and the fact that PRT lets a user shorten it. Reasonable — but see §5.5's comeback. **The arithmetic is INFER.** |
| **Across-company specific correlations assumed zero** | 28, 30 | "Two suppliers to the same collapsing customer. Where does that risk live?" | Assumed zero "**in-line with standard modelling practice**" — appeal to convention, stated as such. This is the *correct* version of CS-3 and is worth raising: it is Level 9's failure mode, printed. |

---

# 8. THE CONCESSIONS — what a credible rival must grant

A player who cannot say what the paper does **well** has not read it. Require at least four of these
before awarding the level.

| # | Concession | Page |
|---|---|---|
| 1 | The identification problem is found, named, fixed and its side-effect disclosed, all on one page | 26 |
| 2 | The regression weighting scheme is argued from three directions, with the alternative named and dismissed | 25, fn 14 |
| 3 | An explicit **Assumptions & Limitations** section that names two shipped defects and says a fix is coming | 30 |
| 4 | A complete data-lineage table — source, QC and limitation for every input, with the vendor and the switch date | 31 |
| 5 | One published before/after diagnostic with a visible failure state (the decile test) | 16 |
| 6 | A **placebo** carried in the candidate inventory — the mark of a team that understood the multiple-testing risk | 56 |
| 7 | The rejected alternatives are named with citations, not ignored (LASSO, LARS, group lasso, Ridge, Bayesian) | 8 |
| 8 | The direction of the error is given where an assumption fails: ignoring specific-return correlation causes "under (or over) prediction of specific risk in a long-only (long-short) portfolio context" | 28 |
| 9 | One parameter justified against an external standard: 99%/252-day VaR, UCITS + Kupiec (1995) | 38 |
| 10 | Full reproducible construction — equations (1.12)–(1.55) for the substyles, per-region weights, five named transformations in stated order | 39–54 |
| 11 | Surveillance benchmarked against an **independent in-house model** (STORM) and reported to clients quarterly | 38, 30 |
| 12 | A footnote whose only purpose is to stop the reader confusing "calculated" with "estimated" | 6, fn 8 |

---

# 9. BOSS-ROUND SCRIPTS

Run as Round E (INTERROGATION). Play the CRO with 30 years and no patience. Three set-pieces, in
ascending difficulty. Do not go easy; if the player hand-waves, dock bps and say why.

### Script 1 — WARM-UP: "Find me three, and rank them."
Give the player five minutes and the paper. Accept any three from §5. **Then ask the ranking question,
which is the real test:** *"Which one do you take into the meeting, and what do you leave out?"*

- **Pass:** picks G-3 or F-2, and can say why the others are weaker — usually because they are
  interpretive (5.1), bounded (A-3), or cosmetic (H).
- **Fail:** picks the standardisation asymmetry as the lead. It is real, but it is rank 9. Ask them what
  it changes about a risk number; the invariance argument (§5.1 DEFENCE 3) should stop them.
- **Instant fail:** leads with √-cap weighting or a typo. Go to §6 and start again.

### Script 2 — THE FLIP: "Now you wrote it."
Player plays the BlackRock author. Attack them with **G-3** (the deferred testing), which is the
strongest attack in the file, and require all four defence points. Then, without warning, make them
attack their own answer.

- **Pass:** delivers the genre argument (client documentation vs research paper), the cycle argument
  (specification vs surveillance), the reproducibility argument (statistic, window, band, portfolio set
  all specified), and the STORM benchmarking — **and then** concedes that none of it argues for
  publishing *zero* values.
- **Fail:** defends by asserting BlackRock's competence, or by saying the results are confidential
  without noticing that "available on request" and "forthcoming" cannot both be true of [27].

### Script 3 — THE FULL EXCHANGE: the multiple-testing charge
The centrepiece. Run F-2 as a three-move conversation and **do not let the player skip a move**.

| Move | Who | What must happen |
|---|---|---|
| 1 | Player attacks | 200+ candidates (p.10, p.55), \|t\| > 2 (p.8), no correction (p.55), **and the Random Substyle** (p.56). All four, or the attack is incomplete. |
| 2 | GM defends as author | Deliver all six defence points from F-2. Do not soften them. |
| 3 | Player comes back | Must land: none of the six is a correction; sub-samples are more chances, not fewer; the placebo's score is the missing number. |

- **Promote to Model Owner** if the player, at move 3, *also* concedes that the persistence statistic
  and the conditional procedure genuinely do reduce the problem — i.e. attacks the gap without
  pretending the defence was empty.
- **Hold** if the player wins move 3 by volume — repeating "you tested 200 things" louder. That is
  Tier 3, not Tier 4.
- **Bonus bps** if the player, unprompted, connects the placebo to E-1's comeback: *"'it explains
  covariance' is the same defence the Random Substyle would get."*

### Vocabulary-under-fire prompts for this level (Round F)
Each must be translated into plain English and then used correctly in a **new** sentence.
1. "The VIFs were reviewed and found to be well within suitable thresholds." *(p.32)*
2. "This metric serves as a good proxy for the persistence of individual factor effects." *(p.8)*
3. "The weighting function places more weight on the time-series forecast as more data becomes
   available." *(p.28)*
4. "We impose the thin country/industry correction by adding a Bayesian prior." *(p.36)*
5. "An exhaustive set of bias statistics was generated and reviewed over the entire research history."
   *(p.32)*

For each, the follow-up question is the same and it is the level in miniature: **"What result would
have made that sentence false?"**

---

# 10. SCORING RUBRIC

| Tier | Attack side | Defence side |
|---|---|---|
| 1 Recognise | Can say "some numbers aren't justified" | Can say "it's a BlackRock model" |
| 2 Compute | Lists real weaknesses with page numbers | Repeats the paper's stated reasons |
| 3 Derive | Explains *why* each weakness matters mechanically | Reconstructs an argument the paper implies but does not print |
| **4 Defend** | **Ranks the weaknesses, leads with the strongest, and avoids every §6 cheap shot** | **Survives the strongest attack (G-3, F-2) with the full defence, then concedes what genuinely cannot be defended** |
| 5 Rebuild | Proposes the specific experiment that would settle each open question — the sensitivity chart, the placebo's score, the published bias-statistic distribution | Would have written the missing paragraph, in the paper's own register |

**Level 12 is passed at Tier 4 on both sides.** Not one side. A player who can only attack fails the
level; a player who can only defend has not audited anything.

**Automatic fail conditions**
- Quotes a pixel-measured figure value as a printed number (Rule 1).
- Attacks the scan instead of the paper (Rule 2).
- Leads with a §6 cheap shot.
- Cites the portfolio-beta formula on p.4 as BlackRock's (it is a **reader's handwritten margin
  annotation**).
- Uses "tracking error" or "eigenvalue" as if the paper contained them. It contains neither.

---

# 11. NEVER CITE — the fabrication traps

The audit of `notes/` caught one invented cross-reference. These are the invitations to repeat it.

**Absent from the paper's own text, all 65 pages:**
eigenvalue · eigenvector · principal component · "least squares" · normal equations · `Σx·e = 0` ·
any derivation of a regression coefficient · standard error (as a formula or an explained concept) ·
degrees of freedom · an `R²` **formula** · marginal contribution to risk · any risk-decomposition
mathematics · "tracking error" · "orthogonal" · Frisch–Waugh–Lovell · shrinkage **of `F`** · any
statement of how many factors a model has in total · any observation-to-factor ratio.

**Also absent from the paper's own text — these are *our* words for *its* problems.** Never put them
in BlackRock's mouth; they appear in `notes/` only as the transcriber's commentary:
"sensitivity analysis" · "multiple testing" · "data mining" · "placebo" · "falsifiable" ·
"post hoc" · "look-ahead bias". The paper's nearest printed equivalents are the `s ≤ t` lag lines
(p.47) for look-ahead, the "Random Substyle" row (p.56) for the placebo, and nothing at all for the
other five.

**Present, but never to be firmed up:**

| Item | Page | The caveat that must travel with it |
|---|---|---|
| Portfolio-beta formula `β = (Xₚᵀ F X_b)/(X_bᵀ F X_b)` | 4 | **A reader's pen annotation in the margin.** Never BlackRock's. |
| Figures 1.1 / 1.2 bar heights | 5, 6 | `[APPROX, read off gridlines only; no data labels printed]` |
| Figure 1.8 style percentages (incl. Sentiment ≈7%, Earnings Yield ≈4–5%) | 15 | `[APPROX, pixel-measured]` — cite the position **relative to the printed 10% line** |
| Figure 1.10 decile percentages | 16 | `[APPROX, ±0.5pp]` — cite the crossing of the line, not the numbers |
| Figure 1.5's top y-axis label | 12 | `[UNREADABLE: 45.0% vs 45.5% cannot be settled from the ink alone]` |
| Figure 1.9 cell **signs** | 15 | `[UNREADABLE]` — the greyscale ramp is **diverging**, so darkness encodes magnitude, not sign |
| Figure 1.11 trace → legend mapping | 17 | `[UNREADABLE]` — never say "the reversal line"; say "one series collapses to ≈0 by lag 1" |
| Figure 1.17 sector bars | 23 | The source **prints no digits at all** for this figure |
| Figure 1.18 bar and dot magnitudes | 35 | **Every one is a pixel measurement, ±10%.** Tick labels are reliable; bar values are not |
| Figure 1.18 "Act Sec 1%" | 35 | `[INFERRED]` — the glyph reads 1 or 2; 1% chosen only because the six slices then sum to 100 |
| Figure 1.18 banner digits | 35 | 2.99% (**2.89 not fully excluded**), 15.62% (**15.67 not fully excluded**). 14.98% and 1.02 are clean |
| CAND Foreign Sensitivity weight | 40 | `[UNREADABLE]` — one `0.5` glyph between two rows. **Do not assume 0.5/0.5** |
| Tables on pp.58, 62, 63 | 58, 62, 63 | Captions cropped out of the photographs. **Never name the region and never cite "Table 1.12" or "Table 1.13"** |
| The `lê_{i,s}` symbol in (1.49) | 52 | Legible at 14×; **meaning ambiguous** — the paper never defines it |
| Mid-Cap rank symbol `r_{i,t}` in (1.48) | 51 | Same glyph as returns; page says "defined below" and **no definition appears** |
| Small-Cap rank direction | 51 | The page **never states whether rank 1 is largest or smallest** |
| Table 1.4's counts (18 styles, 108 substyles) | 56 | **Derived by the transcriber from the printed rows — the page prints no totals** |
| Table 1.2's row set | 10 | 13 rows: Market + **12** styles. Small-Cap, Leverage, Quality, Foreign Sensitivity, Oil and Emerging Market are **not** in it |

---

## APPENDIX — the one-page crib

**Five attacks, in order, for a player with two minutes:**
1. Every accuracy claim is deferred to reference [27], which p.65 lists as **forthcoming** (pp.32, 33, 65).
2. 200+ candidates at |t| > 2 with no correction — and a **Random Substyle** in the inventory whose
   score is never reported (pp.10, 55, 56).
3. Not one diagnostic **value** is printed: VIFs are "well within suitable thresholds", `R²` has no
   number and no formula (p.32).
4. Two dozen windows and half-lives, exactly one justified (the VaR test, UCITS + Kupiec, p.38), and
   **no sensitivity analysis anywhere**.
5. The country-versus-market story rests on **two trading days** in August 2011, on charts with no data
   labels (pp.5, 6).

**Five defences, in order, for a player under fire:**
1. Genre: this is a model **specification** for client audit, not a research paper — and it specifies
   the model completely — (1.7)–(1.11), Table 1.3, and (1.12)–(1.55) across pp.39–54.
2. Test results live on a different cycle from the specification: monthly exception logging, 95% band,
   quarterly client back-testing calls (p.38, p.30) — and the tests are named precisely enough to
   reproduce.
3. Selection is a **persistence rate over ~180 monthly cross-sections**, run **conditionally** on
   residuals, checked on five-year sub-samples — not 200 one-shot p-values (pp.8, 10–12).
4. Parameters are downstream of one published choice — the **1-month forecast horizon** (p.30) — and
   the user can change them in PRT (p.27).
5. Where the paper had an external standard, it used it (Kupiec, p.38). Where an assumption fails, it
   names the **direction** of the error (p.28). Where a factor failed a test, it published the failure
   and the fix (Figure 1.10, p.16).

**The sentence that ends the level, either way:**
> *"The paper's problem is not that its choices are wrong. It is that almost none of them are shown to
> be right — and page 16 and page 38 prove the authors knew exactly how to show it."*
