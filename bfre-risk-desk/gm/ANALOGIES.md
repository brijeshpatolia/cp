# ANALOGY BANK — THE RISK DESK

Game-master reference for `prompt/RISK_DESK.md`. It exists to make two hard rules mechanically
obeyable at speed:

> **ONE STORY FIRST.** Any new concept opens with a single self-contained analogy containing no
> mathematics. Finish the story completely, then map it line by line onto the model.
>
> **NEVER REPEAT A FAILED FRAMING.** Second attempt = new angle. Third attempt = abandon the entire
> domain of the analogy and find another.

That second rule is unusable unless you already have three stocked, from three genuinely different
domains, for every concept. This file is that stock: **16 concepts × 3 analogies = 48**, each with a
domain label you can say out loud ("the mechanics one was rejected — try the courtroom one"), a
line-by-line mapping, the one awkward question that tests whether it landed, and the place it breaks.

**Source of truth:** `notes/` only — the page-indexed transcription of all 65 PDF pages. Every page
citation below was read in `notes/` before being written here. Where the paper contains nothing, the
gap is declared as a gap. Companion files: `gm/LEVEL_ANCHORS.md` (what to point at, level by level)
and `gm/VOCAB.md` (Round F ammunition, the unlock ladder).

---

## §0. HOW TO RUN ONE — the four beats, in order

| Beat | What you do | What you must not do |
|---|---|---|
| **1. STORY** | Tell it whole. No numbers, no symbols, no "imagine a variable". End the story before you say the word "model". | Do not interrupt yourself to explain. Do not name the concept yet. |
| **2. MAP** | Go line by line down the mapping table. Say "the X in the story *is* the Y in the model", not "is like". | Do not skip a row because it seems obvious — the skipped row is where the misconception lives. |
| **3. AWKWARD QUESTION** | Ask it. Wait. This is the test that the analogy landed, not the vocabulary. | Do not accept a right answer with wrong reasoning (`RISK_DESK.md` §8). |
| **4. RETURN TO BFRE** | Name the page, the equation, the factor, and what it changes about a real risk number. Every concept below ends with a ready line. | Never leave an analogy hanging in its own world. |

**The rejection ladder.** Attempt 1 = analogy **A**. Attempt 2 = analogy **B** (new angle *and* new
domain). Attempt 3 = analogy **C** (whole domain family abandoned). If C fails, **stop the level** and
run the Failure Protocol (`RISK_DESK.md` §10) — a third failure is almost never the analogy, it is a
broken rung one step lower down. Diagnose the rung; do not reach for a fourth story.

**When to use "where it breaks".** Not at first telling. Deploy it (a) the moment the player
over-extends the story into a wrong prediction, or (b) deliberately at ladder tier 4 (*Defend*),
because knowing where your own analogy fails is exactly what a hostile CRO probes for.

**Save-file hygiene.** Record by concept-code + domain label, e.g. `C5 courtroom LANDED`,
`C5 audio REJECTED`. That is the format `Analogies that LANDED` / `Analogies REJECTED` expects.

---

## §1. DOMAIN INDEX — the lookup table

Say the domain word, find the analogy. Codes are stable; use them in save files.

| Code | Concept | Level | A | B | C |
|---|---|---|---|---|---|
| **C1** | Why we square the misses | L0 | sport — archery | cooking | medicine — dosing |
| **C2** | The nudge that finds the best dial | L1 | music — tuning | mountaineering — fog | photography — focus |
| **C3** | The balance condition | L2 | mechanics — seesaw | bookkeeping — ledger | farming — fertiliser |
| **C4** | Two dials interacting | L3 | plumbing — shower taps | aviation — trim | painting — colour mixing |
| **C5** | Collinearity and the collision | L4 ⚠ | courtroom — two witnesses | audio — two microphones | carpentry — stacked shims |
| **C6** | The intercept and the pivot | L5 | surveying — the datum | sport — golf par | weighing — the tare button |
| **C7** | Standard error / sampling wobble | L6 | polling | astronomy — seeing | ecology — netting fish |
| **C8** | Degrees of freedom | L6 | party game — announced average | drafting — line through two dots | household budget — last envelope |
| **C9** | Cross-sectional vs time-series | L7 | forestry — one afternoon vs forty years | epidemiology — screening vs cohort | education — class rank vs report card |
| **C10** | Covariance matrix as weather map | L8 | meteorology | traffic — a city's junctions | power grid — coincident peak |
| **C11** | Eigenvalues = directions of most wobble | L8 ⚠ | naval — a ship's roll | tailoring — grain and bias | seismology — the fault axis |
| **C12** | Too few periods, too many factors | L8 boss ⚠ | puzzles — crossword with two clues | linguistics — two sentences of a language | archaeology — a pot from two shards |
| **C13** | Shrinkage | L8 boss ⚠ | sport — the one-innings average | insurance — the village fire rate | cartography — the hurried coastline |
| **C14** | Diagonal `Δ` and what it ignores | L9 | theatre — understudies | horology — two clocks from one shop | structural engineering — one batch of cable |
| **C15** | Assembling the risk equation | L10 | money-changing — the mixed till | pharmacy — compounding | railways — a journey's delay |
| **C16** | Marginal contribution to risk | L11 | canoeing — trim | firefighting — the terrace | music — the choir |

⚠ = **graduate-level material. Say so out loud** (`RISK_DESK.md` §8: BE HONEST ABOUT DIFFICULTY).

---

## §2. DOMAIN-BURN LEDGER

A domain the player has rejected once tends to stay rejected. Check here before reaching.

| Domain family | Used at | If burned, you lose |
|---|---|---|
| **sport** | C1-A (archery), C6-B (golf), C13-A (cricket) | three analogies at three different levels — the biggest single exposure in this file |
| **music / audio** | C2-A (tuning), C5-B (microphones), C16-C (choir) | one at L1, one at L4, one at L11 |
| **health** (medicine / epidemiology / pharmacy) | C1-C, C9-B, C15-B | three, but the labels are distinct enough that rejecting "doctors" rarely burns "chemist" |
| **building / making** (carpentry, plumbing, structural, tailoring, textiles) | C4-A, C5-C, C11-B, C14-C | spread thin; low risk |
| everything else | once each | — |

**Practical rule.** If the player rejects two analogies from the same family in one session, stop
reaching into that family for the rest of the session and note it in the save file.

---

## §3. CITATION CONVENTIONS AND FOUR STANDING WARNINGS

| Tag | Meaning |
|---|---|
| **PAPER** | The paper says this. Quote or close paraphrase, read in `notes/`. |
| **INFER** | The game's inference from what the paper says. At the table: "this follows from…", never "the paper says". |
| **GAP** | The paper does not contain this. Say so out loud. |
| `[APPROX]` | Pixel-measured off an unlabelled chart in the scan. Carry the uncertainty verbatim; never round it into a confident figure. |
| `[UNREADABLE]` / `[INFERRED]` | The scan could not resolve it. Teach with clearly-labelled invented numbers instead. |

Four things that will otherwise bite you mid-story:

1. **Figure 1.3 (p.11) is not `F`.** It is the correlation of *exposures* — the columns of `X`, one
   date, Dec 2013. The "Correlation with Market Factor" column of Table 1.2 (p.10) is the correlation
   of *factor returns*, which is `F` content. Same word, different object. Used in C5, C10, C11.
2. **The portfolio-beta formula on p.4 is a reader's handwritten pen annotation in the margin, not
   printed text.** `notes/` records it as such. Never attribute it to BlackRock. The printed sentence
   only says beta "can instead be computed via the risk factor exposures of the portfolio and market
   index, together with the factor covariance matrix" (PAPER, p.4).
3. **Letter swap.** The game writes `V = X F Xᵀ + D`. The paper (p.24, eq. 1.8) writes
   `Σ = X F Xᵀ + Δ`. Flag it at C15 or the player will think they have found an error.
4. **Every bar height and dot position on Figure 1.18 (p.35) is a pixel measurement, ±10%.** The axis
   tick *labels* and the banner figures are read directly. The pie's "Act Sec 1%" is `[INFERRED]` from
   the other five summing to 99 — the glyph reads 1 or 2. Used heavily in C16.

---
---

# C1 · WHY WE SQUARE THE MISSES

**Unlocks:** L0 (The Miss) · **Difficulty:** ordinary — do not flag it as hard
**Jargon gate:** *residual* and *the miss* are legal from L0. *Specific return* may be **named** at L0
but its machinery waits for L9. **Locked:** loss function, least squares, variance, R², sum of squares.

### BFRE anchor (verified in `notes/`)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| `u` in equation (1.7) `r = X f + u` | p.24 | "`X f` is termed the common factor return and `u` is the asset specific, or idiosyncratic, return." | PAPER |
| One idea under many letters: `u` and `ū` (1.1)/(1.2); `ε` and `ε̃ᵢ` (1.3)/(1.4); `η` and `η̃ᵢ` (1.5)/(1.6); `u` again in (1.7); `ε` again in (1.11) | pp.7–8, 10, 12, 24, 26 | The paper runs its whole factor-selection procedure *on residuals* | PAPER |
| **average squared t-statistic** | p.8 | Computed "to distinguish between factors with t-statistics close to +/- 2 and those that are significantly higher" — the authors reaching for squaring, in their own words, for the player's exact reason | PAPER |
| `R²` defined in words only | p.32 | "the proportion of cross-sectional variation in asset returns explained by the set of common factors in the model." **No formula is printed anywhere in the paper.** | PAPER |
| Specific = **50%** of Active Risk | p.35 (Fig 1.18 pie) | Half of that portfolio's risk number is built out of these misses | PAPER |

**GAP — say it out loud.** The paper never derives or defends squared loss. Zero hits across all 65
pages for "least squares", "sum of squares", "normal equation". Level 0's argument is *ours*; the
paper only inherits the result. That is a good thing to tell the player — it is the first place they
know something the document assumes.

---

### C1-A · SPORT — ARCHERY

**Story.** A club is choosing between two archers for the county team. Both shot a full round
yesterday. The coach's assistant reports the result the way he always does: for each arrow he notes
how far left or right of centre it landed, calls left negative and right positive, and adds them up.
Both archers score zero. The coach walks to the targets. The first archer's arrows are all clustered
in a fist-sized patch dead centre. The second archer's arrows are in two tight groups — half of them
a hand's width off the left edge, half a hand's width off the right edge, none anywhere near the
gold. The assistant's report says these two archers are identical. The coach fires the assistant, and
tells the next assistant to report the size of the patch you would have to cover to hide every hole.

**Map.**

| In the story | In the model |
|---|---|
| one arrow | one stock in this month's cross-section |
| the centre of the target | the return the model predicted for that stock |
| how far left or right the arrow landed | the miss for that stock — later, `u` in (1.7), p.24 |
| the assistant adding signed distances | scoring a fit by the raw sum of misses |
| both archers scoring zero | two completely different models, indistinguishable by that score |
| the second archer's two tight groups | the Level-0 boss round: Desk B's misses of equal size and opposite sign |
| "the size of the patch you'd have to cover" | a score that grows with *size*, not with *cancellation* |
| firing the assistant | why no risk desk on earth reports a raw sum of misses |

**The awkward question.** *"Why not just ignore the signs and add the distances? That already
separates the two archers. What does squaring buy that dropping the minus signs doesn't?"*

- **Landed** sounds like: it does separate them — but it treats one arrow a metre out the same as ten
  arrows a hand's width out, and for a risk model the metre matters more than ten hands. Squaring
  makes the big miss count out of proportion, on purpose.
- **Not landed** sounds like: "because squares are always positive" — true and irrelevant; absolute
  values are also always positive. Dock bps and go to the outlier example in `datasets/level0.md`.

**Where it breaks.** Archery has a real, physical bullseye that exists before the archer shoots. The
model has no such thing — the "centre" is chosen by us, and choosing it is the entire content of L1.
If the player leaves this story believing the prediction is given and only the misses are in play,
they will not understand why `b` has to be *chosen*. Break the story deliberately at the end of L0 by
asking: *who painted the target?*

---

### C1-B · COOKING

**Story.** A caterer runs two kitchens. At the end of the week she reads their seasoning reports. The
first kitchen sent out forty dishes, every one of them very slightly under-salted — nobody complained,
a few people reached for the shaker. The second kitchen also sent out forty dishes: twenty were bland
as boiled paper and twenty were so salty that three diners spat them out and one table walked. Both
kitchens report the same thing: *on average, our seasoning was perfect*. And both are telling the
truth. The caterer closes the second kitchen. She did not close it because its average was wrong. She
closed it because an average that lets a spat-out dish be cancelled by a bland one is not a report
about food.

**Map.**

| In the story | In the model |
|---|---|
| one dish | one stock's return this period |
| the recipe's intended saltiness | the model's prediction for that stock |
| over- or under-salted | the miss, signed |
| "on average, perfect" | the raw sum (or mean) of misses being zero |
| the bland dish cancelling the ruined dish | cancellation masking size — Desk B in the L0 boss round |
| a spat-out dish costing a whole table | one large miss costing far more than several small ones |
| closing the kitchen | rejecting the raw-sum diagnostic outright |
| the caterer's new rule | a score that punishes the ruined dish out of proportion to its number |

**The awkward question.** *"If both kitchens average to perfect, isn't the second one just unlucky
in how the errors happened to fall? Why is one big mistake worse than several small ones — surely a
mistake is a mistake?"*

- **Landed** sounds like: because the consequences are not proportional. Ten slightly bland dishes cost
  ten shakes of salt; one ruined dish costs a table. A risk model's whole job is to say how bad the
  bad case gets, so its scoring has to bend the same way the consequences bend.
- **Not landed** sounds like: "because the second kitchen is less consistent" — that is a restatement,
  not a reason. Push: *consistent in what units, measured how?*

**Where it breaks.** Cooking makes the loss feel like a matter of taste, and a determined player can
argue the caterer is entitled to a different rule. They are — least absolutes *is* a defensible rule
and it picks the median (see `datasets/level0.md`). The story cannot settle which rule is right; it
can only show that the raw sum is not a rule at all. Say that plainly rather than letting the story
pretend to prove more than it does.

---

### C1-C · MEDICINE — DOSING

**Story.** A hospital audits a ward's drug dosing over a month. The pharmacist's summary says the
average dose given was exactly the prescribed dose. The auditor reads the individual records anyway.
Most patients got very close to the right amount. Two got roughly half. One got roughly double, spent
a night in intensive care, and survived. The average is perfect because the double cancelled two
halves. The auditor writes that the ward's dosing is dangerous, and the pharmacist objects that the
numbers say otherwise. The auditor's reply is the whole of the report: *a patient who gets half a dose
is undertreated for a day; a patient who gets a double dose nearly dies. Those two events do not have
the same size, so a summary that lets one cancel the other is measuring the wrong thing.*

**Map.**

| In the story | In the model |
|---|---|
| one patient | one stock |
| the prescribed dose | the model's prediction |
| the dose actually given | what actually happened |
| over- or under-dose | the miss |
| "the average dose was exactly right" | the raw sum of misses being zero |
| half-doses cancelling a double dose | cancellation, again — and this time with a body count |
| the near-death from one double dose | why the score must rise faster than the miss does |
| the auditor's report | choosing a score whose steepness matches the steepness of the harm |
| the ward, not the patient, being audited | the model, not the stock, being judged |

**The awkward question.** *"You have shown that harm from an overdose grows faster than the overdose
does. Does the market actually behave like that — is a large surprise really more than proportionally
damaging to a portfolio, or is that just a nice story about medicine?"*

- **Landed** sounds like: it is a choice we make about the model's job, not a claim about the market.
  We are building a forecaster of how bad things get; we want it more sensitive to big misses, so we
  score it that way. The bedrock here is a design decision, not a fact about the world. (**NAME THE
  BEDROCK** — `RISK_DESK.md` §8.)
- **Not landed** sounds like: "yes, markets have fat tails" — the player has heard a phrase and is
  using it to avoid the question. They cannot define it at L0 and should not be reaching for it.

**Where it breaks.** In medicine there is a right dose, known in advance, written on a chart. Nothing
in the model is known in advance — the "prescription" is itself the thing we are fitting. The story
also implies a moral asymmetry (overdosing is worse than underdosing) that squaring does *not* have:
squaring is perfectly symmetric. If the player concludes "so we punish overprediction more than
underprediction", the analogy has actively misled them and must be corrected on the spot.

---

**RETURN TO BFRE (say this at the end of whichever one landed).**

> "The thing you have been calling *the miss* is the letter `u` in equation (1.7) on page 24. And page
> 8 shows the authors reaching for your exact trick on their own diagnostics — they report the
> **average squared t-statistic**, in their words, 'to distinguish between factors with t-statistics
> close to plus or minus two and those that are significantly higher', precisely so a big score cannot
> be cancelled by a small one. The stake is on page 35: in that sample report, **half of the
> portfolio's Active Risk is Specific** — half the risk number is built out of the spread of these
> misses. A scoring rule that cannot tell a big miss from a cancelling pair sets that half arbitrarily."

---
---

# C2 · THE NUDGE THAT FINDS THE BEST DIAL SETTING

**Unlocks:** L1 (The Dial) · **Difficulty:** ordinary. This is calculus built from slopes, in-game, as
`RISK_DESK.md` §2 requires — do not use the word *derivative*.
**Jargon gate:** *factor return* and *regression weight* become legal at L1. **Locked:** derivative,
minimise, objective function, first-order condition, optimum.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| `f` in (1.7) | p.24 | "`f` : return to each factor" — one number per column per period. The dial setting. | PAPER |
| The first dial BFRE ever turns | p.4 | Market factor: "all equity assets have a **unit exposure** to this factor"; its return is "the cross-sectional average return across all assets in the model estimation". Footnote 2: "Average return based on **regression weights**, i.e. square-root of market capitalisation". | PAPER |
| Why those weights | p.25 | √-market-cap is "a good compromise" between equal weighting (which gives "a poor fit for mega-cap and large-cap securities") and cap weighting ("poorer forecasts for mid-cap and small-cap securities"); "More technically, square-root of market capitalisation **adjusts for heteroskedasticity**…" | PAPER |
| The alternative, dismissed | p.25 fn 14 | Weights of one-over-residual-variance exist, "however, in practice these provide similar results". | PAPER |
| Real dial settings | p.10, Table 1.2 | NAMR, Mar 1996–Dec 2013, annualised: Market **7.0%**, Momentum **5.4%**, Value **3.3%**, Growth **−2.0%**, Reversal **−5.1%**. | PAPER |

**INFER, and flag it as ours:** put p.4 and p.25 together — a column of ones, weighted by
square-root-of-market-cap — and the player's own L1 formula collapses into a weighted average return,
which is exactly what footnote 2 says the market factor return *is*. So the player's first hand
calculation reproduces BFRE's very first factor. The paper does not print that collapse.

---

### C2-A · MUSIC — TUNING A STRING

**Story.** A guitarist tunes the low string by ear against a tuning fork. She turns the peg and
listens: the two notes beat against each other, a slow throb. She turns further; the throbbing speeds
up — wrong way. She turns back past where she started and the throbbing slows, slows, and disappears.
Now she does the thing that actually defines being in tune: she nudges the peg a hair one way, hears
the throb return, nudges a hair the other way, hears it return equally. She is not in tune because the
note sounds right. She is in tune because *both* small moves away from here make it worse, by about the
same amount. That symmetry is the test, and she puts the guitar down.

**Map.**

| In the story | In the model |
|---|---|
| the peg | the single dial `b` — later, `f`, p.24 |
| the pitch of the string | the model's prediction for every stock at once |
| the tuning fork | the actual returns you are trying to match |
| the throbbing | the total badness of the fit at that dial setting |
| turning the peg the wrong way | a setting on the far side of the best one |
| the throb disappearing | the badness reaching its lowest point |
| **nudging a hair each way and hearing it worsen equally** | the defining test: at the best setting, a small move either direction costs the same |
| putting the guitar down | you have found the setting; nothing about the string changed, only the peg |

**The awkward question.** *"Every setting near the right one sounds almost the same. So how does the
nudge ever tell you which is best — doesn't it just tell you that you're roughly there?"*

- **Landed** sounds like: exactly — near the best setting a nudge costs almost nothing, and *that
  flatness is the signal*. Anywhere else, one direction clearly helps and the other clearly hurts. You
  are looking for the one place where neither direction helps.
- **Not landed** sounds like: "you keep turning until it sounds best" — that is the thing being
  defined, used to define itself. Ask for the test a deaf person could run.

**Where it breaks.** A guitar has one string and one peg. The moment L3 arrives with a second column,
tuning-by-ear fails badly as a picture, because two pegs interact (that is C4-A, the shower taps) and
tuning them one at a time does not converge to the right answer. Retire this story at the end of L1
and say you are retiring it.

---

### C2-B · MOUNTAINEERING — THE VALLEY IN FOG

**Story.** A walker is caught on a broad hillside in fog so thick she can see her own boots and
nothing else. She needs to get to the valley floor, and she has no map and no view. So she uses her
feet. She steps a pace forward: uphill. Back, and a pace to the left: downhill, slightly. She keeps
going that way, testing each direction with a single pace, always taking the one that goes down.
Eventually she reaches a place where every direction she tests goes *up*. She has never seen the
valley. She does not know where she is. But she knows she is at the bottom, because there is nowhere
left to go down — and that is the only definition of "bottom" that survives the fog.

**Map.**

| In the story | In the model |
|---|---|
| the hillside | the badness of the fit, as it varies with the dial setting |
| the walker's position | the current dial setting |
| the fog | you cannot see the whole landscape — you only ever get to test one setting at a time |
| taking a single pace to test | nudging the dial a little and recomputing the total badness |
| downhill | the nudge that reduced the badness |
| the valley floor | the best dial setting |
| **every direction now going up** | the stopping condition — this is the whole derivation of L1 |
| never having seen the valley | you never needed a formula first; the formula is what this procedure turns out to be |

**The awkward question.** *"What if she is standing in a dip halfway up the mountain? Every direction
goes up out of a dip too. How would she know?"*

- **Landed** sounds like: she wouldn't — in general this test only finds *a* bottom. Here it happens to
  find *the* bottom, because our hillside has exactly one, and the player can see that in the
  symmetric table of `SS(b)` values in `datasets/level0.md` — one valley, walls rising on both sides,
  no dips. **NAME THE BEDROCK:** the shape of this particular landscape is what makes the nudge
  argument airtight.
- **Not landed** sounds like: "that can't happen" — it certainly can, in other problems. This is the
  question that separates a player who understood the argument from one who memorised it. Award bps
  generously for the honest answer.

**Where it breaks.** Fog-walking suggests you must iterate — take pace after pace, and stop when
tired. The real derivation does not iterate at all: one nudge, done symbolically, lands the answer in
closed form. If the player leaves believing the dial has to be found by trial and error, they will not
believe the formula when it arrives. Correct it explicitly: *the walk is how you understand the
answer; it is not how you compute it.*

---

### C2-C · PHOTOGRAPHY — MANUAL FOCUS

**Story.** A photographer with an old manual lens is focusing on a face across a room. Far off, the
face is a blur; he turns the ring and the blur tightens. He keeps turning past the point where it
looks good, and the blur opens up again on the other side. So he comes back, and now works in small
movements: a touch clockwise, slightly softer; a touch anticlockwise, slightly softer; back to the
middle, sharpest. The two sides going soft by the same amount is how he knows. He does not measure the
distance to the face. He never learns what it is. He only ever compares here against a hair to either
side, and that is enough to fix the ring exactly.

**Map.**

| In the story | In the model |
|---|---|
| the focus ring | the dial `b` |
| the image on the screen | the model's predicted returns for the whole cross-section |
| the face itself | the actual returns |
| sharpness | how good the fit is (the negative of badness) |
| turning past the best point | overshooting the dial |
| a touch each way, softer both times | the nudge test, both directions |
| never measuring the distance | never needing to know the answer in advance to find it |
| the ring settling at one place | a unique best dial setting |

**The awkward question.** *"You said he never measures the distance. But the lens barrel has a
distance scale printed on it. Isn't the whole point that there is a right answer sitting there, and
he is just finding it clumsily?"*

- **Landed** sounds like: the scale is a coincidence of lenses, not of the problem. In the model there
  is no printed scale — there is no single ratio sitting in the data waiting to be read off. (Show
  them: the five per-stock ratios in the cold open disagree wildly, `datasets/level0.md`.) The dial
  setting is *constructed* by the comparison, not looked up.
- **Not landed** sounds like: "so we're estimating the true value of `b`" — the word *true* has smuggled
  in a whole theory the player has not built. At L1 there is no true `b`; there is a best one under a
  stated rule.

**Where it breaks.** A camera's sharpest focus really is a property of the scene, independent of the
photographer's rule. The model's best `b` is *not* independent of the rule — change the rule from
squares to absolutes and the answer moves (in `datasets/level0.md`, from 4 to 2). The photograph story
hides the fact that the loss function was a choice. If the player has just come from C1, remind them
that the choice they made in L0 is what makes this focus ring have a single sharp point at all.

---

**RETURN TO BFRE.**

> "The number you just dialled in is `f` in equation (1.7) on page 24 — the return to a factor. And
> page 4, footnote 2, hands you BFRE's very first one: the market factor, where every asset has unit
> exposure, and the factor return is 'the cross-sectional average return across all assets in the
> model estimation', with the average taken on **regression weights — square root of market
> capitalisation**. Run your calculation with a column of ones and those weights and you have
> reproduced it. That number, annualised over Mar 1996 to Dec 2013, is the **7.0%** in the first row of
> Table 1.2 on page 10."

---
---

# C3 · THE BALANCE CONDITION — leftover misses cannot line up with the column

**Unlocks:** L2 (The Balance) · **Difficulty:** ordinary, but the *proof by contradiction* is the
first genuinely rigorous argument in the game — flag that, not the difficulty.
**Jargon gate:** *orthogonal* becomes legal at L2 (`gm/VOCAB.md` §3.2) — but the word **never appears
anywhere in the paper**, so say "this is the desk's word, not BlackRock's". **Locked:** normal
equations, projection, first-order condition.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| Equation (1.10) | p.26 | Two identifying restrictions: the weighted average Core Industry factor return is forced to zero, and likewise Core Country. Footnote 15: "The average return is a square-root of market capitalisation weighted return." | PAPER |
| Why they exist | p.26 | Without them the specification "is not uniquely identified as there are an infinite number of possible solutions." | PAPER |
| What they cost | p.26 | "the industry and country factors are **net of** the market factor return, which impacts their interpretation." Worked example: if EMEA is broadly up and the UK is up by less than the regional average, "the UK factor return will be **negative**." | PAPER |
| Single-country models | p.26 | Japan has no country factors: "In this instance only **one** linear restriction is required." | PAPER |
| Source typo, free Level-12 exhibit | p.26 | Both sums in (1.10) are printed with index `j` while the second summand is subscripted `k`. Re-verified at 6× in the audit. **The paper's error** — do not silently fix it. | PAPER |

**GAP — say it clearly.** The condition the player is proving at L2 — that the leftover misses must
have zero weighted alignment with each column — **is not in this paper**. Not stated, not derived, not
named; "orthogonal" appears nowhere in 65 pages. The condition is real and they will prove it; it just
has no page number. Do not manufacture one. What p.26 gives you is a *different* balance: one the
authors impose **by hand**. Holding those two apart — what the arithmetic guarantees versus what a
human imposes — is the entire spine of Level 9.

---

### C3-A · MECHANICS — THE SEESAW

**Story.** Children are loading a plank balanced on a log. They put a heavy child far out on the left
and two light ones close in on the right, and the plank tips left. So they shuffle. What they discover
by playing is that it is not the *weight* on each side that settles it, and not the *distance* either
— it is weight and distance together. A small child far out holds down a big child sitting close in.
When the plank finally floats level, any attempt to describe the state as "the same weight on both
sides" is simply wrong; the weights are quite different. The only true description is that the turning
effects have cancelled. And the test is beautiful: if the plank floats level, then nudging it does
nothing useful — it comes back. If it is *not* level, there is an obvious free move available, and
gravity takes it.

**Map.**

| In the story | In the model |
|---|---|
| the plank | the fit at your chosen dial setting |
| each child | one stock |
| how far out along the plank the child sits | that stock's exposure — the value in the column, `x` |
| how heavy the child is | that stock's leftover miss, `e` |
| left of the log / right of the log | the sign of the miss |
| **weight × distance** — the turning effect | exposure × miss for one stock |
| the plank floating level | the weighted alignment of misses with the column summing to zero |
| "the weights are not equal, and that's fine" | the misses do **not** sum to zero in a no-intercept fit — `Σe = 2` in the cold open, and that is not an error |
| a plank that is *not* level | a dial setting that is not the best one — there is a free improvement sitting there |
| gravity taking the free move | the nudge argument: if the balance is broken, you can lower the badness, so you were not at the bottom |

**The awkward question.** *"You told me at Level 0 that the misses don't have to cancel. Now you're
telling me something does have to cancel. Which is it — and how can both be true of the same set of
numbers?"*

- **Landed** sounds like: two different sums. The plain sum of the misses is free to be anything — the
  children's total weight is not constrained. What is forced to zero is the sum of *weight times
  distance*, miss times exposure. Point them at `datasets/level0.md`, where `Σe = 2` and `Σx·e = 0`
  sit two lines apart in the same worked example.
- **Not landed** sounds like: "they're the same thing when the numbers are centred" — a true statement
  from L5 being used to dodge L2. Do not accept it; they have not built centering yet.

**Where it breaks.** On a seesaw, distance from the pivot is always positive on one side and the sign
comes from *which* side. In the model the exposure itself carries a sign, and a stock with a negative
exposure and a negative miss contributes a *positive* turning effect. Players who over-trust the
seesaw draw the sign wrong exactly once, always on the negative-exposure stocks. Pre-empt it: put a
negative-exposure stock in the first worked example and make them state its turning direction out loud.

---

### C3-B · BOOKKEEPING — THE LEDGER THAT WON'T RECONCILE

**Story.** A club treasurer is closing the year's books. Every payment the club received was supposed
to be allocated to one of the categories on the sheet, and whatever the categories could not account
for goes into a single line at the bottom called *unallocated*. She has a large unallocated figure and
that alone does not worry her — some money genuinely has no category. What worries her is what she
notices when she sorts the unallocated items by the size of the member's subscription: the big
subscribers keep showing up with big unallocated amounts and the small subscribers with small ones.
That pattern is the problem. It means she has under-charged the subscription category: the leftovers
still carry the fingerprint of subscription size. She adjusts the subscription rate upward, redoes the
allocation, and repeats until the leftover column shows no relationship at all to subscription size.
Only then does she sign the accounts. The leftover total is still large. It is now merely *unrelated*.

**Map.**

| In the story | In the model |
|---|---|
| the year's receipts | the actual returns |
| a category on the sheet | one column of exposures |
| the rate charged to that category | the dial setting for that column, `b` (later `f`) |
| the *unallocated* line | the misses |
| a large unallocated total | `Σe` being large — perfectly allowed |
| **leftovers lining up with subscription size** | the misses still correlated with the column — the balance broken |
| "I have under-charged that category" | the dial is set too low; there is a free improvement |
| adjusting and repeating | the nudge argument |
| leftovers showing no relationship to the column | the balance condition holding |
| signing the accounts | the fit is the best one under the stated rule |

**The awkward question.** *"She stopped when the leftovers had no relationship to subscription size.
But the leftovers are still big. How is that a finished job — isn't a big leftover a bad model?"*

- **Landed** sounds like: those are two separate verdicts. "No pattern left" says you extracted
  everything this column could explain — it is a statement about the *procedure*. "Leftovers still
  big" says the column does not explain much — a statement about the *world*. A model can be perfectly
  fitted and still explain almost nothing, and the paper reports both kinds of number.
- **Not landed** sounds like: "so we add more categories until the leftover is small" — sometimes yes,
  but this answer skips the distinction entirely, and at L9 it becomes the difference between a real
  factor and a fudge.

**Where it breaks.** A treasurer chooses her categories and can invent new ones at will. Least squares
cannot invent columns; it can only set dials on the columns it was given. Also, the story's iteration
implies the balance is something you *achieve by effort*. It is not — it falls out of the arithmetic
whether you want it or not, which is precisely what makes it usable as a sabotage detector at L2. Say
so: *you could not have prevented this balance if you tried.*

---

### C3-C · FARMING — THE FERTILISER SPREADER

**Story.** A farmer has one dial on the back of her spreader and a field whose soil quality she has
already surveyed strip by strip. Her rule is simple: spread in proportion to how poor the strip is —
the dial sets how much per unit of poorness. She spreads, and at harvest she walks the field noting
where each strip came in above or below what she hoped for. The shortfalls are all over the place, and
that is normal — weather, birds, bad luck. What she is looking for is different. She lines the
shortfalls up against the poorness of the strips, and finds that the poorest strips are the ones
consistently short. That tells her something the individual shortfalls never could: her dial was too
low, and she had fertiliser left in the hopper she should have spent. Next year she turns it up and
walks the field again, and keeps going until the shortfalls show no tilt at all against soil poorness.
Then the dial is right, whatever the harvest.

**Map.**

| In the story | In the model |
|---|---|
| a strip of the field | one stock |
| the surveyed poorness of the strip | that stock's exposure, `x` |
| the dial on the spreader | the factor return, `b` (later `f`, p.24) |
| fertiliser spread on a strip | the model's prediction for that stock |
| the shortfall at harvest | the miss, `e` |
| scattered shortfalls | misses that do not sum to zero — allowed |
| **shortfalls tilting against poorness** | misses correlated with the column — balance broken |
| "I had fertiliser left in the hopper" | there was a free improvement; you were not at the bottom |
| turning the dial until the tilt is gone | the nudge argument ending at the balance condition |
| the harvest still being poor | a fitted model that still explains little |

**The awkward question.** *"She only has one dial for the whole field. Suppose the poor strips need a
different rate from the good strips — her rule can't do that. Doesn't the balance condition just
guarantee she's made the best of a rule that was wrong to begin with?"*

- **Landed** sounds like: yes, precisely, and that is the honest reading. The balance guarantees you
  have extracted everything *this rule* can extract. It says nothing about whether the rule was the
  right shape. Adding a second dial is L3; discovering the two dials fight is L4.
- **Not landed** sounds like: "the balance proves the model is right" — the single most dangerous
  misreading in the whole game. It is exactly the confusion the Level-12 critique of the paper turns
  on. Dock bps and correct it now.

**Where it breaks.** Fertiliser is a physical quantity you can run out of; there is a hopper with a
fixed amount in it. Nothing in the regression is conserved — the dial can be set to any number at all,
and no resource limits it. If the player starts talking about "using up" explanatory power as though
it were finite, they have imported the hopper and will be badly confused at L4, where two columns
genuinely do compete for the same explanation. Kill the hopper before L4.

---

**RETURN TO BFRE.**

> "Your balance came out of the arithmetic for free and you could not have stopped it. Now look at page
> 26, equation (1.10): there the authors impose a balance **by hand** — they force the weighted average
> industry return and the weighted average country return to zero, because otherwise, in their words,
> the specification 'is not uniquely identified as there are an infinite number of possible solutions'.
> And they pay for it in meaning: page 26 again — 'the industry and country factors are **net of** the
> market factor return', so if EMEA is broadly up and UK assets are up by less than the regional
> average, 'the UK factor return will be **negative**'. Hold that difference. Something the arithmetic
> guarantees, versus something a human imposes. Level 9 is entirely that distinction."

---
---

# C4 · TWO DIALS INTERACTING

**Unlocks:** L3 (The Second Dial) · **Difficulty:** ordinary; the algebra is a 2×2 solve in fractions.
**Jargon gate:** *design matrix* is legal at L3 — and the phrase **never appears in the paper**; `X` is
called "factor exposures" (p.24). **Locked:** normal equations, matrix inverse, simultaneous system as
a named object.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| Equation (1.9) | p.25 | `r = X_Mkt f_Mkt + Σ_{i∈Sty} X_Sty,i f_Sty,i + Σ_{j∈CInd} X_CInd,j f_CInd,j + Σ_{k∈CCty} X_CCty,k f_CCty,k + u`. **Four blocks, one regression, one pass.** Verified at 5×; the market term carries no sum. | PAPER |
| Why simultaneously | p.5 | Country factor returns "are estimated in a **multivariate regression together with other common factors**, and are therefore **adjusted to be neutral with respect to market, style and industry effects**." Reason given: a country with a large concentration in a single industry. | PAPER |
| The three-block ancestor | p.7 | Equation (1.1): market + core country + industry-at-level-`n`, fitted together. | PAPER |
| The second pass | p.26 | Equation (1.11): Extended Industry and Extended Country factors fitted **to the first pass's residuals** — so they are not in the joint solve at all. | PAPER |
| Source typo | p.26 | The "where"-list under (1.9) has **five** rows and no Style row; `X_Mkt f_Mkt` is printed against the description "Style Exposures and Factor Returns". Re-verified at 4×. **Paper's error.** | PAPER |

---

### C4-A · PLUMBING — THE SHOWER TAPS

**Story.** An old shower has two taps, hot and cold, and no thermostat. A guest wants a comfortable
temperature and a decent flow. He opens the hot tap until the temperature is right — but the flow is
feeble, so he opens the cold to get more water, and now it is too cold. So he opens the hot further to
recover the temperature, and now the flow is too strong and he is being hosed. He goes round this loop
four times and gets somewhere passable, mainly by luck. His host, who has lived with the shower for
years, does it in one movement: she knows that both taps affect both things, so she does not chase
them one at a time. She sets both hands on both taps at once and moves them together to a position she
already knows. Two knobs, two things to get right, and the knobs are not independent: you have to
solve for both at once or you chase your tail.

**Map.**

| In the story | In the model |
|---|---|
| the hot tap | the dial on column one |
| the cold tap | the dial on column two |
| the temperature | the requirement that the misses balance against column one |
| the flow | the requirement that the misses balance against column two |
| both taps affecting both | each column's dial changes the misses, so it changes *both* balance conditions |
| chasing round the loop | fitting one column at a time — the naive method L4 will show can be catastrophically wrong |
| the host's single movement | solving the two balance conditions simultaneously (the 2×2 system) |
| taps that barely interact (a modern mixer) | two columns that are unrelated — one-at-a-time happens to work |
| taps that interact violently | two columns that overlap — L4's collision |

**The awkward question.** *"He did get there eventually by going round the loop. Is one-at-a-time
actually wrong, or just slow?"*

- **Landed** sounds like: it depends entirely on how much the taps interact. When they interact
  weakly, looping converges and one-at-a-time is merely slow. When they interact strongly, the loop
  either crawls or lands somewhere else entirely — and the one-shot version of it (fit column one,
  keep that answer, then fit column two) is not slow, it is *wrong*, and L4's boss round is
  constructing exactly that case.
- **Not landed** sounds like: "just slow" with no condition attached. That answer will fail L4.

**Where it breaks.** Shower taps have a physically fixed relationship — a plumber could measure it once
and it would hold forever. The relationship between two columns of exposures is re-measured every
single period from the data, and it moves: p.11's Figure 1.3 is a snapshot from **one date, Dec 2013**,
not a constant of nature. A player who thinks the interaction is a fixed property of the model will not
understand p.32's warning about "significant instability in the factor return estimates through time".

---

### C4-B · AVIATION — TRIM

**Story.** A student pilot is told to hold a height and a speed. She is too low and too slow, so she
pulls back on the control column to climb. The nose comes up, the aircraft climbs — and the speed
decays further, because she is now dragging the aeroplane uphill on the same engine setting. So she
adds power to recover the speed, and the extra power pushes the nose up again and she climbs past her
height. Round and round. Her instructor takes control and does it in one smooth coordinated move:
power and pitch together, because in an aeroplane neither control owns a single result. Power and
attitude between them set both speed and height, and any attempt to assign one control to one outcome
is a story pilots tell beginners and then take away.

**Map.**

| In the story | In the model |
|---|---|
| the control column (pitch) | dial one |
| the throttle (power) | dial two |
| the target height | balance condition on column one |
| the target speed | balance condition on column two |
| each control affecting both targets | each dial shifting all the misses, hence both balances |
| the student's oscillation | one-at-a-time fitting |
| the instructor's coordinated input | solving the system jointly, in one pass |
| "one control, one outcome" being a beginner's story | the naive intuition that a coefficient means "the effect of this column", full stop |
| what a coefficient really means | the effect of this column *given that the other one is also in the solve* — L4 |

**The awkward question.** *"In a real aeroplane there's a right answer — one power setting and one
attitude that give exactly that height and speed. Is there always a right answer for two columns, or
can the two demands contradict each other?"*

- **Landed** sounds like: there is exactly one answer as long as the two columns are genuinely
  different from one another. If they are the same column in disguise, the two demands collapse into
  one and there is no unique answer at all — an infinity of them. That is L4 and it is the paper's own
  footnote 16 on p.32.
- **Not landed** sounds like: "yes, always" — the confident wrong answer. It is worth setting up
  deliberately, because the correction is the hook into L4.

**Where it breaks.** Aviation adds dynamics — lag, inertia, the aircraft still moving after the input.
The regression has none: the solve is instantaneous and simultaneous, with no ordering and no
transient. If the player starts talking about which dial to move "first", the aeroplane has misled
them. There is no first.

---

### C4-C · PAINTING — MIXING TWO PIGMENTS

**Story.** A restorer is matching a patch of faded green on a panel. She has two pigments on the
palette, a yellow and a blue, and she must match both the hue and the darkness of the original. She
adds blue to correct the hue and the patch goes darker than the original; she adds yellow to lighten
it and the hue swings back towards green-gold. Neither pigment controls one property. What she
actually does, after the first two attempts, is stop treating them as two separate corrections: she
works out the pair of amounts that hits both hue and darkness together, mixes that, and applies it
once. Any restorer who insists on fixing hue first and darkness second either ends up going round
forever or ends up with a patch that is the right colour and the wrong depth.

**Map.**

| In the story | In the model |
|---|---|
| the yellow pigment | column one |
| the blue pigment | column two |
| how much of each you add | the two dial settings |
| matching the hue | balance condition on column one |
| matching the darkness | balance condition on column two |
| each pigment moving both properties | each dial moving both balances |
| "fix hue first, then darkness" | fitting one column at a time |
| working out both amounts and mixing once | the simultaneous solve |
| two pigments that are nearly the same colour | two columns that nearly agree — L4's collision |
| the patch never matching, however you mix | a demand no pair of dials can meet — leftover misses |

**The awkward question.** *"If she has two pigments and two things to match, that feels like exactly
enough. What happens if she has three things to match — hue, darkness and how glossy it is — and still
only two pigments?"*

- **Landed** sounds like: then she cannot match all three, and the leftover mismatch is exactly the
  thing L0 called the miss. Two dials buy you two balance conditions and no more; everything else
  stays in the residual. This is the sentence that connects L3 back to L0 and forward to L9.
- **Not landed** sounds like: "she buys a third pigment" — true, and it is what BFRE does when it adds
  a factor, but the player has dodged the question. Push: *before she buys it, what is the state of the
  panel?*

**Where it breaks.** Paint is conserved and additive in a physical way — mixing more of both makes more
paint. Dial settings are not amounts of anything; a negative dial setting is completely ordinary
(Reversal ran at **−5.1%** annualised in Table 1.2, p.10) whereas negative blue is not a thing. If the
player starts refusing negative coefficients because "you can't add negative paint", the pigment story
is actively costing them and should be dropped.

---

**RETURN TO BFRE.**

> "Two dials solved together is equation (1.9) on page 25, where BFRE turns the market dial, every
> style dial, every core-industry dial and every core-country dial **in one solve, in one pass**. Page
> 5 gives you the reason in a single line: country factor returns are estimated 'in a multivariate
> regression together with other common factors, and are therefore **adjusted to be neutral with
> respect to market, style and industry effects**' — the country number is only neutral *because* it
> was solved jointly. Solve them one at a time and a country whose index is dominated by one industry
> reports a 'country' return that is partly an industry return."

---
---

# C5 · COLLINEARITY AND THE COLLISION

> **DIFFICULTY: GRADUATE-LEVEL. Say so before the story.** Multicollinearity is a genuine graduate
> topic, and the "regress on what's left over" move the paper uses throughout is the Frisch–Waugh–Lovell
> theorem in disguise. **The paper never names Frisch–Waugh** — zero hits in `notes/`. At the table:
> "this is the mechanism behind a theorem you will meet later called Frisch–Waugh–Lovell." Do not cite
> a page for the name.

**Unlocks:** L4 (The Collision) · **Jargon gate:** *multicollinearity* and *variance inflation factor*
unlock at L4 and both **are** the paper's words (p.32). *Orthogonal* deepens here.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The diagnostic and the failure mode | p.32 | "If style exposures are too closely correlated then the regression procedure will encounter problems in **apportioning the factor return between them**. This can result in **significant instability in the factor return estimates through time**." | PAPER |
| Footnote 16 — the determinant going to zero, in words | p.32 | "In the most extreme case, where factor exposures are **perfectly correlated**, identification issues will exist causing the estimation process to **fail**." | PAPER |
| An exact collision, built in | p.26 | Three intercepts: market, industry and country, "Every asset has unit exposure to these three factors." Fixed only by the two restrictions of (1.10). | PAPER |
| Measured collisions | p.11, Fig 1.3 | NAMR, **Dec 2013**: Size–Liquidity **0.74** (highest off-diagonal), Earnings Yield–Profitability **0.64**, Volatility–Dividend Yield **−0.46**, Size–Volatility **−0.36**. All 144 cells re-read in audit. | PAPER |
| A collision designed *out* | p.17 | Momentum uses "the **previous 11 months with a one month lag** to exclude the reversal effect". Reversal is exactly the excluded month. Two columns engineered not to overlap. | PAPER |
| A collision surrendered to | p.20 | In EMEA, Earnings Yield and Dividend Yield "were found to be highly correlated over the research history and so were **combined into a single factor**, referred to as yield." | PAPER |
| Partialling, everywhere | pp.7, 10, 12, 52 | (1.1)/(1.2), (1.3)/(1.4), (1.5)/(1.6), and (1.49): a candidate is judged by regressing it on the **residuals of the model without it**. | PAPER |
| The stable relationship | p.14 | "portfolios which are positively exposed to size are commonly negatively exposed to volatility, and vice versa. This negative relationship is fairly stable over time." | PAPER |
| The money version | p.13 | AOL: large on market cap, small on sales. "A measure of size based on market capitalisation alone would confer large-size status on AOL, and **reduce its risk forecast accordingly**." Direction of the error: **too low**. | PAPER |
| The desk's verdict | p.32 | VIFs "were reviewed over the research history and **were found to be well within suitable thresholds**" — **no value, no threshold, anywhere**. Level-12 exhibit. | PAPER |

---

### C5-A · COURTROOM — THE TWO WITNESSES

**Story.** A collision at a junction. Two witnesses come forward. They were sitting side by side in
the same car, at the same lights, looking the same way. Their statements are nearly word for word
identical. Counsel wants the court to find that the second witness independently corroborates the
first, and the judge will not have it: the second saw nothing the first did not see, so almost nothing
in that statement is *additional* evidence. Then a third witness appears, a shopkeeper who was facing
the other way and heard rather than saw. Her account adds something new, and it carries real weight
even though it is thinner. Now imagine the hardest case: the two passengers turn out to have submitted
the *same* statement, signed twice. The judge does not weigh them differently. The judge cannot weigh
them at all — there is no fact of the matter about how much each contributed, and any split the court
announced would be arbitrary. The case does not become uncertain. It becomes unanswerable.

**Map.**

| In the story | In the model |
|---|---|
| a witness | a column of exposures |
| the statement | what that column can explain about returns |
| the two passengers in one car | two highly correlated columns — Size and Liquidity at **0.74** (p.11, Dec 2013) |
| "what does the second one add that the first didn't" | what a coefficient actually means: the part this column explains that no other column already explained |
| the shopkeeper facing the other way | a column that overlaps little — it gets a clean, stable coefficient |
| **two identical signed statements** | perfectly correlated columns |
| "the court cannot weigh them at all" | the determinant hitting zero; estimation fails — p.32 footnote 16, in the paper's own words |
| a judge who splits it anyway, differently each week | the instability p.32 warns about: risk attributed to Size this month and Liquidity next month with no change in the portfolio |
| hearing witness two *after* witness one and asking only what is new | the paper's two-step method: fit the model without the candidate, then regress the candidate on the residuals (pp.7, 10, 12, 52) |

**The awkward question.** *"If the two passengers really did see the same thing, and their evidence is
sound, why does the court care which of them it credits? The verdict is the same either way."*

- **Landed** sounds like: for the *verdict*, it does not care — the combined effect is perfectly well
  determined and the total risk number is fine. What breaks is the **attribution**. The risk report on
  p.35 does not just give a total, it splits Active Risk into Style, Industry, Country, FX and
  Specific, and a PM acts on that split. An unstable split is a report that tells you to trade
  something different every month for no reason.
- **Not landed** sounds like: "the estimate becomes inaccurate" — vague, and slightly wrong. The sum is
  not inaccurate; the *decomposition* is unidentified. That distinction is the whole level.

**Where it breaks.** In a courtroom, a witness who adds nothing is simply excluded and no harm is done.
In the regression you cannot cheaply exclude a column, because dropping a genuinely relevant one pushes
its explanation into the residual — where p.16 shows exactly what that looks like (before a small-cap
factor existed, deciles 9 and 10 still showed significant structure in the residuals, at roughly
**10.8%** and **21.1%** `[APPROX — pixel-measured off Figure 1.10, ±0.5pp]`). The court has an option
the model does not.

---

### C5-B · AUDIO ENGINEERING — TWO MICROPHONES

**Story.** An engineer is recording a cello with two microphones a few inches apart, pointed at
roughly the same spot. At the desk she has a fader for each. She sets the pair and it sounds right.
Then, out of curiosity, she pushes one fader up and pulls the other down by the same amount — and
the sound barely changes. She does it again, further. Still almost the same. There is a whole family
of fader settings that produce nearly the same recording, and no way to hear which one she is on.
Meanwhile the *sum* of the two faders matters enormously: push both up and the cello gets loud. So
one quantity is pinned down hard by her ears and another is floating free. Later she moves one
microphone across the room to catch the room's reverberation, and the ambiguity vanishes: now each
fader does something distinctly its own, and she can hear immediately if either is wrong.

**Map.**

| In the story | In the model |
|---|---|
| each microphone | a column of exposures |
| each fader | that column's coefficient |
| the sound coming out | the model's fitted returns |
| **pushing one fader up and the other down with no audible change** | the collinear direction: a whole family of coefficient pairs giving nearly the same fit |
| "the sum is pinned, the split is floating" | the combined effect identified, the individual coefficients not |
| the two microphones inches apart | correlated columns — Earnings Yield and Profitability at **0.64** (p.11) |
| the microphone moved across the room | decorrelating the columns on purpose |
| **the two microphones in exactly the same place** | perfect correlation — the estimation fails, p.32 fn 16 |
| listening and hearing nothing wrong | the total risk number looking perfectly healthy while the decomposition is nonsense |

**The awkward question.** *"You say the sound barely changes. Barely isn't 'not at all'. So there
still is a best pair of fader settings — why isn't the maths just finding it?"*

- **Landed** sounds like: it *is* finding it, and that is precisely the problem. When the difference is
  tiny, the answer is decided by the tiniest wobble in the data — this month's noise, not this month's
  economics. Which is why p.32 phrases the symptom as instability *through time*, not as an error at
  any one date. Re-estimate tomorrow and the split moves; the fit does not.
- **Not landed** sounds like: "so we should use more data" — sometimes helps, sometimes cannot: at
  perfect correlation no amount of data helps at all, because the information is not thin, it is absent.

**Where it breaks.** The two microphones are two *sources* of the same signal; the columns of `X` are
not sources at all, they are characteristics we chose to measure and standardise (p.10, p.39). The
story also makes the collision sound like a recording-studio accident. In BFRE the biggest collision is
deliberate and structural: every asset has unit exposure to a market factor, an industry factor **and**
a country factor (p.26) — three columns of ones, built in by design, knocked down to one by the two
restrictions of (1.10).

---

### C5-C · CARPENTRY — THE STACKED SHIMS

**Story.** A joiner is levelling an old workbench on a sloping floor. Under one leg he slides two thin
tapered shims, one on top of the other, and taps them until the bench sits flat. It is dead level and
it will stay level. A colleague asks how thick each shim is. The joiner cannot say. He knows the pair
comes to a certain total, because the bench is level and the floor is what it is — but the split
between the two shims is whatever it happened to be when he stopped tapping. Knock the bench and
re-tap it and the total will come out the same and the split will be different. The colleague, who is
writing a report on shim usage, records a number anyway. Next month he records a different one. His
report is describing his own hammer, not the floor.

**Map.**

| In the story | In the model |
|---|---|
| the gap under the leg | what the data needs explaining |
| each shim | a column of exposures |
| each shim's thickness | that column's coefficient |
| the bench sitting level | the fit being achieved |
| **the total thickness being determined** | the combined effect identified |
| **the individual thicknesses not being determined** | the individual coefficients unidentified |
| re-tapping and getting a different split | re-estimating next period and getting a different apportionment (p.32: "significant instability… through time") |
| the colleague's monthly report | a risk report that attributes the same risk to Size one month, Liquidity the next |
| "describing his own hammer, not the floor" | reporting estimation noise as though it were an economic fact |
| two shims of very different tapers | columns that are genuinely different — the split becomes determinate again |

**The awkward question.** *"The bench is level. That's what he was hired to do. Why does anyone care
about the shim thicknesses at all?"*

- **Landed** sounds like: nobody would, if the only deliverable were the total. But the deliverable
  here is a *decomposition* — the pie on p.35 splits Active Risk into Specific 50%, Style 25%,
  Industry 14%, Country 6%, FX 4% — and the whole reason a PM reads that report is to decide which bet
  to cut. The shim thicknesses are the report.
- **Not landed** sounds like: "because we want accurate coefficients" — circular. Ask what the
  coefficient is *for*.

**Where it breaks.** Shims are physical and their total is genuinely fixed by the floor; in the model
even the total is estimated and carries its own uncertainty. And there is no "hammer" — the wobble in
the split comes from the data, not from the analyst's technique, so a player who concludes "use a more
careful method" has taken the wrong lesson. The paper's own responses are structural, not procedural:
**engineer the overlap away** (p.17, momentum lagged one month "to exclude the reversal effect"), or
**merge the two columns** (p.20, EMEA yield).

---

**RETURN TO BFRE.**

> "What you just built is why page 17 stops the momentum window one month early — *'the previous 11
> months with a one month lag to exclude the reversal effect'* — and why EMEA does not have separate
> earnings-yield and dividend-yield factors at all: page 20 says they 'were found to be highly
> correlated over the research history and so were combined into a single factor'. Page 32 is the alarm
> the desk actually runs, the **variance inflation factor**, and its footnote 16 says that when two
> columns agree *perfectly*, the estimation does not go wrong — it **fails**. Note what page 32 does
> *not* say: it reports the VIFs 'were found to be well within suitable thresholds' and prints neither
> a value nor a threshold. That is a Level-12 exhibit and you should keep it."

---
---

# C6 · THE INTERCEPT AND THE PIVOT

**Unlocks:** L5 (The Intercept) · **Difficulty:** ordinary, but the payoff — that centering turns the
L1 formula into covariance-over-variance — is the game's first big "you have met this before".
**Jargon gate:** *intercept*, *z-score*, *standardisation* and *covariance* unlock at L5. *Intercept*
and *standardisation* are the paper's own words (p.26, p.10, p.39). **Locked:** demeaning, projection
onto the constant, degrees-of-freedom cost of the intercept (that is C8).

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| A column of ones *is* an intercept — the paper says so | p.26 | "for each asset, there exist three intercept terms – the market factor, an industry factor, and a country factor. **Every asset has unit exposure to these three factors.**" Two linear restrictions reduce them "from three to one". | PAPER |
| Where BFRE does the centering | p.10 | "The **mean** is defined as the **square-root of market capitalisation weighted** average value so that the transformed substyles (and styles) have the property that their **weighted average is zero**… divided by their **equally-weighted standard deviation**… **An exposure of zero indicates that a security has the market average value.**" | PAPER |
| Again, in the appendix | p.39 | Huberisation: exposures "take values between **+/- 3** and are standardised to a square-root capitalisation **mean of zero**, with an **equal-weighted standard deviation of one**". Applied a second time after aggregation. | PAPER |
| An intercept harvested as a factor | p.42, p.44 | `alpha_i` — the intercept of the beta regression (1.12) — is itself used as the **Historical Alpha** substyle. | PAPER |
| Smoothed columns of ones | p.16, p.51 | Small-Cap and Mid-Cap are "smoothed versions of dummy variables"; smoothing is used "to mitigate instability in exposures for assets on the decile boundaries". Constants printed: `α₁=0.95, α₂=0.75, α₃=0.2` and `α₁=0.60, α₂=0.54, α₃=0.7`, with no empirical justification beyond the stated intent to hit deciles 8/9/10 and 6/7. | PAPER |

**Level-12 seed, stated on both pages and never justified:** the **mean** is √-cap weighted while the
**standard deviation** is equal-weighted (p.10 and p.39). The paper states the asymmetry and gives no
reason for it.

**GAP.** The paper never derives covariance-over-variance, never writes the centering algebra, and
never uses "covariance" in the estimator sense (only "factor covariance matrix"). The proof that the
fitted line passes through the mean point is ours.

---

### C6-A · SURVEYING — THE DATUM

**Story.** Two survey teams map the same ridge. One measures every height from mean sea level, forty
miles away. The other, working fast, sets up on the village green and measures everything from there.
They hand in two sets of numbers that disagree on every single hill. Then someone lays the two lists
side by side and sees that every disagreement is the same amount — the height of the green above the
sea. The shape of the ridge is identical in both surveys: every slope, every rise between one hill and
the next, matches perfectly. The teams did not disagree about the ridge. They disagreed about where
zero is. And the village-green team's numbers are more useful for the villagers, because a reading of
zero now means "level with the green" — a thing anyone in the village can picture.

**Map.**

| In the story | In the model |
|---|---|
| the ridge | the relationship between exposure and return |
| a hill's height | one stock's exposure value |
| **the chosen datum — sea level or the green** | where zero is placed on the column: raw units, or centred |
| the two lists disagreeing everywhere | uncentred and centred exposures give different numbers for every stock |
| **the slopes matching perfectly** | centering does not change the tilt — the relationship is the same |
| the constant offset between the lists | the intercept: the one number that absorbs the difference in datum |
| "zero means level with the green" | BFRE, p.10: "An exposure of zero indicates that a security has the market average value" |
| the villagers finding the green datum useful | why BFRE centres every characteristic before it ever reaches a regression |
| a survey with no stated datum | a model with no intercept, where every reading secretly carries a level |

**The awkward question.** *"If the shape is the same either way, why bother re-centring at all? Just
report sea-level heights and let people subtract."*

- **Landed** sounds like: because there is more than one team. When several columns each carry their
  own hidden level, the levels compete to explain the same overall average — and in BFRE that
  competition is real and named: p.26 says every asset carries **three** columns of ones at once, and
  the problem is not solved by subtraction but by two linear restrictions.
- **Not landed** sounds like: "for convenience" — dock a little. Push: *convenient for whom, and what
  goes wrong if you don't?*

**Where it breaks.** A survey's datum is a pure convention with no effect on anything real. Centering
in BFRE is **not** a pure convention, because the mean is taken with √-market-cap weights (p.10) — so a
different weighting gives a different "sea level" and therefore genuinely different exposures. The
choice of datum here has a cap-weighted opinion baked into it. Say so; it is a Level-12 seed.

---

### C6-B · SPORT — GOLF, AND PAR

**Story.** A club has a noticeboard with everyone's scores on it and nobody can read it. Some members
play the long championship course, some the short one; the raw stroke counts are meaningless side by
side. So the club stops posting strokes and posts scores against par instead. Immediately the board
becomes legible: zero means "played the course as it is meant to be played", a negative number means
better than that, and a member who moves from the long course to the short one no longer appears to
have improved. Nothing about anyone's golf changed. The club simply moved where zero sits, and put it
somewhere that means something.

**Map.**

| In the story | In the model |
|---|---|
| a raw stroke count | a raw characteristic value — a market cap, a book-to-price ratio |
| par for the course | the weighted average value of that characteristic across the market (p.10) |
| the score against par | the standardised exposure |
| **zero meaning "as the course is meant to be played"** | p.10 verbatim: "An exposure of zero indicates that a security has the market average value" |
| comparing the long and short courses | comparing characteristics measured in different units — market cap in dollars against a ratio |
| a member who looks better only because they changed course | a stock that looks extreme only because its characteristic is measured in a different unit |
| the handicap adjustment on top | the second half of standardisation: dividing by a spread so a score of one means one standard step above average (p.10, p.39) |
| the noticeboard being for comparing members | the whole reason BFRE standardises: "to facilitate comparison of securities across different regions" (p.10) |

**The awkward question.** *"Par is decided by the club. Who decides par for a stock — and what happens
to everybody's score when whoever it is changes their mind?"*

- **Landed** sounds like: the market decides it, monthly, and it moves. The paper's par is the
  √-market-cap weighted average of the current universe (p.10), so an exposure of zero this month and
  an exposure of zero next month are not the same characteristic value. Every exposure in the model is
  relative to a moving par, and the universe itself is rebuilt "on a country-by-country basis every
  month" (p.24).
- **Not landed** sounds like: "the model decides" — too vague. Make them name the weighting scheme; it
  is printed.

**Where it breaks.** Golf's par is set by a committee in advance and holds all season, so the analogy
makes centering feel like a fixed external standard. BFRE's par is re-derived from the data every
period, which means the *definition of zero* is itself estimated. And golf has only one par per course;
BFRE has three columns of ones fighting over the same job (p.26). If the player leaves thinking there
is one obvious zero, they will be blindsided by (1.10).

---

### C6-C · WEIGHING — THE TARE BUTTON

**Story.** A baker puts an empty mixing bowl on the kitchen scales, presses *tare*, and the display
drops to zero with the bowl still sitting on it. Now every number the scales show is flour, not flour
plus bowl. She never has to remember the bowl's weight or subtract it; the machine has moved its own
zero. Later she works in a different kitchen where the scale has no tare button, forgets the bowl, and
puts far too much flour in the dough — the classic error, and it is not an arithmetic slip. It is what
happens when a constant offset is left sitting inside every measurement. Worse: in a third kitchen she
stacks a bowl inside a tray on top of a mat and tares once. The display reads zero and she has no way
to say how much of that zero was bowl, how much tray, how much mat. She does not need to know — but if
someone asks her for the weight of the tray alone, she genuinely cannot answer.

**Map.**

| In the story | In the model |
|---|---|
| the flour | the part of the return the column is meant to explain |
| the bowl | a constant level sitting in every measurement |
| **pressing tare** | including an intercept / centring the column |
| the display now reading flour only | coefficients that mean "per unit above average", not "per unit of raw characteristic" |
| forgetting the bowl in the second kitchen | fitting with no intercept when the data has a level — the L0 cold open, where `Σe = 2` and not zero |
| the ruined dough | a coefficient that has quietly absorbed a level it should not own |
| **bowl + tray + mat, tared once** | p.26: market, industry and country intercepts, all unit exposure, all at once |
| "how much of that zero was the tray?" | the identification problem — infinitely many answers |
| the baker not needing to know | the paper's line: the fix "simply represents a rotation of the factor returns. It does not impact the efficacy of the risk model" (p.26) |
| someone demanding the tray's weight anyway | a user reading a country factor return as if it were a raw country return — which p.26 warns will make a rising market look like a falling country |

**The awkward question.** *"You said she doesn't need to know how much was the tray. But you also said
someone might ask. Which is it — is the split real information the model is throwing away, or is it
genuinely meaningless?"*

- **Landed** sounds like: it is genuinely not determined by the data, so it is not information being
  thrown away — it is a choice being made. BFRE makes it explicitly on p.26 by forcing the weighted
  average industry return and the weighted average country return to zero. Once you make that choice,
  the numbers *become* meaningful, but only relative to the choice: page 26 spells out the consequence,
  that if EMEA is broadly up and UK assets are up by less than the regional average, "the UK factor
  return will be negative."
- **Not landed** sounds like: "it's meaningless" full stop — that misses that a convention was adopted
  and published, and the numbers are read against it every day.

**Where it breaks.** Tare is exact and instantaneous; the bowl's weight is a fixed physical fact. The
"level" in a regression is estimated with error like everything else, and moves period to period. Also,
kitchen scales tare *before* the measurement; the regression finds its intercept *from* the
measurements, simultaneously with everything else. A player who thinks the intercept is subtracted
first, then the slope fitted, has the order wrong — and that misunderstanding is exactly what C4 (two
dials) exists to prevent.

---

**RETURN TO BFRE.**

> "Your pivot moving to the average is what page 10 does to every single characteristic before it ever
> reaches a regression: the mean is subtracted — a **square-root-of-market-capitalisation weighted**
> mean — so that, in the paper's words, 'an exposure of zero indicates that a security has the market
> average value'. And page 26 shows you what it costs when there are too many pivots: every asset in
> BFRE carries **three** columns of ones — market, industry, country, all unit exposure — and equation
> (1.10) is how the authors knock three back down to one. Keep one thing in your pocket for Level 12:
> page 10 and page 39 both say the mean is cap-weighted and the standard deviation is equal-weighted,
> and neither page says why."

---
---

# C7 · THE STANDARD ERROR AND SAMPLING WOBBLE

**Unlocks:** L6 (The Verdict) · **Difficulty:** hard but not graduate. The honest framing: *this is the
level where the game gives you something the paper assumes and never shows.*
**Jargon gate:** *standard error*, *t-statistic*, *statistically significant* unlock at L6. **The phrase
"standard error" never appears in the paper**; `|t| > 2` does (p.8). **Locked:** sampling distribution,
unbiasedness, variance of an estimator, heteroskedasticity (though the *word* is on p.25 — see below).

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The threshold | p.8 | "We consider an absolute t-statistics in excess of **2** as statistically significant." (Grammar error is the source's.) | PAPER |
| The squared version | p.8 | "the **average squared t-statistic**, computed specifically to distinguish between factors with t-statistics close to +/- 2 and those that are significantly higher." | PAPER |
| Persistence proxy | p.8, p.32 | The **proportion** of significant t-statistics "serves as a good proxy for the persistence of individual factor effects." | PAPER |
| The inclusion bar | p.14 | "A value in excess of **10%** indicates a statistically significant style effect, and would be considered for inclusion in the models." Footnote 11: "t-statistics are based on **monthly cross-sectional regressions**." | PAPER |
| The stopping rule | p.12 | Recursion stops "until the largest proportion of t-statistics from the second step univariate regression is no larger than **10% - 15%**." | PAPER |
| The sample | p.8 | Regressions monthly over the **15-year research history**; results summarised over the full sample **and five-year sub-samples**. | PAPER |
| The evidence | p.15, Fig 1.8 | NAMR styles ranked by proportion of significant t-stats: Volatility ≈63%, Momentum ≈50%, Size ≈42%, Reversal ≈37%, Value ≈34%, Liquidity ≈32%, Dividend Yield ≈23%, MidCap ≈20%, Growth ≈18%, Profitability ≈14%, Sentiment ≈7%, Earnings Yield ≈4–5%. `[APPROX — pixel-measured, no data labels printed. Say so.]` | PAPER + `[APPROX]` |
| Why the weights | p.25 | √-market-cap weighting "adjusts for **heteroskedasticity** based on the observation that higher residual (specific) risk is typically correlated with smaller market capitalisation assets." | PAPER |

**GAP — a big one, say it clearly.** The paper never shows where a standard error comes from, never
mentions degrees of freedom, and never prints a t-statistic formula. Zero hits in `notes/` for "standard
error" and "degrees of freedom" in the paper's own text. The only inference machinery named anywhere is
**Newey–West**, reference [26] (Econometrica, 1987 — bibliography, p.65), cited on pp.27–28 and p.38 for
serial correlation in the *risk* estimates, and **not** presented as the source of the t-statistics.

**Boss-round ammunition (big coefficient, small t — and its mirror).** Table 1.2 (p.10) prints
**Volatility** with an annualised return of **−0.6%** on a volatility of **7.5%** — a Sharpe of
**−0.08**, i.e. no reliable return at all — while Figure 1.8 (p.15) ranks it the **most** significant
style in NAMR at ≈63% `[APPROX]`, and p.14 says its significance is "larger than the other style
factors, and incidentally **most industry and country factors**." A risk model keeps it because it
explains co-movement, not because it pays.

---

### C7-A · POLLING

**Story.** A local newspaper wants to know which way the town will vote. A reporter stops twelve people
outside the station and eight of them say the same thing, so the paper prints that two-thirds of the
town agrees. The next day a rival paper stops a different twelve people outside a different station and
gets exactly the reverse. Neither reporter did anything wrong; neither lied. A polling company then
does the job properly with a thousand people, gets a number, and — this is the part that matters —
publishes a second number beside it saying how far its answer would have moved if they had gone out on
a different day and stopped a different thousand. That second number is not a guess about the town. It
is a measurement of how much their own procedure wobbles. And it shrinks as the sample grows, but slowly:
to halve the wobble you need four times the people, which is why nobody polls a hundred thousand.

**Map.**

| In the story | In the model |
|---|---|
| the town | the thing you actually want to know about |
| the twelve people at the station | this month's cross-section of stocks |
| the reported two-thirds | the estimated factor return for this month |
| the rival paper's opposite result | what the same estimate would have been on a different sample |
| **the second number published beside the answer** | the standard error: how far the estimate itself wobbles |
| a big answer with a huge wobble | a large coefficient with a small t-statistic — L6's boss round |
| a small answer with a tiny wobble | a small coefficient that is nonetheless reliable |
| **the answer divided by its own wobble** | the t-statistic; p.8's bar is that ratio exceeding two |
| needing four times the people to halve the wobble | the square-root law — the `√n` the player will meet again |
| the paper printing only one number | the paper's own habit: it prints t-statistic *thresholds* (p.8, p.14) and never a standard error |

**The awkward question.** *"Where does the polling company get that second number from? They only ran
the poll once. How can they possibly know how much a poll they never conducted would have differed?"*

- **Landed** sounds like: from the spread *inside* the one sample they have. If the thousand answers
  disagree wildly among themselves, a different thousand would plausibly have landed somewhere quite
  different; if they nearly all agree, it would not. The wobble of the average is read off the scatter
  of the individuals. That is the entire trick and it is the thing the game gives the player that the
  paper never shows.
- **Not landed** sounds like: "from statistical theory" or "from the formula" — a name substituting for
  a mechanism. Dock bps under the NO NUMBER WITHOUT ITS ORIGIN rule and rebuild from the scatter.

**Where it breaks.** Polling has a fixed population sitting still while you sample it — the town's
opinion on Tuesday is a real thing that exists whether or not you measure it. There is no analogous
fixed truth for a factor return: the "population" here is a counterfactual set of markets that never
happened. A player who leans hard on the town will start talking about the "true" factor return as a
number in the world, and at L12 they must be able to say why that is a modelling fiction.

---

### C7-B · ASTRONOMY — SEEING

**Story.** An observer measures the position of a star. She takes one exposure and reads off a
position. Then she takes another, and another, through the night — and the readings differ, because
the air above the telescope is moving and the image dances. She ends up with a scatter of positions
around a centre. She reports the centre as her measurement of the star, and beside it she reports how
tightly the scatter clustered, because that is what tells the next astronomer how much to trust the
centre. On a still night the scatter is tiny and her measurement is worth a great deal. On a turbulent
night the same centre, computed the same way, is worth much less — and the only way anyone could know
the difference is the number she published beside it. A centre without a scatter is not a measurement.
It is a number.

**Map.**

| In the story | In the model |
|---|---|
| the star's actual position | the quantity you wish you knew |
| one exposure | one observation in the cross-section |
| the dancing image | the part of each return that no column explains — the misses |
| the centre of the scatter | the estimated coefficient |
| **the tightness of the scatter** | the spread of the residuals: the raw material of a standard error |
| how much the centre itself would move on a rerun | the standard error of the coefficient |
| a still night | small residual spread — a precise coefficient |
| a turbulent night | large residual spread — the same coefficient, worth much less |
| "a centre without a scatter is not a measurement" | why a coefficient without a standard error cannot be acted on |
| taking more exposures | more assets in the cross-section, shrinking the wobble by the square-root law |

**The awkward question.** *"The star doesn't move. If she stares long enough, doesn't the wobble go
away entirely — and if so, why can't we just use more data and stop worrying about standard errors?"*

- **Landed** sounds like: the wobble of the *centre* shrinks with more exposures, but it shrinks slowly
  and never reaches zero, and the wobble of each *individual* exposure never shrinks at all. In the
  model there is a second problem astronomy does not have: the underlying quantity moves. BFRE's answer
  to that is not "more data" but exponential decay — p.27, the default factor covariance calculation
  uses **104 weeks with a half-life of 26 weeks**, deliberately throwing old data away.
- **Not landed** sounds like: "yes, more data always helps" — the player has not met the trade-off the
  paper states on p.27, that forecasts "should be **responsive** to changes in the market environment
  whilst not being unduly **noisy**".

**Where it breaks.** Astronomical seeing is symmetric, well-behaved noise around a fixed truth. Residual
returns are not: the paper itself says smaller companies carry higher residual risk (p.25) and that
specific returns are "cleansed using robust methods to down-weight the influence of outlying
observations" (p.27), and it truncates currency factor returns at **±8% daily and ±20% weekly** before
covariance estimation (p.30). If the player leaves thinking the noise is uniform and tame, they will not
understand why any of that cleaning exists.

---

### C7-C · ECOLOGY — NETTING FISH

**Story.** A ranger must report how many fish are in a lake. She cannot count them, so she nets a
patch, counts what she catches, scales it up by how much of the lake she covered, and writes the total
in the report. Her supervisor sends it back and asks her to net four more patches. She does, and the
five totals disagree — one is nearly double another, because fish shoal and one patch happened to catch
a shoal. Now she reports the average of the five, and beside it the spread of the five, and the report
is finally usable: a manager reading it can see whether "one hundred thousand fish" means somewhere
between ninety and a hundred and ten thousand, or somewhere between forty and two hundred thousand.
Same headline number. Completely different decisions.

**Map.**

| In the story | In the model |
|---|---|
| the lake | the market you are trying to characterise |
| one netted patch | one period's cross-sectional regression |
| the count from one patch, scaled up | that period's estimated factor return |
| the five disagreeing totals | the factor return time series — the thing L7 builds |
| **the spread of the five** | the wobble of the estimate, measured directly by repeating |
| fish shoaling | correlated residuals — the reason the naive wobble is understated |
| the manager's decision changing | why a risk desk cannot act on a point estimate alone |
| netting more patches | more periods; p.8's "**15-year research history**" and "**five-year sub-samples**" |
| reporting how often a patch was decisive | p.8's actual practice: not one t-statistic, but the **proportion** of periods in which `|t| > 2` |

**The awkward question.** *"She got her spread by netting five times. But a regression is run once on
one month's data — you don't get five months of the same month. So where does the spread come from
when you can't repeat the experiment?"*

- **Landed** sounds like: two different sources, and the player should name both. Within one month you
  read it off the scatter of the residuals — that is the standard error, and it is what a t-statistic
  divides by. Across months you can genuinely repeat, and that is what BFRE actually reports: p.8 counts
  the **proportion** of monthly regressions in which the factor cleared `|t| > 2`, and p.15's Figure 1.8
  is nothing but that count, factor by factor.
- **Not landed** sounds like: only one of the two. Give partial bps and make them build the other.

**Where it breaks.** The lake has a definite number of fish; there is a right answer and the ranger is
approximating it. There is no definite factor return sitting in the market waiting to be netted. The
story also makes shoaling sound like an annoyance to be averaged away, whereas in this model the
shoaling *is the subject*: correlated movement between assets is exactly what the factors are for, and
what is left over after the factors is what `Δ` measures.

---

**RETURN TO BFRE.**

> "That ratio you just built — the size of the answer divided by how much the answer itself wobbles — is
> what page 8 calls a **t-statistic**, and BFRE's entire style list is chosen with it. Keep a factor if
> the ratio beats **2** often enough (page 8); stop adding factors once the best remaining candidate
> clears that bar less than **10–15%** of the time (page 12); consider a style for inclusion if it
> clears it more than **10%** of the time (page 14). Figure 1.8 on page 15 is the whole North America
> style list sorted by nothing else — and note that on that measure **Volatility comes first at roughly
> 63%** `[approximate — the figure prints no data labels]` while Table 1.2 on page 10 shows Volatility
> earning **−0.6% a year**. Significance and profit are different questions, and a risk model is asking
> the first one. Say the last part out loud too: the paper never shows you where a standard error comes
> from. You now know something it assumes."

---
---

# C8 · DEGREES OF FREEDOM

**Unlocks:** L6 (The Verdict), immediately after C7 · **Difficulty:** hard. Not graduate, but it is the
most commonly faked concept in the entire syllabus — a player who can only recite "n minus k" has
learned nothing.
**Jargon gate:** *degrees of freedom* unlocks at L6. **The phrase never appears in the paper.**
**Locked:** unbiased estimator, chi-square, Bessel's correction.

### BFRE anchor (verified)

**GAP first, because it dominates.** Zero hits for "degrees of freedom" across all 65 pages. The paper
never counts parameters against observations anywhere. Everything below is an *anchor for the idea*,
not a citation for the term.

| Nearest anchor | Page | What it gives you | Tag |
|---|---|---|---|
| "**effective number of assets**" | p.8 | One of four stated eligibility criteria for an industry factor — the paper does care how many assets stand behind a column, "to ensure that there are sufficient number of firms to calibrate a separate industry factor in our schema". **No numeric threshold is given for it, or for any of the four.** | PAPER |
| Observation counts, printed | p.28, Table 1.3 | Specific-risk model: daily — half-life **125 days**, **375** observations, Newey–West lag **10 days**; weekly (WRLD and EMKT) — **26 weeks**, **104 weeks**, **2 weeks**. Verified digit-for-digit at 4×. | PAPER |
| The covariance window | p.27 | Default WKL: **104 weeks** of factor returns, half-life **26 weeks**. | PAPER |
| The beta window | p.42 | Regression (1.12): **5 years of weekly observations**, exponential half-life **52 weeks**. | PAPER |
| Thin data, handled by hand | p.36 | "thinness corrections for country and industry factors where limited, or no data exists to reliably estimate those factor returns" — the paper's own admission that some columns do not have enough assets behind them. | PAPER |
| Thin history, handled by hand | p.28 | For IPOs and short histories, a cross-sectional overlay infers specific risk from assets of "similar market capitalisation, in the same industry and country". | PAPER |

---

### C8-A · PARTY GAME — THE ANNOUNCED AVERAGE

**Story.** Five friends play a game. Each will write a number on a card and turn it over at the end.
Before anyone writes, the host announces one rule: the five numbers, when the cards are turned, must
average out to exactly seven. The first friend writes whatever she likes. So does the second, the
third, the fourth. Then everyone looks at the fifth, who has no choice at all — his card is already
decided by the other four and the rule. He writes it, and someone at the table points out that they
have been playing a five-person game with four players in it. The rule did not remove a person. It
removed a *choice*.

**Map.**

| In the story | In the model |
|---|---|
| a card | one residual — one leftover miss |
| the five friends | the observations in the fit |
| the host's rule | a fitted parameter: each one imposes a condition the residuals must satisfy |
| **"they must average to seven"** | a balance condition, C3 — e.g. the misses being unable to line up with a column |
| the fifth friend having no choice | the last residual being determined by the others |
| four free choices, not five | degrees of freedom: observations minus fitted parameters |
| adding a second rule | fitting a second column — one more choice gone |
| a game with as many rules as friends | as many parameters as observations: every residual forced, nothing left to judge with |
| the friends still each writing a number | the residuals still all exist and are all non-zero — nothing was deleted |

**The awkward question.** *"All five friends still wrote a number. Nobody was removed from the game. So
in what sense is there 'less' information here — the cards are all still on the table?"*

- **Landed** sounds like: the cards are there but they are no longer five independent pieces of news.
  Knowing four of them tells you the fifth exactly, so the fifth carries nothing you did not already
  have. When you go on to judge how noisy the leftovers are, you must divide by the number of genuinely
  free ones, not by the number of cards — otherwise you will report the fit as tighter than it is.
- **Not landed** sounds like: "because we used up a degree of freedom" — the phrase being used to
  explain itself. Ask them to say it without the phrase.

**Where it breaks.** The party game has *exact* determination — one rule, one card fixed, cleanly. Real
fitted parameters do not pick out one specific residual to sacrifice; the constraint is spread across
all of them, and no individual residual is "the determined one". A player who thinks one particular
stock's miss has been fixed by the fit has taken the story too literally, and will look for it.

---

### C8-B · DRAFTING — THE LINE THROUGH TWO DOTS

**Story.** A draughtsman is given two dots on a sheet and asked to draw the straight line that best
fits them. He lays a straight edge on the dots and draws. The line passes exactly through both. He is
then asked how good the fit is, and he says, correctly, that the question has no answer — the line
touches every dot, the leftover is nothing at all, and that is not evidence of a good fit, it is
evidence of nothing. Give him a third dot and the situation changes completely: now the line generally
misses all three by a little, and for the first time there is something to look at. The size of those
three misses is the only report anyone can make about whether a straight line was the right idea. With
two dots there was no report to make; with three there is one dot's worth of evidence; with fifty
there is a great deal.

**Map.**

| In the story | In the model |
|---|---|
| a dot | one observation |
| the straight edge | the shape you have assumed — a line with two settings, a tilt and a height |
| laying it on two dots | fitting two parameters to two observations |
| **the line passing exactly through** | zero residuals, and therefore zero information about fit |
| "the question has no answer" | no degrees of freedom left: nothing remains with which to judge |
| the third dot | the first genuine degree of freedom |
| the three misses | the residuals that carry the evidence |
| fifty dots | a real cross-section — thousands of assets against dozens of columns |
| adding another bend to the straight edge | adding another parameter — one more dot's worth of evidence consumed |

**The awkward question.** *"A perfect fit is what we've been trying to achieve since Level 0. Now you
are telling me a perfect fit is worthless. Which is it?"*

- **Landed** sounds like: a perfect fit is worthless *when you had exactly as many settings as points*,
  because then it was guaranteed and tells you nothing about the world. A perfect fit with far more
  points than settings would be extraordinary. It is the ratio that carries the meaning, never the
  residual size alone. This is the sentence that makes p.32's `R²` — "the proportion of cross-sectional
  variation in asset returns explained" — readable rather than impressive.
- **Not landed** sounds like: "so we shouldn't want a good fit" — the wrong lesson entirely, and it will
  wreck L12, where the player has to argue about whether BFRE's factors are real or fitted.

**Where it breaks.** With two dots and a straight edge the determination is exact and visible. With
thousands of assets and dozens of columns nobody ever sees the residuals collapse to zero, so the
concept stops being visual and becomes an accounting rule — and that is the moment players start
faking it. Keep this analogy for building the idea, then force them to state the *counting* rule out
loud (C8-A does that better) so the idea has both a picture and a procedure.

---

### C8-C · HOUSEHOLD BUDGET — THE LAST ENVELOPE

**Story.** A household divides the month's money into envelopes on the kitchen table — rent, food,
transport, and so on down to a last envelope for whatever is left. They can argue about how much goes
in the first envelope, and the second, and every one after that. They cannot argue about the last one:
by the time they get to it, its contents are simply what remains. Someone new to the household asks why
they bother having a last envelope at all if nobody ever decides its amount. The answer is that they
do not decide it, but they do *read* it — if the last envelope is thin every month, the household is
overcommitted, and if it is fat, they have room. The envelope carries information precisely because
nobody chose it.

**Map.**

| In the story | In the model |
|---|---|
| the month's money | the total variation in returns you are trying to account for |
| an envelope you argue about | a fitted parameter — a column's coefficient |
| **the last envelope** | what is left after the fit: the residuals |
| its contents not being chosen | residuals are not free parameters; they are the remainder |
| reading it to see if you are overcommitted | using residual size to judge the model |
| more envelopes to argue about | more columns fitted |
| **each new envelope taking from the same pot** | each parameter reducing what remains to judge with |
| a household with as many envelopes as pounds | as many parameters as observations — nothing left to read |
| a thin last envelope every month | small residuals — and, at L9, a small `Δ` |
| a fat last envelope | large residuals — and the p.35 pie, where **Specific is 50%** of Active Risk |

**The awkward question.** *"Adding an envelope doesn't destroy money — the money is still in the house.
So why does adding a column destroy anything?"*

- **Landed** sounds like: nothing is destroyed, it is *reallocated*, and that is exactly the point. Every
  pound moved into a chosen envelope leaves the unchosen one, which is the one you were using to judge
  yourself. The paper does this reallocation for real and shows the arithmetic on p.16: before a
  small-cap factor existed, the smallest deciles carried significant structure inside the residuals —
  roughly **10.8%** and **21.1%** `[APPROX]` — and after the factor was added, they did not. The
  explanation moved from the last envelope into a named one.
- **Not landed** sounds like: "adding columns is bad" or "adding columns is good" — the player has taken
  a side instead of describing a transfer. There is no side; there is a trade, and L9 is where the trade
  gets priced.

**Where it breaks.** Household money is exactly conserved and integer-valued; explained variation is
neither, and adding a column that is pure noise still moves *something* into it — which is precisely why
a random placebo is worth carrying, and why it is notable that Table 1.4 (p.56) lists a style called
**"Random"** with a single substyle, **"Random Substyle"**, in BFRE's own inventory of everything
investigated. The envelope story cannot explain that; use it as the hook into L12.

---

**RETURN TO BFRE.**

> "The counting you just did has a name at every other desk in the world and **no name in this paper** —
> zero mentions of degrees of freedom in sixty-five pages. What the paper does instead is set counts by
> hand and print them: **375 observations** for the daily specific-risk model and **104 weeks** for the
> weekly one, in Table 1.3 on page 28; **104 weeks** for the default factor covariance matrix on page 27;
> **5 years of weekly observations** for the beta regression on page 42. And on page 8 it lists 'a large
> **effective number of assets**' as one of four criteria for admitting an industry factor — and gives a
> numeric threshold for none of the four. Hold that for Level 12."

---
---

# C9 · CROSS-SECTIONAL VERSUS TIME-SERIES ESTIMATION

**Unlocks:** L7 (The Timeline) · **Difficulty:** ordinary to state, hard to defend. The boss round is
"why did BFRE choose this, and what does the choice cost".
**Jargon gate:** *cross-sectional regression* unlocks at L7 and **is** the paper's own core phrase
(pp.7, 24, 30, 32). *In-sample / out-of-sample* waits for L12 — "out-of-sample" appears once, p.30;
"in-sample" never.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The design | p.24 | Estimation is "a series of **cross-sectional** regressions of asset returns against asset factor exposures, which provides estimates of factor returns and asset specific returns." | PAPER |
| The cadence | p.24 | "These regressions are performed **daily** for country and regional models and **weekly** for the World model." **No justification given for the weekly choice.** | PAPER |
| Executive-summary version | p.3 | "Model estimation is performed in cross-section **in two-passes**"; daily factor returns for all models **from March 1996 onwards**. | PAPER |
| The one place BFRE *does* run a time series | p.42 | Equation (1.12): weekly excess returns, **5 years**, exponentially weighted with a **52-week half-life**, against the cap-weighted Estimation Universe. But its output enters BFRE as an **input substyle to Volatility** (Historical Beta) — never as the exposure mechanism. | PAPER |
| The rival design | p.2 | BFRE is positioned against **STORM**, Aladdin's existing equity approach, which builds an asset-by-asset covariance matrix from asset returns alone — each asset effectively its own factor. *(That characterisation of STORM is the transcriber's gloss in `notes/`, not a printed quotation; the printed clause that **is** quotable is the next one.)* BFRE "imposes far more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of factors, which capture the most important sources of asset return commonality". | PAPER + gloss |
| What the choice buys | p.2 | Return-only forecasts "can quickly become misleading if a company undergoes changes in its operating activities, or is subject to corporate actions, or experiences changes to its capital structure"; a fundamental model reflects these "immediately", a returns-only model "only gradually". | PAPER |
| What the choice costs | p.13 | AOL's market-cap substyle exposure rose with the share price while its sales substyle stayed low — the exposure moves with the very thing the model is trying to forecast. Figure 1.6 values are `[APPROX — pixel-measured against warped gridlines]`. | PAPER + `[APPROX]` |
| The horizon | p.30 | "The forecast horizon of the model is **1-month**"; style and industry factors are "selected by assessing explanatory power using **monthly cross-sectional regressions**". | PAPER |

---

### C9-A · FORESTRY — ONE AFTERNOON VERSUS FORTY YEARS

**Story.** Two foresters want to understand how trees grow. The first spends a single afternoon in the
wood with a measuring pole and records the height of five hundred trees, along with how much light each
one stands in, how deep its soil is, how close its neighbours are. By evening she can say a great deal
about how height relates to light and soil — across the whole wood, as it stands today. The second
picks one tree and measures it every year for forty years. At the end he knows that tree's life in
extraordinary detail and can say exactly how it responded to the drought of a particular decade. Then a
new sapling is planted. The first forester can place it in her picture immediately — she knows its
light and soil today. The second can say nothing at all about it for many years, because it has no
history. Both are doing real science. They are answering different questions, and only one of them can
answer on the first day.

**Map.**

| In the story | In the model |
|---|---|
| the wood on one afternoon | one period's cross-section of stocks |
| a tree's height that afternoon | that stock's return this period |
| light, soil, crowding | the columns of `X` — measured characteristics |
| the first forester's relationship | the factor returns from one cross-sectional regression |
| repeating the afternoon every week | "a series of cross-sectional regressions" (p.24), daily for regional models |
| the second forester's forty years on one tree | a time-series regression on one asset — BFRE does this exactly once, at (1.12), p.42 |
| the newly planted sapling | a new listing, an IPO |
| **placing the sapling on day one** | why BFRE uses observed characteristics: they exist immediately (p.2) |
| the second forester having nothing to say | a returns-only model needing history before it can speak |
| a tree that was transplanted last month | a company after a corporate action or capital-structure change — p.2's stated case |

**The awkward question.** *"The first forester measures light and soil with a pole and her eyes, five
hundred times in an afternoon. Isn't every one of those measurements sloppier than the second
forester's careful annual reading — and doesn't all that sloppiness go straight into her conclusion?"*

- **Landed** sounds like: yes, and that is precisely the price. The characteristics are measured with
  error every single period, and the error goes straight into the factor returns, then into `F`, then
  into every risk number. The paper hands you the sharpest example itself on p.13: AOL's market-cap
  measure of size rose with its share price, so "a measure of size based on market capitalisation alone
  would confer large-size status on AOL, and **reduce its risk forecast accordingly**" — the exposure
  moved with the thing being forecast, in the wrong direction, on exactly the name where it hurt.
- **Not landed** sounds like: "you use lots of stocks so the errors cancel" — a real effect, but it does
  not touch a *systematic* mismeasurement like the AOL one, and the player must see the difference.

**Where it breaks.** Trees hold still and light and soil are genuinely exogenous — nothing about
measuring the wood changes the wood. Market characteristics are not exogenous: market capitalisation is
a price, the very quantity whose movement we are modelling, so a column of `X` and the returns in `r`
are entangled in a way soil depth and tree height are not. That entanglement is the deepest criticism
available at L12 and the forestry story hides it. Break it deliberately.

---

### C9-B · EPIDEMIOLOGY — SCREENING DAY VERSUS THE COHORT

**Story.** A health authority runs a screening day: ten thousand people through a hall in one day,
each weighed, measured, blood-pressured, and asked what they eat and whether they smoke. By the end
they can describe, with great confidence, how blood pressure sits alongside weight and smoking across
that whole population, on that day. In the same building another team runs a study that has followed
two hundred people for thirty years, and knows things the screening day can never see — that this
individual's pressure climbed after his divorce, that hers fell when she moved house. When someone
turns eighteen and appears in the town, the screening team has a number for them by lunchtime; the
cohort team will have one in thirty years. And when a drug is withdrawn from the market overnight, the
screening team can measure the town's new state the following week, while the cohort team's model still
contains the drug's effect, fading only gradually as new years accumulate.

**Map.**

| In the story | In the model |
|---|---|
| screening day | the cross-sectional regression, p.24 |
| one person in the hall | one stock |
| blood pressure that day | that stock's return this period |
| weight, smoking, diet | the columns of `X` |
| the relationship the screening finds | the estimated factor returns, `f` |
| running the screening every month | the factor return time series that L7 builds |
| the thirty-year cohort | a time-series regression — BFRE runs one, (1.12), p.42, and only as an input |
| the eighteen-year-old measured by lunchtime | a new listing with immediately computable exposures |
| **the withdrawn drug** | p.2 exactly: a change in operating activities, a corporate action, a capital-structure change, reflected "immediately" versus "only gradually" |
| the cohort's richer causal story | what BFRE gives up: no per-asset history is used to set an exposure |

**The awkward question.** *"The screening day can tell you smokers have higher pressure. It cannot tell
you smoking raised anyone's pressure. If the cross-section can't see causes, what exactly is BFRE
claiming when it says a factor 'explains' returns?"*

- **Landed** sounds like: it is claiming co-movement, not cause, and it says so — p.32 defines `R²` as
  "the proportion of cross-sectional variation in asset returns **explained** by the set of common
  factors", which is an accounting statement about variation, not a causal one. The behavioural stories
  the paper does tell (investors "overreacting" for reversal, p.16; "systematically underreacting" for
  momentum, p.17) are exactly the unfalsifiable parts the L12 brief names.
- **Not landed** sounds like: any answer containing the word "causes". A risk model does not need
  causation and does not claim it; a player who thinks it does will defend the wrong hill at L12.

**Where it breaks.** Epidemiology has a real intervention available — you can stop someone smoking. Nobody
can intervene on a stock's book-to-price to see what happens. Also, in a health screening the
characteristics genuinely predate the outcome; in the market several exposures are computed *from*
prices (Historical Beta at p.42, Reversal's one-month return at p.16, market cap at p.13), so the arrow
of time is muddier than the story allows.

---

### C9-C · EDUCATION — CLASS RANK VERSUS REPORT CARD

**Story.** A school has two ways of talking about a pupil. One is the rank order after Friday's test:
everyone sat the same paper on the same morning, and the ordering is immediate, comparable, and
available for a pupil who arrived on Wednesday. The other is the report card built from four years of
that pupil's own marks: far richer about that individual, useless for a new arrival, and slow to notice
when a pupil's circumstances change — a child whose family situation collapses in September still reads
as a strong pupil on a report card averaged over four years. A new head teacher asks which the school
should use to decide who needs support this term. The answer is not that one is better. It is that only
one of them can answer *this term*, for *everyone*, including the child who arrived on Wednesday.

**Map.**

| In the story | In the model |
|---|---|
| Friday's test | one period's cross-section |
| a pupil | a stock |
| the mark on Friday | that period's return |
| what the school knows about each pupil beforehand | the exposures in `X` |
| the rank order across the class | the cross-sectional relationship the regression extracts |
| running the test every Friday | daily regional regressions, weekly for the World model (p.24) |
| the four-year report card | a time-series estimate on one asset |
| the pupil who arrived Wednesday | a new listing |
| **the pupil whose life changed in September** | p.2's company that "undergoes changes in its operating activities… or experiences changes to its capital structure" |
| the report card being slow to notice | returns-only models incorporating change "only gradually" (p.2) |
| an unfair test on a bad Friday | measurement error in `X` and `r` entering every single period |

**The awkward question.** *"If you rank the class every Friday, a pupil's position bounces around week
to week. Doesn't that make the whole scheme noisier than the report card, not better?"*

- **Landed** sounds like: it is noisier per period and that is accepted deliberately, because the
  *series* of weekly answers is itself the product — L7's output is a row of numbers, and L8 measures
  how that row wobbles. The paper does exactly this: Table 1.2 (p.10) reports the annualised return,
  volatility, Sharpe and autocorrelation of each factor, all computed from that series, over Mar 1996 –
  Dec 2013.
- **Not landed** sounds like: "you average the weeks" — close but too crude; BFRE does not simply
  average, it weights recent observations more, with an exponential decay whose default half-life is
  **26 weeks** over **104 weeks** of data (p.27).

**Where it breaks.** School tests are designed to be comparable; nobody designs the market to be
comparable across months, and the estimation universe itself is rebuilt "on a country-by-country basis
every month" (p.24). Also, ranking implies an ordering with no units, whereas factor returns are in
percent and are added up into cumulative series (Figures 1.7, 1.12, 1.14). If the player starts treating
factor returns as ranks they will not be able to build `F`.

---

**RETURN TO BFRE.**

> "Run your one-day calculation again tomorrow, and the day after, and the row of numbers you build is
> what page 24 means by 'a series of **cross-sectional** regressions of asset returns against asset
> factor exposures' — done **daily** for country and regional models and **weekly** for the World model,
> back to **March 1996** (page 3). Table 1.2 on page 10 is the average and the spread of that row.
> Figures 1.7, 1.12 and 1.14 are that row added up. And page 2 tells you why BFRE built it this way
> rather than the way STORM does — a returns-only model incorporates a corporate action or a
> capital-structure change 'only gradually', where a fundamental model reflects it 'immediately'. Page
> 13 is the bill for that choice: AOL, whose market-cap size exposure rose with its share price."

---
---

# C10 · THE COVARIANCE MATRIX AS A WEATHER MAP

**Unlocks:** L8 (The Weather Map) · **Difficulty:** the *idea* is ordinary; the level around it is the
game's largest gap between what the player must build and what the paper contains. Say that at the start.
**Jargon gate:** *covariance matrix* and *half-life* unlock at L8; both are the paper's words (p.24,
p.27). *Covariance* itself was unlocked at L5. **Locked at C10:** eigenvalue (that is C11), positive
semi-definite, shrinkage (C13).

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| `F`'s name and place | p.24 | Equation (1.8) `Σ = X F Xᵀ + Δ`; "`F` : factor covariance matrix". | PAPER |
| How it is built | p.27 | "The BFRE factor covariance matrices use a history of **daily** factor return series starting in **March 1996**. Observations are weighted using an **exponential decay** that places more emphasis on recent factor returns to give more responsive risk forecasts." | PAPER |
| The default recipe | p.27 | "The default factor covariance matrix calculation for all BFRE models is **WKL (weekly long-term)**, which uses **104 weeks** of factor returns with a **half-life of 26 weeks**." | PAPER |
| The trade-off, in the paper's words | p.27 | Forecasts "should be **responsive** to changes in the market environment whilst not being unduly **noisy** so as to render them unstable and unusable." | PAPER |
| Pre-treatment | p.30 | Currency factor returns truncated before covariance estimation: **±8%** daily, **±20%** weekly, "to remove outliers". | PAPER |
| A readable slice of `F` | p.10, Table 1.2 | "Correlation with Market Factor": Volatility **0.84**, Liquidity **0.69**, Size **0.23**, Momentum **−0.02**, Reversal **−0.32**. These are correlations **between factor returns** — genuine `F` content. | PAPER |
| **Not** `F` | p.11 | Figure 1.3 is *exposure* correlation, the columns of `X`, one date. Do not let the player conflate them. | PAPER |
| Where the paper stops | p.27 | "Model users are referred to the **BRS Covariance Matrix Estimation documentation** for technical details on the factor covariance matrix methodology." | PAPER |

---

### C10-A · METEOROLOGY

**Story.** A regional forecaster is asked to advise on whether to run an outdoor festival across three
towns on the same weekend. Her first instinct is to give three separate forecasts: how gusty each town
gets on a bad day. She does, and the organiser — who has to hire marquees — asks a better question:
when Town A is being blown about, is Town B usually being blown about too, or is it usually calm?
Because if the three towns get their rough weather on different days, the organiser can move marquees
around and needs fewer of them; if all three blow at once, he needs three full sets. So her real
product is not three numbers. It is three numbers *plus* a small table of which towns blow together —
and the marquee bill depends on the table more than on the numbers.

**Map.**

| In the story | In the model |
|---|---|
| a town | a factor |
| how gusty one town gets | that factor's own volatility — a diagonal entry of `F` |
| **whether two towns blow together** | the covariance between two factor returns — an off-diagonal entry of `F` |
| the whole table | `F` itself, equation (1.8), p.24 |
| the festival's marquee bill | the portfolio's risk number |
| towns that blow on different days | offsetting factor bets that partially cancel |
| towns that blow together | factor bets that compound — e.g. Volatility and the market at **0.84** (p.10) |
| the forecaster's history of past weekends | daily factor returns since **March 1996** (p.27) |
| weighting recent weekends more | the exponential decay, half-life **26 weeks** over **104 weeks** (p.27) |
| the forecaster refusing to use 1970s weather | why old observations are decayed rather than averaged in |
| a freak once-a-decade storm | the outliers p.30 truncates for currencies, at **±8%** daily and **±20%** weekly |

**The awkward question.** *"She has three towns and a small table. How big does the table get if she has
a hundred towns — and does she actually have enough past weekends to fill it?"*

- **Landed** sounds like: the table grows far faster than the list of towns, so a hundred towns need
  thousands of pairwise entries, and there is no reason at all to assume the number of past weekends
  keeps up. That is exactly C12, and it is the L8 boss round. Award the callback.
- **Not landed** sounds like: "you just need more history" — the paper's own default uses **104 weeks**
  (p.27), which is the whole point of the boss round.

**Where it breaks.** Weather covariance is a stable physical fact about geography; two towns forty miles
apart will still be forty miles apart next year. Factor co-movement is not stable — the paper builds its
entire estimation around that instability (the half-life exists solely to let the estimate *change*).
Worse for the analogy: a forecaster can look out of the window and check. Nobody can look at `F`; the
paper itself defers the method to a separate document (p.27), so this is one map whose maker's working
you cannot inspect.

---

### C10-B · TRAFFIC — A CITY'S JUNCTIONS

**Story.** A city keeps records on twenty junctions. For each one it knows how badly it jams on a bad
day. The transport chief needs to know something the twenty numbers cannot tell her: how bad is the
*worst morning for the city*. She has two possible worlds. In one, the junctions jam independently —
the ring road seizes on Tuesday, the bridge on Thursday, and the city is never in crisis, because
drivers reroute. In the other, they all jam together, because they all fail when it rains, and then the
whole city stops at once. The twenty individual numbers are identical in both worlds. Only a record of
which junctions jam *at the same time* separates them, and it is the only record she can plan from.

**Map.**

| In the story | In the model |
|---|---|
| a junction | a factor |
| how badly one junction jams | that factor's own volatility |
| **which junctions jam together** | the off-diagonal entries — factor covariances |
| the worst morning for the whole city | the portfolio's total risk |
| drivers rerouting | offsetting factor exposures cancelling |
| everything failing when it rains | positively correlated factors compounding |
| the two worlds with identical junction numbers | two models with identical diagonals and completely different total risk |
| the daily jam log | the daily factor return series since March 1996 (p.27) |
| last month's log mattering more than last decade's | the exponential decay, 26-week half-life (p.27) |
| a junction closed for roadworks all year | a factor with too little data — the thinness problem (p.36) |

**The awkward question.** *"Suppose two junctions never jam together, ever. Does the city then have no
risk of a bad morning at all?"*

- **Landed** sounds like: no — each junction still jams on its own, and the diagonal never goes away.
  Perfect offsetting reduces the *combined* effect below the sum, but the individual variability is
  still there, and on top of it every road has its own private accidents that no junction model
  captures. Those private accidents are `Δ`, and on the sample report on p.35 they are **50% of Active
  Risk**. That is a clean pre-echo of L9 and L10.
- **Not landed** sounds like: "yes, they cancel" — the player has confused negative correlation with
  guaranteed offset, which is the exact error that makes a hedged book look riskless.

**Where it breaks.** Junctions are physically connected — there is a mechanism, a road, joining them —
and the analogy invites the player to look for the mechanism linking two factors. There often is none;
covariance is a measured association, and the paper never claims a causal channel between, say,
Liquidity and the market factor. It reports the number (0.69, p.10) and offers an economic *story*
(p.19: "Liquid securities generally have a higher correlation to the market… liquid stocks react more
quickly to general economic news flow"), which is a story, not a road.

---

### C10-C · POWER GRID — THE COINCIDENT PEAK

**Story.** A grid operator must decide how much generating capacity to build for a region of ten towns.
Each town's electricity manager sends the town's peak demand. The naive plan is to add the ten peaks
together and build that much. The operator does not, because she knows the ten peaks do not happen at
the same moment: the steelworks town peaks at three in the morning, the commuter towns at seven in the
evening. So she builds for the *coincident* peak — the largest total the region ever actually draws at
one instant — which is far less than the sum. Then a cold snap arrives and every town's heating comes on
in the same hour, the coincident peak jumps almost to the sum of the individual peaks, and the operator
has a very bad night. What she needed all along was not ten numbers but a record of how the ten demands
move together, including how that togetherness behaves in a crisis.

**Map.**

| In the story | In the model |
|---|---|
| a town's demand | a factor's return |
| a town's peak demand | that factor's volatility |
| **the coincident peak** | portfolio risk — the total, computed with co-movement included |
| the naive sum of ten peaks | risk computed as if factors could not offset — a hard overstatement |
| the steelworks peaking at three a.m. | negatively or weakly correlated factors |
| **the cold snap** | a regime in which correlations rise together |
| the operator's very bad night | a risk model that was calibrated on calm data |
| weighting last winter over ten winters ago | the exponential decay: responsiveness bought at the cost of noise (p.27) |
| the operator's dilemma about how much history to use | p.27 verbatim: responsive "whilst not being unduly noisy so as to render them unstable and unusable" |
| the grid's own local faults | `Δ` — what no shared pattern reaches |

**The awkward question.** *"If correlations jump in a crisis, then a table built from the last two
years of calm is exactly the wrong table for the only night that matters. Why does the model use it?"*

- **Landed** sounds like: that is the real criticism and it is worth making properly. The paper's only
  lever is the half-life — **26 weeks** over **104 weeks** (p.27) — which makes the estimate react
  *after* the regime changes, not before. The paper never claims otherwise; what it claims is a
  balance between responsive and noisy. And note the honest limit: p.27 hands the actual methodology to
  the **BRS Covariance Matrix Estimation documentation**, which the player does not have. The most
  important matrix in the model is documented elsewhere.
- **Not landed** sounds like: "that's what stress testing is for" — a real answer in the industry, but
  nothing in this paper supports it; the only surveillance described is bias statistics and VaR
  back-tests (p.38). Do not let a real-world platitude stand in for a page.

**Where it breaks.** A grid's coincident peak is a measurable physical quantity that actually occurs on
some real night. Portfolio risk is a forecast statistic that never occurs — no day is "the risk day".
The analogy also makes capacity sound like a decision variable of the same kind as the forecast; in the
model, forecasting and position-taking are separate jobs, and BFRE explicitly does the first one (p.24)
and feeds the second (p.34).

---

**RETURN TO BFRE.**

> "The grid you just built is `F` in equation (1.8) on page 24 — the **factor covariance matrix** — and
> page 27 tells you exactly how BFRE fills it: daily factor returns going back to **March 1996**,
> weighted so recent observations count more, with the default being **WKL, 104 weeks of factor returns
> and a half-life of 26 weeks**. You can read a real slice of it in Table 1.2 on page 10 — the
> Correlation-with-Market column, where Volatility sits at **0.84** and Reversal at **−0.32**. Two
> warnings. Figure 1.3 on page 11 is *not* this matrix — that is correlation between the *columns of
> X*, which is a different object with the same word attached. And page 27 is where the paper stops
> talking: the rest of the method is deferred to the BRS Covariance Matrix Estimation documentation,
> which is not in your hands."

---
---

# C11 · EIGENVALUES — THE DIRECTIONS OF MOST WOBBLE

> **DIFFICULTY: GRADUATE-LEVEL. Say so before the story, and say the second thing too:** the words
> *eigenvalue*, *eigenvector* and *principal component* **appear nowhere in the 65 pages**. Zero hits in
> `notes/`. This construction is entirely the game's; the paper does not contain it and does not need it
> to state its own method. The player is being given a tool for L12 and for the rest of their career,
> not a reading of the document.

**Unlocks:** L8 · **Jargon gate:** *eigenvalue* unlocks at L8 — but see above; when you use it, say
"this is a word from outside the paper".

### BFRE anchor (verified) — what you *can* point at

| Anchor | Page | What it gives you | Tag |
|---|---|---|---|
| One direction dominating, on a real day | p.5, Fig 1.1 | 8 August 2011, EMEA: every one of 19 country indices shows a large negative **market**-factor bar of roughly uniform size, plus small mixed contributions from the other blocks. The paper's own words: "the dominant source of return is clearly due to a broad weakness across markets, which is captured by the market factor." Bar heights are `[APPROX — read off gridlines only; no data labels printed]`. | PAPER + `[APPROX]` |
| The same picture with the dominant direction removed | p.6, Fig 1.2 | 16 August 2011: "the market factor contribution is no longer the largest source of return", and large index returns are attributed mainly to the **country** factor. `[APPROX]` for all magnitudes. | PAPER + `[APPROX]` |
| A measured shadow of the first direction | p.10, Table 1.2 | Correlation with the market factor: Volatility **0.84**, Liquidity **0.69**, Reversal **−0.32**, Size **0.23**, Momentum **−0.02**. | PAPER |

**INFER, and label it:** Figures 1.1 and 1.2 are as close as the paper comes to displaying "one
direction carrying most of the day's variation, and then what is left once you take it out". Use them as
an *illustration* of the idea. Never say the paper decomposes anything.

---

### C11-A · NAVAL — A SHIP'S ROLL

**Story.** A ship in an awkward sea is moving in several ways at once. It rolls side to side, pitches
bow to stern, yaws, heaves. Ask any sailor which of these is worst and they will not hesitate: she
rolls. She rolls far more than she pitches, and she has always rolled more than she pitches, in every
sea she has ever been in, because of the shape of the hull. The sea is disorganised and throws energy at
her from all directions; the ship converts almost all of it into one particular motion. So if you want
to describe how this ship moves in one sentence, you say "she rolls" — and if you want two sentences,
you add "and she pitches a little". You are not describing the sea. You are describing which motions the
hull is willing to make, ranked by how much it makes them.

**Map.**

| In the story | In the model |
|---|---|
| the sea's disorganised push | the raw variation in the factor returns |
| the hull | the covariance matrix `F` |
| roll, pitch, yaw, heave | directions in which a set of factor bets can move |
| **rolling more than pitching** | one direction carrying more variance than the others |
| the roll axis | the first eigenvector — the direction of most wobble |
| how much she rolls | the first eigenvalue — the size of the wobble in that direction |
| "and she pitches a little" | the second direction, at right angles, carrying less |
| motions the hull barely makes at all | directions with tiny eigenvalues |
| the ranking being a property of the hull, not the sea | the decomposition being a property of `F` |
| describing the ship in one sentence | summarising a large matrix by its biggest direction |

**The awkward question.** *"Rolling and pitching are given to us — the ship has a bow and a beam. What
picks out the special directions when there is no hull to look at, just a table of numbers?"*

- **Landed** sounds like: the numbers themselves do. You look for the combination of factor bets whose
  wobble is largest, then the largest one at right angles to that, and so on down. Nothing needs to be
  named in advance; the directions come out of the table. That answer is the whole concept and it is
  worth full bps.
- **Not landed** sounds like: "you choose the important factors" — no. The directions are generally
  *mixtures* of factors, not individual factors, and that distinction is the thing that makes the
  concept useful.

**Where it breaks.** A ship's roll axis is fixed by naval architecture and does not change with the
weather. `F` is re-estimated continuously with an exponential decay (p.27), so its directions move,
and a "direction of most wobble" computed on 104 weeks of data is itself an estimate with all the
frailties of C7 and C12. The hull image makes the decomposition feel permanent. It is not.

---

### C11-B · TAILORING — GRAIN AND BIAS

**Story.** A tailor hands an apprentice a square of woven cloth and asks him to pull it. He pulls
along the line of the threads and it barely gives. He pulls across the threads and it gives a little
more. Then he pulls corner to corner, at forty-five degrees to both, and it stretches noticeably and
goes slack and drapes. The tailor makes the point that matters: these directions belong to the cloth,
not to him. Whoever picks up this square, whatever angle they *think* they are pulling at, the cloth
will always give most on the diagonal and least along the grain. That is why a skirt cut on the bias
hangs the way it does and a skirt cut on the grain does not. A good tailor learns the two special
directions of every cloth and cuts with them, because fighting them is the one thing that guarantees a
bad garment.

**Map.**

| In the story | In the model |
|---|---|
| the square of cloth | the factor covariance matrix `F` |
| pulling in some direction | putting on a particular combination of factor bets |
| how much it gives | how much risk that combination carries |
| **the bias, where it gives most** | the direction of most wobble — the first eigenvector |
| how far it stretches on the bias | the first eigenvalue |
| the grain, where it gives least | the direction of least wobble |
| the directions belonging to the cloth | the decomposition being a property of `F`, independent of who asks |
| every other pull being a blend of the two | any factor bet decomposing into these directions |
| a garment cut on the bias | a portfolio unknowingly loaded onto the biggest direction |
| a tailor who learns the cloth | a risk manager who knows where their portfolio sits relative to the big directions |

**The awkward question.** *"He found the bias by pulling in a lot of directions until one gave most.
That is trial and error. Is there really nothing better than trying every direction?"*

- **Landed** sounds like: the trying-every-direction picture is the *definition*; the arithmetic that
  finds it without trying is a separate machine, and the honest thing at this level is to say the
  definition is what matters and the machine is graduate work. **NAME THE BEDROCK**: "the direction with
  the most wobble" is the definition; everything else is computation.
- **Not landed** sounds like: bluffing about a method they cannot describe. Do not accept it. This is a
  level where "I know what it means and I do not yet know how to compute it" is the correct, full-marks
  answer.

**Where it breaks.** Cloth is two-dimensional with exactly two special directions, and both are
physically visible. `F` has as many directions as it has factors — dozens, and in the World model far
more — and most of them are not interpretable as anything at all. Also, a cloth's grain does not depend
on how much cloth you were given; `F`'s directions absolutely do depend on how many periods you
estimated it from, which is precisely C12.

---

### C11-C · SEISMOLOGY — THE FAULT AXIS

**Story.** A seismology station records ground motion at a site for years. The record is a mess: every
tremor arrives from a different place and shakes the ground in a different way. But when the analyst
plots all of it together, an axis appears. The ground has moved far more along one particular line than
along any other, and much less along the line at right angles to it. Nobody chose that axis. It is a
consequence of the fault system underneath, and once it is known, engineers building on that site brace
for that direction first, because that is where the energy has always gone. The individual tremors were
unpredictable; the axis is not.

**Map.**

| In the story | In the model |
|---|---|
| an individual tremor | one period's factor returns |
| the years of record | the estimation window — p.27's 104 weeks, or longer |
| the mess of directions | raw, uninterpreted factor co-movement |
| **the axis that emerges** | the direction of most wobble |
| how much motion along it | the size of that wobble — the first eigenvalue |
| the quiet perpendicular direction | a low-wobble direction |
| the fault system underneath | the structure in `F` producing the pattern |
| engineers bracing for that direction | risk management aimed at the dominant direction |
| tremors staying unpredictable | individual periods remaining unforecastable — the model forecasts risk, not return |
| a new fault opening | the structure changing; the reason for exponential decay (p.27) |

**The awkward question.** *"How many years of record do you need before you trust the axis? Could a
short record show you an axis that isn't really there?"*

- **Landed** sounds like: absolutely — with a short record you can always draw an axis, and with a
  record shorter than the number of directions you are trying to describe, you are guaranteed to find
  directions in which the ground appears never to have moved at all. That is C12, and it is the L8 boss
  round. The player who reaches it unprompted from this question has earned the promotion.
- **Not landed** sounds like: a number pulled from the air ("about ten years"). No number is defensible
  here; the answer is a relationship between the length of the record and the number of directions.

**Where it breaks.** Seismology has a genuine physical cause under the ground, so the axis has an
explanation and a claim to permanence. `F`'s big direction usually has neither; it is a summary of what
has recently happened, and if the player starts saying "the market factor *is* the first eigenvector",
correct it — that is a plausible guess, and this paper contains no decomposition with which to check it.

---

**RETURN TO BFRE.**

> "Say this part first: **the words eigenvalue and principal component do not appear anywhere in this
> paper** — I checked all sixty-five pages. What the paper does show you is page 5, Figure 1.1: on
> 8 August 2011, across nineteen EMEA country indices, one direction swamped everything — every index
> shows a large negative **market** bar of roughly the same size, and the text says 'the dominant source
> of return is clearly due to a broad weakness across markets'. Then page 6, Figure 1.2, 16 August 2011:
> take that direction away and what is left is mostly **country**. That is the idea you have just built,
> illustrated on two consecutive trading days — and be honest that the bar heights on both figures are
> read off gridlines, because the paper prints no data labels at all."

---
---

# C12 · WHY A COVARIANCE MATRIX FROM FEWER PERIODS THAN FACTORS IS STRUCTURALLY BROKEN

> **DIFFICULTY: GRADUATE-LEVEL, and the paper does not go here at all.** Say both things. There is no
> factor count, no observation-to-factor ratio and no rank discussion anywhere in the 65 pages. Zero
> hits for "rank deficient", "eigen", "principal component". This is the game's argument, built out of
> numbers the paper does print. Say "this is my argument, not BlackRock's" out loud, once, and mean it.

**Unlocks:** L8 boss round · **Jargon gate:** *rank*, *singular*, *degenerate* — none of them are the
paper's words. Prefer plain English: "there are directions the data has never seen."

### BFRE anchor (verified) — the printed numbers you build on

| Ingredient | Page | Value | Tag |
|---|---|---|---|
| Observations in the default factor covariance matrix | p.27 | **104 weeks**, with a **26-week half-life** | PAPER |
| How much less the oldest week counts | p.27 → arithmetic | 104 weeks is exactly **four half-lives**, so the oldest observation carries **one sixteenth** the weight of the newest | INFER (our arithmetic from the paper's two numbers; exact) |
| NAMR industry factors | p.57, Table 1.5 | **54 rows**. *The count is the transcriber's — the page prints no total.* | PAPER + counted |
| NAMR styles | p.10, Table 1.2 | **12 styles plus the market factor** | PAPER |
| Country and currency blocks | p.3, p.5, p.6 | Every regional model carries country factors and "a series of currency factors"; **the paper prints no count for either** | PAPER + GAP |
| Candidate substyles screened | p.10, p.55, p.56 | p.10: "over 200 substyles", formally **N ≥ 200**. p.55: the printed inventory "is a subset of the full list of **200+**", because each horizon variant counts as a separate substyle. The inventory itself is **Table 1.4 on p.56** — 18 styles, 108 printed substyles *(both counts are the transcriber's; the page prints no totals)*. | PAPER + counted |

**GM-only arithmetic, verified computationally.** With a 26-week half-life applied over 104 weekly
observations, the *effective* number of observations — the standard measure, total weight squared
divided by total squared weight — is **≈ 66**, not 104. Set that beside NAMR's 1 market + 12 styles + 54
industries + an unprinted number of country and currency factors, and the arithmetic is uncomfortable
on the paper's own numbers. **This calculation is ours.** Do not present it as the paper's; do present
it, because it is the sharpest thing in the L8 boss round.

---

### C12-A · PUZZLES — THE CROSSWORD WITH TWO CLUES

**Story.** Someone hands you a crossword grid with sixty blank entries and exactly two clues. You solve
both. Then you fill in the other fifty-eight, because the grid must be full, and you hand it in as
complete. It is not that your answers are probably wrong — some of them may be right by luck. It is
that nothing in the puzzle distinguished them from thousands of other complete fillings that also
satisfy the two clues you were given. Your grid is not an uncertain solution. It is one arbitrary member
of an enormous family, presented as if it were the answer. And here is the part that turns a curiosity
into a disaster: suppose the person who receives your grid is looking for the entry the puzzle is least
sure about, because that is where they intend to place a bet. They will go straight to the fifty-eight
you invented.

**Map.**

| In the story | In the model |
|---|---|
| an entry in the grid | one number the covariance matrix has to supply |
| sixty entries | the number of pairwise relationships between factors — which grows much faster than the factor count |
| **two clues** | too few periods of factor returns |
| a complete filled grid | a covariance matrix that computes without complaint |
| thousands of fillings satisfying the clues | many different matrices consistent with the data seen |
| "not uncertain — arbitrary" | the matrix does not report doubt; it reports numbers |
| **the recipient hunting for the least-certain entry** | an optimiser hunting for the lowest-risk portfolio |
| that hunt landing on the invented entries | the optimiser loading into exactly the directions the data never saw |
| the grid still looking complete | the risk report still printing a total, a pie and a beta |

**The awkward question.** *"The matrix still produces a number for every portfolio. If it never refuses,
how would anyone on the desk ever notice this had happened?"*

- **Landed** sounds like: you would not notice from the number itself — you would notice from behaviour.
  The tell is that the model reports suspiciously *low* risk for a very specific, strange-looking
  portfolio, and that the same portfolio changes completely when you re-estimate on slightly different
  data. Any diagnostic that only looks at totals will miss it entirely.
- **Not landed** sounds like: "the risk number would look wrong" — how? Push until they name a check
  they could actually run.

**Where it breaks.** A crossword has a unique intended solution sitting in the setter's drawer, so the
story implies there is a true covariance matrix being approximated. There is not — the matrix is a
summary of a moving world, and even with unlimited history it would not converge to a fixed truth. Also,
crossword answers are discrete and either right or wrong; covariance entries are continuous, and the
failure is gradual as periods shrink, not a cliff.

---

### C12-B · LINGUISTICS — TWO SENTENCES OF A LANGUAGE

**Story.** A field linguist reaches a village and records two sentences before the last fluent speaker
dies. Back at the university she writes a grammar. It is a competent piece of work: it accounts for both
sentences perfectly, and it is internally consistent. It also makes confident statements about how the
language forms questions, marks the past tense, and handles plurals — none of which appeared in either
sentence. A reviewer asks how she knows. The honest answer is that she does not, and could not: those
parts of the grammar were not inferred from evidence, they were supplied by her expectations of what
languages are like. The grammar is not a summary of a language. It is two facts and a great deal of
scaffolding, and the scaffolding is written in the same typeface as the facts.

**Map.**

| In the story | In the model |
|---|---|
| the language | the joint behaviour of all the factors |
| a recorded sentence | one period of factor returns |
| **two sentences** | 104 weeks, effectively about 66 (p.27 + our arithmetic) |
| the grammar | the estimated covariance matrix `F` |
| rules covering the recorded sentences | the directions the data has actually seen |
| **rules about questions and plurals** | directions never observed |
| the scaffolding coming from her expectations | structure coming from the estimator's arithmetic, not from data |
| "written in the same typeface as the facts" | the matrix printing a number for observed and unobserved directions alike, with nothing marking which is which |
| a reader trusting the whole grammar | a user trusting the whole risk report |
| the last speaker dying | the window being fixed at 104 weeks by choice, not by availability — the paper says the history starts in **March 1996** |

**The awkward question.** *"If she had recorded two hundred sentences instead of two, would the grammar
then be sound? Where exactly is the line?"*

- **Landed** sounds like: there is no single line, but there is a hard floor — you need at least as many
  independent observations as there are directions to describe, and comfortably more than that before
  the description is worth anything. Below the floor the failure is not "less accurate", it is
  "structurally impossible": some directions have literally no evidence.
- **Not landed** sounds like: a rule of thumb quoted from nowhere ("ten observations per parameter").
  Ask where the number came from; if they cannot say, dock bps under NO NUMBER WITHOUT ITS ORIGIN.

**Where it breaks.** A language is genuinely there, generated by real speakers, and more fieldwork would
genuinely reveal it. Factor co-movement changes while you watch, so "collect more periods" partly
defeats itself — the older periods describe a different regime, which is exactly why the paper decays
them with a 26-week half-life in the first place (p.27). The linguist's problem has a solution; this one
has a trade-off.

---

### C12-C · ARCHAEOLOGY — A POT FROM TWO SHARDS

**Story.** A dig turns up two shards of a large pot. The conservator glues them together, and from the
curvature of those two pieces she reconstructs the whole vessel in plaster: a smooth, complete,
handsome pot which goes into the case with a label. A visitor asks which parts are original. The
conservator points at the two shards. Everything else is plaster, and — this is the thing — the plaster
is the *smoothest* part of the pot. Precisely where there was no evidence, the reconstruction is at its
most confident and its most featureless. If a student now measures the pot to study how this potter
handled decoration, they will conclude that this potter left large areas undecorated, and they will have
learned nothing about the potter and everything about the conservator.

**Map.**

| In the story | In the model |
|---|---|
| the pot | the true joint behaviour of the factors |
| a shard | a direction the data actually shows you |
| **the plaster** | the parts of `F` supplied by arithmetic rather than by evidence |
| the smooth plaster surface | directions the matrix reports as having little or **no** variability |
| the label saying "Roman pot" | the risk report saying "Active Risk 2.99%" |
| a student measuring the plaster | an optimiser or a PM reading risk off an unobserved direction |
| "they learn about the conservator" | the number describes the estimator, not the market |
| more shards | more independent periods |
| the pot still displayed as one object | the matrix still returning a single, usable-looking number |
| an honest museum shading the plaster differently | what a covariance matrix does **not** do: nothing marks which entries are evidence |

**The awkward question.** *"Nobody would ever hold a portfolio that sits entirely in an invented
direction — surely real portfolios are spread across sensible bets. Isn't this a mathematical curiosity
rather than a desk problem?"*

- **Landed** sounds like: it would be a curiosity if portfolios were chosen at random. They are not:
  anyone using the model to *build* a portfolio is explicitly searching for the combination with the
  lowest predicted risk, and the invented directions are exactly where the predicted risk is lowest. The
  procedure that uses the model hunts for its weakest point. That is the sentence that wins the L8 boss
  round.
- **Not landed** sounds like: agreeing it is a curiosity. It is not, and the player who thinks so will
  build an optimiser that eats itself.

**Where it breaks.** Archaeology has an obvious visible distinction — plaster is a different colour from
pottery — and the story therefore suggests the problem is discoverable by inspection. A covariance
matrix offers no such visual cue; its entries all look alike. Also, real conservators know how much they
invented. A desk running the standard recipe does not automatically know how much of `F` is evidence,
because — as p.27 says — the method is documented somewhere else entirely.

---

**RETURN TO BFRE.**

> "Now the honest part. **Nothing in this argument is in the paper.** There is no factor count anywhere
> in sixty-five pages, no observations-to-factors ratio, no discussion of this failure at all. What the
> paper does print is on page 27: the default factor covariance matrix uses **104 weeks with a 26-week
> half-life** — which is four half-lives, so the oldest week counts one sixteenth of the newest. And on
> page 57, Table 1.5, the NAMR industry schema runs to **54 rows** — a count I made, because the page
> prints no total — on top of the **12 styles plus market** in Table 1.2 on page 10, plus country and
> currency blocks whose sizes the paper never states. Put those beside each other and decide for
> yourself. Then note page 27's last sentence on the subject: the technical details are deferred to the
> **BRS Covariance Matrix Estimation documentation**, which is not in this document. That is your best
> single exhibit for Level 12 — the most important matrix in the model is documented elsewhere."

---
---

# C13 · SHRINKAGE

> **DIFFICULTY: GRADUATE-LEVEL. Say so.** And say the second thing: **BFRE does not shrink `F`.** The
> word "shrinkage" appears in this document exactly once, inside a bibliography entry — reference [7],
> Tibshirani, "Regression shrinkage and selection via the lasso", on page 64. The only shrinkage
> *mechanism* in the paper is on page 36 and it acts on **factor returns**, not on the covariance matrix.

**Unlocks:** L8 boss round · **Jargon gate:** *shrinkage* and *Bayesian prior* unlock here. "Bayesian
prior" **is** the paper's phrase (p.36); "shrinkage" is not the paper's word for what it does.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The paper's one shrinkage | p.36 | "We impose the thin country/industry correction by **adding a Bayesian prior**, which in essence **diverts the estimated country/industry return away from the sample factor return and towards a theoretical prior**." Applied where "limited, or no data exists to reliably estimate those factor returns". | PAPER |
| What it does **not** say | p.36 | **The prior's form, its strength and its shrinkage parameter are not specified.** Nowhere. | PAPER + GAP |
| Shrinkage methods, named and rejected | p.8 | LASSO (Tibshirani [7]), LARS (Efron [8]), Group Lasso and Group LARS (Yuan and Lin [9]), Ridge, and a Bayesian approach (Kadane and Lazar [6]) are all named as alternatives to BFRE's stepwise selection — then dismissed as "purely statistical in nature and rely heavily on historical data", in contrast to BFRE's blend of "economically intuitive industry definition… statistical analysis… and forward-looking views". | PAPER |
| The other blend, same idea | p.28 | Specific risk for assets with little history is "a **weighted sum** of its time-series forecast (if it exists) and its **cross-sectional** forecast… In the limit this weight is set to **1**." **The functional form of the weighting function is not given.** | PAPER |
| Where the cross-sectional forecast comes from | p.28 | Assets with "similar market capitalisation, in the same industry and country". | PAPER |

**GAP.** No shrinkage of `F` anywhere. If the player builds one at L8, that is the game giving them a
standard tool the paper does not use — say so.

---

### C13-A · SPORT — THE ONE-INNINGS AVERAGE

**Story.** A young batsman is picked for one match, scores a hundred, and is not out. On paper his
average is now enormous — the largest in the squad by a distance. Nobody on the selection panel treats
it as real. They have seen a hundred young players score a hundred once, and they know what usually
happens next. So when they rank him, they do not use his number; they use something between his number
and what a typical young player does, leaning toward his own record as his own record grows. After ten
innings they lean on his number quite heavily. After a hundred, they use it almost alone. And they are
open about the trade: their ranking of him is deliberately *wrong* — too low — for a genuinely
exceptional player, in exchange for not being wildly wrong about the ninety-nine who were lucky once.

**Map.**

| In the story | In the model |
|---|---|
| the batsman | a factor, or an asset, with very little data |
| his one hundred | the sample estimate from a thin sample |
| the panel's scepticism | the recognition that a thin estimate is mostly noise |
| **what a typical young player does** | the prior — p.36's "theoretical prior" |
| the blended ranking | the shrunk estimate |
| leaning further on his own record as innings accumulate | p.28's weighting function, which "places more weight on the time-series forecast as more data becomes available" |
| using his number almost alone after a hundred innings | p.28: "In the limit this weight is set to **1**" |
| **being deliberately too low for a great player** | the bias shrinkage knowingly accepts |
| in exchange for not being wildly wrong about ninety-nine | the variance it removes |
| the panel never publishing its blending rule | p.36 and p.28 both: the functional form is not stated |

**The awkward question.** *"You have just told me the panel deliberately publishes a number they know
is wrong. How is that not simply falsifying the record?"*

- **Landed** sounds like: because the job is not to record what happened, it is to forecast what happens
  next, and for that job the blended number is *better* on average than the honest one. Everything is
  traded: a little wrongness you control in exchange for a lot of wildness you don't. That is the whole
  content of shrinkage and it should be said in exactly those terms.
- **Not landed** sounds like: "we're removing noise" — a slogan. Ask them what the cost is. If they
  cannot name the bias, they have only half the concept.

**Where it breaks.** Cricket has a real underlying ability which the average is estimating, and "typical
young player" is a genuinely observable population. A thin country factor has no obvious population of
peers and no obvious true value, which is precisely why p.36 has to speak of a "**theoretical** prior"
and never says what it is. The sports story makes the prior feel empirical. In the paper it is not — and
that gap is a Level-12 exhibit.

---

### C13-B · INSURANCE — THE VILLAGE FIRE RATE

**Story.** An insurer prices fire cover for a village of forty houses. Last year there was one fire.
Taken literally, the village's fire rate is one in forty and the premiums should be enormous. Taken
across the county, the rate is one in six hundred. The actuary uses neither. She charges a rate between
the two, much closer to the county rate, because forty houses over one year is far too little evidence
to overturn the county's experience. If the village keeps burning for a decade, her rate creeps toward
the village's own number; if the fire turns out to have been a one-off, the village drifts back to the
county rate as the years pass without incident. She writes in her file that this is deliberate: the
village is being charged more than a fire-free village and less than its own record implies, and both
of those are on purpose.

**Map.**

| In the story | In the model |
|---|---|
| the village | a factor with limited data — p.36's thin country or industry |
| last year's single fire | the sample estimate |
| the county rate | the prior |
| **the charged rate, between the two** | the shrunk estimate: "diverts the estimated country/industry return away from the sample factor return and towards a theoretical prior" (p.36) |
| how far toward the county rate | the shrinkage strength — **not specified anywhere in the paper** |
| creeping toward the village's own number over a decade | more data earning more weight (p.28's weighting function) |
| houses of similar type in similar places | p.28's cross-sectional overlay: "similar market capitalisation, in the same industry and country" |
| the actuary writing it in the file | what the paper does not do: it names the mechanism and hides the parameter |
| a village charged more than it deserves | the bias, accepted knowingly |
| the insurer staying solvent | the variance reduction, which is the point |

**The awkward question.** *"Suppose the village really is unusually dangerous — thatched roofs, no fire
station. The actuary's blend under-charges it every year, permanently. When is shrinkage simply the
wrong answer?"*

- **Landed** sounds like: when there is a real, persistent difference *and* enough evidence to establish
  it. Shrinkage is a bet that the thing looks unusual because it is thinly measured, not because it is
  unusual, and that bet loses on genuinely exceptional cases. The remedy is more evidence, or a better
  prior built from thatched-roof villages rather than all villages — which is exactly what p.28's
  "similar market capitalisation, in the same industry and country" is groping toward.
- **Not landed** sounds like: "shrinkage is always better" — no. It is better on average over a
  population, worse in the tails of that population, and a risk model lives in the tails.

**Where it breaks.** Insurance has a genuine hierarchy — village inside county inside country — with
real data at every level. BFRE's "theoretical prior" (p.36) is explicitly *theoretical*; the paper does
not say it is estimated from anything. And an insurer knows and publishes its credibility formula.
Page 36 does not, which is the difference between a shrinkage method and a shrinkage gesture. Say so.

---

### C13-C · CARTOGRAPHY — THE HURRIED COASTLINE

**Story.** A survey ship is sent to chart an unmapped stretch of coast and gets three days of bad
weather instead of three weeks. The cartographer has a handful of rough fixes, taken from a pitching
deck. If she plots exactly what she measured, the chart shows a coastline with impossible jagged
excursions — a bay that juts out and back within a few hundred yards — which is not what the coast does,
it is what her instrument did. So she draws a smoother line: one that stays near her fixes but bends
like coastlines bend. She knows two things about the result. Every headland on her chart is in slightly
the wrong place, and no navigator will be misled about the shape of the coast. If she had drawn the raw
fixes, both statements would be reversed.

**Map.**

| In the story | In the model |
|---|---|
| the coast | the quantity being estimated |
| a fix taken from a pitching deck | a noisy sample estimate |
| three days instead of three weeks | a thin sample |
| **the jagged raw plot** | the unshrunk estimate — extreme values that are mostly noise |
| the smooth drawn line | the shrunk estimate |
| "coastlines bend like this" | the prior — an expectation about what such things look like |
| every headland slightly misplaced | the bias introduced deliberately |
| no navigator misled about the shape | the variance removed, and why it is worth the bias |
| a cartographer who draws the raw fixes | an estimator that trusts a thin sample completely |
| the chart carrying no note about which parts were smoothed | p.36 again: mechanism named, parameter withheld |

**The awkward question.** *"She is drawing a coastline she never saw properly. How is that different
from making it up — how is this not exactly the plaster pot from the last level?"*

- **Landed** sounds like: it is uncomfortably close, and the distinction is honesty about direction. The
  plaster pot *hides* the absence of evidence and reports confidence where there is none. Shrinkage
  *declares* that it is pulling toward a stated expectation, and pulls less as evidence arrives. Same
  raw ingredient — missing data — with the opposite disclosure. The player who spots that the two levels
  are the same problem, treated honestly and dishonestly, has understood both.
- **Not landed** sounds like: "shrinkage uses maths" — meaningless. Push for the disclosure argument.

**Where it breaks.** A cartographer has genuine prior knowledge — coastlines really do have a
characteristic shape, established from thousands of surveyed coasts. Whether an analogous prior exists
for a thin emerging-market country factor is exactly what p.36 declines to say. Also, a chart can later
be corrected by a proper survey and the smoothing thrown away; a risk number is used the day it is
produced and is never revisited.

---

**RETURN TO BFRE.**

> "Here is where BFRE actually does this, and it is not where you expect. Page 36: 'We impose the thin
> country/industry correction by **adding a Bayesian prior**, which in essence diverts the estimated
> country/industry return **away from the sample factor return and towards a theoretical prior**.' Note
> three things. First, it is applied to **factor returns**, not to the covariance matrix — the paper
> never shrinks `F`. Second, the form of the prior, its strength and its parameter are **not specified
> anywhere in this document**. Third, page 8 shows the authors considering the whole shrinkage family —
> LASSO, LARS, group LASSO, Ridge, Bayesian selection, all cited — and rejecting them for factor
> selection as 'purely statistical in nature', in favour of a stepwise procedure blended with
> 'forward-looking views'. The word *shrinkage* appears in this paper exactly once: in the title of
> reference [7] in the bibliography on page 64."

---
---

# C14 · THE DIAGONAL `Δ` AND WHAT IT IGNORES

**Unlocks:** L9 (The Private Drama) · **Difficulty:** conceptually ordinary, evidentially the richest
level in the game — this is the one place the paper hands you the boss-round answer in its own words.
**Jargon gate:** *specific risk*, *diagonal* unlock at L9; both are the paper's words (p.24, p.27).
*Specific return* was already legal from L0.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The claim | p.24 | "`Δ` : specific risk matrix (**a diagonal matrix** of asset specific risk forecasts)". | PAPER |
| The retraction, three pages later | p.27 | "The asset specific covariance matrix is made up of **two** components: a vector of asset specific risk forecasts **and a sparsely populated unit diagonal matrix containing non-zero, off-diagonal specific return correlations.**" | PAPER |
| **The direction of the error, in the paper's own words** | p.28 | "these specific returns may be positively correlated, and so **ignoring this correlation would lead to under (or over) prediction of specific risk in a long-only (long-short) portfolio context.**" | PAPER |
| The assumption, stated as an assumption | p.30 | "Factor returns have **zero correlation** with asset specific returns, and specific returns from different issuers are unrelated and have **zero correlation**." | PAPER |
| The justification for it | p.28 | Correlations are "only estimated between assets **in the same company**. Specific return correlations between assets in different companies are **assumed to be zero in-line with standard modelling practice**." | PAPER |
| The override | p.28 | Linkages captured "either **imposed via a constant override of 1**, or where data availability permits, **estimated using asset specific returns**." | PAPER |
| Structural versus empirical | pp.28–29 | Structural: related listings get identical specific risk (typically cloned from the primary listing) and correlation forced to **1** — suited to active managers over "many months". Empirical: estimated separately — suited to index trackers, "where even small differences in how related listings trade on a day-on-day basis can significantly impact their performance." | PAPER |
| The parameters | p.28, Table 1.3 | Daily: half-life **125 days**, **375** observations, Newey–West lag **10 days**. Weekly (WRLD and EMKT): **26 weeks**, **104 weeks**, **2 weeks**. Verified digit-for-digit at 4×. | PAPER |
| The other failure mode | p.16 | Before a small-cap factor existed, deciles 9 and 10 showed residual structure at roughly **10.8%** and **21.1%**, above the 10% line — common variation sitting inside `u`. `[APPROX — pixel-measured, ±0.5pp]` | PAPER + `[APPROX]` |
| A named, admitted failure | p.30 | The model "does **not** adequately capture all relationships between different listings of companies, which have more than one share class with derived securities linked to those share classes, e.g. Chinese MMA securities. This will be addressed in a forthcoming model release." | PAPER |
| The size of the stake | p.35 | Specific is **50%** of Active Risk on the sample report. | PAPER |

---

### C14-A · THEATRE — THE UNDERSTUDIES

**Story.** A producer stages a play with a cast of twenty and one understudy. Her reasoning is sound
and she has done it for years: actors fall ill at random, one at a time, and one spare body covers the
season. She has never had two out at once. This season she casts a married couple, who share a flat and
a car and every meal. In November one of them gets flu, and by the weekend so has the other. The
understudy covers one part; the other part cannot be covered; the performance is cancelled and the
insurers ask why the risk assessment said the chance of a double absence was negligible. It said so
because it treated twenty actors as twenty independent people, and nineteen of them were.

**Map.**

| In the story | In the model |
|---|---|
| an actor | an asset |
| an actor falling ill | that asset's specific return moving |
| "illnesses happen one at a time" | the assumption that specific returns are unrelated across issuers — p.30, stated flatly |
| the single understudy | the safety a diversified book expects from independence |
| **the married couple** | two listings of the same company — a cross-listing, an ADR and its root, an 'A' and a 'B' share (p.28) |
| both getting flu in the same week | correlated specific returns |
| the cancelled performance | the loss the risk number said was negligible |
| nineteen actors genuinely independent | why the assumption is nearly right nearly all the time |
| the insurer's question | the CRO's question at the L9 boss round |
| booking a second understudy for the couple only | p.28's answer: correlations estimated **only** between assets in the same company |

**The awkward question.** *"Nineteen out of twenty independent is a very good approximation. Is one
married couple really worth changing the whole model for?"*

- **Landed** sounds like: it depends entirely on the book, and the paper gives the rule. A long-only
  portfolio holding both listings has its specific risk **understated** — p.28's exact words are that
  ignoring the correlation "would lead to under… prediction of specific risk in a long-only… portfolio
  context". And the stake is not small: on p.35's sample report, specific risk is **half** of total
  Active Risk. Half the number rests on this assumption.
- **Not landed** sounds like: "yes, because correlations matter" — no mechanism, no direction, no stake.
  Push for all three.

**Where it breaks.** Theatre gives you only one direction of failure: two absences are always worse than
one. The model has both directions, and that is the sharper half of p.28 — in a **long-short** book
holding one listing against the other, ignoring the correlation makes the risk number **too high**,
because the shared movement cancels in a spread. The understudy story cannot represent a short position
at all. Reach for C14-B the moment the player needs both directions.

---

### C14-B · HOROLOGY — TWO CLOCKS FROM THE SAME SHOP

**Story.** A race organiser buys two identical stopwatches from the same shop, same batch, same day. He
knows each one drifts a little; the manufacturer says so. He uses them two different ways in the same
afternoon. In the morning event he starts both at the gun and adds their readings together to get a
combined timing figure, and the drift in the two watches — which is the *same* drift, because they are
the same watch — adds up and doubles. In the afternoon event he starts one watch at the beginning and
uses the other at the finish, and reports the difference between them, and the shared drift cancels out
exactly and the timing is better than either watch alone. Same two watches, same shared flaw, opposite
consequences, decided entirely by whether he added or subtracted.

**Map.**

| In the story | In the model |
|---|---|
| a stopwatch | an asset |
| a watch's drift | that asset's specific return |
| **the two watches sharing a drift** | correlated specific returns — two listings of one company |
| assuming the drifts are unrelated | `Δ` treated as purely diagonal, p.24 |
| **adding the two readings** | a long-only position in both |
| the shared drift doubling | specific risk **under**-predicted, because the model assumed cancellation that does not happen — p.28 |
| **subtracting the two readings** | a long-short pair — long one listing, short the other |
| the shared drift cancelling exactly | specific risk **over**-predicted, because the model charged for a wobble that nets out — p.28 |
| watches from different shops | assets in different companies, where the paper assumes zero correlation "in-line with standard modelling practice" (p.28) |
| the organiser forcing the two watches to be treated as one | p.28's structural approach: correlation "imposed via a constant override of **1**" |

**The awkward question.** *"If subtracting makes the shared drift disappear, then the long-short trader
gets a better answer by using a model that's wrong. Why would anyone fix the model for them?"*

- **Landed** sounds like: they do not get a better answer, they get a *conservative* one — the model
  charges them for risk they are not taking, so they will hold a smaller position than they could. Being
  wrong in the safe direction is still being wrong, it just fails quietly. And note who cares which way:
  p.29 says the structural approach suits active managers over "many months" while the empirical
  approach suits index trackers, "where even small differences in how related listings trade on a
  day-on-day basis can significantly impact their performance."
- **Not landed** sounds like: "over-prediction is fine" — flag it hard. A CRO will accept that answer
  and then ask what the firm's unused risk budget cost the fund.

**Where it breaks.** Two stopwatches share a drift because they are physically identical objects; two
listings of one company share a specific return for a subtler reason the paper spells out on p.28 —
"specific returns continue to capture both the idiosyncrasies of asset return **and company return**"
after the common factors have taken their share. The watch story also makes the shared drift perfectly
identical, which corresponds only to the *structural* approach's forced correlation of 1, not to the
empirical one where it is estimated and generally less.

---

### C14-C · STRUCTURAL ENGINEERING — ONE BATCH OF CABLE

**Story.** A footbridge hangs from twenty-four cables. The design assumes each cable might fail on its
own — a bad splice, a flaw, corrosion in one anchorage — and it is built so that the loss of any single
cable is survivable with a wide margin. The calculation is careful and correct given its assumption.
Then the maintenance record is read properly for the first time and it turns out that all twenty-four
cables came from one production run of one mill, on one day. Whatever went wrong at the mill went wrong
in all of them. The bridge was never designed for the failure it actually faces, and no amount of
recalculating the individual cable strengths would have revealed it, because the error was not in any
cable's number. It was in the word *independently*.

**Map.**

| In the story | In the model |
|---|---|
| a cable | an asset |
| a cable's own strength | that asset's specific risk forecast — the entries of the vector on the diagonal |
| the design margin | the diversification a large book expects |
| "any single cable failing" | independent specific returns |
| **one production run** | a shared source of specific movement — the same company, the same share class family |
| the whole design being sound *given its assumption* | p.24's `Δ`, correct arithmetic on a stated assumption |
| **the error being in the word "independently"** | the assumption on p.30, not the numbers |
| recalculating cable strengths not helping | improving specific risk forecasts does not fix an off-diagonal that was set to zero |
| the maintenance record nobody read | p.27 and p.28, which say plainly that `Δ` is not really diagonal |
| the mill's other customers | p.30's admitted gap: multiple share classes with derived securities linked to them, "e.g. Chinese MMA securities. This will be addressed in a forthcoming model release." |

**The awkward question.** *"Every engineer knows to check the batch. If the paper says on page 27 and
page 28 that the matrix is not really diagonal, then nobody is fooled and there is no problem. What is
left to criticise?"*

- **Landed** sounds like: two things are left. First, page 24 — the equation the whole model is stated
  in — calls `Δ` "a diagonal matrix", and that is the line most readers will take away; the correction
  is three pages later, in a different section. Second, and much bigger: the correction only covers
  assets **in the same company**. Across companies the correlation is set to zero, and the stated
  justification is "in-line with standard modelling practice" (p.28) — which is a citation of custom,
  not of evidence. Every shared shock that is not a factor and not the same company is still assumed
  away.
- **Not landed** sounds like: "so it's fine" — the player has stopped reading at the reassurance.

**Where it breaks.** A bridge has a genuine physical common cause with a paper trail; you can walk into
the mill and check. There is no register of which stocks' idiosyncratic returns share a hidden cause,
which is why the paper draws the line at legal identity — the same company — rather than at economic
similarity. That is a defensible, checkable, conservative line, and the player should be able to argue
*for* it as well as against it. Also, bridges fail once; a risk model's understatement shows up as a
slow drip of being wrong more often than the bias statistic expects, which is exactly what p.38's
surveillance regime is built to catch.

---

**RETURN TO BFRE.**

> "The list of leftover sizes you just built is `Δ` in equation (1.8) on page 24, where the paper calls
> it *'a diagonal matrix of asset specific risk forecasts'*. Turn to page 27 and it takes that back: the
> specific covariance matrix has **two** components, the second being 'a sparsely populated unit diagonal
> matrix containing **non-zero, off-diagonal specific return correlations**'. Then page 28 states your
> boss-round conclusion in its own words: ignoring that correlation 'would lead to **under (or over)
> prediction** of specific risk in a **long-only (long-short)** portfolio context'. Both directions, one
> sentence. And page 30 tells you where the line is drawn — 'specific returns from different issuers are
> unrelated and have zero correlation' — with page 28 giving the reason: '**in-line with standard
> modelling practice**'. That is a citation of custom. The stake is on page 35: **Specific is 50% of
> Active Risk**."

---
---

# C15 · ASSEMBLING THE RISK EQUATION

**Unlocks:** L10 (The Assembly) · **Difficulty:** ordinary once C10 and C14 have landed; the level's real
demand is that **every multiplication is explained as a sentence**.
**Jargon gate:** *asset covariance matrix*, *tracking error* unlock here. **"Tracking error" never
appears in the paper** — its word is **Active Risk** (p.34, p.35). Flag the letter swap: the game writes
`V = X F Xᵀ + D`, the paper writes `Σ = X F Xᵀ + Δ` (p.24).

### BFRE anchor (verified)

| Anchor | Page | Sentence version | Tag |
|---|---|---|---|
| Equation (1.7) `r = X f + u` | p.24 | Each asset's return is its characteristics times the payoff to those characteristics, plus what nothing common can reach. Lead-in line: "In general a multi-factor model decomposes asset returns as follows". | PAPER |
| Equation (1.8) `Σ = X F Xᵀ + Δ` | p.24 | `Xᵀ` reads the portfolio's characteristics; `F` says how those characteristics move together; `X` carries the answer back to assets; `Δ` adds each asset's private wobble. | PAPER |
| The ingredient list | p.24 | Portfolio risk is computed from four things: portfolio holdings (asset weights); portfolio-level factor exposures, **aggregated from the asset level**; a factor covariance matrix; and asset specific risk forecasts. *(Close paraphrase of the page, as recorded in `notes/` — not a verbatim sentence.)* | PAPER |
| Exposure is a position, not a sensitivity | p.4 | "The market factor **exposure** of a portfolio should not be confused with its market **beta**." Market factor exposure = "the fraction of portfolio %NAV invested in equities" (footnote 3 adds delta-adjusted derivative exposure). | PAPER |
| Lineage rather than evidence | p.24, fn 13 | The approach is "similar to that used in the fundamental factor risk model literature", citing Rudd and Clasing [24], Grinold and Kahn [25], Connor et al. [17]. **Justified by precedent, not by an empirical comparison.** | PAPER |
| What the assembled number looks like | p.35 | Banner: Active Risk **2.99%**, Portfolio Beta **1.02**, Portfolio Risk **15.62%**, Benchmark Risk **14.98%**, Base Currency EUR. *(Audit doubt: the middle digit of 2.99 is blobby — 2.89 not fully excluded; the last digit of 15.62 is soft — 15.67 not fully excluded. 14.98 and 1.02 are clean.)* | PAPER + `[partly uncertain]` |

---

### C15-A · MONEY-CHANGING — THE MIXED TILL

**Story.** A tourist-shop owner closes up and has to tell her accountant what the day's takings are
worth, in her own currency. The till holds euros, pounds, francs and a scatter of other notes. She does
not value each note separately against her currency; she does it in three moves. First she counts what
she holds in each currency — so much in euros, so much in pounds. Then she looks at the board of
exchange rates, which tells her not just what each currency is worth but how they move against one
another, because on a bad day the euro and the franc go the same way together while the pound goes the
other. Then she converts back and writes down one figure. And she adds a last item by hand: at the
bottom of the till is a commemorative coin from a country nobody trades, whose value nobody quotes, and
she has to estimate that one entirely on its own.

**Map.**

| In the story | In the model |
|---|---|
| the notes in the till | the positions in the portfolio |
| counting what she holds in each currency | reading the portfolio's exposure to each factor — `Xᵀ` applied to the holdings; p.24 says portfolio-level exposures are **aggregated from the asset level** |
| a currency | a factor |
| **the board showing how currencies move together** | `F`, the factor covariance matrix |
| euro and franc moving together | positively correlated factors compounding |
| the pound moving the other way | offsetting exposures partly cancelling |
| converting back to her own currency | `X` carrying the factor answer back to the portfolio |
| the single figure she writes down | the common-factor part of portfolio risk |
| **the untradeable commemorative coin** | specific risk — `Δ` — valued asset by asset, with no shared board to consult |
| the accountant needing both lines | why the pie on p.35 has both a common-factor half and a Specific half |

**The awkward question.** *"She converts to currencies and back again. Why not just look up each note's
value directly and be done — what did the detour through currencies actually buy?"*

- **Landed** sounds like: it buys the *table*. Valuing each note directly would need a relationship
  between every note and every other note; going through currencies means she only needs relationships
  between the handful of currencies. That is exactly the paper's stated reason on p.2: BFRE "imposes far
  more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of
  factors, which capture the most important sources of asset return commonality" — the comparison being
  with STORM, which builds an asset-by-asset covariance matrix from asset returns alone (that
  description of STORM is `notes/`'s gloss of p.2, not a printed quotation).
- **Not landed** sounds like: "because it's more accurate" — it is not obviously more accurate; it is
  vastly more estimable. The player who says "accurate" has missed the entire architectural argument.

**Where it breaks.** Exchange rates are quoted, observable, and agreed by everyone; `F` is estimated by
one desk from 104 weeks of data and is not observable at all. Also, currency conversion is exact and
loses nothing, whereas going through factors deliberately throws away whatever the factors cannot
express — and that discarded part is not an error, it is `Δ`, and on p.35 it is **half the number**.

---

### C15-B · PHARMACY — COMPOUNDING

**Story.** A hospital pharmacist prepares a mixture for a ward. Each branded product on her shelf is
itself a blend of a small number of active ingredients, and she knows the blend for each brand. She is
asked how variable the finished mixture will be in strength. She does not study the brands. She works
out how much of each *active ingredient* the mixture contains, consults what she knows about how those
ingredients vary — including which of them tend to vary together, because two of them come from the same
plant extract and a poor harvest moves both — and converts that back into a statement about the mixture.
Then she adds one more thing: each brand has its own filler and its own factory, and the variability
that comes from *that* has nothing to do with the ingredients and has to be added on top, brand by brand.

**Map.**

| In the story | In the model |
|---|---|
| a branded product | an asset |
| how much of each brand is in the mixture | the portfolio holdings |
| the blend of active ingredients in a brand | that asset's row of exposures — a row of `X` |
| the mixture's total content of each ingredient | the portfolio's factor exposures, `Xᵀ` applied to holdings |
| an active ingredient | a factor |
| how each ingredient varies | a diagonal entry of `F` |
| **two ingredients from the same harvest** | correlated factors — the off-diagonals of `F` |
| converting back to a statement about the mixture | `X` carrying it back |
| **each brand's own filler and factory** | `Δ`, asset specific risk |
| the two contributions being added | the plus sign in `Σ = X F Xᵀ + Δ` |
| the assumption that filler variability is unrelated to harvests | p.30: "Factor returns have **zero correlation** with asset specific returns" — stated as an assumption |

**The awkward question.** *"You added the ingredient variability and the filler variability together.
What if a bad harvest also disrupts the factories — then adding them is wrong, isn't it?"*

- **Landed** sounds like: it would be, and the model assumes it away explicitly. Page 30 lists it as an
  assumption in as many words: factor returns have zero correlation with asset specific returns. The
  player should be able to say that this is a *stated* assumption, not a hidden one, and that the
  paper's own honesty here is a point in its favour — while noting there is no evidence offered for it.
- **Not landed** sounds like: "you'd need a cross-term" — technically pointing in the right direction but
  the player should be naming the page. At L10 they have earned the right to cite.

**Where it breaks.** Compounding is additive in a physical, conserved sense — grams of ingredient really
do add. Risk does not add that way; two equal risks combined do not give twice the risk unless they move
in lockstep, and the whole point of `F` is that they usually do not. If the player starts adding risks
arithmetically, the pharmacy has cost them the single most important non-intuitive fact in the level.
Break it deliberately with two offsetting exposures.

---

### C15-C · RAILWAYS — A JOURNEY'S DELAY

**Story.** A commuter wants to know how unreliable her daily journey is. Her journey is not one thing:
it uses three lines, and she spends a different share of the trip on each. The operator does not study
individual journeys; it keeps records line by line — how erratic each line is, and, crucially, which
lines go wrong at the same time, because two of them share the same signalling centre and when that
fails they both fail. So the operator works out how much of her journey sits on each line, consults the
line-by-line record and the pattern of joint failures, converts that back into a statement about her
particular journey, and then adds one last thing that no line-level record can supply: the chance that
her specific train has a door fault this morning.

**Map.**

| In the story | In the model |
|---|---|
| the journey | the portfolio |
| the share of the trip spent on each line | the portfolio's factor exposures |
| a line | a factor |
| how erratic one line is | that factor's own volatility |
| **the shared signalling centre** | correlated factors — the off-diagonals of `F` |
| the line-by-line record | `F`, built from history (p.27: daily factor returns since March 1996) |
| converting back to her journey | `X` carrying the answer back |
| **her particular train's door fault** | specific risk, `Δ` |
| the operator never modelling journeys directly | the whole architectural bet: model a few factors, not every asset pair |
| a season ticket versus a single trip | holdings — the weights that scale everything |
| the timetable being rewritten every month | the estimation universe rebuilt "on a country-by-country basis every month" (p.24) |

**The awkward question.** *"If a door fault is specific to her train, and she takes a different train
every day, doesn't that just average away? Why does it belong in the risk number at all?"*

- **Landed** sounds like: it averages away only if you hold enough independent trains, and the report on
  p.35 is the evidence that real portfolios do not: that book holds fifteen named positions in its Top
  Asset Contributions panel and **50%** of its Active Risk is still Specific. Diversification across
  names is not the same as diversification into nothing, and C14 is the reason — some of those "door
  faults" are shared.
- **Not landed** sounds like: "specific risk always diversifies away" — the classic textbook sentence,
  and it is exactly what the p.35 pie contradicts.

**Where it breaks.** Railway lines are physical and a journey's use of them is exact and observable. A
portfolio's factor exposures are *estimated* characteristics, standardised against a moving market
average (p.10) and re-derived weekly (p.36: exposures "updated on a weekly basis on Thursday to
incorporate the data as of previous Wednesday market close"). The commuter's route is a fact; `X` is a
measurement. That difference is the whole of L7's cost argument.

---

**RETURN TO BFRE.**

> "What you just assembled is printed on page 24 as equation (1.8), one line below equation (1.7). Two
> lines, and the other sixty-four pages exist only to say what goes into `X`, what goes into `F`, and
> what goes into `Δ`. Two housekeeping notes. The paper writes it as `Σ = X F Xᵀ + Δ` — capital sigma
> and capital delta — where we have been writing `V` and `D`; that is a letter swap, not a different
> model. And page 4 has a trap with your name on it: 'The market factor **exposure** of a portfolio
> should not be confused with its market **beta**' — exposure is the fraction of %NAV invested in
> equities, which is why the report on page 35 can print a Portfolio Beta of **1.02** as a separate
> quantity from the Market factor exposure in the style panel."

---
---

# C16 · MARGINAL CONTRIBUTION TO RISK

**Unlocks:** L11 (The Desk) · **Difficulty:** the *idea* is ordinary; the arithmetic is a nudge argument
you have already built at L1, now applied to a total instead of to a fit — call that back explicitly.
**Jargon gate:** *marginal contribution* unlocks at L11. **The phrase never appears in the paper.**
"Contribution" appears only as a chart axis label on p.35 and as prose on p.34.

### BFRE anchor (verified)

| Anchor | Page | What it is | Tag |
|---|---|---|---|
| The report | p.35, Fig 1.18 | "a sample **Equity Daily Risk (EDR)** report in Aladdin", European Equity portfolio, EMEA model, produced with PRT. | PAPER |
| The decomposition claim | p.34 | "**Active Risk is then decomposed along the different factor blocks in the model**, shown in the pie chart: styles (including the market factor), industries, countries and currencies. The report shows that the Active Risk is **split equally between common factors and stock specific sources**. Style and industry factors account for most of the common factor risks." | PAPER |
| Contribution and exposure as different things | p.35 | Every block panel plots **"Contrib. (% of Act. Risk)"** as bars against **"Act. Exp."** as dots on a *second axis*. The design is deliberate: two axes because they disagree. | PAPER |
| The pie | p.35 | Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec **1%** `[INFERRED — the glyph reads 1 or 2; 1% is recorded only because the six then sum to exactly 100]`. The other five are read directly and are unambiguous. | PAPER + `[INFERRED]` |
| The worked tilt | p.34 + p.35 | Prose: tilts towards "high volatility, momentum driven, low-yielding, smaller stocks". Panel: Volatility ≈ **+0.42 sd**, Momentum ≈ **+0.38**, Yield ≈ **−0.30**, Size ≈ **−0.20**. `[APPROX — every bar and dot on p.35 is a pixel measurement, ±10%. Axis tick labels are read directly and are reliable.]` | PAPER + `[APPROX]` |
| Exposure without contribution | p.35 | Style panel: **Emerging** carries an exposure of about **−0.10 sd** and contributes about **0%** of active risk. Market carries about 0.0 exposure and contributes about 0. `[APPROX]` | PAPER + `[APPROX]` |
| A short position that *adds* risk | p.35 | FX panel: the second pair's exposure dot sits at roughly **−10% of NAV** while its risk contribution is **positive** (≈ +0.55%). Country panel: the **United Kingdom** carries roughly **−10% of NAV** and simultaneously the block's **largest** contribution, ≈ 2.4%. `[APPROX]` | PAPER + `[APPROX]` |
| Fifteen names, still 50% specific | p.35 | "Top Asset Contributions" shows **exactly 15** named holdings (counted at 5×). | PAPER |

**GAP — say it out loud.** The paper contains **no formula for marginal contribution to risk**, no
derivation of the decomposition, and does not use the phrase "marginal contribution" or "tracking error"
anywhere. Level 11's mathematics is entirely ours; only its **output format** is citable.

---

### C16-A · CANOEING — TRIM

**Story.** Two people load a canoe for a week's trip. They keep asking the wrong question — "what is the
heaviest thing we're carrying?" — and the answer, a barrel of water, is not the thing making the canoe
tippy. What makes it tippy is where the weight sits relative to everything else. Move a small dry bag
from the centre out to the left gunwale and the canoe becomes noticeably less stable, because there is
already weight out on the left. Move that same dry bag to the right side and stability *improves* — the
same object, the same weight, the opposite effect, decided entirely by what is already in the boat. By
the end of the loading they have learned to judge every item not by its weight but by what one more
kilogram of it, placed there, does to the whole boat.

**Map.**

| In the story | In the model |
|---|---|
| an item of kit | a position in the portfolio |
| the item's weight | the size of the position — its exposure |
| the canoe's tippiness | total portfolio risk |
| **what one more kilogram in that spot does** | the marginal contribution to risk of that position |
| the heaviest item not being the problem | why the biggest position is not necessarily the biggest risk contributor |
| weight already sitting out on the left | the rest of the portfolio's exposures |
| **the same bag improving stability on the right** | a **negative** marginal contribution — a genuine hedge |
| balancing the boat | reducing risk by offsetting, not by shrinking |
| the barrel of water in the centre | a large position with near-zero contribution — p.35's Emerging, ≈ −0.10 sd exposure and ≈ 0% of active risk `[APPROX]` |
| judging every item by the nudge | the nudge argument from L1, now applied to the total instead of the fit |

**The awkward question.** *"If moving a bag to the right improves stability, why not move everything to
the right?"*

- **Landed** sounds like: because the answer changes as you move things. The moment the right side is
  loaded, the next bag placed there makes things worse. Marginal contribution is a statement about the
  portfolio *as it currently stands*, not a permanent property of the position — which is why the p.35
  report is dated and regenerated daily.
- **Not landed** sounds like: "because you'd capsize the other way" — right conclusion, but they have
  not said the load-bearing thing, which is that the number is recomputed against a changed portfolio.
  Give partial bps.

**Where it breaks.** A canoe's balance is a rigid, instantaneous physical fact; portfolio risk is a
forecast statistic built out of `F` and `Δ`, both estimates. Worse, the canoe's response to a nudge is
exact, whereas the marginal contribution inherits every frailty of C12 — in an unobserved direction the
model will confidently report that adding a position reduces risk. The canoe never lies about which way
it will tip. The model can.

---

### C16-B · FIREFIGHTING — THE TERRACE

**Story.** A fire officer walks a terrace of houses and is asked which one to spend the grant on. The
obvious answer is the house with the biggest woodpile, and it is the wrong answer. The house with the
biggest pile stands at the end of the row with a brick gable and a gap to the next building; a fire
there stays there. Three houses in the middle have modest piles each — but they share a roof void, they
are stacked against a common wall, and a fire in any one of them takes all three. The officer's
recommendation is to clear one of the middle piles, and she has to explain to a councillor that she is
spending money on a smaller pile because of what is *next to it*. The grant is not being awarded for
size. It is being awarded for what one more log there would do to the whole street.

**Map.**

| In the story | In the model |
|---|---|
| a house | a position |
| the size of a woodpile | the size of the position's exposure |
| the terrace | the portfolio |
| **the shared roof void and common wall** | co-movement: the off-diagonals of `F`, and the same-company links of C14 |
| the end house with a brick gable | a position whose risk does not compound with anything else held |
| the officer's recommendation | ranking by contribution, not by exposure |
| the councillor's objection | the PM saying "but that's not my biggest bet" |
| **one more log** | the marginal nudge |
| the whole street burning | portfolio risk, as opposed to position risk |
| clearing a pile that changes nothing | a large exposure with no contribution — p.35's Emerging `[APPROX]` |
| the officer's report | Figure 1.18's deliberate two-axis design: contribution as bars, exposure as dots |

**The awkward question.** *"Fires spread through walls — there's a physical reason those three houses go
together. What is the wall between two stocks? If you can't point at one, isn't 'contribution' just a
number the model made up?"*

- **Landed** sounds like: the "wall" is the factor structure, and the paper is explicit that this is
  measured co-movement rather than a mechanism. The honest position is that BFRE offers economic
  *stories* for its factors (p.19 on why liquid stocks track the market, p.12 on why similar-sized
  companies behave alike) and measures the co-movement empirically; the contribution number is only as
  good as `F`. That is a strong L12 answer arriving early, and it deserves bps.
- **Not landed** sounds like: naming a mechanism the paper does not claim. Do not let the player invent
  causal walls.

**Where it breaks.** The fire officer can see the roof void; she has physical certainty about which
houses are joined. Nobody can see `F`, and its estimate changes with the half-life. Also, fire spreads
in one direction only — it makes things worse — whereas a position can genuinely *reduce* portfolio risk,
which the terrace cannot represent at all. Switch to C16-A the moment negative contribution is needed.

---

### C16-C · MUSIC — THE CHOIR

**Story.** A choirmaster is told the choir sounds ragged and is asked who is at fault. The obvious
suspect is the loudest singer, a bass who can be heard from the car park, and he is not the problem: he
is loud, he is dead on pitch, and if anything he is holding the section together. The problem is a quiet
alto, barely audible on her own, who comes in a fraction late — and because she comes in late on exactly
the entries where the sopranos are already stretching, her small error lands on top of theirs and the
whole chord smears. Remove the loud bass and the choir sounds thinner and just as ragged. Remove the
quiet alto and it sounds clean. The choirmaster's finding is that being loud and being the problem are
two different measurements, and only one of them was on the register.

**Map.**

| In the story | In the model |
|---|---|
| a singer | a position |
| how loud a singer is | that position's exposure — its size |
| the raggedness of the whole choir | portfolio risk |
| **the loud bass who is not the problem** | a large exposure with a small risk contribution |
| **the quiet alto who is** | a small exposure with a large risk contribution |
| her lateness lining up with the sopranos' stretch | co-movement with what the portfolio already holds |
| removing the bass and hearing no improvement | cutting the biggest position and not reducing risk |
| removing the alto and hearing it clean | cutting the biggest *contributor* |
| the register of who sings loudest | the exposure column on the report |
| **two different measurements** | p.35's two axes: "Contrib. (% of Act. Risk)" and "Act. Exp." |
| a singer whose entry steadies a wobbling section | a negative contribution — a position that reduces risk |

**The awkward question.** *"The choirmaster found the alto by listening to the choir with and without
her. That's a real experiment. What is the equivalent for a portfolio — you can't remove a stock and
listen."*

- **Landed** sounds like: you nudge the holding slightly and recompute the total from the model, and
  that is the same trick as L1 — change one thing a little and see what happens to the total. The
  callback is the point: the player has met this exact tool before, first for finding a dial, now for
  attributing a total. (`RISK_DESK.md` §8: **CALL BACK**.)
- **Not landed** sounds like: "you look at the report" — circular; the report is what we are trying to
  explain the origin of. Push under NO NUMBER WITHOUT ITS ORIGIN.

**Where it breaks.** A choir can actually be heard with and without a singer; the model's "with and
without" is computed, never observed, and it is computed from `F` and `Δ`, so every criticism of those
lands here too. Also, choral raggedness is perceptual with no additivity — the parts of the
decomposition do not sum to the whole in any meaningful sense. In the model they do, exactly, which is
why the p.35 pie can print six slices that come to 100%. That additivity is the useful property the
choir story cannot show.

---

**RETURN TO BFRE.**

> "The numbers you just computed are the bars on page 35, Figure 1.18, labelled *'Contrib. (% of Act.
> Risk)'* — plotted deliberately against a **second axis** of plain exposure so you can watch the two
> disagree. Read the style panel: Volatility carries roughly **+0.42** standard deviations of exposure
> and about **11%** of the active risk, while **Emerging** carries exposure of about **−0.10** and
> contributes about **nothing** — and every one of those magnitudes is a pixel measurement off an
> unlabelled chart, so treat them as approximate, not as printed values. Then look at the Country panel:
> the **United Kingdom** carries roughly **−10% of NAV** — a short — and simultaneously the largest risk
> contribution in the block. A short position adding risk. That is your answer to a PM who says 'I hold
> fifteen names, I'm diversified': the report shows exactly fifteen names, and page 34 says in plain
> words that the Active Risk is 'split equally between common factors and stock specific sources' —
> **50% Specific** on the pie, with most of the other half being one style tilt. Say the last thing too:
> the paper gives you the picture and **never gives you the formula**. The phrase 'marginal contribution'
> does not appear in it."

---
---

# §20. CALLBACK MAP — the same tool in new clothes

`RISK_DESK.md` §8 requires you to point out when a tool reappears. This is the list.

| The tool | First met | Comes back as | Say |
|---|---|---|---|
| **The nudge** | C2 (L1) — find the dial | C3 (L2) — prove the balance by contradiction; C16 (L11) — marginal contribution | "This is the fog-walk again, now applied to a total instead of a fit." |
| **Squaring to stop cancellation** | C1 (L0) | p.8's average squared t-statistic (L6); the whole of `F` (L8) | "The authors do your trick to their own diagnostics on page 8." |
| **Balance / nothing left that lines up** | C3 (L2) | C5 (L4) — a coefficient is what is left after the others; the paper's two-step regressions (pp.7, 10, 12, 52) | "Regressing on residuals *is* the balance condition, run deliberately." |
| **Centring** | C6 (L5) | p.10 and p.39's standardisation; and every "net of the market" reading of an industry or country factor (p.26) | "Zero means market-average — that is p.10, not a convention we invented." |
| **The wobble of an estimate** | C7 (L6) | C12 (L8 boss) — when the wobble is so large the estimate has no content at all; C13 — shrinkage as the response | "Standard error and shrinkage are the same worry at two different sizes." |
| **`√n` / needing four times the data to halve the wobble** | C7 (L6) | C12's effective-sample argument | "You met the square-root law at Level 6." |
| **Fewer things than you are describing** | C8 (L6) — degrees of freedom | C12 (L8 boss) — periods versus factors | "Degrees of freedom, one level up and one order of magnitude worse." |
| **What the model assumes vs what the arithmetic forces** | C3 (L2) | C14 (L9) — the whole level | "This distinction was born at Level 2 and it is what Level 9 is." |
| **Exposure ≠ effect** | C6 (L5) — a level is not a slope | C16 (L11) — exposure ≠ contribution; p.4 — market exposure ≠ beta | "Third time you have met a size that is not an effect." |

---

# §21. DO-NOT-SAY LIST — jargon that leaks a level early

Terms appear freely in this file. At the table they are gated. Cross-check `gm/VOCAB.md` §1.

| Do not say before | These words |
|---|---|
| **L0** | residual, specific return |
| **L1** | factor return, exposure, loading, regression weight |
| **L2** | orthogonal *(and when you do say it: the word appears nowhere in the paper)* |
| **L3** | design matrix *(phrase appears nowhere in the paper; `X` is "factor exposures", p.24)* |
| **L4** | multicollinearity, variance inflation factor *(both are the paper's words, p.32)*; Frisch–Waugh *(never cite a page — the name is not in the paper)* |
| **L5** | intercept, z-score, standardisation, covariance |
| **L6** | standard error *(phrase never appears in the paper)*, t-statistic *(p.8 — this one is the paper's)*, degrees of freedom *(phrase never appears)*, statistically significant |
| **L7** | cross-sectional regression *(the paper's core phrase — pp.7, 24, 30, 32)* |
| **L8** | covariance matrix, half-life *(both the paper's, p.24/p.27)*; eigenvalue, eigenvector, principal component *(none appear in the paper — say so every time)*; shrinkage *(appears only in a bibliography title, p.64)* |
| **L9** | specific risk, diagonal *(both the paper's, p.24/p.27)* |
| **L10** | asset covariance matrix; tracking error *(never appears — the paper says **Active Risk**)* |
| **L11** | marginal contribution *(phrase never appears; p.35's axis says "Contrib. (% of Act. Risk)")* |
| **L12** | in-sample / out-of-sample *("out-of-sample" appears once, p.30; "in-sample" never)*; bias statistic *(p.32, p.38 — the paper's)* |

**Thirteen phrases that appear nowhere in the paper** and must never be handed a page number: *least
squares · sum of squares · normal equation · standard error · degrees of freedom · orthogonal ·
eigenvalue · principal component · marginal contribution · tracking error · Frisch–Waugh · design
matrix · loading.*

Verified by grep over the whole of `notes/`. Three of them do produce hits in `notes/` — "orthogonal"
once, "shrinkage" in a bibliography title, "standard error" once — and in every case the hit is either a
**transcriber's commentary line** or a **cited paper's title**, never BFRE's own text. Check the
surrounding line before you cite. If you hand a page number to one of these, you have broken **NO NUMBER
WITHOUT ITS ORIGIN** in its most damaging form.

---

# §22. ONE-PAGE TABLE INDEX

| Code | Concept | Level | Difficulty | Paper support |
|---|---|---|---|---|
| C1 | Squaring the misses | L0 | ordinary | object yes (p.24); reason **GAP** |
| C2 | The nudge / the dial | L1 | ordinary | strong (p.24, p.4, p.25, p.10) |
| C3 | The balance condition | L2 | ordinary | **GAP** on `Σx·e = 0`; p.26 gives a *different*, imposed balance |
| C4 | Two dials interacting | L3 | ordinary | strong (p.25 eq. 1.9, p.5) |
| C5 | Collinearity | L4 | **graduate** | strong (p.32 + fn 16, p.11, p.17, p.20, p.26) |
| C6 | Intercept and pivot | L5 | ordinary | strong (p.26, p.10, p.39, p.42) |
| C7 | Standard error | L6 | hard | thresholds yes (p.8, p.12, p.14); **the standard error itself is a GAP** |
| C8 | Degrees of freedom | L6 | hard | **GAP** — phrase absent; nearest are p.8, p.27, p.28, p.42 |
| C9 | Cross-section vs time series | L7 | ordinary to state, hard to defend | strong (p.24, p.3, p.42, p.2, p.13) |
| C10 | `F` as a weather map | L8 | ordinary idea, large gap around it | recipe yes (p.27); method **deferred to another document** |
| C11 | Eigenvalues | L8 | **graduate** | **GAP** — zero occurrences; illustrate with p.5/p.6 only |
| C12 | Too few periods | L8 boss | **graduate** | **GAP** — the argument is ours, built on p.27 + p.57 + p.10 |
| C13 | Shrinkage | L8 boss | **graduate** | p.36 shrinks a *factor return*, not `F`; parameters unstated; p.8 rejects the family |
| C14 | Diagonal `Δ` | L9 | ordinary, evidentially rich | **very strong** (p.24 vs p.27 vs p.28 vs p.30) |
| C15 | Assembling the equation | L10 | ordinary | **very strong** (p.24, two equations one line apart) |
| C16 | Marginal contribution | L11 | ordinary idea | output format yes (p.34, p.35); **formula is a GAP** |
