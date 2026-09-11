# ★ THE REBUILD — the final exam

Every number below is recomputed in exact rational arithmetic by `tools/verify_rebuild.py`
(**676 assertions, exits 0**). Nothing here is rounded by hand. Where a decimal does not
terminate it is written with the word **rounded** next to it; every other decimal on this
page is exact.

> **This is the win condition, and there is no boss round after it.** `prompt/RISK_DESK.md`
> §5 gives Level ★ one line — *"Everything, from blank"* — and §3 makes Victory Condition 4
> the same sentence: *given only a spreadsheet of stock returns and characteristics, the
> player can construct `X`, estimate factor returns, build `F`, build `D`, assemble
> `V = X F Xᵀ + D`, and compute a portfolio's risk, alone, with no reference material.*
> Sections 2–9 are that rebuild, done correctly. Section 11 marks it. Section 12 diagnoses
> the wrong answers. Section 13 turns all four victory conditions into things you can
> watch happen rather than things you feel about.

> **Difficulty, stated honestly, because the rulebook demands it (`RISK_DESK.md` §8).**
>
> - **Nothing in the eight stages is graduate-level.** Every step is arithmetic the player
>   has done before, on a file they have not seen. The exam is long, not deep. Budget
>   **90 to 150 minutes**; a few hundred multiplications, and two square roots that
>   both come out exact.
> - **Three things that a professional would do here are deliberately absent**, and the
>   player must be able to *name* them, not perform them: the √-market-cap regression
>   weighting (**PAPER, p.25**), the exponential decay with a half-life (**PAPER, p.27**),
>   and the Newey–West serial-correlation adjustment (**PAPER, p.27–28**). Section 14 says
>   why each is out of scope and what each would change.
> - **Eigen-decomposition, shrinkage and Newey–West are graduate-level** and appear nowhere
>   in the eight stages. Two of the three appear nowhere in the paper either:
>   `gm/VOCAB.md` §6 records that *eigenvalue* has **zero** occurrences in 65 pages, and
>   `gm/LEVEL_ANCHORS.md` §11 records that BFRE's only shrinkage is the p.36 Bayesian prior
>   on thin country/industry **returns**, never on `F`.
> - **The hardest part of this level is not arithmetic.** It is Section 11's rule that a
>   right final number with a wrong intermediate object is a **fail**. Section 12.2 proves
>   why that rule has to exist: there is a wrong path on this very file that reaches
>   **exactly 4.5000** and is still wrong.

---

## 0. How to run this level

### 0a. The rules of the exam

| | |
|---|---|
| **Materials allowed** | Blank paper. A calculator for square roots only — every other step is exact and must be shown as a fraction. |
| **Materials forbidden** | Every earlier level's file, every formula sheet, the paper itself, and these notes. The player writes `b = Σxr/Σx²` from memory or does not write it. |
| **Time** | One sitting. If the player asks to break between stages, allow it and record where. |
| **The GM's job during the exam** | Say nothing. Do not confirm intermediate answers. Do not react to a wrong turn. The whole value of this level is that the player finds their own error using the checks in Section 10. |
| **The one exception** | If the player is stuck for more than ten minutes on *what to do next* — not on arithmetic — give them the stage heading only ("you are on `F` now"), and record that you gave it. A player who needed three stage headings has not passed Victory Condition 4. |

### 0b. What the player is already holding

This level introduces no machinery. Every line of it is a tool the player built and was
paid for. The callbacks are the level.

| From | What comes back, and where it is used here |
|---|---|
| **Level 0** | The miss `u`, scored by its size, not its sign. Every `Σu²` in Stage 4. |
| **Level 1** | `b = Σxr/Σx²`, derived by nudging. Stage 2's market column, where it collapses to `Σr/6`. |
| **Level 2** | The balance condition `Σx·u = 0`, one per column, forced by the arithmetic. **Fifteen** of them get checked in Stage 2 — three per month, five months. |
| **Level 3** | Two columns need two balance conditions solved *together*. Stage 2's 2×2 system, and the `/10` in its answer. |
| **Level 4** | A coefficient is a leftover; `det = AC − B²`; the variance inflation factor. Stage 1 measures the collision (**ρ = 2/3**, VIF **1.8**); Stage 2 is where a player who forgot Level 4 loses the exam. |
| **Level 5** | Centering; a column of ones is an intercept; standardisation. The whole of Stage 1, and the reason `Σ1·x = 0` makes Stage 2 fast. |
| **Level 6** | `n − k`; leverage `h_i`; why a denominator is what it is. Stage 4's divisor argument, and Section 5f's `Σh = k = 3`. |
| **Level 7** | The same cross-section, month after month, producing a *row* of factor returns. Stage 2 run five times. |
| **Level 8** | `F` — covariance of factor returns, divisor `T − 1`. Stage 3. Also `det F ≠ 0`, Level 4's test aimed at a new target. |
| **Level 9** | `D` — each stock's private wobble; what least squares **guarantees** versus what BFRE **assumes**. Stage 4, and Section 14. |
| **Level 10** | `V = X F Xᵀ + D`; variances add, risks do not; the two routes to one number. Stages 5 and 6. |
| **Level 11** | Marginal contribution; exposure is not contribution. Stage 8. |
| **Level 12** | Five months is not evidence. Section 14, and the last question in Section 13. |

### 0c. Names

**Nothing unlocks at this level.** `gm/VOCAB.md` §1 puts the last of the sixteen terms
(*in-sample / out-of-sample*) at Level 12. What this level does instead is **demand all
sixteen**, unprompted, in the player's own commentary while they work. Section 13 turns
that into a tally sheet, because *"the player used the right words"* is exactly the kind of
vibe Victory Condition 2 is supposed to stop being.

### 0d. The three simplifications, declared before the player starts

Say these out loud at the start. They are not hidden, they are not tricks, and the player
is expected to be able to name all three back at the end (Section 13, VC2 check 3).

1. **Equal weights in the regression.** BFRE weights each asset by **√ market
   capitalisation** — **PAPER, p.25**: *"Assets are weighted in the regression using
   square-root of market capitalisation."* This file has no market caps and weights every
   asset equally. Levels 7 §11 and 8 §3a made the same declaration.
2. **Exposures frozen for five months.** BFRE re-standardises exposures as the data
   arrives. Here `X` is computed once from one snapshot of the characteristics and reused
   in all five months, which is what makes the Gram matrix a one-off (Section 3).
3. **Monthly units, no annualisation until asked.** Everything is in percent and
   percent-squared **per month**. BFRE's forecast horizon is **1 month** (**PAPER, p.30**),
   so monthly is the right unit; any `×√12` on this page is ours and is flagged where it
   occurs.

---

## 1. THE FILE — hand this over verbatim

### 1a. The spreadsheet

> **NORTHGATE RISK — MODEL BUILD 1, ESTIMATION UNIVERSE**
>
> Six stocks. Two characteristics, measured at the start of the window. Five months of
> returns in excess of the risk-free rate, in percent.
>
> | Stock | Earnings yield (%) | Operating margin (%) | M1 | M2 | M3 | M4 | M5 |
> |---|---:|---:|---:|---:|---:|---:|---:|
> | GRV | 8 | 12 | +8.5 | +3.5 | +3.5 | +2.5 | −4.5 |
> | HLX | 7 | 12 | +13.5 | +4.0 | +7.5 | −1.5 | −1.5 |
> | JDR | 5 | 12 | +11.5 | −3.0 | +1.5 | +0.5 | +2.5 |
> | KPN | 4 | 13 | +7.0 | +1.5 | +1.0 | +3.0 | 0.0 |
> | LTS | 4 | 10 | +3.5 | −10.5 | +2.5 | −4.5 | −3.5 |
> | MRA | 2 | 7 | −2.0 | −13.5 | +2.0 | −6.0 | +1.0 |
>
> **The book** (Kestrel Fund, % of NAV, fully invested):
> GRV **30%**, HLX **40%**, KPN **15%**, MRA **15%**.
>
> **The benchmark** (the NG-6 index, % weights, published by the index provider):
> GRV **25%**, HLX **10%**, JDR **25%**, KPN **15%**, LTS **10%**, MRA **15%**.

That is the whole file: 12 characteristic values, 30 returns, 4 holdings, 6 index weights.
Nothing else exists. No market caps, no industries, no countries, no risk-free rate — the
returns are already in excess of it.

**Nothing in this file appears in Levels 0–12.** Those levels ran on AXL, BRN, CHR, DLT,
EMK and FNX; this one runs on GRV, HLX, JDR, KPN, LTS, MRA. The returns, the exposures,
`F`, `D` and every risk number below are new.

### 1b. The task sheet

> 1. **Build `X`.** Turn the two characteristics into factor exposures. Say what the third
>    column is and why it is there.
> 2. **Estimate the factor returns.** One number per factor per month. Five months.
> 3. **Build `F`.**
> 4. **Build `D`.**
> 5. **Assemble `V`.**
> 6. **Price the book.** One number, in percent per month. Do it twice, by two different
>    routes, and show that they agree.
> 7. **Price the book against the benchmark.** One number.
> 8. **Say where that second number comes from**, position by position, in percentages that
>    sum to 100.
>
> At every stage, state the check you ran on your own work before moving on.

### 1c. What the player should be told about the answer

Nothing. In particular do not tell them that both risk numbers come out exact —
finding that out is one of the pleasures of the level, and *expecting* a round number is a
way to get the wrong one.

---

## 2. STAGE 1 — BUILD `X`

### 2a. The move, and its page

**PAPER, p.10**, the rule, quoted in full because the whole stage is in it:

> *"The mean is defined as the square-root of market capitalisation weighted average value
> so that the transformed substyles (and styles) have the property that their weighted
> average is zero. Additionally, these values are divided by their equally-weighted
> standard deviation so that a value of +1 … is one standard deviation above the market
> average. An exposure of zero indicates that a security has the market average value."*

And **PAPER, p.39**: exposures *"take values between +/- 3 and are standardised to a
square-root capitalisation mean of zero, with an equal-weighted standard deviation of
one."*

Ours uses the equal-weighted mean as well as the equal-weighted standard deviation —
simplification 1 of Section 0d.

### 2b. The Earnings Yield column

```
raw               8      7      5      4      4      2        Σ = 30
mean              30/6 = 5
deviations       +3     +2      0     −1     −1     −3        Σ = 0
squared            9      4      0      1      1      9        Σ = 24
variance          24/6 = 4
standard deviation  √4 = 2        ← exact
exposures        +3/2   +1      0   −1/2   −1/2   −3/2
```

### 2c. The Profitability column

```
raw              12     12     12     13     10      7        Σ = 66
mean              66/6 = 11
deviations       +1     +1     +1     +2     −1     −4        Σ = 0
squared            1      1      1      4      1     16        Σ = 24
variance          24/6 = 4
standard deviation  √4 = 2        ← exact
exposures        +1/2   +1/2   +1/2   +1     −1/2   −2
```

### 2d. `X`

```
        ┌                      ┐
        │  1    +3/2    +1/2   │   GRV
        │  1    +1      +1/2   │   HLX
  X  =  │  1     0      +1/2   │   JDR     6 rows (assets) x 3 columns (factors)
        │  1    −1/2    +1     │   KPN
        │  1    −1/2    −1/2   │   LTS
        │  1    −3/2    −2     │   MRA
        └                      ┘
```

**The third column is the first one.** A column of ones is the market factor. **PAPER,
p.4:** *"all equity assets have a unit exposure to this factor."* **PAPER, p.26:** *"for
each asset, there exist three intercept terms – the market factor, an industry factor, and
a country factor. Every asset has unit exposure to these three factors."* This file has no
industries and no countries, so it carries exactly one intercept and needs none of
equation (1.10)'s identifying restrictions — which is *why* it is solvable by hand and
why Section 14 has to say so out loud.

### 2e. The five sums that decide how hard Stage 2 is

```
Σ1·x = 0        Σ1·g = 0        ← because both columns were centred (Level 5)
Σx²  = 6        Σg²  = 6        ← because both were divided by their own sd
Σx·g = 4
```

`Σx² = 6 = n` is not a coincidence and the player should say so unprompted: dividing by the
equal-weighted standard deviation forces `Σz² = n` for any column, every time. It is the
**cheapest check in the whole exam** (Section 11, Stage 1).

```
              ┌              ┐
              │  6    0   0  │
  XᵀX    =    │  0    6   4  │       det(2×2 style block) = 6·6 − 4·4 = 20
              │  0    4   6  │       det(XᵀX)             = 6 · 20   = 120
              └              ┘
```

### 2f. The collision, measured before it does any damage

The two style columns are correlated: `4/6 = 2/3 = 0.6667` **rounded**. Level 4's diagnostic:

```
VIF = 1/(1 − ρ²) = 1/(1 − 4/9) = 9/5 = 1.8
```

**PAPER, p.11, Figure 1.3**, printed digits — one of only four exhibits in the paper that
prints its values: in the live NAMR model the **Earnings Yield–Profitability** exposure
correlation is **0.64**. Our 0.6667 is that collision, very nearly to the digit. This is
the one place where the toy is not a toy: cheap stocks really are also the ones whose
margins are thin, and the paper's own matrix says so.

**A VIF of 1.8 is mild.** It does not break anything. What it does is make the
one-at-a-time answer wrong by a factor of two in Stage 2 — which is the point.

---

## 3. STAGE 2 — THE FACTOR RETURNS

### 3a. Why this is one solve, not three, and why it is still fast

**PAPER, p.24:** estimation is *"a series of cross-sectional regressions of asset returns
against asset factor exposures, which provides estimates of factor returns and asset
specific returns."*

Three columns means three balance conditions at once (Level 3):

```
Σu = 0            Σx·u = 0            Σg·u = 0
```

Written as the normal equations with the Gram matrix of Section 2e:

```
┌           ┐ ┌       ┐   ┌      ┐
│ 6   0   0 │ │ f_Mkt │   │  Σr  │
│ 0   6   4 │ │ f_EY  │ = │ Σx·r │
│ 0   4   6 │ │ f_Prf │   │ Σg·r │
└           ┘ └       ┘   └      ┘
```

The first row is detached from the other two because `Σ1·x = Σ1·g = 0`. So:

```
f_Mkt = Σr / 6                       ← Level 1's formula on a column of ones
```

**INFER, and say so at the table.** That line is the Level-1 result the anchor map flags:
with a column of ones and centred style exposures, the market column's balance condition
collapses to *the average return*, which is exactly what **p.4 footnote 2** asserts
(*"Average return based on regression weights"*). The paper prints every ingredient and
never assembles them.

The remaining 2×2 has determinant `6·6 − 4·4 = 20`, so by Cramer's rule (Level 3):

```
f_EY   = (6·Σxr − 4·Σgr)/20 = (3·Σxr − 2·Σgr)/10
f_Prof = (6·Σgr − 4·Σxr)/20 = (3·Σgr − 2·Σxr)/10
```

**The exposures do not change from month to month**, so those three formulas are computed
**once** and applied five times. That is not an accident of the toy — for a fixed `X`, the
factor returns are a fixed recipe applied to whatever returns arrive.

### 3b. Five months, three sums each

| month | `Σr` | `Σx·r` | `Σg·r` | `f_Mkt = Σr/6` | `f_EY = (3Σxr−2Σgr)/10` | `f_Prof = (3Σgr−2Σxr)/10` |
|---|---:|---:|---:|---:|---:|---:|
| M1 | 42 | 24 | 26 | **+7** | (72−52)/10 = **+2** | (78−48)/10 = **+3** |
| M2 | −18 | 34 | 36 | **−3** | (102−72)/10 = **+3** | (108−68)/10 = **+4** |
| M3 | 18 | 8 | 2 | **+3** | (24−4)/10 = **+2** | (6−16)/10 = **−1** |
| M4 | −6 | 12 | 18 | **−1** | (36−36)/10 = **0** | (54−24)/10 = **+3** |
| M5 | −6 | −8 | −2 | **−1** | (−24+4)/10 = **−2** | (−6+16)/10 = **+1** |

Every one of those fifteen numbers is an integer. That is the file being kind, not the
method being kind; nothing in the method promises it.

### 3c. The misses, and the fifteen balances

`u = r − f_Mkt·1 − f_EY·x − f_Prof·g`, computed stock by stock:

| month | GRV | HLX | JDR | KPN | LTS | MRA | `Σu` | `Σx·u` | `Σg·u` | `Σu²` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M1 | −3 | +3 | +3 | −2 | −1 | 0 | **0** | **0** | **0** | 32 |
| M2 | 0 | +2 | −2 | +2 | −4 | +2 | **0** | **0** | **0** | 32 |
| M3 | −2 | +3 | −1 | 0 | 0 | 0 | **0** | **0** | **0** | 14 |
| M4 | +2 | −2 | 0 | +1 | −2 | +1 | **0** | **0** | **0** | 14 |
| M5 | −1 | +1 | +3 | −1 | −3 | +1 | **0** | **0** | **0** | 22 |

**Total `Σu²` over the five months = 114.** Hold on to that number; Section 5c spends it.

Worked example, M1, GRV: `r = +8.5`, exposures `(1, +1.5, +0.5)`, factor returns
`(+7, +2, +3)`. Fitted `= 7 + 2(1.5) + 3(0.5) = 7 + 3 + 1.5 = 11.5`. Miss
`= 8.5 − 11.5 = −3`. ✔

**Degrees of freedom per month: `n − k = 6 − 3 = 3`** (Level 6). Six misses, three of which
are determined by the other three through the three balance conditions above. Section 5f
shows what that costs.

### 3d. The wrong way, and exactly what it returns

The one-at-a-time answer — run Level 1's formula on each style column separately, ignoring
that the other column exists — is `Σxr/6` and `Σgr/6`:

| month | true `f_EY` | one-at-a-time | true `f_Prof` | one-at-a-time |
|---|---:|---:|---:|---:|
| M1 | +2 | **+4** | +3 | **13/3 = 4.3333** *(rounded)* |
| M2 | +3 | **17/3 = 5.6667** *(rounded)* | +4 | **+6** |
| M3 | +2 | **4/3 = 1.3333** *(rounded)* | −1 | **1/3 = 0.3333** *(rounded)* |
| M4 | 0 | **+2** | +3 | **+3** |
| M5 | −2 | **−4/3 = −1.3333** *(rounded)* | +1 | **−1/3 = −0.3333** *(rounded)* |

Three things to point at:

- **M1's Earnings Yield return is exactly double the truth.** Not noisy — double.
- **M5's Profitability return changes sign**, from `+1` to `−1/3`. The naive method reports
  that being profitable *lost* money in a month when it made money.
- **M4's Profitability return is right by accident.** The shortcut agrees with the truth
  exactly when `3·Σxr = 2·Σgr`, and in M4 both sides are **36**. That is the cruellest row:
  a player who spot-checks one number and finds agreement will conclude the shortcut is
  fine — while M4's *Earnings Yield* return, in the same month, is 2 against a true 0.

Section 12.1 carries this error all the way to the risk number.

---

## 4. STAGE 3 — BUILD `F`

**PAPER, p.24, equation (1.8):** `Σ = X F Xᵀ + Δ`, where `F` is the *"factor covariance
matrix"*.

### 4a. The three series, and their means

| | M1 | M2 | M3 | M4 | M5 | mean |
|---|---:|---:|---:|---:|---:|---:|
| `f_Mkt` | +7 | −3 | +3 | −1 | −1 | **+1** |
| `f_EY` | +2 | +3 | +2 | 0 | −2 | **+1** |
| `f_Prof` | +3 | +4 | −1 | +3 | +1 | **+2** |

Subtract each series' own mean — and note that they are **not the same mean**; `f_Prof`
averages +2 while the other two average +1. A player who subtracts one number from all
three series has made an error this file can catch.

| deviations | M1 | M2 | M3 | M4 | M5 |
|---|---:|---:|---:|---:|---:|
| `Mkt` | +6 | −4 | +2 | −2 | −2 |
| `EY` | +1 | +2 | +1 | −1 | −3 |
| `Prof` | +1 | +2 | −3 | +1 | −1 |

### 4b. Six cross-products, then one divisor

```
Σ dMkt·dMkt  = 36 + 16 + 4 + 4 + 4  = 64
Σ dEY ·dEY   =  1 +  4 + 1 + 1 + 9  = 16
Σ dPrf·dPrf  =  1 +  4 + 9 + 1 + 1  = 16
Σ dMkt·dEY   =  6 −  8 + 2 + 2 + 6  =  8
Σ dMkt·dPrf  =  6 −  8 − 6 − 2 + 2  = −8
Σ dEY ·dPrf  =  1 +  4 − 3 − 1 + 3  =  4
```

Divide every one by `T − 1 = 4`:

```
        ┌                 ┐
        │  16     2    −2 │   Mkt
  F  =  │   2     4     1 │   EY        percent-squared, per month
        │  −2     1     4 │   Prof
        └                 ┘
```

**Why `T − 1` and not `T`.** Level 6's rule: divide by the number of numbers minus the
number of parameters estimated *from those same numbers*. Each series' mean was estimated
from that series, so one degree of freedom is spent. Stage 4 does **not** spend one, and a
player who cannot say why the two stages use different divisors has not passed Section 13's
VC3 check.

### 4c. Reading `F` out loud

| | value | says |
|---|---:|---|
| `F₁₁ = 16` | vol `√16 = 4.0%` **exact** | the market factor's monthly wobble |
| `F₂₂ = 4` | vol `√4 = 2.0%` **exact** | Earnings Yield's |
| `F₃₃ = 4` | vol `√4 = 2.0%` **exact** | Profitability's |
| `F₁₂ = 2` | corr `2/(4·2) = +1/4` | cheap stocks do slightly better when the market rises |
| `F₁₃ = −2` | corr `−2/(4·2) = −1/4` | profitable stocks do slightly worse when the market rises |
| `F₂₃ = 1` | corr `1/(2·2) = +1/4` | the two style bets lean the same way |

**Level 4's test, aimed at `F` this time.** Leading minors `16`, `16·4 − 2² = 60`, and
`det F = 200`. All positive, so `F` is not singular and the three factors are not
collinear. A negative one would mean the arithmetic was wrong — no real covariance matrix
can have one.

**Against the real model, honestly.** **PAPER, p.10, Table 1.2** (printed digits): NAMR's
market factor has annualised volatility **19.8%**, Earnings Yield **2.1%**, Profitability
**2.2%**; the correlations of those two style factor returns with the market factor are
**0.02** and **−0.14**. Our toy has the market at 4%/month and the styles at 2%/month —
far too close together — and correlations of ±1/4 where the real ones are near zero.
That is a deliberate exaggeration so that the cross terms in Stage 6 do visible work. Say
so; do not let the player leave thinking style factors are half as volatile as the market.

---

## 5. STAGE 4 — BUILD `D`

**PAPER, p.24:** `Δ` is the *"specific risk matrix (a diagonal matrix of asset specific
risk forecasts)"* — under the lead-in *"In general a multi-factor model decomposes asset
returns as follows"*. Section 14 says what BFRE actually ships instead.

### 5a. Turn the miss table on its side

Stage 2's table was read across (one month, six stocks). `D` reads it down (one stock, five
months):

| Stock | M1 | M2 | M3 | M4 | M5 | `Σu²` | `d = Σu²/5` | specific vol |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| GRV | −3 | 0 | −2 | +2 | −1 | 18 | **18/5 = 3.6** | 1.8974 *(rounded)* |
| HLX | +3 | +2 | +3 | −2 | +1 | 27 | **27/5 = 5.4** | 2.3238 *(rounded)* |
| JDR | +3 | −2 | −1 | 0 | +3 | 23 | **23/5 = 4.6** | 2.1448 *(rounded)* |
| KPN | −2 | +2 | 0 | +1 | −1 | 10 | **2** | 1.4142 *(rounded)* |
| LTS | −1 | −4 | 0 | −2 | −3 | 30 | **6** | 2.4495 *(rounded)* |
| MRA | 0 | +2 | 0 | +1 | +1 | 6 | **6/5 = 1.2** | 1.0954 *(rounded)* |

```
  D = diag( 3.6,  5.4,  4.6,  2,  6,  1.2 )      percent-squared, per month
```

### 5b. The divisor, and the asymmetry with Stage 3

`D` divides by `T = 5` and subtracts **no** mean. `F` divided by `T − 1 = 4` and subtracted
a mean. The asymmetry is deliberate and the player must be able to defend it:

- For a factor series, the mean was **estimated from that series**, so it costs a degree of
  freedom.
- For a stock's own specific-return series, **no parameter was estimated from that series**.
  The model asserts the mean is zero.

*That reading is* **INFER**. What **PAPER, p.24** actually prints is: *"In a well-specified
model, the prescribed factors will capture all sources of commonality in asset returns
leaving only return associated with stock-specific events in the idiosyncratic component."*
It never writes `E[u] = 0`. The zero-mean reading follows from it; the paper does not state
it.

**And the assertion is visibly false on this file, which is the honest part.** Nothing
forces a stock's misses to average zero *through time* — the balance conditions run
**across stocks within one month**, never across months within one stock. The five sums:

```
GRV −4      HLX +7      JDR +3      KPN 0      LTS −10      MRA +4
```

LTS's five misses are `−1, −4, 0, −2, −3`: **every one of them negative**, averaging −2.
Five months of a name that did nothing but disappoint. The model books that as wobble, not
as a level, because it has been told the level is zero. With `T = 375` daily observations
(**PAPER, p.28, Table 1.3**) the distinction stops mattering; with `T = 5` it is a live
choice, and Section 14 prices it.

### 5c. The free cross-check — add the same thirty numbers twice

```
down the stocks:   18 + 27 + 23 + 10 + 30 +  6  = 114
across the months: 32 + 32 + 14 + 14 + 22       = 114      ✔
```

Two different orders of summation over the same thirty squares. If they disagree, at least
one miss is wrong and the player knows it **before** building anything on top. This is the
single cheapest error-catcher in the exam and the player should run it unprompted.

### 5d. The other two divisor conventions, for the record

| Convention | `d` for GRV…MRA |
|---|---|
| **used here** — divisor `T = 5`, mean asserted zero | **3.6, 5.4, 4.6, 2, 6, 1.2** |
| divisor `T − 1 = 4`, mean still asserted zero | 4.5, 6.75, 5.75, 2.5, 7.5, 1.5 |
| each stock's own mean removed, divisor `T − 1 = 4` | 3.7, 4.3, 5.3, 2.5, 2.5, 0.7 |

What each does to the final answers is in Section 12, traps T4 and T5. The assembly in
Stages 5–8 takes whatever `D` it is handed and does not care which convention produced it.

### 5e. Level 6's leverage, and a warning this file has to carry

`h_i = Xᵢ (XᵀX)⁻¹ Xᵢᵀ`. With `(XᵀX)⁻¹ = diag-block(1/6, [[3/10, −1/5], [−1/5, 3/10]])`:

```
h_i = 1/6 + (3/10)x² − (2/5)x·g + (3/10)g²
```

| | GRV | HLX | JDR | KPN | LTS | MRA |
|---|---:|---:|---:|---:|---:|---:|
| `h_i` | 37/60 | 41/120 | 29/120 | 89/120 | 13/60 | **101/120** |

`Σh = 3 = k` ✔ — Level 6's check, and it holds exactly.

MRA's leverage is `101/120 = 0.8417` **rounded**. Level 6 proved
`E[u_i²] = (1 − h_i)σ²`, so MRA's squared misses are shrunk by a factor of `19/120`, and an
unbiased `d` would be **6.3158× larger** *(rounded)* — `144/19 = 7.5789` *(rounded)*
instead of 1.2. With six assets and three factors there is almost nothing left over, and
`D` is badly understated as a result. **This is a real defect of the exam file, not of the
model**, because BFRE estimates `D` from **375 daily observations** (p.28, Table 1.3), not
five. Section 14 keeps the receipt.

---

## 6. STAGE 5 — ASSEMBLE `V = X F Xᵀ + D`

**PAPER, p.24, equation (1.8)**, one line below (1.7). The game writes `V` where the paper
writes `Σ`, and `D` where it writes `Δ` (`gm/VOCAB.md` §2) — a letter swap, not a different
model.

### 6a. Read it as a sentence before computing it

`Xᵀ` asks each factor *"how much of you does this book hold?"*; `F` says *"here is how we
move together"*; `X` carries the answer back to individual assets; `D` adds each stock's
private life, which no factor can speak to.

### 6b. One row, in full, so the pattern is visible

GRV's row of `X` is `(1, +3/2, +1/2)`.

```
F · Xᵀ_GRV = ( 16(1) + 2(3/2)  + (−2)(1/2),
                2(1) + 4(3/2)  +    1(1/2),
               −2(1) + 1(3/2)  +    4(1/2) )
           = ( 16 + 3 − 1,  2 + 6 + 0.5,  −2 + 1.5 + 2 )
           = ( 18,  8.5,  1.5 )

GRV–GRV common factor variance = 1(18) + 1.5(8.5) + 0.5(1.5) = 18 + 12.75 + 0.75 = 31.5
GRV–GRV total                  = 31.5 + d_GRV = 31.5 + 3.6   = 35.1
```

And a cross term, GRV against MRA, whose `X` row is `(1, −3/2, −2)`:

```
F · Xᵀ_MRA = ( 16 − 3 + 4,  2 − 6 − 2,  −2 − 1.5 − 8 ) = ( 17, −6, −11.5 )
GRV–MRA    = 1(17) + 1.5(−6) + 0.5(−11.5) = 17 − 9 − 5.75 = 2.25      (no D: i ≠ j)
```

### 6c. `V`, all thirty-six cells

|  | GRV | HLX | JDR | KPN | LTS | MRA |
|---|---:|---:|---:|---:|---:|---:|
| **GRV** | **35.1** | 27.25 | 18.75 | 15.25 | 13 | 2.25 |
| **HLX** | 27.25 | **29.4** | 17.5 | 14.75 | 13.25 | 5.25 |
| **JDR** | 18.75 | 17.5 | **19.6** | 13.75 | 13.75 | 11.25 |
| **KPN** | 15.25 | 14.75 | 13.75 | **16** | 11.75 | 8.5 |
| **LTS** | 13 | 13.25 | 13.75 | 11.75 | **24.5** | 25.75 |
| **MRA** | 2.25 | 5.25 | 11.25 | 8.5 | 25.75 | **50.2** |

Every entry is exact. Volatilities down the diagonal:

| | GRV | HLX | JDR | KPN | LTS | MRA |
|---|---:|---:|---:|---:|---:|---:|
| monthly vol, % | 5.9245 | 5.4222 | 4.4272 | **4.0000** | 4.9497 | **7.0852** |
| | *rounded* | *rounded* | *rounded* | **exact** | *rounded* | *rounded* |

**The one sentence to make the player say out loud about this table.** MRA is the riskiest
stock in the universe — 50.2, a monthly volatility of 7.0852% *(rounded)* — and it has the
**smallest** specific variance of all six (1.2). Its variance is **49** of common factors
plus **1.2** of itself — 97.6% *(rounded)* of it is the market and the two styles. A name that swings wildly is not a name with a big private life; it is a name
with big exposures. That distinction is the entire difference between `X F Xᵀ` and `D`, and
a player who has not internalised it will read every big number as idiosyncratic.

The mirror case is on the same table: GRV–MRA covariance is **2.25**, the smallest of the
fifteen off-diagonals, because GRV is `(+1.5, +0.5)` and MRA is `(−1.5, −2)` — opposite
bets on both styles, so their factor exposures nearly cancel even though both load on the
market.

### 6d. The free structural check

`X F Xᵀ` is built from three factors and describes six assets, so its rank is at most 3 and
**`det(X F Xᵀ) = 0`** — exactly, always, whenever assets outnumber factors. `det V` is
`2308676544/625`, comfortably non-zero: **`D` is what makes `V` invertible.** Level 10 §6e.

Concretely: take month 1's miss column as a set of weights —
`(−30%, +30%, +30%, −20%, −10%, 0%)`. Its factor exposures are `(0, 0, 0)` — all three,
exactly — because that is what `Σu = Σx·u = Σg·u = 0` *means*. Its factor risk is exactly
zero and its whole variance is specific: `341/250`, a risk of **1.1679%** *(rounded)*. A
book can be built out of pure miss, and the model prices it entirely out of `D`.

---

## 7. STAGE 6 — PRICE THE BOOK

The Kestrel Fund: GRV 30%, HLX 40%, KPN 15%, MRA 15%. JDR and LTS are not held.

### 7a. The book's exposures — `h = Xᵀ w`

```
h_Mkt  = 0.30 + 0.40 + 0.15 + 0.15                            = 1
h_EY   = 0.30(1.5) + 0.40(1) + 0.15(−0.5) + 0.15(−1.5)
       = 0.45 + 0.40 − 0.075 − 0.225                          = 11/20 = 0.55
h_Prof = 0.30(0.5) + 0.40(0.5) + 0.15(1) + 0.15(−2)
       = 0.15 + 0.20 + 0.15 − 0.30                            = 1/5   = 0.20
```

`h_Mkt = 1` because the book is fully invested. **PAPER, p.4:** *"The market factor
exposure of a portfolio should not be confused with its market beta"*; market factor
exposure is *"the fraction of portfolio %NAV invested in equities"* (footnote 3 adds
delta-adjusted derivative exposure). Section 8e produces the beta, which is **not** 1.

### 7b. Route 1 — exposures first

```
F h = ( 16 + 2(0.55) − 2(0.20),  2 + 4(0.55) + 1(0.20),  −2 + 1(0.55) + 4(0.20) )
    = ( 16.7,  4.4,  −0.65 )

hᵀF h = 1(16.7) + 0.55(4.4) + 0.20(−0.65) = 16.7 + 2.42 − 0.13 = 18.99
```

Term by term, so that nothing is a black box:

```
market with itself      16 · 1²            = 16
market with EY          2 · 2 · 1 · 0.55   = +2.20
market with Prof        2 · (−2) · 1 · 0.20= −0.80
EY with itself          4 · 0.55²          = +1.21
EY with Prof            2 · 1 · 0.55 · 0.20= +0.22
Prof with itself        4 · 0.20²          = +0.16
                                     total = 18.99
```

Specific:

```
Σ w²·d = 0.30²(3.6) + 0.40²(5.4) + 0.15²(2) + 0.15²(1.2)
       = 0.324 + 0.864 + 0.045 + 0.027 = 1.26
```

```
total variance = 18.99 + 1.26 = 20.25 = 81/4
BOOK RISK      = √20.25 = 4.5% per month          ← EXACT
```

### 7c. Route 2 — build `V`, then squeeze

`wᵀ V w` over the four held names, using Section 6c's table:

```
 0.30²(35.1) + 0.40²(29.4) + 0.15²(16)  + 0.15²(50.2)
 + 2[ 0.30(0.40)(27.25) + 0.30(0.15)(15.25) + 0.30(0.15)(2.25)
    + 0.40(0.15)(14.75) + 0.40(0.15)(5.25) + 0.15(0.15)(8.5) ]
 = 81/4        ✔  the same 20.25
```

**The two routes must agree** and they do, exactly. They are the same sum of products in a
different order — Route 1 aggregates to factors first, Route 2 stays in assets. If they
disagree, the arithmetic is wrong, and this is the check that finds it.

### 7d. The split

```
factor variance  18.99 / 20.25 = 211/225 = 93.7778%   (rounded)
specific        1.26  / 20.25 =  14/225 =  6.2222%   (rounded)
```

Factor risk `√18.99 = 4.3578%` *(rounded)*; specific risk `√1.26 = 1.1225%` *(rounded)*.

**And they do not add to 4.5.** `4.3578 + 1.1225 = 5.4802` *(rounded)*, which is 21.8% too
big. **Variances add; risks do not.** Level 10 §8. If the player writes the two risks
side by side and sums them, stop the exam there — that is a Section 11 fail on Stage 6 no
matter what else is right.

**Six per cent specific is not a contradiction of the paper's fifty.** p.35's 50% is a
share of **Active Risk**, not of total risk, and Stage 7 is where the comparison becomes
legitimate. A long-only fully-invested book is dominated by the market factor; that is what
`h_Mkt = 1` and `F₁₁ = 16` mean together — 16 of the 20.25 before anything else happens.

### 7e. What actually happened, and why it is not a test

The player has the returns, so they can compute what the book **did**:

| | M1 | M2 | M3 | M4 | M5 |
|---|---:|---:|---:|---:|---:|
| book return `Σwᵢrᵢ`, % | **+8.7** | +0.85 | +4.5 | −0.3 | −1.8 |
| of which factor, `h·f` | +8.7 | −0.55 | +3.9 | −0.4 | −1.9 |
| of which specific, `Σwᵢuᵢ` | **0** | +1.4 | +0.6 | +0.1 | +0.1 |

Every row adds. M1 is the striking one: the book made **+8.7%**, and **every basis point of
it** was the three factor returns times the book's three exposures —
`1(7) + 0.55(2) + 0.20(3) = 8.7` — with the four names' misses cancelling to exactly zero
against these weights. That is a coincidence of this file, not a property of the model, and
saying so is part of full credit.

The five book returns have a sample standard deviation (divisor `T − 1 = 4`) of
**4.2259%** *(rounded)*, against the model's forecast of 4.5%. **That is the same number as
trap T11**, and necessarily so: `wᵀ S w` *is* the realised sample variance of the book's own
return series. The realised active return series is `+1.25, +3.175, +1.8, 0, −0.95`, sample
standard deviation **1.5985%** *(rounded)*, against a forecast of 1.3%.

**Do not let the player call that agreement a validation.** Five numbers, in-sample, on the
same data the model was fitted to. Level 12 exists to stop exactly this sentence being said
out loud on a desk.

---

## 8. STAGE 7 — THE ACTIVE BOOK

**PAPER, p.34**, describing a real report: *"Active Risk is then decomposed along the
different factor blocks in the model … The report shows that the Active Risk is split
equally between common factors and stock specific sources."*

### 8a. The bets

| | GRV | HLX | JDR | KPN | LTS | MRA |
|---|---:|---:|---:|---:|---:|---:|
| book | 30% | 40% | 0% | 15% | 0% | 15% |
| index | 25% | 10% | 25% | 15% | 10% | 15% |
| **active** | **+5%** | **+30%** | **−25%** | **0%** | **−10%** | **0%** |

The active weights sum to **zero** — they must, since both books are fully invested. Two
names, KPN and MRA, are *held* and carry **no bet at all**: the manager owns exactly the
index weight.

```
index exposures   h_b = ( 1,  0.125,  0.10 )
active exposures  h_a = ( 0,  0.425,  0.10 )       = h_p − h_b   ✔
```

**`h_a` for the market is exactly zero**, and that single zero is the whole reason active
risk is a different animal. `F₁₁ = 16`, the biggest number in `F`, is multiplied by `0²`.

### 8b. Active risk

```
factor:   4(0.425²) + 2(1)(0.425)(0.10) + 4(0.10²)
        = 4(0.180625) + 0.085 + 0.04
        = 0.7225 + 0.085 + 0.04                       = 339/400 = 0.8475

specific: 0.05²(3.6) + 0.30²(5.4) + 0.25²(4.6) + 0.10²(6)
        = 0.009 + 0.486 + 0.2875 + 0.06               = 337/400 = 0.8425

variance  = 0.8475 + 0.8425 = 1.69 = 169/100
ACTIVE RISK = √1.69 = 1.3% per month                  ← EXACT
```

`aᵀ V a` gives the same 169/100 — the two routes again.

### 8c. The split, and the one comparison the paper lets us make

```
factor   0.8475 / 1.69 = 339/676 = 50.1479%   (rounded)
specific 0.8425 / 1.69 = 337/676 = 49.8521%   (rounded)
```

Half a percentage point off a dead heat. **PAPER, p.35, Figure 1.18**, printed digits:
Specific **50%**, Style **25%**, Industry **14%**, Country **6%**, FX **4%**, Act Sec
**1%** `[INFERRED — the glyph reads 1 or 2; 1% is recorded only because the six then sum to
exactly 100]`. The common blocks sum to 50 and Specific is 50.

**This is the highest-leverage check in the whole game and the player should be made to run
it themselves.** `gm/LEVEL_ANCHORS.md` §16(c): a rebuild returning 95% specific has an `X`
that explains nothing; one returning 95% common has factors that have eaten the
idiosyncratic noise. Ours returns 50.1/49.9 on a book of four names against an index of
six, which is the right neighbourhood for the right reason — and it is a check the paper
never runs on itself, because the Model Testing chapter (pp.32–33) reports no values at
all.

Do not oversell it. **One agreeing ratio on a six-stock toy is corroboration, not
validation.** Say the words.

Active factor risk `√0.8475 = 0.9206%` *(rounded)*; active specific risk `√0.8425 =
0.9179%` *(rounded)*. Those two do not add to 1.3 either — `1.8385` *(rounded)*.

### 8d. The trap with the widest gap between wrong and right

The benchmark's own risk:

```
factor   16 + 2(2)(0.125) + 2(−2)(0.10) + 4(0.125²) + 2(1)(0.125)(0.10) + 4(0.10²)
       = 16 + 0.5 − 0.4 + 0.0625 + 0.025 + 0.04           = 6491/400 = 16.2275
specific 0.25²(3.6)+0.10²(5.4)+0.25²(4.6)+0.15²(2)+0.10²(6)+0.15²(1.2)
       = 0.225 + 0.054 + 0.2875 + 0.045 + 0.06 + 0.027    = 1397/2000 = 0.6985
variance = 8463/500 = 16.926      index risk = 4.1141%    (rounded)
```

```
book risk − index risk = 4.5000 − 4.1141 = 0.3859   (rounded)
true active risk                          = 1.3000
```

Wrong by a factor of more than three, and wrong in the dangerous direction — it makes the
book look three times tamer than it is. **Risk is not a difference of risks.** You must
form the difference *portfolio*, `a = w − b`, and price that.

### 8e. The identity that proves all three numbers hang together

`p = b + a`, so `Var(p) = Var(b) + 2Cov(a,b) + Var(a)`:

```
Cov(a, b) = aᵀ V b = 817/1000 = 0.817
16.926 + 2(0.817) + 1.69 = 16.926 + 1.634 + 1.69 = 20.25    ✔
```

That is a *third* independent route to 20.25, and it is the check a desk actually runs when
a report's three headline numbers are printed side by side.

**Beta**, since the identity hands it over:

```
Cov(p, b) = Var(b) + Cov(a, b) = 16.926 + 0.817 = 17.743
beta      = 17.743 / 16.926 = 17743/16926 = 1.0483    (rounded)
```

**Market factor exposure 1.00, beta 1.0483.** The same book, two different numbers, and
p.4 warns in as many words not to confuse them. **Read the warning label on this
calculation:** the paper prints **no formula** for beta. `notes/` records
`β_{p,b} = (Xₚᵀ F X_b)/(X_bᵀ F X_b)` on p.4 as a **reader's handwritten margin
annotation**, not the paper's text (`gm/LEVEL_ANCHORS.md` §17). The printed sentence only
says beta *"can instead be computed via the risk factor exposures of the portfolio and
market index, together with the factor covariance matrix."* Our `Cov/Var` is the ordinary
definition applied to the model's own `V`; it is **ours**, and it includes the specific
term that the margin formula drops.

---

## 9. STAGE 8 — WHERE THE ACTIVE RISK ACTUALLY IS

Level 11's machinery, on the active book. One matrix–vector product does everything.

```
V a  =  ( 3.9425,  4.4825,  −0.0875,  0.5750,  −1.2625,  −3.7000 )
```

(exactly `1577/400, 1793/400, −7/80, 23/40, −101/80, −37/10`.)

| | active bet `aᵢ` | `(V a)ᵢ` | contribution `aᵢ(Va)ᵢ` | share of active variance | marginal contribution `(Va)ᵢ / 1.3` |
|---|---:|---:|---:|---:|---:|
| GRV | +5% | 3.9425 | 0.197125 | **11.6642%** | +3.0327 |
| HLX | **+30%** | 4.4825 | 1.344750 | **79.5710%** | +3.4481 |
| JDR | **−25%** | −0.0875 | 0.021875 | **1.2944%** | −0.0673 |
| KPN | 0% | 0.5750 | 0 | **0.0000%** | +0.4423 |
| LTS | −10% | −1.2625 | 0.126250 | **7.4704%** | −0.9712 |
| MRA | 0% | −3.7000 | 0 | **0.0000%** | −2.8462 |
| | | | **1.69** ✔ | **100%** ✔ | |

*(All percentages and marginal contributions rounded; the contributions themselves are
exact.)*

**Three sentences the player must produce from this table, unprompted:**

1. **One bet is four-fifths of the risk.** HLX is +30% and carries **79.57%** of active
   variance. Every other decision in the book is noise beside it.
2. **The second-biggest bet is almost free.** JDR is −25% of NAV — a huge position — and
   contributes **1.29%**. Its marginal contribution is **−0.0673**, so covering one
   percentage point of that short moves active risk by `−7/10400 = −0.000673` *(rounded)*
   percentage points: nothing. Exposure is not contribution.
   This is exactly the pattern printed on **p.35**, where Airlines is ninth of ten by
   exposure and second by risk contribution `[APPROX — every bar and dot on p.35 is a pixel
   measurement, ±10%; the ordering survives, the magnitudes are not figures]`.
3. **The riskiest stock in the universe contributes nothing.** MRA has the highest total
   volatility (7.0852% *rounded*) and is **held at 15%** — and its contribution to *active*
   risk is exactly zero, because the index holds 15% too. Its marginal contribution is
   **−2.8462**, so buying one percentage point more MRA moves active risk by
   `−37/1300 = −0.028462` *(rounded)* percentage points — **forty-two times** the effect of
   the same trade in JDR, in a name the active book does not bet on at all. Buying it
   would *reduce* active risk, because it tilts the book away from the bets it already
   has. Risk relative to a benchmark is about **differences**, and a position that matches
   the index is invisible to it however wild the stock.

The same machinery on the book's **total** risk gives a different ordering again — GRV
**35.6370%**, HLX **45.3037%**, KPN **10.4815%**, MRA **8.5778%** *(all rounded, summing to
100%)*. MRA is 8.6% of total risk and 0% of active risk. Two correct answers to two
different questions, and a player who cannot say which question a PM is asking will answer
the wrong one.

---

## 10. The three free checks, and when to run them

These cost nothing, catch nearly everything, and the player must run them **without being
told to**. Section 13 makes that observable.

| # | Check | When | What it catches |
|---|---|---|---|
| 1 | **Fifteen balances.** `Σu = Σx·u = Σg·u = 0`, in every month. | End of Stage 2, before anything else is built | Any arithmetic slip in `f` or in one miss. It is the Level-2 condition and it is free — the arithmetic *forces* it, so a non-zero is proof of an error. |
| 2 | **114 two ways.** Sum the squared misses down the stocks and across the months. | End of Stage 4 | A miss copied wrongly when the table was transposed — the single most common transcription error at this level. |
| 3 | **Two routes to 81/4.** `hᵀF h + Σw²d` against `wᵀ V w`. | End of Stage 6 | Any error in `V`, in `h`, or in the assembly. Route 2 uses cells of `V` that Route 1 never touches. |

A fourth, if the player wants it: `Var(book) = Var(index) + 2Cov(active, index) +
Var(active)`, Section 8e, `16.926 + 1.634 + 1.69 = 20.25`.

---

## 11. THE MARKING SCHEME

**The governing rule, and it outranks every row below** (`RISK_DESK.md` §8): *never accept
a right answer with wrong reasoning.* At this level that has teeth, because Section 12.2
contains a wrong method that produces **exactly 4.5000**. **Mark the objects, not the last
number.** Demand `X`, the five `f` triples, `F`, `D` and `h` on paper before you look at
the risk.

Scoring: each stage is **PASS**, **NEAR MISS** or **FAIL**. A pass on Level ★ requires
**eight PASSes, no FAILs, and at most one NEAR MISS** — and the near miss must be arithmetic,
never a concept.

### Stage 1 — `X`

| | |
|---|---|
| **Full credit** | Three columns. A column of ones, *named as the market factor*, with p.4's "unit exposure" or p.26's "intercept term" said out loud. Both style columns centred and divided by their own equal-weighted standard deviation. Exposures `(+1.5, +1, 0, −0.5, −0.5, −1.5)` and `(+0.5, +0.5, +0.5, +1, −0.5, −2)`. Checks `Σx = 0` and `Σx² = 6` stated unprompted. |
| **Near miss** | Correct columns, but the player cannot say why `Σx² = 6`, or computes the sd as `√(24/5) = 2.1909` *(rounded)* using the `n − 1` divisor. **The tell for the second one is precise:** their `Σx²` comes out **5**, not 6, and every downstream number is off. Accept as a near miss only if they catch it themselves at check 1. |
| **Fail** | No column of ones. Or raw characteristics used as exposures (see 12.2 — this is a **fail even though the final risk is right**). Or the two columns standardised against each other's statistics. |

### Stage 2 — the factor returns

| | |
|---|---|
| **Full credit** | The 3×3 system written down, the market row observed to detach because `Σ1·x = Σ1·g = 0`, `det = 20`, and the five triples `(7,2,3) (−3,3,4) (3,2,−1) (−1,0,3) (−1,−2,1)`. All fifteen balance conditions checked. |
| **Near miss** | Right triples, but obtained by solving the full 3×3 by elimination every month without noticing the structure — slow, correct, and it means they did not use Level 5. Or one arithmetic slip caught by their own balance check and fixed. |
| **Fail** | One column at a time (`Σxr/6`, `Σgr/6`). Or the balance conditions not checked at all. Or the misses computed against the wrong month's factor returns. |

### Stage 3 — `F`

| | |
|---|---|
| **Full credit** | `F = [[16,2,−2],[2,4,1],[−2,1,4]]`, divisor `T − 1 = 4`, each series centred on **its own** mean (1, 1 and **2**), and the player can say why this divisor differs from Stage 4's. Volatilities 4, 2, 2 and correlations +1/4, −1/4, +1/4 read off. |
| **Near miss** | Right matrix, divisor defended as "that's the sample covariance formula" without the degrees-of-freedom argument. Or `det F` not checked. |
| **Fail** | Divisor `T` (gives `[[12.8,1.6,−1.6],…]`, every entry exactly 4/5 of the truth). Or means not subtracted. Or correlations computed and used where covariances belong (trap T10). Or a `+` where a `−` belongs on `F₁₃` — check the sign. |

### Stage 4 — `D`

| | |
|---|---|
| **Full credit** | `d = (3.6, 5.4, 4.6, 2, 6, 1.2)`, divisor `T = 5`, **no** mean subtracted, and the player states that the zero mean is an *assumption* — plus notices that LTS's five misses are all negative and says why that is allowed. Check 2 (114 twice) run. |
| **Near miss** | Right numbers, but the divisor defended by "that's how you average" rather than by the degrees-of-freedom argument. Or the LTS observation not made until prompted. |
| **Fail** | Divisor `T − 1` (gives 4.5, 6.75, 5.75, 2.5, 7.5, 1.5). Or each stock's own mean subtracted (gives 3.7, 4.3, 5.3, 2.5, 2.5, 0.7). Or the misses averaged **across stocks within a month**, which produces five numbers when `D` needs six — a shape error, and an immediate fail. |

### Stage 5 — `V`

| | |
|---|---|
| **Full credit** | `V` correct for at least the four held names, `D` added to the **diagonal only**, symmetry observed, and the singularity of `X F Xᵀ` stated — with the reason (three factors, six assets) and the consequence (`D` is what makes `V` invertible). |
| **Near miss** | Correct `V`, singularity not mentioned until asked. Or only the four held names computed — acceptable, and arguably smart, but then say so rather than leaving the other rows blank. |
| **Fail** | `D` added to every cell. Or `X F Xᵀ` computed as `Xᵀ F X` (wrong shape: 3×3 instead of 6×6 — it will not even conform, and a player who "fixes" the non-conformity by transposing something at random has lost the sentence-reading of Level 10). |

### Stage 6 — the book's risk

| | |
|---|---|
| **Full credit** | `h = (1, 0.55, 0.20)`, factor variance 18.99, specific 1.26, total **20.25**, risk **4.5%**, both routes shown to agree, and the 93.78 / 6.22 split stated with the explanation that the market factor is doing it. |
| **Near miss** | 4.5 by one route only. Or the split computed on risks instead of variances (see below). |
| **Fail** | `4.3578 + 1.1225 = 5.4802`. Adding risks is the one error at this level that cannot be an arithmetic slip — it is a misunderstanding of what a variance is, and Level 10 spent a whole section on it. Also a fail: `h_Mkt` computed as anything other than 1 for a fully-invested long-only book. |

### Stage 7 — active risk

| | |
|---|---|
| **Full credit** | `a = (+5, +30, −25, 0, −10, 0)%` summing to zero; `h_a = (0, 0.425, 0.10)` with the zero **explained**; variance 1.69; risk **1.3%**; the 50.15 / 49.85 split; and the comparison to p.35's printed 50% made *with* the caveat that one toy ratio is corroboration, not validation. |
| **Near miss** | 1.3% correct, but the market-exposure zero treated as a coincidence rather than as the definition of a fully-invested active book. Or the specific leg computed correctly but the player cannot say why `aᵢ` and not `wᵢ` appears in it. |
| **Fail** | `4.5 − 4.1141 = 0.3859`. Or the specific leg computed on the book's weights: `0.8475 + 1.26 = 2.1075`, risk **1.4517** *(rounded)*. Or active risk computed as `|a|ᵀ V |a|`. |

### Stage 8 — contributions

| | |
|---|---|
| **Full credit** | `V a` computed once; contributions summing to 1.69 and to 100%; HLX at **79.57%** identified as the book; JDR's 1.29% on a 25% position called out as the exposure-is-not-contribution case; MRA's zero explained by the index weight. |
| **Near miss** | Contributions right, but presented without the observation that they sum to the variance — which is the only reason the decomposition is legitimate. |
| **Fail** | Contributions computed as `aᵢ² Vᵢᵢ` (ignores every off-diagonal, will not sum to 1.69). Or ranked by position size and called a risk decomposition. |

---

## 12. THE TRAPS — what a memoriser produces, and how to recognise it from the number alone

This is the diagnostic table. **Read the player's wrong number off the left column and you
know what they did.** Every figure here is computed by the verifier.

| # | The wrong move | Book risk | Active risk | The unmistakable tell |
|---|---|---:|---:|---|
| **T1** | one column at a time (Level 4 forgotten) | **4.8388** *(r)* | **1.7039** *(r)* | their misses fail `Σx·u = 0` — month 1 gives **−52/3** |
| **T2** | never standardised `X` | **4.5000** | **1.3000** | **the risk is right.** Their `f_EY` is 1, 1.5, 1, 0, −1 and their book's EY exposure is **6.1** |
| **T3** | `F` divided by `T`, not `T − 1` | **4.0561** *(r)* | **1.2331** *(r)* | every entry of `F` is exactly 4/5 of the truth |
| **T4** | `D` divided by `T − 1`, not `T` | **4.5349** *(r)* | **1.3786** *(r)* | `d_KPN = 2.5` instead of 2 |
| **T5** | each stock's own mean miss removed | **4.4814** *(r)* | **1.2649** *(r)* | `d_LTS` collapses from 6 to **2.5** |
| **T6** | `D` dropped entirely | **4.3578** *(r)* | **0.9206** *(r)* | the split reads 100% factor / 0% specific |
| **T7** | only `F`'s diagonal kept | **4.3162** *(r)* | **1.2669** *(r)* | `hᵀF h` has three terms instead of six |
| **T8** | active risk as a difference of risks | — | **0.3859** *(r)* | a suspiciously small number and no active weight vector on the paper |
| **T9** | no market factor in `X` | **2.6946** *(r)* | — | `d` = 6.2, 29.2, 26.8, 7.8, 23.8, 11.8 — HLX's *private* variance alone would be 29.2, against a total variance of 29.4 |
| **T10** | `F` built as correlations, not covariances | **1.6830** *(r)* | — | `F` has 1s down the diagonal |
| **T11** | the stocks' own sample covariance matrix, no model | **4.2259** *(r)* | **1.5985** *(r)* | `det = 0` — the matrix is singular |
| **T12** | annualise by ×12 | **54** | **15.6** | a monthly-to-annual factor of 12 instead of √12 |
| **T13** | market exposure quoted as beta | — | — | they report beta = 1.00; it is **1.0483** *(rounded)* |

*(r) = rounded.*

The five that need their own paragraph:

### 12.1 T1 — one column at a time, followed all the way through

Level 4's collision is the reason Stage 2 is a *simultaneous* solve, and a player who
reverts to `Σxr/Σx²` per column does not merely get the factor returns wrong. The error
propagates: their misses no longer balance (`Σx·u = −52/3` in month 1), so their `F` comes
out `[[16, 2/3, −2/3], [2/3, 64/9, 61/9], [−2/3, 61/9, 64/9]]` — note the style
correlation, which should be +1/4, has become `61/64 = 0.953125` — and their `D` reads
`(15, 52/9, 92/15, 26/9, 139/45, 454/15)`, i.e. GRV at **15** against the true 3.6 and MRA
at **30.2667** *(rounded)* against the true 1.2. The book prices at **4.8388%** *(rounded)*
and the active book at **1.7039%** *(rounded)* — **7.5%** and **31%** too high
respectively. The tell is not the risk number, which looks plausible. It
is the balance condition, which is free.

### 12.2 T2 — never standardised, and the risk is still exactly right

This is the most important row in the table and the reason Section 11 marks objects rather
than answers.

Run Stage 2 with the **raw** characteristics as columns — earnings yield 8, 7, 5, 4, 4, 2
and operating margin 12, 12, 12, 13, 10, 7, plus a column of ones. The Gram matrix is ugly
(`[[6,30,66],[30,174,346],[66,346,750]]`) but it solves, and month 1 returns
`(−14.5, 1, 1.5)`. And then:

- **The misses are identical.** All thirty of them, in all five months, to the number.
- **`F` is completely different**: `[[201.5, −6.75, −13.25], [−6.75, 1, 0.25], [−13.25, 0.25, 1]]`.
- **`D` is identical**, because it is built from the misses.
- **`X F Xᵀ` is identical, cell for cell**, and therefore so is `V`, and therefore the book
  prices at exactly **20.25** and **4.5%**, and the active book at exactly **1.3%**.

The reason is one line of algebra the player should be made to produce: standardising
replaces `X` by `X A` for an invertible 3×3 `A`, which replaces `f` by `A⁻¹f` and `F` by
`A⁻¹ F A⁻ᵀ`, and `(XA)(A⁻¹FA⁻ᵀ)(XA)ᵀ = X F Xᵀ`. The `A`s cancel. **Standardisation does not
change the risk. It changes what the numbers mean.**

What it does change, and why BFRE does it anyway (**PAPER, p.10**): an exposure of +1 means
*one standard deviation above the market average*, so exposures are comparable across
characteristics measured in different units, across time, and across regional models; and
substyles can be averaged into styles (pp.40–41) only because they share a scale. Without
it, this book's reported Earnings Yield exposure is **6.1** — which is not "6.1 standard
deviations", it is "6.1 percentage points of earnings yield", and it cannot be compared
with anything, capped at ±3 (p.39), or aggregated with anything else.

**Marking:** a player who skips standardisation and lands on 4.5 has *not* passed. Ask them
for the book's Earnings Yield exposure. If they say 6.1 and cannot say what the 6.1 is
measured in, that is a Stage 1 fail regardless of the final number. If they can derive the
invariance above, pay them for it generously — it is a genuinely good piece of
understanding — and still fail Stage 1, because BFRE's exposures are standardised and a
model whose exposures are not is not BFRE.

### 12.3 T9 — the missing column of ones

Drop the intercept and the market's common movement has nowhere to live except the misses.
The specific variances become `(6.2, 29.2, 26.8, 7.8, 23.8, 11.8)`, the book's factor
variance falls to 1.59, its specific variance rises to 5.671, and the total comes to 7.261
— a risk of **2.6946%** *(rounded)* against the true 4.5%. **The book looks 40% safer
because the single largest source of shared risk has been reclassified as six independent
private wobbles that diversify away.** This is Level 9's direction-of-error argument
(**PAPER, p.28**: ignoring correlation *"would lead to under (or over) prediction of
specific risk in a long-only (long-short) portfolio context"*) in its purest form, and it
is the most dangerous single error in the exam.

### 12.4 T11 — why not skip the model entirely?

The obvious question, and it deserves the full answer. Compute the ordinary 6×6 sample
covariance matrix of the six return series directly, divisor `T − 1 = 4`. It exists. It
prices the book at **4.2259%** *(rounded)* and the active book at **1.5985%** *(rounded)*.

And it is **singular**: `det = 0`, exactly. Five months of returns, centred, leave at most
four independent directions, so there are directions in which that matrix reports **zero
risk** for a portfolio that plainly has some. The counting:

```
a 6x6 covariance matrix     :  21 distinct numbers to estimate, from 30 returns
the factor model            :   6 in F  +  6 in D  =  12, from the same 30
```

**PAPER, p.2:** BFRE *"imposes far more structure on the asset covariance matrix, reducing
the modelling problem to a smaller set of factors, which capture the most important sources
of asset return commonality."* That sentence is this arithmetic. And it scales the way the
paper needs it to: at 500 assets the direct matrix needs 125,250 numbers and the factor
model with 3 factors needs 506.

**Say the honest part too.** Our `V` is not singular, but it is not *well* estimated
either: `F`'s six entries come from five observations. Level 8's argument lands here too,
and Section 14 keeps the receipt.

### 12.5 T13 — exposure is not beta

The book's market factor exposure is **1.00** (fully invested; p.4). Its beta against the
NG-6 index is **1.0483** *(rounded)*. Both are correct; they are answers to different
questions. **PAPER, p.4**, in as many words: *"The market factor exposure of a portfolio
should not be confused with its market beta."* A player who reports 1.00 as the beta has
walked into the one confusion the paper explicitly warns about — and the p.35 report makes
the same point in the other direction, printing Portfolio Beta **1.02** in its banner while
the style panel shows a Market dot at ≈**0.0** `[APPROX, ±10%]`, because that panel plots
*active* exposure.

---

## 13. THE FOUR VICTORY CONDITIONS, MADE OBSERVABLE

`RISK_DESK.md` §3 lists four conditions and says each is testable. The failure mode is
marking them on a feeling. Each one below is a thing you **watch happen at a named moment**,
with a pass line.

### VC1 — THE WIKI TEST: *answers from structure, and can produce any number's origin on demand*

**Observable:** six ambush questions, fired mid-stage, without warning, while the player is
mid-arithmetic. Each must be answered in under a minute, from the page in front of them.

| Fire it when | The question | Full credit contains |
|---|---|---|
| They write `/10` in Stage 2 | *"Where did that ten come from?"* | `det = 6·6 − 4·4 = 20`, halved by the 2 in Cramer's numerators. Not "it's the formula." |
| They write `Σx² = 6` | *"Why six? Would it be six if I gave you nine stocks?"* | It is `n`, forced by dividing by the equal-weighted sd. With nine stocks it would be 9. |
| Stage 3, when `F` appears | *"Why 4 and not 5?"* | One mean was estimated from the same five numbers. Degrees of freedom. |
| Stage 4, when `D` appears | *"Then why 5 and not 4 here?"* | No parameter was estimated from that stock's own series; the mean is asserted, not estimated — and that assertion is visibly false for LTS. |
| Stage 6 | *"Your specific risk is 6% of the total. The paper says 50%. Which of you is wrong?"* | Neither: p.35's 50% is of **Active** Risk. Stage 7 is where the comparison becomes legitimate. |
| Stage 8 | *"JDR is a quarter of the book's active bet and 1.3% of its risk. Is the model broken?"* | No, and it is arithmetic, not hand-waving: JDR's covariance with the active book is `+1.0625` through the factors and `−1.15` through `D` (its own `d` of 4.6 times its `−0.25` bet), and those two nearly cancel to `−0.0875`. Contribution is `aᵢ × (V a)ᵢ`, so a near-zero second factor beats a large first one. |
| **Pass line** | **Five of six, first time, without reaching for earlier work.** Two "it's the formula" answers is a fail regardless of the other four. | |

### VC2 — THE PASSING TEST: *nothing reveals that they have no finance or statistics background*

**Observable:** a **20-minute conversation after the exam**, run as round type E
(`RISK_DESK.md` §6E) — a hostile CRO with thirty years on the desk who has the player's
worksheet in front of them. Three things are scored, and all three are countable.

**(i) The sixteen terms.** Keep a tally sheet. `gm/VOCAB.md` §3 lists them; every one is
unlocked by now. The player must use **at least twelve of the sixteen correctly and
unprompted**, in their own explanation of their own work — not in answer to "what does X
mean?"

```
cross-sectional regression · orthogonal · residual · specific risk · exposure · loading
design matrix · degrees of freedom · standard error · covariance matrix · shrinkage
eigenvalue · tracking error · marginal contribution · multicollinearity · in-sample/out-of-sample
```

**Eight of the sixteen do not occur anywhere in the paper** — `gm/VOCAB.md` §6 lists them:
*orthogonal, loading, design matrix, degrees of freedom, standard error, eigenvalue,
tracking error, marginal contribution.* **Four of those eight must come out of the player's
mouth with a warning label attached**, because for each of them the paper has its own word
or its own label and swapping them silently is the tell of somebody who learned the
vocabulary from a textbook and has not read the document:

| The player says | The label they must attach |
|---|---|
| *tracking error* | the paper says **Active Risk** (p.35 banner) — and our 1.3% is the Kestrel Fund's tracking error |
| *orthogonal* | the paper says **neutral** (p.5) |
| *design matrix* | the paper writes `X` throughout and never names it |
| *marginal contribution* | the paper's own label is the axis title *"Contrib. (% of Act. Risk)"* (p.35), and it prints no formula |

Using any of the four as though BFRE used it is a Victory-Condition-2 failure in itself.

**(ii) Five CRO questions, escalating.** Real objections, not quiz questions.

1. *"Your market factor return is just the average return. Why am I paying for a model?"*
   — Landed: because the **other two** columns are solved simultaneously with it, and only
   the fact that the style columns are centred makes the market column collapse to the
   average. Change the centering and it stops being the average. Not landed: "because it's
   weighted" (it isn't, here) or agreeing that the model adds nothing.
2. *"Five months. Would you sign this?"* — Landed: no, and here is the specific damage —
   `F` has six entries from five observations; `D`'s leverage correction is a factor of 6.3
   on MRA; BFRE uses **104 weeks** for `F` and **375 days** for `D` (p.27, p.28,
   Table 1.3). Not landed: "more data would be better" with no numbers.
3. *"Your risk says 4.5% a month, and this book made 8.7% in month one. Useless."* —
   Landed: 4.5% is a standard deviation, not a cap; +8.7% is under two of them, in a month
   when the market factor alone paid +7%. And the model *explains* that month exactly:
   `1(7) + 0.55(2) + 0.20(3) = 8.7`, with the misses cancelling to zero on these weights
   (§7e). Follow-up, if they survive that: *"and MRA fell 13.5% in month two — is that your
   model or your stock?"* — the model: MRA's M2 miss was **+2**, so the model was
   pessimistic about MRA that month; the −13.5% was a −3% market with both style factors
   up strongly against a name short both. Not landed: any answer that treats a single
   realisation as a test of a forecast.
4. *"Drop JDR from the benchmark. What happens to my active risk?"* — Landed: it changes
   the benchmark's exposures, therefore the active exposures, therefore everything — you
   would have to recompute, and the direction is not obvious because JDR's marginal
   contribution is currently negative. Not landed: any confident number produced without
   recomputing.
5. *"Convince me your specific risk isn't just the part you couldn't be bothered to
   model."* — Landed: that is exactly what it is, and the model says so — `D` is the
   variance of what the three columns could not reach, and the near-exact 50/50 split
   in Stage 7 says
   half this book's active risk lives there. The honest defence is p.28's: BFRE assumes
   specific returns across companies are uncorrelated *"in-line with standard modelling
   practice"*, and that assumption is the weak point, not the residual itself. Not landed:
   defending `D` as though it were measured rather than left over.

**(iii) Register.** No hedging on things they computed; hedging exactly where the file is
thin (five months, one snapshot of exposures, no weighting). A player who is *equally*
confident about 4.5% and about what it means out of sample fails this condition even with
every number right.

**Pass line:** twelve of sixteen terms, all four warning labels, four of five objections
landed.

### VC3 — THE ORIGIN TEST: *can derive every formula, including the parts textbooks skip*

**Observable:** a **closed-book derivation slot, 15 minutes, after the exam**, three
prompts, blank paper, nothing else.

| Prompt | Full credit |
|---|---|
| *"Derive `b = Σxr/Σx²` without calculus."* | The nudge argument of Level 1: move `b` by `δ`, watch the sum of squared misses change by `−2δΣxr + δ²Σx²`, set the linear term to zero. |
| *"Where does a standard error come from? Not the formula — where does it come from."* | Level 6: `b̂ = b + Σxu/Σx²`, so the estimate is the truth plus a weighted sum of the misses; the width of that second term is `σ²/Q`. The `n − k` in `σ̂²` because the misses are not free — here, three of six. |
| *"Why is `D`'s divisor 5 and `F`'s divisor 4? Show me a case where it matters."* | The degrees-of-freedom argument in both directions, plus a number from Section 12: T4 gives 4.5349, T3 gives 4.0561. |
| **Pass line** | **All three.** This is the condition the rules call the hardest, and a two-of-three is a re-sit, not a pass. | |

### VC4 — THE REBUILD TEST: *the thing itself*

**Observable:** six checkpoints, which either match or do not. No judgement required.

| # | Checkpoint | The answer |
|---|---|---|
| A | `X`'s two style columns | `Σx² = Σg² = 6`, `Σx·g = 4` |
| B | The five factor-return triples | `(7,2,3) (−3,3,4) (3,2,−1) (−1,0,3) (−1,−2,1)` |
| C | `F` | `[[16,2,−2],[2,4,1],[−2,1,4]]` |
| D | `D` | `(3.6, 5.4, 4.6, 2, 6, 1.2)` |
| E | Book risk | **4.5%** per month, exactly |
| F | Active risk | **1.3%** per month, exactly |

**Pass line:** all six, plus the three free checks of Section 10 run **unprompted**, plus
Section 11's object-marking. Six matching numbers with an unstandardised `X` is a fail
(12.2); six matching numbers with no balance check run is a pass on arithmetic and a fail
on Victory Condition 4, because the condition says *alone, with no reference material* —
and alone means self-checking.

### The scoreboard to write in the save file

```
VC1 WIKI     : __ / 6 ambush questions
VC2 PASSING  : __ / 16 terms, __ / 4 warning labels, __ / 5 objections
VC3 ORIGIN   : __ / 3 derivations
VC4 REBUILD  : __ / 6 checkpoints, __ / 3 unprompted checks
Stages       : __ PASS, __ NEAR MISS, __ FAIL
```

---

## 14. What this exam does NOT settle

Say all of this to the player at the debrief, before they get to feel finished. A rebuild
that does not know its own limits is a Victory-Condition-2 failure waiting to happen.

1. **Five months is not an estimate, it is an anecdote.** `F` has six distinct entries
   estimated from five observations. `D` has six numbers from five observations each, and
   Section 5e's leverage argument says MRA's is understated by a factor of **6.3158**
   *(rounded)*. BFRE uses **104 weeks** with a **26-week half-life** for `F` (**PAPER,
   p.27**) and **375 days** with a **125-day half-life** for `D` (**PAPER, p.28, Table
   1.3**). Nothing on this page would survive being run on next month's data, and the
   player should say so unprompted.
2. **No weighting.** BFRE weights by **√ market capitalisation** (**PAPER, p.25**), for a
   stated reason: equal weighting gives *"a poor fit for mega-cap and large-cap
   securities"*, pure cap weighting gives *"poorer forecasts for mid-cap and small-cap
   securities"*, and the square root *"adjusts for heteroskedasticity."* With weights, the
   market column would **no longer detach** from the styles (`Σw·x ≠ 0` in general) and
   every month would need a genuine 3×3 weighted solve. The error from omitting it has a
   known address: it lands on a size segment, not uniformly.
3. **No exponential decay, no half-life, no Newey–West.** All three are **PAPER** (p.27),
   all three are out of scope here, and the third is graduate-level. Their absence means
   this `F` treats a five-month-old observation exactly like last week's, which is the one
   thing p.27 says a covariance matrix must not do if forecasts are to be *"responsive to
   changes in the market environment."*
4. **`D` is diagonal here, and BFRE's is not.** **PAPER, p.27:** *"The asset specific
   covariance matrix is made up of two components: a vector of asset specific risk
   forecasts and a sparsely populated unit diagonal matrix containing non-zero,
   off-diagonal specific return correlations."* The shipped `Δ` is sparse, not diagonal.
   **Do not teach this as a gotcha** — (1.8) on p.24 is introduced as the *generic*
   multi-factor form (*"In general a multi-factor model decomposes asset returns as
   follows"*), and p.28 gives BFRE's own treatment a full subsection. `gm/CRITIQUE.md`
   CS-3 files "(1.8) says diagonal but p.27 says otherwise" as a named cheap shot. The real
   point is **scope**: correlations are estimated only between assets *in the same company*;
   across companies they are *"assumed to be zero in-line with standard modelling
   practice"* (p.28).
5. **Three factors is not a model.** NAMR carries a market factor, twelve styles, fifty-four
   core industries and a country/currency block. The paper **never prints a factor count**;
   the floor of ≈71 assembled in Level 8 §13c is **ours**, counted from Table 1.2 (p.10)
   and Table 1.5 (p.57). With industries and countries in the file, (1.10)'s two identifying
   restrictions become necessary and the whole of Level 2's second half comes back.
6. **One number agreeing with p.35 is corroboration, not validation.** Our 50.1/49.9 split
   matches the paper's printed 50/50 pie, and that is the best check available — but the
   Model Testing chapter (pp.32–33) reports **no values at all**: no `R²`, no VIF, no bias
   statistic, all deferred. We are checking our toy against a single printed report of a
   single portfolio on a single day. Say that out loud.
7. **The beta in Section 8e is ours.** The paper prints no formula for it; the one in
   `notes/` on p.4 is a reader's **handwritten margin annotation**. Never attribute it to
   BlackRock.
8. **`t`-statistics, factor selection, and whether these two factors deserve to exist at
   all** are Levels 6 and 12, and this exam does not ask. A rebuilt model that nobody
   selected the columns for is half a model. If the player wants the full article, the
   two-step screen of (1.3)–(1.6), pp.10–12, is where it lives.

---

## 15. Back to BFRE — what the player just rebuilt, page by page

**The whole of what they did is on five pages.** `gm/LEVEL_ANCHORS.md` §16 calls this the
five-page checklist; here it is against the eight stages they have just finished.

| Stage | What they built | Where it lives in the paper |
|---|---|---|
| 1 | `X` | Standardisation rule **p.10**; ±3 cap and equal-weighted sd **p.39**; unit exposure to the market factor **p.4**; "three intercept terms" **p.26** |
| 2 | `f`, five months | Equation **(1.9), p.25** — four blocks, one solve; the cadence, **p.24**: *"a series of cross-sectional regressions"*, run **daily** for regional models and **weekly** for the World model; weights **p.25** |
| 3 | `F` | `F` in equation **(1.8), p.24**; construction **p.27** — daily series from **March 1996**, default **WKL**: **104 weeks**, **26-week half-life** |
| 4 | `D` | `Δ` in **(1.8), p.24**; what BFRE actually builds, **p.27**; parameters **Table 1.3, p.28** — daily **125 days / 375 obs / 10-day Newey–West lag** |
| 5 | `V` | Equation **(1.8), p.24**, one line below (1.7) |
| 6 | Book risk | The ingredient list on **p.24**: holdings, portfolio exposures *"aggregated from the asset level"*, a factor covariance matrix, specific risk forecasts |
| 7 | Active risk | **p.34**: *"the Active Risk is split equally between common factors and stock specific sources"*; the report itself, **Figure 1.18, p.35** |
| 8 | Contributions | **p.35**'s axis label, *"Contrib. (% of Act. Risk)"*, plotted against *"Act. Exp."* on a second axis — the paper draws the distinction and prints **no formula** for it. The mathematics of Stage 8 is **ours** |

**The landing sentence, for the end of the game.**

> "Everything you built is on five pages. Page 24 has the model, equations (1.7) and (1.8).
> Page 25 has the regression, equation (1.9). Page 26 has the two restrictions that make it
> solvable, equation (1.10), and the second pass, equation (1.11). Pages 27 and 28 have the
> six numbers — March 1996, 104 weeks, 26 weeks, 125 days, 375 days, 10 days. The other
> sixty pages tell you what to put in `X` and what the answer is supposed to look like when
> you print it. You have just done the five pages by hand, and you can now read the other
> sixty and argue with them."

**And one last thing to hand over with the rank.** The player has built a model whose
`X F Xᵀ` is singular, whose `F` rests on five observations, whose `D` assumes a zero mean
that LTS visibly violates, and whose exposures are equal-weighted where BFRE's are not.
Every one of those is a defect they can name, quantify, and point at a page about. That is
what separates an Author from somebody who can turn a handle: not that the model is right,
but that they know exactly which of its parts are load-bearing and which are assumptions
somebody made on a Tuesday.

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_rebuild.py     # 676 exact-rational assertions, exits 0
```

The script rebuilds the entire model from the raw spreadsheet in `fractions.Fraction`:
the two standardisations and their exact standard deviations; the Gram matrix, its
determinants and the VIF; all five monthly solves, done twice (by the `/10` shortcut and by
Gaussian elimination) and agreeing; all fifteen balance conditions; the thirty misses; `F`
by mean-subtracted sample covariance with divisor `T − 1`, its volatilities, correlations,
leading minors and determinant; `D` under three divisor conventions plus Level 6's leverage
correction, with `Σh = k = 3` checked exactly; all thirty-six cells of `V`, its symmetry,
the singularity of `X F Xᵀ` and the non-singularity of `V`; the book's exposures, both
routes to `81/4`, and the factor/specific split; the active book, both routes to `169/100`,
the 50.1479/49.8521 split, the index's own risk, the `Var(p) = Var(b) + 2Cov + Var(a)`
identity and the beta; the five realised book returns and their exact split into factor
and specific parts; all six risk contributions and marginal contributions, summing to
100%; and every trap in Section 12 with the exact number it returns — including the proof
that the un-standardised path reproduces `X F Xᵀ` cell for cell and lands on exactly
`81/4`, the identity `wᵀSw = ` the realised sample variance, and the exact zero determinant
of the six-asset sample covariance matrix.

If any printed value ever disagrees with this markdown, the markdown is wrong.
