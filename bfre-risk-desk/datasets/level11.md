# Level 11 — The Desk

Every number below is recomputed in exact rational arithmetic by `tools/verify_level11.py`
(626 assertions plus 3,815 swept cases, exits 0). Nothing here is rounded by hand. Where a
decimal does not terminate it is written with the word **rounded** next to it; every other
decimal on this page is exact.

> **DIFFICULTY — honestly, in three parts** (`prompt/RISK_DESK.md` §8, BE HONEST ABOUT
> DIFFICULTY).
>
> **The arithmetic is the easiest on the level list.** One matrix-times-vector — twenty-five
> multiplications, most of them by a two-digit number — then five divisions and five
> multiplications. There is no new estimation, no new matrix, no new data. `V` was assembled at
> Level 10 and is carried across untouched.
>
> **One step is genuinely subtle, and it is Section 4c**: going from *"the variance moved by
> this much"* to *"the risk moved by this much"*. That step is a nudge argument, it is the same
> nudge argument the player built at Level 1, and it is the reason this level exists at the
> point in the game where it does. Do not let a player past it with "you differentiate the
> square root". They have no calculus and they do not need any.
>
> **One thing here IS graduate-level and is deliberately not needed.** The general theorem that
> makes risk contributions sum to exactly the total — Euler's theorem on homogeneous functions —
> is a university result. Section 5 gets the same conclusion two ways with no calculus at all:
> a scaling argument, and one line of ordinary algebra. Say plainly that the named theorem
> exists and that the player is not being asked for it. (`gm/PLAYBOOK.md` §"beyond scope" files
> this exact concession.) Eigen-decomposition (Level 8), shrinkage (Level 8) and the
> Newey–West serial-correlation adjustment (p.27, p.28) remain graduate-level and none of them
> is used on this page.

> **THE BIG GAP, AND SAY IT BEFORE THE LEVEL STARTS, NOT AFTER.** The BFRE paper contains **no
> formula for marginal contribution to risk**, no derivation of a risk decomposition, and the
> phrase "marginal contribution" appears **nowhere in its 65 pages**. What it prints is the
> *output*: a chart axis labelled "Contrib. (% of Act. Risk)" on p.35 and one paragraph of
> prose on p.34. **Level 11's mathematics is entirely ours. Only its output format is citable.**
> A player who is later told "show me where the paper says that" and points at a page has been
> taught a fabrication, and that is the single worst failure available in this repository
> (`gm/LEVEL_ANCHORS.md` §0).

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the miss `u`, scored by its size and not its sign.
**From Level 1** — `b = Σxr/Σx²`, derived by **nudging**: change one thing a little, watch a
total move, and read the answer off the movement. **This level is that argument again.**
**From Level 2** — the balance condition `Σx·u = 0`, one per column, forced by the arithmetic.
**From Level 3** — two columns, two balance conditions, one simultaneous solve.
**From Level 4** — the determinant, and what a determinant of zero means.
**From Level 5** — centering; a column of ones is an intercept; `Cov/Var`.
**From Level 6** — degrees of freedom, leverage, and the standard error built by enumeration.
**From Level 7** — the same cross-sectional regression run month after month.
**From Level 8** — `F`, and `hᵀFh`, the rule that turns factor bets into one variance.
**From Level 9** — `D`, and the difference between what least squares *guarantees* and what
BFRE *assumes*.
**From Level 10** — `V = X F Xᵀ + D`; `wᵀVw`; **variances add and risks do not**; and, in
§7c, the object `V w` — *"how much stock `i` moves with the portfolio as a whole"* — which
Level 10 deliberately pointed at and refused to name.

Level 11 asks the one question none of those answered:

> You have one number for the whole book. A portfolio manager wants to know **which position to
> cut**. The book's risk is not the sum of anything — Level 10 proved that risks do not add — so
> how can any single position be said to own a share of it at all?

Four genuinely new things:

| | What Level 11 adds |
|---|---|
| **A derivative, built without calculus** | How much does total risk move if I add a little to position `i`? Section 4, by nudging — the Level 1 tool, third outing. |
| **A decomposition that is exact** | Five numbers that sum to the total risk with **nothing left over**, on an object that is not a sum. Section 5. |
| **Two rankings that disagree** | Position size and risk contribution are different orderings of the same book, and Section 6 builds a book where they disagree in two separate places. |
| **A negative contribution** | A real, funded position whose marginal contribution is **below zero**: adding to it *reduces* the risk of the book. Section 8. |

**Names deliberately withheld until Section 12.** Do not say *marginal contribution to risk*
or *risk contribution* at the table before Section 4e. Before then say: *what one more point of
this position does to the total*, and *this position's share of the risk*. (`gm/VOCAB.md`
row 14 sets the unlock at L11.) **Already unlocked, at Level 10 §12.4** — *active risk* and
*tracking error*, two words for one number; drill the switch again here, because this is the
level where the report is actually read.

---

## 1. The story — no mathematics

*(Analogy bank: `gm/ANALOGIES.md` **C16-A**, canoe trim. **Check the burn ledger first.** C16-A
sits in the same "balance-a-vehicle" family as **C4-B**, the aviation-trim story used at Level 3
— `gm/ANALOGIES.md` §2 warns in as many words that if C4-B was rejected then, C16-A will be
rejected here for exactly the same reason. If so, go to **C16-B**, the fire officer and the
terrace, or **C16-C**, the choirmaster. Do not open two of them.)*

Two people load a canoe for a week on the water. All morning they have been asking the wrong
question, which is *"what is the heaviest thing we're carrying?"* The answer is a barrel of
drinking water, and the barrel is not what makes the canoe tippy. It sits low, dead in the
middle, and it may as well be part of the hull.

What makes the canoe tippy is a small dry bag. Move it from the centre out to the left gunwale
and you can feel the boat get nervous — not because the bag is heavy, but because there is
already weight out on the left. Move that same bag to the *right* side instead and the boat
settles: same object, same weight, opposite effect, and the thing that decided which was true
was not the bag at all. It was what was already in the boat.

By the end of the loading they have stopped weighing things. They judge every item by one
question only: **what does one more kilogram of this, placed here, do to the whole boat?** And
they have learned that the answer to that question changes every time they move something,
because the boat they are asking about has changed.

---

## 2. Mapping the story onto the model, line by line

Go down the table row by row. Do not skip a row because it looks obvious; the skipped row is
where the misconception lives.

| In the story | In the model |
|---|---|
| an item of kit | a position in the portfolio |
| the item's weight | `w_i`, the size of the position |
| how tippy the canoe is | `√(wᵀVw)`, the risk of the whole book |
| **what one more kilogram, placed there, does** | **the marginal contribution of position `i`** — the object this level builds |
| the barrel that is not the problem | a large position with a small contribution |
| the small dry bag that is | a modest position with a large contribution |
| weight already sitting out on the left | the rest of the book's exposures — the reason `V w` and not `V_ii` |
| the same bag improving stability on the right | a **negative** marginal contribution: a genuine hedge |
| the answer changing every time you move something | the number is only true of today's book — and the report on p.35 is the **Equity Daily Risk** report |
| balancing the boat | reducing risk by offsetting, not by shrinking |

**The awkward question, and ask it exactly like this** (round type D):

> *"If moving the bag to the right makes the boat steadier, why not move everything to the
> right?"*

- **Landed** sounds like: because the answer changes as you move things. The moment the right
  side is loaded, the *next* bag placed there makes it worse. The number is a statement about
  **the boat as it currently stands**, not a permanent property of the bag.
- **Not landed** sounds like: *"because you'd capsize the other way."* Right conclusion, and
  they have not said the load-bearing thing. Half bps, then ask: *"what changed between the
  first bag and the last one?"*

**Where the story breaks, and say it out loud.** A canoe's balance is a rigid physical fact you
can feel through your knees. Portfolio risk is a **forecast** built out of `F` and `D`, both of
which are estimates from a short window (p.27: 104 weeks, 26-week half-life). The canoe cannot
lie to you about which way it will tip. The model can, and in a direction nobody has observed it
will do so confidently. Every criticism the player learned to make of `F` at Level 8 and of `D`
at Level 9 lands on every number in this level.

---

## 3. The dataset — nothing new is estimated

Everything in this section was built by the player in earlier levels. **Say that before showing
any of it.** The verifier does not take it on trust either: it rebuilds `F` from the five
monthly factor returns of Level 7, rebuilds `D` from the twenty-five misses of Level 8, and
re-checks both Level 2 balance conditions in all five months, before assembling `V`.

### 3a. The universe and `X`

| Stock | market `1` | cheapness `x` | `d` = specific variance |
|---|---:|---:|---:|
| AXL | 1 | −2 | 0.6 |
| BRN | 1 | −1 | 2 |
| CHR | 1 | 0 | 4 |
| DLT | 1 | +1 | 2 |
| EMK | 1 | +2 | 0.6 |

`X` is 5 rows (assets) by 2 columns (factors). The cheapness column sums to zero across the
universe — Level 5's centering, still holding. **PAPER, p.4:** "all equity assets have a **unit
exposure** to this factor", which is why the first column is all ones.

`d` is the Level 9 diagonal, `Σu²/T` with `T = 5`: the sums of squared misses are
`3, 10, 20, 10, 3`, so `d = 3/5, 2, 4, 2, 3/5` percent-squared per month. Level 10 §3c argued the
divisor and priced the two rivals; that argument is unchanged and is not reopened here.

### 3b. `F`, unchanged from Level 8

```
        ┌            ┐
  F  =  │  25     6  │        percent-squared, per month
        │   6     9  │
        └            ┘
```

Market volatility `√25 = 5.0%` exact; cheapness volatility `√9 = 3.0%` exact; correlation
`6/(5×3) = 0.40` exact; `det F = 189`, so the two columns are not collinear (Level 4).

**Hold on to the `+6`.** It is small and it is about to do most of the work on this level.

### 3c. `V`, the whole-universe grid

Level 10 built `V` for the three names its book held. The same two products, run on all five
rows of `X`, give the whole grid. Every cell obeys the closed form Level 10 §6a proved:

> `V[i][j] = 25 + 6(x_i + x_j) + 9 x_i x_j`, plus `d_i` when `i = j`.

```
            AXL     BRN     CHR     DLT     EMK
  AXL      37.6      25      13       1     −11
  BRN        25      24      19      16      13
  CHR        13      19      29      31      37
  DLT         1      16      31      48      61
  EMK       −11      13      37      61    85.6
                                     percent-squared, per month
```

The verifier checks all 25 cells against the closed form, checks symmetry, and checks that the
`(AXL, CHR, EMK)` sub-block is bit-for-bit the `V` of Level 10.

**Standalone volatilities — one name at a time, no portfolio in sight:**

| | AXL | BRN | CHR | DLT | EMK |
|---|---:|---:|---:|---:|---:|
| variance `V_ii` | 37.6 | 24 | 29 | 48 | 85.6 |
| volatility, %/month | **6.1319** | **4.8990** | **5.3852** | **6.9282** | **9.2520** |

All five roots are **rounded**. **Write this table on the board and leave it there.** Section 6
is going to contradict the ranking in it, and the contradiction is the level.

### 3d. The book

| | AXL | BRN | CHR | DLT | EMK |
|---|---:|---:|---:|---:|---:|
| **Book D**, `w` | **30%** | 17% | 8% | 15% | **30%** |

Long only, fully invested, weights sum to 1. Two positions are exactly the same size — AXL and
EMK, 30% each — and one, DLT at 15%, is exactly half of them. Those coincidences are
deliberate: they remove every excuse the arithmetic could otherwise offer.

```
  h  =  Xᵀ w :
    market    :  0.30 + 0.17 + 0.08 + 0.15 + 0.30                    =  1
    cheapness :  0.30(−2) + 0.17(−1) + 0.08(0) + 0.15(1) + 0.30(2)
               = −0.60    − 0.17     + 0       + 0.15    + 0.60      = −0.02
```

```
  factor variance    =  25(1)² + 2(6)(1)(−0.02) + 9(−0.02)²
                     =  25     − 0.24           + 0.0036
                     =  24.7636        percent-squared   (exact: 61909/2500)

  specific variance  =  (0.30)²(0.6) + (0.17)²(2) + (0.08)²(4) + (0.15)²(2) + (0.30)²(0.6)
                     =   0.054       +  0.0578    +  0.0256    +  0.045     +  0.054
                     =   0.2364      percent-squared        (exact: 591/2500)

  TOTAL variance     =  24.7636 + 0.2364  =  25        exactly
  TOTAL risk         =  √25  =  5.00%  per month        EXACT root
```

**The book's risk is exactly 5% a month.** That is not luck. The weights were chosen so that the
total variance is a perfect square, which makes every marginal contribution and every
contribution on this page an exact terminating decimal instead of a wall of fractions
(`prompt/RISK_DESK.md` §5 asks for "a tiny dataset the player can compute by hand"; that vile
fractions are a design failure rather than a fact of life is our gloss on it, not the rulebook's
words). Only the standalone volatilities in §3c and the benchmark work in §8 need rounding, and
each is marked. Annualised by `×√12` it is
**17.3205%** a year, **rounded** — and, as at Level 10, **that `×√12` is ours and assumes
independent months, which p.30 says BFRE does not assume.**

**Say this out loud before Section 4:** the book's net cheapness tilt is **−0.02**, which is
nothing. This is, to two decimal places, a pure market bet. Hold that thought; the boss round
turns on it.

### 3e. Three simplifications, declared before they can be mistaken for the model

1. **Five assets, two factors, one month.** BFRE's North America model carries a market factor,
   twelve styles, fifty-four industry rows (fifty-three of them *core* — Level 8 §13c drew that
   distinction from p.25's "all industries **except** the Multi-Sector Holding industry") and a
   country/currency block — a count the paper never prints (Level 8 assembled a floor of ≈71 from
   Table 1.2, p.10, and Table 1.5, p.57, and **that count is ours**).
2. **`V` is treated as known.** It is not. It is a forecast from a 104-week window (p.27). Every
   contribution on this page inherits that.
3. **Percent and percent-squared per month throughout.** BFRE's forecast horizon is **1 month**
   (p.30, PAPER), so monthly is the right unit.

---

## 4. The question, and the nudge that answers it

### 4a. Build the shape before seeing it (round type C — run this first)

> *"You have `V` in percent-squared and a list of weights with no units at all. You want a number
> that answers: **if I add one more point of NAV to EMK, how much does the book's risk change?**
> What are the units of the answer, and what shape must the formula have?"*

The answer they should reach unaided: risk is in **percent**, weight is a **pure number**, so the
answer is in **percent per unit of weight** — which is just percent. And it cannot be built out
of `V_ii` alone, because the canoe story says the effect depends on what is already in the boat.
Something in the formula has to look at **every** position at once.

If they reach for `V_ii` and stop, do not correct it in words. Go to 4b and let the arithmetic
correct them.

### 4b. Nudge the weight, and watch the VARIANCE — this step is exact

Add `ε` to EMK's weight, leaving everything else alone. Write `u₅` for the list
`(0, 0, 0, 0, 1)`. Then:

```
  (w + ε u₅)ᵀ V (w + ε u₅)  =  wᵀVw  +  ε·u₅ᵀVw  +  ε·wᵀVu₅  +  ε²·u₅ᵀVu₅
```

The two middle terms are the same number, because `V` is symmetric — "how EMK moves with the
book" read from either end. So, with no approximation whatsoever:

> **Var(w + ε u_i)  =  Var(w)  +  2ε·(V w)_i  +  ε²·V_ii**

**That identity is exact for every `ε`, large or small.** The verifier confirms it on all five
names at eight different nudge sizes, from a hundredth to a quarter — **40 exact cases**, no
rounding anywhere.

And there is the answer to 4a: the thing multiplying the nudge is `(V w)_i` — **the whole row of
`V`, weighted by the whole book.** Level 10 §7c already built this object and named it in a
sentence: *"`(V w)_i` is how much stock `i` moves with the portfolio as a whole."*

For Book D:

```
  V w :
    AXL:  37.6(0.30) +  25(0.17) +  13(0.08) +   1(0.15) + (−11)(0.30)
       =  11.28      +   4.25    +   1.04    +   0.15    −   3.30      =  13.42
    BRN:    25(0.30) +  24(0.17) +  19(0.08) +  16(0.15) +   13(0.30)  =  19.40
    CHR:    13(0.30) +  19(0.17) +  29(0.08) +  31(0.15) +   37(0.30)  =  25.20
    DLT:     1(0.30) +  16(0.17) +  31(0.08) +  48(0.15) +   61(0.30)  =  31.00
    EMK: (−11)(0.30) +  13(0.17) +  37(0.08) +  61(0.15) + 85.6(0.30)  =  36.70
```

All five are exact. And the cross-check Level 10 installed still works: `w·(Vw)` must return the
variance.

```
  0.30(13.42) + 0.17(19.40) + 0.08(25.20) + 0.15(31.00) + 0.30(36.70)
  =  4.026    +  3.298      +  2.016      +  4.650      +  11.010     =  25   ✓
```

**Spend a minute on AXL's row before moving on.** Its five terms are `11.28, 4.25, 1.04, 0.15,
−3.30`. The last one is **negative**, and it is negative because `V[AXL,EMK] = −11` — the cell
Level 10 §6d spent a full minute on. AXL and EMK are the two ends of the style column; the
market pushes them together and the cheapness factor pushes them apart harder. **AXL's biggest
single relationship in this book is a negative one, with the largest position in it.** That is
the whole reason the rest of this level comes out the way it does, and a player who reads it
here will not be surprised by Section 6.

### 4c. From variance to risk — the only subtle step on the page

The nudge moved the *variance*. Nobody reports a variance. We need what it did to the **risk**,
which is the square root, and the player has no calculus.

**So guess, square the guess, and look at the error.** That is Level 1's move exactly.

The variance is `Var = σ²`. It moves by a small amount `δ`. Guess that the risk moves by
`δ/(2σ)` — i.e. guess that the new risk is `σ + δ/(2σ)`. Square the guess:

```
  ( σ + δ/(2σ) )²  =  σ²  +  2·σ·δ/(2σ)  +  δ²/(4σ²)
                   =  σ²  +  δ           +  δ²/(4σ²)
                   =  (the new variance)  +  δ²/(4σ²)
```

**The guess squares to exactly the right answer plus one leftover term, and the leftover is
built out of `δ²`.** Halve the nudge and `δ` halves, so the leftover falls to a *quarter*. It
dies faster than the thing we are measuring. That is the whole argument, and it is the same
argument the player used at Level 1 to find `b`.

Put numbers on it. Nudge EMK by `ε = +0.01` — one point of NAV, funded from cash:

```
  exact new variance  =  25 + 2(0.01)(36.70) + (0.01)²(85.6)
                      =  25 + 0.7340         + 0.00856
                      =  25.74256            exactly      (160891/6250)
```

Two things then get thrown away, and it is worth naming both.

```
  throw away the root's leftover only:   5 + 0.74256/10  =  5.0743     rounded
  throw away the ε² piece as well:       5 + 0.73400/10  =  5.0734     exactly
  the exact answer:                      √25.74256       =  5.0737     rounded
```

**The two discards push in opposite directions.** Dropping `δ²/(4σ²)` makes the guess too
**high** — by `0.0005`, **rounded**. Dropping `ε²V_ii = 0.00856` of variance makes it too
**low** — by `0.0003`, **rounded**. Keep both discards, as every risk report does, and the net
error is **three ten-thousandths of a percentage point on a nudge of a full point of NAV.** Say
that number; the player will need it again in Section 7d when they push the same tool ten times
as far.

**Name the two pieces, and never let them merge:**

- `2ε(Vw)_i` — **first order**. Proportional to the nudge. This is the piece we keep.
- `ε²V_ii` — **second order**. Proportional to the nudge squared. This is the piece we throw
  away, and it is the *only* place a position's own standalone variance `V_ii` appears at all.

That last sentence is worth a full stop of its own. **A position's own volatility contributes to
its marginal effect only at second order.** Everything at first order is `(V w)_i` — the
position's relationship with the *rest of the book*. That single fact is why Section 3c's
standalone-volatility table is about to be wrong.

### 4d. The same nudge, on a name at the other end

```
  AXL at 31% instead of 30%:
    exact new variance =  25 + 2(0.01)(13.42) + (0.01)²(37.6)
                       =  25 + 0.2684         + 0.00376
                       =  25.27216            exactly     (157951/6250)
    guessed new risk   =  5 + 0.2684/10  =  5.0268
    exact new risk     =  √25.27216      =  5.0271     rounded
```

**Same trade, same size, same book. EMK's point of NAV added `0.0737`; AXL's added `0.0271`.**
Not quite three times as much, from two positions that are the same size in a book that holds
both at 30%.

### 4e. The formula, and the name it does not have in the paper

Divide the first-order piece by the nudge to get the effect *per unit of weight*:

```
                              (V w)_i
  marginal contribution   =   ───────
        of position i             σ
```

where `σ = √(wᵀVw)` is the book's risk. In matrix form, all five at once: **MCR = (V w)/σ.**

**Now hand the name over** (`gm/VOCAB.md` row 14):

> **Marginal contribution to risk.** How much the *total* risk of *this* book moves when you add
> a little to *this* position. Not how risky the position is on its own — that is a different
> number, printed in §3c, and it is about to disagree.

For Book D, dividing `V w` by `σ = 5`:

| | AXL | BRN | CHR | DLT | EMK |
|---|---:|---:|---:|---:|---:|
| `(V w)_i` | 13.42 | 19.40 | 25.20 | 31.00 | 36.70 |
| **MCR**, %/unit | **2.684** | **3.880** | **5.040** | **6.200** | **7.340** |

All five exact. EMK's is **2.7347** times AXL's (**rounded**; exactly `1835/671`), and the two
positions are the same size.

**And here is the sentence that makes the ranking make sense.** Read the MCR row against the
cheapness column of `X`: `−2, −1, 0, +1, +2`. The MCRs run monotonically the same way. Why?
Because with `h = (1, −0.02)`, the book is essentially the market, and

```
  (V w)_i  =  (25 + 6h₂)   +   x_i(6 + 9h₂)   +   d_i w_i
           =   24.88       +   5.82 x_i       +   d_i w_i
```

with the last term worth `0.18, 0.34, 0.32, 0.30, 0.18` across the five names — small, and not
zero. Check it on CHR: `24.88 + 5.82(0) + 0.32 = 25.20` ✓.

The coefficient on `x_i` is **`6 + 9h₂`**, and with `h₂` near zero that is essentially the
**`+6`** — the off-diagonal of `F`. **The growth names co-move more with a market-shaped book
because the cheapness factor is positively correlated with the market factor.**

**Now delete the `+6` and watch.** Rebuild `V` with `F`'s off-diagonal set to zero and the five
co-movements become

```
  25.54,   25.52,   25.32,   25.12,   24.82
```

— **nearly flat, and in the opposite order.** The whole ranking of this level is carried by one
off-diagonal number in a 2×2 grid the player estimated at Level 8 from five months of data. A
player who can say that sentence has understood Level 8, Level 10 and Level 11 in one breath —
and has also just been handed Level 12's best question about this level: *how confident is
anybody in that 6?*

---

## 5. Contributions, and why they add up exactly

### 5a. The definition, and why the weight has to be in it

MCR answers *"what does one more point do?"* It does **not** answer *"what is this position
worth to the total?"* — a position with a big MCR held in size 0 is worth nothing.

> **contribution of position `i`  =  `w_i × MCR_i`**

For Book D:

```
  AXL:  0.30 × 2.684  =  0.8052
  BRN:  0.17 × 3.880  =  0.6596
  CHR:  0.08 × 5.040  =  0.4032
  DLT:  0.15 × 6.200  =  0.9300
  EMK:  0.30 × 7.340  =  2.2020
                          ──────
                          5.0000
```

**They sum to exactly the book's risk.** Not approximately. Not to within rounding. Exactly
5.0000, with every entry an exact decimal.

**Do not explain this yet. Make the player notice it.** Level 10 hammered *variances add, risks
do not*, and now five numbers that are unmistakably in risk units have added up to a risk. The
right reaction is suspicion. Pay bps for the suspicion.

### 5b. Why it works, argument one: scale the whole book

Multiply every weight by `(1 + ε)` — buy 1% more of everything, in proportion, changing no bet.

The variance is built from *products of two weights*, so it scales by `(1 + ε)²`, and the risk —
its square root — scales by exactly `(1 + ε)`. **Exactly.** The verifier checks it at five
different scalings including a 50% one; at `ε = 0.1` the risk goes from `5` to `5.5`, and it is
an exact rational both times.

So the change in risk from scaling everything is exactly `ε·σ`.

Now do the *same* trade as five separate nudges. Position `i` goes up by `εw_i`, so by Section
4c it contributes `εw_i × MCR_i` to the change in risk, plus something of size `ε²`. Add the
five up:

```
  ε·σ   =   ε·Σ w_i·MCR_i   +   (terms in ε²)
```

Divide by `ε` and shrink the nudge. The `ε²` terms die and:

> **Σ w_i · MCR_i  =  σ.**   The contributions sum to the total risk.

**This is the Euler decomposition, and the general theorem behind it is graduate-level.** Say so
(`gm/PLAYBOOK.md` files it as exactly this concession). The player has just derived the only
case of it they will ever need, with no calculus, out of one observation: **risk is homogeneous
of degree one in the weights — double the book, double the risk.**

### 5c. Why it works, argument two: one line

If the scaling argument feels like a conjuring trick, here is the whole thing without any
nudging at all:

```
  Σ w_i · MCR_i   =   Σ w_i·(V w)_i / σ   =   (wᵀ V w)/σ   =   σ²/σ   =   σ
```

**The weight and the marginal contribution multiply back into the quadratic form we started
with.** That is the entire proof. Show argument 5b first — it explains *why* it is true — and
5c second, so the player has a line they can write in five seconds under interrogation.

### 5d. Shares

Dividing each contribution by `σ` turns the five numbers into shares of the total:

| | AXL | BRN | CHR | DLT | EMK |
|---|---:|---:|---:|---:|---:|
| contribution | 0.8052 | 0.6596 | 0.4032 | 0.9300 | 2.2020 |
| **% of risk** | **16.104%** | **13.192%** | **8.064%** | **18.600%** | **44.040%** |

Exact, and they sum to exactly 100%.

**And now say the thing that makes the p.35 pie legal.** A share of risk is *also* a share of
variance: `w_i(Vw)_i / σ² = w_i·MCR_i / σ`, the same number twice. So this decomposition splits
the variance **and** the risk with the same five percentages — which is why a risk report can
print a pie that adds to 100 without violating anything Level 10 established. **Six square roots
would not sum to anything. Six contributions do.** The verifier confirms the two routes give
identical exact rationals name by name, and sweeps **2,226** different books on a 5% grid where
Euler and the shares-sum-to-one identity hold exactly every time.

---

## 6. The report — Book D, position by position

### 6a. Predict-then-reveal (round type A) — run this before revealing anything

Show the weights and the standalone volatilities from §3c, and nothing else. Then ask two
questions and demand a **reason before the number**:

1. *"AXL and EMK are both exactly 30% of this fund. Which one contributes more risk, and by
   what factor?"*
2. *"DLT is 15% — half the size of AXL. Which of those two contributes more?"*

- **Full bps** for *EMK, by roughly three times*, **with** the reason: EMK sits at the growth end
  of the style column, the market and cheapness factors are positively correlated at `+6`, so
  EMK moves more with a market-shaped book — and AXL's `−11` cell with EMK actively pulls its
  co-movement down.
- **No bps** for "EMK, because it's the most volatile name" **on its own**. It is true that EMK
  has the highest standalone volatility, and it is not the reason — question 2 is there to catch
  exactly this player, because DLT's standalone `6.9282` is *higher* than AXL's `6.1319` by only
  13% and yet DLT contributes more on **half** the money.
- **Dock** for *the same, they're the same size*. That is the belief this level exists to break.

### 6b. The table

| Position | Weight | Standalone vol | MCR | Contribution | % of risk |
|---|---:|---:|---:|---:|---:|
| AXL | **30%** | 6.1319 **rounded** | 2.684 | 0.8052 | **16.104%** |
| BRN | 17% | 4.8990 **rounded** | 3.880 | 0.6596 | 13.192% |
| CHR | 8% | 5.3852 **rounded** | 5.040 | 0.4032 | 8.064% |
| DLT | 15% | 6.9282 **rounded** | 6.200 | 0.9300 | 18.600% |
| EMK | **30%** | 9.2520 **rounded** | 7.340 | 2.2020 | **44.040%** |
| **total** | **100%** | — | — | **5.0000** | **100%** |

**Read the two 30% rows against each other and say nothing for ten seconds.** Same size. Same
book. `16.104%` against `44.040%`.

### 6c. Four rankings of one book, and three of them disagree

| Ranked by | 1st | 2nd | 3rd | 4th | 5th |
|---|---|---|---|---|---|
| **position size** | AXL (30%) | EMK (30%) | BRN (17%) | DLT (15%) | CHR (8%) |
| **standalone volatility** | EMK | DLT | **AXL** | CHR | BRN |
| **MCR** | EMK | DLT | CHR | BRN | **AXL** |
| **contribution** | EMK | DLT | AXL | BRN | CHR |

*(AXL and EMK are tied on size; the first row lists them in file order, not in any order of
magnitude.)*

Three facts to make the player state in their own words:

1. **AXL is the joint-largest position in the book and the third-largest contributor.** Its 30%
   of the money buys 16.104% of the risk.
2. **AXL is the third-most-volatile name in the universe standing alone (6.1319) and has the
   lowest marginal contribution of the five (2.684).** Standalone volatility is not the ranking.
   Section 4c said why: a name's own variance enters the nudge only at **second order**.
3. **DLT is exactly half of AXL's size and contributes more** — `0.9300` against `0.8052`, a gap
   of `0.1248`. Half the money, `15.5%` more of the risk (**rounded**).

And the two the PM will quote back at you:

- **EMK and DLT are 45% of the money and 62.640% of the risk.**
- **EMK and AXL are 60% of the money and 60.144% of the risk** — the two 30% positions look
  perfectly ordinary in aggregate. **The concentration is invisible until you split them.** Say
  this; it is the honest reason a report has rows and not just a total.

### 6d. And the split of the whole thing

```
  factor variance   =  24.7636  /  25  =  99.0544%     of the risk
  specific variance =   0.2364  /  25  =   0.9456%     of the risk
```

Both exact, and they sum to 100%. **Ninety-nine per cent of this book's risk is common-factor
risk.** Hold that number. Section 8 is going to move it to 4.5%, and nothing about the book will
change.

---

## 7. What the desk actually does with it

A number nobody trades on is a number nobody funds. This section is what MCR is *for*.

### 7a. The same trade on two names

Sell one point of NAV and hold the proceeds in cash — so the book is 99% invested afterwards.

```
  cut 1% of EMK :  exact new variance = 24.27456  (75858/3125)   risk = 4.9269   rounded
  cut 1% of AXL :  exact new variance = 24.73536  (77298/3125)   risk = 4.9735   rounded
```

```
  risk removed by the EMK cut :  0.0731     rounded
  risk removed by the AXL cut :  0.0265     rounded
```

**The identical trade on two identically-sized positions removes 2.7 times as much risk from
one as from the other**, and MCR said so before either trade was priced: `7.340` against
`2.684`, a ratio of `1835/671 = 2.7347` **rounded**. The first-order predictions were `4.9266`
(exact) and `4.97316` (exact) against true answers of `4.9269` and `4.9735` — both **rounded**,
both out by three ten-thousandths.

### 7b. The funded swap, which is what actually gets traded

Nobody holds cash. Sell 1% of EMK and put it into AXL, staying fully invested:

```
  predicted change  =  0.01 × (MCR_AXL − MCR_EMK)  =  0.01 × (2.684 − 7.340)  =  −0.04656
  predicted risk    =  4.95344    exactly                 (30959/6250)
  exact new variance=  24.54892   exactly                 (613723/25000)
  true new risk     =  4.9547     rounded
```

And the same trade run backwards, which is the one a momentum-chasing PM wants to do:

```
  sell 1% AXL, buy 1% EMK :  exact variance 25.48012  →  risk 5.0478   rounded
```

**One point of NAV moved between two 30% positions, and the risk of the book moves by about
five hundredths of a point in either direction.** The spread between the two outcomes is
`0.0931`, **rounded**. That is the desk's whole lever. It is also the honest
answer to "risk management means selling things": the two trades above **change no position by
more than one point** and one of them is a genuine risk reduction.

### 7c. How far can the swap run? Until the MCRs are equal

Keep swapping. As AXL grows, its own MCR rises (there is more AXL to co-move with) and EMK's
falls. The swap is worth doing while `MCR_AXL < MCR_EMK`, and it stops paying at the moment they
are equal.

Solve it: with `t` points swapped from EMK into AXL,

```
  (V w)_AXL  =  13.42 + 48.6 t          (V w)_EMK  =  36.70 − 96.6 t
```

and they meet at `t = 23.28/145.2 = 97/605 = 16.0331%` **rounded** — a swap of about sixteen
points of NAV, taking AXL to `46.0331%` and EMK to `13.9669%` (both **rounded**). There:

```
  (V w)_AXL  =  (V w)_EMK  =  21.2121   rounded      (exact: 128333/6050)
  variance   =  21.2675    rounded      (exact: 321671/15125)
  risk       =  4.6117%    rounded,  against 5.00% at the start
```

The verifier checks that this is a genuine minimum by pricing **60** nearby swap sizes on both
sides; every one is riskier.

> **The general rule, and it is the punchline of the level:** for a fully-invested book, risk is
> at its minimum when **every position has the same marginal contribution**. If two differ, there
> is a funded trade — sell the high one, buy the low one — that reduces risk, and it exists no
> matter how the two positions are sized.

**And immediately say what that rule is not.** It is not advice. Minimising risk is trivially
achieved by owning nothing interesting; a manager is paid for the return the risk buys. MCR
tells you the **price** of a bet in risk terms. What the bet is worth is not in this model, is
not in this paper, and is not in this game.

### 7d. First order is not exact, and here is the bill

Push the same swap to **ten** points instead of one:

```
  first-order prediction :  5 + 0.10 × (2.684 − 7.340)  =  4.5344
  exact answer           :  √21.796  =  4.6686    rounded
```

**Out by 0.1342 — more than a hundred times the error on the one-point version.** The error grows
like the square of the trade, exactly as Section 4c said it would.

| Trade | first-order prediction | exact | error |
|---|---:|---:|---:|
| +1% EMK | 5.0734 | 5.0737 | 0.0003 |
| +1% AXL | 5.0268 | 5.0271 | 0.0003 |
| cut 1% EMK | 4.9266 | 4.9269 | 0.0003 |
| cut 1% AXL | 4.9732 | 4.9735 | 0.0003 |
| swap 1% EMK→AXL | 4.9534 | 4.9547 | 0.0012 |
| **swap 10% EMK→AXL** | **4.5344** | **4.6686** | **0.1342** |

The right-hand two columns are **rounded**. The prediction column holds exact rationals shown to
four places: `5.0734`, `4.9266` and `4.5344` are exact as printed; `5.0268`, `4.9732` and
`4.9534` are **rounded** from `5.02684`, `4.97316` and `4.95344`. **MCR is a statement about the book you have, priced for a trade
you have not done yet.** Do a big trade and you must recompute, because the book that the number
described no longer exists. That is the canoe story's awkward question, arriving as arithmetic.

---

## 8. Against a benchmark — the same machinery, a completely different answer

**Do not skip this.** It is where the numbers on this page connect to the numbers on p.35, and
it is where the negative contribution lives.

Level 10 §12 established the move: **subtract the benchmark's weights from the portfolio's and
run exactly the same three lines on the difference.** The benchmark here holds all five names
equally.

| | AXL | BRN | CHR | DLT | EMK |
|---|---:|---:|---:|---:|---:|
| Book D | 30% | 17% | 8% | 15% | 30% |
| Benchmark | 20% | 20% | 20% | 20% | 20% |
| **active `a = w − b`** | **+10%** | **−3%** | **−12%** | **−5%** | **+10%** |

The benchmark's own exposures are `h = (1, 0)`: fully invested, no style tilt at all. Its
variance is `25 + 0.368 = 25.368`, a risk of **5.0367%** **rounded**.

> **Book D is *less* volatile than the index it is measured against — 5.00 against 5.0367 — and
> it still carries active risk.** Level 10 §12.2 made this point and it is worth making twice: a
> manager who says *"I'm below the index's volatility, so I'm not taking risk"* has said
> something false, and the arithmetic that shows it is below.

```
  active exposures  h  =  Xᵀ a :
     market    :  0.10 − 0.03 − 0.12 − 0.05 + 0.10                 =  0      ← cancels exactly
     cheapness :  0.10(−2) − 0.03(−1) − 0.12(0) − 0.05(1) + 0.10(2)
                = −0.20    + 0.03     + 0       − 0.05    + 0.20    = −0.02
```

```
  active factor variance   =  9 × (−0.02)²  =  0.0036   (the 25 and the 6 are multiplied by 0)
  active specific variance =  (0.10)²(0.6) + (0.03)²(2) + (0.12)²(4) + (0.05)²(2) + (0.10)²(0.6)
                           =   0.006       +  0.0018    +  0.0576    +  0.005     +  0.006
                           =   0.0764
  ACTIVE variance          =  0.0036 + 0.0764  =  0.08    exactly    (2/25)
  ACTIVE RISK              =  √0.08  =  0.2828%  per month           rounded
```

### 8a. The pie turns inside out

| | factor share | specific share |
|---|---:|---:|
| Book D, **total** risk | **99.0544%** | **0.9456%** |
| Book D, **active** risk | **4.5000%** | **95.5000%** |

All four exact. **The specific share is 100.9941 times larger** (**rounded**) in the active pie,
and *nothing about the book changed*. Subtracting the benchmark deleted the market factor, which
was carrying essentially all of the common risk.

**This is the mechanism behind p.35's 50/50 pie, and now the player has felt it rather than been
told it.** Say the two guard-rails immediately:

- Our toy swings further than a real book because its net active style tilt is `−0.02`, i.e.
  nothing. A real book with real tilts lands in between — p.35's does, at 50/50.
- **PAPER, p.34:** "The report shows that the Active Risk is **split equally between common
  factors and stock specific sources**." That sentence is about **Active** Risk. It is not a
  claim about anybody's total volatility.

### 8b. The active report, and two entries that will start an argument

```
  V a :
    AXL:  37.6(0.10) +  25(−0.03) +  13(−0.12) +   1(−0.05) + (−11)(0.10)  =   0.30
    BRN:    25(0.10) +  24(−0.03) +  19(−0.12) +  16(−0.05) +   13(0.10)   =   0.00
    CHR:    13(0.10) +  19(−0.03) +  29(−0.12) +  31(−0.05) +   37(0.10)   =  −0.60
    DLT:     1(0.10) +  16(−0.03) +  31(−0.12) +  48(−0.05) +   61(0.10)   =  −0.40
    EMK: (−11)(0.10) +  13(−0.03) +  37(−0.12) +  61(−0.05) + 85.6(0.10)   =  −0.42
```

| Position | active weight | `(V a)_i` | MCR | contribution | % of active risk |
|---|---:|---:|---:|---:|---:|
| AXL | **+10%** | +0.30 | +1.0607 **rounded** | +0.1061 **rounded** | **+37.5%** |
| BRN | −3% | **0.00** | **0.0000** | **0.0000** | **0.0%** |
| CHR | −12% | −0.60 | −2.1213 **rounded** | +0.2546 **rounded** | **+90.0%** |
| DLT | −5% | −0.40 | −1.4142 **rounded** | +0.0707 **rounded** | **+25.0%** |
| EMK | **+10%** | −0.42 | −1.4849 **rounded** | −0.1485 **rounded** | **−52.5%** |
| **total** | **0%** | | | **0.2828** **rounded** | **100.0%** |

The five percentage shares are **exact**: `37.5, 0, 90, 25, −52.5`, summing to exactly 100.

Three things here, and every one of them is worth bps:

1. **BRN's marginal contribution is exactly zero.** A real, funded, three-point underweight, and
   nudging it changes the active risk of the book by nothing at all (to first order). *Why:*
   `(V a)_BRN` is a sum of five terms that cancel to zero. A position can be genuinely present
   and genuinely irrelevant.
2. **EMK's marginal contribution is negative.** Buying *more* of a position that is already the
   joint-largest overweight **reduces** the book's active risk. *Why:* the book's net active
   style tilt is `−0.02`, i.e. very slightly towards value, and EMK is the growth end. Adding EMK
   pushes `h₂` towards zero, and the factor term `−0.02 × 24 = −0.48` beats EMK's own specific
   term `+0.6 × 0.10 = +0.06`. **That is a hedge, and the model found it.**
3. **CHR's marginal contribution is negative and its contribution is positive.** Its active
   weight is `−12%`. Two negatives. **You cannot read the sign of a marginal contribution off a
   contribution bar without also reading the exposure**, and this is precisely why p.35 plots
   both series on two axes. `gm/VOCAB.md` §14 records a previous reading of the p.35 FX panel
   that got this exact inference backwards; the mechanism above is what stops it happening
   again.

**The warning that goes with the −52.5%.** A negative share is real and it is not a bug, but it
means *this decomposition is not a pie you can shade in*. Book D's active decomposition has a
slice below zero and another above 90%; drawn as a pie it is nonsense, and printed as a table it
is exactly right. p.35 prints a pie because that book's block contributions all happen to be
positive. **Do not teach "contributions are always a pie."**

---

## 9. Traps, and exactly what each wrong belief returns numerically

Every row is computed by the verifier. Give the number, not the adjective.

| Wrong belief | What it computes | Result | Versus the truth |
|---|---|---:|---|
| 1. "Cut the biggest position first" | cut 1% of AXL, one of the two 30% names | risk **4.9735** | removes **0.0265**; the same cut in EMK removes **0.0731** — **2.7×** more |
| 2. "Contribution = weight × the name's own volatility" | `w_i × √V_ii` | totals **6.9180** | overstates the risk by **38.3609%**, and ranks AXL 2nd where the truth ranks it 3rd |
| 3. "Rank by MCR and you're done" | `Σ MCR_i` | **25.1440** | not a risk of anything; the weights are the point |
| 4. "Just use each name's own variance" | `Σ w_i² V_ii` | risk **3.6121** | **−27.76%** |
| 5. "Specific risk diversifies away, drop `D`" | `hᵀFh` only | risk **4.9763** | −0.47% |
| 6. "Factors are separate, drop `F`'s off-diagonals" | `25h₁² + 9h₂² + Σw²d` | risk **5.0239** | +0.48% |
| 7. "A contribution cannot be negative" | Book D's active report | **−52.5%** for EMK | and the five shares still sum to exactly 100% |
| 8. "MCR tells me what a trade will do" | 10-point swap, predicted | **4.5344** | the exact answer is **4.6686** — out by **0.1342** |

All risks **rounded**; all variances exact.

**Read rows 5 and 6 together before dismissing either.** On *this* book, deleting `D` and
deleting `F`'s off-diagonals are both worth about half a per cent, and in opposite directions.
At Level 10 the same two traps were worth `−1.83%` and `+19.88%` on a different book. **The size
of a modelling error is a property of the book, not of the error.** A player who has memorised
"ignoring correlations understates risk" has a slogan; rows 5 and 6 are here to take it away.

**Row 1 is the one PMs actually believe**, and row 2 is the one that sounds sophisticated. Row 2
deserves a second look: it gets the top name right (EMK), it gets the bottom name right (CHR),
and it still ranks AXL above DLT when the truth is the other way round — *and* it produces a
"total" that is 38% too big. **A method that ranks nearly correctly and totals absurdly is more
dangerous than one that is obviously wrong**, because it survives the eyeball test.

---

## 10. Sabotage round (round type B) — run this before the boss

Hand the player this risk report and say only: *"one number in this table is wrong. Find it, say
by how much, and repair it — without recomputing `V w`."*

| Position | Weight | Contribution |
|---|---:|---:|
| AXL | 30% | 0.8052 |
| BRN | 17% | 0.6596 |
| CHR | 8% | 0.4032 |
| DLT | 15% | **0.9030** |
| EMK | 30% | 2.2020 |
| **Book D total risk** | | **5.0000** |

**The check they should reach for is Section 5's**, and it is a single addition:

```
  0.8052 + 0.6596 + 0.4032 + 0.9030 + 2.2020  =  4.9730     against a stated 5.0000
```

**Euler says these must sum to the total risk exactly. They are short by 0.0270.** And because
exactly one entry is corrupted, the repair falls out for free: the four survivors sum to
`4.0700`, so the true entry is `5.0000 − 4.0700 = 0.9300`. DLT's digits were transposed.

**Two independent confirmations, and make the player produce at least one:**

- **Divide by the weight.** A contribution divided by its weight must be that position's MCR:
  `0.9030/0.15 = 6.0200`, against a true `31/5 = 6.2000`. The corrupted report claims DLT
  co-moves with the book at `6.02 × 5 = 30.10` when `V w` says `31.00`.
- **The shares.** `4.9730/5.0000 = 99.4600%`. A risk report whose contributions do not come to
  100% has a defect, full stop.

The verifier corrupts every one of the five entries at six different magnitudes — **30 cases** —
and the Euler check catches all thirty.

**CALL BACK, and say the words.** This is the third sabotage round in the game and the third
different kind of check:

| Level | The check | What guarantees it |
|---|---|---|
| **L2** | `Σ x·u = 0` | the **arithmetic** of the fit — you could not stop it if you tried |
| **L10** | `X F Xᵀ z = 0` for an exposure-free `z` | the **structure** — three assets built out of two factors |
| **L11** | `Σ w_i·MCR_i = σ` | an **identity about the object itself** — risk doubles when the book doubles |

**Finding one of these unprompted is what separates a quant from a spreadsheet.** Say that, and
mean it: from here to the Rebuild, every level has one.

---

## 11. BOSS ROUND — the manager who is diversified

### 11.1 The setup, as the player receives it

**Meera is back.** At Level 8 she was the audience for a teach-back — a portfolio manager of
nineteen years' standing who has never opened a statistics textbook and does not intend to.
Today she is not asking questions. She is defending her book, she has a committee behind her,
and she is not wrong about anything she says.

> *"Here is the fund. Five names, all five of them, and I want you to notice three things before
> you open your laptop.*
>
> | | AXL | BRN | CHR | DLT | EMK |
> |---|---:|---:|---:|---:|---:|
> | **Book P** | 18% | 19% | **28%** | 9% | 26% |
>
> *One: **nothing is over twenty-eight per cent.** Two: I own the cheapest name in your universe
> and the dearest one, and everything in between — my net style tilt is plus nought-point-nought-
> six of a standard deviation, which is **nothing**. Three: my biggest position is CHR, which has
> **no style tilt at all** — it is the most boring stock on your list.*
>
> *So tell me where the concentration is. And do not tell me about beta; I know I own equities."*

**Give the player `V`, `F`, `D` and nothing else. Twenty minutes.**

### 11.2 The arithmetic, in full

```
  h  =  Xᵀ w :
    market    :  0.18 + 0.19 + 0.28 + 0.09 + 0.26                             =  1
    cheapness :  0.18(−2) + 0.19(−1) + 0.28(0) + 0.09(1) + 0.26(2)
               = −0.36    − 0.19     + 0       + 0.09    + 0.52               = +0.06
```

```
  factor variance   =  25(1)² + 2(6)(1)(0.06) + 9(0.06)²
                    =  25     + 0.72          + 0.0324     =  25.7524   (64381/2500)
  specific variance =  (0.18)²(0.6) + (0.19)²(2) + (0.28)²(4) + (0.09)²(2) + (0.26)²(0.6)
                    =   0.01944     +  0.0722    +  0.3136    +  0.0162    +  0.04056
                    =   0.4620                                            (231/500)
  TOTAL variance    =  25.7524 + 0.4620  =  26.2144                       (16384/625)
  TOTAL risk        =  √26.2144  =  5.12%  per month        EXACT root
```

```
  V w :
    AXL:  37.6(0.18) +  25(0.19) +  13(0.28) +   1(0.09) + (−11)(0.26)  =  12.388
    BRN:    25(0.18) +  24(0.19) +  19(0.28) +  16(0.09) +   13(0.26)   =  19.200
    CHR:    13(0.18) +  19(0.19) +  29(0.28) +  31(0.09) +   37(0.26)   =  26.480
    DLT:     1(0.18) +  16(0.19) +  31(0.28) +  48(0.09) +   61(0.26)   =  32.080
    EMK: (−11)(0.18) +  13(0.19) +  37(0.28) +  61(0.09) + 85.6(0.26)   =  38.596
```

| Position | Weight | MCR = `(Vw)/5.12` | Contribution | % of risk |
|---|---:|---:|---:|---:|
| AXL | 18% | 2.4195 **rounded** | 0.4355 **rounded** | 8.51% |
| BRN | 19% | 3.7500 | 0.7125 | 13.92% |
| CHR | **28%** | 5.1719 **rounded** | 1.4481 **rounded** | 28.28% |
| DLT | **9%** | 6.2656 **rounded** | 0.5639 **rounded** | 11.01% |
| EMK | 26% | 7.5383 **rounded** | 1.9600 **rounded** | **38.28%** |
| **total** | 100% | | **5.1200** | **100.00%** |

(All five MCRs and contributions are exact rationals with terminating decimals; they are marked
**rounded** where the printed digits stop short of the full expansion. The shares are printed to
two decimals and sum to exactly 100.00.)

### 11.3 The answer, in four numbers

**1. Her largest position is not her largest contributor.** CHR is 28% of the fund and 28.28% of
the risk. EMK is **26%** of the fund and **38.28%** of the risk. The ranking by size and the
ranking by contribution are not the same list.

**2. Her smallest position beats one twice its size.** DLT is **9%** of the fund and carries
**11.01%**. AXL is **18%** — exactly twice as much money — and carries **8.51%**. **Half the
position, 2.51 percentage points more risk** (**rounded**: the exact gap is `2.5076`, and
subtracting the two-decimal shares in the table gives `2.50` — that is rounding drift, not a
second answer).

**3. And now the number that answers the actual question.** Split her risk:

```
  factor    :  25.7524 / 26.2144  =  98.2376%     of the risk
  specific  :   0.4620 / 26.2144  =   1.7624%     of the risk
```

**Ninety-eight per cent of her risk is common-factor risk, and no amount of holding more names
touches it.** Prove it rather than asserting it — this is the killer and it must be arithmetic:

| An equally weighted book of… | variance | risk |
|---|---:|---:|
| 5 names like these | 25.368 | **5.0367** **rounded** |
| 10 | 25.184 | 5.0184 **rounded** |
| 50 | 25.0368 | 5.0037 **rounded** |
| 1,000 | 25.00184 | 5.0002 **rounded** |
| **the limit** | **25** | **5.0000** |

The specific term is `9.2/(5n)` and it goes to zero. **The market term, 25, never moves.** She
could hold ten thousand names from this universe and her risk would not go below 5% a month.
She is at 5.12%. **Diversification has 0.0453 of a percentage point left to give her**
(`5.1200 − 5.0747`, where `5.0747` **rounded** is what her book would be worth if every one of
her five names' private lives vanished entirely).

**4. Kill the "my tilt is nothing" defence, because it is her best line.** Set the style tilt to
**exactly zero** — any book at all with `h = (1, 0)` — and write down the **factor-driven**
co-movement of each name with it:

```
  25 + 6h₂ + x_i(6 + 9h₂)  =  25 + 6x_i  =  13,  19,  25,  31,  37
                                              for  x = −2, −1, 0, +1, +2
```

*(That is the common-factor half. Each name's own `d_i w_i` then adds a little on the diagonal —
`0.108, 0.38, 1.12, 0.18, 0.156` on her weights — which does not change the ordering.)*

**A spread of 37/13 = 2.8462 (rounded) between her cheapest and dearest name, with no style bet
at all.** Her *aggregate* exposure cancels. Her assets' *co-movements* do not, because they run
through `F`'s off-diagonal — the `+6`. **What cancels in the exposure vector does not cancel in
the risk**, and that single sentence is the boss round.

### 11.4 The honest counter — have it ready before she says it

**Meera is not wrong that this is a fund, not a hedge fund.** Say so out loud, unprompted:

- **Owning the market is not a failure of diversification.** It is what an equity fund is for.
  A book whose risk is 98% common factor is *normal*, and the paper's own example report is a
  benchmarked European equity book (p.34) rather than a market-neutral one.
- **The charge that survives** is narrower and much harder to answer: *within* the part she
  controls — the deviation from her index — her risk is concentrated in a small number of names,
  and the concentration does not follow her position sizes. Run it: against the equally weighted
  benchmark her active weights are `−2%, −1%, +8%, −11%, +6%`, her **active risk is 0.2912%** per
  month (**rounded**), and it splits **38.2075% factor / 61.7925% specific** (both **rounded**).
- **This is exactly why the paper's example report is an *active* report.** Every dot on p.35 is
  labelled "Act. Exp." and the pie is a split of **Active Risk 2.99%**, not of Portfolio Risk
  15.62% (p.35 banner, both read directly from the scan). A player who refutes "I am
  diversified" using only total risk has answered a question about the market, not about her.

### 11.5 The interrogation script (real objections, escalating)

Play Meera. Nineteen years of it, a committee behind her, and no patience at all.

| Objection | A passing answer contains | Hand-waving sounds like |
|---|---|---|
| **"My biggest position is CHR and you say my biggest risk is EMK. One of us is wrong."** | Neither: size and contribution are different quantities of different shapes. Size is a number about the position; contribution is a number about the position **and** the rest of the book, via `(V w)_i`. p.35 plots the two on **two different axes** for exactly this reason. | "Risk isn't intuitive." "The optimiser knows." |
| **"Then show me the arithmetic of a contribution. And show me where it is in the paper."** | Derives it: nudge `w_i` by `ε`, the variance moves by exactly `2ε(Vw)_i + ε²V_ii`, the risk moves by `ε(Vw)_i/σ` to first order, multiply by `w_i`. **Then says plainly: the paper contains no formula for this and never uses the phrase.** "Contribution" is a chart axis label on p.35 and one paragraph on p.34. | **Citing a formula to the paper. That is an automatic fail** — it is the fabrication `gm/LEVEL_ANCHORS.md` exists to prevent. |
| **"Your five numbers add to my total risk. Level 10 spent an hour telling me risks don't add."** | Both are true and they are about different objects. Level 10: `√a + √b ≠ √(a+b)` — **volatilities** do not add. Level 11: `Σ w_i(Vw)_i/σ = σ²/σ = σ` — **contributions** do, by construction, because each one already carries a `w_i`. Names the homogeneity argument (double the book, double the risk) and concedes that the general theorem is graduate-level. | "It's Euler's theorem." *(Offered as a name rather than a mechanism. Ask them to do it with the scaling argument instead.)* |
| **"My net style tilt is 0.06. You cannot pin a style story on 0.06."** | Sets it to exactly 0 and shows the co-movements are still `13, 19, 25, 31, 37` — a factor of **2.8462** (**rounded**) — because the ranking runs through `F`'s off-diagonal `+6`, not through her aggregate bet. **What cancels in `Xᵀw` does not cancel in `Vw`.** | "It's still a tilt." (Unquantified, and she will eat them.) |
| **"Fine. I'll add fifteen more names. Then what?"** | The table in 11.3: the specific term falls like `1/n` and the factor term does not move at all. 5 names → 5.0367; 1,000 names → 5.0002; the floor is 5.0000. **Names diversify names. They do not diversify a shared factor.** | "It'll help a bit." |
| **"So what do I sell?"** | Refuses the trap and answers with the model. On a funded basis, sell the highest MCR and buy the lowest: sell EMK (7.5383 **rounded**) and buy AXL (2.4195 **rounded**). Says the size of the effect, says it is **first order** and re-priced after any large trade, and says the thing that is not in the model: **the risk is a price, not a verdict — nothing here says what her EMK bet is worth.** | "Sell EMK." Full stop, with no size, no first-order caveat, and no acknowledgement that return exists. |
| **"Your report has a slice at minus fifty-two per cent."** *(if the player has shown Book D §8b, or once Book P's active table is on the table)* | A contribution is negative when the position offsets the rest of the book: adding to it reduces the total. Book P's own active table has a cleaner version — **CHR and DLT have identical co-movements, `(V a)_i = +0.68` each, so identical marginal contributions of `2.3351` — that is `0.68/0.2912`, rounded — and opposite-signed contributions**, `+0.1868` against `−0.2569` (both **rounded**), because one is an `+8%` overweight and the other an `−11%` underweight. Shares: `17.2642, 2.3585, 64.1509, −88.2075, 104.4340` (all **rounded**), which sum to exactly 1 as fractions and to `100.0001` as printed — **rounding drift, said out loud.** | "That's a rounding error." Or drawing it as a pie. |

### 11.6 Pass conditions

All six, and the third and fifth are the level:

1. **5.12% per month**, with `25.7524` and `0.4620` shown separately and `V w` visible.
2. The five contributions produced and shown to sum to `5.1200`.
3. **The disagreement stated in both directions**: CHR biggest and not the biggest contributor;
   DLT half of AXL and contributing more. One direction is half marks.
4. MCR derived by **nudging**, not asserted — and the player says the word "first order"
   unprompted at least once.
5. **The "I'll add more names" objection answered with the `1/n` table and the floor of 25.**
   A player who answers it with "diversification helps but not enough" has not passed.
6. The GAP stated without being asked: **the paper has no formula for any of this.**

**Fail modes and where to drop to:**

| They say | The broken rung | Drop to |
|---|---|---|
| "The biggest position is the biggest risk" | Size and contribution are one idea. This is the whole level | §6b, the two 30% rows of Book D, and do not move until they can say why |
| "EMK, because it's the most volatile" | Standalone volatility has been mistaken for MCR | §4c: `V_ii` enters only at **second order**. Then §6c's four rankings |
| Correct numbers, cannot say what `(V w)_i` means | Level 10 §7c did not land | Level 10 §7c, one sentence: *"how much stock `i` moves with the portfolio as a whole"* |
| "You'd have to run the optimiser" | Outsourcing the mechanism. Dock 20 | §4b. The nudge is four lines of algebra and needs no software |
| Cites a page for the MCR formula | **The repository's worst failure, live at the table.** Dock 50 | `gm/LEVEL_ANCHORS.md` §14's GAP paragraph, read out |

---

## 12. Names unlocked, ladder position, and what this level does not settle

### 12.1 Names unlocked at the end of this level

| Name | Where it was earned | The BFRE position |
|---|---|---|
| **marginal contribution to risk** | Section 4e — the object exists now | **GAP. The phrase appears nowhere in the paper.** `gm/VOCAB.md` row 14. The industry word for something BFRE computes and never writes down. |
| **risk contribution / contribution to risk** | Section 5 | **PAPER, as a label only.** p.35's axes read "**Contrib. (% of Act. Risk)**" and "**Contribution (%)**"; the legend series are "Contrib. to Act. Risk" and "Contrib. to Spec. Risk". p.34 has one paragraph of prose. **No formula anywhere.** |
| **risk decomposition** | Sections 5, 8 | **PAPER, as words.** The phrase appears on pp.2, 4 and 18 as a description of what the model is useful for, never with mathematics attached. |
| **active risk** / **tracking error** | Level 10 §12.4 unlocked both; **this** is the level where the report is read | **PAPER** for *Active Risk* (p.34 prose, p.35 banner). **"Tracking error" has zero occurrences in 65 pages.** Drill the switch in both directions — getting it wrong either way is a Victory-Condition-2 failure. |

**Do not unlock here:** *bias statistic* (Level 12). And do not let *Euler's theorem* be used as
an answer — it is a name for the thing the player proved, not a substitute for proving it.

**Vocabulary under fire (round type F) — run it before the ladder table.** Give the sentence,
demand plain English, then demand the term used correctly in a *new* sentence, unprompted.

> *"Its weight is small but the marginal contribution is the biggest in the book — it's
> correlated with everything else you own."*

- **Plain English that passes:** it is not a big position, but adding to it moves the whole
  book's risk more than adding to anything else, because it goes up and down with the rest of
  what is already held.
- **The tell that fails:** *"it's the riskiest stock"* — that is standalone volatility, a
  different number, and Book D's AXL is the counterexample (third-most-volatile standing alone,
  lowest MCR in the book).
- **Then the follow-up, and do not skip it:** *"name me a position whose marginal contribution
  is negative. What has to be true about it, and what happens if I double it?"* A pass says: it
  moves against the rest of the book, and doubling it reduces risk **at first** — the words "at
  first" are the marks, because as it grows it stops hedging and its own MCR crosses zero.
  Section 7c's equal-MCR point is exactly that crossing.

### 12.2 Ladder position after this level

| Concept | Tier reached | What is still missing for tier 5 |
|---|---|---|
| Marginal contribution, derived by nudge | **5 — Rebuild** | nothing; this is the level |
| Contributions summing to the total | **4 — Defend** | tier 5 is spotting a broken decomposition in someone else's report |
| Exposure ≠ contribution | **5 — Rebuild** | nothing, if both directions of §11.3 were produced |
| Reading a real risk report | **3 — Derive** | tier 4 needs Section 13 run on p.35 with the four warnings intact |
| Active risk against a benchmark | **4 — Defend** | tier 5 is doing it on a benchmark they were handed cold |
| Negative and zero contributions | **3 — Derive** | tier 4 needs the §8b sign argument survived under attack |

### 12.3 What this level does NOT settle

1. **Whether `V` is any good.** Every contribution here is as good as `F` (104 weeks, 26-week
   half-life, p.27, method deferred to a separate BRS document) and `D` (Table 1.3, p.28,
   blending function not given). Level 12.
2. **What a bet is worth.** MCR prices risk. Nothing in this level, and nothing in this paper,
   says what return that risk buys.
3. **How BFRE actually computes the bars on p.35.** It does not say. The output format is
   citable; the arithmetic is ours.
4. **Whether a contribution is stable.** Ours is computed once on a frozen `V`. The p.35 report
   is named the **Equity Daily Risk** report and p.34's flowchart 1.19 describes a **daily**
   production process for the model estimation — so these numbers are regenerated constantly —
   and the paper prints **no** stability diagnostic for any contribution anywhere.
5. **The optimisation problem.** §7c found the minimum along **one** swap line by hand. Doing it
   in every direction at once is portfolio optimisation, it is a different subject, and this
   game does not teach it.
6. **Annualisation.** Every `×√12` on this page is ours and assumes independent months, which
   p.30 says BFRE does not assume.

---

## 13. Back to BFRE — what this machinery does in the real model

### 13a. p.34 — the only prose about using the number

**PAPER, p.34**, on Figure 1.18:

> "Top-line risk numbers are shown along the top of the report: Active Risk, Portfolio Beta,
> Portfolio Risk and Benchmark Risk. **Active Risk is then decomposed along the different factor
> blocks in the model, shown in the pie chart: styles (including the market factor), industries,
> countries and currencies.** The report shows that the **Active Risk is split equally between
> common factors and stock specific sources.** Style and industry factors account for most of
> the common factor risks."

And on the panels:

> "For each factor block, there is a corresponding bar chart (using a consistent colour) that
> shows the top contributing factors in that block – **this displays the active exposure together
> with the contribution to active risk.**"

**That last sentence is the whole of what the paper says about the design of the chart the player
just rebuilt.** It says the two series are plotted together. It does not say why, and it never
says how either is computed. *(That two axes are needed **because the two quantities rank
differently** is* **INFER** *— ours. `gm/ANALOGIES.md` C16 marks it as an inference explicitly.
Say "this is why I think they did it", never "the paper says".)*

### 13b. p.35 — the report, and four ways to misread it

**PAPER, p.35**, Figure 1.18, caption: "a sample **Equity Daily Risk (EDR)** report in Aladdin".
European Equity portfolio, EMEA model, generated with PRT (p.34).

Banner, read directly from the scan:

| Active Risk | Portfolio Beta | Portfolio Risk | Benchmark Risk | Base Currency |
|---:|---:|---:|---:|---|
| **2.99%** | **1.02** | **15.62%** | **14.98%** | EUR |

*(Carry the audit's doubt: the middle digit of `2.99` is blobby — `2.89` not fully excluded — and
the last digit of `15.62` is soft — `15.67` not fully excluded. `14.98` and `1.02` are clean.)*

**The four misreadings, and a GM must hold all four:**

1. **It is an ACTIVE report, end to end.** The dot series on every panel is labelled
   "**Act. Exp.**" — active exposure, portfolio minus benchmark. A dot at −10% of NAV is a
   **ten-point underweight, not a short.** This is a European book against a European benchmark;
   it is almost certainly still long the UK. **Say "underweight". Never say "short".**
2. **The pie is a split of Active Risk (2.99%), not of Portfolio Risk (15.62%).** "Specific 50%"
   means half of **2.99**, i.e. about **1.4950** points of active risk. A reader who takes it as
   half of Portfolio Risk gets **7.8100** and is wrong by a factor of more than five.
3. **"Top Asset Contributions" is a top-N panel with exactly 15 bars.** The report **never states
   how many holdings the portfolio has**, and neither may the GM or the player. Never say "a
   fifteen-stock portfolio". What is sayable: *fifteen names are enough to fill the panel and
   specific risk is still half the total.*
4. **The style panel's Market dot sits at ≈0.0, and that does not contradict Portfolio Beta
   1.02.** It is a zero **active** market exposure — portfolio and benchmark equally invested.
   Reading it as "the book has no market exposure" teaches the exact confusion **p.4** exists to
   warn about: "The market factor **exposure** of a portfolio should not be confused with its
   market **beta**."

**And the numbers that are not printed.** Every bar height and dot position on p.35 is a
**pixel measurement, ±10%** (`notes/`, p.35). The axis tick labels and the banner figures are
read directly and are reliable. The pie's **Act Sec 1%** is `[INFERRED]` — the glyph reads 1 or
2, and 1 is recorded only because the six slices then sum to exactly 100. **Never launder any of
this into a confident figure.**

### 13c. The pie, and why it is allowed to be a pie

| Slice | Share |
|---|---:|
| **Specific** | **50%** |
| Style | 25% |
| Industry | 14% |
| Country | 6% |
| FX | 4% |
| Act Sec | 1% `[INFERRED]` |

`25 + 14 = 39` of the 50 common-factor points, which is p.34's "Style and industry factors
account for most of the common factor risks", checked. The six sum to exactly 100.

**Section 5 is why that sum is legal.** These are *contributions*, and contributions add. Six
volatilities would not. p.35 is Level 10's lesson and Level 11's identity printed in the same
picture — and the block-level version of the arithmetic the player just did name by name.

### 13d. Contribution against exposure, in the paper's own figure

The paper's own panels show the two rankings disagreeing, on the same page, in the same
picture. `[APPROX — every bar and dot magnitude below is a pixel measurement, ±10%. The
**orderings** survive that error bar; the magnitudes are not printed values and must not be
quoted as figures.]`

- **Industry panel, the clean case.** **Airlines** carries an active exposure of only about
  **+2.2% of NAV** — ninth of ten by magnitude in its block — and ranks **second by risk
  contribution**. **Food Household** carries about **−5.5% of NAV**, the second-largest position
  in the panel, and ranks below Media. *Two and a half times the position, less than half the
  risk.* **That is this level, in the paper's own figure.**
- **Style panel, the degenerate case.** **Emerging** carries about **−0.10 sd** of active
  exposure and contributes about **0%**. A real exposure that adds no risk — Book D's BRN, with
  its marginal contribution of exactly zero, is the same phenomenon.
- **Country panel, where they agree — say this too.** The **United Kingdom** has both the
  largest active exposure in its block (about **−10% of NAV**, an underweight) and the largest
  contribution (about 2.4%). **Exposure and contribution are different quantities, not opposite
  ones.** A big bet on a volatile block usually does both, and a player who has over-learned this
  level will call that a contradiction.
- **FX panel, the sign lesson.** The second pair sits at roughly **−10% of NAV** with a
  **positive** contribution of about **+0.55%**. **An underweight that adds risk.** Active risk is
  charged on the *size* of the deviation; the sign of the bet does not settle the sign of its
  contribution. Book D's §8b table is the same fact with exact arithmetic: CHR at `−12%` active
  with a **negative** MCR and a **positive** contribution.

### 13e. The one arithmetic check the banner supports

```
  Portfolio Risk − Benchmark Risk  =  15.62 − 14.98  =  0.64
  Active Risk (printed)                              =  2.99
```

**The reported Active Risk is 4.6719 times the difference of the two risks** (**rounded**), on a
real portfolio in a published document. Risks do not subtract any more than they add, and this is
the printed proof. *(Neither alternative digit reading rescues subtraction:
`15.67 − 14.98 = 0.69`, still nowhere near `2.89`.)* Book D makes the same point in miniature and
in the opposite direction: its total risk is **5.00%** against a benchmark's **5.0367%**
(**rounded**) — *lower* — and its active risk is still **0.2828%** (**rounded**).

### 13f. Where this level's machinery ends up in the finished model

1. Levels 1–7 fill `X` and produce a factor-return series.
2. Level 8 turns that series into `F`; Level 9 turns the misses into `Δ`.
3. Level 10 is equation (1.8), `Σ = X F Xᵀ + Δ`, p.24.
4. **Level 11 is what a human being actually looks at.** Nobody reads `Σ`. They read one row of
   it per position, divided by the book's risk — which is Figure 1.18 on p.35, and the
   conversation p.34 says the report is for: *"more informed discussions between portfolio
   managers and risk managers around the level and types of risks being taken in portfolios."*
5. Level 12 asks how anyone knows `Σ` is right, and finds pp.32–33 printing no values at all.

**Scale check, and say clearly that it is a check and not a target.** Book D annualised is
**17.3205%** (**rounded**, ours, `×√12`); p.35's Portfolio Risk is **15.62%**. Same order of
magnitude, which tells you only that nobody has slipped a factor of ten. p.35's Active Risk of
**2.99%** is **10.5712 times** Book D's monthly active risk (**rounded**) — different book,
different model, different horizon, **no comparison intended**. A player who *tunes* a rebuild
until it matches p.35 has committed the error `gm/PLAYBOOK.md` flags at ★ THE REBUILD.

### 13g. What the notes do NOT support — searched across all 65 transcribed pages

- **No formula for marginal contribution to risk.** None. The phrase "marginal contribution"
  never appears. The bare word "marginal" occurs three times in `notes/` and **only one of those
  is the paper's own text** — p.7, "the **marginal benefit** of increasing granularity", about
  industry schema depth, a different idea entirely. The other two ("marginally the taller",
  p.23; "marginally finer", p.57) are **the transcriber's prose, not the paper's**. Grep hits are
  not citations; check whose sentence you landed in.
- **No formula for portfolio risk at all.** `wᵀΣw` does not appear; nor does `hᵀFh`. The p.24
  ingredient list is prose. The only expression of that shape anywhere in `notes/` is the
  `X_pᵀ F X_b / X_bᵀ F X_b` beta formula on p.4 — recorded as a **reader's handwritten pen
  annotation in the margin**, not printed text, and **never to be attributed to BlackRock**.
- **No derivation of the decomposition, and no statement that contributions sum to the total.**
  The p.35 pie sums to 100 and the paper never remarks on it.
- **"Tracking error" has zero occurrences.** The paper says **Active Risk**.
- **No stability, sensitivity or accuracy diagnostic for any contribution.** The Model Testing
  chapter (pp.32–33) prints no values at all.

**Landing sentence:**

> "The five numbers you just computed are the bars in Figure 1.18 on page 35, labelled
> *'Contrib. (% of Act. Risk)'* — and the paper plots them deliberately against a **second axis**
> carrying plain exposure, so that you can watch the two disagree. Its own industry panel does
> exactly what your Book D did: **Airlines** is ninth of ten by exposure and second by risk
> added, while **Food Household** carries two and a half times the position Airlines does and
> less than half the risk — and every one of those magnitudes is a pixel measurement off an
> unlabelled chart, so treat them as approximate, never as printed values. And when a portfolio manager says *'look how many names I hold'*, page 34 answers in
> plain words — the Active Risk is *'split equally between common factors and stock specific
> sources'* — which is 50% Specific on that pie, on a book run by professionals against a
> benchmark. Two things to say carefully and out loud. That pie splits **Active Risk, 2.99%**,
> not the Portfolio Risk of 15.62% printed three inches above it. And *Top Asset Contributions*
> is a **top-fifteen list**, not the portfolio: the report never tells you how many names that
> book holds, so neither of us gets to say. Last thing, and say it before anyone asks: the paper
> gives you the picture and **never gives you the formula.** The phrase *marginal contribution*
> does not appear in it. Everything you derived today is yours."

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level11.py     # 626 exact-rational assertions, exits 0
```

The script recomputes every figure on this page in `fractions.Fraction`, from the Level 7/8
returns file upward: the five factor-return solves and all 25 misses, with both Level 2 balance
conditions in all five months; `F` rebuilt from those series and `D` rebuilt from those misses;
`V = X F Xᵀ + D` for all five names, all 25 cells checked against the closed form
`25 + 6(x_i + x_j) + 9 x_i x_j (+ d_i)`, symmetry, both bracketings, and agreement with Level
10's 3×3 sub-block; every standalone volatility; Book D's exposures, factor and specific
variance, `V w`, MCR, contributions and shares, each as an exact rational; the exact nudge
identity `Var(w + ε u_i) = Var + 2ε(Vw)_i + ε²V_ii` swept over five names and eight nudge sizes;
the square-root nudge algebra `(σ + δ/2σ)² = Var + δ + δ²/4Var`; every worked trade in Section 7
with its first-order prediction and its exact answer side by side; the equal-MCR swap point
`t = 97/605`, proved a minimum against 60 nearby swap sizes; Euler and the shares-sum-to-one
identity swept over **2,226** books on a 5% grid and **1,450** zero-sum active books; the
benchmark, Book D's active decomposition including the exactly-zero and the negative marginal
contribution; all eight traps with the exact number each returns; the sabotage report, its
shortfall, its repair and two independent confirmations, plus **30** swept single-entry
corruptions all caught; the whole boss round including Book P's active table, the `1/n`
diversification floor and the zero-tilt counterfactual; and the p.35 banner and pie arithmetic,
including the two alternative digit readings the audit could not exclude.

Its final section exists purely for this page's typography: **every decimal the markdown prints**
— every MCR at three places, every contribution at four, every share at two or three, every
two-decimal short form used in the dialogue — is re-rendered from the exact rational and compared
string-for-string against what is written above. A rounding that drifted by one in the last digit
fails the script.

If any printed value ever disagrees with this markdown, the markdown is wrong.
