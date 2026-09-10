# Level 7 — The Timeline

Every number below is recomputed in exact rational arithmetic by `tools/verify_level7.py`
(238 assertions, exits 0). Nothing here is rounded by hand. Where a decimal does not
terminate it is written with the word **rounded** next to it; every other decimal on this
page is exact.

> **Difficulty warning, stated up front because the rulebook demands it.**
>
> This level is **not** graduate-level. Every piece of arithmetic on this page is Level 1,
> Level 5 or Level 6 machinery, turned five times. Nothing new is derived.
>
> What *is* hard here is entirely conceptual, and it is the thing the boss round tests:
> **the same five columns of numbers can be sliced two ways, and the two slices answer
> different questions.** Players do not fail this level on arithmetic. They fail it by
> quietly sliding back into a time-series picture — one stock, many dates — because that
> is the picture every textbook and every finance article they have ever read uses.
> Section 9 exists to make that slide impossible.
>
> Two things on this page *are* flagged honestly as beyond what is built:
> - **Section 8** (the noise floor) needs "the variance of a sum of independent things is
>   the sum of the variances". That is used, stated as an assumption, and **not proved**.
> - **Section 6e** (annualising) needs "variance grows in proportion to time". That is the
>   industry convention, it is **assumed**, and Section 6f shows the paper's own numbers
>   arguing against it.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the miss `e`, and why it is scored by its square.
**From Level 1** — `b = Σxr/Σx²`, derived by nudging; and √-market-cap regression weights (**p.25**).
**From Level 2** — `Σx·e = 0`, forced by the arithmetic of minimising.
**From Level 3** — two columns need two balance conditions at once; the 2×2 solve.
**From Level 4** — a coefficient is a *leftover*; `det = AC − B²`; overlap `cos² = B²/(AC)`;
`VIF = 1/(1 − cos²)`.
**From Level 5** — the intercept is a column of ones; centring a column moves the pivot to
`x̄` and turns `Σxr/Σx²` into `Cov/Var`.
**From Level 6** — `Var(b) = σ²/Q` with `Q = Σx²`; `σ̂² = SSE/(n − k)`; `t = b/SE`; BFRE's
own bar `|t| > 2` (**p.8**).

**Every single one of those was computed inside one month.** Level 0's five stocks were five
stocks *on one day*. Level 6's boss round was six stocks *in one month* — and its pass
condition already contained the sentence this level is built on:

> *"The player refuses to make the call from one month."*

That refusal has been an instruction until now. This level makes it an operation.

Three genuinely new things:

| | What Level 7 adds |
|---|---|
| **A second index** | Every quantity now carries a date. `x_i` becomes `x_{i,t}`, `b` becomes `f_t`. The regression is re-run from scratch each period on a **new set of exposures**, and nothing is carried over between periods except the *list of columns*. |
| **An output that is a row, not a number** | Five months of five stocks produce **five separate regressions** and **ten numbers** — one per factor per month. That row of numbers is the entire raw material for Level 8, and for Table 1.2 on **p.10** of the paper. |
| **A rival design, made concrete** | The same twenty-five returns can be sliced the other way — one stock, five dates — and Section 9 does exactly that, on the same file, and gets an answer with the **wrong sign**. |

**Locked, and staying locked:** the name of the grid Level 8 builds out of this row, and
everything downstream of it. This level stops at the diagonal.

---

## 1. The story — no mathematics

*(Domain: forestry. `gm/ANALOGIES.md` C9-A. If the player has already rejected this domain,
switch to C9-B or C9-C and do not re-dress this one.)*

Two foresters want to understand how trees grow.

The first spends a single afternoon in the wood with a measuring pole. She records the
height of five hundred trees, and for each one she also records how much light it stands
in, how deep its soil is, how close its neighbours are. By evening she can say a great deal
about how height goes with light and with soil — **across the whole wood, as it stands
today**.

The second forester picks one tree and measures it every year for forty years. At the end
he knows that tree's life in extraordinary detail. He can tell you exactly how it responded
to the drought of a particular decade, and what happened the year the tree next to it fell
over.

Now a new sapling is planted.

The first forester can place it in her picture **that same afternoon**. She knows its light
and its soil today, because those are things you can walk up to and measure. The second
forester can say nothing at all about it, and will be able to say nothing for many years,
because the sapling has no history and his whole method is history.

And here is the sting. The first forester goes back the next week and measures the wood
again — and she does not assume the light is the same. A neighbour has been felled; a tree
that stood in shade last week stands in sun this week. Her method re-reads every measurement
every time. The second forester's method cannot do that. **His forty-year answer for one
tree is a single number, and a single number cannot describe a tree that spent twenty years
in shade and twenty in sun.**

Both are doing real science. They are answering different questions, and only one of them
can answer on the first day.

---

## 2. Mapping the story onto the model, line by line

| In the story | In the model |
|---|---|
| the wood on one afternoon | one month's **cross-section** of stocks |
| one tree's height that afternoon | that stock's return this month, `r_{i,t}` |
| light, soil, crowding | the columns of exposures, `x_{i,t}` — **measured, not fitted** |
| "how height goes with light, across the wood today" | the factor return `f_t` from **one** regression |
| going back next week and measuring again | *"a series of cross-sectional regressions"* — **p.24** |
| the neighbour that was felled | an exposure that **changed between months** — Section 3a |
| forty years on one tree | a **time-series** regression on one stock — Section 9 |
| the newly planted sapling | a new listing; it has exposures on day one and no history at all |
| the second forester's single number | a beta: one number standing in for an exposure that moved |
| **measuring five hundred trees quickly and roughly** | the cost: every exposure is measured with error, every period |

The last row is the boss round. Hold it.

---

## 3. The file: five stocks, five months, exposures that move

Same five names the player has carried since Level 0. **New numbers** — this is not the
cold-open file, and saying so out loud prevents an hour of confusion.

One style column: **value exposure `x`**, a standardised score. It is *observed*, not
fitted — that is the whole design. It is re-read every month, and it moves.

### 3a. The exposures

| Stock | M1 | M2 | M3 | M4 | M5 | mean over the five months |
|---|---:|---:|---:|---:|---:|---:|
| AXL | −2 | −2 | −1 | −1 | −2 | **−8/5 = −1.6** |
| BRN | −1 | 0 | −2 | 0 | −1 | −4/5 = −0.8 |
| CHR | 0 | +1 | 0 | +1 | 0 | +2/5 = +0.4 |
| DLT | **+2** | **+2** | **+1** | **−1** | **+1** | **+1** |
| EMK | +1 | −1 | +2 | +1 | +2 | +1 |
| **Σ down the column** | **0** | **0** | **0** | **0** | **0** | |
| **`Q = Σx²`** | **10** | **10** | **10** | **4** | **10** | `ΣQ = 44` |

Three things to make the player say back before any arithmetic:

1. **Every column sums to zero.** That is Level 5's centring, imposed on purpose, and
   Section 4a shows exactly what it buys. BFRE does the same thing — **p.10**, and the
   weighting subtlety is in Section 11.
2. **DLT changes sign.** +2, +2, +1, then **−1**, then +1. A time-series method must
   represent DLT with *one* number. Ask the player which one, and let them fail.
3. **M4's column is squashed.** `Q = 4` where every other month has `Q = 10`. Nothing
   about the factor changed; the *spread of the exposures* changed. Level 6 called `Q`
   "distance covered". Section 7a collects the bill.

Also: **CHR sits at exactly zero in M1, M3 and M5.** Level 6 proved a stock at `x = 0` cannot
move the style dial at all. So CHR is unreachable in three months out of five — and reachable
in the other two. *A stock's unreachability is not a property of the stock. It is a property
of the month.*

### 3b. The returns

Percent, one month each.

| Stock | M1 | M2 | M3 | M4 | M5 |
|---|---:|---:|---:|---:|---:|
| AXL | +2.5 | +1.0 | −1.0 | +2.5 | +0.5 |
| BRN | +2.5 | −2.0 | −2.5 | +2.0 | +1.5 |
| CHR | +6.0 | −2.5 | −3.0 | +3.5 | 0.0 |
| DLT | +8.5 | −4.0 | −1.0 | −0.5 | +3.5 |
| EMK | +5.5 | −2.5 | −2.5 | +2.5 | +4.5 |
| **Σ** | **+25** | **−10** | **−10** | **+10** | **+10** |

Read that table **twice, deliberately**, because the whole level is in the reading:

- **Down a column** is one month across five stocks. That is a cross-section. There are five
  of them.
- **Across a row** is one stock over five months. That is a time series. There are five of
  those too, and they are made of the same twenty-five numbers.

Nothing in the data prefers one reading. The *model* prefers one. Section 9 runs the other.

---

## 4. Month 1 in full, by hand

Two columns: a column of ones (Level 5 says a column of ones **is** an intercept; BFRE says
the same on **p.26** and calls it the market factor) and the value column.

```
market column  =  [  1,   1,  1,   1,   1 ]
value column   =  [ −2,  −1,  0,  +2,  +1 ]
returns        =  [2.5, 2.5, 6.0, 8.5, 5.5]
```

### 4a. The 2×2 system is diagonal — and that is not luck, it is the centring

Level 3's Gram matrix, Level 4's names:

```
A = Σ 1·1 = n  = 5
B = Σ 1·x      = 0      ← because the column was centred
C = Σ x·x = Q  = 10
det = AC − B²  = 5·10 − 0 = 50
```

```
        ┌ 5   0 ┐ ┌ f_Mkt ┐   ┌ Σr  ┐
        │       │ │       │ = │     │
        └ 0  10 ┘ └ f_Val ┘   └ Σxr ┘
```

**`B = 0` is Level 4's collision number set to zero on purpose.** Overlap
`cos² = B²/(AC) = 0`; `VIF = 1/(1 − 0) = 1` exactly. There is no collision, so the two dials
do not have to be solved together — the 2×2 splits into two Level-1 problems:

```
f_Mkt = Σr/n        f_Val = Σxr/Q
```

Say plainly what has been bought and what has been assumed. **Bought:** five months of
arithmetic that a student can do on paper. **Assumed:** that the style column is centred.
BFRE *does* centre it (**p.10**) — but with weights, and Section 11 shows what changes.

### 4b. The two dials

```
Σr  = 2.5 + 2.5 + 6.0 + 8.5 + 5.5 = 25          f_Mkt = 25/5  = 5
Σxr = (−2)(2.5) + (−1)(2.5) + 0(6) + 2(8.5) + 1(5.5)
    = −5 − 2.5 + 0 + 17 + 5.5        = 15       f_Val = 15/10 = 3/2 = 1.5
```

`f_Mkt = 5` is the **plain average return of the five stocks**. That is Level 1's collapse:
a column of ones has `x = 1` everywhere, so `Σxr/Σx²` becomes `Σr/n`. BFRE's footnote 2 on
**p.4** says the market factor return *is* the cross-sectional average return — and Level 5
showed why it survives having other columns in the regression: because the other columns are
centred. This month is that argument in five numbers.

### 4c. Fitted, missed, balanced

```
fitted = f_Mkt + f_Val·x = [ 5−3, 5−1.5, 5, 5+3, 5+1.5 ] = [2, 3.5, 5, 8, 6.5]
e      = r − fitted                                       = [+0.5, −1, +1, +0.5, −1]

Σe    = 0.5 − 1 + 1 + 0.5 − 1                      = 0    ← Level 2, market column
Σx·e  = (−2)(0.5) + (−1)(−1) + 0(1) + 2(0.5) + 1(−1)
      = −1 + 1 + 0 + 1 − 1                         = 0    ← Level 2, value column
SSE   = 0.25 + 1 + 1 + 0.25 + 1                    = 7/2 = 3.5
```

Both balances hold, so the fit is genuine. Nothing on this page is new. **That is the point:
Level 7 does not teach you a new regression. It teaches you to run the old one again.**

---

## 5. The other four months — the same handle, four more turns

Each month is a **separate** regression. Nothing is carried across the join except the
identity of the two columns.

| Month | `f_Mkt` | `f_Val` | `Q` | residuals `e` | `SSE` |
|---|---:|---:|---:|---|---:|
| M1 | **+5** | **+3/2** | 10 | [+1/2, −1, +1, +1/2, −1] | 7/2 |
| M2 | **−2** | **−1** | 10 | [+1, 0, +1/2, 0, −3/2] | 7/2 |
| M3 | **−2** | **0** | 10 | [+1, −1/2, −1, +1, −1/2] | 7/2 |
| M4 | **+2** | **+1** | 4 | [+3/2, 0, +1/2, −3/2, −1/2] | 5 |
| M5 | **+2** | **+1** | 10 | [+1/2, +1/2, −2, +1/2, +1/2] | 5 |

Every row is checked: `Σe = 0` and `Σx·e = 0` in all five months. Total miss over the whole
file: `Σ SSE = 41/2 = 20.5`.

Worked example for M5, so the player has two done in full:

```
Σr  = 0.5 + 1.5 + 0 + 3.5 + 4.5                                = 10   →  f_Mkt = 10/5 = 2
Σxr = (−2)(0.5) + (−1)(1.5) + 0(0) + 1(3.5) + 2(4.5)
    = −1 − 1.5 + 0 + 3.5 + 9                                   = 10   →  f_Val = 10/10 = 1
```

**M3 is the month the factor did nothing.** `Σxr = 0` exactly, so `f_Val = 0`, and every
fitted return in M3 is the same number, `−2`. A player who has only ever seen one month
would report "the value factor is worthless" and be reporting one draw.

### 5a. Count what came out

```
regressions run          =  5      ← one per month, five rows each
rows in each regression  =  5      ← the stocks
numbers produced         = 10      ← 5 months × 2 factors
```

**One number per factor per month.** Say it, and make the player say it. The rulebook's
diagnostic for this level (`gm/PLAYBOOK.md`) is exactly this: *"I hand you 60 months of
returns for 500 stocks. Tell me exactly what you regress on what, how many regressions you
run, and how many numbers come out."* The answer is 60 regressions of 500 rows, one number
per factor per month. Anyone who says "500 regressions of 60 rows" has built the rival design and does
not know it.

---

## 6. The factor-return time series — this level's output

The ten numbers, laid out as two rows:

| | M1 | M2 | M3 | M4 | M5 |
|---|---:|---:|---:|---:|---:|
| **`f_Mkt`** | +5 | −2 | −2 | +2 | +2 |
| **`f_Val`** | +3/2 | −1 | 0 | +1 | +1 |

**Those two rows are the product of this level.** Everything below is arithmetic *on* them —
and every one of those operations is something the paper does to its own factor returns.

### 6a. The mean of each row

```
mean f_Val = (3/2 − 1 + 0 + 1 + 1)/5 = (5/2)/5 = 1/2 = 0.5 %  per month
mean f_Mkt = (5 − 2 − 2 + 2 + 2)/5   = 5/5     = 1          %  per month
```

### 6b. The spread of each row — and `T − 1`, not `T`

Deviations from the mean:

```
f_Val:  d = [ +1, −3/2, −1/2, +1/2, +1/2 ]      Σd = 0      Σd² = 4
f_Mkt:  d = [ +4,   −3,   −3,   +1,   +1 ]      Σd = 0      Σd² = 36
```

Level 6 settled the denominator, and the argument transfers with no change: fitting one
number — here the mean — costs exactly one degree of freedom, so

```
degrees of freedom = T − 1 = 5 − 1 = 4

sample variance of f_Val = 4/4  = 1        sample sd = 1   exactly
sample variance of f_Mkt = 36/4 = 9        sample sd = 3   exactly
```

Both roots are exact; there is nothing to round. If instead you divide by `T`:

```
population variance f_Val = 4/5  = 0.8     √0.8  = 0.894427 (rounded)
population variance f_Mkt = 36/5 = 7.2     √7.2  = 2.683282 (rounded)
```

Both conventions appear in the wild. **The paper never states which it uses**, and its
"Annualised Volatility" column on **p.10** carries no formula — see Section 17c.

### 6c. And now Level 6, run down the timeline instead of across it

The mean of a row is itself an estimate, so it has its own wobble. Level 6's machine, with
the *months* as the observations:

```
Var(mean f_Val) = (sample variance)/T = 1/5      SE = √(1/5) = 0.447214 (rounded)
Var(mean f_Mkt) = 9/5                            SE = √(9/5) = 1.341641 (rounded)

t² for mean f_Val = (1/2)²/(1/5) = 5/4 = 1.25    t = 1.118034 (rounded)
t² for mean f_Mkt = (1)²/(9/5)   = 5/9           t = 0.745356 (rounded)
```

**Neither clears `|t| > 2`.** Five months of a real factor and a real market and the file
cannot distinguish either average from zero. Level 6 said a t near 1 is not weak evidence but
*no* evidence; here is that sentence with a date index on it. **INFER**, and worth saying as
such: it is why a table like Table 1.2 covers **Mar 1996 – Dec 2013** rather than five months.
The paper prints that window and never says why it chose it.

*(Section 12 names the two-stage procedure — monthly cross-sections, then a mean and a
standard error of the resulting row. The name is not in the paper.)*

### 6d. The cross-term — computed, named, and then handed to Level 8

```
Σ d_Mkt · d_Val = 4(1) + (−3)(−3/2) + (−3)(−1/2) + 1(1/2) + 1(1/2)
                = 4 + 4.5 + 1.5 + 0.5 + 0.5            = 11

sample covariance = 11/4 = 2.75
correlation       = (11/4)/(3 × 1) = 11/12 = 0.916667 (rounded)
```

Three numbers now exist — `1`, `9`, and `11/4` — and they are the whole of a 2×2 grid.
**Building that grid, and knowing what it is for, is Level 8's job, and its name is Level 8's
to hand over.** Stop here. What this level owes Level 8 is the row, not the grid.

Worth flagging honestly at the table: `11/12` is a *very* high correlation between a market
factor return and a style factor return, and the real NAMR value factor's correlation with
the market is **0.03** (Table 1.2, **p.10**, printed). These are teaching numbers, chosen so
Section 9's arithmetic lands cleanly; say so rather than letting the player calibrate on them.

### 6e. Cumulative sums — what Figures 1.7, 1.12 and 1.14 actually plot

Running totals of the two rows:

| | M1 | M2 | M3 | M4 | M5 |
|---|---:|---:|---:|---:|---:|
| cumulative `f_Mkt` | +5 | +3 | +1 | +3 | **+5** |
| cumulative `f_Val` | +3/2 | +1/2 | +1/2 | +3/2 | **+5/2** |

The last entry is `T × mean` in both cases (`5 × 1 = 5`, `5 × 1/2 = 5/2`) — a cumulative chart
is a picture of the mean, drawn slowly. Every "cumulative performance" figure in the paper is
this operation applied to a series produced exactly the way Section 5 produced ours.

**GAP, and say it out loud.** The paper never states whether its cumulative series are sums of
returns or compounded products. `notes/` records the captions and the axes and no formula. We
use the sum; the paper may not.

### 6f. Annualising — the convention, and the assumption inside it

To compare a monthly row with Table 1.2's **annualised** columns:

```
annualised mean     = 12 × monthly mean
annualised variance = 12 × monthly variance
```

```
f_Val:  12 × 1/2 = 6 %          12 × 1 = 12       √12  = 3.464102  (rounded)
f_Mkt:  12 × 1   = 12 %         12 × 9 = 108      √108 = 10.392305 (rounded)
```

Return over volatility, annualised — the shape of Table 1.2's "Sharpe Ratio" column:

```
f_Val:  6/√12   →  squared = 3      ratio = √3   = 1.732051 (rounded)
f_Mkt: 12/√108  →  squared = 4/3    ratio = √(4/3) = 1.154701 (rounded)
```

For scale: Table 1.2 (**p.10**, printed digits) gives NAMR **Value 3.3% / 2.3% / Sharpe 1.43**
and **Market 7.0% / 19.8% / Sharpe 0.35**. Our toy value factor lands in the same
neighbourhood; our toy market factor is far too calm, because five invented months cannot
contain a financial crisis.

**Now the assumption, and it is a real one.** `variance × 12` says the months are unrelated —
that knowing last month tells you nothing about this month. Our own row says otherwise:

```
first-order autocorrelation, f_Val = (Σ d_t d_{t+1})/Σd²
                                   = (1(−3/2) + (−3/2)(−1/2) + (−1/2)(1/2) + (1/2)(1/2)) / 4
                                   = (−3/2 + 3/4 − 1/4 + 1/4)/4 = (−3/4)/4 = −3/16 = −0.1875

first-order autocorrelation, f_Mkt = (4(−3) + (−3)(−3) + (−3)(1) + 1(1))/36
                                   = (−12 + 9 − 3 + 1)/36 = −5/36 = −0.138889 (rounded)
```

That is one convention among several, and **the paper does not state which convention its own
autocorrelation column uses** — say so. But the direction of the lesson is safe and it is the
paper's own: Table 1.2's last column prints **Momentum 0.22** and **Reversal 0.17**, both
positive and both material. A series with autocorrelation 0.22 does **not** have a variance
that grows by a clean factor of 12 over a year. **The paper prints an annualised volatility
column and an autocorrelation column on the same table and never reconciles them.** That is
Level 12 ammunition, earned here — and it is also exactly why **p.3** says the factor
covariance matrices are constructed from a daily series of factor returns *"correcting for
serial correlations"*, and why **p.27** says Portfolio Risk Tools lets users *"control for
serial correlations and asynchronicity in the factor return series"*. The correction is named
in the paper; its method is not, and neither page prints one.

---

## 7. A t-statistic per month — Level 6, five times

Inside each cross-section: `n = 5` stocks, `k = 2` columns, so

```
df = n − k = 3          ← NOT n − 1 = 4. Level 6, trap 1.
σ̂²_t = SSE_t/3          Var(f_Val,t) = σ̂²_t/Q_t          Var(f_Mkt,t) = σ̂²_t/n
```

| Month | `SSE` | `σ̂²` | `Q` | `Var(f_Val)` | `t²` | `t` *(rounded)* | `\|t\| > 2`? |
|---|---:|---:|---:|---:|---:|---:|:--:|
| M1 | 7/2 | 7/6 | 10 | 7/60 | 135/7 | **+4.391550** | **YES** |
| M2 | 7/2 | 7/6 | 10 | 7/60 | 60/7 | **−2.927700** | **YES** |
| M3 | 7/2 | 7/6 | 10 | 7/60 | 0 | 0 *(exact)* | no |
| M4 | 5 | 5/3 | **4** | 5/12 | 12/5 | +1.549193 | no |
| M5 | 5 | 5/3 | 10 | 1/6 | 6 | **+2.449490** | **YES** |

The market column, same machine with `Q = n = 5`:

```
Var(f_Mkt) = [7/30, 7/30, 7/30, 1/3, 1/3]
t²         = [750/7, 120/7, 120/7, 12, 12]
t(M1) = +10.350983 (rounded)   t(M2) = t(M3) = −4.140393 (rounded)
t(M4) = t(M5) = +3.464102 (rounded)
```

All five market months clear the bar. Three of the five value months do.

### 7a. M4 against M5 — the level's sharpest single comparison

Run this as a **round type A (predict-then-reveal)**. Show the player only this:

| | `f_Val` | `SSE` | `σ̂²` | `Q` |
|---|---:|---:|---:|---:|
| M4 | +1 | 5 | 5/3 | **4** |
| M5 | +1 | 5 | 5/3 | **10** |

*Same factor return. Same total miss. Same typical miss. Ask them whether the two months
give the same verdict, and why.*

```
Var(f_Val, M4) = (5/3)/4  = 5/12          Var(f_Val, M5) = (5/3)/10 = 1/6
ratio                      = (5/12)/(1/6) = 5/2 = 2.5 exactly = Q₅/Q₄ = 10/4

t²(M4) = 12/5 = 2.4   →  t = 1.549193 (rounded)   →  FAILS  |t| > 2
t²(M5) = 6           →  t = 2.449490 (rounded)   →  CLEARS |t| > 2
```

**The factor paid the same, and one month calls it significant and the other does not.** The
only thing that changed is how far apart the exposures were — Level 6's "distance covered",
now varying month by month because the exposures themselves vary month by month.

This is the deepest consequence of the cross-sectional design, and it has no analogue in a
time-series model: **the precision of this month's answer is a property of this month's
cross-section**, and it is outside anyone's control. In M4 the five stocks simply were not
spread out on value.

### 7b. The proportion of significant months — this is BFRE's selection statistic

```
months with |t| > 2   =  3        of 5
proportion            =  3/5 = 60%
average squared t     =  (135/7 + 60/7 + 0 + 12/5 + 6)/5 = 1269/175 = 7.251429 (rounded)
```

Both of those numbers are the paper's, by name:

- **p.14**: *"A value in excess of **10%** [proportion of significant t-statistics] indicates a
  statistically significant style effect, and would be considered for inclusion in the
  models."* (The bracket is `notes/`'s gloss, kept visible so it is not mistaken for printed
  text.) Footnote 11 on the same page:
  *"t-statistics are based on **monthly cross-sectional regressions**."* Our 60% clears it.
- **p.8**: BFRE also computes the **average squared t-statistic** — and the paper's printed
  reason for it is *"to distinguish between factors with t-statistics close to +/- 2 and those
  that are significantly higher"*. **Quote only that clause**: `notes/` records the surrounding
  framing ("Also computed: the average squared t-statistic, computed specifically …") as the
  transcriber's sentence, not the paper's. Our `1269/175` is that statistic, on five months.
- **p.32**: *"Individual factor efficacy is assessed using a history of t-statistics for each
  common factor by calculating the proportion of significant t-statistics over different
  periods."*

**So Level 6's t-statistic and Level 7's timeline are not two topics. They are one procedure,
and the paper runs it on a fifteen-year history.** Figure 1.8 (**p.15**) is nothing but this
column, computed for twelve NAMR styles and sorted — value measures at **≈34%**
`[APPROX — pixel-measured from the scan; the figure prints no data labels]`.

Do not let the player compare our 60% to that 34% as if both were the same kind of number.
Ours is five invented months; theirs is a measured bar height off a photocopy of a fifteen-year
study. Say which is which every time.

---

## 8. The noise floor — how much of that spread is real?

Level 8 is going to take the row `f_Val = [3/2, −1, 0, 1, 1]` and treat its variance as the
factor's risk. Before it does, this level owes it one honest correction.

Each month's `f̂_t` is an **estimate**, not the truth. Write

```
f̂_t  =  f_t  +  ν_t
```

where `f_t` is what the factor really paid and `ν_t` is this month's estimation error.
Section 7 already computed the size of `ν_t` — it is `Var(f̂_t) = σ̂²_t/Q_t`, month by month.

**The assumption, named as an assumption** (this is the bit that is *not* built here): the
errors `ν_t` are unrelated to the true `f_t` and unrelated to each other across months. Then
the variance of a sum is the sum of the variances, and

```
expected sample variance of the observed row  =  variance of the truth  +  average Var(ν_t)
```

so

```
        ┌─────────────────────────────────────────────────────────────┐
        │  variance of the truth  =  observed variance  −  noise floor │
        └─────────────────────────────────────────────────────────────┘
```

On this file:

```
noise floor, f_Val = mean of [7/60, 7/60, 7/60, 5/12, 1/6]
                   = (7/60 + 7/60 + 7/60 + 25/60 + 10/60)/5 = (56/60)/5 = 14/75
                   = 0.186667 (rounded)

observed sample variance                            = 1
so the honest estimate of the factor's own variance = 1 − 14/75 = 61/75 = 0.813333 (rounded)
```

**18.67% (rounded) of what looks like value-factor risk in this file is the estimation error
of the monthly regressions.** Do the same for the market row:

```
noise floor, f_Mkt = mean of [7/30, 7/30, 7/30, 1/3, 1/3] = 41/150 = 0.273333 (rounded)
observed variance  = 9
truth              = 9 − 41/150 = 1309/150 = 8.726667 (rounded)
noise share        = (41/150)/9 = 41/1350 = 0.030370 (rounded)  ≈ 3.04%
```

**3.04% for the market row against 18.67% for the value row**, and the reason is structural, not
accidental: the market factor moves a lot relative to how precisely it is measured; the style
factor does not. A grid built from these rows overstates every variance, and overstates the
*small* ones most.

Three honest labels on this section:

- The correction itself is **ours**. `notes/` contains nothing about estimation error in `f̂`
  inflating the variance of the factor-return series — no correction, no mention, in 65 pages.
- The box is an equation about an **expected** sample variance, and we then apply it to the one
  sample variance we actually have. That step — treating a single realisation as its own
  expectation — is the same law-of-large-numbers IOU Level 6 flagged twice. On five months it
  is a rough correction, not a precise one. Say so.
- The independence assumption is **not proved here** and is not obviously true: an exposure
  measured with a systematic error (a stale data vendor, a price-driven column) produces `ν_t`
  that are *related* across months, and then this correction is the wrong size.
- What the paper *does* correct is a different thing wearing similar words: **p.3** says the
  factor covariance matrices are built *"correcting for serial correlations"* (**p.27** puts
  that control in the user's hands via PRT), and **p.30** truncates currency factor returns at
  **±8% daily / ±20% weekly** before they enter. Neither of those is this.

---

## 9. The contrast — a time-series beta, on the same twenty-five numbers

Now slice the table the other way: one stock, five dates.

Take **AXL**. Its value exposure was `−2, −2, −1, −1, −2` — **negative in every single
month**, average `−8/5 = −1.6`. Its returns were

```
AXL:  +2.5, +1.0, −1.0, +2.5, +0.5        mean = 11/10 = 1.1
```

### 9a. Same formula, one index swapped

Level 5's centred formula, `slope = Cov/Var`, with the **months** as the observations and the
**factor return series** as the column:

```
column      f_Val   = [ 3/2,  −1,   0,   1,   1 ]     d_Val = [ +1, −3/2, −1/2, +1/2, +1/2 ]
observations r_AXL  = [ 2.5, 1.0, −1.0, 2.5, 0.5 ]    dev   = [ +1.4, −0.1, −2.1, +1.4, −0.6 ]

numerator = Σ d_Val · dev
          = 1(1.4) + (−3/2)(−0.1) + (−1/2)(−2.1) + (1/2)(1.4) + (1/2)(−0.6)
          = 1.4 + 0.15 + 1.05 + 0.7 − 0.3                                    = 3
denominator = Σ d_Val²                                                        = 4
```

```
        ┌────────────────────────────────────────────────┐
        │   time-series slope for AXL  =  3/4  =  +0.75  │
        └────────────────────────────────────────────────┘

intercept = 11/10 − (3/4)(1/2) = 29/40 = 0.725        SSE = 129/20 = 6.45
```

**AXL's value exposure was negative in all five months, and the time-series regression returns
`+0.75`.** Not a different number. The **wrong sign**.

Make the player sit with that before explaining it. This is not a bug in the arithmetic — both
numbers are correct, and both are answers to questions. They are different questions:

| Question | Method | Answer |
|---|---|---|
| *"How cheap was AXL this month, relative to the market?"* | read the column | **−2** in M1; **−1** in M3 |
| *"Over these five months, did AXL's return move with the value factor's return?"* | fit down the time index | **+0.75** |

### 9b. Where the `+3/4` comes from — every term, no hand-waving

The numerator `3` decomposes exactly, because each return was built as
`r = f_Mkt + x·f_Val + e`:

```
Σ d_Val · r_AXL  =  Σ d_Val · f_Mkt      (the market channel)
                 +  Σ d_Val · x_AXL · f_Val   (the exposure channel)
                 +  Σ d_Val · e_AXL      (the residual channel)
```

```
market channel   = 1(5) + (−3/2)(−2) + (−1/2)(−2) + (1/2)(2) + (1/2)(2)
                 = 5 + 3 + 1 + 1 + 1                                    = +11
exposure channel = (1)(−2)(3/2) + (−3/2)(−2)(−1) + (−1/2)(−1)(0)
                     + (1/2)(−1)(1) + (1/2)(−2)(1)
                 = −3 − 3 + 0 − 0.5 − 1                                 = −15/2
residual channel = 1(1/2) + (−3/2)(1) + (−1/2)(1) + (1/2)(3/2) + (1/2)(1/2)
                 = 0.5 − 1.5 − 0.5 + 0.75 + 0.25                        = −1/2
                                                                   sum  = +3  ✓
```

Divide each by `Σd² = 4`:

| Channel | Contribution to the slope | |
|---|---:|---|
| the market factor, leaking in | **+11/4 = +2.75** | this is exactly the two rows' sample covariance, Section 6d |
| AXL's actual (moving) exposure | **−15/8 = −1.875** | the thing we wanted to measure |
| AXL's own residuals | **−1/8 = −0.125** | five months is not many |
| **total** | **+3/4 = +0.75** | |

**The sign flip is Level 4, relocated.** The time-series regression left out a column — the
market factor return — that overlaps the column it kept. Level 4 called that a leftover
problem and priced it; here the price is a coefficient that points the wrong way.

### 9c. Put both columns in — Level 3's 2×2, run down the time index

```
A = Σ d_Mkt²      = 36
B = Σ d_Mkt d_Val = 11
C = Σ d_Val²      = 4
det = AC − B² = 144 − 121 = 23

p = Σ d_Mkt · dev(r_AXL) = 4(1.4) + (−3)(−0.1) + (−3)(−2.1) + 1(1.4) + 1(−0.6) = 13
q = Σ d_Val · dev(r_AXL)                                                        = 3

slope on f_Mkt = (Cp − Bq)/det = (52 − 33)/23 =  19/23 =  0.826087 (rounded)
slope on f_Val = (Aq − Bp)/det = (108 − 143)/23 = −35/23 = −1.521739 (rounded)
```

Done properly, the sign is right and the size is sensible: `−1.52` against an average
exposure of `−1.6`. **And it is still one number.** AXL's exposure took two distinct values
over these five months and the method has no slot to put the second one in.

Two more numbers before leaving this fit, both of them Level 4's:

```
overlap between the two series:  cos² = B²/(AC) = 121/144 = 0.840278 (rounded)
VIF = 1/(1 − cos²) = 144/23 = 6.260870 (rounded)
df  = T − 3 = 2
```

A VIF of 6.26 on two degrees of freedom. **This is a bad regression**, and the badness is not
fixable by being cleverer — it is what you get when you have five observations and want to
separate two things that move together. A time-series method needs a long history. BFRE's own
one, (1.12) on **p.42**, uses **5 years of weekly observations** — 260 of them — and the next
subsection says what that buys and what it costs.

### 9d. The second exhibit — DLT, whose exposure changes sign

```
DLT returns   = [8.5, −4.0, −1.0, −0.5, 3.5]      mean = 13/10 = 1.3
numerator     = Σ d_Val · dev = 33/2 = 16.5       denominator = 4

time-series slope = 33/8 = 4.1250            intercept = −61/80 = −0.7625
```

DLT's actual exposures were `+2, +2, +1, −1, +1`, average `+1`. **The time-series slope is
4.125 times the average exposure**, and it is a single positive number for a stock that spent
one of the five months on the *other side* of the factor.

Ask the player which number they would put in a risk model for DLT's value exposure in M4,
when the true answer that month was `−1`. There is no good answer. That is the point.

### 9e. What BFRE's own time-series regression is for

The paper runs a time-series regression **exactly once**, and it is worth being precise about
what comes out of it. **p.42**, equation **(1.12)**, Historical Beta:

```
r_{i,s} = alpha_i + beta_i · r^M_{i,s} + epsilon_{i,s}
```

described on the page as *"The estimated slope coefficient β̂_i from an exponentially weighted
univariate regression of asset returns r on a market index r^M"*, with three qualifying lines
printed underneath it:

> *"All returns are weekly and in excess of the local risk-free rate."*
> *"The market index is defined as the market capitalisation-weighted Estimation Universe."*
> *"The exponential weighting function has a half-life of 52 weeks, and uses 5 years of weekly
> observations."*

Run the same shape on our file — AXL's returns against the **market** row:

```
slope = Σ d_Mkt · dev(r_AXL) / Σ d_Mkt² = 13/36 = 0.361111 (rounded)
```

And AXL's market exposure in the model? **1.** Every asset's is 1, in every month — **p.4**:
*"all equity assets have a **unit exposure** to this factor."* So the time-series answer
(`0.36`) and the model's exposure (`1`) are not even close, and they are not supposed to be:
they are different objects.

**Here is the sentence the level exists to produce.** BFRE does run a time-series regression —
and its output is fed back in as an **input substyle to Volatility** (Historical Beta,
**p.42**, **p.44**). It is a *characteristic of the stock*, one more column of `X`. It is
**never** the mechanism by which exposures are obtained, and it never produces a factor
return. In BFRE, time-series regressions make columns; cross-sectional regressions make the
row.

---

## 10. The other rival — pooling all twenty-five observations

Every player eventually asks it: *why not stack all twenty-five stock-months into one big
regression?* Run it, and price it.

```
25 observations           Σx = 0        Σx² = 44        Σr = 25        Σxr = 19
                          Σr² = 272

pooled f_Mkt = Σr/25  = 25/25 = 1
pooled f_Val = Σxr/Σx² = 19/44 = 0.431818 (rounded)
```

### 10a. The pooled style number is a `Q`-weighted average of the monthly ones

```
Σ Q_t · f_Val,t = 10(3/2) + 10(−1) + 10(0) + 4(1) + 10(1) = 15 − 10 + 0 + 4 + 10 = 19
Σ Q_t                                                       = 44

so   pooled f_Val = 19/44   =   Σ Q_t f_t / Σ Q_t      ← exactly the pooled estimate
```

whereas the timeline's answer is the **plain** average:

```
mean of the monthly f_Val = 1/2 = 22/44
gap                        = 22/44 − 19/44 = 3/44 = 0.068182 (rounded)
```

The gap has a precise cause. M4 — the squashed month, `Q = 4` — carries weight `4/44 = 1/11`
in the pooled answer and weight `1/5` in the monthly average. **Pooling silently weights each
month by how spread out its exposures happened to be.** Nobody chose that. It is a
side-effect.

The market number happens to agree (`1` both ways) because every month has the same number of
stocks. That coincidence is worth showing and then destroying: it is `n`, not `Q`, that
weights the market column, and `n` is constant here.

### 10b. What pooling throws away, measured

```
pooled SSE                 = 10507/44 = 238.795455 (rounded)
sum of the five monthly SSEs =  41/2  =  20.5
```

and the difference is not a mystery — it decomposes exactly:

```
Σ_t n·(f_Mkt,t − pooled f_Mkt)²  = 5 × 36                       = 180
Σ_t Q_t·(f_Val,t − pooled f_Val)²                               = 1685/44 = 38.295455 (rounded)

    20.5  +  180  +  1685/44   =  10507/44    ✓ exactly
```

```
extra miss created by pooling = 9605/44 = 218.295455 (rounded)
ratio pooled/monthly          = 10507/902 = 11.648559 (rounded)
```

**Pooling multiplies the unexplained return by 11.65.** And the whole of that increase is
precisely the month-to-month variation in the factor returns — the thing this level produces
and Level 8 is about to use. *A pooled regression does not lose the timeline by accident; it
converts the timeline into residual.*

### 10c. One month is not a small version of the timeline

| Evidence | Verdict on the value factor |
|---|---|
| M1 alone | `f_Val = +3/2`, `t = +4.39` (rounded) — **strong, positive** |
| M2 alone | `f_Val = −1`, `t = −2.93` (rounded) — **strong, negative** |
| M3 alone | `f_Val = 0`, `t = 0` — **nothing at all** |
| the five together | mean `+1/2`, `t = 1.118034` (rounded) — **cannot tell** |
| pooled | `19/44 = 0.431818` (rounded) — a fourth number, weighted by nobody's choice |

Five defensible procedures, five different answers, one file.

---

## 11. The weight, put back in for one month

The five-month file above is **equally weighted**, so the arithmetic fits on a page. BFRE is
not. **p.25**:

> *"Assets are weighted in the regression using square-root of market capitalisation… More
> technically, square-root of market capitalisation **adjusts for heteroskedasticity** based on
> the observation that higher residual (specific) risk is typically correlated with smaller
> market capitalisation assets."*

Level 1 built the weighted dial and Level 2 the weighted balance. Redo **M1** with market caps
`4, 1, 1, 1, 9` — so the weights `w = √cap` are `2, 1, 1, 1, 3`:

```
Σw     = 8            Σw·x   = 2(−2) + (−1) + 0 + 2 + 3(1) = 0     ← still centred, this month
Σw·x²  = 2(4) + 1 + 0 + 4 + 3(1)                           = 16
Σw·r   = 2(2.5) + 2.5 + 6 + 8.5 + 3(5.5)                   = 77/2 = 38.5
Σw·x·r = 2(−2)(2.5) + (−1)(2.5) + 0 + 2(8.5) + 3(1)(5.5)   = 21

f_Mkt = 38.5/8 = 77/16 = 4.8125          f_Val = 21/16 = 1.3125
```

Against the equal-weighted `5` and `3/2`:

```
the market dial moved by 5 − 77/16   = 3/16 = 0.1875
the value  dial moved by 3/2 − 21/16 = 3/16 = 0.1875
```

Both balances still hold, in their weighted form:

```
weighted residuals e = [ 5/16, −1, 19/16, 17/16, −5/8 ]
Σ w·e   = 2(5/16) − 1 + 19/16 + 17/16 + 3(−5/8) = 0        ✓
Σ w·x·e = 2(−2)(5/16) + (−1)(−1) + 0 + 2(17/16) + 3(1)(−5/8) = 0   ✓
weighted SSE = 157/32 = 4.90625
```

Two things to say out loud, because both are traps:

1. **`Σw·x = 0` happened to hold this month.** Our column was centred with *equal* weights and
   M1's numbers make it centred under these weights too — a coincidence of this month, not a
   law. In M2, M3, M4 and M5 it does not hold, `B ≠ 0`, and the honest 2×2 of Level 3 comes
   back. **BFRE removes the coincidence by construction**: **p.10** standardises every
   substyle so that *"the transformed substyles (and styles) have the property that their
   **weighted average is zero**"* — weighted by √-market-cap, the same weights the regression
   uses. That is why the market column and the style columns stay out of each other's way in a
   real BFRE cross-section, and it is Level 5's argument arriving at Level 7 with a page number.
2. **Everything in Sections 6, 7 and 8 inherits the weights.** Every `f`, every `SE`, every
   `t` in the paper is a weighted quantity. Our unweighted file is a teaching simplification
   and should be labelled as one every time it is used.

---

## 12. Names unlocked at the end of this level

| Name | What it actually is, in this level's terms | Status in the paper |
|---|---|---|
| **cross-sectional regression** | one regression, one date, many stocks — Sections 4 and 5 | **the paper's own core phrase**: p.24, p.30, and footnotes 11 (p.14) and 12 (p.16). p.32's "cross-sectional *variation*" is a different phrase |
| **factor-return time series** | the row in Section 6 — one number per factor per period | the object behind Table 1.2 (p.10) and every cumulative-performance figure |
| **time-series regression** | one stock, many dates — Section 9 | the paper runs one: (1.12), p.42. It never calls it that |
| **pooled / panel regression** | all stock-months in one solve — Section 10 | **neither word appears in the paper** |
| **Fama–MacBeth** | the industry name for exactly Sections 5 + 6c: run cross-sections period by period, then take the mean of the row and its standard error | **never appears in the paper** — no mention, no citation |
| **cumulative factor return** | the running sum of Section 6e | Figures 1.7 (p.14), 1.12 (p.18), 1.14 (p.20) — the paper never states whether it sums or compounds |
| **estimation error in `f̂`, and the noise floor** | Section 8 — the part of the row's spread that is measurement, not market | **nothing in the paper** |
| **stationarity** | the assumption a time-series beta needs: that the thing being measured did not change over the window | **never appears.** And the paper's own p.17 says style exposures *do* change |

Run a **round type F (vocabulary under fire)** on:

> *"We estimate cross-sectionally, so the exposures are observed rather than fitted — which
> means the factor returns are a monthly series, not a set of betas."*

Plain English, then a fresh sentence of their own. **The tell to hunt for:** a player who
translates "cross-sectional" as "across the market" and stops. The word that must appear in
their translation is **date** — one date, many stocks. A player who cannot say which index is
held fixed has recognised the word and not the object.

---

## 13. Traps, and exactly what each wrong belief returns numerically

| Wrong belief | What it returns | The refutation |
|---|---|---|
| "a stock's exposure is its time-series slope" | AXL: **+0.75** | AXL's exposure was negative in all five months (max `−1`). Section 9b decomposes the sign flip into three named channels |
| "then just average the monthly exposures" | AXL: **−1.6**, DLT: **+1** | Not the same object as a slope, and not the same number: DLT's slope is `33/8 = 4.125`. Averaging also throws away the very variation that made M4 different from M3 |
| "pool all the stock-months, it's more data" | `f_Val = 19/44 = 0.431818` (rounded) | Not the timeline's `1/2`. Pooling weights each month by `Q_t` (Section 10a) and inflates the miss by **11.65×** (Section 10b) |
| "the series' variance is the factor's variance" | `1` | `61/75 = 0.813333` (rounded) after removing the noise floor `14/75`. The error is **18.67%** here, and it is worst for the quietest factors |
| "a month with a small `t` means the factor didn't work" | M4: `t = 1.549193` (rounded) | M4 and M5 have **identical** `f` and `σ̂²`. Only `Q` differs, `4` against `10`, and `t²` differs by exactly `5/2` |
| "`f_Mkt` is the plain average return" | M1: **5** | With √-cap weights, `77/16 = 4.8125`. It is the *weighted* average, and only because `Σw·x = 0` (p.10) |
| "more stocks make the series longer" | — | More stocks raise `Q`, which sharpens each `f̂_t`. Only more **months** raise `T`, which is what `Var(mean) = variance/T` and `df = T − 1` need. Level 6's "distance covered, not count", with a date on it |
| "five months is a small version of fifteen years" | mean `t = 1.118034` (rounded) | It is not a small version; it is *no* version. The mean of the row is indistinguishable from zero. Table 1.2 covers **Mar 1996 – Dec 2013**; the paper prints that window and never justifies it |
| "annualise volatility by ×√12" | `√12 = 3.464102` (rounded) | Assumes months are unrelated. Our own row has autocorrelation `−3/16`; the paper prints **+0.22** for Momentum and **+0.17** for Reversal (Table 1.2, p.10) |
| "the exposures are fixed, we just refit the returns" | — | Then M4 could not exist. `Q` fell from 10 to 4 *because the exposure column changed* |

---

## 14. Ladder position after this level

| Concept | Tier to demand |
|---|---|
| "one regression per period, one number per factor per period" | **5 (rebuild)** — unprompted, on a dataset shape they have never seen |
| the factor-return series, and its mean and variance | 4 (defend), including why the denominator is `T − 1` |
| cross-sectional vs time-series: which index is fixed | **5 (rebuild)** — this is the level's gate |
| why BFRE chose cross-sectional | 4 (defend) — with the paper's own words, not adjectives |
| what the choice costs | 4 (defend) — with at least three numbers, not "measurement error" as a phrase |
| the noise floor in `f̂` | 3 (derive) is enough; the independence assumption must be named |
| pooling, and why it is not the same | 3 (derive) |
| annualisation and its assumption | 2 (compute) is acceptable this level |

Do not mark Level 7 complete until the player, handed a fresh panel of returns and
characteristics with no instructions, **says how many regressions they are about to run and
what each row of the answer means — before touching a number.**

---

# 15. BOSS ROUND — why cross-sectional, and what it costs

Round type: **E. INTERROGATION.** Play a Chief Risk Officer with thirty years on the desk who
has bought three time-series risk models and is not impressed.

**The rulebook's pass condition has two halves and both are mandatory.** A player who can only
praise the choice has not understood it. A player who can only attack it has not understood it
either. Demand both, each with numbers from the file or pages from the paper.

## 15.1 The setup, as the player receives it

> *"Every risk model I have ever bought estimates a beta per stock from that stock's own return
> history. You are telling me you throw that away and instead run one regression per day across
> the whole market. Convince me — and then tell me what it costs me, because nothing is free."*

## 15.2 THE CASE FOR — every claim a page or a number

| Argument | The evidence |
|---|---|
| **1. It is what the paper does, stated plainly.** | **p.24**: estimation is *"a series of **cross-sectional** regressions of asset returns against asset factor exposures, which provides estimates of factor returns and asset specific returns."* **p.3**, the executive summary: model estimation is performed in cross-section, *"in two-passes"* (the hyphenation is the source's). |
| **2. Exposures are observed, so they update when the company changes.** | **p.2**: a returns-only forecast *"can quickly become misleading if a company undergoes changes in its operating activities, or is subject to corporate actions, or experiences changes to its capital structure"*; a fundamental model reflects these *"immediately"*, a returns-only model *"only gradually"*. |
| **3. A new listing has exposures on day one and no history at all.** | **p.42**: (1.12) needs *"5 years of weekly observations"* — 260 of them. An IPO has none. Its balance sheet exists the morning it lists. **INFER on the consequence**; the sample size is the paper's. |
| **4. The exposures genuinely move, and this design tracks them.** | Our file: DLT goes `+2, +2, +1, −1, +1` — a sign change. The paper's own version, **p.17**: *"In contrast to most style factors in BFRE, the reversal and momentum factor exposures of a security **can vary considerably through time**"*, and *"Reversal and momentum clearly exhibit the **least persistence** relative to other styles, which reflects the highly time-varying nature of these factor exposures."* Figure 1.11 (p.17) is that measurement — and `notes/` records `[UNREADABLE]` for which plotted trace is which style, so quote the sentence, never a trace. |
| **5. A time-series beta on a moving exposure returns the wrong number, and can return the wrong sign.** | Section 9: AXL's slope is **+0.75** against exposures that were never positive. Even the two-column version, `−35/23 = −1.521739` (rounded), is one number for a quantity that took two values. |
| **6. Structure buys you a small problem instead of a huge one.** | **p.2**: BFRE *"imposes far more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of factors, which capture the most important sources of asset return commonality"* — positioned against **STORM**, which the paper calls *"an alternative and entirely complementary methodology"*, not a thing to replace. **Careful with the citation:** the description of STORM as an asset-by-asset covariance matrix built from asset returns alone, each asset effectively its own factor, is `notes/`'s **gloss**, not a printed quotation. The quotable clause is the "imposes far more structure" one. |
| **7. A cross-section is wide, so each period's answer is well determined.** | Our five stocks give `df = 3` per month and a `t` of 4.39. BFRE's cross-sections are the whole Estimation Universe. Compare Section 9c's time-series fit: `df = 2` and `VIF = 6.260870` (rounded). |

## 15.3 THE CASE FOR WHAT IT COSTS — every claim a page or a number

| Cost | The evidence |
|---|---|
| **1. Every exposure is measured with error, every single period, and the error goes straight into `f_t`.** | This is the price of measuring five hundred trees in one afternoon. Section 8 puts a number on the consequence: **18.67% (rounded)** of the value row's variance is estimation noise, against **3.04% (rounded)** for the market row. The correction is **ours** — the paper contains nothing on it. |
| **2. Some exposures move *with the price*, which is the thing being forecast.** | The paper's own exhibit, **p.13**: AOL's market-capitalisation exposure *"is significantly positive at the beginning of the period, and increases substantially during 1998-9 following strong price performance"* — and *"A measure of size based on market capitalisation alone would confer large-size status on AOL, and **reduce its risk forecast accordingly**."* Figure 1.6's levels are `[APPROX — pixel-measured against warped gridlines]`; the sentence is printed. Direction: **too low, on the name where it hurt.** |
| **3. This month's precision is a property of this month's cross-section, and nobody controls it.** | M4 against M5: identical `f_Val = 1` and identical `σ̂² = 5/3`; `Q = 4` versus `10`; `t = 1.549193` versus `2.449490` (both rounded). One month clears BFRE's own `\|t\| > 2` bar (**p.8**) and the other does not, **for no reason connected to the factor**. |
| **4. Every month is then treated as one equal observation of the factor.** | Section 6b weights M4 and M5 equally in the mean and the variance, although M4's estimate is `5/2` times as wobbly. **GAP:** the paper says nothing about weighting factor-return observations by their precision; **p.27** describes exponential decay by *age*, not by precision. |
| **5. You need identifying restrictions that a time-series model never needs.** | **p.26**: market, industry and country are all columns of ones for every asset, so the specification *"is not uniquely identified as there are an infinite number of possible solutions"* until (1.10) is imposed by hand. And the fix changes meanings: *"the industry and country factors are **net of** the market factor return, which impacts their interpretation."* Level 2's lesson, now a running cost. |
| **6. The exposures are refreshed weekly while the regression runs daily.** | **p.24**: *"These regressions are performed **daily** for country and regional models and **weekly** for the World model."* **p.36**: *"The model universes, **factor exposures**, specific risk and specific return correlations are updated on a **weekly basis on Thursday** to incorporate the data as of previous Wednesday market close."* **INFER, and say so**: it follows that roughly five consecutive daily cross-sections are run against **the same** exposure matrix. So p.2's *"immediately"* is, operationally, *by next Thursday*. The paper never remarks on the gap. (`gm/CRITIQUE.md` **B-1** lists four frequencies for one horizon; this is a fifth, and it belongs there.) |
| **7. The World model is coarser for no stated reason.** | **p.24**, again: weekly for the World model. `notes/` records explicitly that **no justification is given**. Its factor returns are a coarser row feeding the same downstream machinery. |
| **8. You still cannot answer "how sensitive is this stock?" from a cross-section.** | The cross-section answers *what did this characteristic pay this month*. To get a sensitivity you must run a time-series regression — which BFRE does, once, at (1.12) on **p.42** — and then it enters as **an input substyle to Volatility** (p.42, p.44), never as the exposure mechanism. The player must be able to state that round trip. |

## 15.4 The trap the good players fall into — have this ready

A player defending the cross-sectional design will reach for the pooled regression as
"the same thing with more data":

```
pooled f_Val = 19/44 = 0.431818 (rounded)        vs   mean of the monthly f_Val = 1/2
pooled SSE   = 10507/44 = 238.795455 (rounded)   vs   Σ monthly SSE = 41/2 = 20.5
```

Both are correct arithmetic. The player must say which answers the question and why:

- The pooled number is a **`Q`-weighted** average of the monthly numbers, `Σ Q_t f_t / Σ Q_t`,
  and nobody chose that weighting — it is whatever the exposure spreads happened to be
  (M4 gets `1/11`, not `1/5`).
- Worse, the pooled fit has **no row to hand to Level 8 at all**. It produces one number where
  the risk model needs a series. The `9605/44 = 218.295455` (rounded) of extra miss is not
  waste; it *is* the timeline, reclassified as noise.

A player who offers the pooled estimate as "the cross-sectional answer with more power" has
failed the level regardless of anything else they said.

## 15.5 The interrogation script — real objections, escalating

1. *"Betas are estimated from returns. Everyone knows that. Why are you different?"*
   → wants 15.2.2 (p.2, "immediately" vs "only gradually") **and** 15.2.4 (p.17, exposures
   move). Either alone is half an answer.
2. *"Fine. But your 'exposure' is a number some analyst typed in. Mine comes out of market
   data. Whose is more reliable?"*
   → wants 15.3.1 and 15.3.2. The player must **concede** the point and then produce **p.13**
   — the paper's own exhibit against itself — plus the paper's mitigation (several substyles
   from balance sheet, market data and analyst estimates, not one price-driven measure).
   A player who defends exposure quality without conceding has hand-waved. Dock bps.
3. *"You said your model updates immediately. How often does it actually update?"*
   → 15.3.6. Daily regressions (p.24), weekly exposures (p.36). If the player says "daily"
   without qualification they have accepted marketing over the document.
4. *"Show me one number. How wrong does a time-series beta actually get?"*
   → Section 9. **+0.75 on a stock that was never positive**, decomposed into `+11/4`,
   `−15/8` and `−1/8`. If they cannot produce the decomposition, they have memorised an
   anecdote.
5. *"So run it monthly and average. That's your whole model — an average of five numbers."*
   → wants Section 6c: the mean's own `t` is `1.118034` (rounded) on five months. The player
   must say that BFRE does not judge on five months, and cite the actual criterion — the
   **proportion of significant t-statistics**, **p.14**'s 10% and **p.32**'s history — not
   invent one.
6. *"Your factor's risk. You computed 1. Is it 1?"*
   → Section 8. `61/75 = 0.813333` (rounded) after removing the noise floor, **and** the
   admission that the correction is ours, that the paper does not make it, and that the
   independence assumption behind it is not proved here.
7. *"Which of your five months is the model about?"*
   → The horizon answer, **p.30**: *"The forecast horizon of the model is **1-month**"*, and
   *"Style and industry factors are **selected by assessing explanatory power using monthly
   cross-sectional regressions**"*. A player who calls the mismatch of frequencies "circular"
   has taken a cheap shot (`gm/CRITIQUE.md` **CS-8**) — p.30 states the organising principle
   openly. The admissible version is the *fifth* frequency in 15.3.6.

## 15.6 Pass conditions

Deny promotion unless **all** of these happen:

- [ ] The player states the shape unprompted: **one regression per period, `n` stocks per
      regression, one number per factor per period**, and can say what is *not* carried across
      the join.
- [ ] Both halves argued — for and cost — each with **at least three** items from Section 15.2
      and Section 15.3 respectively, and each item attached to a number or a page.
- [ ] The AXL sign flip is produced **and explained**, not just quoted: the three channels,
      `+11/4`, `−15/8`, `−1/8`.
- [ ] The pooled trap is identified and disarmed (15.4).
- [ ] The player concedes the exposure-measurement cost **without being pushed**, and produces
      p.13 as the paper's own exhibit.
- [ ] The player separates **PAPER** from **INFER** correctly at least once, unprompted — the
      obvious candidates being the weekly-exposure consequence (15.3.6) and the noise floor
      (Section 8).
- [ ] The player says, in some form: *the cross-section answers what a characteristic paid
      today; a time series answers how one asset has behaved. BFRE uses the first for factor
      returns and the second only to manufacture a column.*

---

## 16. What this level does NOT settle

- **What to do with the row.** Building anything out of two rows at once is Level 8. This
  level stops at the diagonal — a variance per factor — and hands over the cross-term `11/4`
  without using it.
- **Whether the noise floor correction is the right one.** Section 8 assumes the estimation
  errors are unrelated across months and unrelated to the truth. Neither is proved here, and
  the second is doubtful whenever an exposure is stale or price-driven. **IOU.**
- **Why the variance of a sum of independent things is the sum of the variances.** Used in
  Section 8, not built. **IOU.**
- **Why annualising multiplies variance by 12.** Convention, and the same independence
  assumption. Section 6f shows the paper's own autocorrelations arguing against it. **IOU.**
- **Whether a factor's mean return should be in a risk model at all.** Level 6 raised it; this
  level computes a mean and does not defend it. A risk model is paid for the *spread* of the
  row, not its level.
- **Serial correlation in the row.** We compute one autocorrelation and stop. **p.3** says
  the covariance matrices are built *"correcting for serial correlations"* and **p.27** defers
  the whole method to a separate BRS document. The correction itself is not built anywhere in
  this game.
- **What the residuals of these five regressions are for.** They are `u` in (1.7), and they
  are Level 9's entire subject. This level uses them only to make `σ̂²`.

---

## 17. Back to BFRE — what this machinery does in the real model

### 17a. p.24 — the design sentence, quoted

Under the heading that introduces the estimation, the paper describes the estimation phase as

> *"a series of **cross-sectional** regressions of asset returns against asset factor exposures,
> which provides estimates of factor returns and asset specific returns."*

Read the sentence slowly against Section 5. *A series* — Section 5's five rows. *Of
cross-sectional regressions* — Section 4's shape, one date at a time. *Which provides estimates
of factor returns* — the row in Section 6. *And asset specific returns* — the residual columns,
which Level 9 will take.

**The whole of Level 7 is one sentence on page 24.** The rest of this page is the arithmetic
underneath it.

### 17b. p.24, p.3, p.36 — the cadence, and the fifth frequency

**PAPER, p.24:**

> *"These regressions are performed **daily** for country and regional models and **weekly** for
> the World model."*

`notes/` records explicitly that **no justification is given for the weekly choice**.

**PAPER, p.36**, on the operational schedule:

> *"The model universes, **factor exposures**, specific risk and specific return correlations are
> updated on a **weekly basis on Thursday** to incorporate the data as of previous Wednesday
> market close."*

**PAPER (in substance), p.3**, the executive summary's update-cadence bullet: monthly updates
to the estimation universes, weekly updates to factor exposures and specific risk forecasts,
daily updates to coverage universes and factor covariance matrices, and daily factor returns
for all models **from March 1996 onwards**. *(The wording here is `notes/`'s summary of the
printed bullet; the verbatim sentence for the weekly exposure update is the p.36 one above.)*

**INFER — the consequence, and it is ours:** run the regression daily and refresh `X` on
Thursdays and the same exposure matrix serves roughly five consecutive cross-sections. Within
a week, `X` is a constant and only `r` moves. That does not make the design a time-series
model — the columns are still observed characteristics, not fitted slopes — but it does mean
p.2's *"immediately"* is bounded below by a week. The paper never puts these two sentences
side by side.

### 17c. p.10 — Table 1.2 is this level's output, summarised

Every column of Table 1.2 is an operation on the row Section 6 produced:

| Table 1.2 column | The operation | Ours |
|---|---|---|
| Annualised Return | mean of the row, annualised | `f_Mkt` **12%**, `f_Val` **6%** |
| Annualised Volatility | spread of the row, annualised | variance **108** and **12**; roots `10.392305` and `3.464102` (both rounded) |
| Sharpe Ratio | the ratio of the two | `√(4/3) = 1.154701` and `√3 = 1.732051` (both rounded) |
| Correlation with Market Factor | the cross-term, Section 6d | `11/12 = 0.916667` (rounded) — **Level 8's object** |
| First-Order Autocorrelation | Section 6f | `−5/36` and `−3/16` |

Printed values, for calibration only, verified digit-for-digit in `notes/`: Market
**7.0% / 19.8% / 0.35 / 1.00 / 0.00**; Value **3.3% / 2.3% / 1.43 / 0.03 / 0.14**; Momentum's
autocorrelation **0.22**; Reversal's **0.17**.

**Two GAPs on this table, both real:** the paper never states its annualisation convention, and
never defines "Sharpe Ratio" — no formula, no risk-free rate named. And a warning carried
forward from Level 1: **do not derive one printed column from another**. Return and volatility
are each rounded to one decimal before the Sharpe column is printed, so three of the thirteen
rows do not reproduce (Profitability 3.1/2.2 = **1.41** *(rounded)* against a printed **1.37**).

### 17d. p.14, p.18, p.20 — the plots are the running sums

Figure 1.7 (**p.14**, NAMR Size against a negated Fama-French SMB), Figure 1.12 (**p.18**, EMEA
momentum) and Figure 1.14 (**p.20**, NAMR Value against Fama-French HML) are cumulative
performance charts. **They are Section 6e's operation, run on nearly eighteen years
(Mar 1996 – Dec 2013) instead of five months.** The paper's two printed correlations between its own factor and the academic
counterpart — **0.67** for size (p.13) and **0.45** for value (p.20) — are correlations between
two *rows* of the kind Section 6 builds.

All plotted *levels* in those figures are `[APPROX — measured off the scan; the paper prints no
data labels on any chart]`. The correlations 0.67 and 0.45 are printed text and may be quoted
as figures.

### 17e. p.14 fn 11, p.16 fn 12, p.30, p.32 — the row is what selects the factors

The paper's entire factor-selection apparatus runs on the column of monthly t-statistics that
Section 7 produces:

- **p.14, footnote 11** and **p.16, footnote 12**, identical: *"t-statistics are based on
  **monthly cross-sectional regressions**."*
- **p.30**: *"Style and industry factors are **selected by assessing explanatory power using
  monthly cross-sectional regressions**"*, under the stated organising principle *"The forecast
  horizon of the model is **1-month**."*
- **p.14**: the 10% bar. **p.32**: the proportion, over different periods, as *"a good proxy for
  the persistence of individual factor effects."*
- **p.8**: `|t| > 2`, and the average squared t-statistic.

So the chain is: Level 7 produces a row of `f` and a row of `t` → the proportion of significant
months decides which factors exist → the surviving factors are the columns of `X` → and `X` and
the row of `f` are the two inputs to (1.7) and (1.8) on **p.24**.

### 17f. p.42 — the one time-series regression, and what it is for

Equation **(1.12)**, Historical Beta: weekly excess returns, five years, exponentially weighted
with a **52-week half-life**, against the cap-weighted Estimation Universe. Its slope becomes
the **Historical Beta** substyle and its intercept becomes the **Historical Alpha** substyle
(**p.44**); the equally-weighted standard deviation of its residuals becomes **Historical
Sigma** (p.42).

**Every one of those is a column of `X`.** Not one of them is a factor return. The rival design
is present inside BFRE — as a supplier of characteristics, on the input side of the very
regression this level runs.

Say the round trip out loud, because it is the sentence that proves the level landed:

> *A time-series regression on one stock makes a number. That number is standardised (p.10) and
> becomes one column of `X`. Then a cross-sectional regression across all stocks, on that `X`,
> makes the factor returns. The time series feeds the cross-section; it never replaces it.*

### 17g. Where the machinery ends up in the finished model

1. Each period, a cross-sectional regression (**p.24**) produces one `f` per factor and one
   residual per asset.
2. Repeat daily for country and regional models, weekly for the World model (**p.24**), from
   **March 1996** (**p.3**).
3. The rows of `f` are the input to the covariance machinery — **p.27**, default **WKL**,
   **104 weeks** with a **26-week half-life**. That is **Level 8**.
4. The residual columns are the input to the specific-risk machinery — **p.27**, **p.28**. That
   is **Level 9**.
5. Both meet in **(1.8)**, **p.24**: `Σ = X F Xᵀ + Δ`. That is **Level 10**.

**Every number in the finished risk model traces back through this level.** A factor return
mis-estimated in one month is one bad entry in the row; a factor return mis-estimated
*systematically* — because an exposure column is stale, or price-driven, or squashed the way
M4's was — is a bias in everything built on the row.

### 17h. What `notes/` does NOT support — searched across all 65 transcribed pages

- **No number of assets is ever given for any cross-sectional regression.** So the `n`, the `k`
  and the `df` behind every t-statistic the paper reports cannot be reconstructed. (Carried
  forward from Level 6; it is a Level 7 problem too, because the row's precision depends on it.)
- **No standard error is ever reported for any factor return.** The row is printed; its
  uncertainty is not. The one confidence interval anywhere in the paper is p.38's 95% band on a
  *bias statistic*, which is a different object.
- **Nothing on estimation error in `f̂` inflating the variance of the factor-return series.**
  Section 8's correction is entirely ours.
- **No annualisation convention, and no definition of "Sharpe Ratio".**
- **No statement of whether "cumulative returns" means a sum or a compounded product.**
- **The words "panel" and "pooled regression" never appear.** Neither does **"Fama–MacBeth"** —
  not in the text and not in the bibliography (27 entries, counted from the printed rows on
  p.65; the page prints no total). Fama and French appear only
  as the source of the **SMB** and **HML** comparison series (p.13, p.14, p.20).
- **The word "stationarity" never appears**, although p.17's finding that reversal and momentum
  exposures *"can vary considerably through time"* is precisely a statement that the assumption
  a time-series beta needs is false for two of BFRE's own factors.
- **No justification for the World model's weekly estimation** (p.24) — `notes/` records the
  absence explicitly.
- **No weighting of factor-return observations by their precision.** p.27's exponential decay
  weights by **age**. Nothing weights by `Q_t`, and nothing acknowledges that `Q_t` varies.

So: the paper states the design in one sentence and prints the finished row in Table 1.2, and
between those two things it shows **none** of the arithmetic — not a sample size, not a standard
error, not a convention. That is the third level running in which the paper reports a verdict
and withholds the trial, and by now the player should notice it without being told.

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level7.py     # 238 exact-rational assertions, exits 0
```

The script rebuilds every figure on this page from the raw `x` and `r` tables in
`fractions.Fraction`, using the same exact Gaussian-elimination and weighted-least-squares
helpers as `tools/verify_level5.py`: the five exposure columns and their sums, `Q_t` and
`ΣQ = 44`; all five cross-sectional regressions solved from the 2×2 Gram matrix, with both
balance conditions checked in every month; the diagonal Gram matrix and its `VIF = 1`; the
factor-return rows, their means, their `T − 1` variances (both exact squares), their population
variances, the standard error and `t` of each row's mean, the cross-term `11`, the cumulative
sums, the annualisation and both autocorrelations; the per-month `σ̂²`, `Var(f)` and `t²` for
both factors, the M4-against-M5 identity `t²₅/t²₄ = Q₅/Q₄ = 5/2`, the proportion of significant
months and the average squared t-statistic; the noise floors `14/75` and `41/150` and the
corrected variances; AXL's time-series slope by two routes, its exact three-channel
decomposition into `+11`, `−15/2` and `−1/2`, the two-column time-series solve `19/23` and
`−35/23` with its determinant, overlap and VIF, DLT's slope `33/8`, and the (1.12)-shaped
market slope `13/36`; the pooled regression, its `Q`-weighted-average identity, and the exact
decomposition `20.5 + 180 + 1685/44 = 10507/44`; and the √-cap-weighted month with both
weighted balance conditions at zero.

If any printed value ever disagrees with this markdown, the markdown is wrong.
