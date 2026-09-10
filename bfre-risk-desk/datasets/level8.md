# Level 8 — The Weather Map

Every number below is recomputed in exact rational arithmetic by `tools/verify_level8.py`
(347 assertions plus 20,946 swept cases, exits 0). Nothing here is rounded by hand. Where a
decimal does not terminate it is written with the word **rounded** next to it; every other
decimal on this page is exact.

> **DIFFICULTY WARNING — read this to the player before anything else. The rulebook
> (`prompt/RISK_DESK.md` §8, BE HONEST ABOUT DIFFICULTY) requires it, and this is the level
> where it matters most.**
>
> **This level is graduate-level, and three separate things on it are.**
>
> - **Section 6 — eigenvalues and eigenvectors.** Normally taught in a second-year university
>   linear algebra course, usually by definition (*"a vector that the matrix only stretches"*)
>   and then justified afterwards. Here it is built the other way round, from *"which
>   combination of bets wobbles most"*, and it comes out in exact fractions with no calculus
>   and no determinant theory. That is doable at 12th standard with strong algebra. The
>   general `K × K` theory is not doable and is not needed.
> - **Section 11.4 — rank deficiency.** The statement "fewer periods than factors makes the
>   estimate structurally broken, not merely imprecise" is a graduate statistics point. It is
>   made here by *exhibiting an actual portfolio* the grid scores at exactly zero risk, so
>   nothing has to be taken on faith.
> - **Section 11.6 — shrinkage.** Bias–variance trading, Stein-type estimators, Bayesian
>   priors. Graduate-level and genuinely contested in the literature.
>
> **And the thing the player must be told loudest: none of the three appears in the BFRE
> paper.** The words *eigenvalue*, *eigenvector*, *principal component* and *PCA* have **zero
> occurrences across all 65 transcribed pages**. The word *shrinkage* appears exactly once,
> inside a bibliography title on p.64 (Tibshirani, "Regression shrinkage and selection via the
> lasso"), for a method the paper on p.8 explicitly **did not adopt**. The paper never
> discusses rank, never prints a factor count, never reports a condition number or a smallest
> eigenvalue.
>
> So Sections 6 and 11 are **the game's argument, not BlackRock's**. Say that out loud, once
> per section, and mean it. Section 13 is where the paper's own numbers come back, and it is
> the only part of this level that is BFRE's.
>
> If the player finds Section 6 heavy, that is correct calibration, not failure. Tell them so
> once, and keep going.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the miss `u`, and why it is scored by its size and not its sign.
**From Level 1** — `b = Σxr/Σx²`, derived by nudging.
**From Level 2** — the balance condition `Σx·e = 0`, forced by the arithmetic of minimising.
**From Level 3** — two columns require two balance conditions at once; the 2×2 solve.
**From Level 4** — the determinant, and what happens as two columns collide. `det = AC − B²`.
**From Level 5** — centering, the pivot moving to `x̄`, and `Cov/Var`.
**From Level 6** — the standard error, degrees of freedom, and the fact that **estimating a
mean costs you one**. `n − k`, and the catastrophe at `n = k`.
**From Level 7** — the same cross-sectional regression run period after period, producing a
*row of factor returns through time* instead of one number.

Level 8 asks the question none of those can answer:

> Level 7 gave you two rows of numbers — one per factor, one entry per period. **Two rows are
> not a risk model.** A book that is long both factors and a book that is long one and short
> the other can have identical exposures to each factor separately and completely different
> risk. What is the missing object, and where does it come from?

Four genuinely new things:

| | What Level 8 adds |
|---|---|
| **A grid instead of a list** | `F`. Section 4 builds it out of the Level 7 series with nothing but sums of products and Level 6's `T − 1`. |
| **A rule that turns the grid into one number** | `hᵀFh`. Section 5 *derives* it by expanding a square — it is not a definition, it is what "variance of a sum" forces. |
| **Directions, not factors** | Section 6. The riskiest thing in a book is usually not a factor; it is a *mixture*. Finding the worst mixture by hand is where an eigenvalue comes from. |
| **A grid that is broken rather than wrong** | Section 11. A grid every entry of which looks perfectly sensible, that nevertheless certifies a real, non-zero, leverable book at **exactly zero risk**. |

**Names deliberately withheld until Section 6h and Section 11.9.** Do not say *covariance
matrix*, *eigenvalue*, *eigenvector*, *positive semi-definite*, *rank*, *singular* or
*shrinkage* at the table before the player has built the corresponding mechanism. Before then,
say: *the grid*, *the direction with the most wobble*, *how much wobble lives in that
direction*, *no book can have negative variance*, *directions the data has never seen*,
*pulling a noisy number toward a steadier one*. (`gm/VOCAB.md` rows 10, 11, 12 set these
unlocks.)

---

## 1. The story — no mathematics

A regional forecaster is asked to advise on a festival that will run across three towns on the
same weekend. Her first instinct is to give three separate forecasts: how gusty each town gets
on a bad day. She works them out and sends them over.

The organiser writes back, and his question is better than her answer. He has to hire
marquees. What he needs to know is this: when Town A is being blown about, is Town B usually
being blown about too, or is it usually calm? Because if the three towns get their rough
weather on different days, he can move marquees between them and hire fewer. If all three blow
at once, he needs three full sets and there is no way around it.

So her real product is not three numbers. It is three numbers **plus a small table of which
towns blow together** — and the marquee bill depends on the table more than it depends on the
three numbers.

She builds the table out of her own past weekends. And immediately she has a second problem,
which is the one that will occupy the rest of the day. Weather is not a fixed fact. The
coastline changes, the new bypass channels wind differently, and the storms of thirty years ago
came off a different Atlantic. So she does not treat every past weekend the same. She lets
recent weekends count for more and old ones fade. How fast to fade them is a judgement, and it
is *her* judgement: fade too fast and the table jumps about from month to month on nothing;
fade too slowly and the table is describing a coastline that no longer exists.

And here is the trap she has to stay out of. Suppose she has a hundred towns instead of three.
The table of which-towns-blow-together grows enormously — every pair needs an entry — while the
number of past weekends she has does not grow at all. Fill the table anyway and it will still
*look* like a table. Every cell will have a number in it. It will just be, in large part, a
record of coincidences.

---

## 2. Mapping the story onto the model, line by line

Go down this table row by row. Do not skip a row because it looks obvious; the skipped row is
where the misconception lives.

| In the story | In the model |
|---|---|
| a town | a factor |
| how gusty one town gets on a bad day | that factor's own volatility |
| **whether two towns blow together** | how two factor returns move together |
| the whole small table | **`F`** — equation (1.8), p.24 |
| the organiser's marquee bill | the portfolio's risk number |
| towns that blow on different days | offsetting factor bets that partly cancel |
| towns that always blow together | factor bets that compound |
| her record of past weekends | the factor-return series **you built at Level 7** |
| letting recent weekends count more | the exponential decay — p.27 |
| how fast to fade the old ones | the **half-life**: BFRE's default is **26 weeks** over **104 weeks** (p.27) |
| fading too fast → the table jumps about | p.27's own words: "unduly noisy so as to render them unstable and unusable" |
| fading too slowly → describing an old coastline | p.27: forecasts "should be responsive to changes in the market environment" |
| a hundred towns and the same few weekends | the boss round, Section 11 |

Two rows in that table are the paper's own sentence and should be read out verbatim, because
the paper states the trade-off better than any paraphrase (p.27):

> "Ultimately, forecasts of factor volatilities and factor correlations should be **responsive**
> to changes in the market environment whilst not being unduly **noisy** so as to render them
> unstable and unusable."

**Where the story breaks — deploy this at tier 4, not at first telling.** Weather covariance is
a stable physical fact about geography: two towns forty miles apart will still be forty miles
apart next year. Factor co-movement is *not* stable, and the paper's entire estimation design
exists to let the estimate change (that is what the half-life is *for*). Worse: a forecaster can
look out of the window and check. Nobody can look at `F`, and p.27 hands the actual method to a
document the reader does not have.

---

## 3. The dataset — Level 7's machinery, run five times

### 3a. The file

Same five names as every level since the cold open. The desk works with a re-standardised
cheapness column, one whose mean is zero — which is exactly what BFRE does to every
characteristic before it reaches a regression (**p.10**, PAPER: "the transformed substyles (and
styles) have the property that their **weighted average is zero**"). Here the weights are equal
rather than square-root-of-market-cap, which is a simplification of ours, flagged in 3d.

Two columns: a column of ones (the **market factor** — p.4, PAPER: "all equity assets have a
unit exposure to this factor") and the centred cheapness column.

| Stock | market `1` | cheapness `x` |
|---|---:|---:|
| AXL | 1 | −2 |
| BRN | 1 | −1 |
| CHR | 1 | 0 |
| DLT | 1 | +1 |
| EMK | 1 | +2 |

Five months of returns, in percent:

| Stock | month 1 | month 2 | month 3 | month 4 | month 5 |
|---|---:|---:|---:|---:|---:|
| AXL | 0 | −3 | +6 | +6 | −8 |
| BRN | +1 | +2 | +3 | +7 | −6 |
| CHR | +9 | +3 | −1 | +1 | −8 |
| DLT | +9 | +10 | −1 | +3 | −4 |
| EMK | +16 | +13 | −2 | −2 | −4 |

### 3b. Why this is one solve and not five (CALL BACK to Levels 3, 4 and 5)

The Level 3 machinery needs the Gram matrix — the three distinct cross-products of the columns
with each other (the fourth is the same as the off-diagonal, read the other way):

```
Σ1·1 = 5        Σ1·x = 0        Σx·x = 10        det = 5 × 10 − 0 × 0 = 50
```

`Σ1·x = 0` **because the column was centred**, and that single zero is the whole reason this
level is hand-computable. Level 4 taught that the off-diagonal `B` is what makes two columns
fight over the same return; here `B = 0`, so there is no fight at all, and the 2×2 system splits
into two independent 1×1 systems. This is Level 4's collision at its opposite extreme.

And **the exposures do not change from month to month in this file**, so the Gram matrix is
computed **once** and reused five times. That is not an accident of the toy — it is a real
property of the estimator: for a fixed `X`, the factor returns are a fixed recipe applied to
whatever returns arrive.

```
f_Mkt(t) = Σr(t) / 5                 ← Level 1's formula on a column of ones
f_Chp(t) = Σx·r(t) / 10              ← Level 1's formula on the cheapness column
```

**INFER, and say so.** That first line is the Level-1/Level-5 result the anchor map flags: with
a column of ones and centred style exposures, the market column's balance condition collapses to
`f_Mkt = weighted average return`, which is exactly what **p.4 footnote 2** asserts ("Average
return based on regression weights"). The paper prints every ingredient and never assembles
them. Here the assembly is visible in one line because `Σ1·x = 0`.

### 3c. Five months, five solves, thirty seconds each

| month | `Σr` | `Σx·r` | `f_Mkt = Σr/5` | `f_Chp = Σxr/10` |
|---|---:|---:|---:|---:|
| 1 | 35 | 40 | **+7.0%** | **+4.0%** |
| 2 | 25 | 40 | **+5.0%** | **+4.0%** |
| 3 | 5 | −20 | **+1.0%** | **−2.0%** |
| 4 | 15 | −20 | **+3.0%** | **−2.0%** |
| 5 | −30 | 10 | **−6.0%** | **+1.0%** |

The misses, month by month (`u = r − f_Mkt·1 − f_Chp·x`), with both Level 2 balance conditions
holding in every column. *This is the object Levels 0–6 wrote as `e`; from here on it is written
`u`, which is the letter the paper uses for it in equation (1.7) on p.24.*

| month | `u` for AXL…EMK | `Σu` | `Σx·u` | `Σu²` |
|---|---|---:|---:|---:|
| 1 | +1, −2, +2, −2, +1 | 0 | 0 | 14 |
| 2 | 0, +1, −2, +1, 0 | 0 | 0 | 6 |
| 3 | +1, 0, −2, 0, +1 | 0 | 0 | 6 |
| 4 | −1, +2, −2, +2, −1 | 0 | 0 | 14 |
| 5 | 0, +1, −2, +1, 0 | 0 | 0 | 6 |

Those five columns of misses total `Σu² = 46` across the file, and they are **Level 9's raw
material, not this level's**. Point at them, name nothing, move on.

**The two rows Level 7 hands to Level 8:**

```
f_Mkt  =  +7,  +5,  +1,  +3,  −6      (percent, month 1 to month 5)
f_Chp  =  +4,  +4,  −2,  −2,  +1
```

### 3d. Three simplifications, declared before they can be mistaken for the model

1. **The exposure column is frozen across the five months.** BFRE re-standardises and reposts
   exposures **weekly, on a Thursday, using data as of the previous Wednesday's close** (p.36,
   PAPER). A moving `X` means the recipe changes every period and the errors in `X` at time `t`
   push straight into `f` at time `t` — which is Level 7's cost, already paid.
2. **Equal weights, not √-market-cap.** BFRE weights by the square root of market capitalisation
   (p.25, PAPER) and defines the standardisation mean with those same weights (p.10, PAPER).
   Nothing on this page depends on the weighting; every formula below takes whatever `f` series
   it is given.
3. **Five months, two factors.** BFRE's default `F` uses **104 weeks** (p.27, PAPER) and a
   factor count that the paper never prints (Section 13c). Five and two are chosen so the
   arithmetic fits on a page.

---

## 4. Building the grid — `F`, by hand

### 4a. The centre of each row, and the wobble around it

A factor's risk is not how big its returns are; it is how much they move about. So the first
move is the one Level 5 already taught — find the centre, and measure from it.

```
mean of f_Mkt  =  (7 + 5 + 1 + 3 − 6)/5   =  10/5  =  +2.0%
mean of f_Chp  =  (4 + 4 − 2 − 2 + 1)/5   =   5/5  =  +1.0%
```

Deviations from those centres:

| month | `d_Mkt` | `d_Chp` |
|---|---:|---:|
| 1 | +5 | +3 |
| 2 | +3 | +3 |
| 3 | −1 | −3 |
| 4 | +1 | −3 |
| 5 | −8 | 0 |
| **sum** | **0** | **0** |

Both columns sum to zero, and they must — that is what subtracting the mean *does*. Which is
also the whole point of the next line.

### 4b. The divisor, and why it is 4 (CALL BACK to Level 6)

Level 6 established the rule: **you divide by the number of numbers minus the number of
parameters you estimated from those same numbers.** Here `T = 5` observations, and we spent one
of them estimating the mean of each series. So the divisor is `T − 1 = 4`.

Say it in the Level 6 words: once four of the five deviations are known, the fifth is forced,
because they have to add to zero. There were never five free numbers; there were four.

Three sums, and that is the entire calculation:

```
Σ d_Mkt²      =  25 +  9 + 1 + 1 + 64   =  100
Σ d_Chp²      =   9 +  9 + 9 + 9 +  0   =   36
Σ d_Mkt·d_Chp =  15 +  9 + 3 − 3 +  0   =   24
```

Divide each by 4:

```
        ┌                ┐
F   =   │   25       6   │        (percent-squared, per month)
        │    6       9   │
        └                ┘
```

**Read the grid out loud, cell by cell, before anything else happens to it:**

- **top-left `25`** — how much the market factor return wobbles, squared.
- **bottom-right `9`** — how much the cheapness factor return wobbles, squared.
- **off-diagonal `6`, appearing twice** — how the two wobble *together*. It appears twice
  because "how A moves with B" and "how B moves with A" are the same sentence read from either
  end. That is why the grid is symmetric, and it is a fact about language, not a modelling
  choice.

### 4c. Volatilities and the correlation

```
factor volatility of the market factor    =  √25  =  5.0%  per month   (exact)
factor volatility of the cheapness factor =  √9   =  3.0%  per month   (exact)
correlation                               =  6 / (5 × 3)  =  6/15  =  2/5  =  0.40  (exact)
```

**This is the first correlation in the game that lives inside `F`, and there is a trap directly
next to it.** Hold this distinction; Levels 4, 8 and 11 all trip on it:

| | Correlation of **exposures** | Correlation of **factor returns** |
|---|---|---|
| what is being correlated | the columns of `X` | the rows of `f` |
| across what | stocks, within one period | periods |
| in this file | the two columns are **orthogonal**: `Σ1·x = 0`, by centering | **0.40** |
| in BFRE | **Figure 1.3, p.11** (Size–Liquidity 0.74) | **Table 1.2's market-correlation column, p.10** (Volatility 0.84) |
| is it part of `F`? | **No** | **Yes** |

In this file the two columns of `X` are **orthogonal** — their cross-product `Σ1·x` is exactly
zero, built that way — and the two factor **returns** are correlated at 0.40. Two factors whose exposures share nothing can
still be paid at the same time. A player who cannot separate those two sentences has not built
`F`.

### 4d. The divisor the paper does not state, and how much it matters

**GAP, and it is real: nowhere in the 65 pages does the paper say whether a mean is subtracted
from the factor returns before the covariance is formed, or what divisor is used.** p.27
describes the window (104 weeks), the weighting (exponential decay), the half-life (26 weeks),
and then defers the rest. So the following is *our* convention, and the player should see what
the alternatives return.

| convention | `Var(f_Mkt)` | `Var(f_Chp)` | `Cov` |
|---|---:|---:|---:|
| subtract the mean, divide by `T − 1 = 4` — **used on this page** | **25** | **9** | **6** |
| subtract the mean, divide by `T = 5` | 20 | 7.2 | 4.8 |
| **no mean subtracted at all**, divide by `T = 5` | 24 | 8.2 | 6.8 |

Row 2 is row 1 multiplied by exactly `4/5` in every cell, so it changes every risk number by the
same factor and no comparison between books changes at all.

Row 3 is a different object and does not scale. Its sums are taken about zero instead of about
the mean: `Σ f_Mkt² = 120`, `Σ f_Chp² = 41` and `Σ f_Mkt·f_Chp = 34`, giving `120/5 = 24`,
`41/5 = 8.2` and `34/5 = 6.8`. Note the variances went **down**
and the covariance went **up** — because it silently asserts that the true average factor return
is zero, and any real average gets counted as wobble. The exact relationship is worth showing,
because it is Level 5's algebra again:

```
no-mean grid  =  (4/5) × F  +  (mean vector) × (mean vector)ᵀ

  24  = (4/5)(25) + (2)(2)        8.2 = (4/5)(9) + (1)(1)        6.8 = (4/5)(6) + (2)(1)
```

Which convention is right depends on whether you believe the average factor return over the
window is information or noise. **Say plainly: the paper does not tell you, so a rebuild of BFRE
has to choose, and the choice is the rebuilder's.** File it for Level 12.

---

## 5. Turning the grid into one number — `hᵀFh`, derived

### 5a. Build the shape before seeing it (round type C)

Give the player only the units and the job:

> *You hold a book with an exposure of `h₁` to the market factor and `h₂` to the cheapness
> factor. You have three numbers: two variances in percent-squared and one co-movement in
> percent-squared. You want one number in percent-squared. What must the formula look like?*

Almost everyone reaches `h₁²·25 + h₂²·9` and stops. Then ask: *does your formula give a different
answer for a book that is long both and a book that is long one and short the other?* It does
not. It must. Let them find the missing term themselves.

### 5b. The derivation, which is one line of school algebra

A book's factor return in month `t` is `p(t) = h₁·f_Mkt(t) + h₂·f_Chp(t)`. Its deviation from its
own mean is the same combination of the deviations:

```
d_p(t) = h₁·d_Mkt(t) + h₂·d_Chp(t)
```

Square it — and this is the *only* step. `(A + B)² = A² + 2AB + B²`:

```
d_p(t)² = h₁²·d_Mkt(t)² + 2·h₁h₂·d_Mkt(t)·d_Chp(t) + h₂²·d_Chp(t)²
```

Add over the five months and divide by 4. Every piece is one of the three sums from 4b:

```
Var(book) = h₁²·25 + 2·h₁h₂·6 + h₂²·9
```

**That is `hᵀFh`.** It is not a definition and not a convention: it is `(A + B)²` and nothing
else. The middle term is doubled for exactly the reason the `2AB` in the identity is doubled.
Name the object *the grid* for now; the notation `hᵀFh` can wait for Level 10.

### 5c. The same number twice, three books over

Every row below is computed **both ways** — once by building the book's own return series and
taking its spread, once from the grid — and the two agree exactly.

**Book A: long both, `h = (1, 1)`.**

```
p        =  11,   9,  −1,   1,  −5        mean = 15/5 = 3
d_p      =   8,   6,  −4,  −2,  −8        Σd_p² = 64+36+16+4+64 = 184
variance =  184/4 = 46
grid     =  25 + 2(6) + 9 = 46            ✓
risk     =  √46 = 6.7823% per month       (rounded)
```

**Book B: long the market, short cheapness, `h = (1, −1)`.**

```
p        =   3,   1,   3,   5,  −7        mean = 5/5 = 1
d_p      =   2,   0,   2,   4,  −8        Σd_p² = 4+0+4+16+64 = 88
variance =  88/4 = 22
grid     =  25 − 2(6) + 9 = 22            ✓
risk     =  √22 = 4.6904% per month       (rounded)
```

**Book C, chosen so the answer is a whole number: `h = (4, 3)`.**

```
p        =  40,  32,  −2,   6, −21        mean = 55/5 = 11
d_p      =  29,  21, −13,  −5, −32        Σd_p² = 841+441+169+25+1024 = 2500
variance =  2500/4 = 625
grid     =  16(25) + 24(6) + 9(9) = 400 + 144 + 81 = 625     ✓
risk     =  √625 = 25% per month exactly
```

**The number that carries the lesson:** Books A and B hold *the same size bet on each factor*.
Their variances differ by `46 − 22 = 24`, which is exactly `4 × 6` — four times the off-diagonal
cell. Delete that cell and both books get the same risk, `√34 = 5.8310%` (rounded) — which is
`√(34/46) = 0.8597` of the truth for Book A and `√(34/22) = 1.2432` times the truth for Book B
(both rounded). One number, wrong in opposite directions on two books.

The verifier sweeps all **169** integer books with exposures from −6 to +6 and confirms that
the series route and the grid route agree in every one.

### 5d. Sabotage round (round type B) — run it before Section 6

Hand the player this grid, said to have come from the same two series, and one entry is
corrupted:

```
        ┌                ┐
F' =    │   25      16   │
        │   16       9   │
        └                ┘
```

**Two structural checks find it in under a minute, and neither needs the original data.**

1. **The correlation check.** `16 / (5 × 3) = 16/15 = 1.0667` (rounded). A correlation above 1
   is impossible: it would say the two series agree more than perfectly.
2. **The negative-variance check, which is the one that generalises.** Take the book
   `h = (3, −5)`:

```
variance = 9(25) + 2(3)(−5)(16) + 25(9) = 225 − 480 + 225 = −30
```

A variance is a sum of squares divided by a positive number. It cannot be negative. **This grid
is not inaccurate; it is impossible** — no series of factor returns whatsoever could have produced it.

Under the true grid the same book is perfectly ordinary: `225 − 180 + 225 = 270`.

The determinant, from Level 4, sees it too: `25(9) − 16² = −31 < 0`, where the true grid gives
`25(9) − 6² = 189 > 0`. Hold that comparison — Section 6 is about to explain what the sign of
that determinant was telling you.

---

## 6. The direction with the most wobble

> **Graduate-level, and outside the paper. Say both.** There is no eigenvalue, eigenvector,
> principal component or PCA anywhere in the 65 pages. This section is a lens the game is
> lending the player, because it is the only honest way to see why a grid can be broken. It is
> not a BFRE mechanism, and a player who tells a quant that BFRE extracts factors from a
> covariance matrix has described a completely different family of model. (BFRE is the opposite
> design: named, interpretable characteristics chosen against four stated criteria on p.4.)

### 6a. The question, and the cheat that has to be blocked first

Section 5 scored three books. Now score every book at once:

> **Which direction of betting wobbles most?**

Asked naively, the question is broken: double every exposure and the variance goes up
four-fold, so there is no largest. `h = (100, 100)` beats `h = (1, 1)` and means nothing.

So fix the *size* of the bet and let only its *direction* vary. Size, here, is
`h₁² + h₂²` — the same sum-of-squares measure the game has used since Level 0 (and, for
the geometrically minded, the squared length of the arrow `(h₁, h₂)`).

**Variance per unit of size:**

```
              h₁²·25 + 2·h₁h₂·6 + h₂²·9
     R(h)  =  ─────────────────────────
                     h₁² + h₂²
```

`R` is unchanged if you scale `h`, so it really is a property of the *direction* and nothing
else. Every value below is an exact fraction — no square roots are needed anywhere in this
section, which is why the whole construction is hand-computable.

*(The industry name for `R` is the **Rayleigh quotient**. It is not in the paper. Use it once,
then go back to "variance per unit of size".)*

### 6b. Try directions and watch it peak (round type A — predict first)

Before any arithmetic, make the player commit: *the market factor is the more volatile of the two
— 5% a month against 3% — and they are positively correlated at 0.40. Which direction wobbles most
— and is it a pure market bet?* Most players say a pure market bet. Write it down.

Sweep directions written as `(p, 1)` — that is, `p` units of market for one unit of cheapness —
plus the pure market direction `(1, 0)`:

| direction `h` | `R(h)` exact | `R(h)` decimal |
|---|---:|---:|
| `(−4, 1)` | 361/17 | 21.2353 (rounded) |
| `(−3, 1)` | 99/5 | 19.8 |
| `(−2, 1)` | 17 | 17 |
| `(−1, 1)` | 11 | 11 |
| `(0, 1)` — pure cheapness | 9 | 9 |
| `(1, 1)` | 23 | 23 |
| `(2, 1)` | 133/5 | 26.6 |
| **`(3, 1)`** | **27** | **27** |
| `(4, 1)` | 457/17 | 26.8824 (rounded) |
| `(1, 0)` — pure market | 25 | 25 |

**The prediction fails, and it fails informatively.** A pure market bet scores 25. Three parts
market to one part cheapness scores **27** — riskier than the riskiest single factor, because
the two factors are positively correlated and the mixture stacks them.

Zoom in around the peak to see that 27 really is the top and not a step on the way up:

| `h` | `(2,1)` | `(5,2)` | **`(3,1)`** | `(7,2)` | `(4,1)` |
|---|---:|---:|---:|---:|---:|
| `R` exact | 133/5 | 781/29 | **27** | 1429/53 | 457/17 |
| decimal | 26.6 | 26.9310 (rounded) | **27** | 26.9623 (rounded) | 26.8824 (rounded) |

And zoom in on the other end, the *calmest* direction:

| `h` | `(−1,1)` | `(−1,2)` | `(−2,5)` | **`(−1,3)`** | `(−1,4)` |
|---|---:|---:|---:|---:|---:|
| `R` exact | 11 | 37/5 | 205/29 | **7** | 121/17 |
| decimal | 11 | 7.4 | 7.0690 (rounded) | **7** | 7.1176 (rounded) |

The quietest direction is **one part cheapness against three parts market, in opposite
directions** — `(1, −3)`, the same line as `(−1, 3)` — and it scores **7**, well below either
factor on its own.

**A free arithmetic check the player should run unprompted.** Take any direction and the
direction at right angles to it. Their two scores always add to `25 + 9 = 34`:

```
R(1,0) + R(0,1) = 25 + 9 = 34            R(2,1) + R(−1,2) = 133/5 + 37/5 = 34
R(1,1) + R(−1,1) = 23 + 11 = 34          R(3,1) + R(−1,3) = 27 + 7 = 34
R(1,3) + R(−3,1) = 71/5 + 99/5 = 34      R(4,1) + R(−1,4) = 457/17 + 121/17 = 34
```

That `34` is the sum of the diagonal, and it is conserved: **whatever the grid does to one
direction, it must undo in the perpendicular one.** So the peak and the trough are two ends of
one fact, not two facts.

### 6c. Now prove it — which scores are reachable at all?

Sweeping is not a proof. Turn the question round, and this is the move that builds an eigenvalue
from nothing:

> **For which numbers `λ` does there exist a direction scoring exactly `λ`?**

Write the direction as `(t, 1)` — every direction except the pure-market one, which we check
separately — and set the score equal to `λ`:

```
   25t² + 12t + 9
   ──────────────  =  λ
      t² + 1
```

Multiply out and gather:

```
   (25 − λ)·t²  +  12·t  +  (9 − λ)  =  0
```

This is a quadratic in `t`. **A direction with score `λ` exists exactly when this quadratic has
a real solution** — which, by the discriminant rule the player has known since Class 10, means

```
   12² − 4(25 − λ)(9 − λ)  ≥  0
```

Expand:

```
   144 − 4(225 − 34λ + λ²)  ≥  0
   36  ≥  225 − 34λ + λ²
   λ² − 34λ + 189  ≤  0
```

Factorise: `189 = 7 × 27` and `7 + 27 = 34`, so

```
   (λ − 7)(λ − 27)  ≤  0        ⟺        7  ≤  λ  ≤  27
```

**Stop and look at what just happened.** The scores a book can achieve are exactly the interval
from 7 to 27, and the two endpoints came out of a quadratic whose coefficients are

```
   λ²  −  (25 + 9)·λ  +  (25×9 − 6×6)  =  λ² − 34λ + 189
        └── the diagonal sum ──┘   └── Level 4's determinant ──┘
```

The sum of the diagonal and the determinant — two numbers the player has been carrying since
Level 4 — are the sum and the product of the two endpoints:

```
   7 + 27 = 34 = 25 + 9              7 × 27 = 189 = 25×9 − 6×6
```

Solved directly, with `a = 25`, `d = 9`, `b = 6`:

```
                (a + d) ± √( (a − d)² + 4b² )        34 ± √(16² + 4·36)       34 ± √400      34 ± 20
   endpoints =  ────────────────────────────    =    ──────────────────   =   ─────────  =   ───────
                            2                                2                    2             2
```

`400` is a perfect square, so both endpoints are whole numbers: **27** and **7**. *(The file was
designed that way. In general the roots are irrational and the whole calculation has to be done
with decimals — say so, so the player does not think rationality is a property of covariance
matrices.)*

Two loose ends, both worth closing out loud because a careful player will find them:

- **The direction we skipped.** `(1, 0)` scores 25, comfortably inside `[7, 27]`. ✓
- **The value `λ = 25`, where the `t²` coefficient vanishes** and the equation is not a quadratic
  at all but the linear `12t − 16 = 0`, i.e. `t = 4/3`. That is still a real solution, so 25 is
  still reachable and the rule survives — and the direction `(4/3, 1)`, which is the direction
  `(4, 3)`, does score exactly `625/25 = 25`. ✓ *(That is Book C from Section 5c, which is why
  its variance was exactly `25 × 25 = 625`.)*

### 6d. The airtight version — two squares, no discriminants

The discriminant argument is complete, but there is a version so short it can be checked on a
napkin, and it also *hands you the winning direction*. Subtract the score from the top of the
band:

```
   27·(h₁² + h₂²)  −  (25h₁² + 12h₁h₂ + 9h₂²)
      =  2h₁² − 12h₁h₂ + 18h₂²
      =  2·(h₁² − 6h₁h₂ + 9h₂²)
      =  2·(h₁ − 3h₂)²                              ← a square, therefore ≥ 0 always
```

So `R(h) ≤ 27` for **every** direction, with equality **only** when `h₁ = 3h₂` — the direction
`(3, 1)`. And at the other end:

```
   (25h₁² + 12h₁h₂ + 9h₂²)  −  7·(h₁² + h₂²)
      =  18h₁² + 12h₁h₂ + 2h₂²
      =  2·(9h₁² + 6h₁h₂ + h₂²)
      =  2·(3h₁ + h₂)²                              ← a square, therefore ≥ 0 always
```

So `R(h) ≥ 7` always, with equality only when `h₂ = −3h₁` — the direction `(1, −3)`.

**That is a complete proof, in six lines, that 27 is the maximum and 7 the minimum, and it names
both winning directions.** The verifier checks the two identities on all **361** integer
directions from −9 to +9.

And the two winning directions are at right angles:

```
   (3, 1)·(1, −3)  =  3 − 3  =  0
```

Which is not a coincidence — it is 6b's conservation law again: the peak direction and the
trough direction have to be perpendicular, because their scores add to 34.

### 6e. The thing nobody tells you first: the grid maps those directions onto themselves

Feed the two winning directions through the grid — that is, take each row of `F` and dot it with
the direction:

```
   F · (3, 1)  =  ( 25(3) + 6(1),  6(3) + 9(1) )  =  ( 81, 27 )  =  27 · (3, 1)
   F · (1, −3) =  ( 25(1) + 6(−3), 6(1) + 9(−3) ) =  ( 7, −21 )  =   7 · (1, −3)
```

**The grid returns the same direction, only stretched.** Every other direction comes out
pointing somewhere else; these two come out pointing exactly where they went in. The stretch
factors are 27 and 7 — the peak and the trough scores.

This was not assumed anywhere. It fell out of "which direction wobbles most". The player has
just built, from a sweep and a discriminant, the equation that most courses open with as a
definition:

```
   F · v  =  λ · v
```

**Now, and only now, hand over the names (Section 6h).**

### 6f. Rebuilding the grid out of its two directions

The two directions are perpendicular, so any book splits cleanly between them. Build the two
"pure direction" grids by multiplying each direction by itself and dividing by its own squared
length (`3² + 1² = 10` for both):

```
          1  ┌         ┐              1  ┌           ┐
   P₁  =  ── │  9    3 │       P₂  =  ── │  1    −3  │
          10 │  3    1 │              10 │ −3     9  │
             └         ┘                 └           ┘
```

Three facts, each checkable in seconds and each worth stating:

```
   P₁ + P₂  =  the identity grid  ┌ 1  0 ┐      (every book splits, nothing is lost)
                                  └ 0  1 ┘

   27·P₁ + 7·P₂  =  ┌ 25   6 ┐  =  F           (the grid IS its two directions and two scores)
                    └  6   9 ┘

   P₁ × P₁ = P₁       and       P₁ × P₂ = the zero grid
```

Check the middle one entry by entry, in exact fractions:

```
   top-left:      (27·9 + 7·1)/10   =  (243 + 7)/10   =  25    ✓
   off-diagonal:  (27·3 − 7·3)/10   =  (81 − 21)/10   =   6    ✓
   bottom-right:  (27·1 + 7·9)/10   =  (27 + 63)/10   =   9    ✓
```

**Everything in `F` is those two directions and those two numbers.** Four cells of information
turned out to be two directions plus two sizes.

### 6g. Splitting a real book between the two directions

Take Book A from 5c, `h = (1, 1)`, whose variance we know is 46.

```
   how much of it lies along (3,1):    (1·3 + 1·1)² / 10  =  16/10  =  8/5
   how much of it lies along (1,−3):   (1·1 − 1·3)² / 10  =   4/10  =  2/5
   the two add to the book's own size:  8/5 + 2/5 = 2 = 1² + 1²     ✓
```

Now score it using only the two scores:

```
   27 × (8/5)  +  7 × (2/5)  =  216/5 + 14/5  =  230/5  =  46      ✓
```

The same 46 as Section 5c, by a completely different route.

**And here is the sentence a risk desk actually says.** By size, the book is **80%** along the
noisy direction. By *variance*, it is `27×(8/5)/46 = 108/115 = 0.9391` (rounded) — **about 94%
of this book's risk lives in one direction**, even though the book was built as an even split
between two factors. Balanced-looking exposures, single-direction risk. That is the whole reason
this section exists, and it is Level 11's opening move.

### 6h. Names, now that the mechanisms exist

| Name | What the player just built |
|---|---|
| **covariance matrix** | the grid: variances down the diagonal, co-movements off it, symmetric because "A with B" and "B with A" are one sentence |
| **factor covariance matrix, `F`** | that grid, built from **factor returns**. p.24, equation (1.8) |
| **eigenvector** | a direction the grid maps back onto itself — `(3,1)` and `(1,−3)` here |
| **eigenvalue** | the stretch factor for that direction, which *is* the variance per unit of size along it — **27** and **7** here |
| **spectrum / eigen-decomposition** | the whole list, and the rebuild `F = 27P₁ + 7P₂` |
| **positive semi-definite** | no eigenvalue is negative — equivalently, no book has negative variance. Section 5d's corrupted grid fails this |
| **positive definite** | stronger: every eigenvalue is strictly positive, so no book has *zero* variance either |
| **condition number** | `λ_max / λ_min = 27/7 = 3.8571` (rounded) — how stretched the grid is, biggest direction against smallest |
| **trace** | the diagonal sum, `25 + 9 = 34` — and it equals `27 + 7`, the eigenvalue sum |
| **determinant** | Level 4's number, `189` — and it equals `27 × 7`, the eigenvalue product |

Two shares worth writing down, because a quant will quote them in this form:

```
   first direction's share of total variance   =  27/34  =  0.7941   (rounded)
   second direction's share                    =   7/34  =  0.2059   (rounded)
```

> **Round type F (vocabulary under fire).** Fire this, deadpan, mid-task: *"The first eigenvalue
> is eating about half the variance — that's just the market showing up in the factor block
> again."* Demand plain English, then a **fresh** sentence of their own.
>
> **The tell to hunt** (`gm/VOCAB.md` §3.12): swapping eigenvalue and eigenvector. The value is
> the *amount*; the vector is the *direction*. Dock bps for "the eigenvalue is the direction".
> Second tell: assuming the model does this. It does not — see the warning box at the top of
> this section.

### 6i. The cliff — what the determinant going to zero looks like now (CALL BACK to Level 4)

Level 4 pushed two columns of `X` together and watched `det = AC − B²` go to zero. Do the same
thing to `F`. Keep the two variances and raise the co-movement from 6 to **15**:

```
        ┌            ┐
F* =    │  25    15  │     correlation = 15/(5×3) = 1 exactly
        │  15     9  │     determinant = 25(9) − 15² = 225 − 225 = 0
        └            ┘
```

Eigenvalues: `(a − d)² + 4b² = 256 + 900 = 1156 = 34²`, so they are `(34 ± 34)/2` = **34 and 0**.

A **zero eigenvalue** means there is a direction along which the grid says there is no wobble at
all. Find it: `F*·h = 0` gives `25h₁ + 15h₂ = 0`, i.e. `h = (3, −5)`. Check both rows:

```
   25(3) + 15(−5) = 75 − 75 = 0        15(3) + 9(−5) = 45 − 45 = 0
   variance = 9(25) + 2(3)(−5)(15) + 25(9) = 225 − 450 + 225 = 0
```

**Three parts market against five parts cheapness has, according to this grid, exactly zero
risk.** Not small. Zero. And of course it does — a correlation of exactly 1 says the two factor
returns are the same series in different units, so one bet can cancel the other perfectly.

That is a preview of the boss round, on two factors, where you can still see everything at once.

---

## 7. What the grid is for, and the three health checks a desk runs on it

Before the boss round, the player should be able to look at any grid and answer three questions
without computing a portfolio at all.

**1. Is it possible?** Every eigenvalue must be `≥ 0`. For a 2×2 this needs no eigenvalues at
all: it is possible exactly when the determinant is `≥ 0` and the diagonal sum is `> 0`. Our
`F`: `189 > 0` and `34 > 0` ✓. The corrupted grid of 5d: `−31 < 0` ✗ — and the failure is
exhibited by an actual book with variance `−30`.

**2. How stretched is it?** `λ_max / λ_min`. Here `27/7 = 3.8571` (rounded), which is mild. A
grid where that ratio is enormous has directions it claims to know a great deal about and
directions it claims to know almost nothing about — and the second kind are the dangerous ones,
because that is where a book looking for cheap risk will end up.

**3. Where does the risk actually live?** The largest eigenvalue's share of the diagonal sum:
here `27/34 = 0.7941` (rounded). One direction, four-fifths of everything.

**The one thing to say about `Σ` and stop.** `F` sits inside equation (1.8) on p.24,
`Σ = XFXᵀ + Δ`. The other two objects in that line are **not this level's**: `Δ` is Level 9 and
the assembly is Level 10. Name their position, open nothing.

### 7a. Teach-back (round type D) — run it here, before the traps

The player explains `F` to **Meera, a portfolio manager of nineteen years' standing who has never
opened a statistics textbook and does not intend to.** She is quick, impatient, and thinks in
positions. Play her, and ask exactly the three questions she would ask:

1. *"I hold the market and I hold cheapness. You have given me one number for each and a third
   number I do not recognise. What does the third one do for me that the first two don't?"*
   — Passing: it is the difference between the `(1,1)` book at `√46 = 6.7823%` and the `(1,−1)`
   book at `√22 = 4.6904%` (both rounded), which have identical bets on each factor.
2. *"Your grid says my quietest possible book is a three-to-one short. Nobody trades that. Why
   should I care about a direction I will never hold?"* — Passing: because the *opposite* end of
   the same calculation is the direction that is riskiest, `(3,1)` at 27, and because anything
   that hunts for cheap risk is a machine for finding the quiet end. Also because Section 6g
   showed her ordinary-looking `(1,1)` book is `0.9391` (rounded) of one direction anyway.
3. *"You built this from five months. I have been doing this for nineteen years. Why would you
   throw away my nineteen years?"* — Passing: BFRE throws away most of its own history too, on
   purpose, and the reason is on p.27 in the paper's own words — responsive versus noisy — with
   the arithmetic in Section 13c: a 26-week half-life leaves 104 weeks worth about 66.

**Grade the explanation, not the vocabulary.** Meera is allowed to reject every technical word.
If the player cannot make the third number matter to her without using "covariance", they have
computed `F` and not understood it.

---

## 8. Traps, and exactly what each wrong belief returns numerically

| Wrong belief | What it returns on this file | Why it is wrong |
|---|---|---|
| "Risk is just the two volatilities" | Book A and Book B both get `√(25+9) = √34 = 5.8310%` (rounded) | Ignores the off-diagonal. Truth: 6.7823% and 4.6904% (both rounded). Their variances are in the ratio `46/22 = 23/11 = 2.0909` (rounded), their risks in the ratio `√(23/11) = 1.4460` (rounded) |
| "Volatilities add" | Book A: `5 + 3 = 8%` | **Variances** combine, never volatilities. Truth 6.7823% (rounded) |
| "Correlation 0.40 is in the grid" | Book A gets `25 + 2(0.4) + 9 = 34.8`, risk `5.8992%` (rounded) instead of 6.7823% (rounded) | Correlation is the covariance *divided by both volatilities*. The grid holds `6`, not `0.4` |
| "Figure 1.3 on p.11 is `F`" | reads Size–Liquidity 0.74 as a factor-return correlation | p.11 is the correlation of **exposures** — columns of `X`. The factor-return correlations are in **Table 1.2, p.10** |
| "Table 1.2's 0.84 is a cell of the shipped `F`" | quotes a full-sample equal-weighted 1996–2013 statistic as a live model input | `F` is 104 weeks with a 26-week half-life (p.27). Same kind of object, different window and different weights |
| "The riskiest direction is the riskiest factor" | says pure market, 25 | The peak is `(3,1)` at **27**, above either factor alone |
| "The eigenvalue is the direction" | — | The eigen**vector** is the direction; the eigen**value** is the amount. This is the single most common failure |
| "A negative eigenvalue just means low risk" | — | It means a book with negative variance — `(3,−5)` at `−30` in 5d. The grid is invalid, not conservative |
| "More history always makes the grid better" | — | Only if the world held still. The half-life exists precisely because it does not (p.27) |
| "Divide by `T`, everyone does" | scales every variance by 4/5 | Level 6's `n − k`: one parameter (the mean) was estimated from the same numbers. And **the paper does not say**, so declare your choice |

---

## 9. Names unlocked at the end of this level

Locked until now on purpose. Each is now attached to something the player built with their own
hands.

| Name | What it actually is, in this level's terms |
|---|---|
| **covariance matrix** | the grid of 4b |
| **factor covariance matrix `F`** | that grid built from factor returns — p.24, eq. (1.8) |
| **variance / covariance of two series** | `Σd²/(T−1)` and `Σd₁d₂/(T−1)` |
| **quadratic form `hᵀFh`** | Section 5b: `(A+B)²`, nothing more |
| **eigenvector** | a direction the grid maps back onto itself |
| **eigenvalue** | variance per unit of size along that direction |
| **spectrum** | the list of eigenvalues |
| **trace** | diagonal sum = eigenvalue sum = 34 |
| **positive semi-definite / positive definite** | no book has negative / no book has zero variance |
| **condition number** | `λ_max/λ_min` |
| **half-life** | how fast old observations fade — **p.27**, BFRE's default is 26 weeks |
| **exponential decay / exponential weighting** | the weighting scheme itself — **p.27** |
| **effective sample size** | Section 13c — how many equally-weighted observations a decayed window is worth |
| **rank** *(boss round)* | how many independent directions the data actually contains |
| **singular / rank-deficient** *(boss round)* | at least one eigenvalue exactly zero |
| **shrinkage** *(boss round)* | pulling a noisy estimate toward a steadier target on purpose |
| **bias–variance trade-off** *(boss round)* | what shrinkage buys and what it pays with |

**Say, as you hand over each of the middle nine:** *this is the industry word for the thing you
just built — the paper never uses it.* Of the seventeen, exactly **three** are the paper's own
words: **half-life** and **exponential decay**, both on p.27, and **factor covariance matrix**,
the where-list entry under equation (1.8) on p.24. Everything else is borrowed.

**Do not unlock here:** *specific risk / `Δ`* (Level 9), *asset covariance matrix `Σ`*
(Level 10), *tracking error* and *marginal contribution to risk* (Level 11), *bias statistic*
(Level 12).

---

## 10. Ladder position after this level

| Concept | Tier to demand |
|---|---|
| building `F` from a factor-return series | **5 (rebuild)** — on a series they have never seen, unprompted |
| `hᵀFh` derived from `(A+B)²` | 4 (defend) — including why the middle term is doubled |
| the `T − 1` divisor, and the fact the paper does not state it | 4 (defend) |
| exposure correlation vs factor-return correlation (p.11 vs p.10) | **4 (defend)** — this is the level's most examinable confusion |
| eigenvalue as "variance per unit of size in the best direction" | 3 (derive) — via the sweep and the two-squares proof |
| eigenvector, and `Fv = λv` as a *consequence* | 3 (derive) |
| trace = eigenvalue sum, determinant = eigenvalue product | 2 (compute) is acceptable |
| a zero eigenvalue = a book scored at exactly zero risk | **4 (defend)** — this is the boss-round gate |
| shrinkage: target, intensity, and what it costs | 3 (derive) at minimum; 4 to pass the boss round |

Do not mark Level 8 complete unless the player can, **unprompted, on a new two-factor series**,
build the grid, find the peak direction by sweeping, and prove the peak is the peak with the
two-squares identity.

---

# 11. BOSS ROUND — The Weather Map

Round type: **E. INTERROGATION**. Play a Chief Risk Officer with thirty years on the desk and no
patience. The task, from the rulebook: *show why a covariance matrix estimated from fewer
periods than factors is structurally broken, and what shrinkage does about it.*

> **Announce the difficulty at the top of the round.** This is graduate material and the paper
> does not go here. Also announce the scope, in these words or close to them: **"the case I am
> about to build is a toy I constructed to make the mechanism visible. It is not what BFRE
> ships. We will do BFRE's actual numbers afterwards, in Section 13c, and they are different."**
> A GM who runs the toy and then says "and that is what BlackRock does" has fabricated.

## 11.1 The setup, as the player receives it

A different desk. **Three** factors, and the covariance was built from **three** months of
factor returns. Every number below is a plain, ordinary-looking factor return in percent.

| month | `g₁` | `g₂` | `g₃` |
|---|---:|---:|---:|
| 1 | +6 | +5 | +9 |
| 2 | +1 | −1 | −2 |
| 3 | −4 | +2 | −4 |

**Predict-then-reveal, before any arithmetic.** Ask: *does anything about this file look
dangerous?* Almost nobody sees it. Write down whatever they say. Then build the grid — which
takes about ninety seconds — and let them look at it.

## 11.2 The grid

Means: `(6+1−4)/3 = 1`, `(5−1+2)/3 = 2`, `(9−2−4)/3 = 1`.

| month | `d₁` | `d₂` | `d₃` |
|---|---:|---:|---:|
| 1 | +5 | +3 | +8 |
| 2 | 0 | −3 | −3 |
| 3 | −5 | 0 | −5 |

Six sums, then divide each by `T − 1 = 2`:

```
Σd₁² = 25 + 0 + 25 = 50        Σd₁d₂ = 15 + 0 + 0 = 15
Σd₂² =  9 + 9 +  0 = 18        Σd₁d₃ = 40 + 0 + 25 = 65
Σd₃² = 64 + 9 + 25 = 98        Σd₂d₃ = 24 + 9 + 0 = 33
```

```
        ┌                        ┐
        │  25.0    7.5    32.5   │
S   =   │   7.5    9.0    16.5   │        (percent-squared, per month)
        │  32.5   16.5    49.0   │
        └                        ┘
```

**Every single entry looks fine.** The three factor volatilities are exactly `√25 = 5%`,
`√9 = 3%` and `√49 = 7%` — respectable, unremarkable monthly numbers. The three correlations
are

```
   ρ₁₂ = 7.5/(5×3)  = 0.5                    (exact)
   ρ₁₃ = 32.5/(5×7) = 13/14 = 0.9286         (rounded)
   ρ₂₃ = 16.5/(3×7) = 11/14 = 0.7857         (rounded)
```

— all inside `[−1, +1]`, so the 5d correlation check passes. Every pair satisfies
`S_ij² ≤ S_ii·S_jj`. **Nothing on the face of this grid is wrong.**

## 11.3 The book the grid scores at exactly zero

Hold `+1` of factor 1, `+1` of factor 2, and `−1` of factor 3: `w = (1, 1, −1)`.

Compute what it actually returned, month by month:

```
   month 1:   +6 + 5 − 9  =  +2%
   month 2:   +1 − 1 + 2  =  +2%
   month 3:   −4 + 2 + 4  =  +2%
```

**+2% every month.** Its mean is +2%, so all three deviations are zero, so its sample variance
is zero. Now get the same answer from the grid, which is what a risk system would do:

```
   variance = 25 + 9 + 49 + 2(7.5) − 2(32.5) − 2(16.5)
            = 83 + 15 − 65 − 33
            = 0
```

Or, faster, multiply the grid by the book directly — every row gives zero:

```
   row 1:   25(1) +  7.5(1) − 32.5(1)  =  0
   row 2:  7.5(1) +  9.0(1) − 16.5(1)  =  0
   row 3: 32.5(1) + 16.5(1) − 49.0(1)  =  0
```

`S·w = 0` with `w ≠ 0` — which, in Section 6e's language, means **`w` is an eigenvector with
eigenvalue exactly 0.** The determinant is 0 too, and you can see why by eye: **row 3 of `S` is
row 1 plus row 2, exactly.**

**Now make the CRO say it out loud, because this is the whole boss round:**

- The model reports this book's risk as **0.00%**. Not "small". Zero.
- Multiply the book by 100 — hold `+100, +100, −100`. The reported risk is **still exactly
  zero**, because scaling a zero is a zero. Meanwhile the thing actually moved **200 basis
  points every single month**.
- So the model has certified an **unlimited** position in a book that demonstrably moves. Any
  risk budget, any optimiser, any leverage limit expressed in forecast risk is now unbounded in
  this direction.

**That is what "structurally broken" means, and it is why it is not the same as "imprecise".**
An imprecise number is 4% when the truth is 6%. This is a *hole*: a direction the estimate has
no opinion about at all, reported as certainty.

## 11.4 Why it had to be there — the counting argument (CALL BACK to Level 6)

The player must be able to predict the hole before finding it. Three steps:

**Step 1 — the deviations, not the returns, are what the grid is built from.** Every deviation
column sums to zero, by construction. So the three deviation columns all live inside the set of
month-triples that sum to zero — and that set has only **two** independent directions, not
three.

**Step 2 — the mean cost one, exactly as at Level 6.** `T = 3` months, one mean estimated per
series, `T − 1 = 2` independent directions of variation. That is the *same* subtraction the
player made when they divided by `n − k`. The rulebook's CALL BACK rule applies: say it out
loud, and say it in these words — *"the mean cost you a degree of freedom at Level 6 and it
costs you a dimension here; it is one fact wearing two coats."*

**Step 3 — the count.**

```
   independent directions in the data:   T − 1  =  2
   directions the grid claims to score:  K      =  3
   directions with nothing behind them:  K − (T − 1)  =  1
```

**At least `K − (T − 1)` eigenvalues are exactly zero, and each zero eigenvalue is a real,
non-zero, leverable book the model scores at zero risk.** That is the general statement, and it
needs no properties of the numbers whatsoever.

The verifier hammers this: it builds the grid for **all 19,683** three-factor three-month
datasets whose nine entries lie in `{−1, 0, +1}`, and **every single one is singular.** Not
"usually". Always. The data cannot avoid it.

**And now the sharpest version of the point, which the player must be able to state:** you could
give this desk perfect data, perfect execution, a perfect estimator and infinite care, and the
hole would still be there. It is not an error. It is arithmetic.

### 11.4a The mean is genuinely what does it — a check that isolates the culprit

Skip the mean subtraction and build the raw second-moment grid instead
(`Σg_i·g_j / T`, `T = 3`):

```
Σg₁²  = 36 + 1 + 16  = 53          Σg₁g₂ = 30 − 1 −  8 = 21
Σg₂²  = 25 + 1 +  4  = 30          Σg₁g₃ = 54 − 2 + 16 = 68
Σg₃²  = 81 + 4 + 16  = 101         Σg₂g₃ = 45 + 2 −  8 = 39
```

The determinant of the three-by-three table of raw monthly returns is **90**, not zero, and the
second-moment grid's determinant is `90²/27 = 300 > 0`. Under that convention the offending book
scores `w·(second moment)·w = 4`, not 0.

**Do not let the player take the wrong lesson.** This does *not* fix anything. `T = K` with no
mean subtracted is Level 6's `n = k` all over again: the grid is exactly determined, with zero
spare information and no way to check itself. All that changed is which disease is visible.
It does establish the causal claim precisely: **the missing dimension is bought by the mean.**

## 11.5 What it does on a real desk — INFER, flag it

**This paragraph is the game's inference, not the paper's.** BFRE never discusses rank, an
optimiser, or a portfolio search.

A hole is not dangerous while nobody looks for it. Something always does. Any process that
searches for low forecast risk — an optimiser, a risk-budgeting screen, a leverage rule, a PM
hunting for a cheap hedge — is precisely a machine for finding the smallest eigenvalue and
loading it. The directions the estimate knows least about are exactly the ones such a process
selects. So the error is not random across books: **it concentrates on the books that get
built.** That is why "on average the estimate is fine" is no defence at all.

## 11.6 What shrinkage does about it

The disease is that the estimate believes the three months it saw *completely*. So do not use
the estimate alone. Mix it with something that could not possibly have a hole:

```
   F_shrunk  =  (1 − a)·S  +  a·Prior
```

*(The target is written `Prior`, not `T`, purely because `T` already means the number of periods
on this page — and because "prior" is the paper's own word for the same idea on p.36.)*

- **`Prior` is the target** — the steadier thing you are pulling toward. Here: **keep the three
  variances, throw the correlations away** — `Prior = diag(25, 9, 49)`. It is the honest choice
  when you trust your volatility estimates more than your co-movement estimates, which with
  three months you very much should.
- **`a` is the intensity**, between 0 and 1. Take **`a = 1/4`**: three parts data, one part
  target.

The arithmetic is two lines. Diagonal entries are the same in both grids, so they do not move.
Every off-diagonal entry is multiplied by `1 − a = 3/4`:

```
        ┌                              ┐
        │  25.0     5.625    24.375    │
F_sh =  │   5.625   9.0      12.375    │        a = 1/4
        │  24.375  12.375    49.0      │
        └                              ┘
```

```
   7.5  × 3/4 = 45/8  = 5.625            correlations, all × 3/4:
   32.5 × 3/4 = 195/8 = 24.375              ρ₁₂: 0.5 → 3/8 = 0.375            (exact)
   16.5 × 3/4 = 99/8  = 12.375              ρ₁₃: → 39/56 = 0.6964             (rounded)
                                            ρ₂₃: → 33/56 = 0.5893             (rounded)
```

**Now re-score the book that had zero risk:**

```
   variance = 25 + 9 + 49 + 2(5.625) − 2(24.375) − 2(12.375)
            = 83 + 11.25 − 48.75 − 24.75
            = 20.75            =  83/4          exactly
   risk     = √20.75 = 4.5552%  per month       (rounded)
```

**From exactly 0.00% to 4.5552%.** And the general form is one line, which the player should be
made to derive:

```
   wᵀ F_shrunk w  =  (1−a)·(wᵀSw)  +  a·(wᵀ Prior w)  =  (1−a)·0  +  a·83  =  83a
```

The hole's variance is `83a` for *any* intensity. **Any** positive `a` closes it. `a` controls
how far, not whether.

### 11.6a The proof that no hole is left anywhere — not just at this book

Showing one book got rescued proves nothing about the others. Here is the complete argument, and
it needs no eigenvalues:

```
   hᵀ F_shrunk h  =  (3/4)·hᵀSh  +  (1/4)·(25h₁² + 9h₂² + 49h₃²)
```

- The first term is `(3/4)` times a sum of squared monthly deviations divided by 2 — **never
  negative**, whatever `h` is. That is Section 5b's derivation, run backwards.
- The second term is at least `(1/4)·9·(h₁² + h₂² + h₃²)`, because 9 is the smallest of the three
  diagonal entries.

So for every non-zero book:

```
   variance per unit of size  ≥  9/4  =  2.25          (exact)
   risk per unit of size      ≥  √2.25  =  1.5%        (exact)
```

**No direction can be scored below 2.25 any more.** The smallest eigenvalue has been lifted off
zero and a floor put under it, and the floor is `a × (smallest variance)` — which the player can
now compute for any `a` without touching an eigenvalue. The determinant, which was exactly 0,
is now `945225/256 = 3692.28515625` (exact). The verifier confirms the floor holds on all
**728** non-zero integer books with exposures from −4 to +4.

### 11.6b Shrinkage is not "making the numbers smaller" — the definitional test

This is the tell that catches nearly everyone (`gm/VOCAB.md` §3.11). Shrinkage moves an estimate
**toward a target**. Which direction any particular number goes depends entirely on which side
of the target it started. On this grid, with the same single `a = 1/4`:

| book | sample risk | after shrinkage | direction |
|---|---:|---:|---|
| `(1, 1, −1)` — the hole | **0%** exactly | **4.5552%** (rounded) | **up**, from nothing to something |
| `(1, −1, 0)` | `√19 = 4.3589%` (rounded) | `√22.75 = 4.7697%` (rounded) | **up** |
| `(1, 1, 0)` | `√49 = 7%` exactly | `√45.25 = 6.7268%` (rounded) | **down** |
| `(1, 0, 0)` — factor 1 alone | `√25 = 5%` exactly | `5%` exactly | **unchanged** |

One `a`. One target. Three different directions of travel and one no-change. Any player who says
"shrinkage makes the risk numbers smaller" is now looking at a row where it made one bigger and
a row where it made one smaller, and they cannot explain either without saying the word
*target*.

*(Why those directions: shrinking the off-diagonals toward zero **reduces** the risk of a book
whose factor bets reinforce each other, and **raises** the risk of a book whose bets were
cancelling. The cancelling books are exactly the ones the sample was most optimistic about.
That is not an accident of this example — it is the mechanism.)*

## 11.7 The same thing where the eigenvalues can be watched — back to the 2×2

The three-factor grid makes the *hole* visible. The two-factor grid of Section 4 makes the
*eigenvalues* visible, exactly, in fractions. Run shrinkage on it with a target of the same
shape a textbook uses: **the average variance, with no correlation at all**.

```
   average variance  =  (25 + 9)/2  =  17      Prior = ┌ 17   0 ┐
                                                       └  0  17 ┘

   F(a)  =  (1 − a)·F  +  a·Prior
```

This target is chosen for a reason worth stating: it leaves the eigen**vectors** exactly where
they were and moves only the eigen**values**. The direction of most wobble is still `(3, 1)` at
every intensity; only its size changes.

| `a` | the grid | eigenvalues | spread | determinant |
|---|---|---|---:|---:|
| 0 | `[[25, 6], [6, 9]]` | **27, 7** | 20 | 189 |
| 1/4 | `[[23, 4.5], [4.5, 11]]` | **24.5, 9.5** | 15 | 232.75 |
| 1/2 | `[[21, 3], [3, 13]]` | **22, 12** | 10 | 264 |
| 3/4 | `[[19, 1.5], [1.5, 15]]` | **19.5, 14.5** | 5 | 282.75 |
| 1 | `[[17, 0], [0, 17]]` | **17, 17** | 0 | 289 |

Check the `a = 1/2` row by hand, the long way, so nothing is taken on trust:

```
   grid:          (25+17)/2 = 21     (9+17)/2 = 13     6/2 = 3
   discriminant:  (21 − 13)² + 4(3²)  =  64 + 36  =  100      → √100 = 10
   eigenvalues:   (21 + 13 ± 10)/2   =  (34 ± 10)/2  =  22 and 12
   eigenvectors:  F(½)·(3,1)  = (63+3, 9+13) = (66, 22) = 22·(3,1)    ✓ unmoved
                  F(½)·(1,−3) = (21−9, 3−39) = (12, −36) = 12·(1,−3)  ✓ unmoved
```

**Read the table as one sentence:** shrinkage takes the biggest eigenvalue **down** and the
smallest **up**, keeps the diagonal sum fixed at 34 throughout, and drives the condition number
from `27/7 = 3.8571` (rounded) toward 1 — at `a = 1/2` it is `22/12 = 11/6 = 1.8333` (rounded).
Along the noisiest direction the risk falls from `√27 = 5.1962%` to `√22 = 4.6904%`; along the
quietest it rises from `√7 = 2.6458%` to `√12 = 3.4641%` (all rounded).

**Extremes toward the middle, in both directions at once.** That is what shrinkage *is*, and
this table is the cleanest statement of it in the whole game.

## 11.8 What shrinkage costs — a number, not an adjective

A player who says shrinkage "makes the estimate better" has memorised something. Make them price
it. The 2×2 file is the one place where the *truth* is known, because Section 5c computed Book
C's variance from the series directly: **625**, exactly.

```
   Book C = (4, 3)      true variance (from the five months)   =  625     risk = 25%
                        under the a = ½ grid                   =  525     risk = √525 = 22.9129%  (rounded)
                        moved by                                  100     =  4/25  =  16% of it
```

Shrinkage put a **16% error into a number that was previously exactly right**, in exchange for
closing holes elsewhere. That is the trade, stated with a number:

> **You buy a reduction in how wildly the estimate would jump around on fresh data, and you pay
> in being wrong on purpose. Bias for variance.**

And the intensity `a` is the price dial. `a = 0` is the raw sample: unbiased, holed. `a = 1` is
the target: no holes, and it has thrown away every correlation the data contained. **Nothing in
the mathematics tells you where to sit between them.** Choosing `a` is a modelling judgement,
exactly like choosing a half-life — and the player should say so before the CRO says it for them.

## 11.9 Names unlocked by the boss round

| Name | Built where |
|---|---|
| **rank** | 11.4 — how many independent directions the data actually contains |
| **rank-deficient / singular / degenerate** | 11.3 — at least one eigenvalue exactly zero. *None of these three words is in the paper. Prefer plain English at the table: "there are directions the data has never seen."* |
| **null direction** | the book scored at exactly zero |
| **shrinkage** | 11.6 |
| **shrinkage target** | the steadier thing you pull toward — here `diag(S)`, and in 11.7 `17·I` |
| **shrinkage intensity** | `a` |
| **bias–variance trade-off** | 11.8, priced at 16% |
| **Bayesian prior** | the target, said the other way round: what you believed before you saw three months of data. **The paper's own phrase — p.36** |
| **regularisation** | the family name for adding structure to fix an under-determined estimate |

## 11.10 The trap good players fall into — have this ready

The strong player, having enjoyed 11.3, will say: **"and that is what is wrong with BFRE's
factor covariance matrix."**

**Stop them. It is false, and it is exactly the kind of confident falsehood that fails Victory
Condition 2 in the first thirty seconds of a real conversation.** BFRE's default uses **104
weeks** of factor returns (p.27, PAPER), and NAMR's factor count assembles from the paper's own
printed tables to roughly **71** (Section 13c, INFER). `71 < 103`, so the literal counting
argument of 11.4 **does not bite** for NAMR: that grid is generically full rank with no zero
eigenvalues at all.

Do not reward the answer. Correct it, hand them Section 13c, and make them re-make the argument
in the form that survives. The rulebook's rule — NEVER ACCEPT A RIGHT ANSWER WITH WRONG
REASONING — applies to the GM as much as to the player here.

The second trap: *"so BFRE shrinks `F`."* **The paper never says that.** See 13f.

## 11.11 The interrogation script (real objections, escalating)

Play them in this order. Each has a passing answer and a hand-waving answer.

**1. "Every number in your matrix is sensible. Volatilities of five, three and seven, correlations
between a half and 0.93. Where exactly is the defect?"**
*Passing:* not in any entry — in the *relationship between the rows*. Row 3 is row 1 plus row 2
exactly, so the grid has three rows but only two independent ones, and the missing one shows up
as a real book, `(+1, +1, −1)`, scored at exactly zero. Produce the book and its three monthly
returns of `+2%`.
*Hand-waving:* "three months isn't enough data." True, evasive, and it does not say what breaks.

**2. "Fine. So it is unlucky data. Give me different data and the problem goes away."**
*Passing:* it cannot. `K − (T − 1) = 1` is a count, not a coincidence: every possible
three-factor three-month dataset gives a singular grid, and the verifier checks 19,683 of them.
The mean subtraction is what costs the dimension, and it is the same subtraction as Level 6's
`n − k`.
*Hand-waving:* "you'd need to be careful with the estimation."

**3. "Suppose I never look at that book. Why do I care?"**
*Passing:* because something on the desk *does* look — any optimiser or low-risk screen is a
machine for finding the smallest direction and loading it. Flag it as INFER: the paper says
nothing about optimisers. Then the leverage point: the reported risk of that book is zero at
*every* scale, so no risk-based limit binds it, while it moved 200bp a month.
*Hand-waving:* "in practice it wouldn't come up."

**4. "Then shrink it. Towards what, by how much, and what does it cost me?"**
*Passing:* names all three. Target: `diag(S)` — keep the variances, disbelieve the correlations
(or the average-variance identity of 11.7). Intensity: `a`, and the hole's variance becomes
exactly `83a` so any positive `a` closes it. Cost: bias — 16% on Book C in 11.8, a number that
was previously exactly right. And the honest closing line: nothing in the mathematics picks `a`.
*Hand-waving:* "shrinkage makes it stable." "You'd use Ledoit–Wolf." (Not in this paper — say so
if you use the name at all.)

**5. "You have been describing my model for ten minutes. Does BFRE actually have this problem?"**
*Passing:* **no — not the literal one, and the player must concede it before being pushed.** 104
weeks (p.27) against a NAMR count that assembles to ≈71 from Table 1.2 and Table 1.5 (INFER),
so no zero eigenvalues. Then the two arguments that *do* survive, both flagged as ours: the
26-week half-life reduces 104 observations to an effective **≈66** (13c), which is *below* the
factor count; and the paper prints no factor count, no condition number, no smallest eigenvalue
and no shrinkage of `F`, deferring the entire method to a document the reader does not have
(p.27). The claim that survives contact is **not** "the matrix is broken" but *"the document
does not contain what a reader would need to rule it out."*
*Hand-waving:* asserting BFRE ships a singular matrix. That is an automatic fail — it is
checkable, it is wrong, and a CRO with a calculator will end the conversation there.

## 11.12 Pass conditions

All five, or the level is not passed and the player does not make Researcher:

1. Produces the zero-risk book **and** its actual monthly returns, unprompted.
2. Explains the hole with the count `K − (T − 1)`, and connects the `−1` to Level 6's mean.
3. States what a zero eigenvalue *means operationally* — unbounded leverage under a risk limit —
   rather than restating the definition.
4. Names target, intensity and price for shrinkage, and gets the direction right: shrinkage
   moves numbers **toward the target**, up or down.
5. **Refuses** to say BFRE's `F` is singular, and can give the effective-sample argument instead
   with the 104 and the 26 attributed to p.27 and the ≈66 and ≈71 attributed to us.

---

## 12. What this level does NOT settle, stated so the player is not misled

- **How to choose the half-life.** p.27 says the value "is primarily driven by the target
  horizon, but can also reflect issues relating to forecast accuracy and stability", and gives
  the default. It gives no procedure, no criterion and no test.
- **How to choose the shrinkage intensity.** The literature has answers (they are named after
  people); the paper has none, because the paper does not shrink `F` at all.
- **Whether `F` should be exponentially weighted at all.** BFRE says yes (p.27). This page built
  an unweighted grid because five equally-weighted months is what fits on a page. **The weighted
  version is the same arithmetic with `w_t` inside every sum** — the machinery from Level 1's
  weighted dial — and Section 13c computes what BFRE's own weights do to its sample size.
- **Whether a mean should be subtracted.** Section 4d: not stated anywhere in the paper.
- **Anything about `Δ` or `Σ`.** Levels 9 and 10.
- **What the eigenvalues of a real `F` look like.** Nobody outside BlackRock knows, because no
  eigenvalue, condition number or rank diagnostic is printed anywhere in the 65 pages.

---

## 13. Back to BFRE — what this machinery does in the real model

### 13a. p.24 — where `F` lives

Equation (1.8), printed one line after (1.7):

```
   Σ  =  X F Xᵀ  +  Δ
```

and the where-list under it, verbatim (PAPER):

> `Σ` : asset covariance matrix
> **`F` : factor covariance matrix**
> `Δ` : specific risk matrix (a diagonal matrix of asset specific risk forecasts)

Note the lead-in sentence, because Level 9 turns on it: "**In general a multi-factor model**
decomposes asset returns as follows". That is the generic form, not BFRE's shipped object. Do
not open it here.

The grid the player built in Section 4 **is** the letter `F` in that line. Everything else on
this page is about how to fill it and how to tell when it is broken.

### 13b. p.27 — how BFRE actually fills it

Four sentences, all PAPER, all on one page:

> "The BFRE factor covariance matrices use a history of **daily** factor return series starting
> in **March 1996**. Observations are weighted using an **exponential decay** that places more
> emphasis on recent factor returns to give more responsive risk forecasts."

> "The responsiveness is controlled through the **half-life** of the exponential decay. The value
> of the half-life is primarily driven by the target horizon…"

> "The default factor covariance matrix calculation for all BFRE models is **WKL (weekly
> long-term)**, which uses **104 weeks** of factor returns with a **half-life of 26 weeks**."

> "Model users are referred to the **BRS Covariance Matrix Estimation documentation** for
> technical details on the factor covariance matrix methodology."

**Make the player notice the discard before you explain it.** The history available starts in
March 1996 — eighteen years of daily data by the paper's own 2013-ending samples. The default
recipe uses **104 weeks**, exponentially decayed. Those are not the same number and the paper
never remarks on the gap. A GM who says "`F` is built from eighteen years of data" has said
something false about the shipped default and has thrown away the boss round: the entire point
is that they *had* nine hundred-odd weeks and chose to use 104 of them, down-weighted, because
of the responsive-versus-noisy trade-off p.27 states in its own words.

Also on p.27 and p.3: the matrices are built "**correcting for serial correlations**", and
Aladdin's Portfolio Risk Tools lets a user "change the half-life of the exponential decay,
control for serial correlations and asynchronicity in the factor return series, and apply
different assumptions to factor volatilities and factor correlations". **The correction's form is
not given.**

### 13c. What BFRE's own half-life does to its own sample — arithmetic, and it is ours

> **INFER, every line of it.** The 104 weeks and the 26-week half-life are the paper's (p.27).
> The effective sample size, the factor count and the ratio are the game's. The paper prints no
> factor count, no effective sample size and no eigenvalue of anything.

**The weights.** A 26-week half-life means the weight halves every 26 weeks: the observation `t`
weeks back carries `λᵗ` with `λ = 0.5^(1/26) = 0.973693` (rounded). Over a 104-week window the
oldest observation sits 103 weeks from the newest, so it carries

```
   λ¹⁰³  =  0.064189   (rounded)   =  6.42% of the newest week's weight
```

— **about one sixteenth, and say "about".** Exactly one sixteenth would be `λ¹⁰⁴`, i.e. a
104-week *separation*, not a 104-observation *window*. That one-off-by-one is the kind of detail
a CRO checks.

**The effective sample size.** The standard measure of "how many equally-weighted observations is
this decayed window worth" is `(Σw)² / Σw²`. Both sums are geometric series, and because 104
weeks is exactly four half-lives they collapse to something a student can evaluate:

```
   Σw   =  (1 − λ¹⁰⁴)/(1 − λ)   =  (1 − 1/16)/(1 − λ)      since λ¹⁰⁴ = 2⁻⁴ exactly
   Σw²  =  (1 − λ²⁰⁸)/(1 − λ²)  =  (1 − 1/256)/(1 − λ²)    since λ²⁰⁸ = 2⁻⁸ exactly

                 (1 − 2⁻⁴)     1 + λ        15    1 + λ
   N_eff   =   ───────────  ×  ─────    =   ──  × ─────    =   66.1982   (rounded)
                 (1 + 2⁻⁴)     1 − λ        17    1 − λ
```

**`N_eff ≈ 66`, not 104.** The paper's own half-life throws away just over a third of its own
window.

Run the same calculation on the *other* set of parameters the paper prints — Table 1.3, p.28,
the **daily** specific-risk model: half-life **125 days**, **375** observations, which is exactly
three half-lives:

```
                 (1 − 2⁻³)     1 + λ         7    1 + λ
   N_eff   =   ───────────  ×  ─────    =   ── × ─────   =  280.5248  ≈ 281  of 375   (rounded)
                 (1 + 2⁻³)     1 − λ         9    1 − λ
```

**≈ 281 of 375 is a gentle decay; ≈ 66 of 104 is an aggressive one.** Both are the paper's own
numbers. The contrast is worth showing, because it demonstrates the GM is doing arithmetic rather
than complaining.

**Now the factor count — assembled from printed rows, because the paper prints no total.**

| block | NAMR | where it comes from |
|---|---:|---|
| market | 1 | p.4 — every asset has unit exposure |
| styles | 12 | Table 1.2, p.10 — 13 rows, Market plus 12 |
| core industries | 53 or 54 | Table 1.5, p.57 — **54 rows, counted by the transcriber; the page prints no total.** p.25 says Core Industry factors "include all industries **except** the Multi-Sector Holding industry", and FINMULTSEC is one of the 54 rows — so the schema is 54 and the core block is 53 |
| core countries | ~2 | US and Canada (p.4 names Canadian stocks) |
| currencies | ~2 | p.6, one-to-one with countries |
| **total** | **≈ 70–71** | `1 + 12 + 53 + 2 + 2 = 70`; with all 54 industry rows, 71 |

**Say "counted from the printed rows", never "the paper says 54".** And say the count is a floor.

**Put the two together, and get the conclusion right — the tempting version is false:**

- `K ≈ 71` against `T = 104` — and, doing 11.4's counting properly, against the `T − 1 = 103`
  independent directions that survive a mean subtraction. **103 > 71, so the sample grid is
  generically full rank, with no zero eigenvalues at all.** BFRE does **not** ship the boss
  round's disease. Anyone who says it does will be caught by a player with a calculator.
- But `K ≈ 71` against `N_eff ≈ 66`. **The effective count is below the factor count.** The
  estimator carries roughly the precision of 66 observations while trying to resolve 71
  directions — and it is the paper's own half-life that puts it there.
- And even at full weight the grid is thinly determined: `71 × 72 / 2 = 2,556` distinct entries
  from `104 × 71 = 7,384` numbers — `7,384/2,556 = 2.8889` (rounded) observations per estimated
  entry, and `66 × 71 / 2,556 = 1.8333` (rounded) on the effective count.

**And the arithmetic trap inside that last bullet, which the GM must not fall into either.**
"104 observations cannot determine 2,556 quantities, therefore the matrix is rank-deficient" is
**wrong**. Rank is decided by `T` against `K`, never by `T` against `K(K+1)/2`. The
observations-per-parameter ratio is a statement about *precision*, not about rank. Correct a
player who conflates them, even though they reached the conclusion you wanted.

**Where the literal rank argument does plausibly bite: the World model.** WRLD covers "the
superset of all assets in the regional and country models" (p.3), and BFRE's asset coverage spans
**87 countries** (p.3). p.5: "Every asset is assigned a unit exposure to a single country
factor"; p.6: currency exposures follow "a **one-to-one mapping** between countries and their
principal traded currency". Add an industry schema (Table 1.11, p.61 — **49 rows, the
transcriber's count; the page prints no total**) and a style block, against the **same 104-week
WKL default** (p.27, which states WKL is the default "for all BFRE models") and **weekly**
regressions (p.24). A country block and a currency block spanning that coverage, plus industries
and styles, cannot plausibly sit below 104. **But the paper never prints the count**, so this is
an inference about an unprinted number — say "it follows that", never "the paper says". And note
that the absence *is itself the finding*.

### 13d. A real slice of `F`, and the thing that is not `F`

**Table 1.2, p.10, the "Correlation with Market Factor" column — these are genuine `F` content,
printed digits, NAMR, Mar 1996 – Dec 2013:**

| factor | correlation with the market factor |
|---|---:|
| Volatility | **0.84** |
| Liquidity | **0.69** |
| Size | **0.23** |
| Momentum | **−0.02** |
| Reversal | **−0.32** |

These are correlations **between factor returns**, which is exactly what Section 4c built. Two
warnings, both of which a CRO will test:

1. **Figure 1.3 on p.11 is not this object.** It is the correlation of **exposures** — the
   columns of `X` — where Size–Liquidity is 0.74 and Earnings Yield–Profitability 0.64 (printed
   digits; Figure 1.3 is one of only four exhibits in the paper that prints its values). Same
   word, different object. Section 4c's table exists to keep them apart.
2. **Table 1.2 is the right kind of object but is still not a cell of the shipped `F`.** It is a
   full-sample, equally-weighted summary over Mar 1996 – Dec 2013. `F` is 104 weeks with a
   26-week half-life. Same species, different animal.

**If a player asks what a covariance cell would look like — INFER, and label it.** Table 1.2 also
prints annualised volatilities: Volatility **7.5%**, Market **19.8%**. Multiplying,
`0.84 × 7.5 × 19.8 = 124.74` percent-squared per year. That is the arithmetic of Section 4c run
backwards, and it is *our* multiplication of three printed numbers, at an annual horizon, not a
figure the paper prints and not a cell of the shipped weekly matrix.

### 13e. p.30 — the one pre-treatment the paper does specify

> "Currency factor returns are **truncated to remove outliers** prior to the estimation of the
> factor covariance matrix. Daily currency returns are bounded by **+/- 8%**, and weekly currency
> returns are bounded by **+/- 20%**." (PAPER)

This is the story's freak storm, handled by hand. **INFER on the direction:** clipping the tails
of a return series before squaring it lowers the estimated variance of that factor relative to
the untruncated series; the paper states the rule and not its effect. It applies to **currency
factors only** — the paper specifies no equivalent treatment for style, industry or country
factor returns.

p.30 also lists, under "MODEL ASSUMPTIONS & LIMITATIONS", the sentence that will matter at Level
10: "Factor returns have **zero correlation with asset specific returns**". That assumption is
what lets the two halves of (1.8) be added without a cross-term.

### 13f. p.36 — the paper's only shrinkage, and it is not of `F`

The word *shrinkage* appears in the 65 pages **only inside a bibliography title** — reference
[7], p.64, Tibshirani, "Regression **shrinkage** and selection via the lasso" — for a method
p.8 names among alternatives BFRE did **not** adopt.

The paper's one shrinkage-shaped device is on p.36, and it is somewhere a textbook would not put
it (PAPER):

> "The estimation procedure uses **thinness corrections for country and industry factors** where
> limited, or no data exists to reliably estimate those factor returns. We impose the thin
> country/industry correction by **adding a Bayesian prior**, which in essence **diverts the
> estimated country/industry return away from the sample factor return and towards a theoretical
> prior**."

Three things about it, and the player must be able to say all three:

1. It shrinks a **factor return** — a single number, per factor, per period — **not the
   covariance matrix**. Different object, different stage of the pipeline.
2. **The prior's form, strength and shrinkage parameter are not specified anywhere.** There is no
   number to trace, and under NO NUMBER WITHOUT ITS ORIGIN there is therefore nothing to teach
   from it except the mechanism, which is Section 11.6's with both the intensity `a` and the
   `Prior` left unstated.
3. Its *reason* is the boss round's reason wearing different clothes: with only a handful of
   assets in a country, the "country factor return" is mostly a few stocks' own returns
   misattributed. Too little data, an estimate that is mostly noise, a prior imposed to stop the
   noise being read as signal.

**p.8 — shrinkage's family, named and declined** (PAPER): Bayesian priors (Kadane and Lazar [6]),
**LASSO** (Tibshirani [7]), **LARS** (Efron [8]), **Group Lasso / Group LARS** (Yuan and Lin [9])
and **Ridge**, all named as alternatives for factor selection and rejected because they "are
purely statistical in nature and rely heavily on historical data". A player who says "BFRE uses
Ridge on the covariance matrix" has inverted the paper twice over.

**The honest headline:** *BFRE does not state anywhere that it shrinks the factor covariance
matrix.* If a rebuild shrinks `F`, that is the rebuilder's decision and must be declared as one.

### 13g. Newey–West — exactly where it is, and exactly where it is not

This one has already been got wrong once in this repository, so state it precisely.

**Newey–West [26] appears in three places and no others:** **p.27**, in the **Specific Risk**
subsection — "the **Newey-West [26]** methodology is used to aggregate daily specific returns to
form specific risk forecasts that account for serial correlations in the daily data"; **p.28**,
in Table 1.3's **Newey-West Lag** column (10 days for the daily model, 2 weeks for the weekly),
plus the sentence "…West serial correlation adjustment" running over from p.27; and the
**bibliography, p.65**.

- It is used for the **specific-risk** side, on the aggregation of daily specific returns.
- It is **never** named in connection with the factor covariance matrix. p.3 and p.27 do say the
  factor covariance matrices are built "correcting for serial correlations" and that PRT lets a
  user "control for serial correlations", but **no method is named for that correction**.
- It is **not** on p.38. An earlier draft of the anchor map cited p.38 and was wrong.
- It is **not** presented as the source of any t-statistic anywhere.

Since the player will ask what it *is*: Newey–West is a way of computing a variance for something
built out of overlapping or serially-correlated observations, by adding in a decaying allowance
for the correlation between an observation and the ones nearby, out to a stated number of lags.
It is graduate-level and **it is a name, not a mechanism, at this level** — the paper gives no
formula and neither does this page. Do not let the player claim to have derived it.

**One curiosity worth handing over, correctly framed.** The full title of reference [26] on p.65
is *"A Simple, **Positive Semi-Definite**, Heteroskedasticity and Autocorrelation Consistent
Covariance Matrix"*. That phrase — *positive semi-definite* — is Section 6h's health check
exactly: no eigenvalue is negative, no book has negative variance. It is the closest the 65
pages come to this level's machinery, **and it appears only inside a reference title.** The paper
never uses the phrase in its own sentences and never unpacks it. Cite it as a title, never as a
claim the paper makes.

### 13h. Where this level's machinery ends up in the finished model

Trace it forward once, out loud, so the player sees the level's place in the pipeline:

1. Level 7's cross-sectional regressions produce a factor return `f` per factor per day —
   **daily** for country and regional models, **weekly** for the World model (p.24).
2. Those series, from March 1996, are exponentially weighted with a 26-week half-life over 104
   weeks and turned into **`F`** (p.27). **This level.**
3. `F` enters equation (1.8) on p.24 as the middle of `XFXᵀ`, which converts a book's factor
   exposures into its common-factor risk. (Level 10.)
4. Every number on the risk report of p.34–35 that is not Specific comes out of that product —
   on the paper's one worked example, an EMEA equity portfolio whose banner reads **Active Risk
   2.99%** `[read directly; the middle digit is soft and 2.89 is not fully excluded]`, the
   common-factor half is Style 25%, Industry 14%, Country 6%, FX 4% and Act Sec 1% of active
   risk against Specific at 50% `[p.35 pie, read directly — INFERRED, the slices carry no printed
   labels; they do sum to 100]`. p.34 says it in prose: "the Active Risk is split equally between
   common factors and stock specific sources". (Level 11.)

Get the half-life wrong at step 2 and every one of those percentages moves, with no change to a
single holding and no change to a single exposure. That is what this level changes about a real
risk number.

### 13i. What the notes do NOT support — searched across all 65 transcribed pages

- **No eigenvalue. No eigenvector. No "eigen-" anything. No principal component. No PCA.** Zero
  hits. The entire construction in Section 6 is the game's.
- **No shrinkage of `F`.** The only shrinkage-shaped device is p.36's Bayesian prior on thin
  country/industry **returns**, and its form, strength and parameter are unspecified.
- **No factor count for any model.** Not for NAMR, not for WRLD, not for any of the eleven
  models. The ≈70–71 of 13c is assembled by us from Table 1.2 and Table 1.5's printed rows.
- **No rank, no condition number, no smallest eigenvalue, no positive-semi-definiteness
  discussion, no observation-to-factor ratio.** The paper never confronts "fewer periods than
  factors" in any form.
- **No statement of the covariance estimator itself.** p.27 gives a window, a weighting scheme
  and a half-life, then says: "Model users are referred to the **BRS Covariance Matrix
  Estimation documentation** for technical details on the factor covariance matrix
  methodology." The most important matrix in the model is documented elsewhere. **This is Level
  12's single best exhibit** — do not spend it here beyond naming it.
- **No statement of whether a mean is subtracted, or of the divisor.** Section 4d.
- **No numerical example of `F` anywhere.** Not one cell of any factor covariance matrix is
  printed in the 65 pages. Table 1.2's market-correlation column is the closest thing in the
  document, and it is a full-sample summary, not the shipped matrix.

So: **the object this level builds is named on p.24, sourced on p.27, and never shown.** Tell the
player exactly that. Then tell them the consequence, which is the sentence that wins the boss
round: *the criticism that survives is not that the matrix is broken — nobody can know that — it
is that the document does not contain what a reader would need to rule it out.*

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level8.py     # 347 exact-rational assertions, exits 0
```

The script recomputes every figure on this page from the raw exposure column and the five months
of returns, in `fractions.Fraction`: the Gram matrix and its zero off-diagonal; all five
cross-sectional solves, both ways (Level 1's formula and the full two-column Gaussian
elimination), with both balance conditions and every residual; the means, deviations and three
sums behind `F`; all three divisor conventions and the exact identity linking them; the
quadratic form derived from the series and from the grid for three named books and swept over
**169** integer books; every number the Section 8 trap table returns, including what dropping
the off-diagonal does to each book and in which direction; the sabotage grid's impossible
correlation and its negative-variance book; the full direction sweep in exact fractions with the
peak and trough ladders; the perpendicular-pair sum rule; the degenerate `λ = 25` case where the
quadratic turns linear; the discriminant, the characteristic quadratic and its factorisation;
the two sum-of-squares identities checked on **361** directions; `Fv = λv` for both eigenvectors;
the rebuild `F = 27P₁ + 7P₂` with `P₁+P₂ = I`, `P₁² = P₁` and `P₁P₂ = 0`; the split of Book A
between the two directions; the perfectly-correlated cliff grid and its zero-risk book; and the
entire boss round — the 3×3 grid, its three exact volatilities, all three correlations,
`S·w = 0`, the determinant, the row-3-equals-row-1-plus-row-2 structure, the levered version, the
**19,683**-case brute force showing every three-factor three-month dataset is singular, the
no-mean second-moment contrast, the shrunk grid at `a = 1/4` with every entry and correlation,
the hole's variance as exactly `83a`, the positive-definiteness floor of `9/4` checked on **728**
books, the five-intensity 2×2 shrinkage table with eigenvalues, spreads and determinants at each
`a`, and the 16% bias priced on Book C.

The only non-rational quantities on the page are in Section 13c, where the decay factor is
`2^(−1/26)`. Those are computed with `decimal.Decimal` at 50 digits, the closed forms
`(15/17)(1+λ)/(1−λ)` and `(7/9)(1+λ)/(1−λ)` are proved against the direct sums to 20 decimal
places, and every decimal printed from them is marked **rounded** here.

If any printed value ever disagrees with this markdown, the markdown is wrong.
