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

Three standing traps, all of which have already caught someone:

1. The portfolio-beta formula on p.4 is a **reader's handwritten margin annotation**, not BlackRock's
   text. Never attribute it.
2. Every bar height and dot position in Figure 1.18 (p.35) is a pixel measurement, ±10%. The **axis
   tick labels** and the **pie percentages** are read directly and are reliable — except `Act Sec 1%`,
   which is `[INFERRED]` from the six slices summing to 100.
3. `notes/` contains the transcriber's commentary as well as the paper's words. "Orthogonal" (p.52),
   "coefficient of determination" (p.32), "placebo" (p.56) and every "(my count)" total are **the
   transcriber's**, not the paper's.

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
| Frisch–Waugh–Lovell | L4 — **graduate** | GAP — the mechanism is on pp.7, 10, 12, 52; the name never appears |
| intercept, centering, z-score | L5 | PAPER — p.26 ("three intercept terms"), p.10, p.39 |
| t-statistic, significance | L6 | PAPER — \|t\| > 2, p.8 |
| standard error, degrees of freedom | L6 | **GAP — neither phrase appears anywhere in 65 pages** |
| cross-sectional regression | L7 | PAPER — p.24, and pp.3, 8, 30, 32 |
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
| Frisch–Waugh–Lovell | L4 | "Graduate-level. You are getting the mechanism without the theorem, which is the right trade. The paper uses it four times and never names it." |
| Standard error from scratch | L6 | "Most textbooks skip this derivation. We are not skipping it — it is Victory Condition 3. And note: this paper never derives it either." |
| Eigen-decomposition | L8 | "Graduate-level, and the paper never uses it. We are borrowing a lens to see why a covariance matrix can be broken." |
| Shrinkage / bias–variance | L8 boss | "Graduate-level. The paper's version (p.36, a Bayesian prior on thin factor returns) is not the textbook's version, and we will do both." |
| Euler decomposition of risk | L11 | "The theorem that makes contributions sum to the total is beyond scope. The nudge argument gets you there without it." |

---

## 3. THE SIX ROUND TYPES — rotation

### 3.1 The rotation rules

1. **Never open a level with arithmetic.** Every level opens with **A** (predict-then-reveal) or
   **C** (build-the-shape). The player commits before they compute, or they are not learning, they
   are following.
2. **Never two of the same type back to back** inside a level.
3. **Every level closes with E.** That is the boss round. There is no other way out of a level.
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
A or C  →  the computation  →  B or D  →  (F fired mid-task, unannounced)  →  E boss
 commit      turn the handle     audit or explain          the word              survive
```

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
| 2 | A — will `Σe` be zero? | verify `Σx·e = 0` | **B — the sabotage is the boss** | "orthogonal"/"neutral" (p.5) | E |
| 3 | C — how many conditions for two columns? | 2×2 in fractions | B — corrupt one of two conditions | "design matrix" (outside word) | E |
| 4 | A — predict both coefficients before fitting | the collided fit | D — explain to a PM why the split moved | "multicollinearity" (p.32), "VIF" | E |
| 5 | A — shift every `x` by 100, predict | the pivot | B — corrupt the centering | "intercept", "z-score", "standardised" | E |
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
| **Interrogation: boss round passed** (all three held, see §6) | **+100** | This is the promotion currency. |
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
| Quoting a pixel-measured chart value as a printed number | −15 | The player-side version of your own rule. Figures 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.12, 1.14, 1.17, 1.18. |
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
| 8 ★ | Covariance from fewer months than factors | There exists a factor combination the estimate scores at **exactly zero** risk | An optimiser finds that combination and loads it — risk understated exactly where the book concentrates (**INFER**, flag it) | p.27: WKL = 104 weeks, 26-week half-life, daily returns from March 1996; method **deferred** to BRS documentation. **GAPS**: no eigenvalue, no factor count, no rank discussion, no shrinkage of `F` |
| 9 | Diagonal assumption fails; risk too low where it hurts | A concrete two-asset scenario, computed both ways | **Too low** on a long-only book, too high on a long-short one | p.28, verbatim: ignoring the correlation "would lead to under (or over) prediction of specific risk in a long-only (long-short) portfolio context." Also p.24 ("a diagonal matrix") vs p.27 (it is not) |
| 10 | 3-stock portfolio risk by hand, decomposed | Every multiplication read as a sentence; variances add, volatilities do not | What a dropped `Δ` does (single-stock portfolio's risk = its factor risk) and what dropped off-diagonals of `F` do (offsetting bets stop cancelling) | (1.7) and (1.8), p.24, one line apart. The `D`/`Δ` letter swap. p.4: exposure ≠ beta |
| 11 | The PM who insists they are diversified | Contribution ≠ exposure, demonstrated with the model's own numbers | Which position to cut first, and by what criterion | p.34/p.35: Active Risk decomposed by block; Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec **1%** `[INFERRED]`. **GAP**: no marginal-contribution formula in the paper |
| 12 ★ | Defend as author, attack as rival | Both sides at Tier 4 (`gm/CRITIQUE.md` §10). One-sided fails | Ranks the weaknesses and says which one goes into the meeting and which stays out | p.33 ([27] "available on request") vs p.65 (bibliography: "**forthcoming**"); N ≥ 200 (p.10), 200+ (p.55), \|t\| > 2 (p.8), Random Substyle (p.56, Table 1.4) |
| ★ | THE REBUILD | The whole model on fresh data, alone, no reference material | Sanity-checks their own output: the common/specific split | p.35's worked example is 50/50. A rebuild at 95% specific has an `X` that explains nothing; 95% common has factors that ate the noise |

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
6. **Distinguishes what is forced from what is chosen.** The single sharpest instrument in this game:
   `Σx·e = 0` is forced by the arithmetic; (1.10) on p.26 is chosen by the authors; `Δ` being called
   diagonal on p.24 is an assumption the same authors walk back on p.27. A player who tracks that
   distinction is Tier 4. One who does not is Tier 3 no matter how good the algebra is.

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

| They answer | The broken rung | Drop to |
|---|---|---|
| "True — with fewer observations than factors there is always a combination that was flat in every month observed, and the estimate reads that as zero risk" | Nothing broken; this is Tier 4 material | Return. Then the consequence: an optimiser **finds** that combination (INFER — the paper never confronts this) |
| "False — risk can't be zero" | Intuition with no mechanism | Stay at L8. Build the smallest case by hand: two factors, **one** observation. Every combination that was flat that day is scored at zero |
| "True, but I can't say why" | Tier 1. They have heard this somewhere | Stay at L8 and build it from 2 factors up |
| "You'd need more data" | True and evasive — it does not say what breaks | Stay at L8; the question is what the estimate **claims**, not what would fix it |
| Answers correctly using eigenvalues, unprompted | Tier 4 plus. Reward it — and note the **GAP**: no eigenvalue, eigenvector or principal component anywhere in the 65 pages | Return |

---

#### L9 — THE PRIVATE DRAMA

> **"A book holds two things only: an ADR and the ordinary share of the same company, half and half. The model gives each a specific risk of 20%. What does the model say the portfolio's specific risk is — and what is it really?"**

| They answer | The broken rung | Drop to |
|---|---|---|
| "Model says ≈14.1%; really 20%, because the two specific returns are the same event" | Nothing broken. `0.2 × √0.5 = 14.14%` versus `20%` — the model understates by about 30% of the true number | Return, then hand them p.28's own sentence |
| "The model says 20%" | They have not got the aggregation — they are averaging risks rather than combining them | L10 preview, on two assets only. Variances add, volatilities do not |
| "It's too high" | **Sign error on the direction**, which is the whole level. Dock and stop | Stay at L9. p.28: ignoring the correlation "would lead to **under** (or over) prediction of specific risk in a **long-only** (long-short) portfolio context" |
| "They'd be correlated so it's more complicated" | Right instinct, no number | Stay at L9 and make them compute both cases |
| "That's what `Δ` being diagonal means" | Tier 3–4. Ask the follow-up: does the paper actually say `Δ` is diagonal? | Return. p.24 says "a diagonal matrix"; p.27 says the specific covariance carries **non-zero off-diagonal** correlations. Three pages apart |

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
| "A — it's the bigger position" | Exposure and contribution have collapsed into one idea. This is the level's entire content | Stay at L11 with p.35: Emerging carries exposure ≈ **−0.10 sd** and contributes ≈ **0%** of active risk `[APPROX — pixel-measured, ±10%]`. The report plots the two on **two different axes** for exactly this reason |
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
| Attacks the scan — missing values, unreadable figures | They are attacking `notes/`, not the paper. Never allowed | Restate the rule and re-ask. This is an automatic fail if repeated |

### 7.3 When the diagnostic itself fails

If the diagnostic question is also met with silence, the break is **at least two levels down**. Do not
ask a second diagnostic at the same level — go straight to the L0 or L1 question, whichever is nearer,
and rebuild from there. Record in the save file that you did this: the level was passed too early and
its ladder positions are now suspect.
