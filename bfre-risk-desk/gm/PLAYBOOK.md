# THE RISK DESK — GAME-MASTER PLAYBOOK

The operational manual. `prompt/RISK_DESK.md` is the law; this file is what you *do* at the table
while the player is waiting for you to say something.

**Companion files, and what each is for.** Do not duplicate their work mid-round — jump.

| File | Use it when |
|---|---|
| `gm/LEVEL_ANCHORS.md` | You need the page/equation to land a level on. Anchor tables, per level. |
| `gm/VOCAB.md` | You are running Round F, or need the unlock level and the tell for a term. |
| `gm/ANALOGIES.md` | An explanation failed and you need a *different domain*, not more words. |
| `gm/CRITIQUE.md` | Level 12, attack and defence, ranked. |
| `datasets/level*.md` | The exact arithmetic. Every number verified by `tools/verify_*.py`. |
| `notes/` | The paper. The only source. Nothing is cited here that was not read there. |

---

## 0. SOURCE DISCIPLINE — read once, obey always

Every page reference in this file was checked in `notes/` before it was written down. `notes/` is a
transcription of a **scan**; its markers travel with the fact.

| Tag | Meaning at the table |
|---|---|
| **PAPER** | The paper says this. Quote or close paraphrase. |
| **INFER** | Follows from what the paper says. Say *"this follows from"* — never *"the paper says"*. |
| **GAP** | The paper does not contain this. Say so out loud; do not manufacture a page. |
| `[APPROX]` | Pixel-measured off a chart with no printed data labels. Say *"measured off the chart, roughly"* every time. |
| `[UNREADABLE]` / `[INFERRED]` / `[TENTATIVE]` | The scan could not settle it. Never resolve these. |

Four standing traps, all of which have already caught someone:

1. The portfolio-beta formula on p.4 is a **reader's handwritten margin annotation**, not BlackRock's
   text. Never attribute it.
2. Every bar height and dot position in Figure 1.18 (p.35) is a pixel measurement, ±10%. The **axis
   tick labels** and the **pie percentages** are read directly and are reliable — except `Act Sec 1%`,
   which is `[INFERRED]` from the six slices summing to 100.
3. `notes/` contains the transcriber's commentary as well as the paper's words. "Orthogonal" (p.52),
   "coefficient of determination" (p.32), "placebo" (p.56) and every "(my count)" total are **the
   transcriber's**, not the paper's.
4. **p.27 prints two different histories for `F` and never reconciles them.** "The BFRE factor
   covariance matrices use a history of **daily** factor return series starting in **March 1996**" and
   "The default … is WKL (weekly long-term), which uses **104 weeks** of factor returns with a
   half-life of 26 weeks" are both on that page. A GM who says "`F` is built from eighteen years of
   data" has said something false about the shipped default and has thrown away the L8 boss round —
   the point is that they *had* 900-odd weeks and chose 104 of them, down-weighted. Make the player
   notice the discard before you explain it.

---

## 1. JARGON UNLOCK — which level buys which word

Terms appear freely *in this file*. They must not leave your mouth at the table before the level in
column 2. Full treatment and the failure tells are in `gm/VOCAB.md` §3.

| Term used in this playbook | Unlocked at | Status in the paper |
|---|---|---|
| residual, the miss | L0 | PAPER — `u` in (1.7), p.24 |
| specific return | L0 (name) / L9 (machinery) | PAPER — p.24 |
| factor return, `f` | L1 | PAPER — (1.7), p.24 |
| exposure | L1 (name) / L5 (BFRE's meaning) | PAPER — defined outright, p.39 |
| regression weight | L1 | PAPER — √market cap, p.25 |
| orthogonal / neutral | L2, deepens L4 | PAPER says "**neutral**" (p.5). The word *orthogonal* never appears |
| design matrix | L3 | GAP — the paper says "factor exposures", `X` |
| multicollinearity, VIF | L4 — **graduate** | PAPER — p.32 + fn 16 |
| Frisch–Waugh–Lovell | L4 — **graduate** | GAP — the mechanism is on pp.7, 10, 12, **25–26** and 52; the name never appears |
| intercept | L5 | PAPER — p.26, "three intercept terms" |
| z-score, standardised | L5 | PAPER — p.10 ("similar to forming a z-score"), p.39 ("i.e. z-scores") |
| centering / centred | L5 | **GAP — the word never appears.** The mechanism does: p.10 and p.39 standardise to a √-cap-weighted mean of **zero**. Say "the paper removes the level by construction", not "the paper centres" |
| t-statistic, significance | L6 | PAPER — \|t\| > 2, p.8 |
| standard error, degrees of freedom | L6 | **GAP — neither phrase appears anywhere in 65 pages** |
| cross-sectional regression | L7 | PAPER — p.24 ("a series of cross-sectional regressions"); also p.3 ("in cross-section"), p.7 (the two-step regressions (1.1)/(1.2)), p.14 fn 11 and p.16 fn 12 and p.30 ("monthly cross-sectional regressions"). **Not** p.32 — that page says cross-sectional *variation* |
| factor covariance matrix, `F` | L8 | PAPER — (1.8), p.24; p.27 |
| half-life, exponential decay | L8 | PAPER — p.27, Table 1.3 p.28 |
| eigenvalue / eigen-decomposition | L8 — **graduate** | **GAP — zero occurrences in the paper** |
| shrinkage | L8 boss — **graduate** | Word appears only in a bibliography title ([7], p.64). Mechanism p.36 |
| specific risk, `Δ` | L9 | PAPER — (1.8) p.24; p.27; p.28 |
| asset covariance matrix, `Σ` | L10 | PAPER — (1.8), p.24 |
| active risk | L11 | PAPER — p.34, p.35 banner |
| tracking error | L10 as outside vocabulary | GAP — the paper's word is **Active Risk** |
| marginal contribution to risk | L11 | **GAP — no formula, no term, anywhere** |
| bias statistic | L12 | PAPER — p.32, p.38 |
| in-sample / out-of-sample | L12 | "Out-of-sample" once (p.30); "in-sample" never |

**Letter warning, fire it at L10.** The game's rules write `V = XFXᵀ + D`. The paper writes
`Σ = X F Xᵀ + Δ` (p.24). Say so explicitly or the player will think they have found an error.

---

## 2. DIFFICULTY HONESTY — say these out loud, at these moments

Rule §2: never soften genuinely hard material. Frustration is then correctly calibrated.

| Material | Level | Say, verbatim or close |
|---|---|---|
| Multicollinearity | L4 | "This is graduate econometrics. The 2×2 you are about to build will be genuinely clear; the general theory is a course." |
| Frisch–Waugh–Lovell | L4 | "Graduate-level. You are getting the mechanism without the theorem, which is the right trade. The paper leans on that mechanism five separate times — (1.1)/(1.2) p.7, (1.3)/(1.4) p.10, (1.5)/(1.6) p.12, **(1.9)/(1.11) pp.25–26** and (1.49) p.52 — and never names it." **The fifth is the one that matters**: (1.9)/(1.11) is the shipped estimation, where the second pass fits Extended factors to the first pass's residual `u`. The other four are selection machinery |
| Standard error from scratch | L6 | "Most textbooks skip this derivation. We are not skipping it — it is Victory Condition 3. And note: this paper never derives it either." |
| Eigen-decomposition | L8 | "Graduate-level, and the paper never uses it. We are borrowing a lens to see why a covariance matrix can be broken." |
| Shrinkage / bias–variance | L8 boss | "Graduate-level. The paper's version (p.36, a Bayesian prior on thin factor returns) is not the textbook's version, and we will do both." |
| Euler decomposition of risk | L11 | "The theorem that makes contributions sum to the total is beyond scope. The nudge argument gets you there without it." |

---

## 3. THE SIX ROUND TYPES — rotation

### 3.1 The rotation rules

0. **The story comes before the round type, always.** Rules §8: *"Any new concept opens with a single
   self-contained analogy containing no mathematics. Finish the story completely, then map it line by
   line onto the model."* The rotation below governs the **task**; ONE STORY FIRST governs the
   **concept**, and it wins. Run the four beats in `gm/ANALOGIES.md` §0, finish the story, map it,
   and end it on the page/factor/equation it changes (Rules §8, ALWAYS RETURN TO BFRE). *Then* open
   the task with A or C. A GM who opens a brand-new concept with Round C has opened it with units —
   which is mathematics — and has skipped a hard rule.
1. **Never open a level with arithmetic.** Once the story has landed, every level opens with **A**
   (predict-then-reveal) or **C** (build-the-shape). The player commits before they compute, or they
   are not learning, they are following.
2. **Never two of the same type back to back** inside a level.
3. **Every level closes with a boss round, and the boss round is played as E.** For every level but
   one the boss round *is* an E interrogation. **Level 2 is the exception the rules name:** Rules §5 makes
   L2's boss round a *sabotage* — "you corrupt one residual; the player must find it using only the
   balance condition". Run it as **B carrying E on its back**: the player finds the corruption, and
   then the CRO attacks the find with the three objections in §8.2. Passing requires both — the
   location and size, *and* all three objections held. There is no other way out of a level.
4. **D (teach-back) at least once per level.** It is the cheapest instrument you own: it detects a
   memorised explanation in about ninety seconds.
5. **F (vocabulary) is fired, never scheduled.** Drop it mid-task as an aside. Maximum two per level.
   Announcing it ("vocabulary question:") converts the game into a quiz and forfeits its purpose.
6. **B (sabotage) requires an invariant.** Do not run it on a level that has not yet produced
   something that should be exactly zero, or should add up. Levels 2, 3, 5, 9, 10 are the natural
   homes; 0, 6, 8 have weaker versions; 1, 4, 7, 11, 12 have none worth running.
7. **If two consecutive rounds were both computation, you have lost the rotation.** Recover with D or A.

### 3.2 The default spine of a level

```
 story  →  A or C  →  the computation  →  B or D  →  (F fired mid-task)  →  E boss
no maths    commit     turn the handle    audit or explain     the word       survive
```

The story is beat zero and it is not optional (§3.1 r.0). At **L2** the last box reads **B+E**, not E.

### 3.3 Which round suits which material

| Shape of the material | Round | Why this one |
|---|---|---|
| A formula about to be introduced, with clear units | **C** | Units alone pin the shape. "You need a number in percent; you have a sum in percent and a sum of squared pure numbers." |
| A direction claim — *what happens if I …* | **A** | Forces a reason on the table before the answer exists. A lucky guess earns nothing. |
| An invariant: a balance that must be zero, a decomposition that must add up, an impossible sign | **B** | Teaches the checks working quants run. Structural discovery beats recomputation. |
| Something the player believes they understand | **D** | The awkward question the character would ask finds the seam. |
| A judgement call, an assumption, a threshold, a weakness | **E** | Assumptions cannot be computed; they can only be defended. |
| A word, *after* the mechanism exists | **F** | Victory Condition 2 is decided here, not on definitions. |
| A number in the paper the player has not traced | **A** then **E** | Predict it, then be asked where it came from. |

### 3.4 Round type by level — the recommended mix

| L | Opens with | Core | Audit / explain | F ammunition (fire mid-task) | Boss |
|---|---|---|---|---|---|
| 0 | A — guess a single `b` before anything is taught | compute `Σxr/Σx²` | D — explain to a non-quant why sign is useless | "residual", "specific return" | E |
| 1 | C — build the shape from units | the nudge derivation | D — teach the nudge | "factor return", "exposure", "regression weight" | E |
| 2 | A — will `Σe` be zero? | verify `Σx·e = 0` | — (the sabotage *is* the boss) | "orthogonal"/"neutral" (p.5) | **B+E** (§3.1 r.3) |
| 3 | C — how many conditions for two columns? | 2×2 in fractions | B — corrupt one of two conditions | "design matrix" (outside word) | E |
| 4 | A — predict both coefficients before fitting | the collided fit | D — explain to a PM why the split moved | "multicollinearity" (p.32), "VIF" | E |
| 5 | A — shift every `x` by 100, predict | the pivot | B — corrupt the centring step (the paper's word at the table is **standardised**, not "centred" — §1) | "intercept", "z-score", "standardised" | E |
| 6 | C — what must a "is this real?" number look like? | build the SE | D — teach degrees of freedom | "t-statistic", "significant" | E |
| 7 | A — same data, two ways to slice it | the monthly loop | D — explain the choice to a returns-only shop | "cross-sectional regression" | E |
| 8 | C — units of a covariance | build `F` | D — teach "the direction with the most wobble" | "half-life", "covariance matrix", "shrinkage" | E |
| 9 | A — will `Δ` be too big or too small? | build `Δ` | **B** — a decomposition that fails to add up | "specific risk", "diagonal" | E |
| 10 | C — assemble from units alone | `Σ = XFXᵀ + Δ` by hand | **B** — factor + specific ≠ total | "asset covariance matrix", the `D`/`Δ` letter swap | E |
| 11 | A — which position is the risk? | contributions | D — explain to the PM | "active risk", "marginal contribution" (GAP) | E |
| 12 | A — predict what the paper omits | the audit | D — brief a committee in 90 seconds | "bias statistic", "in/out-of-sample" | E ×3 (`gm/CRITIQUE.md` §9) |

---

## 4. THE bps SCHEDULE

bps are earned for **reasoning**, never for answers. `[GM DESIGN]` — the rules set the currency and
the three deductions; the numbers below are this playbook's calibration, chosen so that one boss
round outweighs a whole level of arithmetic and one untraced number outweighs two correct sums.

### 4.1 Earning

| What the player did | bps | Condition |
|---|---|---|
| **Correct computation** — turns the handle on given numbers, arithmetic right, method stated | **+10** | Zero if the method cannot be stated. |
| Computation where the player caught their own slip before you did | +15 | Self-audit is the habit being built. |
| **Correct derivation** — rebuilds the formula from nothing | **+40** | Must be from nothing. Recalling it is +0. |
| Derivation that includes the step textbooks skip (where the denominator comes from, why squared, where a standard error comes from) | +10 bonus | Victory Condition 3 in miniature. |
| **Round A** — direction and rough size committed *with a reason*, reason correct | **+15** | Right guess, wrong reason: **+0**. Say so out loud. |
| Round A where the prediction was wrong but the reason was structurally sound | +5 | Reward the reasoning; the game is not about being right first. |
| **Round B** — finds the corruption via a structural check | **+30** | Naming the check *before* looking: +10 bonus. |
| Round B solved by recomputing everything | +10 | Brute force works and is not the lesson. Say that. |
| **Round C** — correct shape from units alone, before seeing the formula | **+25** | |
| **Round D** — explanation survives the character's awkward question | **+30** | Grade the explanation, not the vocabulary. |
| **Round F** — translation + new sentence about a *different* situation + survives the follow-up | **+15** | Translation only: +5. Circular translation: +0 and a dock (§4.2). |
| **Interrogation: one objection held** | **+25** | Per objection, three per boss round. |
| **Interrogation: boss round passed** (all three objections held, on all three columns of §5.1) | **+100** | This is the promotion currency. |
| Unprompted callback — spotting that √n, Cov/Var, the balance condition, centering or `t²` has appeared before, and where | +10 | Rule §8, CALL BACK. Reward loudly. |
| **Demanding the origin of a number you asserted** | **+20** | Victory Condition 1 in miniature. Pay it even when it costs you the flow. |
| Catching a genuine error of yours | +25 | Pay it, say it, fix it. |
| Correctly refusing to firm up an `[APPROX]` or `[UNREADABLE]` value | +10 | The player must inherit the source discipline. |
| **Right answer, wrong reasoning** | **+0, always** | Rule §8, the single most important rule. Never partial credit. |

### 4.2 Deductions — the three named in the rules, made specific

| Offence | What it looks like | Deduction | Recovery |
|---|---|---|---|
| **HAND-WAVING** | An assertion offered where a mechanism was asked for: "it just works out", "that's the standard approach", "the maths gives you that", "it generalises". | **−20**, first time in a round. **−40** the second time in the same round. | Rebuilt on demand, in the same round: half returned. The escalation is the teaching device — name it out loud each time: *"that was hand-waving; twenty."* |
| **UNDEFINED TERM** | The player uses a term they cannot define when stopped mid-sentence. Includes terms you have not yet unlocked, which they imported from outside. | **−25**, and **the term is confiscated** — they may not use it again until they define it unprompted in a later round. | Defining it correctly later: +15 and the word is returned. |
| **ACCEPTING AN UNTRACED NUMBER** | Uses a figure — yours, the paper's, or their own from three rounds ago — and cannot say what arithmetic produced it. Includes accepting a number *you* planted. | **−30** — the most expensive deduction in the game. | Tracing it fully: +20. Never waive it: this is exactly the Wiki Test failing. |

### 4.3 Secondary deductions

| Offence | bps | Note |
|---|---|---|
| Quoting a pixel-measured chart value as a printed number | −15 | The player-side version of your own rule. **Fourteen figures print no data label anywhere**: 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, **1.11**, 1.12, 1.14, 1.17, 1.18. **Four do print every cell** and are safe to quote as printed: the exposure-correlation matrices 1.3 (p.11), 1.13 (p.19) and 1.15 (p.20), plus 1.16 (p.22), the table of company emerging-market exposures. The remaining two, 1.19 and 1.20 (p.37), are flowcharts with no data. |
| Argument from authority — "BlackRock wouldn't do that", "it's an industry standard model" | −15 | Fatal at L12; dock from L4 onward. |
| Circular translation in Round F — "cross-sectional means we do it in the cross-section" | −10 | |
| Reading a right answer off a remembered formula when the round asked for a derivation | −10 | Not dishonest; just not the round being run. |
| Guessing, and saying so | **0** | Never punish an honest guess. It earns nothing, which is punishment enough. |

### 4.4 House rules on the ledger

- **bps may go negative.** Say the number, do not comment on it.
- **bps never buy a promotion, and never block one.** A player at −200 who passes the L8 boss is a
  Researcher. A player at +2,000 who has not is not. (Rules §4.)
- **Deductions are announced at the moment they happen, with the reason and the number**, then the
  round continues. Do not accumulate silently and reveal at the end — the deduction is feedback, not
  a scoreline.
- **Never dock for being stuck.** Stuck is your failure (Rules §2). Dock only for the three named
  offences, which are all forms of pretending.

---

## 5. PROMOTION GATES — Intern to Author

Two rules from `prompt/RISK_DESK.md` govern this and they are different:

- **Every** boss round must be passed to advance a **level**. "Do not advance until the boss round is
  passed" (§5).
- **Four** boss rounds also advance a **rank**. "Promotion requires passing a Boss Round, never just
  accumulating bps" (§4).

`[GM DESIGN]` — the rules name the five ranks but do not attach them to levels. This is the
attachment, chosen so each rank corresponds to a thing the player can now do alone.

| Rank | Held during | Promotion gate | What the gate proves |
|---|---|---|---|
| **Intern** | L0 – L3 | — (starting rank) | — |
| **Analyst** | L4 – L7 | **L4 boss — The Collision** | Can be trusted with more than one column. A coefficient means "what this column explains that no other column already explained", and they can *quantify* how wrong the one-at-a-time answer gets. |
| **Researcher** | L8 – L11 | **L8 boss — The Weather Map** | Can be trusted with an estimated matrix. Knows that an estimate can be structurally broken while every individual number in it looks fine. |
| **Model Owner** | L12 | **L12 boss — The Critique** | Can be trusted in a room with the model's authors and its critics, and can tell a real weakness from a cheap shot. |
| **Author** | ★ | **★ THE REBUILD** | Built the whole thing on fresh data with no help. Victory Condition 4. |

**Reconciliation note.** `gm/CRITIQUE.md` §9 Script 3 says "Promote to Model Owner" at Level 12. That
is this table. A rank advances **one step per gate**; a player who arrives at L12 having somehow not
been promoted earlier is promoted only one rank by it.

### 5.1 What each boss round must demonstrate before you pass it

Pass on **all three** columns. Two out of three is a fail, and you say which one failed.

| L | Boss round | Must demonstrate — mechanism | Must demonstrate — direction of error | Must demonstrate — origin |
|---|---|---|---|---|
| 0 | Two datasets, identical raw sum of misses | Why cancellation is not smallness; why squares and not absolutes | Which desk's model is worse and **by how many times** (Desk B is 144× Desk A by `Σe²`, `datasets/level0.md`) | That squaring is *our* argument — **GAP**: the paper never derives squared loss, never writes "least squares" |
| 1 | A factor return by hand, magnitude guessed first | `b = Σxr/Σx²` derived by nudging, no calculus | What happens to `b` when a stock with `x = 0` is added, and why | `f` in (1.7), p.24; the market factor return is this calculation on a column of ones with √-cap weights (p.4 fn 2, p.25) |
| 2 | Sabotage: find the corrupted residual | Locates it by `Σx·e ≠ 0`, not by eyeballing | The size of the corruption, `d / xᵢ`, not just its location | That `Σx·e = 0` is forced by arithmetic, whereas (1.10) on p.26 is forced **by hand** — and that the paper contains the second, not the first (**GAP**) |
| 3 | 2×2 normal equations in fractions | Two conditions holding **simultaneously**, sharing one residual vector | What one-at-a-time gets wrong when the columns are related | (1.9), p.25 — four blocks in one solve; p.5's "neutral with respect to market, style and industry effects" |
| 4 ★ | Dataset where naive one-at-a-time is catastrophically wrong | Coefficients blow up in opposite directions **while fitted values barely move** | Quantified: the ratio between the naive answer and the joint answer, on their own dataset | p.32 (VIFs, "problems in apportioning the factor return between them", "instability … through time") + fn 16 (perfect correlation → estimation **fails**) |
| 5 | Fitted line passes through `(x̄, r̄)` | The proof, not the assertion | What breaks if exposures are not centred: the market column and the style column fight for the same level | p.10 and p.39 — BFRE standardises to a √-cap-weighted mean of zero; p.26 — three columns of ones exist at once |
| 6 | Big coefficient, small t — argue both ways | A standard error built from scratch; `t² = (S²/Q)/σ²` | Which way the model is wrong if the bar is set too low (junk columns in `F`) and too high (real common variation dumped into `Δ`) — **INFER** | \|t\| > 2 (p.8); 10% (p.14, p.32); the 10–15% stopping rule (p.12). **GAP**: no standard error, no degrees of freedom anywhere in the paper |
| 7 | Why cross-sectional, and what it costs | Describes the loop exactly: one regression per period, `n` assets per regression, one number per factor per period | The cost: exposures measured with error every period, and errors in `X` at `t` go straight into `f` at `t` | p.24 "a series of cross-sectional regressions"; daily for country/regional, weekly for World; p.2 (STORM contrast); p.13 (AOL) |
| 8 ★ | Covariance from fewer *effective* observations than factors | On the **toy** (`K` factors, `T < K` observations) there exists a combination the estimate scores at **exactly zero** risk. On **BFRE** the honest claim is the effective-sample one — see §8.2 L8 and `gm/LEVEL_ANCHORS.md` §11; the naive "fewer months than factors" line is **false for NAMR** and must not be asserted | An optimiser searches for low risk, finds the under-estimated directions and loads them — risk understated exactly where the book concentrates (**INFER**, flag it) | p.27: WKL = 104 weeks, 26-week half-life — *and* "a history of daily factor return series starting in **March 1996**", which is a different number the paper never reconciles; method **deferred** to BRS documentation. **GAPS**: no eigenvalue, no factor count, no rank discussion, no condition number, no shrinkage of `F` |
| 9 | Diagonal assumption fails; risk too low where it hurts | A concrete two-asset scenario, computed both ways, **and** knows which of the two failure modes BFRE catches and which it does not | **Too low** on a long-only book, too high on a long-short one | p.28, verbatim: ignoring the correlation "would lead to under (or over) prediction of specific risk in a long-only (long-short) portfolio context." Plus the generic-vs-shipped distinction (p.24's "In general…a diagonal matrix" vs p.27's sparse off-diagonals) **and** the assumption that actually ships uncorrected: different issuers assumed zero, p.28 and p.30 |
| 10 | 3-stock portfolio risk by hand, decomposed | Every multiplication read as a sentence; variances add, volatilities do not | What a dropped `Δ` does (single-stock portfolio's risk = its factor risk) and what dropped off-diagonals of `F` do (offsetting bets stop cancelling) | (1.7) and (1.8), p.24, one line apart. The `D`/`Δ` letter swap. p.4: exposure ≠ beta |
| 11 | The PM who insists they are diversified | Contribution ≠ exposure, demonstrated with the model's own numbers | Which position to cut first, and by what criterion | p.34/p.35: Active Risk decomposed by block; Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec **1%** `[INFERRED]`. **GAP**: no marginal-contribution formula in the paper |
| 12 ★ | Defend as author, attack as rival | Both sides at Tier 4 (`gm/CRITIQUE.md` §10). One-sided fails | Ranks the weaknesses and says which one goes into the meeting and which stays out | p.33 ([27] "available on request") vs p.65 (bibliography: "**forthcoming**"); N ≥ 200 (p.10), 200+ (p.55), \|t\| > 2 (p.8), Random Substyle (p.56, Table 1.4) |
| ★ | THE REBUILD | The whole model on fresh data, alone, no reference material | Sanity-checks their own output: the common/specific split | p.35's worked example is 50/50 — of **active** risk, on **one** EMEA portfolio (p.34), so it is an order-of-magnitude check and not a target. A rebuild at 95% specific has an `X` that explains nothing; 95% common has factors that ate the noise |

★ = promotion gate.

### 5.2 Failing a boss round

- Say **which of the three columns failed**, in one sentence.
- Do not re-run the same boss round with the same framing. Change the dataset or change the attack.
- A boss round failed twice means the level was passed too early. Drop to the diagnostic in §7 for
  that level, and expect the break to be **one level below**.
- Never let a boss round be passed at Tier 3. See §6.

---

## 6. THE FIVE TIERS — scoring, per concept

Score every concept, not every level. A player is routinely Tier 5 on residuals and Tier 2 on
covariance in the same session; the ladder is a per-concept object and the player must see theirs.

| Tier | Name | The evidence that puts them there | The evidence that does **not** |
|---|---|---|---|
| 1 | **Recognise** | Uses the word in a sentence that is not wrong | Nodding. Repeating your sentence back |
| 2 | **Compute** | Turns the handle on numbers you supply and gets the right answer | Getting it right with a method they cannot state — that is Tier 0 and a dock |
| 3 | **Derive** | Rebuilds the formula from nothing, unprompted, including the step textbooks skip | Recalling it. Reconstructing it after you supply the first line |
| 4 | **Defend** | See §6.1 — survives an attack on the **assumption**, not the algebra | Restating the derivation louder. Winning by volume |
| 5 | **Rebuild** | Constructs it unprompted on data they have never seen, and notices when its assumption is violated there | Doing it correctly on the same dataset again |

**Never call a level complete below Tier 4** on the concepts that level exists to build (Rules §7).

### 6.1 The tier 3 → tier 4 boundary — the whole game turns here

Tier 3 is about the **derivation**. Tier 4 is about the **assumption**. A player at Tier 3 can rebuild
the formula and cannot tell you what would have to be true for it to be the right formula.

**The three-question test.** One exchange, three questions, in this order. Tier 4 requires all three,
without you supplying vocabulary or the first half of the answer.

| # | The question | What Tier 4 sounds like | What Tier 3 sounds like |
|---|---|---|---|
| 1 | **The assumption question.** "What did you assume?" | Names the assumption *before* you say there is one, and names it as an assumption rather than as a fact | "Nothing, it's just algebra." Or names a step of the derivation instead of an assumption |
| 2 | **The counterexample question.** "Here is a case where that fails. Now what?" | Answers with a *mechanism* — what specifically breaks, in what order | Repeats the derivation more slowly. Or "that's an edge case" |
| 3 | **The consequence question.** "Which number in the model moves, and in which direction, and on whose book?" | Names the number, the direction and the kind of portfolio it hurts | "The risk would be wrong." Or the direction stated with no reason |

### 6.2 The six markers of Tier 4

Log these in the save file when you see them; they are what "Defend" means concretely.

1. **Volunteers the assumption unprompted**, before the attack arrives.
2. **States the direction of error**, not merely that there is one, and says which portfolio it hurts.
3. **Concedes** the part that cannot be defended, without abandoning the part that can.
4. **Refuses argument from authority** — including yours, and including BlackRock's.
5. **Survives a change of angle**: you attack a second front and they do not have to restart.
6. **Distinguishes what is forced from what is chosen from what is assumed.** The single sharpest
   instrument in this game. Three worked examples, in ascending difficulty:
   - `Σx·e = 0` is **forced** by the arithmetic of the fit. It could not have been otherwise.
   - (1.10) on p.26 is **chosen** by the authors, and they say why: without it the specification "is
     not uniquely identified as there are an infinite number of possible solutions".
   - The specific covariance is **assumed** — but be precise about *which* assumption, because the
     obvious version is a cheap shot. p.24's "a diagonal matrix" sits under the lead-in "**In general
     a multi-factor model** decomposes asset returns as follows": it describes the generic textbook
     object. p.27 then says what BFRE actually ships — a vector of specific risks **plus** "a sparsely
     populated unit diagonal matrix containing non-zero, off-diagonal specific return correlations" —
     and p.28 gives it a subsection with two methodologies and the direction of the error. That is a
     textbook form followed by a shipped form, **not a contradiction**, and calling it one is
     `gm/CRITIQUE.md` **CS-3**, a named cheap shot that costs the player Level 12. The real assumption
     is the **scope**: correlations are estimated only between assets *in the same company*, and
     across companies are "assumed to be zero **in-line with standard modelling practice**" (p.28),
     listed as an assumption on p.30. An appeal to convention, stated as one, never tested.

   A player who tracks all three categories is Tier 4. One who does not is Tier 3 no matter how good
   the algebra is. A player who reaches for the p.24-vs-p.27 "contradiction" is Tier 3 *and* has to be
   walked to the scope version before the level closes.

### 6.3 Demotion

A concept can lose a tier, and must. If a player at Tier 4 on the balance condition later accepts a
corrupted file without checking it, they are Tier 3 on that concept again. Say so, record it, move on.
Do not soften it and do not dwell.

---

## 7. THE FAILURE PROTOCOL — one diagnostic question per level

The rules (§10) forbid "what don't you understand". That question asks a lost person to survey their
own ignorance, which is the one thing being lost makes impossible. Ask instead a **specific question
whose answer localises the break**.

### 7.1 The five steps, in order

1. **Stop the level.** Mid-sentence if necessary. Do not finish the thought you were on.
2. **Ask the one question below.** Nothing else. No preamble, no "let's just check something".
3. **Read the answer against the table** and identify the rung.
4. **Drop to the level named**, and say plainly that you are doing so and why.
5. **Rebuild with smaller steps and a different analogy.** Never elaborate the failed version
   (`gm/ANALOGIES.md` §2 has the burn ledger — check what has already been spent).

Say the frustration line **once**, and then never again in the session:

> "That explanation failed, not you. I am going to throw it away and build a different one."

### 7.2 The thirteen questions

Each cell in "Drop to" is a level or a specific artefact. Where it names a file, open the file.

---

#### L0 — THE MISS

> **"Here are two misses: +6 and −6. Here are two others: +1 and −1. Which pair is worse, and by how many times?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "The same — both cancel to zero" | They are still scoring by **sign**. The level has not started. | The three-desks table in `datasets/level0.md`. Desk A, B and C all report `Σe = 0`; Desk B is 144× Desk A by `Σe²`. Re-run it in money |
| "The first, but I can't say by how much" | They have **size** but not **scale** — no loss function yet, only an intuition | Stay at L0. Build the scorecard explicitly: `Σe²` for the pairs is **72 vs 2**, ratio **36** |
| "Six times worse" | They are scoring with **absolute values** (12 vs 2). Real answer, wrong loss | Stay at L0, run the `r = [1, 2, 9]` exhibit: least absolutes picks the **median** (b = 2, ignores the 9); least squares picks the **mean** (b = 4). A risk model must be moved by the big miss |
| "Thirty-six times" | Nothing is broken here. The break is elsewhere — re-ask at L1 | Return to the level and find the real break |
| "Depends what you're using it for" | Tier 4 answer at L0. Ask them to name the two uses | Return, and note the tier |

---

#### L1 — THE DIAL

> **"Without computing anything: I add one more stock, with `x = 0` and any return you like. Does `b` change? Why?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "Yes — it changes the average return" | They think `b` is an **average of returns**, not a ratio of two sums | L0's CHR trap: the stock with `x = 0.0` and `r = +0.5%` that **no** `b` can ever predict (`datasets/level0.md`) |
| "No, because zero exposure means no effect" | True conclusion, no mechanism. Tier 2, hand-wave — dock | Stay at L1. Make them name the **two sums**: it adds `0` to `Σxr` and `0` to `Σx²` |
| "No — it adds nothing to `Σxr` and nothing to `Σx²`" | Nothing broken. Formula owned | Return to the level |
| "I'd have to compute it" | They can turn the handle and do not own the formula | Stay at L1, run Round **C**: units only. A sum in percent over a sum of squared pure numbers |
| "It changes because there are more stocks now" | They have imported a `1/n` from somewhere — a half-remembered average | L0, then rebuild the nudge from `SS(b+h) − SS(b) = −2h·P(b) + h²·Σx²` |

---

#### L2 — THE BALANCE

> **"Here is a finished fit — the `x` column and the miss column. `Σe = 0`, but `Σx·e = 4.2`. Is this a least-squares fit? Which of those two numbers did I actually need?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "Not sure" / "Yes" | They have not internalised which balance the arithmetic **forces** | L1's nudge identity. `P(b) = Σxr − b·Σx²` **is** `Σx·e`, and the fit is defined by `P(b) = 0` |
| "No, because `Σe` should be zero" | The two conditions are **swapped**. This is the most common break in the game | `datasets/level0.md`: in the cold open `Σe = 2` while `Σx·e = 0` — the fit is optimal and the raw sum is not zero |
| "No — `Σx·e` must be 0; `Σe` is irrelevant here because there is no intercept" | Nothing broken. Note the intercept clause: that is L5 arriving early | Return, and record the callback |
| "No, the numbers look wrong" | Hand-waving. Dock 20 | Stay at L2, re-run the balance as a **turning force** about a pivot (`gm/ANALOGIES.md` C3) |
| "Both should be zero" | They have a remembered fact about intercept models and no mechanism | L1, then L5's preview: which condition an intercept adds, and why |

---

#### L3 — THE SECOND DIAL

> **"Two columns now. I tell you the finished fit satisfies `Σx₁·e = 0`. Is that enough to know `b₁` is right?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "Yes" | They are solving columns **independently**. This is the exact error L4 is built to punish | L2 → L3 bridge. Show that `e` is a single shared vector: fixing `b₂` changes `e`, which changes whether `Σx₁·e` is still zero |
| "No — `Σx₂·e = 0` has to hold at the same time, and it is the **same** `e`" | Nothing broken. "The same `e`" is the Tier 3 marker | Return |
| "No, you need more data" | Confusing **identification** with **sample size** | L1. Then p.26's "three intercept terms" as the identification story, not a data story |
| "No, because they're correlated" | Right instinct, wrong level — that is L4 and it does not answer the question | Stay at L3. Correlation is not needed: two conditions are required even for uncorrelated columns |

---

#### L4 — THE COLLISION  *(graduate-level — say so before you diagnose)*

> **"Column 2 is column 1 plus a tiny wiggle. I fit both. What happens to the two coefficients — and what happens to the fitted values?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "The coefficients blow up in opposite directions; the fitted values barely move" | Nothing broken. This *is* multicollinearity | Return. Then hand them p.32: the paper's own words are "problems in **apportioning** the factor return between them" |
| "Everything blows up" | They have not separated **coefficient instability** from **prediction stability**. This is the heart of the level | Stay at L4. Compute both: the fitted values, then the coefficients. Two columns, four rows, by hand |
| "The second coefficient goes to zero, it's redundant" | They expect the algebra to do the tidy thing. It does not — it splits the credit arbitrarily | L3: two conditions, one shared `e`, and the determinant approaching zero |
| "I don't know what happens to the fitted values" | The break is **below** L4: they have lost that the fit is chosen to minimise the miss | L0 → L1. Rebuild the loss, then return |
| "You'd drop one of them" | A practitioner's answer with no mechanism. Dock if offered as an explanation | Stay at L4, then show the paper doing exactly that once (EMEA merged Earnings Yield and Dividend Yield into "yield", p.20) and declining to do it elsewhere |

---

#### L5 — THE INTERCEPT

> **"The fit has an intercept. I add 100 to every single `x`. What happens to the slope, and what happens to the intercept?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "Slope unchanged; intercept moves by −100 × slope" | Nothing broken | Return |
| "Both change" / "the slope changes" | The pivot is not understood — they think the line is anchored at `x = 0` | L1, then rebuild with two points and actual arithmetic. Two data points, compute both fits |
| "Nothing changes" | They believe the intercept absorbs everything, without having done it | Stay at L5. Make them compute it. Then show p.10: BFRE removes the level by construction — exposures are standardised to a **√-cap-weighted mean of zero** |
| "It depends on the data" | Hand-waving. Dock | Stay at L5; the answer is data-independent and that is the point |

---

#### L6 — THE VERDICT

> **"Same coefficient, same data, but now I quadruple the number of stocks and the misses stay exactly the same size. What happens to the t-statistic, and why exactly?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "It doubles — the wobble in `b` falls like √n" | Nothing broken. Fire the callback: they have met √n before | Return |
| "It quadruples" | They have `SE ∝ 1/n` instead of `1/√n`. Very common | Stay at L6. Rebuild the estimate's spread from `Σx²` in the denominator, and take the square root **out loud** |
| "It goes up, I don't know how much" | Tier 2. Direction without machinery | Stay at L6, build the standard error from scratch. Flag it: most textbooks skip this; **so does this paper** (GAP) |
| "Nothing — t depends on the size of `b`" | They think `t` is a statement about the coefficient alone | L1: `b` is a computed number; ask what would change it. Then build "how much does `b` wobble" as its own object |
| "You'd need to know the variance" | Close. Ask which variance, of what | Stay at L6 and finish the construction; this is one prompt from Tier 3 |

---

#### L7 — THE TIMELINE

> **"I hand you 60 months of returns for 500 stocks. Tell me exactly what you regress on what, how many regressions you run, and how many numbers come out."**

| They answer | The broken rung | Drop to |
|---|---|---|
| "60 regressions, 500 rows each, one number per factor per month" | Nothing broken | Return. Anchor it: p.24, "a series of cross-sectional regressions" |
| "500 regressions of 60 rows each" | They are doing **time-series betas**. That is the rival design, not this one | Stay at L7 and run it as the contrast. BFRE does that exactly once — (1.12), p.42, historical beta, 5 years of weeklies with a 52-week half-life — and it enters as an **input substyle to Volatility**, never as the exposure mechanism |
| "One regression with 30,000 rows" | Pooled. They have lost that `f` changes every period | L3 → L7. Ask what a single `f` would mean if the factor paid differently in 2008 and 2013 |
| "One regression, I think" | Below L3. The multi-column solve is not solid | L3 |
| Correct, then adds "and the exposures move too" | Tier 4 arriving early — that is the cost of the design | Return, record the tier, and use it in the boss round |

---

#### L8 — THE WEATHER MAP  *(graduate-level — say so before you diagnose)*

> **"You have 20 factors and 12 months of factor returns. I claim there is a combination of those factors whose forecast risk is exactly zero — even though every single factor is risky. True or false, and why?"**

**This question is about a toy, and you must say so before you ask it.** 20-and-12 is invented, clearly
labelled, and its only job is to make the mechanism visible. **Do not let it slide into a claim about
BFRE.** BFRE's default is 104 weekly observations (p.27) against a NAMR factor count that assembles to
roughly 71 from Table 1.2 and Table 1.5 — so the literal `T < K` case does *not* hold there. The
BFRE-side version of this argument is the effective-sample one in §8.2 L8. A GM who runs the toy and
then says "and that is what BFRE does" has fabricated.

| They answer | The broken rung | Drop to |
|---|---|---|
| "True — with fewer observations than factors there is always a combination that was flat in every month observed, and the estimate reads that as zero risk" | Nothing broken; this is Tier 4 material *on the toy* | Return. Then the consequence: an optimiser **finds** that combination (INFER). Then the honest bridge: ask them what BFRE's actual numbers are, and whether the argument still bites at 104-against-71 |
| "False — risk can't be zero" | Intuition with no mechanism | Stay at L8. Build the smallest case by hand: two factors, **one** observation. Every combination that was flat that day is scored at zero |
| "True, but I can't say why" | Tier 1. They have heard this somewhere | Stay at L8 and build it from 2 factors up |
| "You'd need more data" | True and evasive — it does not say what breaks | Stay at L8; the question is what the estimate **claims**, not what would fix it |
| Answers correctly using eigenvalues, unprompted | Tier 4 plus. Reward it — and note the **GAP**: no eigenvalue, eigenvector or principal component anywhere in the 65 pages | Return |

---

#### L9 — THE PRIVATE DRAMA

> **"A book holds two things only: an ADR and the ordinary share of the same company, half and half. The model gives each a specific risk of 20%. What does the model say the portfolio's specific risk is — and what is it really?"**

**Say "the model" and mean equation (1.8) as printed on p.24, not BFRE as shipped — and say which you
mean, out loud.** This exact pair is the case BFRE *catches*: p.28 names "ADRs and their root assets"
and forces the specific return correlation to **1** under the structural approach. So a GM who says
"BFRE would understate this book's risk" has said something false, and a player who has read p.28 will
know it. The scenario is here because it makes the arithmetic of a broken diagonal visible in two
numbers — and the payoff is the follow-up: *"BFRE fixes this one. Name the one it does not fix."*
The answer is two assets in **different** companies whose specific returns really do move together —
assumed to zero "in-line with standard modelling practice" (p.28), listed as an assumption on p.30 —
and the residual case BFRE admits it still misses: companies with more than one share class carrying
derived securities, e.g. Chinese MMA securities, "will be addressed in a forthcoming model release"
(p.30).

| They answer | The broken rung | Drop to |
|---|---|---|
| "Model says ≈14.1%; really 20%, because the two specific returns are the same event" | Nothing broken. `0.2 × √0.5 = 14.14%` versus `20%` — the model understates by about 30% of the true number | Return, then hand them p.28's own sentence |
| "The model says 20%" | They have not got the aggregation — they are averaging risks rather than combining them | L10 preview, on two assets only. Variances add, volatilities do not |
| "It's too high" | **Sign error on the direction**, which is the whole level. Dock and stop | Stay at L9. p.28: ignoring the correlation "would lead to **under** (or over) prediction of specific risk in a **long-only** (long-short) portfolio context" |
| "They'd be correlated so it's more complicated" | Right instinct, no number | Stay at L9 and make them compute both cases |
| "That's what `Δ` being diagonal means" | Tier 3–4. Ask the follow-up: does **BFRE** ship a diagonal `Δ`? | Return. p.24's "a diagonal matrix" is the generic form ("In general a multi-factor model…"); p.27 says BFRE's own specific covariance carries **non-zero off-diagonal** correlations, and p.28 gives them a subsection. Do not sell this as a contradiction — see CS-3. Push instead to the scope: same company only; across companies zero "in-line with standard modelling practice" (p.28, p.30) |

---

#### L10 — THE ASSEMBLY

> **"Read `XFXᵀ` to me as a sentence, right to left, and tell me the units at each step."**

| They answer | The broken rung | Drop to |
|---|---|---|
| Sentence + units, correctly, ending in variance | Nothing broken | Return. Then the letter warning: the game writes `V = XFXᵀ + D`, the paper writes `Σ = XFXᵀ + Δ` (p.24) |
| "It's matrix multiplication" | Hand-wave. Dock 20 | Stay at L10 with **one** factor and **two** assets, entirely in scalars |
| Gets the order backwards, or cannot say which side is the portfolio | The meaning of a column has not survived from L3 | L3. What one column of `X` is, and whose numbers are in it |
| Correct sentence, no units | Tier 3. Units are how they will catch their own errors forever | Stay at L10 for one round: percent, percent-squared, and where the square root goes back in |
| "And then you add `D` because the model can't explain everything" | Tier 4 sentence. Ask which number on p.35 that `D` is | Return: Specific is **50%** of Active Risk on the paper's own example report |

---

#### L11 — THE DESK

> **"Position A is 10% of the book and contributes 2% of the risk. Position B is 3% of the book and contributes 5%. Which do you cut first to reduce risk fastest — and what number are you actually using to decide?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "B — its contribution per unit of weight is far higher, and the number is the **marginal** one: how total risk moves when I nudge the weight" | Nothing broken | Return. **GAP**: the paper has no formula for this and never uses the term |
| "A — it's the bigger position" | Exposure and contribution have collapsed into one idea. This is the level's entire content | Stay at L11 with p.35: Emerging carries **active** exposure ≈ **−0.10 sd** and contributes ≈ **0%** of active risk `[APPROX — pixel-measured, ±10%]`. The report plots the two on **two different axes** for exactly this reason |
| "Depends on the correlations" | True and useless until they say how | Stay at L11 and build the nudge: change one weight a little, watch the total |
| "B, because 5 > 2" | Right answer, incomplete reasoning — the weights are the point | Stay at L11 one more round; this is one prompt from Tier 3 |
| "You'd have to re-run the optimiser" | Outsourcing the mechanism. Dock if offered as the answer | L10, then rebuild the contribution from the assembled `Σ` |

---

#### L12 — THE CRITIQUE

> **"Name the weakness you would lead with in front of the model risk committee, and name a weakness you would refuse to raise at all. Why each?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| Leads with the deferred testing evidence, or with 200+ candidates and no correction; refuses a typo or a cosmetic complaint | Nothing broken. Tier 4 on the attack side | Move to the defence side — one-sided fails the level (`gm/CRITIQUE.md` §10) |
| Leads with a typo, or with √-cap weighting | No **ranking**. They can find weaknesses and cannot weigh them | `gm/CRITIQUE.md` §6, the cheap-shot list. Then re-ask |
| Cannot name one to refuse | Tier 3, not 4. Everything looks equally damning, which means nothing is | Stay at L12. Make them rank five, out loud, and defend the ordering |
| "The whole thing is unfalsifiable" | Overreach — and it is false: the VaR back-test is specified precisely (99%, 252 days, UCITS + Kupiec 1995, p.38) | `gm/CRITIQUE.md` §8, the concessions a credible rival must grant |
| Attacks the scan — "I can't read Figure 1.9", "the captions on p.58 are cropped" | They are attacking `notes/`, not the paper. Never allowed | Restate the rule and re-ask. This is an automatic fail if repeated. **But separate it from the two adjacent moves that are correct and paid.** (a) Refusing to firm up an `[APPROX]`/`[UNREADABLE]` value — including one *you* just used — is +10 under §4.1 and is the discipline you are trying to install; never dock it. (b) The one admissible version of the figure complaint is about the **document**, not the photocopy: fourteen of the paper's twenty figures carry no data label at all, so every quantitative claim made from a chart is unauditable by design. That is `gm/CRITIQUE.md` CS-10-done-properly, and it is a real attack |

### 7.3 When the diagnostic itself fails

If the diagnostic question is also met with silence, the break is **at least two levels down**. Do not
ask a second diagnostic at the same level — go straight to the L0 or L1 question, whichever is nearer,
and rebuild from there. Record in the save file that you did this: the level was passed too early and
its ladder positions are now suspect.

### 7.4 NAME THE BEDROCK — the other way a "why" chain ends

Rules §8: *"When a 'why' chain reaches a definition or an axiom, say so plainly, so the player knows
they've arrived rather than stalled."* This is not the failure protocol's twin, it is its opposite,
and confusing the two is expensive in both directions. A player who has hit bedrock and is not told
so will keep digging and conclude they are stupid. A GM who has hit bedrock and will not admit it
will invent a deeper reason — which is the hand-waving offence, in your own mouth, uncharged.

**The line, and say it exactly this flatly:** *"That is the bottom. It is a choice, not a consequence —
here is what it buys and here is what it costs."* Then give both, and move.

The bedrock in this game, in the order the player will hit it:

| The "why" that ends | What it is | The honest sentence |
|---|---|---|
| *Why squared misses and not absolute ones?* | **A choice.** No theorem forces it. `datasets/level0.md`'s `r = [1, 2, 9]` shows the two losses picking the median and the mean | "Squaring is our choice, made because a risk model must be moved by the big miss. **The paper never derives it and never writes 'least squares'** — it inherits it" |
| *Why is `Σx·e = 0`?* | **Forced.** Bedrock of a different kind: it is a consequence of the definition of the minimiser, provable by the nudge, and could not have been otherwise | "This one is not a choice. Nudge `b` and the identity falls out. If it fails, arithmetic failed" |
| *Why does an exposure of zero mean market average?* | **A definition**, p.10 and p.39: standardised to a √-cap-weighted mean of zero | "Because they defined the mean to be there. Nothing deeper — and that is why the sentence is true rather than merely nice" |
| *Why `Σ = XFXᵀ + Δ` and not something else?* | **A modelling assumption**, and p.24 says so in its own lead-in: "**In general** a multi-factor model decomposes asset returns as follows" | "That is the model, not a result. Every number downstream is conditional on it" |
| *Why are specific returns of different companies uncorrelated?* | **A convention**, and the paper marks it as one: "in-line with standard modelling practice" (p.28), listed as an assumption (p.30) | "The paper's whole justification is that everyone does it. That is bedrock by convention, which is the weakest kind — and it is Level 12's material" |
| *Why √-cap regression weights?* | **Argued, not derived** (p.25: three arguments, plus fn 14's alternative) | "Argued from three directions and never proved. This is the best-justified choice in the paper, which is why attacking it is a cheap shot (`gm/CRITIQUE.md` CS-1)" |
| *Why a 26-week half-life? Why 104 weeks? Why ±3?* | **Bare parameters.** p.27 gives the trade-off in words; the numbers themselves are unjustified, and no sensitivity analysis is printed | "The paper prints the number and not the reason. Do not let me pretend otherwise, and do not let anyone else" |

Two standing warnings. **Bedrock is not an excuse to stop early** — say it only when the chain has
genuinely reached a definition, an axiom or an admitted choice, never because you have run out of
explanation. And **"the paper doesn't say" is bedrock about the document, not about the world**: it
ends the citation chain, not the reasoning chain, and the next sentence is always *"so here is what
we would have to build ourselves."*

---

## 8. INTERROGATION SCRIPTS — the boss rounds

### 8.1 How to play the CRO

Thirty years, no patience, has seen four models fail and signed off on three of them. He is not
hostile because he is unpleasant; he is hostile because he is the one who gets fired.

- **Never ask a question you would not ask a colleague.** Every objection below is one a real risk
  officer raises, and most are raised by the paper's own text.
- **Interrupt.** Three sentences of preamble is the point at which he cuts in.
- **Do not accept the first correct-sounding sentence.** Ask the consequence question every time:
  *"Which number moves, in which direction, on whose book?"*
- **Name hand-waving the instant it happens**, dock, and continue in the same breath. Do not stop to
  discuss the deduction.
- **He concedes when beaten.** A CRO who never concedes teaches nothing. When the player lands the
  mechanism, say so — "fine" — and switch to the next front.
- **Three objections per boss round.** All three must be held (§5.1). Hold means: mechanism, direction
  of error, and the origin of every number used. A **follow-up inside** an objection — "fine, now
  answer this" on the same front — is part of that objection, not a fourth. Marked `↳` in §8.2. Adding
  a genuine fourth front because the player is doing well is moving the goalposts; do not.

### 8.2 The scripts

---

#### L0 — THE MISS

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Squares. My P&L is in dollars, not dollars-squared. Score it in the units I get paid in."** | Squaring is the **scoring** device, not the report: the reported number is the square root, so the units come back. And squaring is what makes the loss care about the big misses, which is the entire job of a risk model. Offered with the arithmetic: `Σe²` of 144 vs 1 on the two desks that report the same `Σe = 0` | "Because that's the standard loss function." "Squares are mathematically convenient." |
| **"Least absolute deviations is more robust. Your squared loss will chase one bad print."** | Concedes robustness is real, then: with `x = 1` and `r = [1, 2, 9]`, least absolutes picks the **median**, `b = 2`, and would pick 2 if the 9 were 900 — it discards the tail. A risk model must be *more* sensitive to the big miss, not immune. Bonus: notes that BFRE handles the outlier problem separately, cleansing specific returns "using robust methods to down-weight the influence of outlying observations" (p.27) rather than by changing the loss | "Outliers are rare." "You'd winsorise first." (True, and it is not an answer to the question.) |
| **"Show me one number in this model that would be wrong if you got this wrong."** | `Δ` in (1.8), p.24, is built from the spread of these misses. On the paper's own worked report, Specific is **50%** of **Active Risk** (p.35 pie, read directly) — so on that portfolio, half the *active* risk number is set by how the misses are scored. **Two qualifiers the answer must carry or the CRO takes it apart:** it is a decomposition of *active* risk, not total risk (the paper prints no decomposition of the 15.62% Portfolio Risk on the same banner), and it is *one* portfolio, a European equity book on the EMEA model (p.34) — 50/50 is that book's split, not a constant of the model | "Everything would be wrong." "It would affect the whole model." **"Half of all risk is specific."** — that is a portfolio-specific number stated as a model property, and it is the untraced-number offence in your own mouth |

---

#### L1 — THE DIAL

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"You have fitted a slope with no intercept. Justify that."** | The intercept exists — it just has a name. Exposures are standardised so their weighted mean is zero (p.10, p.39), and the column of ones **is** an intercept: p.26 counts "three intercept terms" per asset, market, industry and country | "The intercept doesn't matter here." "It came out near zero anyway." |
| **"Why is my mega-cap weighted the same as your micro-cap? Your number is being set by names I cannot trade."** | BFRE does not equal-weight: it weights by **√market capitalisation** (p.25), with the reason printed — equal weighting gives "a poor fit for mega-cap and large-cap securities", cap weighting gives "poorer forecasts for mid-cap and small-cap securities", and √-cap "adjusts for heteroskedasticity based on the observation that higher residual (specific) risk is typically correlated with smaller market capitalisation assets". Footnote 14: the textbook alternative, weights of 1/residual variance, "provide similar results" | "Bigger companies matter more." "You'd cap-weight it." |
| **"Your market factor return — that's just the index return, isn't it?"** | No. It is the **√-cap-weighted cross-sectional average return across the estimation universe** (p.4, fn 2). Highly correlated but not identical: regressing daily S&P 500 excess returns on daily NAMR market factor returns gives **beta 0.99, R² 91%** (p.4), and the paper says why they differ — a broader universe including Canadian stocks, and √-cap weights that lift mid- and small-caps | "It's basically the index." "Close enough for risk work." |

---

#### L2 — THE BALANCE

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Your check flagged a violation. How do I know your check isn't the broken thing?"** | `Σx·e = 0` is an **identity forced by the arithmetic of the fit**, not an assumption imposed on it — and they can show the nudge that produces it. Therefore any violation is arithmetic, not judgement. Contrast, and this is the Tier 4 move: the balance in (1.10) on p.26 is forced **by hand**, because without it the specification "is not uniquely identified as there are an infinite number of possible solutions" | "The maths says so." "That's just how least squares works." |
| **"Fine. Which residual is corrupted, and by how much? Do not tell me 'one of them'."** | From `Σx·e = d`, a corruption of a single residual `i` is `d / xᵢ` — so the size follows immediately once the index is known, and the index needs a **second** structural check (`Σe`, or recomputing `b` on subsets) | "The one that looks odd." "You'd have to check them all." |
| **"This is a toy. On my desk it is 2,000 stocks and 60 factors and nobody checks anything by hand."** | The check is one pass per column and is exactly what a production QC does. BFRE runs a **daily Model QC** whose named checks include "Standardised factor returns" and "Asset returns cleaning" (p.37, Figure 1.19), and the release is exception-based: no exception, auto sign-off and touch files; exception, manual sign-off via the GP Workflow monitor (p.37) | "You'd automate it." "That's an engineering problem." |

---

#### L3 — THE SECOND DIAL

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"You solved two equations. My model has sixty factors. Does anything you just did survive?"** | `k` columns give exactly `k` conditions, one per column, all sharing a single residual vector — the 2×2 is the general case in miniature. BFRE does exactly this for four blocks at once: market, style, core industry, core country, in one regression, (1.9), p.25 | "It generalises." "Same idea, bigger matrix." |
| **"Why not fit each factor on its own and add them up? It is faster and I can explain it to a client."** | Because a coefficient means *what this column explains that no other column already explained*. p.5, the paper's own case: country factor returns are estimated "in a multivariate regression together with other common factors, and are therefore **adjusted to be neutral with respect to market, style and industry effects**" — with the reason, a country whose index is concentrated in one industry | "You'd get bias." "It's not statistically valid." |
| **"Where did the second equation come from? Show me it is not an assumption you helped yourself to."** | Each column supplies a direction to nudge in; the nudge identity yields one condition per column, and nothing was assumed. Then the contrast with p.26 again — that *is* an imposed restriction, and the paper says so | "They're the normal equations." "One equation per unknown." |

---

#### L4 ★ — THE COLLISION  *(graduate-level: say so at the top of the round)*

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Correlated factors are a fact of life. Size and Liquidity sit at 0.74 in your own exhibit. Why haven't you merged them?"** | First, the object: **0.74 is an exposure correlation** (Figure 1.3, p.11, NAMR Dec 2013) — the columns of `X` — not a correlation of factor returns, which is a different matrix. Then: merging is a real option and the paper takes it exactly once, EMEA combining Earnings Yield and Dividend Yield into "yield" (p.20), on the stated ground that they "were found to be highly correlated over the research history". **The paper gives no reason for declining to merge elsewhere** — say that, do not invent one. The defence that *is* available: the selection is recursive, each candidate judged on the residuals of the model built so far ((1.3)–(1.6)), so a heavily overlapping factor scores low *marginally* by construction; dropping it does not remove the risk, it pushes it into other factors' loadings and into `Δ`. And merging costs the interpretability the model is sold on (p.2, p.34). **Do not claim both factors clear the significance bar** — in NAMR, Earnings Yield is the *shortest* bar in Figure 1.8 (p.15, ≈4–5% `[APPROX — pixel-measured]`), below the 10% stated on p.14, and it ships anyway in Table 1.2. That is `gm/CRITIQUE.md` F-1, and a player who finds it before you do should be paid | "0.74 isn't that high." "They measure different things." "Both are significant anyway." (The third is false — check Figure 1.8.) |
| **"If the apportionment between two collided factors is unstable, my attribution report changes month to month with no trades. How is that not a broken product?"** | The mechanism, in the paper's words: "If style exposures are too closely correlated then the regression procedure will encounter problems in **apportioning the factor return between them**. This can result in **significant instability in the factor return estimates through time**" (p.32), and footnote 16: at perfect correlation the estimation **fails** outright. Then what BFRE does about it — VIFs reviewed over the research history (p.32), momentum's window stopped one month early "to exclude the reversal effect" (**the quote is p.17**; the construction is (1.17)/(1.18) on p.44) — and the concession that the **block total** is far more stable than the split inside it. Note honestly: p.32 reports the VIF result as "well within suitable thresholds" and prints **no value and no threshold** | "We monitor multicollinearity." "The VIFs were fine." (That is the paper's hand-wave; do not let the player borrow it.) |
| **"Give me the number that goes wrong, and its direction."** | AOL, p.13: a size measure using market capitalisation alone "would confer large-size status on AOL, and **reduce its risk forecast accordingly**" while its sales-based substyle described "a significantly smaller, and riskier, company". Direction: **too low**, on precisely the name where it hurt. Figure 1.6 levels are `[APPROX — pixel-measured against warped gridlines]` | "The risk would be off." "You'd misattribute the return." |

---

#### L5 — THE INTERCEPT

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"You proved a property of a line. What does it buy me?"** | It is what makes "an exposure of zero means market average" a true statement rather than a slogan: p.10 defines the standardisation so the weighted average exposure is zero, and p.39 repeats it (√-cap mean 0, equal-weighted sd 1, capped at ±3). Without it the market column and the style column compete to explain the same level — the L4 collision, manufactured on purpose | "Centering makes the maths nicer." |
| **"Your mean is √-cap weighted and your standard deviation is equal weighted. Defend that."** | Concede first: it is stated twice (p.10, p.39) and **justified nowhere**. Then the defence that is actually available — the scale factor does not change ranks, signs, or the zero point, so the exposure ordering and the meaning of zero survive it; what it changes is what "one standard deviation" means. Must not pretend the paper argues this | "It's a z-score, it doesn't matter." "That's a detail." |
| **"If you re-standardise every period, a factor's exposure history is meaningless. Isn't it?"** | Exposures are deliberately **relative** — cross-sectional position, not level. The paper measures the persistence question directly: Figure 1.11 (p.17) plots each style's Dec-2013 exposure correlation against its own value in each month of "the previous two years" — the x-axis runs lags 0 to 23, so Dec 2013 itself plus the 23 months before it — and states that reversal and momentum "clearly exhibit the least persistence". One trace collapses from 1.0 to ≈0 by lag 1, which is what a one-month-return exposure would do — but `[UNREADABLE: the mapping of traces to legend entries is not recoverable]`, so never name that line | "We re-standardise, so it's fine." "The correlations stay stable." |

---

#### L6 — THE VERDICT

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Your t-statistic is 1.4. Drop the factor."** | The drop case, mechanically: below \|t\| = 2 the factor's return is not distinguishable from zero in this sample (p.8), and BFRE's actual test is not one t but the **proportion** of significant t-statistics, which "serves as a good proxy for the persistence of individual factor effects" (p.8, p.32), with a stated bar of **10%** for inclusion (p.14) | "It's not significant." (True and empty — no mechanism, no threshold, no consequence.) |
| **"Now argue the other way, and do not say 'get more data'."** | A risk model keeps factors that explain **co-movement**, not factors that pay. The paper's own case: NAMR Volatility has an annualised return of **−0.6%** and a Sharpe of **−0.08** (Table 1.2, p.10) — no reliable return at all — yet ranks as the most significant style in Figure 1.8 (p.15, ≈63% `[APPROX — pixel-measured]`), and p.14 says its significance exceeds "most industry and country factors". Return significance and risk relevance are different tests | "It's still useful." "It might work in other regimes." |
| **"Where did your standard error come from? Show me the arithmetic."** | Builds it: the wobble in `b` comes from the spread of the misses divided by `Σx²`, degrees of freedom is the count of numbers minus the number of dials fitted, and `t² = (S²/Q)/σ²` falls out. **And states the GAP**: this paper never derives a standard error, never says "degrees of freedom", never prints a t-statistic formula. The only inference machinery it names is Newey–West [26] — **p.27, p.28 (Table 1.3's "Newey-West Lag" column) and the bibliography on p.65; it is not on p.38** — and it is used for serial correlation in the *risk* estimates, never for the factor-return t-statistics the selection procedure runs on | "It comes out of the regression." "The software gives you the t-stats." |

---

#### L7 — THE TIMELINE

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Every model I have bought uses time-series betas. Why are you different?"** | BFRE's exposures are **observed characteristics**, so they update the day the company changes: p.2, a returns-only model incorporates a change in operating activities, a corporate action or a capital-structure change "only gradually", while a fundamental model reflects it "immediately". p.24: estimation is "a series of cross-sectional regressions". The rival is named in the paper — STORM, Aladdin's existing equity risk approach, which builds an asset-by-asset covariance matrix from asset returns alone (p.2); BFRE, by contrast, "imposes far more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of factors, which capture the most important sources of asset return commonality" (p.2, verbatim) | "Cross-sectional is more modern." "Betas are backward-looking." |
| **"So your exposure moves with the price. You are forecasting risk with the thing you are forecasting."** | Concede it, then produce the paper's own exhibit against itself: AOL's market-capitalisation substyle exposure rose sharply through 1998–9 "following strong price performance" while its total-sales substyle stayed far below (Figure 1.6, p.13, values `[APPROX]`). The paper's answer is multiple substyles from balance-sheet, market and analyst-estimate data (p.13) rather than one price-driven measure — a mitigation, not a cure | "Standardisation handles that." "Everyone has that problem." |
| **"How many regressions a day, and what is the World model doing differently?"** | Daily for country and regional models, **weekly** for the World model (p.24); daily factor returns for all models from **March 1996** (p.3, p.27). And: the paper gives **no justification** for the weekly choice — a coarser series feeding the same `F` | Guessing a cadence. Any number not on p.24 or p.3 |

---

#### L8 ★ — THE WEATHER MAP  *(graduate-level: say so at the top of the round)*

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Your default uses 104 weeks. How many factors are in the North America model?"** | **The paper states no total for any model** — that absence is the first half of the finding. The second half is that a *lower bound* for NAMR can be assembled from what is printed, and a Tier 4 answer assembles it rather than shrugging: 1 market (p.4) + 12 styles (Table 1.2, p.10 — 13 rows, Market plus 12) + 54 core industries (Table 1.5, p.57, *rows counted by the transcriber; the page prints no total*) + ~2 core countries (US, Canada — p.4 names Canadian stocks) + ~2 currencies (p.6, assigned from the country exposures) ≈ **71**. So `K ≈ 71` against `T = 104`: **NAMR's WKL matrix is not rank-deficient, and a GM who claims it is will be caught by a player with a calculator.** Say the count, then say it is a floor, then move to the two arguments that survive it (next row) | Any specific factor count offered as *the paper's*. The 71 is **ours**, assembled from two tables; presenting it as printed is the exact fabrication the rules forbid |
| ↳ *follow-up inside objection 1, not a fourth objection:* **"So your matrix is fine, then. 104 beats 71."** | The two arguments that survive, both **INFER**, both ours, both flagged as such. **(1) The half-life throws most of the sample away.** Weights are `λᵗ` with `λ = 0.5^(1/26) ≈ 0.9737`; the effective sample size `(Σw)²/Σw²` over 104 weeks is **≈ 66** — *below* the ≈71 factors. The oldest week carries `0.5⁴ = 1/16` of the newest week's weight. Show the sum; it is one line of arithmetic and it is Victory Condition 1 in miniature. (For contrast, the daily specific-risk model in Table 1.3 — 125-day half-life over 375 days — gives an effective **≈ 281 of 375**, which is gentle.) **(2) Even at full weight it is thinly determined.** `F` carries `K(K+1)/2 = 2,556` distinct entries for `K = 71`, estimated from `104 × 71 = 7,384` numbers: under **3** observations per estimated parameter, under **2** on the effective count. The paper reports no condition number, no smallest eigenvalue and no shrinkage of `F` | "It's still not enough data." (No mechanism, no number.) Reasserting rank-deficiency after the count has been done |
| **"If your matrix is rank-deficient, tell me what happens on my book."** | First the honest scope: **literal** rank deficiency needs `K > T`, and the model where that is near-certain is **WRLD** — 49 industry rows in Table 1.11 (p.61, transcriber's count) plus styles plus a country block spanning "the superset of all assets in the regional and country models" across **87 countries** of coverage (p.2, p.3), plus currencies mapped from those countries (p.6), against the same 104 weeks (p.27) and *weekly* regressions (p.24). **But the paper never prints that count**, so this is an inference about an unprinted number: say "it follows that", never "the paper says". Then the consequence: near-null directions are scored at or near zero risk; an optimiser searching for low risk finds them and loads them, so risk is understated precisely where the book concentrates. **INFER throughout** — the paper never confronts rank, and this is the game's argument, not BlackRock's | "The matrix would be unstable." "You'd get numerical problems." Asserting a WRLD factor count as printed |
| **"Then shrink it. What does shrinkage cost, and what are you shrinking towards?"** | Shrinkage trades bias for variance and is meaningless without saying **towards what** and **by how much**. BFRE's only shrinkage in the paper is p.36's thin country/industry correction — "adding a **Bayesian prior**, which in essence diverts the estimated country/industry return away from the sample factor return and towards a theoretical prior" — which shrinks a **factor return**, not `F`, and whose **form, strength and parameter are not specified**. LASSO, LARS, Group Lasso and Ridge appear only on p.8, as alternatives BFRE **did not adopt**. And the `F` methodology itself is deferred: "Model users are referred to the BRS Covariance Matrix Estimation documentation" (p.27) | "Shrinkage makes it stable." "You'd use Ledoit–Wolf." (Not in this paper — say so if you use it.) |

---

#### L9 — THE PRIVATE DRAMA

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Is `Δ` diagonal? Yes or no."** | "In the textbook equation, yes; in the shipped model, no — and those are two different objects, not a contradiction." p.24's "a diagonal matrix of asset specific risk forecasts" is introduced by "**In general** a multi-factor model decomposes asset returns as follows" — the generic form. p.27 says what BFRE builds: a vector of specific risk forecasts **plus** "a sparsely populated unit diagonal matrix containing non-zero, off-diagonal specific return correlations", and p.28 devotes a subsection to it. The player must then land the real point — separate what least squares **guarantees** (`Σx·e = 0` per column) from what BFRE **assumes**, and name the assumption that is actually load-bearing: the **scope** of those off-diagonals (objection 3) | "It's diagonal by assumption." (Half true.) **"They contradict themselves three pages apart."** — this is `gm/CRITIQUE.md` **CS-3**, a named cheap shot. Do not let the player leave the level holding it, and do not reward it |
| **"Give me the direction of the error and the kind of book it hits."** | p.28, verbatim: ignoring the correlation "would lead to **under (or over) prediction of specific risk in a long-only (long-short) portfolio context**". Backed by their own arithmetic — two half-weights at 20% specific risk each: a purely diagonal `Δ` gives `0.2 × √0.5 ≈ 14.1%`, the truth when the two are one event is `20%`, an understatement of ≈**29%** of the true number. And the scope, unprompted: BFRE *does* correct this for related listings of one company (p.28); it does **not** correct it across companies | "It would be wrong in some cases." "You'd under-diversify." Claiming BFRE understates the ADR book — it does not; that is the case p.28 fixes |
| **"Different companies, though. You assume zero correlation there. Defend it."** | The paper's justification is literally "in-line with standard modelling practice" (p.28), and the assumption is listed as an assumption on p.30 ("specific returns from different issuers are unrelated and have zero correlation"). The real defence is structural: anything genuinely common **should have been a factor** — p.24, "In a well-specified model, the prescribed factors will capture all sources of commonality in asset returns" — and the paper shows the test failing and being fixed: before a small-cap factor existed, deciles 9 and 10 were **the only two bars above the printed 10% line**, and both fall far below it afterwards (Figure 1.10, p.16). **Cite the crossing of the line, which the chart draws, not the heights, which it does not print** — the measured values are ≈10.8% and ≈21.1% falling to ≈2.1% and ≈3.4%, `[APPROX — ±0.5pp, pixel-measured]`, and they are only for use when a player asks how far above | "Specific means specific." "By definition they're independent." Quoting 10.8% or 21.1% as printed figures |

---

#### L10 — THE ASSEMBLY

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Your factor risk and your specific risk do not add up to your total. Explain that before we go further."** | **Variances** add; volatilities do not. Total is `√(factor variance + specific variance)`, and the p.35 pie splits **risk contributions**, not volatilities — which is why 50 + 25 + 14 + 6 + 4 + 1 reaches 100 while the square roots would not | "Risk isn't additive." "There's a correlation term." (There is not, under the model's own assumption — p.30: factor returns have zero correlation with specific returns.) |
| **"Which matrix is transposed, and why? Get it wrong and the answer is still a number."** | Reads `XFXᵀ` as a sentence with dimensions checked at each step: `Xᵀ` turns holdings into the portfolio's factor exposures; `F` turns exposures into how those bets move together; `X` carries the answer back to assets; the result is a variance in percent-squared. p.24 lists the ingredients: holdings, portfolio-level exposures "aggregated from the asset level", `F`, and specific risk forecasts | "You transpose to make the dimensions work." |
| **"Your market exposure is 1.0 and your beta is 1.02. Which is which, and why aren't they the same number?"** | p.4 warns explicitly: "The market factor exposure of a portfolio **should not be confused with** its market beta." Exposure is the fraction of portfolio %NAV invested in equities (fn 3: plus delta-adjusted derivative exposure); beta must be computed from the factor exposures of portfolio and index together with the factor covariance matrix. The paper's example report shows both at once: Portfolio Beta **1.02** (p.35 banner, read directly). **Never** attribute the beta formula in the p.4 margin to BlackRock — it is a reader's handwritten annotation | "They're the same thing when you're fully invested." Or quoting the margin formula as the paper's |

---

#### L11 — THE DESK

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"I hold fifteen names across six countries. Tell me why that isn't diversified."** *(The PM's book is invented and the fifteen is arbitrary. **Do not confuse it with p.35's "Top Asset Contributions" panel, which has exactly 15 bars because it is a top-N chart — the report never states how many holdings that portfolio has. Never say "the paper's 15-stock portfolio".**)* | Answers with the model, not with intuition. On the paper's own example — a European equity portfolio, EMEA model — Active Risk is **2.99%** and the block split is Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec **1%** `[INFERRED]` (p.35, pie read directly; banner digit `2.99` has a soft middle digit — 2.89 not fully excluded). p.34 states it in prose: "the Active Risk is split equally between common factors and stock specific sources". And one tilt does most of the common half: **active** exposures of Volatility ≈ +0.42 sd, Momentum ≈ +0.38 sd `[APPROX — pixel-measured, ±10%]`. Diversifying **names** does not diversify a shared **tilt** | "Fifteen names isn't many." "You're concentrated in Europe." (True, unquantified, and not from the model.) |
| **"My biggest position is not your biggest risk contributor. One of us is wrong."** | Neither: exposure and contribution are different objects, and the report plots them on **two different axes** for exactly that reason. Every dot on p.35 is an **active** exposure (portfolio − benchmark), which is why the style panel's Market dot sits at ≈0.0 in the same frame as a Portfolio Beta of 1.02 — say that before a player reads it as "no market exposure", which is the confusion p.4 warns about. p.35: Emerging carries active exposure ≈ −0.10 sd and contributes ≈ 0% of active risk; the United Kingdom is both the largest active country exposure (≈ −10% of NAV) and the largest country contribution (≈2.4%); the FX panel shows a pair at roughly −10% of NAV with a **positive** risk contribution — a short adding risk. All `[APPROX — pixel measurements, ±10%]` | "Risk isn't intuitive." "The optimiser knows." "The report shows zero market exposure." |
| **"Show me the arithmetic of a contribution. Where is it in the paper?"** | Derives the nudge version — how much total risk changes when a little more of this position is added, multiplied by the position — and then says plainly: **the paper contains no formula for marginal contribution and never uses the term.** "Contribution" appears as a chart axis label on p.35 and as prose on p.34, and nowhere else. The mathematics here is ours; only the output format is citable | Citing a formula to the paper. That is an automatic fail — it is the fabrication the audit already caught once |

---

#### L12 ★ — THE CRITIQUE

Run the full set from `gm/CRITIQUE.md` §9. These three are the spine; the scoring is §10 of that file
(Tier 4 on **both** sides, or the level is not passed).

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Show me one bias statistic. One number."** | Concedes the Model Testing chapter prints **no values, no pass/fail criteria and no summary results** (p.32, p.33), and that the evidence is deferred to reference [27], described on p.33 as "available on request" and listed in the bibliography on p.65 as "**forthcoming**" — which cannot both be true. Then defends properly: the genre is client model documentation, not a research paper; the ongoing surveillance **is** specified precisely — bias statistics on a rolling window of 12 monthly standardised returns flagged at a 95% confidence interval, and 99% 1-day VaR violations over 252 days, justified by UCITS guidelines and Kupiec (1995), benchmarked against STORM (p.38) — and the test portfolio set is enumerated (p.32–33). Then concedes that none of that justifies printing zero values | "It's BlackRock, they test everything." "The results are confidential." (Then why "available on request"?) |
| **"You tested more than two hundred candidates at two sigma and corrected for nothing."** | All four elements or the attack is incomplete: N ≥ 200 candidate substyles (p.10); "200+" with each horizon variant counted separately (p.55); \|t\| > 2 as the significance bar (p.8); no multiple-testing correction stated anywhere (p.55) — **plus** the Random Substyle sitting in Table 1.4 (p.56), whose score is never reported. Then the author's defence: the procedure is recursive and conditional, each candidate tested against the residuals of the model built so far (1.3)–(1.6); the statistic is a **persistence** proportion, not a one-shot p-value; the stopping rule is 10–15% (p.12); results are checked on five-year sub-samples (p.8). Then the concession: none of those is a multiple-comparison correction, and sub-samples are more chances, not fewer | "They probably corrected for it." "Everyone data-mines." Or leading with a typo instead of this |
| **"Your model says investors overreact at one month and underreact at eleven. Which is it?"** | Both stories are in the paper and they are adjacent: reversal is attributed to "market investors **overreacting** to stock information in the near-term" (p.16); momentum to "market investors systematically **underreacting** to newly available company information" (p.17). The two are engineered not to overlap — momentum is the previous 11 months with a one-month lag, explicitly "to exclude the reversal effect" (**quote: p.17**), and reversal (1.18) is exactly the excluded month (the two constructions are (1.17) and (1.18) on p.44; the phrase itself is not printed there). The honest defence is that both factors are kept for **explanatory power**, and the psychology is decoration that no result in the paper could falsify. Same class: the VIX is conceded to be only "a **first approximation**" to the risk-on/risk-off paradigm (p.23) | "Behavioural finance explains both." "Different horizons, different investors." (Offered without noticing that this is unfalsifiable, which is the charge.) |

---

#### ★ THE REBUILD

Not an interrogation in the same sense — the player has already been promoted. Three questions asked
**after** they hand over the rebuilt model, to certify Victory Condition 4.

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Pick any exposure in your `X` and trace it to a raw number."** | The full chain without notes: raw item → the transformation → standardisation to weighted mean zero and equal-weighted sd one, capped at ±3 (p.39) → the substyle weight inside its style (pp.40–41) → the column of `X`. Any link they cannot name is the level to re-open | "It's a z-score of the raw data." |
| **"Your risk number is 12%. Convince me it is not 6% or 24%."** | Runs the sanity check unprompted: the split between common-factor and specific risk. The one comparison available is p.35's worked example — 50/50, with Style 25% and Industry 14% of **active** risk on **one** European equity portfolio (p.34). It is an order-of-magnitude sanity check, **not a target**: a different book on a different model would split differently, and the player must say so rather than tuning to 50/50. What the check does catch: a rebuild at 95% specific has an `X` explaining nothing; at 95% common the factors have eaten the idiosyncratic noise. Neither extreme is caught by any diagnostic the paper prints, because the Model Testing chapter prints no values at all (pp.32–33) | "The maths is right, so the number is right." Tuning the rebuild until it hits 50/50 |
| **"What did you assume that the paper also assumes, and what did you assume that it does not?"** | Separates the two lists cleanly. Shared: `Δ` treated as diagonal, factor returns uncorrelated with specific returns, specific returns of different issuers uncorrelated (p.24, p.30). Theirs alone: whatever they chose for the covariance estimator, the weighting, the window — because p.27 defers the `F` methodology entirely to an external BRS document. That inventory **is** Victory Condition 3 | "I followed the paper." (They cannot have — five of the choices are not in it.) |

---

## 9. THE RUNNING STATE — what you keep between sessions

The save file (`saves/SAVE_TEMPLATE.md`) can only be filled in honestly if you have been keeping the
state **live**. Reconstructing it from memory at the end of a session is how a ladder position drifts
upward by one tier per session until the player fails a boss round they were recorded as having
passed.

### 9.1 The live tally — keep this open during play

Six things, updated as they happen, not at the end.

| Keep | Update when | Why it cannot wait |
|---|---|---|
| **bps ledger**: every award and deduction with its one-word reason | At the moment it happens | The reason is the audit trail. "−30" with no reason is an untraced number, which is the offence you dock the player for |
| **Ladder moves**: concept, old tier → new tier, and the *evidence* | Whenever a tier changes | "Tier 4" with no evidence is an assertion. Record which of the six markers (§6.2) you saw |
| **Analogy log**: domain, concept, LANDED or REJECTED | The moment you can tell | A rejected analogy re-used is the failure the rules single out (§8, NEVER REPEAT A FAILED FRAMING). `gm/ANALOGIES.md` §2 is the burn ledger |
| **Open questions**: anything the player asked that you did not fully answer | Immediately, verbatim | These are the highest-value openings for the next session, and the fastest way to lose trust if dropped |
| **Anchors used**: page numbers you cited this session | As you cite them | So you can vary the exhibits, and so a wrong citation can be traced and corrected |
| **Uncertainty carried**: every `[APPROX]` / `[UNREADABLE]` / `[INFERRED]` figure you put on the table | As you say it | If the player later quotes it as printed, you must know that you flagged it |

### 9.2 The close-out — five minutes, in this order

1. **Reconcile the bps ledger.** Sum it. Do not round.
2. **Re-read the ladder moves and demote anything you cannot evidence.** If you wrote Tier 4 and
   cannot name which marker you saw, it is Tier 3. Always resolve downward.
3. **Confirm every analogy that landed actually landed** — did the player use it back at you,
   unprompted, in their own words? If not, it is unconfirmed, not landed (Rules §8, CONFIRM
   ANALOGIES LANDED).
4. **Copy the open questions across verbatim.** Do not paraphrase them into things you know how to
   answer.
5. **Write the four victory-condition lines against the evidence standard in §9.4** — not against
   your impression.
6. **Write one Next move.** One. A list of five is a list of none.

### 9.3 Filling each save-file field honestly

| Field | Fill it with | Dishonest version — the thing to avoid |
|---|---|---|
| **Rank** | The rank earned by the last **promotion gate** passed (§5), never by bps | Promoting because the player has been working hard |
| **bps** | The reconciled total, including negatives | A tidied number, or a floor at zero |
| **Levels cleared** | Only levels whose boss round was **passed on all three columns** (§5.1) | Levels "basically done". If a boss round is outstanding, the level is not cleared |
| **Current level** | The level in progress, plus the round type you were mid-way through | "Level 8-ish" |
| **Boss rounds passed / failed** | Both lists, with the failed ones naming **which column failed** | Recording only passes. The failures are the map of where to re-attack |
| **Ladder positions** | One line per concept: `concept → tier`, plus the evidence marker for anything at tier 4+ | A tier with no evidence. A concept list that only grows |
| **Analogies that LANDED** | Domain + concept, only where the player used it back unprompted | Anything you thought was a good analogy |
| **Analogies REJECTED** | Domain + concept + one word on how it failed | Leaving it out because you might want to reuse it. That is precisely why it must be in |
| **Open questions** | Verbatim, with the level at which they arose | Dropping the ones that are hard |
| **Wiki test** | Which questions they have actually answered **from structure**, and which parts of the model have never been probed | "Good progress" |
| **Passing test** | Named tells still present (`gm/VOCAB.md` TELL rows) and terms currently **confiscated** under §4.2 | A general impression of fluency |
| **Origin test** | The list of formulas derived from nothing, and the list still outstanding — including the ones the **paper** does not derive either (standard error, squared loss, `Σx·e = 0`, marginal contribution) | Counting a formula they can recall as one they can derive |
| **Rebuild test** | Which of the eight rebuild steps (`gm/LEVEL_ANCHORS.md` §16) they can do unaided, one line each | A single percentage |
| **Next move** | One concrete opening line for the next session | "Continue Level 8" |

### 9.4 Evidence standards for the four victory conditions

Track them visibly, every session (Rules §3). These are the bars.

| Condition | Counts as progress | Does **not** count |
|---|---|---|
| **1. Wiki test** | Answers a question you have never asked before, about a part of the model they did not build this session, **from structure**, and produces the number's origin when asked | Answering a question you asked last session. Answering correctly without being able to trace the number |
| **2. Passing test** | Uses a term correctly, unprompted, in a *new* situation, and does not use any term they cannot define. Register correct: says "Active Risk", not "tracking error", when talking about a BFRE report | Correct definitions on demand. Correct vocabulary in a sentence you supplied the frame for |
| **3. Origin test** | Derives from nothing, including a step textbooks skip. Additionally: knows which formulas the **paper itself** never derives, and says so unprompted | Reproducing a derivation you walked them through in the same session |
| **4. Rebuild test** | Executes a step of the rebuild on **data they have not seen**, unaided and unprompted, and sanity-checks their own output | Doing it again on the level's dataset. Doing it with the anchor file open |

### 9.5 The session-open ritual — three minutes

1. **Read the save file out loud to yourself**, especially REJECTED analogies and open questions.
2. **Answer one open question first**, before any new material. It repays trust and it is a free
   warm-up.
3. **Re-verify one earlier concept at random** with its diagnostic question from §7. Tiers decay
   between sessions; a Tier 4 that has decayed to Tier 3 must be found now, not at a boss round.
4. **Do not re-explain anything they already hold.** If step 3 passes, move on immediately.

### 9.6 THE FIRST SESSION — there is no save file, and the opening is scripted

Rules §11 specifies the opening move and it is the one part of the game you do not improvise. Four
beats, in this order, and **do not ask the player if they are ready** (Rules §11, last line).

1. **Introduce the Risk Desk in three sentences.** Three. Not a paragraph. They are a new hire at a
   risk-model shop; the model is locked in modules; each level is a desk task and they earn the next
   piece by rebuilding the one before it.
2. **State the four victory conditions** (Rules §3) — Wiki, Passing, Origin, Rebuild — and say that
   you will track all four **visibly**, every session. That promise is why §9.4 exists; make it and
   then keep it, in writing, at every close-out.
3. **Run the 60-second cold open before teaching anything.** Five stocks, one characteristic, one
   return, and one question: *what single number best turns the characteristic into the return, and
   how did you get it?* The dataset is `datasets/level0.md` — AXL/BRN/CHR/DLT/EMK, `b = 2` exactly.
   **Let them fail.** The three shortcuts a beginner reaches for return 2.0, 4.0 and 2.7708; the
   per-stock ratios are 1.3333, 4.0000, 4.0000 and 1.7500 and disagree wildly, which is the hook.
   Do not rescue, do not hint, and do not name the method. The failure *is* Level 0's opening.
4. **Then begin Level 0.** No lecture in between.

Vocabulary discipline starts at beat 1, not at Level 1. In the cold open the characteristic is a
"cheapness score" and nothing else — *exposure*, *factor*, *regression* and *residual* are all still
locked (§1). If the player supplies one of those words themselves, that is a gift: ask them to define
it, and you have your first ladder reading before the game has started.

The three things that go wrong on beat 3, every time: explaining the loss function before they have
guessed (which removes the failure the level is built on), accepting "I'd fit a line" as an answer
(that is a method name, not a number — ask for the number), and treating a wrong guess as a problem.
A wrong guess with an honest reason is worth 0 bps and is exactly what you wanted.

---

## 10. THE CRIB — one screen

**Opening a new concept:** story first, no mathematics, finished, then mapped, then landed on the page
it changes (Rules §8). *Then* the round. **First session ever:** three sentences → four victory
conditions → the 60-second cold open, let them fail → Level 0. Never ask if they are ready (§9.6).

**Rotation:** open with A or C, never arithmetic → compute → B or D → fire F mid-task, unannounced →
close with E. Never two of a type in a row. B needs an invariant; D at least once per level.
**L2's boss is B+E**, not E: the rules make it the sabotage round.

**When the "why" chain ends:** say so — *"that is the bottom; it is a choice, not a consequence"* — and
name which kind: forced (`Σx·e = 0`), defined (exposure zero = market average, p.10/p.39), chosen
(squared loss, (1.10)), conventional (different-issuer independence, p.28) or simply unjustified (26
weeks, 104 weeks, ±3). Full list §7.4. Never use bedrock as a way to stop early.

**bps:** derivation **+40** · computation **+10** · Round A with correct reason **+15** · sabotage by
structural check **+30** · build-the-shape **+25** · teach-back **+30** · one objection held **+25** ·
boss round **+100** · demanding your origin **+20** · right answer with wrong reasoning **+0, always**.

**Deductions:** hand-waving **−20** (**−40** second time in a round) · undefined term **−25** and the
term is confiscated · untraced number **−30**, the most expensive in the game. Announce each one, with
the reason, at the moment it happens.

**Gates:** L4 → Analyst · L8 → Researcher · L12 → Model Owner · ★ REBUILD → Author. Every other boss
round advances the level but not the rank. bps never promote and never block.

**Tier 3 → 4:** the assumption question, the counterexample question, the consequence question — all
three, no vocabulary supplied. The deepest single marker: can they separate what the arithmetic
**forces** (`Σx·e = 0`) from what the authors **chose** ((1.10), p.26) from what the paper **assumes
by convention and never tests** (specific returns of *different companies* uncorrelated, "in-line with
standard modelling practice", p.28, p.30)? Not "p.24 says diagonal and p.27 says not" — that is
CS-3, a cheap shot: p.24 is the generic form, p.27 is the shipped one.

**When lost:** stop → ask the one diagnostic question (§7) → read the answer → drop to the named level
→ rebuild with a *different* analogy. Say the frustration line once. Never elaborate the failed version.

**The five pages that are the whole model:** p.24 (1.7)(1.8) · p.25 (1.9) · p.26 (1.10)(1.11) ·
p.27–28 the six parameters — March 1996, 104 weeks, 26 weeks, 125 days, 375 days, 10 days.

**Never invent:** a **printed** factor count · a VIF value or threshold · a bias-statistic value or
pass mark · a **model** R² · a standard-error page · a marginal-contribution formula · an eigenvalue
anywhere · the p.4 beta formula as BlackRock's. When the player asks for one of these, the correct
answer is *"the paper does not say, and that is a finding."*

**Three of those need a footnote, and the footnote is what keeps you honest at the table:**
- **Factor count.** The paper states no total for any model. A NAMR *floor* can still be assembled from
  printed tables — ≈71 (§8.2 L8) — and assembling it is Tier 4. Saying "≈71" is fine; saying "the
  paper says 71" is the fabrication.
- **R².** The paper prints exactly one: **91%**, on p.4, for the regression of daily S&P 500 excess
  returns on daily NAMR market factor returns. That is a fit between two return series, **not** a model
  explanatory-power diagnostic. p.32 defines R² in words and prints no value. So "the paper prints no
  R²" is false; "the paper prints no model R²" is true. Say the second.
- **Standard error / degrees of freedom.** Neither *phrase* appears in 65 pages. Newey–West [26] does
  (p.27, p.28, p.65) — but for serial correlation in the *risk* estimates, not for the t-statistics.
