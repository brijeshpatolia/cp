# Level 12 — The Critique

Every number below is recomputed in exact rational arithmetic by `tools/verify_level12.py`
(418 assertions, exits 0). Nothing here is rounded by hand. Where a decimal does not
terminate at six places it is written with the word **rounded** next to it; every other
decimal on this page is exact.

The verifier does two further jobs that no earlier level needed, because this is the level
where the player starts making claims about a *document*:

- **Every figure this page quotes from the BFRE paper is asserted against the string
  recorded in `notes/`, in the right page chunk.** If a figure is not in `notes/`, the
  script fails. It cannot check that `notes/` is right; it can check that this level never
  invents a figure `notes/` does not carry.
- **Every count this page gives of the attack dossier is recomputed from `gm/CRITIQUE.md`
  itself** — weaknesses, cheap shots, concessions, grey-zone items, scoreboard ranks. The
  two files cannot drift apart without the script noticing.

> **Difficulty warning, stated up front because the rulebook demands it.**
>
> One thing on this page is **graduate-level** and is the hardest single argument in the
> game: **the multiple-testing charge** (Sections 5 and 7). Testing two hundred candidates
> at a fixed bar is not the same problem as testing one, the correction for it is a research
> literature, and *the paper names five members of that literature and declines them all*
> (p.8). If the player finds Section 7 heavy, that is correct calibration.
>
> One number on this page is **not hand arithmetic and is labelled as such**: the exact
> binomial tail in 7c. Everything else — including the entire null distribution in Section 5
> — is done by enumeration, by hand, with no distribution assumed. That is deliberate. This
> is the level about not accepting numbers whose origin you cannot trace; it would be
> grotesque to smuggle one in.
>
> The rest of this level is **not hard**. It is *disciplined*. The failure mode here is not
> confusion, it is enthusiasm: a player who has spent eleven levels learning how the model
> works will find twenty things wrong with the paper in ten minutes and will lose the room
> by minute two. Section 8 and Section 11 exist for exactly that.

> **`gm/CRITIQUE.md` is the dossier. This file is the level.** The dossier holds the
> fact-checked weaknesses, their defences, their comebacks and the named cheap shots. This
> page holds the *running order*, the arithmetic the player has to be able to do, what they
> must produce, the interrogation script and the pass conditions. Do not read one without
> the other, and do not quote the dossier at the table — the player earns each item by
> finding it.

---

## 0. What the player is already holding, and what is actually new

Every tool this level uses was built somewhere else. The level adds no machinery at all.

| From | The tool | Where it is used here |
|---|---|---|
| **Level 0** | three desks, identical `Σe = 0`, `Σe²` of 1, 144 and 0 — a published diagnostic that cannot tell a perfect model from a catastrophic one | §11's whole class of complaint, and `gm/CRITIQUE.md`'s Class G. Say the words "Desk B" out loud when you get there |
| **Level 1** | `b = Σxr/Σx²`, derived by nudging | §3c — every candidate column here has `Σx² = 6`, so the dial is just `S/6` |
| **Level 2** | `Σx·e = 0`, forced by the arithmetic | §3a and §4f — §3a is where `Σz·e = 0` makes the true dial come out exactly right; §4f is where it is printed as an audit on the shipped fit |
| **Level 3** | two columns, two balance conditions, the 2×2 system | §4f — the joint fit of the truth and the placebo |
| **Level 4** | a coefficient is a *leftover*; overlap wrecks the split while leaving the fit intact; `det = AC − B²`; VIF | §4d and §4f — the placebo steals three eighths of the true factor's coefficient, with `det = 32` and `VIF = 9/8` |
| **Level 5** | centering; a column of ones is an intercept | §3a — the market column, which fits exactly zero here and still costs a degree of freedom |
| **Level 6** | `SE`, `df = n − k`, `t² = (S²/Q)/σ²`, `t² = df·R²/(1−R²)`, `E[t²] = 1` under the null, and the Markov bar with no distribution assumed | the entire page. §5 is Level 6's 32-world enumeration pointed at a different object |
| **Level 7** | one cross-section per month, run again and again | §6 — months two, three and four are what make month one interpretable |
| **Level 8** | `F`, half-life, the trade-off between responsive and stable | §17 — where a junk factor's variance ends up |
| **Level 9** | what least squares *guarantees* versus what the modeller *assumes* | §7d — the independence assumption underneath the paper's best defence |
| **Level 10** | `V = XFXᵀ + D` | §17 — a junk column is a column of `X` |
| **Level 11** | contribution to risk | §17 — 84.375% of a portfolio's return booked to a column that means nothing |

**What is new is not a technique. It is a job.** Levels 0–11 asked *is this number right?*
Level 12 asks a different question, and it is the question a Chief Risk Officer is actually
paid to ask:

> **Would I believe this document if I had not written it?**

Three genuinely new things:

| | What Level 12 adds |
|---|---|
| **A search is not a test** | A single column's `t` and the *best of ten* columns' `t` are different quantities with the same name. §4 and §5 separate them by enumeration. |
| **Ranking, not listing** | Naming weaknesses is Tier 2 on the five-tier ladder. Putting them in order — and knowing which ones lose you the room — is Tier 4. §8. |
| **A defence you have to mean** | The player argues BlackRock's side first, with no warning that an attack is coming. §15. A player who cannot make the defence has not earned the attack, and this level is scored so that this is literally true. |

---

## 1. The stories — no mathematics

Two concepts arrive at this level, so two stories. Finish each one completely before mapping it.

### Story A — the tipster

A man in a town of a thousand people posts a letter to every household on the first of the
month. Five hundred letters say *the price of onions will rise this month*. Five hundred say
*it will fall.*

At the end of the month he throws away the five hundred households he was wrong about, and
posts again to the five hundred he was right about. Two hundred and fifty get *rise*, two
hundred and fifty get *fall*.

He does this six times. At the end, fifteen or sixteen households have received **six
correct predictions in a row** from a man who has never once looked at an onion. He writes to
them a seventh time and asks for money, and they pay, and they are not fools for paying: from
inside a single household, six in a row is overwhelming.

The tipster made no prediction. The *search* made the prediction, and the search is invisible
to the person holding the letter.

**The moral, in one line:** *you cannot judge a winner without knowing how many entrants
there were.*

### Story B — the inspector

A structural engineer inspects a building and finds two things: a cracked load-bearing beam
in the basement, and a doorbell that does not work.

She writes both in her report. She puts the doorbell first, because she walked in the front
door first.

The owner reads the first line, decides she is the kind of inspector who pads a report, skims
the rest, and does nothing. The beam is still cracked. The report was *entirely correct*.

**The moral, in one line:** *a true complaint delivered in the wrong order destroys the true
complaint that follows it.*

---

## 2. Mapping the stories onto the paper, line by line

| Story A | The paper |
|---|---|
| a thousand households | **PAPER, p.10:** *"for i = 1, 2, …, N (where N ≥ 200 is the number of candidate substyles) we run the following two-step regression"*. **PAPER, p.55:** the printed inventory is *"a subset of the full list of 200+"*, with each horizon variant counted separately |
| six months of letters | **PAPER, p.8:** the t-statistic history over the *15-year research history*, summarised over the full sample **and five-year sub-samples** |
| "six in a row" | **PAPER, p.8:** *"We consider an absolute t-statistics in excess of 2 as statistically significant"* (the grammar error is the source's). **PAPER, p.14:** *"A value in excess of 10% indicates a statistically significant style effect, and would be considered for inclusion in the models"* |
| the household cannot see the search | **ABSENCE, checked:** no multiple-testing correction is mentioned anywhere in the paper, and p.55 prints no criterion, statistic or threshold by which a substyle was kept or discarded. *(Say this as an absence you have checked, in your own voice. It is **not** a quotation — see §11, trap 8.)* |
| the printed list of entrants | **PAPER, p.56, Table 1.4**, titled an inventory of substyles *investigated*: **18 styles, 108 substyles** — *both counts derived from the printed rows; the page prints no totals, so say "counted from the rows"*. That is a subset; p.55 says the full list is 200+ |
| the one household that would have settled it | **PAPER, p.56, Table 1.4:** the candidate inventory contains a style called **Random**, whose single substyle is **Random Substyle**. The authors carried a placebo. **Its score is never reported.** |

| Story B | The level |
|---|---|
| the cracked beam | `gm/CRITIQUE.md` **G-3** — every accuracy claim deferred to a document the bibliography calls *forthcoming*. Scoreboard rank **1** of 20 |
| the doorbell | `gm/CRITIQUE.md` **CS-5** — the paper's typos; **CS-1** — "√-cap weighting is arbitrary", which the paper answers in a full paragraph and a footnote |
| putting the doorbell first | the single most common way to fail this level |

---

## 3. The dataset — THE PLACEBO DESK

### 3a. The file

Six stocks, four months. Returns are in percent, and they are **relative returns**: each
month sums to zero across the six, so the market column fits exactly zero and everything on
this page is about the style column. *(That is not a simplification of BFRE; it is BFRE's own
arrangement — style exposures are standardised to a weighted mean of zero, **p.10**, and the
market factor carries the level.)*

| Stock | month 1 `r₁` | month 2 `r₂` | month 3 `r₃` | month 4 `r₄` |
|---|---:|---:|---:|---:|
| AXL | +4% | +2% | +4% | +2% |
| BRN | +3% | +2% | +1% | +1% |
| CHR | +1% | −3% | −1% | −3% |
| DLT | −1% | +5% | +1% | +3% |
| EMK | −2% | 0% | −1% | 0% |
| FNX | −5% | −6% | −4% | −3% |

```
Σr = 0 in every month.       Σr² = 56, 78, 36, 32.
```

Months 1 and 2 are worked in full (§4 and §6); months 3 and 4 are needed only for the
persistence table in §6e, which is what the paper's actual selection rule needs.

**And here is the thing no desk ever has: the file is rigged, and we know how.** All four
months were generated from one real factor, and the game is telling the player so:

```
z  = the true exposure column:  +1 on AXL, BRN, DLT      −1 on CHR, EMK, FNX
r₁ = 2·z + e₁      e₁ = [+2, +1, +3, −3,  0, −3]      Σe₁ = 0   Σz·e₁ = 0   Σe₁² = 32
r₂ = 3·z + e₂      e₂ = [−1, −1,  0, +2, +3, −3]      Σe₂ = 0   Σz·e₂ = 0   Σe₂² = 24
r₃ = 2·z + e₃      e₃ = [+2, −1, +1, −1, +1, −2]      Σe₃ = 0   Σz·e₃ = 0   Σe₃² = 12
r₄ = 2·z + e₄      e₄ = [ 0, −1, −1, +1, +2, −1]      Σe₄ = 0   Σz·e₄ = 0   Σe₄² =  8
```

The true factor returns are `f = 2, 3, 2, 2`. The misses were chosen to satisfy `Σz·e = 0` —
Level 2's balance condition — which has a consequence worth pausing on:

> **The true dial is recovered *exactly* by least squares in every month.** `b_z = Σz·r/6`
> gives `12/6 = 2`, `18/6 = 3`, `12/6 = 2`, `12/6 = 2`. There is no estimation error in the
> true coefficient at all. Everything that goes wrong on this page goes wrong anyway.

Say plainly at the table: **this is a constructed file.** No real desk knows `z`. The whole
point is to watch a search fail in a case where we can see the answer.

### 3b. The candidate universe — why there are exactly ten tests

A candidate substyle here is a rule that calls three of the six stocks "high" and three
"low": exposure `+1` and `−1`. That is the crudest possible standardised column, and it has
two properties the paper's real columns also have — **weighted mean zero** (p.10) and the
same spread for every candidate.

```
ways to choose 3 of 6 = 20
```

But a column and its mirror image are **the same test**. Flip every sign: `S → −S`, `b → −b`,
the residuals are untouched, `SSE` is untouched, and `t²` is unchanged. (Verified for all ten
columns in the script.) So:

```
20 splits ÷ 2 mirror images  =  10 distinct tests
```

**Ten candidates is not a number I chose. It is every balanced `±1` column that exists on six
stocks.** That exhaustiveness is what makes Section 5's null rate exact rather than assumed.
*(Columns with other values — `+2, +1, 0, 0, −1, −2` — are balanced too; the level restricts
itself to the three-high/three-low rule defined above, and that family has exactly ten members.)*

List them with AXL always on the high side, one per mirror pair. The names are **invented**,
except one: *Random Substyle* is the paper's own (p.56, Table 1.4).

| | high side | low side | what it is pretending to be |
|---|---|---|---|
| **C1** | AXL BRN CHR | DLT EMK FNX | **Random Substyle** — a coin flip, carried as a control |
| **C2** | AXL BRN DLT | CHR EMK FNX | **Payout** — and it is `z`, the true factor |
| C3 | AXL BRN EMK | CHR DLT FNX | Asset Growth |
| C4 | AXL BRN FNX | CHR DLT EMK | Analyst Revision |
| C5 | AXL CHR DLT | BRN EMK FNX | Accruals |
| C6 | AXL CHR EMK | BRN DLT FNX | Share Turnover |
| C7 | AXL CHR FNX | BRN DLT EMK | Book-to-Price |
| C8 | AXL DLT EMK | BRN CHR FNX | Cash-Flow Yield |
| C9 | AXL DLT FNX | BRN CHR EMK | Sales Growth |
| C10 | AXL EMK FNX | BRN CHR DLT | Debt-to-Assets |

### 3c. The shortcut that makes this hand work

Every candidate column has `Σx² = 6`. Every month has `Σr = 0`. So for a column with `+1` on
a triple `T`:

```
S = Σx·r  =  (sum of T)  −  (sum of the rest)  =  2 × (sum of T)
b = S/Σx² = S/6
```

**One addition per candidate.** Add up the three returns the column calls high, and double
it. That is the whole calculation. No multiplication, no division, ten candidates in about a
minute. Fit the market column as well and the model is `r = a·1 + b·x`; because `Σx = 0` the
two columns do not interfere (Level 5), `a` comes out exactly 0, and:

```
SSE = Σr² − S²/6            df = n − k = 6 − 2 = 4            σ̂² = SSE/4
Var(b) = σ̂²/6               t² = b²/Var(b)                    R² = (S²/6)/Σr²
```

> **The intercept costs a degree of freedom even though it comes out zero.** `df = 4`, not 5.
> A player who writes `df = 5` here has forgotten Level 6 §6, and BFRE has **three** columns
> of ones (p.26: *"for each asset, there exist three intercept terms"*), not one.

### 3d. The bar, expressed in `S`

Substitute and the bar `t² ≥ 4` becomes something you can check by eye:

```
t²  =  b²/Var(b)  =  (S/6)² ÷ (σ̂²/6)  =  S²/(6·σ̂²)          ← Level 6's t, nothing new
     with σ̂² = SSE/4 = (Σr² − S²/6)/4:

t²  =  4S² / (6·(Σr² − S²/6))  =  (2/3)·S² / (Σr² − S²/6)     ≥  4
⇔   2S²  ≥  12·Σr² − 2S²
⇔   4S²  ≥  12·Σr²
⇔   S²   ≥  3·Σr²
```

```
month 1:  S² ≥ 3×56 = 168   ⇒   |S| ≥ 12.961481 (rounded)   ⇒   |S| ≥ 14, since S is even
month 2:  S² ≥ 3×78 = 234   ⇒   |S| ≥ 15.297059 (rounded)   ⇒   |S| ≥ 16, since S is even
```

*(`S` is even because `S = 2 × (sum of the high triple)` and the returns are whole numbers of
percent. That is a property of this file, not of the world.)*

---

## 4. Month one — the search finds the placebo

### 4a. All ten, ranked

| | high side | `S` | `b` | `SSE` | `R²` | `t²` | `\|t\|` |
|---|---|---:|---:|---:|---:|---:|---:|
| **C1** *Random* | AXL BRN CHR | **16** | 8/3 | 40/3 | 16/21 | **64/5** | **3.577709** *(rounded)* |
| **C2** *the truth* | AXL BRN DLT | 12 | 2 | 32 | 3/7 | 3 | 1.732051 *(rounded)* |
| C3 | AXL BRN EMK | 10 | 5/3 | 118/3 | 25/84 | 100/59 | 1.301889 *(rounded)* |
| C5 | AXL CHR DLT | 8 | 4/3 | 136/3 | 4/21 | 16/17 | 0.970143 *(rounded)* |
| C6 | AXL CHR EMK | 6 | 1 | 50 | 3/28 | 12/25 | 0.692820 *(rounded)* |
| C10 | AXL EMK FNX | −6 | −1 | 50 | 3/28 | 12/25 | 0.692820 *(rounded)* |
| C4 | AXL BRN FNX | 4 | 2/3 | 160/3 | 1/21 | 1/5 | 0.447214 *(rounded)* |
| C9 | AXL DLT FNX | −4 | −2/3 | 160/3 | 1/21 | 1/5 | 0.447214 *(rounded)* |
| C8 | AXL DLT EMK | 2 | 1/3 | 166/3 | 1/84 | 4/83 | 0.219529 *(rounded)* |
| C7 | AXL CHR FNX | 0 | 0 | 56 | 0 | 0 | 0 *(exact)* |

**Exactly one of the ten clears `|t| > 2`, and it is the placebo.**

### 4b. The winner, in full

```
C1:   S = 16        b = 16/6 = 8/3
      SSE = 56 − 256/6 = 40/3
      σ̂²  = (40/3)/4 = 10/3
      Var(b) = (10/3)/6 = 5/9        SE = √(5/9) = 0.745356 (rounded)
      t  = (8/3)/0.745356 = 3.577709 (rounded)          t² = 64/5 = 12.8
      R² = (256/6)/56 = 16/21 = 0.761905 (rounded)
```

A researcher writes: *"C1 is significant at t = 3.58 and explains 76% of the cross-section.
Recommend adding it to the model."* Every number in that sentence is arithmetically correct.

### 4c. The truth, in full — and it fails

```
C2:   S = 12        b = 12/6 = 2      ← exactly the true factor return
      SSE = 56 − 24 = 32              ← exactly Σe₁², because Σz·e₁ = 0
      σ̂²  = 32/4 = 8
      Var(b) = 8/6 = 4/3              SE = √(4/3) = 1.154701 (rounded)
      t  = 2/1.154701 = 1.732051 (rounded)              t² = 3
      R² = 24/56 = 3/7 = 0.428571 (rounded)
```

> **Put the two side by side and read them out loud.** The column that is *really there*,
> whose coefficient is estimated with **zero error**, scores `t = 1.73` and would be
> rejected. The column that is **nothing at all** scores `t = 3.58` and would be shipped. The
> file is not unlucky and it is not extreme — it is one of the twenty deals in §5a.

### 4d. Where the winner's 16 came from

`r₁ = 2z + e₁`, so:

```
S_C1 = C1·r₁ = 2·(C1·z) + C1·e₁ = 2×2 + 12 = 4 + 12 = 16
```

| Part | Size | What it is |
|---|---:|---|
| `2·(C1·z)` | **4** | borrowed — C1 overlaps the true column |
| `C1·e₁` | **12** | pure luck — C1 happened to line up with this month's misses |

```
share of the winner's score that is luck = 12/16 = 3/4
overlap:  C1·z = 2   ⇒   cos = 2/6 = 1/3   ⇒   VIF = 1/(1 − 1/9) = 9/8
```

**A `VIF` of 1.125 is nothing.** Level 4's disease is not what is happening here — for scale,
the largest exposure correlation the paper prints anywhere is **0.74**, Size against
Liquidity, Figure 1.3 on **p.11** *(printed digits, not a pixel measurement — Figure 1.3 is
one of only four exhibits in the paper that prints its values)*, and Level 4's formula turns
that into `1/(1 − 0.74²) = 2500/1131 = 2.210433` (rounded). Our columns barely touch. Three
quarters of this discovery is not borrowed from a real factor — it is **the residual, found
by looking**, and no collinearity diagnostic in the paper or anywhere else can see that.

### 4e. BFRE's own two-step screen, run on this file

The paper does not test a candidate against raw returns. **PAPER, pp.10–12,** equations
(1.3)–(1.6): fit the model you already have, then regress the candidate on the **residuals**.
So do that. The desk already has the true factor in the model:

```
step 1:   fit z alone      b = 2      residuals e₁ = [+2, +1, +3, −3, 0, −3]     SSE = 32
step 2:   regress e₁ on C1     b = 12/6 = 2     SSE falls 32 → 8
          the placebo removes 24 of the 32 remaining miss  =  3/4 of it
          σ̂² = 8/4 = 2      Var(b) = 2/6 = 1/3      t = √12 = 3.464102 (rounded)
```

**The paper's own screen, applied to a model that already contains the true factor, hands the
Random Substyle a `t` of 3.46 and three quarters of the remaining miss.** That is the attack
in its sharpest form, and it is built entirely out of the paper's stated procedure.

*(The two-step `t` of 3.46 and the joint `t` of 4.02 in 4f are different numbers for the
reason Level 4 §14e gave: residualising the *return* but not the *column* is the incomplete
half of the move. Neither number rescues anything here.)*

### 4f. What it costs to ship it — the joint fit

Put both columns in the model, which is what shipping means. Level 3's 2×2 system:

```
A = z·z  = 6        B = z·C1 = 2        C = C1·C1 = 6
p = z·r₁ = 12       q = C1·r₁ = 16
det = AC − B² = 36 − 4 = 32

b_z  = (Cp − Bq)/det = (72 − 32)/32 = 40/32 = 5/4
b_C1 = (Aq − Bp)/det = (96 − 24)/32 = 72/32 = 9/4

fitted  = [3.5, 3.5, 1, −1, −3.5, −3.5]
e       = [+0.5, −0.5, 0, 0, +1.5, −1.5]      Σe = 0   Σz·e = 0   ΣC1·e = 0   SSE = 5
df = 6 − 3 = 3      σ̂² = 5/3      Var(b) = σ̂²·A/det = 5/16      SE = 0.559017 (rounded)
t_z  = (5/4)/0.559017 = 2.236068 (rounded)         t_C1 = (9/4)/0.559017 = 4.024922 (rounded)
R² = 1 − 5/56 = 51/56 = 0.910714 (rounded)
```

Three things to say to the player, in this order:

1. **The reported factor return for the true factor drops from 2 to 5/4** — it loses `3/8`
   of itself, 37.5%, to a column that means nothing. This is Level 4's lesson with a new
   victim: the coefficient is a *leftover*, and the placebo took some of the leftover.
2. **Now both columns clear the bar.** `t_z = 2.24`, `t_C1 = 4.02`. Admitting the junk column
   made the real one look *more* significant, not less. There is no diagnostic on this page
   that flags what has happened.
3. **`R²` went up.** `3/7 → 51/56`, i.e. `0.428571 → 0.910714` (both rounded). It always
   does, and the one-line reason is new here, so give it: least squares is free to set the new
   column's coefficient to **zero**, which reproduces the old fit exactly, so the best it can do
   is never worse — `SSE` can only fall and `R²` can only rise. `R²` rising when you add a column
   is not evidence, it is arithmetic — and it is why the paper's own
   `R²` (**PAPER, p.32:** *"the proportion of cross-sectional variation in asset returns
   explained by the set of common factors in the model"*) cannot on its own distinguish a
   model that explains from a model that interpolates.

---

## 5. The null rate, computed exactly — no distribution assumed

Level 6 built a standard error by enumerating 32 worlds rather than quoting a formula. Do the
same thing here, to a different object.

### 5a. The permutation null: deal the six returns out at random

Fix one candidate column. Now imagine the six returns were dealt out to the six stocks at
random — the column knows nothing, so this is exactly the world in which the column is
worthless. `S = 2 × (sum of the three returns that land on the high side)`, and the three
that land there are a uniformly random choice of 3 from 6.

```
20 equally likely deals.     Which of them clear the bar?
```

**Month 1** (`|S| ≥ 14`, i.e. high-side sum ≥ 7 in magnitude), from `{+4, +3, +1, −1, −2, −5}`:

```
{+4, +3, +1} = +8  ✓        {−1, −2, −5} = −8  ✓        every other triple: |sum| ≤ 6
```

**Month 2** (`|S| ≥ 16`, i.e. high-side sum ≥ 8), from `{+2, +2, −3, +5, 0, −6}`:

```
{+2, +2, +5} = +9  ✓        {−3, 0, −6} = −9  ✓         every other triple: |sum| ≤ 7
```

```
        ┌────────────────────────────────────────────────────────────────┐
        │  P(a worthless column clears |t| > 2 on this file)             │
        │        =  2 deals out of 20  =  1/10  =  10%,   exactly,       │
        │  in both months, with no distribution assumed anywhere.        │
        └────────────────────────────────────────────────────────────────┘
```

### 5b. The expected count — and why it needs no independence

The ten tests are run on the *same* returns, so they are not independent of one another. It
does not matter:

```
expected number of the ten that clear  =  10 × 1/10  =  1        exactly
```

**Expectation adds, whether or not things are independent.** That is the whole argument, and
it is why this is the assumption-free part of the level. In this file, exactly one *did*
clear. A desk running this screen over ten candidates should expect **one "discovery" a
month even if every single candidate were worthless** — and it will not look like a
discovery-per-month, it will look like one convincing result.

### 5c. The average squared t-statistic — BFRE's own diagnostic, on a placebo universe

**PAPER, p.8:** alongside the proportion of significant t-statistics the paper computes *"the
average squared t-statistic"*, *"to distinguish between factors with t-statistics close to
+/− 2 and those that are significantly higher"*. Compute it here, over the ten candidates:

```
month 1:  average of the ten t²  =  1.984428 (rounded)
month 2:  average of the ten t²  =  1.691074 (rounded)
```

Roughly **two**, from a universe of columns of which nine are meaningless and one is real.

> **Careful, and this is a Level-6 callback the player must get right.** Level 6 §8e proved
> `E[t²] = 1` **when `σ²` is known**, and that with an *estimated* `σ̂²` at `df = 4` the
> average comes out larger — it computed 1.676788 (rounded) for its own 32 worlds. These two numbers
> (1.98, 1.69) are a *different* enumeration of a *different* null, so they need not equal
> Level 6's. What travels between them is the shape of the claim: **an average squared `t` of
> about two is what nothing looks like at this `df`.** Do not let the player quote 1.98 as a
> universal constant, and do not let them carry it to BFRE, whose cross-sections have
> thousands of stocks and therefore a `df` in the thousands.

---

## 6. Month two — the winner is somebody else

Same six stocks, next month. Run the same ten sums.

### 6a. All ten, ranked

| | high side | `S` | `b` | `SSE` | `R²` | `t²` | `\|t\|` |
|---|---|---:|---:|---:|---:|---:|---:|
| **C2** *the truth* | AXL BRN DLT | **18** | 3 | 24 | 9/13 | **9** | **3** *(exact)* |
| C7 | AXL CHR FNX | −14 | −7/3 | 136/3 | 49/117 | 49/17 | 1.697749 *(rounded)* |
| C8 | AXL DLT EMK | 14 | 7/3 | 136/3 | 49/117 | 49/17 | 1.697749 *(rounded)* |
| C3 | AXL BRN EMK | 8 | 4/3 | 202/3 | 16/117 | 64/101 | 0.796030 *(rounded)* |
| C5 | AXL CHR DLT | 8 | 4/3 | 202/3 | 16/117 | 64/101 | 0.796030 *(rounded)* |
| C10 | AXL EMK FNX | −8 | −4/3 | 202/3 | 16/117 | 64/101 | 0.796030 *(rounded)* |
| C4 | AXL BRN FNX | −4 | −2/3 | 226/3 | 4/117 | 16/113 | 0.376288 *(rounded)* |
| **C1** *Random* | AXL BRN CHR | **2** | 1/3 | 232/3 | 1/117 | **1/29** | **0.185695** *(rounded)* |
| C6 | AXL CHR EMK | −2 | −1/3 | 232/3 | 1/117 | 1/29 | 0.185695 *(rounded)* |
| C9 | AXL DLT FNX | 2 | 1/3 | 232/3 | 1/117 | 1/29 | 0.185695 *(rounded)* |

Again **exactly one** of the ten clears the bar — and this month it is the true factor, at
`t = 3` exactly (`SE = 1` exactly, because `σ̂² = 24/4 = 6` and `Var(b) = 6/6 = 1`).

### 6b. The three numbers that matter

```
last month's champion, C1:     t = 3.577709 (rounded)   →   0.185695 (rounded)
                               R² = 16/21 = 0.761905    →   1/117 = 0.008547     (both rounded)
                               finishes 8th of ten, tied at the bottom with C6 and C9
the true factor, C2:           t = 1.732051 (rounded) → 3 exactly     R² = 3/7 → 9/13
```

The placebo's `R²` fell by a factor of `624/7 = 89.142857` (rounded). Nothing about the
*column* changed. Only the month changed.

### 6c. And this is what "in-sample" means

|  | month it was found | the next month |
|---|---:|---:|
| **C1** (Random Substyle) | `R² = 0.761905` *(rounded)* | `R² = 0.008547` *(rounded)* |
| **C2** (the true factor) | `R² = 0.428571` *(rounded)* | `R² = 0.692308` *(rounded)* |

> **Name it now, because the mechanism is finally on the table.** A number computed on the
> data used to choose the thing is **in-sample**. A number computed on data the choice never
> saw is **out-of-sample**. The gap between C1's two columns is not noise: it is the size of
> the search, made visible.

**In the paper (`gm/VOCAB.md` term 16):** *"in-sample"* appears **nowhere** in the 65 pages.
*"Out-of-sample"* appears **exactly once** — **PAPER, p.30:** *"Out-of-sample model
back-testing is conducted on a subset of such portfolios as part of the Quarterly Aladdin
Risk Model conference calls."* Read that sentence carefully with the player: it is
out-of-sample testing of **portfolios poorly represented in the estimation universe**, not an
out-of-sample test of the factor-selection procedure. Same words, different object. A player
who cites p.30 as "they did test out-of-sample" has fallen for it.

### 6d. What the desk would have published

Ship the placebo and report both factor returns each month, from the joint fit:

| | month 1 | month 2 |
|---|---:|---:|
| `b` for the true factor | 5/4 = 1.25 | 13/4 = 3.25 |
| `b` for the Random Substyle | **+9/4 = +2.25** | **−3/4 = −0.75** |
| `t` for the Random Substyle | 4.024922 *(rounded)* | 0.654654 *(rounded)* |

The placebo's published factor return **changes sign between two consecutive months**, from
`+2.25%` to `−0.75%`, with no change to any column. **PAPER, p.32**, on what collinear or
unstable columns do: *"This can result in significant instability in the factor return
estimates through time."* The paper's diagnostic for that is the variance inflation factor,
and here `VIF = 9/8` — which would have raised no alarm whatsoever. **INFER, and say so:**
this file shows a failure mode that a VIF cannot see, because it is not collinearity, it is
selection.

### 6e. Months three and four — and the paper's actual rule, run on the file

BFRE does not admit a factor on one month. It counts the **proportion of months** in which a
candidate clears `|t| > 2` (**PAPER, p.14**). So run the ten sums twice more. Months 3 and 4:

```
r₃ = [+4, +1, −1, +1, −1, −4]     Σr² = 36     bar: S² ≥ 108  ⇒  |S| ≥ 10.392305 (rounded) ⇒ |S| ≥ 12
r₄ = [+2, +1, −3, +3,  0, −3]     Σr² = 32     bar: S² ≥  96  ⇒  |S| ≥  9.797959 (rounded) ⇒ |S| ≥ 10
```

`S` for all ten, all four months — **forty numbers, each one addition** — with the ones that
clear their month's bar in bold:

| | month 1 <br>`\|S\| ≥ 14` | month 2 <br>`\|S\| ≥ 16` | month 3 <br>`\|S\| ≥ 12` | month 4 <br>`\|S\| ≥ 10` | months cleared |
|---|---:|---:|---:|---:|---:|
| **C1** *Random* | **16** | 2 | 8 | 0 | **1 of 4 = 25%** |
| **C2** *the truth* | 12 | **18** | **12** | **12** | **3 of 4 = 75%** |
| C3 | 10 | 8 | 8 | 6 | 0 |
| C4 | 4 | −4 | 2 | 0 | 0 |
| C5 | 8 | 8 | 8 | 4 | 0 |
| C6 | 6 | −2 | 4 | −2 | 0 |
| C7 | 0 | −14 | −2 | −8 | 0 |
| **C8** | 2 | 14 | 8 | **10** | **1 of 4 = 25%** |
| C9 | −4 | 2 | 2 | 4 | 0 |
| C10 | −6 | −8 | −2 | −2 | 0 |

The five clears in full, with `t` from the same formula as everywhere else on this page:

```
month 1  C1  t = 3.577709 (rounded)        month 3  C2  t² = 8   t = 2.828427 (rounded)
month 2  C2  t = 3 exactly                 month 4  C2  t² = 12  t = 3.464102 (rounded)
                                           month 4  C8  t² = 100/23  t = 2.085144 (rounded)
```

Three facts, and the third is the one that matters:

1. **The ranking works.** The true factor is top of the table at 75%, and it is the only
   column that ever clears twice. A persistence count is a genuinely better statistic than any
   single month's `t`, and Sections 4 and 5 do not touch that claim.
2. **The bar does not.** BFRE's stated bar is a proportion of significant t-statistics *"in
   excess of 10%"* (p.14). Over four months, **the smallest non-zero proportion that exists is
   25%** — so "clears more than 10% of months" and "clears at least once, ever" are the *same
   rule*, and it admits **three of the ten columns, two of which are noise** (C1 and C8).
3. **And this is not bad luck.** If a junk column clears in a given month with probability
   `1/10` (§5a) and the months are independent, then `P(at least once in four) = 1 − (9/10)⁴ =
   3439/10000`; nine of our ten columns are junk, so the expected number of junk columns
   clearing at least once is `9 × 3439/10000 = 3.0951`. The file delivered **2**. The
   arithmetic is not describing a freak file; it is describing the ordinary one — and §7a
   lays it out properly, with the independence assumption named.

> **This is what the whole level turns on.** A proportion bar is only a filter if there are
> enough months behind it. BFRE has roughly **180** (p.8's 15-year history); this file has
> four. The next section is the arithmetic that says how much those 180 months buy — and it is
> the paper's best answer, so the player has to be able to make it.

---

## 7. THE DEFENCE, as arithmetic — persistence

**Run this section *before* the boss round and make the player do the arithmetic, because it
is the paper's best answer and they will have to give it under fire.**

The desk's answer to everything in Sections 4–6 is one sentence: *we do not admit a factor on
one month.* **PAPER, p.14:** a style is considered for inclusion when the **proportion** of
significant t-statistics exceeds 10%. **PAPER, p.12:** the recursion stops when the best
remaining candidate's proportion is *"no larger than 10% - 15%"*. **PAPER, p.8:** the whole
thing is measured over a 15-year history and checked on five-year sub-samples.

§6e has just shown the rule failing on four months. So: how much does requiring repetition
actually buy, and how many months does it take to buy it?

### 7a. Repetition rules on this file — 10 candidates, `p = 1/10`

**One assumption, and it must be said out loud every time this table is used: the months are
treated as independent.** §5b needed nothing; this table needs that. Level 9's distinction —
what the arithmetic guarantees versus what the modeller assumes — is exactly the distinction
between §5b and §7a.

| Rule for admitting a factor | `P` for one junk column | Expected junk winners out of 10 |
|---|---:|---:|
| clears once, in one month | 1/10 | **1** *(exact)* |
| clears in **both** of 2 months | 1/100 | 1/10 = 0.1 *(exact)* |
| clears in **at least 1 of 4** months (= 25% of months) | 3439/10000 | 3.439 *(exact)* |
| clears in **at least 3 of 4** months | 37/10000 | 0.037 *(exact)* |

The arithmetic for the last two, by hand:

```
P(at least 1 of 4)  = 1 − (9/10)⁴ = 1 − 6561/10000 = 3439/10000
P(at least 3 of 4)  = 4·(1/10)³·(9/10) + (1/10)⁴ = 36/10000 + 1/10000 = 37/10000
```

```
the 3-of-4 rule divides the expected number of junk winners by
        (1/10) ÷ (37/10000)  =  1000/37  =  27.027027 (rounded)
```

**That is a real defence, and it is large.** Requiring a factor to keep clearing the bar is
worth a factor of twenty-seven here. A player who cannot say that has not understood the
paper.

### 7b. The same rules with 200 candidates

| Rule | Expected junk winners out of **200** |
|---|---:|
| clears once, in one month | **20** *(exact)* |
| clears in both of 2 months | 2 *(exact)* |
| at least 1 of 4 months | 68.78 *(exact)* |
| at least 3 of 4 months | 0.74 *(exact)* |

> **This is the shape of the whole argument.** The persistence rule divides by 27. Multiplying
> the candidate list by 20 multiplies back. Whether the rule is *enough* is not a matter of
> opinion; it is a division, and it depends on a number the paper prints (**200+**, p.55) and
> a number the paper does not (the null rate).

### 7c. Scaled to the paper's own numbers — and where hand arithmetic stops

**Everything in this box is INFER. It is the rival's arithmetic on the paper's printed
numbers, and none of it is a calculation the paper performs.**

BFRE's cross-sections carry thousands of stocks, so `df` is enormous and Level 6 §8e's
`E[t²] ≈ 1` is safe. Take the rival's assumption that a worthless column clears `|t| > 2` in
about **1 month in 20** — *this is an assumption, it is not on any page, and the player must
say so every single time.* Take the 15-year monthly history of p.8 as ~180 cross-sections and
the bar of p.14 as 10% of them. *(Even that count is approximate **on the paper's own
evidence**: p.8 says "15-year research history", while **p.32** dates the whole testing
history *"from 1996 to 2013"* and the paper's longest-running dated exhibits — Table 1.2 on
**p.10** and Figure 1.7 on **p.14** — are labelled **Mar 1996 – Dec 2013**, which is nearly
eighteen years and would be ~214 monthly cross-sections. (Do **not** say "every dated exhibit":
the paper's dated exhibits run to several different windows — Figure 1.8 ends Jun 2013,
Figure 1.10 ends Dec 2010, and Figures 1.1–1.3 are single dates.) The paper never reconciles
the 15 years with the 1996–2013 span, so say "roughly 180" and never quote a precise month
count as theirs.)*

```
expected significant months for a junk column   =  180 × 1/20  =  9        ← hand arithmetic
the bar                                          =  10% of 180  =  18
so the bar is exactly 2× the expected count.
Markov (Level 6 §8f), assuming nothing:   P(count ≥ 18) ≤ 9/18 = 1/2       ← useless, and honest
```

To do better than "at most a half" you need a distribution. Here is the exact binomial —
**and this is machine arithmetic, not hand arithmetic, and it assumes the months are
independent draws:**

```
P(count ≥ 18 | 180 months, p = 1/20)  =  0.004217 (rounded)
expected junk survivors out of 200 candidates  =  0.843421 (rounded)
```

| The screen | Expected junk factors admitted, out of 200 |
|---|---:|
| `\|t\| > 2` in a single month, no persistence rule | 10 *(exact)* |
| ≥10% of ~180 months at `\|t\| > 2` | **0.843421** *(rounded)* |

**Say both halves of that out loud.** The persistence rule takes ten spurious factors per
month down to under one across the whole history. It is a *good* rule. And "under one out of
two hundred" is not zero — it is approximately the number of factors a rival would be arguing
about.

### 7d. The comeback — and the one line in Table 1.2 that pays for it

Three things, in this order, and the third is the one worth bps:

1. **A persistence rule is a stronger single test, not a multiple-comparison correction.**
   The correction you need scales with the number of candidates; nothing in the paper scales
   with anything. **PAPER, p.8** names LASSO, LARS, group lasso, Ridge and Bayesian priors —
   the literature that contains the corrections — and declines them because they *"are purely
   statistical in nature and rely heavily on historical data"*. Having named the shelf, the
   paper owes an alternative control, and there is none.
2. **The 0.843 above rests entirely on independence across months.** Drop that and the number
   moves, in the direction that hurts: a column whose luck persists is exactly a column that
   clears the bar in runs.
3. **The paper prints its own evidence that months are not independent draws.**
   **PAPER, p.10, Table 1.2**, first-order autocorrelation of factor returns: Momentum
   **0.22**, Reversal **0.17**. **INFER, and the gap must be stated:** those are
   autocorrelations of *factor returns*, not of the monthly *t-statistics* the screen counts,
   and the paper never reports the latter. So this does not prove the screen is broken. It
   proves the paper had, on page 10, the beginning of the check it never ran.

And then the sentence that ends the exchange, which is the *measurement* the whole of Section
5 has been substituting for:

> **PAPER, p.56:** there is a **Random Substyle** in the candidate inventory. One line — what
> proportion of months did it clear `|t| > 2`? — would replace every estimate in this section
> with a fact. It is not printed.

---

## 8. The three questions that turn a complaint into an attack

A complaint is something true about the document. An attack is a complaint that survives the
answer. The filter, applied before opening your mouth:

| | Question |
|---|---|
| **Q1** | **Does it reach something the users rely on** — a risk number, or the evidence behind every risk number? |
| **Q2** | **Can the person you are attacking check it in two page-turns, without doing arithmetic you supply?** |
| **Q3** | **Does it survive the paper's own best answer?** |

Worked, on six items. *(The dossier ranks are `gm/CRITIQUE.md` §4's, recomputed from that file
by the verifier — they are not my opinion.)*

| Item | Q1 | Q2 | Q3 | Verdict | Dossier rank |
|---|:--:|:--:|:--:|---|---:|
| **G-3** — every accuracy claim deferred to reference [27], listed *forthcoming* (pp.32, 33, 65) | ✓ | ✓ | ✓ | **lead with this** | **1** of 20 |
| **F-2** — 200+ candidates, no correction, a placebo whose score is never printed (pp.10, 55, 56) | ✓ | ✓ | ✓ | second | **2** of 20 |
| **F-1** — a stated 10% bar with factors shipped below it (pp.14, 15, 32) | ✓ | part — p.32's *"majority"* is printed; the bar heights are not | ✓ | third | **3** of 20 |
| **A-6** — the whole factor covariance method deferred to a BRS document (p.27) | ✓ | ✓ | ✓ | strong, and it pairs with G-3 | **5** of 20 |
| **5.1** — √-cap-weighted mean, equal-weighted standard deviation (pp.10, 39) | ✗ — the invariance argument bounds the harm to interpretation | ✓ | ✗ — the defence is the strongest in the dossier | *a question, not a charge* | **9** of 20 |
| **H-3…H-5** — prose that contradicts its own formula (pp.45, 49, 54) | ✗ | ✓ | ✗ — "follow the formula" | **corroboration only** | **20** of 20 |

**The tie-break, when two items pass all three.** G-3 and F-2 both score 3/3, and the dossier
rates both attacks at five stars. It ranks G-3 first because its **defence** is rated three
stars against F-2's four. So:

> **Equal attacks: lead with the one whose defence is weaker.** Your opening should be the
> thing they can least easily answer, not the thing you find most interesting.

**And the rule that outranks all of the above.** Twelve items in `gm/CRITIQUE.md` §6 are
**cheap shots**: complaints that are true, or nearly true, and that *cost you the room*
because the paper answers them on the page. Leading with one is the doorbell in Story B. The
player must be able to name at least three of the twelve unprompted before this level is
passed.

---

## 9. What the player must produce — THE CRITIQUE SHEET

One page, eleven line items, handwritten, no notes at the table. This is the level's
deliverable and the boss round is run against it.

| Block | Count | What each line must contain |
|---|---:|---|
| **Attacks, ranked** | 3 | claim · page · the mechanism by which it changes or fails to support a number · the paper's best defence, stated at full strength · the comeback |
| **Concessions** | 4 | something the paper does **well**, with the page. `gm/CRITIQUE.md` §8 lists twelve; the dossier requires at least four |
| **Cheap shots refused** | 3 | the attack you are *not* making, and the one line that kills it |
| **The experiment** | 1 | the single thing that, if published, would settle your biggest attack |
| **Total** | **11** | |

**Grading the sheet, before any conversation happens:**

- An attack with no defence written next to it is not an attack. Strike it and its rank.
- A concession that is really a compliment ("it is thorough") is not a concession. A
  concession names a specific thing the paper did that the rival would have to grant under
  oath — p.26's identification problem found, named, fixed and its side-effect disclosed;
  p.16's published before/after diagnostic with a visible failure state; p.28's stated
  *direction* of the error; and **p.38's tail test, the one parameter in the document
  justified against an external standard** — *"the proportion of violations of 99% 1-day VaR
  over the previous 252 days"*, footnoted as consistent with UCITS guidelines and following
  **Kupiec (1995)**.
- The experiment is Tier 5 on the ladder and it is where the best players separate. The
  strongest one available is one line long: **print what the Random Substyle scored** (p.56).

---

## 10. The map of the dossier — counts only

The player finds the items. The GM checks them against `gm/CRITIQUE.md`, which holds
**40** named weaknesses, **12** cheap shots, **12** concessions, **6** grey-zone items and a
**20** ranked scoreboard, with **5** automatic-fail conditions. Those counts are recomputed
from that file every time the verifier runs, so this paragraph cannot go stale.

The 40 break down as 38 numbered items in eight classes plus two charges the dossier argues
as wholes (the standardisation asymmetry in §5.1, and the whole window/half-life class D):

| Class | What the class is | Items |
|---|---|---:|
| A | parameters and thresholds stated without justification | 7 |
| B | asymmetries stated but never explained | 6 |
| C | evidence resting on a single date or anchor month | 9 |
| D | windows and half-lives with **no sensitivity analysis anywhere** | *argued as one charge* |
| E | stories no result could falsify | 4 |
| F | significance thresholds and multiple testing | 2 |
| G | diagnostics that cannot tell a good model from a bad one | 5 |
| H | internal inconsistencies — free ammunition, low glory | 5 |

Class sizes A–H, in order: **7 / 6 / 9 / 4 / 2 / 5 / 5** *(class D carries no numbered
items)*.

**Do not read the dossier to the player.** Two of the eight classes are this level's
arithmetic (F, and G by way of Level 0's boss round); the player should arrive at those
unaided after Sections 4–7. Hand over an item only when they have circled the page it lives
on.

---

## 11. Traps, and exactly what each one costs

| # | The wrong belief | What it actually is | What it costs |
|---|---|---|---|
| 1 | *"Sentiment scores 7% and Earnings Yield 4%, both below your own bar."* | Those are **pixel measurements** of Figure 1.8 (p.15) `[APPROX]`. **The paper prints no data labels on that chart.** | **Automatic fail** (`gm/CRITIQUE.md` §10). The admissible form: *"the two shortest bars sit below the 10% you state in prose on the previous page, and you print no values"* — and note Figure 1.8 **has no threshold line drawn on it**; the dashed 10% line is on Figure 1.10, p.16 |
| 2 | *"You never print an `R²` anywhere."* | **PAPER, p.4:** daily S&P 500 excess returns on daily NAMR market factor returns gives **beta = 0.99, R² = 91%** — a different regression, one index on one factor | One page-turn and the exchange is over. The correct sentence: *the only `R²` in the document is a two-variable sanity check on p.4; the cross-sectional `R²` you name on p.32 as your measure of overall explanatory power never gets a value, a formula or a benchmark* |
| 3 | *"As the paper says, tracking error…"* / *"…their eigenvalues…"* | Neither phrase occurs in 65 pages. The paper's word is **Active Risk** (p.35) | **Automatic fail.** Both words are the *game's* — tracking error at L11, eigenvalue at L8. Using the concepts is expected; sourcing them to BFRE is the fail |
| 4 | *"Their portfolio beta formula is `βₚ = (Xₚᵀ F X_b)/(X_bᵀ F X_b)`."* | A **reader's pen annotation in the margin of p.4**. The printed sentence only says beta can be computed from exposures and the factor covariance matrix | **Automatic fail.** Never attribute it to BlackRock |
| 5 | *"(1.8) says `Δ` is diagonal and p.27 admits it isn't — caught them."* | **CS-3.** p.24's lead-in is *"In general a multi-factor model…"*; p.27 states what BFRE builds and p.28 gives it a subsection with the direction of the error | Loses the room. The real attack is the **scope**: correlations only *within* a company; across companies assumed zero *"in-line with standard modelling practice"* (p.28) |
| 6 | *"√-cap weighting is arbitrary."* | **CS-1.** p.25 gives three arguments including heteroskedasticity, and footnote 14 names and dismisses the textbook alternative | Leading here says you did not read p.25. **Instant credibility loss** |
| 7 | *"Selection is monthly but estimation is daily — incoherent."* | **CS-8.** **PAPER, p.30:** the 1-month forecast horizon is the stated organising principle | Half a cheap shot. The real version is the **four** frequencies and the unexplained *weekly* World-model estimation on p.24, for which no reason is given |
| 8 | Quoting *"…no multiple-testing correction is mentioned despite 200+ candidates being tested"* as the paper's words | That sentence is the **transcriber's commentary** in `notes/`, not the paper's text | The worst defect available at this level: it puts a self-indictment in BlackRock's mouth. Say it as an **absence you have checked**, in your own voice |
| 9 | *"I computed the null rate: 10% of columns clear the bar by chance, so their 10% bar is exactly the noise rate."* | **This level's own trap.** `1/10` is an exact fact about a **six-stock** file with `df = 4`. BFRE's cross-sections carry thousands of stocks | Laundering a toy number onto the real model — the same offence as trap 1, committed with your own arithmetic. The transferable claim is the **mechanism**, never the number |
| 10 | *"The Random Substyle proves the model is data-mined."* | It proves the opposite about the authors: a team that carries a placebo has understood the problem. It is **concession 6** in the dossier | Hands the defence a free point. The attack is that its **score** is unpublished |
| 11 | *"They report `R² = 0.91` after adding the junk column, so the model got better."* | §4f. `R²` rises whenever a column is added, because the fit can always set the new coefficient to zero and do no worse | The same failure as Level 0's Desk B: a diagnostic that cannot discriminate |

---

## 12. A sabotage round (round type B) to run before the boss

Hand the player this desk note, told it is finished work, and say one number in it is
corrupted:

```
Candidate C1 (Random Substyle), month 1, six stocks, market + one style column
S = 16     b = 8/3     SSE = 40/3     df = 4
SE = 0.745356 (rounded)      t = 3.577709 (rounded)      t² = 64/5 = 12.8
R² = 0.68
```

`R²` is the lie. It must be caught **without** recomputing `Σr²`, using Level 6 §8c:

```
t² = df·R²/(1 − R²)     ⇒     R² = t²/(t² + df) = 12.8/16.8 = 16/21 = 0.761905 (rounded)
```

`0.68` is impossible given the other numbers on the page. Cross-check the other way: an `R²`
of 0.68 implies `SSE = 0.32 × 56 = 17.92` (exact), and the page says `40/3 = 13.333333`
(rounded). Three views of two numbers, and they must agree.

**Then ask the question this level exists for:** *"You just refused to accept a number whose
origin you could not trace. Page 32 tells you the variance inflation factors 'were found to be
well within suitable thresholds'. Do the same thing to that sentence."*

---

## 13. Names unlocked at the end of this level

**From the sixteen terms the rulebook names (§6F), this level unlocks exactly one** —
`gm/VOCAB.md` term 16:

| Name | What it is, in this level's terms |
|---|---|
| **in-sample / out-of-sample** | C1's `R²` is `16/21 = 0.761905` in the month it was found and `1/117 = 0.008547` in the next one (§6c; both decimals rounded). **"In-sample" appears nowhere in the paper; "out-of-sample" appears exactly once, p.30 — and it is about portfolios, not about the factor list** |

Seven more names come from `gm/CRITIQUE.md`'s own ledger, which files all seven at L12. **All
seven are our words for the paper's problems — none of them appears in the paper**, so they
may never be put in BlackRock's mouth:

| Name | What it is here | Nearest thing the paper prints |
|---|---|---|
| **multiple testing / data mining** | §5b: expected discoveries = candidates × null rate | `N ≥ 200` (p.10), `200+` (p.55) — the problem, never the name |
| **placebo / control descriptor** | C1 | **Random Substyle**, p.56, Table 1.4 — the object, with no prose attached |
| **falsifiable** | §15.6's standing question: *what result would have made that sentence false?* | nothing |
| **post hoc** | choosing the bar after seeing the bars — an accusation this level forbids unless it can be shown | nothing |
| **look-ahead bias** | using tomorrow's information in today's exposure | the `s ≤ t` lag lines, p.47 |
| **sensitivity analysis** | *"we also tried 52 weeks; here is what changed"* | nothing — the absence **is** dossier class D |
| **bias statistic** | forecast risk against realised risk | **p.32**, and its construction on **p.38** — this one the paper does name |

*(Heteroskedasticity was met and named at Level 6 §9 and lives on BFRE p.25; nothing new is
unlocked here. **Newey–West** may be *named* now — p.27, p.28 and reference [26] on p.65 —
but only for what it actually does there: aggregating daily specific returns. It is
**graduate-level** and it is never presented in the paper as the source of any t-statistic.)*

Run a **round type F (vocabulary under fire)** on the five sentences in `gm/CRITIQUE.md` §9,
each of which is a real sentence from the paper. The follow-up is the same every time:
**"What result would have made that sentence false?"**

---

## 14. Ladder position after this level

| Concept | Tier to demand |
|---|---|
| a search is not a test; the winner's `t` is not a column's `t` | **5 (rebuild)** — must be constructible on a file they have never seen |
| in-sample vs out-of-sample, with a number attached | 4 (defend) |
| expected count = candidates × null rate, and why it needs no independence | 4 (defend) — including the independence line in 7a |
| the persistence defence, with the factor of 27 | 4 (defend) — a player who cannot make it may not attack it |
| ranking weaknesses, and naming three cheap shots | **4 (defend)** — this is the level's gate |
| the exact binomial in 7c | 2 (compute) is enough; it is labelled machine arithmetic |
| the paper's own two-step screen, run on new data | 3 (derive) |

Do not mark Level 12 complete unless the player can produce the Critique Sheet of §9
**unprompted**, and defend it in both directions.

---

# 15. BOSS ROUND — The Hearing

Round type: **E. INTERROGATION**. Play the chair of a model-risk committee with thirty years
on the desk and no patience. The round has four moves and they must happen **in this order**.

## 15.1 The shape of the round, and why the order is fixed

> **Defence first. Attack second. The player is not told in advance that they will have to
> switch sides.**

A player who attacks first builds a weak version of the paper and knocks it down, and does not
notice. Making them argue BlackRock's side *cold* forces them to find the real arguments
before they need to beat them. Every strong attack in `gm/CRITIQUE.md` is strong precisely
because it survives a defence the player has already had to make.

## 15.2 Move 0 — the sealed list (two minutes, in writing)

Before anything is said, the player writes their three ranked attacks, four concessions, three
refused cheap shots and one experiment — §9's Critique Sheet — and **hands it over face
down**. It is not read until Move 3.

This exists to stop the level's own version of `post hoc`. A player who hears the defence
first and then produces attacks shaped to it is doing precisely what the rival is forbidden
from *accusing the paper of* (`gm/CRITIQUE.md` F-1: never upgrade "the bar is on a later page"
into "the bar was set after they saw the results"). Hold the player to the standard they are
about to apply to somebody else.

## 15.3 Move 1 — THE CHAIR: you wrote it, now defend it

*"You are the author. I have read your paper. Two questions."*

Attack them with the two strongest items in the dossier and require the **full** defence — not
a gesture at it. The pass bar is that they produce these before hearing any comeback.

**Attack 1 — G-3, the deferred evidence** (dossier rank 1 of 20).
> *"Page 32 tells me an exhaustive set of bias statistics was generated and reviewed. Page 33
> sends me to reference [27] for the results, 'available on request'. Page 65 lists [27] as
> **forthcoming**. So on the day you published, the evidence for every accuracy claim in
> sixty-five pages did not exist in a form anyone could read. Defend that."*

Require all four: **the genre** (client model documentation, not a research paper — and it
specifies the model completely, (1.7)–(1.11), Table 1.3, and (1.12)–(1.55)); **the cycle**
(specification changes rarely, surveillance is continuous — monthly exception logging, a 95%
confidence interval on a rolling 12-month bias statistic, quarterly client reporting, all
**p.38**); **the reproducibility** (statistic, window, band, tail test and portfolio set are all
specified precisely enough for a user to run every one of them on their own book); **the external
exposure** (benchmarking against STORM, **p.38**, and quarterly out-of-sample back-testing in
front of clients, **p.30** — two different pages, and say which is which).

**Attack 2 — F-2, the multiple-testing charge** (rank 2 of 20; graduate-level, say so).
> *"You tested more than two hundred candidates at `|t| > 2` with no correction for having
> tested two hundred. You knew the risk — you put a Random Substyle in your own inventory on
> page 56. What did it score?"*

Require the persistence arithmetic of §7 **as the defence**, not as a slogan: the statistic is
a persistence rate over ~180 monthly cross-sections, not a one-shot p-value; the tests are
conditional, run on the residuals of the model so far ((1.3)–(1.6)); five-year sub-samples;
the alternatives named and declined on the record (p.8); the economic prior; peer review. And
require the number: **10 spurious factors per month becomes 0.843421 (rounded) across the
whole history** — the player's own arithmetic from 7c, delivered with its two caveats intact.

- **Fail** if they defend by asserting BlackRock's competence.
- **Fail** if they say the results are confidential without noticing that *"available on
  request"* and *"forthcoming"* cannot both be true of [27].
- **Fail** if they give the persistence defence without the independence caveat. That is the
  mimicry Victory Condition 2 exists to catch: right answer, borrowed reasoning.

## 15.4 Move 2 — THE FLIP: now take it apart

*"Good. You are no longer the author. You are the rival, you have four minutes with the same
committee, and they have just heard everything you said."*

The player must now attack **the defence they themselves built**, which is the only kind of
attack worth anything. Require:

- an **opening** that is G-3 or F-2 — and a reason for choosing which, in the language of §8
  (equal attacks, lead with the weaker defence);
- the **comeback** to their own Move 1 answers: for G-3, that the cycle and reproducibility
  arguments argue for publishing a *history*, a distribution or a single worst case, not for
  publishing **none**, and that benchmarking against STORM shows the two agree, not that
  either is right; for F-2, that not one of the six defence points is a multiple-comparison
  correction, that sub-samples are three more chances rather than fewer, and that the placebo's
  score is the missing number;
- at least **one concession, unprompted**, in the middle of the attack.

**The bonus, and it is the hinge of the level** (`gm/CRITIQUE.md` E-1's comeback): if the
player connects the unfalsifiable-story class to the multiple-testing class on their own —
*"'it explains co-movement' is the same defence the Random Substyle would get if it happened
to score well"* — award the bps and promote.

## 15.5 Move 3 — THE BAIT: three offers, two of them poison

Turn the sealed sheet over, then say: *"A colleague has sent me three more. Which do you want
me to put in front of the committee?"*

| Offered | What it is | Required response |
|---|---|---|
| *"Their `Δ` is called diagonal on p.24 and isn't on p.27."* | **CS-3** | refuse — *"they give it a subsection with the direction of the error; what I'd attack is the across-company zero"* |
| *"Square-root-of-market-cap weighting is arbitrary."* | **CS-1** | refuse — *"page 25 answers that in a paragraph and footnote 14 answers the follow-up"* |
| *"Reference [27] is listed as forthcoming."* | **G-3**, rank 1 | take it |

A player who takes either of the first two **fails the level**, however well Moves 1 and 2
went. That is not harsh: `gm/CRITIQUE.md` §0 records this as the single thing the level exists
to teach, and a rival who spends a cheap shot has discounted everything they say afterwards.

## 15.6 The interrogation script — real objections, escalating

1. *"You are telling me a factor with a t of 3.58 might be nothing. Show me."*
   → §4a and §5a. Wants the **enumeration**, not an assertion. If they reach for a bell curve,
   stop them: this level assumes no distribution anywhere except the labelled binomial in 7c.
2. *"One in ten. Fine — their bar is 10% of months, so their bar is exactly the noise rate."*
   → **Trap 9.** The `1/10` is a fact about six stocks at `df = 4`. A player who carries it
   to BFRE has done with their own arithmetic exactly what trap 1 forbids doing with a
   pixel measurement. Dock bps, and make them say what the number would be at `df = 2000`
   — they cannot, and neither can I, and that is the honest answer.
3. *"Then their persistence rule fixes it and we are done."*
   → §7a and §7b. Wants the factor of **27**, and then the fact that 200 candidates multiply
   twenty back in. A player who cannot produce both halves is not ranking, they are agreeing
   with whoever spoke last.
4. *"Your 0.843 assumes each month is a fresh coin. Is it?"*
   → §7d. Wants: no, that is an assumption; the paper prints first-order autocorrelations of
   **0.22** and **0.17** on p.10; **and** the honest gap — those are factor returns, not
   t-statistics, so it is a reason to check, not a proof.
5. *"Everything you have said is a made-up six-stock file. Why should I care?"*
   → The right answer names what does and does not transfer: the **mechanism** transfers, the
   **numbers** do not, and the paper's own procedure (1.3)–(1.6) was run on the file in §4e
   and admitted the placebo at `t = 3.46`.
6. *"Give me your best single attack in three sentences."*
   → G-3, pp.32 → 33 → 65. If it takes more than three sentences it is the wrong attack.
7. *"What would change your mind?"*
   → The experiment. Best available: **print what the Random Substyle scored.** Second best:
   one published sensitivity chart for the 26-week half-life against the 1-month horizon.
8. *"Name three things this paper does better than the last one you read."*
   → The concessions. A player who cannot do this in ten seconds has been reading for
   ammunition, and everything they said today was worth less than they thought.

## 15.7 Scoring — why a player who only attacks fails

The level is scored in two halves and they are not independent:

```
DEFENCE  — up to 300 bps: Move 1, the two full defences with their caveats
ATTACK   — up to 300 bps: Move 2, ranked, with the comebacks

                LEVEL SCORE  =  DEFENCE  +  min(ATTACK, DEFENCE)
```

> **Your attack is capped by your defence.** A player who scores zero on Move 1 scores zero
> overall, no matter how true their attacks are — because an attack on a paper you cannot
> state the case for is an attack on a straw man, and the committee can tell.

**Penalties, applied on top:** −100 bps for any pixel-measured figure value quoted as a
printed number; −100 for attacking the scan rather than the document; **level failed** for
opening with a §6 cheap shot, for attributing "tracking error" or "eigenvalue" to the paper,
or for citing p.4's handwritten margin formula as BlackRock's.

## 15.8 Pass conditions

Deny promotion unless **all** of these happen:

- [ ] Move 1's two defences delivered **in full, before any comeback is heard**, including the
      independence caveat on the persistence argument.
- [ ] Move 2 opens with G-3 or F-2, and the player can say **why that one and not the other**
      in the language of §8.
- [ ] At least **four concessions** offered, at least one of them unprompted during the attack.
- [ ] At least **three cheap shots** named as cheap shots, with the one-line kill for each.
- [ ] Move 3's bait refused, both halves.
- [ ] The player produces the §9 Critique Sheet's ranking and can defend the ranking, not just
      the items. *Naming weaknesses is Tier 2. Ranking them is Tier 4, and Tier 4 is the bar.*
- [ ] Somewhere in the round, the player says in their own words: **"the paper's problem is not
      that its choices are wrong, it is that almost none of them are shown to be right"** — and
      can name the two pages that prove the authors knew how to show it (**p.16**, the published
      before/after decile diagnostic with a visible failure state; **p.38**, the one parameter
      justified against an external standard).

---

## 16. What this level does NOT settle

- **Whether BFRE's factors are actually data-mined.** Nothing on this page shows that. It shows
  what a search *can* do and that the paper reports no measurement of what its own search did.
  A player who says "their factors are noise" has overshot and will be shown Table 1.2.
- **The null rate for a real cross-section.** `1/20` in 7c is an assumption. Deriving it needs
  a distribution for `t` at large `df`, which this game has not built (Level 6 §15's standing
  IOU). Flag it every time.
- **Whether monthly t-statistics are independent.** Nobody knows. The paper does not check and
  neither do we; §7d says exactly how far the p.10 autocorrelations get you and no further.
- **Multiple-testing corrections themselves.** Bonferroni, false-discovery rates, family-wise
  error: none is built here, and none of the three phrases appears anywhere in `notes/`. The
  paper names the *shrinkage* literature and declines it (p.8); that is a different shelf.
- **Whether the paper's behavioural stories are true.** Reversal is justified on **p.16** by
  investors *"overreacting"* in the near term and momentum on **p.17** by investors
  *"underreacting"* over *"the previous 11 months with a one month lag"* — opposite
  psychologies at adjacent horizons, on facing pages. The attack is that they are
  **decoration**: nothing in the data could refute them and the model does not use them. A
  player who attacks momentum *itself* has misread Table 1.2 — **p.10** prints Momentum at
  **5.4%** annualised with a Sharpe of **1.43** and Reversal at **−5.1%** with **−1.59** —
  and will lose the exchange (`gm/CRITIQUE.md` E-1).
- **The six page numbers that rest on an unbroken sequence rather than a visible footer**
  (pp.40, 41, 58, 60, 62, 63). Nothing on this page cites them. If the player builds an attack
  on one, say so out loud rather than pretending to certainty.

---

## 17. Back to BFRE — what this machinery does in the real model

### 17a. Where the candidate search actually lives

**PAPER, p.10, equations (1.3)–(1.4), and p.12, (1.5)–(1.6).** The two-step recursion of §4e
*is* the paper's factor-selection procedure: fit the model so far, take the residuals, regress
each candidate on them, keep the winner, repeat. **PAPER, p.12:** it stops *"until the largest
proportion of t-statistics from the second step univariate regression is no larger than
10% - 15%."* **PAPER, p.8:** each test is judged at `|t| > 2`. **PAPER, p.10:** the candidate
count is `N ≥ 200`.

Every ingredient of Sections 4–7 is on those three pages, plus the 10% bar on p.14. What is not on them — and not on any
of the 65 — is any statement of how many candidates were tested against what null, or what the
placebo scored.

### 17b. What a mined column does to a real risk number

This is the answer to *"so what?"*, and it is Levels 9, 10 and 11 in one paragraph.

Take an equal-weighted portfolio that is long the three stocks C1 calls high and short the
three it calls low — a pure bet on the discovered factor:

```
weights  = [+1/3, +1/3, +1/3, −1/3, −1/3, −1/3]        Σw = 0
exposure to C1 = 2          exposure to the true factor z = 2/3
month 1 return = 16/3 = 5.333333% (rounded)          month 2 return = 2/3 = 0.666667% (rounded)
```

Now decompose month 1's return through the **shipped** model of §4f, which is exactly
`X f` from equation **(1.7), p.24**:

```
booked to the Random Substyle:   exposure 2    × b_C1 = 9/4   →  2 × 9/4   = 9/2 = 4.5
booked to the true factor:       exposure 2/3  × b_z  = 5/4   →  (2/3)×5/4 = 5/6 = 0.833333% (rounded)
left in the residual:                                                        0   exactly

check:  9/2 + 5/6 + 0  =  27/6 + 5/6  =  32/6  =  16/3   ✓ the portfolio's actual return
share booked to the placebo:  (9/2) ÷ (16/3)  =  27/32  =  84.375%   (exact)
```

**84.375% of this portfolio's month-1 return is booked to a column that means nothing, and
the residual — the part the model calls stock-specific — is exactly zero.** The return
decomposition is arithmetic; the *risk* decomposition follows the same exposure of 2 through
`X F Xᵀ` (Level 10), which is **INFER**: four months cannot estimate an `F`, and this file
does not try.
Trace it forward:

| Step | Where it goes | Page / equation |
|---|---|---|
| the mined column is a column of `X` | it carries an exposure for **every asset in the model** | (1.7), **p.24** |
| its factor-return series carries the search's luck | that series' variance and covariances go into `F` | (1.8), **p.24**; construction **p.27** |
| `F` is built from a daily history starting **March 1996**, and the shipped default uses **104 weeks** with a **26-week** half-life | a series that flips sign month to month (§6d) is exactly what a short half-life amplifies | **p.27** |
| the risk it *seems* to explain leaves `Δ` | specific risk is reported lower than it is | **p.27**, **p.28** |
| the report shows a factor tilt | a PM hedges an exposure that does not exist | Figure 1.18, **p.35** |

The direction is the one Level 9 taught: **common risk over-attributed, specific risk
understated.** That is **INFER** — the paper never traces this chain — but every link in it is
a printed sentence.

### 17c. And the concession that has to travel with all of it

**PAPER, p.16, Figure 1.10.** Before a small-cap factor existed, model residuals regressed on
market-cap decile dummies showed the bottom deciles above the printed 10% line; after it was
added, they fell far below. *(The bar heights are `[APPROX]` — pixel measurements, no data
labels. Cite the **crossing of the printed line**, never the numbers.)*

That is a diagnostic **with a visible failure state**: a specific way the model could be
wrong, evidence that it was, a fix, and evidence the fix worked. It is precisely what §9's
"experiment" asks for everywhere else — which makes it simultaneously the defence's best
exhibit and the attack's best proof that publishing such a thing was possible.

> **The landing sentence for the whole level.**
> *"You now know enough to notice three things at once: page 32 says the multicollinearity
> diagnostics 'were found to be well within suitable thresholds' without printing a single
> number; page 33 sends you for the actual test results to reference [27], which the
> bibliography on page 65 lists as forthcoming; and pages 5 and 6 rest the whole
> country-versus-market story on two individual trading days in August 2011. And you also know
> that page 16 and page 38 prove these authors knew exactly how to show that a choice was
> right — which is what makes the silence everywhere else a finding rather than a style."*

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level12.py     # 418 assertions, exits 0
```

The script recomputes every figure on this page from the raw `r₁`, `r₂` and `z` vectors in
`fractions.Fraction`: all four months' sums, the true misses and their balance conditions,
including that `Σz·e = 0` in every month so `b_z` lands exactly on `f`; all
twenty splits folded to ten tests and the sign-flip invariance of `t²` proved for each; the
closed-form `S`-shortcut checked against a generic Gaussian-elimination least-squares solve
for every column in months 1 and 2, with `Σx·e = 0` audited each time; both full ten-column
tables including `b`, `SSE`, `R²`, `t²` and the count clearing the bar; the winner's
decomposition into 4 borrowed and 12 lucky, its cosine and VIF; the paper's own two-step screen
run on the file; both joint fits with `det = 32`, the coefficient the truth loses, and the
placebo's sign flip between months; the permutation null enumerated over all twenty deals in
months 1 and 2; the average squared t-statistic; the four-month persistence panel — all forty
`S` values, each month's bar, which columns clear and the proportion each ends with; the
whole persistence table by exact binomial at
10 and 200 candidates; the 180-month scaling with its Markov bound and its exact tail; the
sabotage round's two cross-checks; and the portfolio attribution, including that the residual
is exactly zero and the placebo's share is exactly `27/32`.

It then does the two jobs peculiar to this level. **Citations:** every figure this page quotes
from the paper is asserted against the string recorded in `notes/`, in the correct page chunk —
p.4's `beta = 0.99` and `R2 = 91%`; p.8's threshold, its average squared t-statistic, its
15-year history, its five-year sub-samples and its stated reason for declining LASSO and the
rest; p.10's `N ≥ 200` and the six Table 1.2 cells used in §7d and §16; p.11's 0.74; p.12's
`10% - 15%`; p.14's and p.16's inclusion bar; p.16's "overreacting" and p.17's momentum
window; p.24's "In general a multi-factor model"; p.25's √-cap weights; p.26's "three intercept
terms"; p.27's 104 weeks, 26 weeks, March 1996 and the deferred BRS
document; p.28's "in-line with standard modelling practice";
pp.5-6's two August 2011 trading days; p.30's single "Out-of-sample" and its 1-month forecast
horizon; p.32's "well within suitable thresholds", "exhaustive
set", "majority", its `R²` definition, its "significant instability" sentence and its
"1996 to 2013" span; p.33's "available on request"; p.35's "Active Risk"; p.38's 99%/252-day
VaR, Kupiec, the 12-month bias window, the 95% band and STORM; p.47's `s ≤ t`; p.55's
`200+`; p.56's Random Substyle and its 18/108 row counts; and p.65's "forthcoming" — plus a
check that nine phrases that must never be attributed to this paper (Bonferroni, family-wise,
false discovery rate, eigenvalue, principal component, tracking error, least squares, normal
equation, degrees of freedom) appear nowhere in `notes/` at all. **Counts:** the 40
weaknesses, 12 cheap shots, 12 concessions, 6 grey-zone items, 20 scoreboard rows with their
star ratings, 5 automatic-fail conditions and the 7 terms this level unlocks are all
recomputed from `gm/CRITIQUE.md` and asserted against the numbers printed in §10 and §13 of
this file.

If any printed value ever disagrees with this markdown, the markdown is wrong.
