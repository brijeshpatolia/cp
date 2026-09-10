# Level 10 — The Assembly

Every number below is recomputed in exact rational arithmetic by `tools/verify_level10.py`
(447 assertions plus 1,167 swept cases, exits 0). Nothing here is rounded by hand. Where a
decimal does not terminate it is written with the word **rounded** next to it; every other
decimal on this page is exact.

> **DIFFICULTY — and this time the honest answer is "not hard", which has to be said just as
> plainly as the warnings at Levels 4 and 8** (`prompt/RISK_DESK.md` §8, BE HONEST ABOUT
> DIFFICULTY).
>
> **The arithmetic on this level is the easiest since Level 3.** Two matrix products — thirty
> small multiplications in all, many of them by `1` or `0` — and one addition. There is no calculus, no probability, no estimation, nothing graduate-level. A
> player who found Level 8's Section 6 punishing should be told, before starting, that this
> level is not that.
>
> **The difficulty has moved somewhere else: this is the hardest level to *read*.** The demand
> is not "can you multiply matrices" — it is *"say out loud what this row, this column and this
> single number mean, in a sentence with no symbols in it."* That is a genuinely harder skill
> than the multiplication, it is the one a Chief Risk Officer tests in thirty seconds, and it
> is the whole of the boss round. A player who can compute `X F Xᵀ` and cannot say what cell
> (1,3) means has **not** passed this level, no matter how fast they multiplied.
>
> **What is graduate-level, and is deliberately not needed here.** Eigen-decomposition
> (Level 8 §6), shrinkage (Level 8 §11.6) and the Newey–West serial-correlation adjustment
> (p.27, p.28) are all graduate material, and none of them is required to assemble `V`. Say
> that. Assembly is the cheap step; the expensive steps were `F` and `D`, and the player has
> already paid for both.
>
> **One thing on this level is subtle rather than hard, and it is Section 13**: the plus sign in
> `V = X F Xᵀ + D` is an *assumption*, not an identity, and Section 13 prices it exactly on this
> file. Run it. It is where the level stops being bookkeeping.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the miss `u`, scored by its size and not its sign.
**From Level 1** — `b = Σxr/Σx²`, derived by nudging.
**From Level 2** — the balance condition `Σx·u = 0`, forced by the arithmetic, one per column.
**From Level 3** — two columns, two balance conditions, one simultaneous solve.
**From Level 4** — the determinant, and what a determinant of zero means.
**From Level 5** — centering; why a column of ones is an intercept; `Cov/Var`.
**From Level 6** — degrees of freedom, `n − k`, leverage `h_i`, and `E[u_i²] = (1 − h_i)σ²`.
**From Level 7** — the same cross-sectional regression run month after month: a *row* of factor
returns through time.
**From Level 8** — `F`, the 2×2 grid of how the factor returns move together, and `hᵀFh`, the
rule that turns a set of factor bets into one variance.
**From Level 9** — `D`, the list of each stock's private wobble, and the difference between what
least squares *guarantees* and what BFRE *assumes*.

Level 10 asks the one question none of those answered:

> You have a grid for the **factors** and a list for the **stocks**. A portfolio is neither: it
> is a handful of stocks, held in chosen amounts, whose risks come partly from shared factors
> and partly from their own private lives. What single object prices *that*, and how do you
> build it out of the two things you already have?

Four genuinely new things:

| | What Level 10 adds |
|---|---|
| **One object for the whole market** | `V`. A grid with one row and one column per **asset**, built out of a grid whose rows are **factors**. Section 6. |
| **Multiplication as language** | Every product in `V = X F Xᵀ + D` is a sentence about who is being asked what. Sections 4, 5, 6. This is the level's actual content. |
| **The decomposition** | Total risk splits into factor risk and specific risk — and the two **add as variances and not as risks**. Section 8. This is the single most common error at this level and the player must meet it. |
| **A structural check that is free** | `X F Xᵀ` is *always* singular when there are more assets than factors. Section 6d turns that into a bug-finder (Section 10) and into the reason `D` has to exist. |

**Names deliberately withheld until Section 14.** Do not say *asset covariance matrix*, `Σ`, or
*tracking error* at the table before the corresponding object is built. Before then say: *the
big grid*, *the whole-market grid*, *the risk of the difference between the book and its
benchmark*. (`gm/VOCAB.md` rows 10 and 13 set these unlocks.) **Do not unlock here:** *marginal
contribution to risk* — that is Level 11, and Section 7c walks right past it without naming it.

---

## 1. The story — no mathematics

*(Analogy bank: `gm/ANALOGIES.md` **C15-A**, money-changing. If the player has already rejected
an analogy from the money/accounts family — C3-B the ledger, C8-C the envelopes, C13-B the
village fire rate — go straight to C15-B, the pharmacy, and do not open this one at all. The
burn ledger in `gm/ANALOGIES.md` §2 flags money as the biggest hidden exposure in the file.)*

A tourist-shop owner closes up on a Saturday night and has to tell her accountant what the day's
takings are worth in her own currency. The till is a mess: euros, pounds, francs, and a scatter
of notes from wherever this week's coach party came from.

She does not value each note on its own. She does it in three moves.

First she sorts and counts. So much held in euros. So much held in pounds. So much in francs.
The individual notes stop mattering the moment they are sorted; what matters is the pile.

Second she looks at the board on the wall. The board does not just say what each currency is
worth. It also says — and this is the part she has learned to care about — how they move
*against one another*. On a bad day the euro and the franc go the same way together, so holding
both is not two separate worries, it is one worry twice the size. The pound tends to go the
other way, so holding pounds against euros is quieter than holding either alone.

Third she converts the whole thing back and writes one number on the slip.

And then she adds one item by hand. At the bottom of the till there is a commemorative coin from
a country nobody trades. No board quotes it. Nothing on the wall says anything about how it moves
with anything else. She has to estimate that one entirely on its own, and add it on at the end.

The slip has two lines on it. Everything the board could speak to, and the coin.

---

## 2. Mapping the story onto the model, line by line

Go down this table row by row. Do not skip a row because it looks obvious; the skipped row is
where the misconception lives.

| In the story | In the model |
|---|---|
| the notes in the till | the positions in the portfolio |
| **sorting the notes into currency piles** | `Xᵀ` applied to the holdings — turning a list of *stocks* into a list of *factor bets* |
| a currency | a factor |
| how much she holds in one currency | the portfolio's exposure to one factor |
| **the board on the wall** | `F` — p.24, equation (1.8) |
| euro and franc moving together | a positive off-diagonal in `F`: two bets compounding |
| the pound moving the other way | a negative product of exposures: two bets partly cancelling |
| converting the whole pile back | `X` carrying the factor answer back to individual assets |
| the number on the slip, before the coin | the common-factor part of risk |
| **the untradeable commemorative coin** | `D` — one number per asset, no board to consult |
| the slip having two lines | the `+` in `V = X F Xᵀ + D` |
| the accountant needing the *total*, not the two lines | the boss round |

**The awkward question to ask before moving on** (round type D, and ask it exactly like this):

> *"She converts into currencies and back out again. Why not just look up what each note is worth
> and be done? What did the detour through currencies actually buy her?"*

- **Landed** sounds like: it buys the *board*. Valuing note against note would need a
  relationship between every note and every other note. Going through currencies means she only
  needs relationships between the handful of currencies — and there are far fewer currencies
  than notes. That is the paper's own architectural claim, **PAPER, p.2**: BFRE "imposes far
  more structure on the asset covariance matrix, reducing the modelling problem to a smaller set
  of factors, which capture the most important sources of asset return commonality".
- **Not landed** sounds like: *"because it's more accurate."* It is not obviously more accurate.
  It is vastly more **estimable**. A player who says "accurate" has missed the entire argument
  and will not understand Section 6d when it arrives.

**Where the story breaks, and say this out loud.** Exchange rates are quoted, observable, and
agreed by everybody. `F` is *estimated*, by one desk, from a window the paper sets at 104 weeks
(p.27), and it is not observable at all. Also, currency conversion is exact and loses nothing,
whereas going through factors deliberately throws away everything the factors cannot express —
and that discarded part is not an error. It is `D`, and on the paper's own example report it is
**half the number** (p.35 pie, read directly: Specific **50%**).

---

## 3. The three pieces, and where each one came from

Nothing in this section is new. That is the point of the section: **the player built all three
of these already, and this level only stacks them.** Say so before showing anything.

### 3a. `X` — three rows of the file the player has been working since the cold open

Level 8's estimation universe was five names with two columns: a column of ones (the market
factor — **PAPER, p.4**: "all equity assets have a unit exposure to this factor") and a centred
cheapness column.

| Stock | market `1` | cheapness `x` |
|---|---:|---:|
| AXL | 1 | −2 |
| BRN | 1 | −1 |
| CHR | 1 | 0 |
| DLT | 1 | +1 |
| EMK | 1 | +2 |

**The book on this desk holds three of those five names: AXL, CHR and EMK.** That is not a
simplification — it is the real structure. **PAPER, p.24:** the estimation universe "comprises
the set of assets that are used during the model estimation process to infer the factor returns
and asset specific returns" and is "constructed on a country-by-country basis every month". The
universe is what the model was *fitted on*; the portfolio is what somebody *owns*. They are
different sets and the player must never conflate them. `F` and `D` were estimated on five
names; the book holds three.

So:

```
        ┌            ┐
        │  1     −2  │   AXL
  X  =  │  1      0  │   CHR          3 rows (held assets) x 2 columns (factors)
        │  1     +2  │   EMK
        └            ┘
```

**Read the two directions of `X` out loud before anything multiplies it:**

- **A row of `X` is one stock's answers to the two questions the model asks.** AXL's row says
  *"I am an equity (1), and I am two standard deviations cheap (−2)."*
- **A column of `X` is one question asked of every stock.** The cheapness column says
  *"here is how cheap each of you is, measured against the average of the universe."*

Rows are assets. Columns are factors. Every single confusion on this level is a row/column
confusion, and this is the sentence to come back to when one appears.

### 3b. `F` — lifted straight off Level 8, unchanged

**This is a callback and you must say the word.** The player built this grid themselves in
Level 8 §4b, out of the five monthly factor returns Level 7 produced. Nothing is re-derived
here; it is carried across.

```
        ┌            ┐
  F  =  │  25     6  │        percent-squared, per month
        │   6     9  │
        └            ┘
```

- top-left **25** — how much the market factor return wobbles, squared. Volatility `√25 = 5.0%`
  per month, exact.
- bottom-right **9** — the same for the cheapness factor. Volatility `√9 = 3.0%`, exact.
- off-diagonal **6**, twice — how the two wobble together. Correlation `6/(5×3) = 0.40`, exact.

`det F = 25×9 − 6×6 = 189`, which is not zero, so the two factors are not collinear (Level 4).
The verifier rebuilds `F` from the raw returns file rather than accepting it: the five factor
return pairs are `(+7,+4), (+5,+4), (+1,−2), (+3,−2), (−6,+1)` in percent, mean subtracted,
divided by `T − 1 = 4`.

### 3c. `D` — built from the miss columns Level 8 handed forward

**Second callback, and again say the word.** Level 8 §3c printed five columns of misses and said
of them: *"they are Level 9's raw material, not this level's."* Here they are, per name, over the
same five months:

| Stock | m1 | m2 | m3 | m4 | m5 | `Σu²` |
|---|---:|---:|---:|---:|---:|---:|
| AXL | +1 | 0 | +1 | −1 | 0 | **3** |
| BRN | −2 | +1 | 0 | +2 | +1 | 10 |
| CHR | +2 | −2 | −2 | −2 | −2 | **20** |
| DLT | −2 | +1 | 0 | +2 | +1 | 10 |
| EMK | +1 | 0 | +1 | −1 | 0 | **3** |

(The verifier re-derives every one of those 25 misses from the returns and the fitted factor
returns, and re-checks both Level 2 balance conditions in all five months.)

Each stock's specific variance is the **average squared miss**:

```
d_AXL = 3/5  = 0.6          d_CHR = 20/5 = 4          d_EMK = 3/5 = 0.6      percent-squared
```

```
        ┌                  ┐
  D  =  │  0.6   0     0   │
        │  0     4     0   │      3 x 3, and every off-diagonal is zero
        │  0     0    0.6  │
        └                  ┘
```

Specific volatilities: `√0.6 = 0.7746` **rounded**, `√4 = 2.0000` exact, `√0.6 = 0.7746`
**rounded**.

**The divisor is Level 9's argument, not this level's — but this page must say which one it is
using, or the numbers below have no origin.** It divides by `T = 5` and subtracts no mean. The
reason, in one line the player can check: Level 6's rule is *divide by the number of numbers
minus the number of parameters you estimated from those same numbers*, and for a stock's own
specific-return series **no parameter was estimated from that series** — the model asserts the
mean is zero. *(That reading is* **INFER***. What p.24 actually prints is "In a well-specified
model, the prescribed factors will capture all sources of commonality in asset returns leaving
only return associated with stock-specific events in the idiosyncratic component." It never
writes `E[u] = 0`. The zero-mean reading follows from it; the paper does not state it.)*

For the factor series in §3b a mean *was* estimated from the data, which is why that one divides
by `T − 1 = 4`. The asymmetry is real and deliberate; a sharp player will spot it and must be
paid for spotting it.

**And here is the honest part.** Nothing forces a stock's own misses to average to zero. The
balance conditions of Level 2 run **across stocks within one month**, never across months within
one stock. Check CHR: its five misses average `−6/5 = −1.2`, which is nowhere near zero. So the
divisor is a live choice, and here is what each choice returns:

| Convention | `d_AXL` | `d_CHR` | `d_EMK` | Book A's total risk (§7) |
|---|---:|---:|---:|---:|
| **used on this page** — divisor `T = 5`, mean asserted to be zero | **3/5** | **4** | **3/5** | **4.6857%** rounded |
| subtract each name's own mean, divisor `T − 1 = 4` | 7/10 | 16/5 | 7/10 | 4.6748% rounded |
| Level 6's leverage correction, `Σu²/(T(1 − h_i))` with `h_i = 1/5 + x_i²/10` | 3/2 | 5 | 3/2 | 4.7276% rounded |

The three answers span **1.13%** of the middle one. **Say that number out loud**, because it
settles a live argument at the table: the divisor debate moves the risk number by about one part
in a hundred, whereas the *diagonal* assumption — the one Level 9 spent a whole level on — moves
it by far more, and Section 13 measures exactly how much on this very file. The assembly in
Sections 4–7 takes whatever `D` it is handed and does not care which convention produced it.
The verifier checks all three.

*(For Level 6's leverage row: `h_AXL = 1/5 + 4/10 = 3/5`, `h_CHR = 1/5 + 0 = 1/5`,
`h_EMK = 3/5`, and the five leverages sum to `k = 2` exactly, which is the check Level 6
installed.)*

### 3d. The letter warning — say this before the player finds it and thinks they caught an error

`gm/VOCAB.md` §2 requires this and it must not be skipped.

| The game writes | The paper writes | Where |
|---|---|---|
| `V` | `Σ` (capital sigma) | p.24, equation (1.8) |
| `D` | `Δ` (capital delta) | p.24, equation (1.8) |
| `X`, `F` | `X`, `F` | p.24 — same letters |

**PAPER, p.24**, the whole of equation (1.8) and its where-list:

> `Σ = X F Xᵀ + Δ`
> where `Σ` : asset covariance matrix; `F` : factor covariance matrix; `Δ` : specific risk
> matrix (a diagonal matrix of asset specific risk forecasts)

It is a letter swap, not a different model. A player who reads the paper and thinks the game got
it wrong has lost twenty minutes for nothing.

### 3e. Three simplifications, declared before they can be mistaken for the model

1. **Three assets and two factors.** BFRE's North America model carries a market factor, twelve
   styles, fifty-four core industries and a country/currency block — a count the paper never
   prints (Level 8 §13c assembled a floor of ≈71 from Table 1.2 on p.10 and Table 1.5 on p.57,
   and that count is **ours**, not the paper's). Three and two are chosen so that every
   multiplication fits on a page.
2. **Exposures frozen across the five months.** BFRE re-standardises and reposts exposures
   weekly (p.36, PAPER). Level 7 already paid for this simplification and named its cost.
3. **Monthly units throughout, percent and percent-squared.** BFRE's forecast horizon is
   **1 month** (p.30, PAPER), so monthly is the right unit; but where this page annualises by
   `×√12` it is assuming months are independent, which p.30 explicitly says BFRE does *not*
   assume — risk estimates take "into account daily serial correlations in factor returns and
   asset specific returns". Any `×√12` on this page is ours and is flagged where it occurs.

---

## 4. How to read a matrix product as a sentence

**This section has no numbers in it on purpose.** Do it before Section 5 and do not let the
player skip to the arithmetic.

**The one rule.** In any product `AB`, the entry in **row `i`, column `j`** is *row `i` of `A`
meeting column `j` of `B`* — multiply the pairs, add them up. So:

- **The rows of the answer inherit their meaning from the rows of the LEFT matrix.**
- **The columns of the answer inherit their meaning from the columns of the RIGHT matrix.**
- The thing being summed over — the shared middle dimension — is the thing that **disappears**.

That third line is the useful one. Every multiplication in this level is chosen to make one
particular index vanish, and naming which one vanishes is how a player proves they understand
the product rather than the procedure.

**What `Xᵀ` is.** `X` has assets down the side and factors across the top. `Xᵀ` is the same
numbers with the axes swapped: factors down the side, assets across the top. Nothing is
computed. It is a relabelling, and it exists so that the shared index of the next
multiplication lines up.

**Build the shape before seeing it** (round type C — run this before revealing anything):

> *"`X` is 3 by 2: assets by factors. `F` is 2 by 2: factors by factors. You want a grid that is
> assets by assets. Which multiplications are even legal, and which one gives you the shape you
> want?"*

The player should reach `X F Xᵀ` unaided, from shapes alone: `(3×2)(2×2)(2×3) → 3×3`. Then push
one step further and make them say **what vanished**: the factor index appears in the middle
twice and is summed away both times, which is exactly why an asset-by-asset grid can be built
from a factor-by-factor one.

Two shapes that are *legal* and *wrong*, worth showing so the trap is closed early:

| Expression | Shape | What it is |
|---|---|---|
| `X F Xᵀ` | 3×3 | assets by assets — **the one we want** |
| `Xᵀ V X` | 2×2 | factors by factors — a legal grid, but it answers a question about factors |
| `Xᵀ F X` | — | **not defined.** `Xᵀ` is 2×3, `F` is 2×2; 3 does not meet 2 |

The last row is the good news about dimensional discipline: the most common transposition
mistake at this level does not silently return a wrong number, it fails to compute at all.

---

## 5. Stage one — `F Xᵀ`, and what its columns mean

Do the product in **two stages**, and name the intermediate. A player who computes `X F Xᵀ` in
one blur has learned a procedure; a player who can say what the halfway object is has learned
the model.

```
              ┌         ┐   ┌                  ┐
              │ 25   6  │   │  1    1    1     │       market row
  G = F Xᵀ =  │  6   9  │ x │ −2    0   +2     │       cheapness row
              └         ┘   └                  ┘
                              AXL  CHR  EMK
```

Column by column — each column of `G` is `F` applied to one stock's own exposure row:

```
  AXL:   25(1) + 6(−2) = 13          6(1) + 9(−2) = −12
  CHR:   25(1) + 6( 0) = 25          6(1) + 9( 0) =   6
  EMK:   25(1) + 6(+2) = 37          6(1) + 9(+2) =  24
```

```
        ┌                      ┐
  G  =  │  13     25     37    │      market row
        │ −12      6     24    │      cheapness row
        └                      ┘        percent-squared
          AXL    CHR    EMK
```

**The sentence, and make the player say it before you do:**

> **Row = a factor. Column = a stock. Entry = how that factor's return moves together with
> that stock's factor-driven return.**

Test the sentence on the two most interesting cells:

- **`G[cheapness][AXL] = −12`.** *"When the cheapness factor pays, AXL's factor-driven return
  goes the other way."* Why? AXL's cheapness exposure is **−2**, so a cheapness payoff hits AXL
  with `9 × (−2) = −18`; but AXL is also an equity with market exposure 1, and the market factor
  moves with cheapness at `+6`, which pulls back `+6`. Net `−12`. **Two effects, opposite signs,
  and the off-diagonal of `F` is the second one.** A player who cannot produce that sentence has
  not understood `F` and should be sent back to Level 8 §4c before going on.
- **`G[market][CHR] = 25`.** CHR has zero cheapness exposure, so the cheapness column of `F`
  contributes nothing and the answer is just the market's own variance. **The stock with no
  style tilt is the stock whose common return is pure market.**

**What vanished:** nothing yet — `G` still has a factor axis and an asset axis. It is the object
half-way between the two worlds, which is exactly why it is worth naming.

---

## 6. Stage two — `X G`, then `+ D`

### 6a. The multiplication

```
              ┌          ┐   ┌                      ┐
              │  1   −2  │   │  13     25     37    │
  X G   =     │  1    0  │ x │ −12      6     24    │
              │  1   +2  │   └                      ┘
              └          ┘
```

Row by row. Row AXL is `(1, −2)`, so it takes `1 ×` the market row of `G` and `−2 ×` the
cheapness row:

```
  AXL row:   13 + (−2)(−12) = 37     25 + (−2)(6) = 13     37 + (−2)(24) = −11
  CHR row:   13 + ( 0)(−12) = 13     25 + ( 0)(6) = 25     37 + ( 0)(24) =  37
  EMK row:   13 + (+2)(−12) = −11    25 + (+2)(6) = 37     37 + (+2)(24) =  85
```

```
              ┌                        ┐
              │   37     13     −11    │   AXL
  X F Xᵀ  =   │   13     25      37    │   CHR      percent-squared, per month
              │  −11     37      85    │   EMK
              └                        ┘
                 AXL    CHR     EMK
```

**The sentence:**

> **Row = a stock. Column = a stock. Entry = how much of those two stocks' returns move together
> because of the factors they share.** The factor axis has been summed away twice and is gone.

Two arithmetic facts worth stating so the player can check any cell in five seconds:

- **The matrix is symmetric**, and it has to be: "how AXL moves with EMK" and "how EMK moves with
  AXL" are the same sentence read from either end (Level 8 §4b made the same point about `F`).
- **Every cell has a closed form.** With `x_i` and `x_j` the two cheapness exposures,
  cell `(i,j) = 25 + 6(x_i + x_j) + 9 x_i x_j`. Check `(AXL, EMK)`:
  `25 + 6(−2 + 2) + 9(−2)(+2) = 25 + 0 − 36 = −11`. The verifier checks all nine cells this way.

### 6b. The other bracketing, and why it agrees

`(X F) Xᵀ` gives the same answer, because matrix multiplication is associative:

```
             ┌            ┐
  X F   =    │  13   −12  │   AXL
             │  25     6  │   CHR
             │  37    24  │   EMK
             └            ┘
```

Those rows are `G`'s **columns**. That happens because `F` is symmetric, and it is worth showing
because a player who has only ever seen one bracketing thinks the order of operations is a rule
to memorise rather than a choice about which intermediate you want to look at.

**Which intermediate is the useful one depends on the question.** `G = F Xᵀ` reads
factor-by-stock. `X F` reads stock-by-factor: row AXL of `X F` is *"how AXL's common return
moves with each factor"* — the same content, transposed. Say that; do not let it go by as a
coincidence.

### 6c. Adding `D`

`D` is diagonal, so this changes exactly three numbers:

```
        ┌                          ┐        ┌                          ┐
        │  37+0.6    13      −11   │        │  37.6     13      −11    │
  V  =  │   13      25+4      37   │   =    │  13       29       37    │
        │  −11       37     85+0.6 │        │  −11      37      85.6   │
        └                          ┘        └                          ┘
```

**The sentence for the whole line:**

> **`X F Xᵀ` is everything two stocks share. `D` is what each stock has that it shares with
> nobody. `V` is both.**

And the sentence for the *shape* of `D`, which is Level 9's content arriving with a bill:

> **Every zero off the diagonal of `D` is a claim.** It says: whatever is left in AXL after the
> market and cheapness have been taken out has nothing whatever to do with whatever is left in
> EMK. Section 13 tests that claim on this file and it fails, in the direction p.28 predicts.

### 6d. `V`, read cell by cell

Now make the player narrate the grid. Nothing else on this level matters as much.

| Cell | Value | The sentence |
|---|---:|---|
| `V[AXL,AXL]` | **37.6** | AXL's whole variance: `37` from the two factors, `0.6` from its own private life. Volatility `√37.6 = 6.1319%` per month, **rounded** — `21.2415%` a year, **rounded**, `×√12`, ours. |
| `V[CHR,CHR]` | **29** | CHR's whole variance: `25` common, `4` private. Volatility `5.3852%` **rounded**. CHR is the least volatile of the three *and* the one with the largest private wobble — those are different statements, and the player must not merge them. |
| `V[EMK,EMK]` | **85.6** | Volatility `9.2520%` **rounded**. EMK is **1.7181 times** as volatile as CHR (**rounded**) without having any bigger private life at all — its `d` is `0.6` against CHR's `4`. The whole difference is a `+2` style tilt magnified by `F`. |
| `V[AXL,CHR]` | **13** | Positive: same market. Implied correlation `13/√(37.6×29) = 0.3937`, **rounded**. |
| `V[CHR,EMK]` | **37** | Strongly positive: same market, and CHR sits between AXL and EMK on cheapness. Correlation `0.7426`, **rounded**. |
| **`V[AXL,EMK]`** | **−11** | **Negative.** Two stocks in the same market that the model expects to move *against* each other. Correlation `−0.1939`, **rounded**. |

**Spend real time on `−11`.** It is the cell that teaches the level.

Both stocks are equities, so both carry the market factor, which pushes them together: that is
the `+25` in the closed form. But their style tilts are exactly opposite, `−2` against `+2`, and
the cheapness factor's own variance of `9` pushes them apart by `9 × (−2)(+2) = −36`. The
cross-term `6(x_i + x_j)` is zero here because the tilts cancel. Net `−11`: **the style
disagreement is bigger than the market agreement.** That is a real thing a real model says about
a deep-value name and a deep-growth name, and it is the reason a portfolio holding both can be
quieter than a portfolio holding either.

**And now the trap next to it.** Switch `D` off and recompute the same three correlations from
`X F Xᵀ` alone: `0.4274`, `−0.1961`, `0.8026` (all **rounded**). Every one of them is *further
from zero* than the correlation implied by `V`. Say why: `D` adds variance to the diagonal and
nothing to the off-diagonal, so it can only dilute a correlation, never strengthen one. **A
model with more specific risk in it is a model with lower asset correlations**, mechanically,
before anyone has looked at any data. That single fact is worth a full minute — it is the
cleanest statement of what `D` does to a risk report.

### 6e. The structural fact: `X F Xᵀ` is singular, and `D` is what repairs it

This is the deepest thing on the level and it takes four lines.

Three assets, two factors. So there must be a way of holding those three assets that has **no
factor exposure at all** — two conditions on three unknowns always leaves one direction free.
Find it: we need weights `z` with `Σz = 0` (no market exposure) and `Σ z·x = 0` (no cheapness
exposure). Try `z = (1, −2, 1)`:

```
  market:      1 + (−2) + 1 = 0
  cheapness:  (1)(−2) + (−2)(0) + (1)(+2) = 0
```

Apply the common-factor matrix to it:

```
  row AXL:    37(1) + 13(−2) + (−11)(1)  =  37 − 26 − 11  =  0
  row CHR:    13(1) + 25(−2) +   37 (1)  =  13 − 50 + 37  =  0
  row EMK:   −11(1) + 37(−2) +   85 (1)  = −11 − 74 + 85  =  0
```

Every row gives zero. So `X F Xᵀ z = 0`, and therefore `zᵀ (X F Xᵀ) z = 0`: **the common-factor
matrix scores that book at exactly zero risk.** Its determinant is exactly `0`, which is Level
4's collision arriving in new clothes — not two columns colliding, but a matrix that was only
ever built out of two columns and cannot say anything about a third direction.

**This is not a bug.** It is correct: that book really does have no factor bet. The bug would be
reporting it as riskless. Add `D`:

```
  V z  =  (0.6, −8, 0.6)          zᵀ V z  =  17.2 percent-squared
  det V  =  13306.44   (exact:  332661/25)
```

`D` alone accounts for all `17.2` — because the common part contributed nothing.

**And `V` can never score any book at zero, for a reason the player can state in one line.** For
any holdings `w`, `wᵀVw = hᵀFh + Σ w_i² d_i`. The first term is a variance and can never be
negative — Level 8 §5b built it by expanding a square, and `F`'s own entries `25` and `9` are
positive with `det F = 189 > 0`. The second term is **strictly** positive unless every weight is
zero, because every entry of `D` is strictly positive. So the total is strictly positive for
every real book. The verifier sweeps all **342** non-zero holding vectors with entries in
`{−3, …, 3}` and confirms it. Separately, `det V = 13306.44` is not zero, which says `V` is
invertible where `X F Xᵀ` was not — a fact an optimiser cares about and a player does not need
yet.

**CALL BACK, and this is the payoff of Level 8's boss round.** At Level 8 a grid scored a real,
leverable book at exactly zero risk and that was a **catastrophe**, because the grid had run out
of data. Here a grid scores a real book at exactly zero risk and it is **correct**, because the
book genuinely has no factor bet — and `D` is precisely the thing that stops the *total* from
being zero. Same arithmetic, opposite verdict, and the difference is whether the zero came from
structure or from ignorance. Make the player state that difference in their own words before
moving on. (Book C in Section 12 is exactly this book, at one tenth the size.)

---

## 7. The portfolio — two routes to one number

The book on this desk:

| | AXL | CHR | EMK |
|---|---:|---:|---:|
| **Book A, weights `w`** | 50% | 40% | 10% |

Fully invested, long only, weights sum to 1.

### 7a. Build the shape before seeing it (round type C)

> *"`V` is 3 by 3 in percent-squared. `w` is a list of three plain numbers with no units. You
> want one number in percent-squared. What must the formula look like?"*

Most players reach `Σ w_i² V_ii` and stop — the same failure Level 8 §5a produced with `hᵀFh`,
and it should be pointed out as the same failure. Then ask the killer: *does your formula give a
different answer for a book that is long AXL and long EMK versus long AXL and short EMK?* It
does not. It must. The off-diagonals are the missing piece, each one appearing **twice**.

### 7b. Route 1 — aggregate the exposures first

This is the route p.24 describes. **PAPER, p.24** — recorded in `notes/` as a close paraphrase of
the page rather than a verbatim sentence, so present it as such: portfolio risk is computed from
portfolio holdings, portfolio-level factor exposures **aggregated from the asset level**, a
factor covariance matrix, and asset specific risk forecasts.

```
  h  =  Xᵀ w
```

`Xᵀ` is 2×3 and `w` is 3 long, so `h` is 2 long: **a list of factor bets, not of stocks.**

```
  market   :  0.5(1)  + 0.4(1) + 0.1(1)  =  1
  cheapness:  0.5(−2) + 0.4(0) + 0.1(+2) = −1.0 + 0 + 0.2  =  −0.8
```

```
  h  =  ( 1 ,  −0.8 )
```

**Two sentences the player must produce here.**

1. **The market exposure is exactly 1 because the weights sum to 1.** And this is where **p.4's
   warning** lives, so read it out: *"The market factor exposure of a portfolio should not be
   confused with its market beta."* Market factor exposure is a **position**, not a sensitivity
   — p.4 defines it as "the fraction of portfolio %NAV invested in equities" (footnote 3 adds
   "delta-adjusted market exposure for derivatives"). Ours is 1 because the book is fully
   invested, and it would still be 1 if every stock in it were a sleepy utility.
2. **The cheapness exposure is −0.8**: this book is, net, eight tenths of a standard deviation
   towards the cheap end. Three stocks went in; one number about *value* came out. **The stocks
   are gone.** That vanishing is the whole architectural bet of the model.

Now Level 8's `hᵀFh`, unchanged:

```
  factor variance  =  25(1)²  +  2(6)(1)(−0.8)  +  9(−0.8)²
                   =  25      −  9.6            +  5.76
                   =  21.16        percent-squared        (exact: 529/25)

  factor risk      =  √21.16  =  4.6%  per month          (EXACT root: 23/5)
```

**Look at the middle term.** `−9.6` is a *subtraction*, and it is bigger than the whole cheapness
contribution of `+5.76`. The book's value tilt is **hedging** its market exposure, because the
two factors are positively correlated (`+6`) and the book is long one and short the other. A
player who deletes the off-diagonals of `F` will get this book badly wrong in the direction of
*too risky* — Section 9, trap 2, prices it at `+19.88%`.

Then the specific part. `D` is diagonal, so the double sum collapses to three terms:

```
  specific variance =  (0.5)²(0.6)  +  (0.4)²(4)  +  (0.1)²(0.6)
                    =   0.15        +   0.64      +   0.006
                    =   0.796         percent-squared        (exact: 199/250)

  specific risk     =  √0.796  =  0.8922%  per month     rounded
```

**The weights are squared.** Say why, do not let it pass: a variance is built from products of
*two* holdings, and for the diagonal both of them are `w_i`. Forgetting the square is trap 6 in
Section 9 and it returns `4.8083%` **rounded** instead of `4.6857%`.

Note also that CHR supplies `0.64` of the `0.796` — **80.4020%** (**rounded**) **of the book's
specific variance comes from one 40% position**, because the specific variances differ by a
factor of nearly seven across these three names (`4` against `0.6`) and the weight is squared on
top. That is Level 11's whole subject and it is visible here for free; point at it, do not name
it.

```
  TOTAL variance  =  21.16  +  0.796  =  21.956            (exact: 5489/250)
  TOTAL risk      =  √21.956  =  4.6857%  per month        rounded
```

Annualised by `×√12` — **ours, and it assumes months are independent, which p.30 says BFRE does
not assume** — that is `16.2318%` a year, **rounded**.

### 7c. Route 2 — build `V` first, then `wᵀ V w`

```
  V w :
    AXL row:   37.6(0.5) +  13(0.4) + (−11)(0.1)  =  18.80 + 5.20 − 1.10  =  22.90
    CHR row:     13(0.5) +  29(0.4) +    37(0.1)  =   6.50 +11.60 + 3.70  =  21.80
    EMK row:   (−11)(0.5)+  37(0.4) +  85.6(0.1)  =  −5.50 +14.80 + 8.56  =  17.86
```

**`V w` has a meaning, and it is the best-kept secret of this level:**

> **`(V w)_i` is how much stock `i` moves with the portfolio as a whole.**

Row `i` of `V` is stock `i`'s relationship with each stock in turn; weighting those by how much
of each stock is held gives stock `i`'s relationship with the blend. So AXL co-moves with this
book at `22.9`, CHR at `21.8`, EMK at only `17.86` — EMK is the *most volatile* name in the book
and the one that co-moves with it *least*, because of the `−11`. Those two facts sitting side by
side are the whole reason risk reports exist.

Then:

```
  wᵀ V w  =  0.5(22.90) + 0.4(21.80) + 0.1(17.86)
          =  11.450     +  8.720     +  1.786
          =  21.956        percent-squared        — the same number as Route 1
```

Which gives a third sentence, free:

> **The portfolio's variance is the weighted average of how much each stock moves with the
> portfolio.** `11.450 + 8.720 + 1.786`, and those three add to `21.956` exactly.

As shares of the total: AXL **52.1498%**, CHR **39.7158%**, EMK **8.1345%** (all **rounded**;
they sum to exactly 100%). EMK is 10% of the money and 8% of the variance; AXL is 50% of the
money and 52% of the variance. **Do not name this.** *Marginal contribution to risk* is Level
11's word and Level 11's arithmetic is different from this in a way the player will discover
there. Point, do not label.

### 7d. Why the two routes must agree

Because `wᵀ(X F Xᵀ)w = (Xᵀw)ᵀ F (Xᵀw) = hᵀ F h` — the brackets move, nothing else happens. And
`wᵀ D w = Σ w_i² d_i` because everything off `D`'s diagonal is zero.

The verifier sweeps **729** holding vectors — every triple with entries in tenths from `−0.4` to
`+0.4` — and confirms the two routes give identical exact rationals every time, including
short books and books that do not sum to 1.

**Say which route a desk actually uses, and why.** Route 1, always. A real `V` for the North
America model would be tens of thousands of rows square; nobody forms it. Route 1 needs only a
`K`-long exposure vector and a `K × K` grid, where `K` is the factor count. That is the *entire*
practical payoff of the architecture in §2, and the player should be able to state it in one
sentence without prompting.

### 7e. Predict-then-reveal (round type A) — run this before revealing 4.6857

> *"Here are the three volatilities: AXL `6.13%`, CHR `5.39%`, EMK `9.25%` per month. The book
> is 50/40/10. Commit to a number for the book's risk, and give the reason before the number."*

The weighted average of the three is:

```
  0.5(6.1319) + 0.4(5.3852) + 0.1(9.2520)  =  6.1452%   rounded
```

The truth is **4.6857%** — lower by **1.4595** points, **rounded**, or **23.75%** of the naive
figure, **rounded**.

- **Full bps** only for a player who says *lower*, **and** whose reason is that the three do not
  move in lockstep — with `V[AXL,EMK] = −11` cited by name if they have already seen Section 6.
- **No bps** for "lower" with no reason. That is a lucky guess and `RISK_DESK.md` §6A pays
  nothing for it.
- **Dock** for *higher*. It means risks are being added, which is Section 8's entire subject, and
  it should be caught here rather than there.

---

## 8. Variances add. Risks do not.

**This is the single most common error at this level. Do not explain it — make the player
collide with it.**

### 8a. The illustration, with clearly invented round numbers

*(Labelled invented numbers, per `RISK_DESK.md` §8. They are not from this file and not from the
paper.)*

A book has factor risk **3%** a month and specific risk **4%** a month. What is its total risk?

Almost everybody says 7. It is 5.

```
  3² + 4²  =  9 + 16  =  25          √25  =  5
```

Three, four, five. **Risks combine like the two sides of a right-angled triangle, not like two
numbers in a column.** Adding them would have overstated the truth by `2/5` — forty per cent.

And the reason it is a right angle, said now and proved in §8d: the model asserts that the factor
part and the specific part have **nothing to do with each other**. Two things with nothing to do
with each other are, in this arithmetic, at right angles.

### 8b. The same test on Book A's real numbers

```
  factor risk    =  4.6000%                    (exact root of 21.16)
  specific risk  =  0.8922%                    rounded, root of 0.796
  ---------------------------------------------------------------
  added:            5.4922%                    rounded  ← WRONG
  the truth:        4.6857%                    rounded, root of 21.956
```

Adding the risks overstates by **0.8065** points, **rounded** — **17.21%** of the true risk,
**rounded**.

But:

```
  21.16  +  0.796  =  21.956          exactly, with nothing left over
```

**Factor variance and specific variance add to the total variance with zero remainder.** The
verifier checks the identity on all **66** long-only books on a tenths grid; on all 66 the
variances add exactly and on **none of them** do the risks.

**Shares of the variance** — and these are the numbers a report prints:

```
  factor:    21.16 / 21.956  =  96.3746%     rounded
  specific:  0.796 / 21.956  =   3.6254%     rounded          (they sum to exactly 100%)
```

### 8c. The warning that goes with those shares — read it before the player over-learns

96/4 is **not** a fact about risk models. It is a fact about *total* risk on a long-only book,
where the market factor's variance of 25 dwarfs everything. Two corrections, both citable:

1. **p.35's famous 50/50 is about ACTIVE risk, not total risk.** **PAPER, p.34:** "The report
   shows that the Active Risk is split equally between common factors and stock specific
   sources." The same report's banner prints **Portfolio Risk 15.62%** and **Active Risk 2.99%**
   — different quantities by a factor of **5.2241** (**rounded**). Section 12 computes the active
   version of Book A
   and the specific share jumps from `3.6254%` to `11.3300%` (both **rounded**), which is the
   same lesson in miniature.
2. **Our toy's specific risks are small because Level 8's two-factor fit was very good by
   construction.** Real single-name specific volatility is a much larger share of a single
   stock's risk than `0.6` out of `37.6`. Say so; do not let a player leave believing specific
   risk is a rounding error.

### 8d. Why there is no third term — the four-term expansion

A sharp player will ask: *"variance of a sum usually has a cross-term. Where did it go?"* They
are right and the answer is a page number.

Take equation (1.7), **PAPER, p.24**: `r = X f + u`, and the paper's own gloss, "`X f` is termed
the common factor return and `u` is the asset specific, or idiosyncratic, return." Take the
variance of both sides:

```
  Var(r)  =  X·Var(f)·Xᵀ  +  X·Cov(f, u)  +  Cov(f, u)ᵀ·Xᵀ  +  Var(u)
                 ↑                ↑                ↑              ↑
              X F Xᵀ          deleted           deleted          ≈ D
```

Equation (1.8) is that expression **with the two middle terms crossed out**, and the licence to
cross them out is printed in the paper's own list of assumptions, **PAPER, p.30**:

> "Factor returns have **zero correlation** with asset specific returns, and specific returns
> from different issuers are unrelated and have **zero correlation**"

**Mark this clearly: the expansion is standard algebra a Level-10 player can do, and it is
absolutely not in the paper.** The paper never writes it and never connects its p.30 bullet to
its own equation (1.8). The connection is **INFER** (`gm/VOCAB.md` files it as a
GM inference, in its §3 entry for *orthogonal*). What the paper *does* supply is the assumption,
stated as an assumption, in one sentence, on the page where assumptions live. That is the honest position and the player should
be able to state it in exactly that shape: *the paper assumes it, out loud, and offers no
evidence for it.*

**And the second half of the p.30 sentence is Level 9's, arriving in the same breath.** "Specific
returns from different issuers are unrelated" is what makes `D` diagonal. Section 13 tests both
halves on this file. Both fail. The direction of the failure is the one **p.28** names.

---

## 9. Traps, and exactly what each wrong belief returns numerically

Every row is computed by the verifier. **Give the number, not the adjective** — "you'd be wrong"
teaches nothing; "you'd have reported 5.6175 instead of 4.6857" teaches permanently. All roots
below are **rounded**; all variances are exact.

| Wrong belief | What it computes | Variance | Risk | Versus 4.6857 |
|---|---|---:|---:|---:|
| 1. "Specific risk diversifies away, drop `D`" | `hᵀFh` only | 21.16 | **4.6000** | −1.83% |
| 2. "Factors are separate things, drop `F`'s off-diagonals" | `25h₁² + 9h₂² + Σw²d` | 31.556 | **5.6175** | **+19.88%** |
| 3. "Just weight each stock's own variance" | `Σ w_i² V_ii` | 14.896 | **3.8595** | **−17.63%** |
| 4. "Total risk = factor risk + specific risk" | `4.6 + 0.8922` | — | **5.4922** | **+17.21%** |
| 5. "Transpose the other one" | `Xᵀ F X` | — | **does not compute** | — |
| 6. "Weights, not squared weights, in `D`" | `Σ w_i d_i = 1.96` | 23.12 | **4.8083** | +2.62% |
| 7. Level 9's divisor, taken the other two ways | see §3c | 21.854 / 22.35 | **4.6748 / 4.7276** | −0.23% / +0.89% |

**Read the table as a whole before dismissing any row.** Trap 2 — the one that *deletes*
information — makes the book look **riskier**, not safer, because on this book the factor
covariance is doing hedging work. Trap 3 — also deleting information — makes it look **safer**.
Deleting information does not have a direction; you have to know which cells you deleted. A
player who has internalised "ignoring correlations understates risk" has learned a slogan, and
trap 2 is here to break it. (Level 9's p.28 direction claim is narrower and survives: it is
about the off-diagonals of the *specific* matrix, in a *long-only* book.)

Trap 7 is the honest one. The divisor argument the player may want to have about `D` moves the
answer by less than one per cent in either direction. Traps 2 and 3 move it by about twenty.
**Spend your scepticism where the numbers are.**

---

## 10. Sabotage round (round type B) — run this before the boss

Hand the player this common-factor matrix and say only: *"one cell of this is wrong. Find it,
say by how much, and repair it — without recomputing `X F Xᵀ` from scratch."*

```
        ┌                        ┐
        │   37     13      −1    │
  M  =  │   13     25      37    │
        │   −1     37      85    │
        └                        ┘
```

**The check they should reach for** is the one Section 6e built: three assets and two factors
means the exposure-free book `z = (1, −2, 1)` must be scored at **exactly zero** by the
common-factor matrix, row by row.

```
  row 1:    37(1) + 13(−2) + (−1)(1)  =  37 − 26 − 1  =  +10      ← fails
  row 2:    13(1) + 25(−2) +  37 (1)  =  13 − 50 + 37 =    0      ← passes
  row 3:    (−1)(1) + 37(−2) + 85(1)  =  −1 − 74 + 85 =  +10      ← fails
```

**Rows 1 and 3 fail, row 2 passes. The matrix is symmetric, so the corrupted cell is where the
two failing rows meet: `(1,3)` and its mirror `(3,1)`.**

Better still, the size falls out for free. `z`'s third entry is `+1`, so row 1's residual **is**
the error in cell `(1,3)`: the printed value is `10` too high, and the true entry is
`−1 − 10 = −11`.

Two things to make the player say afterwards:

- **What the corruption would have cost.** Priced on `M`, Book A comes out at `22.956`
  percent-squared, a risk of **4.7912%** **rounded**, against the true `4.6857%`. A **2.25%**
  error (**rounded**) that no eyeball would ever catch — which is why the structural check exists.
- **The alarm has a second form.** `det M = 12620`, and it should have been exactly `0`. A
  determinant that is not zero on a three-asset two-factor common matrix is a bug, full stop.

The verifier sweeps every symmetric single-cell corruption of `X F Xᵀ` at five different
magnitudes — **30** cases — and `z` catches all thirty.

**CALL BACK.** This is the Level 2 sabotage round in new clothes. There, the check was a balance
that arithmetic *guarantees* (`Σx·u = 0`), and a corrupted residual broke it. Here, the check is
a structure the *model* guarantees (`X F Xᵀ z = 0` for any exposure-free `z`), and a corrupted
covariance breaks it. **Every level from here on has one of these, and finding them unprompted is
what separates a quant from a spreadsheet.**

---

## 11. BOSS ROUND — Book B, the mirror

### 11.1 The setup, as the player receives it

> *"Same three names. Same `F`. Same `D`. New book.*
>
> | | AXL | CHR | EMK |
> |---|---:|---:|---:|
> | **Book B** | 10% | 40% | 50% |
>
> *Give me the total risk of this book, per month, and split it into factor and specific. Show
> the arithmetic. Then tell me why it is not the same as the other book, which held the same
> three names in the same three sizes."*

The last sentence is the round. Book B is Book A with the first and third weights swapped.

### 11.2 The arithmetic, in full

```
  h  =  Xᵀ w :
     market    :  0.1 + 0.4 + 0.5           =  1
     cheapness :  0.1(−2) + 0.4(0) + 0.5(2) = −0.2 + 0 + 1.0  =  +0.8
```

```
  factor variance  =  25(1)² + 2(6)(1)(+0.8) + 9(0.8)²
                   =  25     + 9.6           + 5.76
                   =  40.36                                (exact: 1009/25)
  factor risk      =  √40.36  =  6.3530%  per month        rounded

  specific variance = (0.1)²(0.6) + (0.4)²(4) + (0.5)²(0.6)
                    =  0.006      +  0.64     +  0.15
                    =  0.796                               (exact: 199/250)
  specific risk     = √0.796  =  0.8922%                   rounded

  TOTAL variance    =  40.36 + 0.796  =  41.156            (exact: 10289/250)
  TOTAL risk        =  √41.156  =  6.4153%  per month      rounded
```

Cross-check by Route 2: `V w = (3.46, 31.40, 56.50)` and `w·(Vw) = 41.156`. Same number.

Shares of variance: factor **98.0659%**, specific **1.9341%**, both **rounded**.

The additivity test again: `6.3530 + 0.8922 = 7.2451` **rounded**, against a truth of `6.4153`
**rounded** — an overstatement of **12.94%**, **rounded**.

### 11.3 The mirror question — this is what is actually being marked

> **"Book A and Book B hold the same three stocks in the same three sizes. Their specific
> variances are identical — `0.796` both times, to the last digit. Book B is **36.91%** riskier
> (**rounded**). Where did that come from?"**

A passing answer is one sentence and one number:

> **The `+6` in `F`.** Book A's cheapness exposure is `−0.8` and Book B's is `+0.8`. The
> cross-term is `2 × 6 × 1 × h₂`, so it is `−9.6` for A and `+9.6` for B — a swing of **19.2**
> percent-squared, which is the entire difference between `21.16` and `40.36`. Book A's value
> tilt hedges its market exposure; Book B's growth tilt compounds it. **Same names, same sizes,
> opposite sign on one number.**

Everything else in the two books is identical: same market exposure, same `9 × 0.64 = 5.76` from
the cheapness variance, same specific variance to the last digit. The verifier checks that
`40.36 − 21.16` equals `2 × (2 × 6 × 0.8)` exactly.

**Why the specific variances are identical is worth one extra question**, because a player who
cannot answer it has been pattern-matching: `Σ w_i² d_i` with `d_AXL = d_EMK = 0.6` is unchanged
when the AXL and EMK weights swap. `D` cannot tell the two books apart at all. **Only `F` can.**

### 11.4 The interrogation script (real objections, escalating)

Play a Chief Risk Officer with thirty years and no patience. `gm/PLAYBOOK.md` §L10 has the
matching diagnostic table; these are the escalating versions.

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"Read `X F Xᵀ` to me as a sentence, right to left, with the units at each step."** | `Xᵀ` turns holdings into the portfolio's factor bets (dimensionless in, dimensionless out); `F` turns factor bets into percent-squared; `X` carries a percent-squared answer back onto assets; the result is a variance and the square root is a percent. Names what vanished: the factor index, twice. | "You transpose it to make the dimensions work." |
| **"Your factor risk is 6.35 and your specific risk is 0.89. Those add to 7.25 and you told me 6.42. Explain that before we go further."** | **Variances add; risks do not.** `40.36 + 0.796 = 41.156` exactly; `√41.156 = 6.4153` **rounded**. The right-angle picture, and the reason for the right angle: **p.30**, factor returns are *assumed* to have zero correlation with specific returns. And the tell that the report agrees: p.35's pie sums to exactly 100 because it splits **contributions to variance**, not volatilities. | "Risk isn't additive." "There's a correlation term." *(There is not — the model deletes it by assumption, and the player must name the page.)* |
| **"Which of your three stocks is the risky one?"** | Refuses the question as posed and separates it. **Standalone:** EMK, `√85.6 = 9.2520%` **rounded**, the most volatile of the three. **In Book B:** EMK carries **68.6413%** of the variance (**rounded**). **In Book A:** the *same stock at the same volatility* carries **8.1345%** (**rounded**) — it was 10% of the money there, and the rest of that book sat in AXL, the one name EMK moves *against* (`V[AXL,EMK] = −11`). *Risky* is not a property of a stock alone; it is a property of a stock **and** a book. | Naming EMK and stopping. |
| **"So drop `D`. It's two per cent of your number."** | Two answers, and the first one concedes. On **this** book dropping `D` moves total risk from `6.4153` to `6.3530` — **−0.97%** (**rounded**), and on Book A it is **−1.83%**. Both small, and say so rather than bluffing. But the book Section 6e and Section 12.3 exhibit has **zero** factor risk, so dropping `D` prices a real, funded, leverable book at exactly `0`. `D` is not small; it is small *on long-only books measured against cash*. On the paper's own example report, measured against a benchmark, `D`'s share is **50%** of Active Risk (p.35, read directly). | "You need it for completeness." |
| **"Your market exposure is 1.0 and my report says Portfolio Beta 1.02. Which is which?"** | **PAPER, p.4:** "The market factor exposure of a portfolio should not be confused with its market beta." Exposure is a position — "the fraction of portfolio %NAV invested in equities", footnote 3 adding delta-adjusted derivative exposure. Beta must be computed from portfolio and index exposures **together with** `F`. p.35 prints Portfolio Beta **1.02** as its own banner item. **Never attribute the beta formula in the p.4 margin to BlackRock** — `notes/` records it as a reader's handwritten pen annotation, not printed text. | "They're the same thing when you're fully invested." Or quoting the margin formula as the paper's. |
| **"Prove your `V` isn't nonsense. One check, ten seconds."** | Any of: it is symmetric; every diagonal entry is positive; `X F Xᵀ` alone has determinant exactly `0` and must have, because three assets came out of two factors; the exposure-free book `(1, −2, 1)` is scored at exactly `0` by the common part and at `17.2` by `V`. | "It looked right." |

### 11.5 Pass conditions

All five, and the third is the level:

1. **`6.4153%` per month**, with `40.36` and `0.796` shown separately and the arithmetic visible.
2. The additivity test survived: the player did **not** offer `7.2451`, or offered it and caught
   it unprompted.
3. **Every multiplication read aloud as a sentence** — `Xᵀ`, `F`, `X`, `+ D` — with rows and
   columns named and with the vanishing index identified at least once. *Fluent computation with
   no sentence is a fail at this level.* Send them to Section 4, not Section 5.
4. The mirror question answered by naming the `+6` and the sign of `h₂`, not by re-running the
   arithmetic and shrugging.
5. Under interrogation, at least one structural check produced **unprompted**.

**Fail modes and where to drop to** (this expands `gm/PLAYBOOK.md` §L10):

| They say | The broken rung | Drop to |
|---|---|---|
| "It's matrix multiplication" | Hand-wave. Dock 20 | Section 4, then redo Section 5 with **one** factor and **two** assets, entirely in scalars |
| Gets the order backwards, cannot say which side is the portfolio | The meaning of a column has not survived from Level 3 | Level 3 — what one column of `X` is, and whose numbers are in it |
| Correct sentences, no units | Tier 3. Units are how they catch their own errors for the rest of their career | Stay at Level 10 one round: percent, percent-squared, and where the root goes back in |
| Adds the risks and defends it | The level's core error, live | Section 8a, the 3-4-5 triangle, then Section 8b on their own numbers |
| "And you add `D` because the model can't explain everything" | Tier 4 sentence. Ask which number on p.35 that `D` is | Return: Specific is **50%** of Active Risk on the paper's own example report |

---

## 12. The same machinery against a benchmark

**Do not skip this.** It is fifteen minutes, it unlocks a word the player will need in every
conversation they ever have about a portfolio, and it is the bridge to Level 11.

Everything so far measured the book against **cash** — how much does this book move, full stop.
Almost nobody is paid on that. A manager is paid on how the book does **against its benchmark**.

The machinery does not change at all. **Subtract the benchmark's weights from the portfolio's,
and run exactly the same three lines on the difference.**

### 12.1 The benchmark, and Book A's active bet

| | AXL | CHR | EMK |
|---|---:|---:|---:|
| Book A | 50% | 40% | 10% |
| Benchmark | 40% | 50% | 10% |
| **active `a = w − b`** | **+10%** | **−10%** | **0** |

The active weights sum to **zero** — always, because both rows sum to 1. And that single fact
changes the character of the answer:

```
  active exposures  h  =  Xᵀ a :
     market    :  0.1 − 0.1 + 0        =  0        ← the market bet cancels exactly
     cheapness :  0.1(−2) − 0.1(0) + 0 = −0.2
```

```
  active factor variance   =  9 × (−0.2)²  =  0.36        (the 25 and the 6 are multiplied by 0)
  active factor risk       =  √0.36  =  0.6%  per month   (EXACT root: 3/5)

  active specific variance =  (0.1)²(0.6) + (−0.1)²(4) + 0  =  0.006 + 0.04  =  0.046
  active specific risk     =  √0.046  =  0.2145%          rounded

  ACTIVE variance          =  0.36 + 0.046  =  0.406      (exact: 203/500)
  ACTIVE risk              =  √0.406  =  0.6372%          rounded
```

Shares: factor **88.6700%**, specific **11.3300%**, both **rounded**. Compare with the same book's
*total* split of 96.4/3.6: **the specific share is 3.1252 times bigger** (**rounded**), and nothing
about the stocks changed. It happened because subtracting the benchmark **deleted the market
factor**, which was carrying nearly all the common risk. That is the mechanism behind p.35's 50/50
pie, and now the player has felt it rather than been told it.

### 12.2 The number that stops the room

```
  Book A's total risk    =  4.6857%     rounded
  Benchmark's own risk   =  4.7055%     rounded          (its variance: 21.04 + 1.102 = 22.142)
  ----------------------------------------------------
  difference             = −0.0198%     rounded
  ACTIVE risk            =  0.6372%     rounded
```

**The book is slightly *less* volatile than its benchmark, and it still carries two thirds of a
percent of active risk a month.** Risks do not subtract any more than they add. A manager who
says "my portfolio is less risky than the index, so I'm not taking risk" has said something
false, and this is the arithmetic that shows it.

**And the paper's own report says it too.** **PAPER, p.35** banner, read directly from the scan:
Portfolio Risk **15.62%**, Benchmark Risk **14.98%**, Active Risk **2.99%**.

```
  15.62 − 14.98  =  0.64          the report's Active Risk  =  2.99
```

The reported Active Risk is **4.6719 times** the difference of the two risks (**rounded**), on a
real portfolio in a published document. *(Carry the audit's doubt: the middle digit of
`2.99` is blobby — `2.89` is not fully excluded — and the last digit of `15.62` is soft — `15.67`
is not fully excluded. `14.98` and `1.02` are clean. **Neither alternative reading rescues
subtraction**: `15.67 − 14.98 = 0.69`, still nowhere near `2.89`. Say the uncertainty out loud;
the point survives it.)*

### 12.3 Book C — an active bet the factors cannot see at all

Same benchmark. A different book:

| | AXL | CHR | EMK |
|---|---:|---:|---:|
| Book C | 50% | 30% | 20% |
| Benchmark | 40% | 50% | 10% |
| **active** | **+10%** | **−20%** | **+10%** |

That active vector is one tenth of `z = (1, −2, 1)` — **the exposure-free direction from Section
6e**. So:

```
  active exposures     =  ( 0 , 0 )
  active factor risk   =  0            exactly. Not small: zero.
  active specific var  =  (0.1)²(0.6) + (0.2)²(4) + (0.1)²(0.6)  =  0.006 + 0.16 + 0.006  =  0.172
  ACTIVE risk          =  √0.172  =  0.4147%   rounded      —  100% specific
```

**A real, funded, non-trivial bet — overweight both extremes, underweight the middle — that the
model's factors are structurally incapable of seeing.** Drop `D` and this book is reported at
zero active risk. It is the cleanest possible argument for why `D` exists, and it is also, in one
move, the answer to *"is a factor model enough?"*: **no, and here is a book that proves it in
four multiplications.**

### 12.4 The word

Now hand the word over (`gm/VOCAB.md` row 13 unlocks it here, once `V` exists):

> **Tracking error** is the industry word for the number you just computed: the risk of the
> *difference* between a portfolio and its benchmark. **The BFRE paper never uses the phrase —
> zero occurrences in 65 pages.** Its word is **Active Risk**, and that is what the banner on
> p.35 says. Both words, one number. Hearing one and not instantly producing the other is a tell
> that fails Victory Condition 2, so drill the switch in both directions before moving on.

*(Note the small split in the game's own reference files: `gm/VOCAB.md` row 13 books* tracking
error *at L10, once `V` exists; `gm/LEVEL_ANCHORS.md` §2 books* active risk *at L11, where the
report is actually read. Hand over both words here — they name the same number — and leave the
report to Level 11.)*

---

## 13. The plus sign is an assumption, and here is exactly what it costs

**Run this after the boss round, not before.** It is the level's real intellectual content and
it is the last thing before Level 11.

Section 8d crossed two terms out of an expansion because p.30 says to. **This section puts them
back and measures them, on this file, exactly.**

### 13.1 What actually happened to Book A over the five months

Level 8's returns file, for the three held names, with `w = (0.5, 0.4, 0.1)`:

| | m1 | m2 | m3 | m4 | m5 |
|---|---:|---:|---:|---:|---:|
| AXL | 0 | −3 | +6 | +6 | −8 |
| CHR | +9 | +3 | −1 | +1 | −8 |
| EMK | +16 | +13 | −2 | −2 | −4 |
| **Book A** | **+5.2** | **+1.0** | **+2.4** | **+3.2** | **−7.6** |

Mean `+0.84`. Deviations `+4.36, +0.16, +1.56, +2.36, −8.44`. Sum of squares `98.2720`, divided
by `T − 1 = 4`:

```
  realised variance   =  24.568   percent-squared        (exact: 3071/125)
  realised volatility =  4.9566%                         rounded
  the model said      =  21.956                          →  a gap of 2.612
```

**The model's number is the smaller one.** Do not rush past that. Ask the player to predict the
sign of the gap before revealing it, and pay for a right answer with a reason.

### 13.2 The four terms, computed

Split Book A's realised return each month into its two pieces, using the factor returns and the
misses the player already has:

```
  factor part  p_f  =  1×f_Mkt − 0.8×f_Chp  =  +3.8, +1.8, +2.6, +4.6, −6.8
  specific part p_u =  0.5u_AXL + 0.4u_CHR + 0.1u_EMK
                                            =  +1.4, −0.8, −0.2, −1.4, −0.8
  and p_f + p_u                             =  +5.2, +1.0, +2.4, +3.2, −7.6   ✓
```

Now the same mean-subtracted, divide-by-4 estimator on each piece:

| Term | What it is | Value |
|---|---|---:|
| `Var(Xf)` | the common part | **21.16** |
| `2·Cov(Xf, u)` | **the term (1.8) deletes** | **+2.26** |
| `Var(u)` | the true specific part, off-diagonals and all | **1.148** |
| **sum** | | **24.568** ✓ |

**Term one is exactly the model's factor variance — to the last digit**, because `F` was built
with this same estimator. The model gets the common half exactly right on its own data. **The
entire gap is in the other two terms**, and both are things (1.8) asserts away.

### 13.3 Splitting the specific gap into its two named causes

Build the *full* residual covariance matrix of the three names — same estimator, mean
subtracted, divisor 4 — and do not throw the off-diagonals away:

```
        ┌                      ┐
  Ω  =  │  0.7    0.8    0.7   │   AXL
        │  0.8    3.2    0.8   │   CHR
        │  0.7    0.8    0.7   │   EMK
        └                      ┘
```

**Look at the corners.** `Ω[AXL,EMK] = 0.7` and both diagonal entries are `0.7`: the correlation
between AXL's and EMK's specific returns is **exactly 1**. And it is not an accident of rounding
— go back to §3c and read the two miss rows: `+1, 0, +1, −1, 0` and `+1, 0, +1, −1, 0`. **They
are the same five numbers.** *(This is an artifact of a five-month toy with a symmetric exposure
column, not a claim about real stocks. Say so. Then use it, because Level 9's entire lesson is
sitting in this file waiting.)*

Now three numbers, each one a named cause:

```
  model's specific variance   (D diagonal, divisor 5, no mean)   =  0.796
  same book, diagonal only, but the OTHER convention (÷4, mean)  =  0.694     → −0.102
  same book, full Ω, off-diagonals included                      =  1.148     → +0.454
```

- **The divisor convention** — the argument §3c said was small — moves it by **−0.102**.
- **The diagonal assumption** — Level 9's whole subject — moves it by **+0.454**, four and a half
  times as much, and in the direction that makes the reported number **too low**.
- **The deleted cross-term** adds a further **+2.26** on top.

And they reconcile exactly: `(1.148 − 0.796) + 2.26 = 0.352 + 2.26 = 2.612`, which is the gap.

### 13.4 What to say about it

Three claims, each with its own tag, and do not blur them:

- **PAPER, p.28**, on ignoring specific-return correlation: it "would lead to under (or over)
  prediction of specific risk in a **long-only** (long-short) portfolio context." Book A is
  long-only. The model under-predicted. **The paper called the direction and the paper was
  right.**
- **PAPER, p.27**, and this is why the failure is not a "gotcha": BFRE does **not** ship the
  purely diagonal version. "The asset specific covariance matrix is made up of two components: a
  vector of asset specific risk forecasts and a sparsely populated unit diagonal matrix
  containing non-zero, off-diagonal specific return correlations." p.24's "a diagonal matrix" is
  introduced by "**In general** a multi-factor model decomposes asset returns as follows" — it is
  the generic form. `gm/CRITIQUE.md` **CS-3** files "they contradict themselves three pages
  apart" as a named cheap shot; do not let the player leave holding it.
- **INFER, and ours**: on this file the cross-term is *bigger* than the whole specific
  correction, and the paper offers no evidence at all for `Cov(f, u) = 0` — it is one clause in
  one bullet on p.30. With five observations our `+2.26` is itself a very noisy number and proves
  nothing about BFRE. What it does prove is that the plus sign in (1.8) is **load-bearing**, and
  a player who can say that sentence and produce the four-term expansion behind it has done the
  whole of Level 9's brief in a single move.

---

## 14. Names unlocked, and ladder position

### 14.1 Names unlocked at the end of this level

| Name | Where it was earned | The BFRE position |
|---|---|---|
| **asset covariance matrix**, `Σ` | Section 6c — the object exists now | **PAPER.** p.24, the where-list under (1.8): "`Σ` : asset covariance matrix". The game writes `V`; the paper writes `Σ`. |
| **specific risk matrix**, `Δ` | Level 9 built it; this level places it | **PAPER.** p.24: "`Δ` : specific risk matrix (a diagonal matrix of asset specific risk forecasts)". The game writes `D`. |
| **common factor return** | Sections 5–6, the object `X f` | **PAPER.** p.24: "`X f` is termed the common factor return and `u` is the asset specific, or idiosyncratic, return." |
| **tracking error** | Section 12 | **The phrase appears nowhere in the 65 pages.** BFRE's word is **Active Risk** (p.34, p.35). Hand over both and drill the switch. |
| **active risk** | Section 12 | **PAPER.** p.34 prose and the p.35 banner. `gm/LEVEL_ANCHORS.md` books this at L11; introduce it here, read the report there. |

**Do not unlock here:** *marginal contribution to risk* (Level 11 — and note the paper has **no
formula** for it and never uses the phrase); *bias statistic* (Level 12).

### 14.2 Ladder position after this level

| Concept | Tier reached | What is still missing for tier 5 |
|---|---|---|
| Assembling `V = X F Xᵀ + D` | **5 — Rebuild** | nothing; this is the level |
| Reading a matrix product as a sentence | **4 — Defend** | tier 5 needs it done on a model they did not build |
| Total / factor / specific decomposition | **5 — Rebuild** | nothing |
| Variances add, risks do not | **4 — Defend** | survives the CRO; tier 5 is spotting it in someone else's report |
| Active risk against a benchmark | **3 — Derive** | Level 11, on a real report |
| `Cov(f, u) = 0` as a load-bearing assumption | **3 — Derive** | tier 4 needs the Level 12 exchange |
| Structural checks (`det = 0`, the exposure-free book) | **4 — Defend** | tier 5 is producing one unprompted on a new model |

### 14.3 What this level does NOT settle, stated so the player is not misled

1. **How `F` is really built.** p.27 gives the window (104 weeks), the weighting (exponential
   decay), the half-life (26 weeks), and then defers everything else: "Model users are referred
   to the BRS Covariance Matrix Estimation documentation for technical details on the factor
   covariance matrix methodology." Level 8 said this; it is still true.
2. **How `D` is really built.** p.27 and Table 1.3 (p.28) give half-lives, observation counts and
   a Newey–West lag; the weighting function that blends a time-series forecast with a
   cross-sectional one is described in words and **its functional form is not given** (p.28).
3. **Whether `D` should be diagonal.** Level 9's subject, and Section 13 measured the cost on one
   toy book only. Five observations prove nothing about a real model.
4. **How to decide which position to cut.** That is Level 11, the arithmetic is a nudge argument,
   and **the paper contains no formula for it at all**.
5. **How anyone knows `V` is any good.** The Model Testing chapter (pp.32–33) prints **no
   values**, no pass/fail criteria and no summary results. That is Level 12.
6. **Annualisation.** Every `×√12` on this page is ours and assumes independent months. p.30 says
   BFRE's 1-month risk estimates take "into account daily serial correlations in factor returns
   and asset specific returns", so BFRE does **not** do what we just did.

---

## 15. Back to BFRE — what this machinery does in the real model

### 15a. p.24 — the two lines that are the whole model

**PAPER, p.24**, lead-in and equation:

> "In general a multi-factor model decomposes asset returns as follows:"
>
> `r = X f + u`   (1.7)
>
> where `r` : asset returns (in excess of the local risk-free rate); `X` : set of factor
> exposures based on asset characteristics; `f` : return to each factor; `u` : asset specific
> return.

And one line below:

> `Σ = X F Xᵀ + Δ`   (1.8)
>
> where `Σ` : asset covariance matrix; `F` : factor covariance matrix; `Δ` : specific risk
> matrix (a diagonal matrix of asset specific risk forecasts).

**Equations (1.7) and (1.8) are one line apart on one page, and they are the entire model.** The
other sixty-four pages of the document exist to say what goes into `X` (pp.39–54, every substyle
definition), what goes into `F` (p.27, and then a deferral), and what goes into `Δ` (pp.27–28).
Say that to the player at the end of this level; it reorganises everything they have done so far.

### 15b. The ingredient list, and the one word in it that matters

**PAPER, p.24** — recorded in `notes/` as a close paraphrase of the page, so quote it as a
paraphrase, not as a printed sentence: portfolio risk is calculated from portfolio holdings
(asset weights), portfolio-level factor exposures **aggregated from the asset level**, a factor
covariance matrix, and asset specific risk forecasts.

"Aggregated from the asset level" **is** `h = Xᵀ w`, Section 7b. The paper names the operation in
four words and never writes it down. That is worth pointing at: the player has just written down
something the document assumes its reader can supply.

### 15c. p.4 — the trap with the player's name on it

**PAPER, p.4:** "The market factor exposure of a portfolio should not be confused with its market
beta." Exposure is a **position** — "the fraction of portfolio %NAV invested in equities",
footnote 3 adding "and delta-adjusted market exposure for derivatives". Beta to an index is a
different quantity, computed from the factor exposures of portfolio and index together with `F`.

Our Book A has market exposure exactly **1** because it is fully invested. p.35's example
portfolio prints **Portfolio Beta 1.02** in its banner. Those are two different numbers about two
different things and they are allowed to disagree.

**Do not attribute the beta formula to BlackRock.** `notes/` records the portfolio-beta formula on
p.4 as a **reader's handwritten pen annotation in the margin**, not as printed text. The printed
sentence says only that beta "can instead be computed via the risk factor exposures of the
portfolio and market index, together with the factor covariance matrix". Quoting the margin
formula as the paper's is exactly the fabrication `gm/LEVEL_ANCHORS.md` §0 exists to prevent.

### 15d. p.34 and p.35 — the assembled number, in a real report

**PAPER, p.34:** "Active Risk is then decomposed along the different factor blocks in the model,
shown in the pie chart: styles (including the market factor), industries, countries and
currencies. The report shows that the **Active Risk is split equally between common factors and
stock specific sources**. Style and industry factors account for most of the common factor
risks."

**PAPER, p.35**, Figure 1.18, the pie "Risk Contributions by Block", read directly from the scan:

| Slice | Share |
|---|---:|
| **Specific** | **50%** |
| Style | 25% |
| Industry | 14% |
| Country | 6% |
| FX | 4% |
| Act Sec | 1% `[INFERRED — the glyph reads 1 or 2; 1% is recorded only because the six then sum to exactly 100]` |

The five other values are read directly and are unambiguous. `25 + 14 = 39` of the 50
common-factor points, which is p.34's "Style and industry factors account for most of the common
factor risks", checked. And the pie summing to exactly 100 is itself the Section 8 lesson in print: **a
pie can only add up because it is splitting variance contributions, not volatilities.** Six
square roots would not sum to anything.

**The scale check, and say clearly that it is a check and not a target.** Book A annualised is
**16.2318%** **rounded**; p.35's Portfolio Risk is **15.62%**. Those are the same order of
magnitude, which tells you nothing except that nobody has slipped a factor of ten. A different
book on a different model would land somewhere else entirely, and a player who *tunes* a rebuild
until it hits 50/50 has committed the error `gm/PLAYBOOK.md` flags at ★ THE REBUILD.

### 15e. Where this level's machinery ends up in the finished model

1. Levels 1–7 fill `X` and produce a factor return series.
2. Level 8 turns that series into `F` — p.24's "`F` : factor covariance matrix".
3. Level 9 turns the misses into `Δ` — p.24's "`Δ` : specific risk matrix".
4. **Level 10 is equation (1.8) itself**: `Σ = X F Xᵀ + Δ`, p.24.
5. Level 11 reads a number off `Σ` for one position — the bars on p.35.
6. Level 12 asks how anybody knows `Σ` is right, and finds pp.32–33 printing no values at all.

**Nothing downstream of this page exists without it.** Every risk number, every beta, every
attribution, every optimiser run in Aladdin (p.34: the Green Package, PRT, Portfolio Construction
and Prism) consumes `Σ`. The assembly is two matrix products and an addition, and they are the two
most important multiplications in the document.

### 15f. What the notes do NOT support — searched across all 65 transcribed pages

- **The four-term expansion of `Var(X f + u)` is not in the paper.** Not in any form. The paper
  states the assumption (p.30) and prints the result (p.24) and never connects them. Section 8d
  is **ours**.
- **No worked example of (1.8) appears anywhere.** No numeric `X`, no numeric `F`, no numeric `Δ`,
  no numeric `Σ`. Every matrix on this page is the game's.
- **No formula for portfolio risk is printed.** `wᵀ Σ w` does not appear; nor does `hᵀ F h`. The
  ingredient list on p.24 is prose. The **only** expression of that shape anywhere in `notes/` is
  the `X_pᵀ F X_b / X_bᵀ F X_b` beta formula on p.4 — recorded as a **reader's pen annotation**,
  not printed text, and never to be attributed to BlackRock.
- **The phrase "tracking error" has zero occurrences.** The paper says Active Risk.
- **No formula for marginal contribution to risk, and the phrase never appears.** "Contribution"
  occurs as a chart axis label on p.35 and as prose on p.34, and that is the whole of it.
- **The approach is justified by precedent, not by evidence.** p.24, footnote 13: the method is
  "similar to that used in the fundamental factor risk model literature", citing Rudd and Clasing
  [24], Grinold and Kahn [25] and Connor et al. [17]. **No empirical comparison against any
  alternative assembly is offered anywhere in the paper.** File that for Level 12.

**Landing sentence:**

> "What you just assembled is printed on page 24 as equation (1.8), `Σ = X F Xᵀ + Δ`, one line
> below equation (1.7), `r = X f + u`. Those two lines are the entire model, and the other
> sixty-four pages exist only to say what goes in `X`, what goes in `F`, and what goes in `Δ`.
> Two housekeeping notes before you read them. The paper writes `Σ` and `Δ` where we have been
> writing `V` and `D` — a letter swap, not a different model. And page 4 has a trap with your
> name on it: 'The market factor **exposure** of a portfolio should not be confused with its
> market **beta**' — which is why the report on page 35 can print a Portfolio Beta of 1.02 as a
> separate quantity from anything in your `X`."

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level10.py     # 447 exact-rational assertions, exits 0
```

The script recomputes every figure on this page in `fractions.Fraction`, from the raw Level 8
returns file upward: the five factor-return solves and all 25 misses, with both Level 2 balance
conditions in all five months; `F` rebuilt from those series and `D` rebuilt from those misses,
under all three divisor conventions plus the Level 6 leverage check that the five leverages sum
to `k = 2`; `F Xᵀ` and `X F Xᵀ` cell by cell, both bracketings, the closed form
`25 + 6(x_i + x_j) + 9 x_i x_j` for all nine cells, symmetry, and `V = X F Xᵀ + D`; every implied
volatility and correlation, with and without `D`; `det(X F Xᵀ) = 0`, the exposure-free vector
`(1, −2, 1)`, `det V = 332661/25`, and a sweep of **342** integer holding vectors confirming `V`
never returns a non-positive variance; Book A by both routes with `V w` and the per-name
variance shares; a sweep of **729** holding vectors confirming the two routes agree exactly; the
naive weighted average of volatilities and the 23.75% diversification gap; the 3-4-5 illustration
and the additivity test, plus a sweep of all **66** long-only books on a tenths grid where the
variances always add and the risks never do; all seven traps with the exact number each returns;
the sabotage matrix, the row-by-row `z` test, the repair, and a sweep of **30** symmetric
single-cell corruptions all caught; the whole boss round including the `19.2` percent-squared
cross-term swing between Books A and B; the benchmark, both active books, and the
factor-cancels-to-zero case; the full four-term expansion of Book A's realised variance,
reconciled to the last digit, with the specific gap split into its divisor part and its
diagonal-assumption part; and the p.35 banner and pie arithmetic, including the two alternative
digit readings the audit could not exclude.

Its final section exists purely for this page's typography: **every decimal the markdown prints**
— every intermediate product written out in longhand, every monthly series, every two-decimal
short form used in the interrogation dialogue — is re-rendered from the exact rational and
compared string-for-string against what is written above. A rounding that drifted by one in the
last digit fails the script.

If any printed value ever disagrees with this markdown, the markdown is wrong.
