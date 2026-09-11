# Level 9 — The Private Drama

Every number below is recomputed in exact rational arithmetic by `tools/verify_level9.py`
(273 assertions plus 2,401 swept books, exits 0). Nothing here is rounded by hand. Where a
decimal does not terminate it is written with the word **rounded** next to it; every other
decimal on this page is exact. Every square root on this page sits on top of an **exact**
variance, and the root itself is printed as an explicitly-rounded decimal.

> **DIFFICULTY WARNING, and a framing warning that matters more.**
>
> **Difficulty.** Two things on this page are above 12th-standard:
> - **Section 5** — the argument that the fit's own balance condition makes an exactly
>   diagonal specific covariance matrix *impossible*, and that the impossibility is worth
>   `−1/(N−1)` at equal weights and therefore does not matter. That is a graduate-level observation about
>   least-squares residuals. It is built here from one line of algebra and then checked on a
>   file the player already owns.
> - **Newey–West** (p.27, p.28). Serial-correlation-robust aggregation is a graduate
>   econometrics topic. It is **named** on this page and **not built**. Say so out loud.
>
> Everything else is ordinary algebra done carefully.
>
> **Framing — read this before you open the level, because getting it wrong costs the player
> Level 12.** This is the sharpest honest-limitation level in the game, and it is *not* a
> gotcha. Page 24 introduces `Δ` as "a diagonal matrix" under the lead-in **"In general a
> multi-factor model decomposes asset returns as follows"** — that is the *textbook* form.
> Page 27 then says what BFRE actually ships, and it is **not** diagonal. Page 28 gives the
> whole subject its own subsection, with examples, two named methodologies, and the direction
> of the error stated in the paper's own words. `gm/CRITIQUE.md` **CS-3** files
> *"(1.8) says diagonal but p.27 says otherwise"* as a **named cheap shot** — a rival who
> leads with it loses the room. The real, narrow, defensible criticism is about **scope**:
> the off-diagonals BFRE keeps are only ever *within one company*, and across companies the
> correlations are "assumed to be zero **in-line with standard modelling practice**" (p.28).
> That is the boss round. Teach the distinction the level is actually for — **what the
> arithmetic guarantees versus what the modeller assumes** — and hand the player the cheap
> shot only so they can refuse it.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the miss, and why it is scored by its size and not its sign.
**From Level 2** — the balance condition `Σx·u = 0`, forced by the arithmetic of minimising,
and the difference between *a balance the arithmetic gives you free* and *a balance a human
imposes by hand* (equation (1.10), p.26). Level 2's landing sentence promised that "Level 9 is
entirely that distinction." This is that level.
**From Level 3** — two columns, two balance conditions, one solve.
**From Level 5** — centering, and a column of ones being an intercept.
**From Level 6** — the divisor question, and the fact that a choice of divisor has to be
declared rather than assumed.
**From Level 7** — the same cross-section run month after month.
**From Level 8** — a grid built out of sums of products; `hᵀFh` derived by expanding a square;
positive semi-definiteness ("no book has negative variance"); the counting argument that a
matrix with more entries than you have numbers is *structurally* broken, not merely imprecise.
Level 8 also said, of the misses it left lying on the desk: *"Those five columns of misses
total `Σu² = 46` across the file, and they are Level 9's raw material, not this level's."*

Here they are.

Level 9 asks the question none of those levels can answer:

> Level 8 built the grid for the **factors**. Every asset also has a leftover — the part no
> factor reached. Those leftovers have sizes, and the sizes go somewhere. **Where?** And once
> you have written down each asset's leftover size, what have you *assumed* about how one
> asset's leftover relates to another's — and did you notice yourself assuming it?

Four genuinely new things:

| | What Level 9 adds |
|---|---|
| **A second matrix** | `Δ`. Section 4 builds its diagonal out of Level 8's own leftovers. It is the other half of the risk model, and it is the half the paper is most careful about. |
| **A clean split: guaranteed vs assumed** | Section 3 lists exactly what least squares forces (and it forces a lot), and Section 3d lists three things it conspicuously does *not* force — each one checked, on the file, and each one non-zero. |
| **An off-diagonal that is real** | Section 6 builds a file where two names share a shock the factor model has no column for. The link is not noise: Section 6c shows the shock itself. |
| **The asymmetry** | Section 8. The same modelling error costs **64.58 bps** *(rounded)* on the book a manager would actually hold and **0.60 bps** *(rounded)* on a wide one — a factor of **108.3** *(rounded)*, from one identical mistake. That asymmetry *is* the lesson. |

**Names deliberately withheld until Section 12.** Do not say *specific risk*, *specific risk
matrix*, *diagonal*, *specific return correlation*, *structural* or *empirical approach*,
*sparse*, or *second moment* at the table before the player has built the mechanism. Before
then, say: *the leftover*, *the size of the leftover*, *the grid of leftovers*, *the list with
nothing off the middle line*, *two names whose leftovers move together*.
(`gm/VOCAB.md` row 4 sets these unlocks at L9. Three neighbours are **not** yours, and their
owners are not all where a first guess puts them: the **asset** covariance matrix `Σ` is Level
10's (`gm/LEVEL_ANCHORS.md` jargon ledger — VOCAB row 10's *"covariance matrix"* was already
spent at L8 on `F`); *Active Risk* and *tracking error* are **Level 10's**, handed over in
`datasets/level10.md` §12 and drilled again at L11 (VOCAB row 13: "L10 … used at L11"); only
*marginal contribution* is Level 11's own (VOCAB row 14).)

---

## 1. The story — no mathematics

A small insurer writes fire policies on the shops of one town. Four hundred shops, four hundred
policies. The actuary works out, for each shop, how likely a fire is and how big it would be:
a chip-pan here, old wiring there, a shop with a sprinkler system and one without. Every one
of those four hundred numbers is carefully done and, taken one at a time, every one of them is
right.

Then he adds them up to get the swing in next year's claims, and he gets a small number. That
is not a mistake either — it is the whole reason insurance works. Fires do not co-ordinate.
One shop burning tells you nothing about the shop across the road, so four hundred small
independent accidents average out into something almost predictable.

Two things spoil it, and neither is a wrong number.

The first is easy to see once it is pointed out. Policy 118 and policy 119 are the same
building: the shopfront on the high street and the storeroom behind it, insured separately
under two names because the paperwork came from two different agents. When that building
burns, two claims arrive. The actuary has not made an arithmetic error; he has counted one
accident twice as if it were two.

The second is the one nobody has written down anywhere. The Nayar bakery on Mill Street and
the Nayar flour mill two streets over are separate businesses with separate accounts and
separate policies — and one ancient diesel generator behind the mill that powers both. It has
been rewired four times. When it goes, both go. Nothing in the insurer's files connects them,
because nothing in the insurer's files is *about* families or generators. The file has a
column for sprinklers and a column for wiring age. It does not have a column for *this*.

Now the part that decides how much any of this matters.

Across the whole four-hundred-shop book, the mistake is nearly invisible. There are seventy-nine
thousand eight hundred pairs of shops on that book and exactly two of them are linked. Add up
the claims and the two extra co-arrivals disappear into the noise of four hundred.

But the insurer also writes one special policy. A landlord owns exactly two properties: the
Nayar bakery and the Nayar flour mill. Nothing else. On *that* policy the mistake is not a
rounding error — it is the entire answer. The actuary's number for it says "two independent
small risks, which mostly cancel." The truth is "one generator."

And here is the twist that makes it a *risk* problem rather than an arithmetic problem:
**nobody will ever find the error by checking the sums.** Every number in the file is right.
The error is in a step that was never written down — the step where separate policies were
treated as separate accidents. It shows up not as a discrepancy but as a claim, once, on the
one policy where it was fatal.

---

## 2. Mapping the story onto the model, line by line

Go down this table row by row. Do not skip a row because it looks obvious; the skipped row is
where the misconception lives.

| In the story | In the model |
|---|---|
| a shop | an asset |
| this year's fire at that shop | that asset's leftover for that period — `u` in (1.7), p.24 |
| "how bad a fire could that shop have" | the size of that asset's leftover: one number per asset |
| the actuary's list of four hundred such numbers | **the diagonal of `Δ`** — Section 4 |
| the columns the file *does* have (sprinklers, wiring) | the columns of `X` — the factors |
| "fires do not co-ordinate" | the assumption that different assets' leftovers are unrelated |
| policy 118 and 119 being one building | **a cross-listing or an ADR and its root** — p.28, and BFRE **does** model it |
| the Nayar generator | a shared shock with **no column in `X`** and **no company in common** — p.28 assumes this to zero |
| the four-hundred-shop book | a diversified portfolio — Book W, Section 8d |
| the landlord's two-property policy | a concentrated portfolio — Book P, Section 8a |
| "every number in the file is right" | the diagonal is estimated correctly; the *assumption* is what is wrong |
| nobody finds it by checking sums | there is **no internal consistency check** that catches a missing off-diagonal |

**Where the story breaks — deploy this at tier 4, not at first telling.** In insurance the
underwriter can, in principle, go and *look*: walk to Mill Street and see the generator. A
risk model cannot. Its leftovers are defined as "whatever the columns did not reach", so the
only evidence that two leftovers are linked is the leftovers themselves — and Section 14.4
shows there are nowhere near enough of them to test every pair. The insurer's problem is
laziness. The model's problem is arithmetic.

---

## 3. The guarantee — what least squares cannot help doing

### 3a. Level 8's file, unchanged

Five names, two columns — a column of ones (the market factor: p.4, PAPER, "all equity assets
have a **unit exposure** to this factor") and a centred cheapness column.

| Stock | market `1` | cheapness `x` |
|---|---:|---:|
| AXL | 1 | −2 |
| BRN | 1 | −1 |
| CHR | 1 | 0 |
| DLT | 1 | +1 |
| EMK | 1 | +2 |

```
Σ1·1 = 5        Σ1·x = 0        Σx·x = 10        det = 5 × 10 − 0 × 0 = 50
```

Five months of returns, in percent, exactly as Level 8 printed them:

| Stock | month 1 | month 2 | month 3 | month 4 | month 5 |
|---|---:|---:|---:|---:|---:|
| AXL | 0 | −3 | +6 | +6 | −8 |
| BRN | +1 | +2 | +3 | +7 | −6 |
| CHR | +9 | +3 | −1 | +1 | −8 |
| DLT | +9 | +10 | −1 | +3 | −4 |
| EMK | +16 | +13 | −2 | −2 | −4 |

```
f_Mkt = +7, +5, +1, +3, −6        f_Chp = +4, +4, −2, −2, +1
```

### 3b. The misses, and the two balances that hold in every single month

| month | `u` for AXL…EMK | `Σu` | `Σx·u` | `Σu²` |
|---|---|---:|---:|---:|
| 1 | +1, −2, +2, −2, +1 | **0** | **0** | 14 |
| 2 | 0, +1, −2, +1, 0 | **0** | **0** | 6 |
| 3 | +1, 0, −2, 0, +1 | **0** | **0** | 6 |
| 4 | −1, +2, −2, +2, −1 | **0** | **0** | 14 |
| 5 | 0, +1, −2, +1, 0 | **0** | **0** | 6 |

`Σu² = 46` across the file — the number Level 8 handed over.

### 3c. Why those zeros are a guarantee and not a result (CALL BACK to Level 2)

The player proved this at Level 2 and it has not changed. Take any column `x` of `X` and nudge
its coefficient by a hair `h`. The sum of squared misses becomes

```
SS(f + h)  =  Σ(u − h·x)²  =  Σu²  −  2h·Σx·u  +  h²·Σx²
```

If `Σx·u` were anything other than zero, a small nudge in the right direction would lower
`SS` — because the `−2h·Σx·u` term is **linear** in `h` and the `h²` term is not, so for small
enough `h` the linear term wins. So at the minimum, `Σx·u = 0`. Not approximately. Exactly.
For **every** column, in **every** period, on **every** dataset, whatever the data are.

**This is bedrock.** It is not a property of these numbers, not a modelling assumption, and not
something BFRE chose. It is what "best fit" *means*. Say the word **guarantee** and hold the
player to it — the rest of the level turns on the contrast.

Two riders, both important:

- The first column here is a column of **ones**, so its balance condition reads `Σ_i u_i = 0`:
  *in every single month, the five leftovers add to exactly nothing.* That is Level 5's
  intercept doing its work.
- BFRE does not run an unweighted regression. Assets are weighted by the **square root of
  market capitalisation** (p.25, PAPER). So what the real fit forces is `Σ_i ω_i x_i u_i = 0`
  — orthogonality in the **weighted** sense, with `ω` the regression weights. `Σ_i x_i u_i` on
  its own is generally *not* zero in BFRE. A player who says "sum of exposure times specific
  return is zero" without the weights has said something false about the shipped model; this
  is a tier-5 marker and worth drilling.

### 3d. What the guarantee does **not** say — three checks, all on this file, all non-zero

This is the section the level exists for. Each row is a thing people assume the fit gave them.
It did not.

| The claim | What it would need | What this file actually gives |
|---|---|---|
| "Each asset's leftovers average to zero over time" | `Σ_t u_i(t) = 0` for each `i` | **CHR: `−6`.** AXL: `+1`. Not zero. |
| "Factor returns and leftovers are uncorrelated" | `Σ_t f(t)·u_i(t) = 0` | **`Σ_t f_Chp·u_CHR = +6`**, and `Σ_t f_Mkt·u_CHR = +8`. Centred, `Cov(f_Chp, u_CHR) = 12/5 = 2.4` exactly. Not zero. |
| "Different assets' leftovers are unrelated" | `Σ_t u_i(t)·u_j(t) = 0` for `i ≠ j` | **`Σ_t u_BRN·u_DLT = 10`**, which is as large as `Σ_t u_BRN²` itself. Not zero. |

Row 1 is why Section 4a has to declare a divisor rather than assume one.

Row 2 is worth stopping on, because **the paper assumes exactly this**, in as many words, and
lists it as an assumption rather than a result. p.30, PAPER, from the *Model Assumptions &
Limitations* bullet list:

> "Factor returns have **zero correlation** with asset specific returns, and specific returns
> from different issuers are **unrelated and have zero correlation**"

The cross-sectional fit forces `Σ_i ω_i x_i u_i = 0` **inside one period**. That is a statement
about a column of `X` and a column of leftovers, added across *assets*. p.30's bullet is a
statement about a **factor return series** and a **leftover series**, added across *time*.
Different sums, different indices, different objects. Nothing in the fitting procedure delivers
the second one, and this file shows it coming out at `+6` on our own numbers.
**[INFER — this connection is ours. The paper states the assumption and never links it to the
estimation procedure.]**

Row 3 is the rest of this level.

---

## 4. Building the leftover sizes — the diagonal of `Δ`

### 4a. The divisor, declared before it is used (CALL BACK to Level 6 and Level 8)

Level 8 had to choose between dividing by `T` and dividing by `T − 1` when it built the factor
grid, and had to declare the choice because **the paper does not state one**. The same silence applies here, and the
choice this level makes is different, on purpose:

```
d_i  =  ( Σ_t u_i(t)² ) / T          ← no mean subtracted, divide by T
```

Three reasons, said out loud:

1. **A leftover has no business having a mean.** The model's own claim (p.24, PAPER) is that
   `u` is "return associated with stock-specific events" — news, not drift. Subtracting a
   sample mean would be subtracting an estimate of a quantity the model asserts is zero, and
   you would be throwing away real leftover size to do it.
2. **What we want is a forecast of size, not of spread about a five-month average.** `Δ` is a
   forecast of how big the leftovers will be, and "big" is measured from zero.
3. **It is honest about the file.** Section 3d row 1 showed CHR's leftovers averaging `−6/5`
   over five months. On the second-moment convention that `−6/5` counts as risk, which is what
   we want, because next month is not obliged to repeat it.

**And here is the check that stops this being a fudge — and the exact place where the check
stops.** Two separate choices are hiding inside `d`, and **only one of them is harmless.** Do not
let them be run together; a player who merges them has a false guarantee in their pocket.

*The divisor is harmless.* Keep the second moment and divide by `T − 1 = 4` instead of `T = 5`.
Every entry is multiplied by the **same** factor `5/4` — `d_CHR` becomes `5` instead of `4`,
`d_BRN` becomes `5/2` instead of `2`, and so on down the column. A common factor cancels out of
every ratio, so **no ratio on this page moves**: `d_CHR / d_BRN = 2` either way. When the CRO
attacks the **divisor** in the boss round, that is the answer, and it is exact.

*The centring is not harmless, and we do not pretend otherwise.* Subtract each row's own
five-month average first — `Σ_t (u_i − ū_i)² / (T − 1)`, the full sample-variance convention —
and the rows stop scaling together, because **each row has a different mean**:

| Stock | `ū` | `Σ(u − ū)² = Σu² − T·ū²` | centred `d`, divisor `4` | our `d` |
|---|---:|---:|---:|---:|
| AXL | 1/5 | 3 − 1/5 = 14/5 | **7/10 = 0.7** | 3/5 = 0.6 |
| BRN | 2/5 | 10 − 4/5 = 46/5 | **23/10 = 2.3** | 2 |
| CHR | −6/5 | 20 − 36/5 = 64/5 | **16/5 = 3.2** | 4 |
| DLT | 2/5 | 10 − 4/5 = 46/5 | **23/10 = 2.3** | 2 |
| EMK | 1/5 | 3 − 1/5 = 14/5 | **7/10 = 0.7** | 3/5 = 0.6 |

`d_CHR / d_BRN` moves from `2` to `32/23 = 1.391304` *(rounded)*. CHR is the row that loses most,
and it loses it for precisely the reason **1** above gives: CHR's `−6/5` average *is* leftover
size on our convention, and centring throws that size away. (Note the centred column is *not*
uniformly smaller either — AXL and BRN go **up**, CHR goes **down**. That is the giveaway that no
common factor is available.)

**So the honest boss-round answer is two sentences, not one:** the divisor changes nothing that
matters, and the centring does — which is why the choice not to centre is declared on the record,
above, with its reason, rather than smuggled in under the divisor.

BFRE's own words on this, p.27, PAPER — note what they do and do not settle:

> "Specific risk forecasts are primarily estimated using a **time-series of specific returns**.
> Specific returns are calculated using local asset excess returns, factor exposures and
> (estimated) factor returns, and are then **cleansed using robust methods** to down-weight the
> influence of outlying observations."

A time series of leftovers, cleaned, then turned into a size. Which size, with which divisor,
around which centre: not stated.

### 4b. The five numbers

Take the five columns of misses from 3b and square them along each **row**:

| Stock | `u` across the five months | `Σ_t u²` | `d = Σu²/5` | leftover size `√d` |
|---|---|---:|---:|---:|
| AXL | +1, 0, +1, −1, 0 | 3 | **3/5 = 0.6** | 0.7746% *(rounded)* |
| BRN | −2, +1, 0, +2, +1 | 10 | **2** | 1.4142% *(rounded)* |
| CHR | +2, −2, −2, −2, −2 | 20 | **4** | **2.0000%** *(exact)* |
| DLT | −2, +1, 0, +2, +1 | 10 | **2** | 1.4142% *(rounded)* |
| EMK | +1, 0, +1, −1, 0 | 3 | **3/5 = 0.6** | 0.7746% *(rounded)* |

```
Σ d_i = 46/5 = 9.2       ← the file's Σu² = 46, divided by T = 5
```

CHR's `2.0000%` is exact because 4 is a perfect square; the other four are irrational and are
marked rounded. **CHR alone supplies `4 / (46/5) = 10/23 = 0.434783` (rounded) — just over
43% — of the whole file's leftover variance.** That is the same CHR that Level 0 introduced as
the stock no `b` can predict and Level 6 showed has zero leverage on `b`. Its exposure is
`x = 0`, so no column reaches it, so everything it does lands here. **CHR is what `Δ` is for.**

### 4c. What BFRE actually does instead — five simplifications, declared

Everything above is the shape of the calculation. BFRE's version has five more moving parts,
and every one is on p.27 or p.28. Declare them before a player mistakes our five numbers for
the model.

| Our toy | BFRE | Where |
|---|---|---|
| 5 equally-weighted monthly leftovers | **exponential decay**, half-life **125 days** over **375** daily observations (daily models); **26 weeks** over **104 weeks** (WRLD and EMKT) | Table 1.3, **p.28** — verified digit for digit |
| raw leftovers | "**cleansed using robust methods** to down-weight the influence of outlying observations" | p.27 |
| no serial-correlation adjustment | the **Newey–West [26]** methodology, "used to aggregate daily specific returns to form specific risk forecasts that account for serial correlations in the daily data", lag **10 days** daily / **2 weeks** weekly | p.27, Table 1.3 p.28 |
| every asset has five months of history | assets with little or no history (IPOs) get a **cross-sectional overlay** inferred from assets of "similar market capitalisation, in the same industry and country", blended as "a **weighted sum** of its time-series forecast (if it exists) and its cross-sectional forecast … In the limit this weight is set to **1**" | p.28 |
| our horizon is "one month, because the returns are monthly" | "The forecast horizon of the model is **1-month** … Risk estimates are computed at a 1-month horizon taking into account **daily serial correlations** in factor returns and asset specific returns" | p.30 |

**Say the difficulty out loud on row 3.** Newey–West is graduate econometrics. It is named here
and **not built**, and the player should know they have an IOU rather than a gap in their
understanding. Note also the shape of it: **375 daily observations with a 125-day half-life**
is a much gentler decay than the factor grid's 104 weeks at a 26-week half-life — Level 8
computed the effective sample sizes as ≈281 of 375 against ≈66 of 104. BFRE is more willing to
use old data for leftover sizes than for factor co-movement, and the paper does not say why.

**One thing the paper does *not* leave vague, and it is the whole next section.** p.27, PAPER,
first sentence of the *Specific Covariance Matrix* subsection:

> "The asset specific covariance matrix is made up of **two** components: a vector of asset
> specific risk forecasts **and a sparsely populated unit diagonal matrix containing non-zero,
> off-diagonal specific return correlations.**"

A list of sizes, **and** some off-diagonal entries. Hold that until Section 9.

---

## 5. The guarantee that forbids a perfect diagonal — and why BFRE is right to ignore it

> **This section is graduate-level and is the game's argument, not BlackRock's.** Nothing on
> these lines appears in the paper. Say so before you start and again at the end.

### 5a. Fill in the whole grid, not just the middle line

Nothing stops us computing `Δ_ij = (Σ_t u_i(t)·u_j(t))/T` for every pair, not just `i = j`.
Do it on the Level-8 file (`T = 5`):

|  | AXL | BRN | CHR | DLT | EMK | **row sum** |
|---|---:|---:|---:|---:|---:|---:|
| **AXL** | 3/5 | −4/5 | 2/5 | −4/5 | 3/5 | **0** |
| **BRN** | −4/5 | 2 | −12/5 | 2 | −4/5 | **0** |
| **CHR** | 2/5 | −12/5 | 4 | −12/5 | 2/5 | **0** |
| **DLT** | −4/5 | 2 | −12/5 | 2 | −4/5 | **0** |
| **EMK** | 3/5 | −4/5 | 2/5 | −4/5 | 3/5 | **0** |

**Every row sums to exactly zero.** That is not luck. In every month `Σ_i u_i(t) = 0` — the
market column's balance condition, Section 3c — so for any asset `i`,

```
Σ_j Δ_ij  =  (1/T) Σ_t u_i(t) · ( Σ_j u_j(t) )  =  (1/T) Σ_t u_i(t) · 0  =  0
```

and adding those `N` zeros gives the whole-matrix version:

```
Σ_i d_i  +  Σ_{i≠j} Δ_ij  =  0        so       Σ_{i≠j} Δ_ij  =  − Σ_i d_i
```

On this file: the off-diagonals sum to **−46/5**, which is exactly minus the sum of the
diagonal. The average off-diagonal entry is `−(46/5)/20 = −23/50 = −0.46` exactly.

**The off-diagonals cannot all be zero.** A perfectly diagonal `Δ` would need
`Σ_i d_i = 0`, which needs every leftover to be zero, which means a perfect fit. So a model
with an intercept column *guarantees* that its leftovers are slightly negatively related, and
then *assumes* they are not. *(That conclusion holds weighted or unweighted; only its **size**
depends on the weights — see the rider at the end of 5c before you quote a number.)*

### 5b. Watch it bite: a book the diagonal model charges for nothing

Take the equal-weight book, 20% in each of the five names. Its leftover, month by month, is
`(1/5)·Σ_i u_i(t)` — which the balance condition makes **exactly zero in all five months**:

```
book leftover:   0,  0,  0,  0,  0
```

Its true leftover variance is therefore exactly **0**. And the diagonal-only version says:

```
Σ w_i² d_i  =  (1/25)(0.6 + 2 + 4 + 2 + 0.6)  =  9.2/25  =  46/125  =  0.368     (exact)
risk  =  √0.368  =  0.6066%     (rounded)
```

**The diagonal model charges 0.6066% (rounded) of leftover risk to a book that has provably
never had any.** Note the direction: here the diagonal model runs **too high**, not too low. Hold onto
that — the boss round runs the other way, and a player who thinks the diagonal assumption has
one signed direction has not understood it (Section 8f).

### 5c. And now the reason it does not matter

Suppose all `N` assets had the same leftover size `d` and the same average off-diagonal
correlation `ρ̄`. The identity says `N·d + N(N−1)·ρ̄·d = 0`, so

```
        ┌────────────────────┐
        │   ρ̄  =  −1/(N−1)   │
        └────────────────────┘
```

| `N` | `ρ̄` |
|---:|---:|
| 5 (this toy) | **−0.250000** *(exact)* |
| 50 | −0.020408 *(rounded)* |
| 749 | −0.001337 *(rounded)* |
| 3,000 | −0.000333 *(rounded)* |

*(`749` is not a number picked for effect: it is the break-even universe size **derived in Section
14.4** from the paper's own 375 observations. It sits in this table so the two arguments can be
read at the same `N`. `3,000` is ours, chosen to be obviously large — 14.4 says so again.)*

**One rider, because Section 3c already earned it.** `−1/(N−1)` is the **equal-weight** value. BFRE
weights the regression by `√`market cap, so what its intercept actually forces is
`Σ_i ω_i u_i(t) = 0`, and the identity becomes `Σ_i ω_i² d_i = − Σ_{i≠j} ω_i ω_j Δ_ij`. The
*conclusion* survives untouched — the left-hand side is a sum of positive things, so the
off-diagonals still cannot all be zero — but the **size** `−1/(N−1)` is this toy's, not the shipped
model's. Say the conclusion at the table; never quote the number as BFRE's.
**[INFER — the weighted version is ours. The paper writes no balance condition of any kind
(Section 16i), so it writes neither of these.]**

At five assets the mechanical link is a quarter, which is enormous. At three thousand assets it
is `−0.000333` (rounded), about three parts in ten thousand. **The exact-diagonal assumption is
false for a reason that gets small like `1/N`, and BFRE's estimation universes are not small.**
The paper never prints the size of one — but it says the universe is built "on a
country-by-country basis every month" (p.24, PAPER) out of "representative assets from each
market" (p.25, PAPER), and that asset coverage spans **87 countries** (p.3, PAPER).

This is the single best example in the game of a criticism that
is *technically correct and practically worthless*, and a player who cannot tell those apart
will embarrass themselves at Level 12. Make them say the sentence: *"true, negligible, and not
the problem."*

### 5d. Two artifacts in this file, named so they are never mistaken for economics

Look again at the grid. `Δ_BRN,DLT = 2`, which is the same as `d_BRN` and `d_DLT` — a
correlation of **exactly 1**. Same for AXL and EMK. Two pairs of names in a five-name file with
perfectly correlated leftovers, and it means nothing:

- **BRN and DLT have literally identical miss series** (`−2, +1, 0, +2, +1`), and so do AXL and
  EMK. That is a symmetry the Level-8 returns happened to have, not a fact about companies.
- With 5 assets and 2 columns, the misses in any month have only **3** free directions — and
  the five months this file actually delivered used only **2** of them. Month 4's misses are
  exactly minus month 1's; month 5's are exactly month 2's; and month 3's are month 1's plus
  twice month 2's. Five months, two independent patterns.

If a player points at this and says "look, correlated leftovers!" — pay them for noticing, then
dock the conclusion. This is why Section 6 builds a *new* file, where the link is put there on
purpose by a mechanism you can see.

---

## 6. The new file — where the correlation is real

### 6a. Four names, and the reason each is there

New names, because the old five have no relationships to have. These four are **four rows
lifted out of a large estimation universe**, not a universe of their own — which matters,
because Section 5's balance condition binds on the *whole* universe, not on any four rows of
it. Nothing in Section 5 constrains this file.

| Ticker | What it is | Why it is here |
|---|---|---|
| **KVR** | Kaveri Castings — a components maker | one half of the link |
| **TLM** | Talmar Motors — the vehicle assembler that is KVR's only customer | the other half. **A different company.** |
| **GNP** | Ganpat Foods | a control: linked to nothing |
| **HRB** | Harbour Logistics | a second control |

KVR and TLM are in different industries, different size bands, different everything the model
has a column for. A factor model built out of industry, country and style columns has **no
column for "Talmar's order book"** — and when Talmar cuts production, both stocks move for a
reason none of the columns can reach. So it lands in the leftovers. Of both of them.

**This is the case p.28 assumes to zero, in as many words** (PAPER):

> "Note that specific return correlations are **only estimated between assets in the same
> company**. Specific return correlations between assets **in different companies** are
> **assumed to be zero** in-line with standard modelling practice."

### 6b. The panel

Six months of leftovers, in percent. (`T = 6`.)

| | month 1 | month 2 | month 3 | month 4 | month 5 | month 6 | `Σu` | `Σu²` | `d = Σu²/6` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **KVR** | +5 | −1 | −1 | −4 | +2 | −1 | 0 | 48 | **8** |
| **TLM** | +4 | −2 | −4 | −2 | +2 | +2 | 0 | 48 | **8** |
| **GNP** | +3 | +3 | −3 | +3 | −3 | −3 | 0 | 54 | **9** |
| **HRB** | 0 | −3 | 0 | +3 | +3 | −3 | 0 | 36 | **6** |

Leftover sizes: KVR **2.8284%** *(rounded)*, TLM **2.8284%** *(rounded)*, GNP **3.0000%**
*(exact — 9 is a perfect square)*, HRB **2.4495%** *(rounded)*.

The four sample means are zero, deliberately, so that the divisor argument of 4a cannot muddy
anything below. That is a convenience of ours, not a property of leftovers.

### 6c. Where the numbers came from — a shock with no factor

The panel is not arbitrary. KVR's and TLM's rows are each **a shared shock plus a private
part**:

```
g    =  +3,   0,  −3,  −3,  +3,   0        ← the order-book shock. No column of X reaches it.
p_K  =  +2,  −1,  +2,  −1,  −1,  −1        ← KVR's own news
p_T  =  +1,  −2,  −1,  +1,  −1,  +2        ← TLM's own news

KVR  =  g + p_K  =  +5,  −1,  −1,  −4,  +2,  −1        ✓ matches the table
TLM  =  g + p_T  =  +4,  −2,  −4,  −2,  +2,  +2        ✓ matches the table
```

The three pieces are mutually orthogonal — `Σ g·p_K = 0`, `Σ g·p_T = 0`, `Σ p_K·p_T = 0` — so
their sizes simply add:

```
Var(g)   = 36/6 = 6            Var(p_K) = 12/6 = 2            Var(p_T) = 12/6 = 2
d_KVR    = 6 + 2 = 8           d_TLM    = 6 + 2 = 8
Δ_KVR,TLM = Var(g)  =  6       ← the shared piece, and nothing else
```

**Round type C (build the shape first).** Before showing this, ask: *"if two stocks' leftovers
are 'one shared shock plus one private shock each', and the shared shock has size 6 while each
private one has size 2, what should the cross-entry be?"* The answer has to be **6** — the
private parts have nothing to do with each other, so all that can survive the cross-product is
the shared piece. A player who says "somewhere between 0 and 8" has not yet seen why it is
exactly the shared variance.

### 6d. The grid

`Δ_ij = (Σ_t u_i(t)·u_j(t))/6`, all six off-diagonal cross-products computed by hand:

```
Σ KVR·TLM = 20 + 2 + 4 + 8 + 4 − 2 = 36    →  Δ = 6
Σ KVR·GNP = 15 − 3 + 3 − 12 − 6 + 3 =  0   →  Δ = 0
Σ KVR·HRB =  0 + 3 + 0 − 12 + 6 + 3 =  0   →  Δ = 0
Σ TLM·GNP = 12 − 6 + 12 − 6 − 6 − 6 =  0   →  Δ = 0
Σ TLM·HRB =  0 + 6 + 0 −  6 + 6 − 6 =  0   →  Δ = 0
Σ GNP·HRB =  0 − 9 + 0 +  9 − 9 + 9 =  0   →  Δ = 0
```

|  | KVR | TLM | GNP | HRB |
|---|---:|---:|---:|---:|
| **KVR** | **8** | **6** | 0 | 0 |
| **TLM** | **6** | **8** | 0 | 0 |
| **GNP** | 0 | 0 | **9** | 0 |
| **HRB** | 0 | 0 | 0 | **6** |

One correlation in the whole file:

```
ρ(KVR,TLM)²  =  6² / (8 × 8)  =  9/16          so   ρ  =  6/8  =  3/4   exactly
```

and the 2×2 block's determinant is `8×8 − 6×6 = 28 > 0`, so nothing here can hand a book a
negative variance (Level 8's health check, run without being asked).

Two matrices to compare from here on. Nothing else changes:

```
Δ_full  =  the grid above                    Δ_diag  =  the same grid with the 6s deleted
```

`Δ_diag` is what a model that assumes *"leftovers of different assets are unrelated"* writes
down. Every number on its middle line is **correct**. That is the point of Section 1.

---

## 7. From a grid to one number

### 7a. Build the shape before seeing it (round type C)

*"You have four leftover sizes and one link. You have a book with a weight on each name. You
want one number, in percent, for how much the book's leftovers wobble. What must the formula
look like?"*

Force the answer out of units and out of Level 8. Variances add; volatilities do not (Level 8's
first trap). Weights are pure numbers, sizes are percent-squared, so weights must enter
**squared** on the diagonal. And two names that move together must contribute a term involving
**both** weights.

### 7b. The derivation — one line, and it is Level 8's line again

The book's leftover in month `t` is just the weighted sum of the names' leftovers:

```
u_p(t)  =  Σ_i w_i · u_i(t)
```

Square it and average over the six months, exactly as Level 8 did for `hᵀFh`:

```
(1/T) Σ_t u_p(t)²  =  (1/T) Σ_t ( Σ_i w_i u_i(t) )( Σ_j w_j u_j(t) )
                   =  Σ_i Σ_j w_i w_j · (1/T) Σ_t u_i(t) u_j(t)
                   =  Σ_i Σ_j w_i w_j Δ_ij
```

so

```
        ┌───────────────────────────────────────────────────────┐
        │   book leftover variance  =  wᵀ Δ w                    │
        │       =  Σ_i w_i² d_i   +   2 Σ_{i<j} w_i w_j Δ_ij     │
        └───────────────────────────────────────────────────────┘
```

That is the whole of it. **It is not a new object; it is bookkeeping for a sum you could do by
hand**, and the next section proves it by doing both.

### 7c. The proof that the matrix is only bookkeeping

For each book below, the verifier builds the book's own six-month leftover series and takes its
second moment directly — **no matrix at all** — and gets the same number as `wᵀΔ_full w`:

| Book | its own leftover series, months 1–6 | direct second moment | `wᵀΔ_full w` |
|---|---|---:|---:|
| **P** 50% KVR + 50% TLM | +9/2, −3/2, −5/2, −3, +2, +1/2 | **7** | **7** |
| **H** +50% KVR − 50% TLM | +1/2, +1/2, +3/2, −1, 0, −3/2 | **1** | **1** |
| **A** 25% each of four | +3, −3/4, −2, 0, +1, −5/4 | **43/16** | **43/16** |

And now the sentence that makes the level land:

> **`Δ_diag`'s numbers cannot be reproduced this way at all.** Book P's own leftover series is
> the six numbers in the table above, and its sum of squares is `42`, so its second moment is
> `42/6 = 7`. There is no arithmetic anywhere in this file that produces `4` from those six
> numbers. The diagonal model's answer for Book P is not a summary of something that happened;
> it is a statement about a world in which KVR's and TLM's news arrive independently — a world
> this file is not from.

---

## 8. Four books, two numbers each

All four use the same `Δ`, correct on its diagonal, with one entry either kept or deleted.

### 8a. Book P — the pair trade. 50% KVR, 50% TLM

```
diagonal part :  (1/2)²·8  +  (1/2)²·8   =   2 + 2   =   4
cross term    :  2 · (1/2) · (1/2) · 6   =   3

wᵀΔ_diag w  =  4          risk  =  √4  =  2.0000%        (exact)
wᵀΔ_full w  =  4 + 3 = 7  risk  =  √7  =  2.6458%        (rounded)
```

```
variance ratio  7/4       exactly
risk ratio      √7/2  =  1.322876      (rounded)
the model reports  2/√7  =  0.755929   (rounded)  of the truth
risk missing:  √7 − 2  =  0.645751 pp  =  64.58 bps       (rounded)
```

**The diagonal model files this book at 2.0000% when it is 2.6458%** *(rounded)*. It has thrown away
`3/7 = 0.428571` (rounded) of the variance — three-sevenths of it — and every number it used
was right.

### 8b. Book H — the hedge, where the error changes sign

Same two names, opposite way round: **+50% KVR, −50% TLM.**

```
wᵀΔ_diag w  =  (1/2)²·8 + (−1/2)²·8       =  4      ← unchanged. Squares do not care about signs.
wᵀΔ_full w  =  4  +  2·(1/2)·(−1/2)·6     =  4 − 3  =  1

risk, diagonal only  =  2.0000%       (exact)
risk, full matrix    =  1.0000%       (exact)
```

**The diagonal model says 2% where the truth is 1% — exactly double, and exactly 100 bps too
high.** The discarded term is `−3` against a full variance of `1`: three times the whole answer,
with the opposite sign.

This is the paper's own sentence, and it is worth reading before the player has finished being
surprised. p.28, PAPER:

> "…these specific returns may be positively correlated, and so **ignoring this correlation
> would lead to under (or over) prediction of specific risk in a long-only (long-short)
> portfolio context.**"

BFRE states the direction of the error, both directions, in one line. The player has just
derived both halves.

### 8c. Book A — all four names, equally weighted

```
diagonal part :  (1/16)(8 + 8 + 9 + 6)     =  31/16  =  1.9375     (exact)
cross term    :  2 · (1/4) · (1/4) · 6     =  12/16  =  0.75       (exact)

wᵀΔ_diag w  =  31/16  =  1.9375   risk  =  1.3919%      (rounded)
wᵀΔ_full w  =  43/16  =  2.6875   risk  =  1.6394%      (rounded)
```

```
variance ratio  43/31   exactly
risk ratio      1.177751       (rounded)
reported share  0.849076       (rounded)
risk missing    0.247419 pp  =  24.74 bps      (rounded)
```

Four names is not diversification. **One of the six pairs in this book is linked**, and the
model is still `1 − 0.849076 = 0.150924` (rounded) — just over 15% — light.

### 8d. Book W — the wide book

Now the same four names inside a real book: **fifty names at 2% of NAV each.** The other
forty-six are assumed to have a leftover size of `d = 8` and **no** link to anything —
*that is a stated assumption about names we have not shown you, not a derivation.*

```
diagonal part :  (1/50)² · ( 8 + 8 + 9 + 6  +  46 × 8 )
              =  (1/2500) · ( 31 + 368 )   =  399/2500  =  0.1596      (exact)
cross term    :  2 · (1/50) · (1/50) · 6   =   12/2500  =  0.0048      (exact)

wᵀΔ_diag w  =  399/2500  =  0.1596   risk  =  0.3995%      (rounded)
wᵀΔ_full w  =  411/2500  =  0.1644   risk  =  0.4055%      (rounded)
```

```
variance ratio  137/133   exactly
risk ratio      1.014926       (rounded)
reported share  0.985293       (rounded)
risk missing    0.005963 pp  =  0.60 bps       (rounded)
```

### 8e. The asymmetry, in one table

| Book | pairs in the book | linked pairs | variance ratio, exact | share of variance discarded | reported / true | **bps missing** |
|---|---:|---:|---:|---:|---:|---:|
| **P** — the pair trade | 1 | 1 | **7/4** | **3/7** = 0.428571 *(r)* | 0.755929 *(r)* | **64.58** *(r)* |
| **A** — four names | 6 | 1 | 43/31 | 12/43 = 0.279070 *(r)* | 0.849076 *(r)* | 24.74 *(r)* |
| **W** — fifty names | 1225 | 1 | 137/133 | 4/137 = 0.029197 *(r)* | 0.985293 *(r)* | **0.60** *(r)* |
| **H** — the hedge | 1 | 1 | 4 *(the other way up)* | −3 *(of a variance of 1)* | **2.000 — too high** | −100 *(exact)* |

```
Book P's shortfall ÷ Book W's shortfall  =  108.3       (rounded)
```

**One identical modelling error. A hundredfold difference in what it costs.** And the direction
of the difference is the worst possible one: the error is smallest where the manager is safest
and largest where the manager has concentrated. Book W has 1225 pairs and one of them is
linked (`1/1225 = 0.000816`, rounded). Book P has one pair and it is the linked one.

### 8f. And the sign is not fixed either

The thing deleted when you go from `Δ_full` to `Δ_diag` is a matrix with zeros down its middle
and `6`s off it. That matrix is **indefinite**: Book P gets `+3` from it and Book H gets `−3`.
Sweeping every whole-number book with weights from −3 to +3 on the four names — **2,401** books
— the full-matrix variance is non-negative in all 2,401 (as it must be: it is a genuine sum of
squares), and the diagonal model **overstates** the risk in **882** of them.

So the honest sentence is not *"the diagonal assumption understates risk"*. It is:

> **The diagonal assumption deletes a term whose sign it does not control. In a long-only book
> holding linked names it deletes a positive number and the risk comes out too low. In a book
> that is long one and short the other it deletes a negative number and the risk comes out too
> high. Which is exactly what page 28 says.**

### 8g. The general formula, so the player never has to guess again

Take `N` names at equal weight `1/N`, all with leftover size `d`, exactly one linked pair with
correlation `ρ`:

```
wᵀΔ_diag w  =  N · (1/N)² · d            =  d/N
wᵀΔ_full w  =  d/N  +  2 · (1/N)² · ρd

        ┌──────────────────────────────────────────┐
        │   variance ratio  =  1  +  2ρ/N          │
        └──────────────────────────────────────────┘
```

With this file's `ρ = 3/4`, that is `1 + 3/(2N)`:

| `N` | variance ratio, exact | risk ratio |
|---:|---:|---:|
| 2 | **7/4** | 1.322876 *(rounded)* |
| 4 | 11/8 | 1.172604 *(rounded)* |
| 10 | 23/20 | 1.072381 *(rounded)* |
| 25 | 53/50 | 1.029563 *(rounded)* |
| 50 | **103/100** | 1.014889 *(rounded)* |
| 100 | 203/200 | 1.007472 *(rounded)* |

`N = 2` reproduces Book P's `7/4` exactly. `N = 50` gives `1.014889` (rounded) against Book W's
measured `1.014926` (rounded) — **the same to four decimal places**, the tiny gap being that
Book W's four named assets do not all have `d = 8`.

**The error dies like `1/N`, and concentration is exactly the failure of `N` to be large.** Say
that sentence at the table and make the player say it back with `2ρ/N` in their hand.

---

## 9. The same-company case — the one BFRE *does* put a number in

Everything above has been about two *different* companies. Now suppose TLM were not Talmar
Motors but **a second listing of Kaveri itself** — a cross-listing, or a depositary receipt on
the same shares. Page 28 tells you exactly what BFRE does, and the two methodologies it names
are worth building because they disagree loudly.

**PAPER, p.28:**

> "The first approach is referred to as the **structural approach** and assigns related listings
> identical specific risk forecasts (typically **cloned from the primary listing**) and **forces
> the specific return correlation to be 1**. In contrast, the second – empirical– approach
> estimates these quantities separately using data specific to each asset, and so results in
> different specific risk forecasts and specific return correlations."
> *(the unbalanced dash pair around "empirical" is the source's)*

So under the **structural** approach both lines get `d = 8` (cloned) and `Δ_12 = 8`, because a
correlation of 1 with equal sizes means the covariance *is* the variance:

|  | line 1 | line 2 |
|---|---:|---:|
| **line 1** | 8 | **8** |
| **line 2** | **8** | 8 |

`det = 8×8 − 8×8 = 0` exactly — the matrix is on the edge of Level 8's cliff, by construction.

**50/50 across the two lines:**

```
wᵀΔ_diag w  =  4                risk  =  2.0000%      (exact)
wᵀΔ_full w  =  4 + 4  =  8      risk  =  2.8284%      (rounded)

variance ratio  2   exactly   — the diagonal model throws away exactly half
risk ratio      √2  =  1.414214   (rounded)
reported share  1/√2 = 0.707107   (rounded)
```

And two facts that make the structural approach's *meaning* unmistakable:

1. **The split does not matter at all.** 50/50, 60/40, 90/10, 25/75 — the true variance is
   **exactly 8** every time, because `8w² + 8(1−w)² + 2·w(1−w)·8 = 8(w + (1−w))² = 8`. Holding
   one company through two tickers is holding one company. The diagonal model, by contrast,
   claims your risk *falls* when you split the position across the two lines, which is
   nonsense dressed as diversification.
2. **The hedged version has exactly zero leftover risk.** `+50%` one line, `−50%` the other:
   `4 − 4 = 0`. The diagonal model still says 4, i.e. 2.0000%.

That second one is not a defect — it is why the paper ships **two** methodologies, and p.29
says so in one sentence (PAPER):

> "…**structural approach** is typically used by **active portfolio managers** who view related
> listings as being entirely fungible over longer horizons, i.e. **many months**, whereas the
> **empirical approach** is typically more suited to **index tracking portfolios**, where even
> small differences in how related listings trade on a day-on-day basis can **significantly
> impact their performance**."

For the manager holding both lines for six months, they are one position and the structural
answer (2.8284%, rounded) is right. For the tracker whose entire risk *is* the day-to-day basis
between the two lines, forcing the correlation to 1 declares that risk to be zero, and the
empirical approach exists for them. **A single default would be wrong for one of the two by
construction.**

**Two refinements the player must carry, because they are the difference between reciting and
knowing** (both PAPER, p.28):

- The structural approach applies to "(a) **cross-listings** and (b) **derived securities**
  (ADRs, GDRs, NVDRs & Certificates) and their root assets."
- **Different share classes are NOT included.** "Note that specific risk forecasts and specific
  return correlations for different share classes, e.g. 'A' and 'B', ordinary and preference
  shares, are **still estimated empirically under the structural approach** as these lines
  confer different rights to the owner and are **in no way fungible**." A player who says "BFRE
  forces A and B shares to correlation 1" has it backwards, and it is the kind of error a real
  quant will catch in one sentence.

---

## 10. Sabotage round (round type B) — run both before the boss

### 10a. A grid no data could have produced

Hand the player this and say nothing:

|  | KVR | TLM |
|---|---:|---:|
| **KVR** | 8 | **10** |
| **TLM** | **10** | 8 |

Three ways to catch it, in increasing order of what they prove:

1. `ρ = 10/8 = 1.25 > 1`. A correlation above one is not a large correlation; it is not a
   correlation.
2. `det = 8×8 − 10×10 = −36 < 0` (Level 4's determinant, Level 8's health check).
3. **The one that actually matters on a desk:** price the hedged book. `4 − 5 = −1`. A book
   with **negative variance**. Level 8's rule, unchanged: *no book can have negative variance,
   and a grid that says otherwise is invalid, not conservative.*

### 10b. A corrupted miss, and a check that only half works

Go back to the Level-8 file, month 1, and push **CHR's** miss from `+2` to `+3`.

```
Σu    =  +1     ← broken. The market column's balance is gone.
Σx·u  =   0     ← still holds!
```

Only one of the two checks fires, and the reason is Level 6's: **CHR's exposure is zero**, so
CHR is invisible to the cheapness balance. Corrupt **EMK** instead (`+1 → +2`) and both fire:
`Σu = +1` and `Σx·u = +2`.

The lesson is the desk one: *the balance conditions catch corruption, but each column only
catches corruption it can see, and a stock at `x = 0` is invisible to every column but the
intercept.* A model with no intercept would catch neither.

---

## 11. Traps, and exactly what each wrong belief returns numerically

| Wrong belief | What it returns on these files | Why it is wrong |
|---|---|---|
| "Least squares makes the leftovers independent" | — | It forces `Σ_i ω_i x_i u_i = 0` **across assets, within a period**. It says nothing across time. Section 3d: `Σ_t f_Chp·u_CHR = 6`, `Σ_t u_BRN·u_DLT = 10` |
| "`Δ` is diagonal because the paper says so" | — | p.24's "a diagonal matrix" describes the **generic** model ("In general a multi-factor model…"). p.27 says BFRE's is "a vector of asset specific risk forecasts **and** a sparsely populated … matrix containing non-zero, off-diagonal specific return correlations" |
| "The diagonal assumption always understates risk" | Book H: it **overstates** by exactly 100 bps; 882 of 2,401 swept books | The deleted matrix is indefinite. p.28: "under (or over) prediction … in a long-only (long-short) portfolio context" |
| "Specific risk diversifies away, so this doesn't matter" | Book P loses **64.58 bps** *(rounded)* | True of a wide book (Book W: 0.60 bps, rounded). False of a concentrated one, and `1 + 2ρ/N` says exactly how false |
| "The link is small because the correlation is only 0.75" | variance ratio 7/4 — the truth carries **75% more variance** and **32.3% more risk** *(rounded)* | Correlation is not the answer; `2 w_i w_j ρ √(d_i d_j)` is. At equal weights on two names, `ρ` is the *whole* excess |
| "Add the two names' risks: 2.8284 + 2.8284" | 5.6569% *(rounded)* | Variances combine, never volatilities — Level 8's first trap. Truth 2.6458% *(rounded)* |
| "Use the correlation 3/4 in the grid" | Book P gets `4 + 2·(1/2)·(1/2)·(3/4) = 35/8 = 4.375` exactly, risk **2.0917%** *(rounded)* instead of 2.6458% *(rounded)* | The grid holds the **covariance** `6`, not the correlation `3/4`. Same error Level 8 catalogued for `F` |
| "BFRE assumes all specific returns are uncorrelated" | — | It assumes it **across companies** (p.28, p.30). Within a company it estimates or overrides them (p.28). Saying the first without the second is the cheap shot |
| "BFRE forces A and B shares to correlation 1" | — | Backwards. p.28: share classes "are still estimated empirically **under the structural approach**" |
| "Divide by `T−1`, everyone does" | every `d` scales by `T/(T−1)`; `d_CHR` becomes 5 | Defensible, and it changes **no ratio on this page**, because a common factor cancels. The paper states no divisor at all. Declare it |
| "…and subtract the mean while you're at it" | `d_CHR` becomes **16/5 = 3.2**, `d_BRN` **23/10 = 2.3**, and `d_CHR/d_BRN` moves from `2` to `32/23` | A *different* choice from the divisor, and this one is **not** a common factor — every row has its own mean (Section 4a). Anyone who says "divisor or mean, same thing" has just lost the ratio argument |
| "A negative off-diagonal means the model is broken" | Section 5a's grid is full of them | With an intercept column they are *forced*: rows sum to zero. Worth `−1/(N−1)` and no more |

---

## 12. Names unlocked at the end of this level

Locked until now on purpose. Each is now attached to something the player built.

| Name | What it actually is, in this level's terms |
|---|---|
| **specific return** / **idiosyncratic return** | the leftover `u` — p.24's own two words for it |
| **specific risk** | a **forecast** of how big that leftover will be. A volatility, not a return |
| **specific risk matrix `Δ`** | the grid of Section 6d — equation (1.8), p.24 |
| **diagonal** | the middle line only; everything off it set to zero |
| **specific return correlation** | the off-diagonal, expressed as a correlation — **p.28's own phrase** |
| **structural approach** | clone the risk, force the correlation to 1 — **p.28** |
| **empirical approach** | estimate both from the data — **p.28** |
| **cross-sectional overlay** | a forecast borrowed from similar assets when history is short — **p.28** |
| **sparse** | mostly zeros, with a few entries that are not |
| **second moment** | `(1/T)Σu²` — a size measured from zero, not a spread about a mean |
| **Newey–West** | the serial-correlation adjustment BFRE uses to turn daily leftovers into a one-month forecast — **p.27, p.28**. **Named, not built. Graduate-level. Say so.** |

**Say, as you hand each one over:** *this is the industry word for the thing you just built.*
Of the eleven rows above, **nine carry the paper's own words**: specific return / idiosyncratic
return (p.24), specific risk (p.27), specific risk matrix (p.24), diagonal (p.24), specific
return correlation (p.28), structural approach (p.28), empirical approach (p.28), cross-sectional
overlay (p.28), Newey–West (p.27). A tenth, *sparse*, is the paper's own adjective ("sparsely
populated", p.27) turned into a noun-phrase. Exactly **one** of the eleven — *second moment* —
never appears in the paper at all. `9 + 1 + 1 = 11`.

Contrast that with Level 8, where nearly everything had to be borrowed from outside the paper:
**`Δ` is the best-documented object in the model.** Say so before you criticise it.

**Do not unlock here:** *asset covariance matrix `Σ`* and the assembly `Σ = XFXᵀ + Δ`, plus
*Active Risk* and *tracking error* (all **Level 10** — you may point at the printed equation, but
the left-hand side is not yours); *marginal contribution to risk* (Level 11); *bias statistic*
(Level 12).

---

## 13. Ladder position after this level

| Concept | Tier to demand |
|---|---|
| building `Δ`'s diagonal from a leftover panel | **5 (rebuild)** — on a panel they have never seen, unprompted |
| `wᵀΔw` derived from squaring a weighted sum | 4 (defend) — including why the cross term is doubled |
| **guaranteed vs assumed**, with a worked example of each | **5 (rebuild)** — this is the level's whole point; nothing less passes |
| `Σ_i ω_i x_i u_i = 0` stated *with the weights* | 4 (defend) |
| the direction of the error, both signs, with a book for each | **4 (defend)** — the boss-round gate |
| `1 + 2ρ/N`, derived and used | 3 (derive) at minimum |
| what BFRE keeps off the diagonal, and what it does not | **4 (defend)** — including the share-class carve-out |
| structural vs empirical, and which user each suits | 3 (derive) — the argument, not the labels |
| the `−1/(N−1)` mechanical link, and why it does not matter | 3 (derive); 4 to survive the CRO |
| the divisor choice and its irrelevance to every ratio | 2 (compute) is acceptable |

Do not mark Level 9 complete unless the player can, **unprompted, on a new leftover panel**,
build `Δ`, price two books with and without the off-diagonals, say which direction the error
runs **and why it runs that way for that book**, and then argue the paper's side.

---

# 14. BOSS ROUND — The Private Drama

Round type: **E. INTERROGATION**. Play a Chief Risk Officer with thirty years on the desk and
no patience. The task, from the rulebook: *construct a scenario where the diagonal assumption
fails, and show the risk number comes out too low exactly where it hurts.*

> **Announce the scope at the top of the round, in these words or close to them:**
> *"You are not going to catch BlackRock out. They wrote the failure mode down, they wrote
> the direction of the error down, and they built two different fixes for it. Your job is to
> find the case they explicitly excluded, price it, and then tell me why they were right to
> exclude it anyway. If you open with 'page 24 says diagonal and page 27 says it isn't', I
> will end the interview."*

## 14.1 The setup, as the player receives it

A portfolio manager runs a book. She has one high-conviction idea: Kaveri Castings is being
priced as though Talmar Motors' order book will hold up, and it will not. She expresses it as
**50% of NAV in KVR and 50% in TLM**, both long, because she thinks the whole supply chain
re-rates together.

She asks the risk system for the leftover risk on that book. The system returns **2.00%**.

*What is wrong, by how much, and how would anyone ever know?*

The player has the panel of Section 6b and nothing else.

## 14.2 The arithmetic they must produce

```
d_KVR = 48/6 = 8            d_TLM = 48/6 = 8            Δ_KVR,TLM = 36/6 = 6

diagonal only :  (1/4)(8) + (1/4)(8)                    =  4      risk 2.0000%   (exact)
full          :  4  +  2·(1/2)·(1/2)·6  =  4 + 3        =  7      risk 2.6458%   (rounded)
```

```
variance ratio          7/4                    exactly
risk ratio              1.322876               (rounded)
the system reports      0.755929               (rounded)  of the truth
missing                 64.58 bps              (rounded)
```

**And the counterfactual that proves it is not a maths trick.** Build the book's own leftover
series from the panel — `(KVR + TLM)/2` month by month:

```
+9/2,  −3/2,  −5/2,  −3,  +2,  +1/2         second moment  =  42/6  =  7
```

Seven. Straight off the six months, no matrix involved. **The book really did wobble that much,
and the system said it did not.**

## 14.3 Where it hurts, side by side

| Book | risk, diagonal | risk, truth | missing | reported / true |
|---|---:|---:|---:|---:|
| **P** the PM's pair trade, 2 names | 2.0000% *(exact)* | 2.6458% *(r)* | **64.58 bps** *(r)* | 0.755929 *(r)* |
| **A** four names, equal | 1.3919% *(r)* | 1.6394% *(r)* | 24.74 bps *(r)* | 0.849076 *(r)* |
| **W** fifty names, equal | 0.3995% *(r)* | 0.4055% *(r)* | **0.60 bps** *(r)* | 0.985293 *(r)* |

```
Book P's shortfall  ÷  Book W's shortfall
   =  (√7 − 2)  ÷  (√411 − √399)/50
   =  0.645751  ÷  0.005963   =   108.3        (rounded)
```

*Divide the **shortfalls**, not the two-decimal bps printed in the table above: `64.58 / 0.60`
reads `107.6`, and the gap is entirely the rounding of `0.596…` up to `0.60`. Both shortfalls
above are themselves rounded from the exact roots shown.*

**Say the sentence.** The error is invisible on the book that did not need the warning and
maximal on the book that did. It is not a random error; it is an error that has learned where
to hide. A risk system that is right about the diversified book and wrong about the
concentrated one is wrong in the only place a risk system is read.

The player must also volunteer the sign flip without being asked. If the same PM had put the
trade on as **long KVR / short TLM** — a perfectly reasonable way to express "the components
maker is cheap relative to the assembler" — the diagonal model would report **2.00%** against
a truth of **1.00%**: exactly **twice** the risk, exactly 100 bps too high, and she would be
told to cut a position that is safer than the system believes. **Both mistakes come from the
same deleted `6`.**

## 14.4 Why BFRE does it anyway — the counting argument (CALL BACK to Level 8's boss round)

This is the half that separates a critic from a rival. Ask: *"fine — so estimate them all.
What stops you?"*

`Δ` for `N` assets has `N(N+1)/2` distinct entries. Table 1.3 (p.28, PAPER) says the daily
specific-risk model uses **375** observations. So you have `375 × N` numbers.

| `N` | distinct entries `N(N+1)/2` | numbers available `375N` | |
|---:|---:|---:|---|
| 100 | 5,050 | 37,500 | enough |
| 375 | 70,500 | 140,625 | enough |
| **749** | **280,875** | **280,875** | **exactly break-even** |
| 750 | 281,625 | 281,250 | not enough |
| 3,000 | **4,501,500** | **1,125,000** | not enough — **3001/750 = 4.001333** *(rounded)* parameters per number |

The break-even is clean and the player can derive it in one line:
`N(N+1)/2 ≤ 375N ⟺ (N+1)/2 ≤ 375 ⟺ N ≤ 749`. For the weekly models (104 observations,
Table 1.3) the break-even is `N ≤ 207`.

And it is worse than a shortage, in exactly the way Level 8's boss round was worse: a
second-moment matrix built from 375 observations has **rank at most 375**. For any universe
bigger than that, the estimated full `Δ` is singular — it certifies some real, non-zero,
leverable book at **exactly zero** leftover risk. Level 8 showed that on a 3×3 grid from three
months. Nothing about the argument changes here except which matrix it is aimed at.

Meanwhile **the diagonal alone needs `N` numbers**, and has 375 observations for each one. The
diagonal is over-determined 375 to 1. The full matrix is under-determined.

> **This is the defence, and the player must make it before they are allowed to attack.**
> BFRE is not being lazy. There is no estimator of a full `Δ` for a real universe, at any price.
> The only question available is *which* off-diagonals to restore by hand, from structure rather
> than from data — and p.28 answers it: the ones inside a single company, "either **imposed via
> a constant override of 1**, or where data availability permits, **estimated using asset
> specific returns**."

**Flag the invention honestly.** The paper **never prints the size of any estimation universe**.
The 3,000 in that table is ours, chosen to be obviously large. The break-even of 749 is *not*
ours — it follows from the paper's own 375 — and the player should quote it that way: *"their
own observation count says the full matrix stops being estimable somewhere around seven hundred
and fifty names."*

## 14.5 So what *is* the criticism? — the version that survives

Having granted all that, the attack narrows to one sentence and gets sharper for it:

> **The rule "within a company, yes; across companies, no" is a rule about legal structure, and
> the risk it is trying to catch is not about legal structure.** Kaveri and Talmar are one
> economic exposure and two companies. The rule cannot see them, and the justification the
> paper offers for the cut-off is, in full: **"in-line with standard modelling practice"**
> (p.28). That is an appeal to convention, printed as such.

Three things make this the *good* version of the attack rather than the cheap one:

1. It grants the counting argument (14.4) in advance, so it cannot be answered by it.
2. It attacks a **stated** justification rather than an omission — the paper's own sentence is
   the exhibit.
3. It comes with a number: on the book that actually holds the pair, **64.58 bps** (rounded) of
   a **2.6458%** (rounded) leftover risk — `1 − 0.755929 = 0.244071` (rounded) of it — and half of a real Active Risk
   report is booked as Specific in the first place (p.35: **Specific 50%**, read directly off
   the pie; p.34, PAPER: "the Active Risk is **split equally** between common factors and stock
   specific sources").

`gm/CRITIQUE.md` files this in the **grey zone**, correctly: *"Two suppliers to the same
collapsing customer. Where does that risk live?"* — raise it as a question, never as a scandal.

## 14.6 The trap good players fall into — have this ready

The sharpest players make **one** of these three moves, and each is half-right:

**(a) "So the model understates risk."** No — Section 8b. It understates for the long book and
overstates for the hedged one, and p.28 says so. A player who has only learned the long-only
direction has memorised a fact instead of a mechanism. Send them to Book H.

**(b) "Then just add an industry factor for supply chains."** Genuinely interesting, and it is
what BFRE did for the small-cap effect: p.16, PAPER — before a small-cap factor existed,
deciles 9 and 10 still showed enough leftover commonality to clear the paper's own 10% line
`[APPROX — Figure 1.10's heights are pixel measurements; quote the position relative to the
printed 10% line, never the digits]`, and adding the factor pushed both below it. So *common
structure left in the leftovers can be fixed by adding a column*, and BFRE has done it.
**But the fix does not generalise here.** A small-cap effect is shared by a decile of the
universe, so one column serves thousands of assets. "Kaveri's exposure to Talmar's order book"
is shared by two. You cannot buy a factor per supply chain, and if you tried you would be
undoing the thing BFRE is *for*. p.2, PAPER: BFRE "**imposes far more structure on the asset
covariance matrix, reducing the modelling problem to a smaller set of factors, which capture
the most important sources of asset return commonality**". A factor per supply chain is that
sentence run backwards. *(`notes/` also describes Aladdin's existing STORM approach as an
asset-by-asset covariance matrix with each asset effectively its own factor — but that
sentence is the **transcriber's summary**, not printed text, so do not quote it as the
paper's.)* Pay them for the idea, then make them find its limit.

**(c) "The paper contradicts itself: page 24 says diagonal."** Dock it. This is `gm/CRITIQUE.md`
**CS-3**, a named cheap shot. p.24's sentence is introduced by "**In general a multi-factor
model** decomposes asset returns as follows" — it is a description of the textbook object, and
p.27 states BFRE's own version plainly two pages later, and p.28 gives it a subsection. If the
player has been holding this since Section 4c waiting to spend it, that is the moment to
explain that a rival who opens with it has told the room they read the equations and not the
prose.

## 14.7 The interrogation script (real objections, escalating)

1. *"Your correlation is three-quarters. Where did you get it? Six months. I've seen six-month
   correlations of 0.75 between a bank and a bakery."*
   → Section 6c. The link is not a sample statistic here; it is **built** — a shared shock of
   size 6 plus two private shocks of size 2, orthogonal by construction. On real data they
   would need the p.28 machinery, and its whole point is that six months of data is not what
   justifies restoring an off-diagonal — **structure** is.
2. *"Change the divisor to `T−1` and your number changes."*
   → Every `d` and every `Δ_ij` scales by `6/5`. Every **ratio** on the page is identical.
   `7/4` stays `7/4`. Section 4a. **If he follows up with "and subtract the means too" — on
   *this* panel the four sample means are already zero (6b), so centring changes nothing here;
   on the Level-8 file it changes plenty, and Section 4a shows exactly how much. Concede that
   half; it costs nothing and it is the half he is testing for.**
3. *"Fine. Now show me it matters on a real book, not a two-name cartoon."*
   → Book A: **24.74 bps** (rounded) on four names. Then concede Book W: **0.60 bps** (rounded)
   on fifty. Then produce `1 + 2ρ/N` and let the CRO pick any `N` he likes. A player who
   concedes Book W *before* being pushed has understood the level.
4. *"Then it's a rounding error and you've wasted my morning."*
   → Only if the book is wide. The whole point is that it is not a random error: `2ρ/N` is
   monotone in concentration, and concentration is the condition under which a risk number is
   read at all. Page 35's own example books **50%** of its Active Risk as Specific.
5. *"Estimate the whole matrix then. Stop complaining."*
   → 14.4. Break-even 749 names on the paper's own 375 observations; rank at most 375; the
   estimated matrix would price real books at zero.
6. *"So BlackRock is right and you have nothing."*
   → 14.5. They are right about the impossibility and right about the fix; the justification
   for where the fix stops is "standard modelling practice", and that sentence is doing a lot
   of work for a boundary drawn by company registration rather than by economics.
7. *"Last one. Your model says my pair trade is 2.6458% and the system says 2.0000%. Which do
   I put in the report?"*
   → **Neither, without saying which.** The honest answer is that the system's number is
   correct given its assumption, the assumption is wrong for this specific book, and the
   fix belongs in the model rather than in a spreadsheet override — because an override
   applied by hand to one book is exactly the thing nobody can audit later. If the player
   says "I'd just add 65 bps", ask them what they will do about the next PM's pair trade, and
   the one after that.

## 14.8 Pass conditions

All seven, and the second one is the level:

1. Produces `Δ` from the panel, both matrices, and both book numbers, by hand.
2. States **guaranteed vs assumed** without prompting, and gives a *worked example of each* —
   `Σ_i u_i(t) = 0` in every month of the Level-8 file, against `Σ_t u_BRN·u_DLT = 10` in the
   same file.
3. Gets the **direction** right for both a long and a hedged book, and can say why the sign
   flips.
4. Concedes the diversified case (Book W, **0.60 bps**, rounded) unprompted.
5. Makes the counting defence (14.4) **for** the paper before attacking it.
6. Refuses the cheap shot when offered it.
7. Knows what BFRE actually keeps off the diagonal — cross-listings and derived securities
   under the structural approach; share classes empirically **under both**; nothing across
   companies.

---

## 15. What this level does NOT settle, stated so the player is not misled

- **How BFRE actually estimates a specific return correlation when it does estimate one.**
  p.28 says "estimated using asset specific returns" and stops. No window, no weighting, no
  shrinkage, no estimator. IOU.
- **The functional form of the cross-sectional overlay's weighting function.** p.28 says the
  weight rises with data availability and reaches 1 "in the limit". The function itself is
  not given. IOU, and a Level-12 exhibit.
- **Newey–West.** Named, not built. Graduate-level. IOU.
- **How `Δ` and `F` combine.** Nothing on this page prices a *total* risk — every number here
  is the leftover half alone. `Σ = X F Xᵀ + Δ` is Level 10, and the cross-terms that equation
  quietly deletes are Level 10's problem, not this one.
- **Whether the factor list should have had another column.** Section 14.6(b) opens it and
  deliberately does not close it. p.16's small-cap fix is the paper's own answer to a related
  question; the general question — how you would know a factor is missing rather than a
  correlation — is Level 12.
- **Estimating the whole thing with structure instead of data.** Factor-model-of-residuals,
  clustering, industry-block specific correlations: all real research directions, none of them
  in this paper, none of them built here.

---

## 16. Back to BFRE — what this machinery does in the real model

### 16a. p.24 — where `Δ` lives, and the exact words it is introduced with

Equation (1.8), one line under (1.7):

```
(1.7)   r  =  X f  +  u
(1.8)   Σ  =  X F Xᵀ  +  Δ
```

The where-list defines the last symbol as (PAPER):

> "`Δ` : specific risk matrix (**a diagonal matrix** of asset specific risk forecasts)"

and the lead-in sentence above (1.7) reads (PAPER):

> "**In general a multi-factor model** decomposes asset returns as follows:"

Read those two together and the "diagonal" is a description of the textbook object. Same page,
the sentence that says what `u` is (PAPER):

> "`X f` is termed the common factor return and `u` is the asset specific, or idiosyncratic,
> return."

and the sentence that says what has to be true for the split to mean anything (PAPER):

> "In a well-specified model, the prescribed factors will capture **all** sources of commonality
> in asset returns leaving only return associated with **stock-specific events** in the
> idiosyncratic component."

**That sentence is the whole level in one line.** `Δ` is defined as the home of stock-specific
events — so anything *not* stock-specific that ends up there has been mislabelled, and the
mislabelling is invisible from inside the diagonal.

*(The left-hand side of (1.8) is Level 10's. Do not name it here.)*

### 16b. p.27 — what BFRE actually builds

PAPER, the first sentence of the *Specific Covariance Matrix* subsection:

> "The asset specific covariance matrix is made up of **two** components: a vector of asset
> specific risk forecasts **and a sparsely populated unit diagonal matrix containing non-zero,
> off-diagonal specific return correlations.**"

Two components. A list of sizes — Section 4 — and a set of off-diagonals — Section 6d. **The
shipped `Δ` is not diagonal**, and the paper says so on the page where it describes it.

### 16c. p.28 — the direction of the error, in BFRE's own words

PAPER:

> "Linkages between related assets in the same company are **not completely captured by the
> common factors** in the model. In these instances, specific returns continue to capture both
> the idiosyncrasies of asset return **and company return**. As a result these specific returns
> may be **positively correlated**, and so **ignoring this correlation would lead to under (or
> over) prediction of specific risk in a long-only (long-short) portfolio context.**"

Every clause of that maps onto something the player built:

| The paper's clause | What the player built |
|---|---|
| "not completely captured by the common factors" | the shock `g` in Section 6c, which no column of `X` reaches |
| "continue to capture both … and company return" | `KVR = g + p_K`: two things in one leftover |
| "may be positively correlated" | `Δ_KVR,TLM = 6`, `ρ = 3/4` |
| "**under** … prediction … in a **long-only** … context" | Book P: 2.0000% against 2.6458% *(rounded)* |
| "(**over**) … (**long-short**)" | Book H: 2.00% against 1.00%, exactly double |

### 16d. p.28 — the two methodologies, and the parameters

Table 1.3 (**p.28**, PAPER, verified digit for digit):

| Model frequency | Half-life | Observations | Newey–West lag |
|---|---|---|---|
| Daily | **125 days** | **375 days** | **10 days** |
| Weekly (WRLD and EMKT) | **26 weeks** | **104 weeks** | **2 weeks** |

375 trading days is about **18 months**, not 15 — a trading year is roughly **252** days, so
`375/252 = 1.4881` years *(rounded)*, i.e. `125/7 = 17.8571` months *(rounded)*. 104 weeks is
exactly **2** years. *(252 is the market's number, not the paper's: BFRE never prints a
trading-day count. Quote the 375 and give the conversion's assumption out loud.)*
And the mechanism for the off-diagonals, PAPER:

> "In all circumstances linkages can be captured through specific return correlations, either
> **imposed via a constant override of 1**, or where data availability permits, **estimated
> using asset specific returns**."

Section 9 priced the override. Its consequence — the split not mattering, the hedge going to
zero — is not a bug in our toy; it is what "1" means.

### 16e. p.30 — the assumptions, filed as assumptions

The *Model Assumptions & Limitations* section is one of the paper's better pages, and two of
its bullets are this level's (both PAPER):

> "Factor returns have **zero correlation** with asset specific returns, and specific returns
> from different issuers are **unrelated and have zero correlation**"

> "Specific return correlations are computed relative to a **representative, root asset**.
> Despite being a popular approach in industry, this model **does not adequately capture all
> relationships between different listings of companies, which have more than one share class
> with derived securities linked to those share classes**, e.g. Chinese MMA securities. **This
> will be addressed in a forthcoming model release**"

That second bullet is a **shipped defect, named by its authors, with a fix promised**. A player
who wants to attack `Δ` should notice that the paper got there first on the hardest sub-case,
and that this is a concession a credible rival must grant (`gm/CRITIQUE.md` §8, concession 3).

### 16f. p.16 — the other way a leftover goes wrong

The failure this level prices is *a real link, not modelled*. The mirror failure is *a real
factor, not modelled* — common variation that has nowhere to go but into the leftovers, where
it is then declared private and diversifiable.

BFRE found one and published the before-and-after. PAPER, p.16:

> "Prior to the addition of a small-cap factor, there is significant explanatory power in the
> lower deciles, **9 and 10**, in excess of the **10% threshold** used to determine whether
> styles are eligible for inclusion in the model."
> "Following the addition of a small-cap factor, the proportion of t-statistics for these
> deciles is **no longer statistically significant**."

Figure 1.10 draws the 10% line, and deciles 9 and 10 are the **only two of the ten** that clear
it before the fix and neither clears it after. `[APPROX — the bar heights in notes/ are pixel
measurements, ±0.5pp; cite the positions relative to the printed line, never the digits.]`

**INFER, and say so:** the direction is the same as this level's, for the same reason. A common
effect sitting inside `u` is booked as private, so a book concentrated in small caps is told
its risk diversifies when it does not.

### 16g. p.35 — the size of the stake

The sample Equity Daily Risk report (Figure 1.18, p.35) splits Active Risk by block:
**Specific 50%**, Style 25%, Industry 14%, Country 6%, FX 4%, Act Sec 1%
`[the last is INFERRED — the glyph reads 1 or 2, and 1% is recorded only because the six then
sum to exactly 100. The other five are read directly.]` p.34 states it in prose (PAPER):

> "The report shows that the Active Risk is **split equally between common factors and stock
> specific sources**."

**Half of a real risk number is the object this level built.** Everything Levels 1–8
constructed — `X`, `f`, `F` — accounts for the other half.

### 16h. Where this level's machinery ends up in the finished model

1. Run the cross-sectional regression (Levels 1–5), daily for regional models, weekly for the
   World model (p.24). Keep `u`.
2. Do that every period (Level 7). Now every asset has a **time series** of leftovers.
3. Cleanse it robustly; weight it with a 125-day half-life over 375 days; aggregate with
   Newey–West to a 1-month horizon (p.27, p.28, p.30). That is the **diagonal** — Section 4.
4. For assets with no history, borrow from similar assets and blend (p.28's cross-sectional
   overlay).
5. Restore the off-diagonals **inside a company only** — override to 1 or estimate — choosing
   structural or empirical by the user's horizon (p.28, p.29). That is Section 6d and Section 9.
6. Hand the finished `Δ` to equation (1.8) on p.24, where Level 10 will add it to `X F Xᵀ`.

### 16i. What the notes do NOT support — searched across all 65 transcribed pages

- **No numerical example of `Δ` anywhere.** Not one specific risk forecast, not one specific
  return correlation, not one asset's leftover. The parameters are printed (Table 1.3); the
  outputs never are.
- **No formula for a specific risk forecast.** No divisor, no statement of whether a mean is
  subtracted, no weighting formula. p.27 gives the ingredients and the adjectives.
- **No estimation-universe size for any model.** So the counting argument in 14.4 must be run
  on the break-even (749 names, from the paper's own 375 observations), never on an asserted
  asset count.
- **No count of how many off-diagonals are actually populated.** "Sparsely populated" (p.27) is
  the only description the document offers; no number, no proportion, no example.
- **No evidence offered for the structural-vs-empirical recommendation.** p.29 argues from
  investor horizon; no bias statistic, no back-test, no comparison is reported for either
  choice. (`gm/CRITIQUE.md` **E-4**.)
- **No justification for the across-company zero beyond "in-line with standard modelling
  practice"** (p.28). That clause is the entire argument, and it is an appeal to convention
  stated as one.
- **The phrases "least squares", "normal equation" and "sum of squares" have zero hits anywhere
  in `notes/`, and "orthogonal" has exactly one — inside a transcriber's comment on p.52, not in
  the paper's own text.** So the whole of Section 3 — the guarantee that makes this level's
  contrast possible — is the game's, built at Level 2. The paper inherits the result and never
  states it, never names the estimator, and never writes a balance condition of any kind.

So: **the object this level builds is named on p.24, described on p.27, given a subsection and
a parameter table on p.28, listed among the assumptions on p.30, and reported at 50% of a real
portfolio's Active Risk on p.35 — and not one of its numbers is ever shown.** That is a much
better record than `F` got at Level 8, and the player should say so out loud before they say
anything else.

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level9.py     # 273 exact-rational assertions, exits 0
```

The script recomputes every figure on this page in `fractions.Fraction`, with square roots
taken in `decimal.Decimal` at 60 digits on top of exact variances: the Level-8 Gram matrix and
all five cross-sectional solves, with both balance conditions checked in all five months and
every miss reproduced; the **weighted** re-fit of that same file behind Section 3c's rider, with
both weighted balance conditions holding in all five months while the unweighted sums do not, and
the weighted form of Section 5's identity (`Σ_i ω_i² d_i = −Σ_{i≠j} ω_i ω_j Δ_ij`) shown to keep
the conclusion while losing the `−1/(N−1)` number; the three non-guarantees of Section 3d,
including the centred covariance of `f_Chp` with `u_CHR`; the five specific variances under the
`T`-divisor and the `T−1`-divisor and the proof that the swap is a **common factor** so every ratio
survives it, then the five **centred** variances (`7/10`, `23/10`, `16/5`, `23/10`, `7/10`) and the
proof that centring is **not** a common factor — two entries rise, one falls, and `d_CHR/d_BRN`
moves from `2` to `32/23`; the fact that the Section-6 panel's four row means are exactly zero, so
centring is moot there; the full 5×5 second-moment matrix with all ten
off-diagonals, all five zero row sums, the `Σ_{i≠j}Δ_ij = −Σd_i` identity and the
`ρ̄ = −1/(N−1)` relation at four values of `N`; the equal-weight book's identically-zero leftover
series and the 0.368 the diagonal model charges it; the three linear relations that collapse the
file's five monthly miss vectors onto a 2-dimensional slice; the new panel's four rows, their sums and
sums of squares; the shared-shock decomposition `g + p_K` and `g + p_T` with all three
orthogonality checks; the full 4×4 `Δ`, its six cross-products, its one correlation and its
2×2 determinant; the quadratic form checked **against each book's own leftover series computed
from the raw panel** for three books and then swept over all **2,401** integer books in
`[−3,3]⁴`, confirming non-negative variance in every one and counting the **882** in which the
diagonal model overstates; all four books' two variances, two risks, exact variance ratios,
rounded risk ratios, reported shares and basis-point shortfalls; the `108.3` ratio taken from the
**unrounded** shortfalls, together with the `107.6` that the rounded bps would wrongly give;
the discarded-variance shares
`3/7`, `12/43` and `4/137`; the two wrong formulas of Section 11 priced (adding the volatilities,
and putting the correlation in the grid instead of the covariance); the pair counts 1, 6 and
1225 and the town's 79,800; the `1 + 2ρ/N` table at six values
of `N` and its agreement with Book W to four decimal places; the structural override's cloned
matrix, its zero determinant, its invariance to the long-only split at four different splits,
and its exactly-zero hedged book; both sabotage exhibits including the negative variance and
the balance check that CHR's zero exposure defeats; the counting argument at five universe
sizes with the 749 and 207 break-evens derived; and Table 1.3 (including the `375 trading days
= 125/84 years = 125/7 months ≈ 18 months` conversion at 252 trading days a year, and the check
that the naive "25 days a month" would imply an impossible 300-day trading year), the p.35 pie's
sum to 100, and the p.16 decile positions relative to the printed 10% line.

If any printed value ever disagrees with this markdown, the markdown is wrong.
