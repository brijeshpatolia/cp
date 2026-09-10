# Level 4 — The Collision

Every number below is recomputed in exact rational arithmetic by `tools/verify_level4.py`
(277 assertions, exits 0). Nothing here is rounded by hand. Where a decimal does not
terminate it is written with the word **rounded** next to it; every other decimal on this
page is exact.

> **Difficulty warning, stated up front because the rulebook demands it.**
> This is the first genuinely **graduate-level** level in the game. What is built here —
> multicollinearity, partialling out, the Frisch–Waugh–Lovell theorem, ill-conditioning —
> is first-year PhD econometrics. It is normally taught *after* matrix algebra and *after*
> probability, and it is normally taught badly, as three unrelated facts.
> It is being built here with nothing but fractions and five stocks, which is harder work
> but produces a better understanding. If the player finds this level heavy, that is
> correct calibration, not failure. Tell them so, once, and keep going.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the cold-open column, which is reused here unchanged:

```
x = [−1.5, −0.5, 0, +1, +2]     Σx = 1     Σx² = 15/2     (both already known cold)
```

**From Level 1** — one column, one dial: `b = Σxr / Σx²`, derived by nudging.

**From Level 2** — the miss `e = r − b·x`, and the balance condition `Σx·e = 0`, read as a
turning force about a pivot. The balance is an *audit*: it is forced by the arithmetic of
minimising, so a file that fails it is a broken file.

**From Level 3** — two columns need **two** balance conditions holding **simultaneously**:

```
Σ x₁·e = 0        and        Σ x₂·e = 0
```

which, written out with `e = r − b₁x₁ − b₂x₂`, is a 2×2 linear system:

```
A·b₁ + B·b₂ = p          where   A = Σx₁²    B = Σx₁x₂    p = Σx₁r
B·b₁ + C·b₂ = q                  C = Σx₂²                 q = Σx₂r
```

Level 3 solved one of these by hand and stopped. **Level 4 is about what that solution
means and when it stops being trustworthy.** Three new things:

| | What Level 4 adds |
|---|---|
| **A meaning for `b₁`** | Not "the effect of column 1". It is *what column 1 explains that column 2 has not already explained* — and that sentence is not a slogan, it is an exact arithmetic identity that will be verified numerically in Section 6. |
| **A failure mode** | The obvious shortcut — fit each column on its own and report both answers — is not slightly wrong. On the boss-round data it returns a coefficient with **the wrong sign**. |
| **A health number** | `det = AC − B²` — this is Level 3's `D`, renamed to match the letters above. Level 3 built it and moved on; Level 4 is what it is *for*. When it shrinks, the *fit* stays perfect and the *split* becomes garbage. When it hits zero, there is no answer at all. |

Say all of this to the player before starting, or they will think Level 4 is Level 3 again.

---

## 1. The story (no mathematics)

Two flatmates, Ravi and Sunil, share a flat and an electricity bill. Each has an electric
heater in his own room. The landlord sees only one number each month: the total bill.

The landlord wants to know how expensive each heater is to run, because he is thinking of
replacing one of them.

**Case one.** Ravi and Sunil are inseparable. They come home together, switch both heaters
on together, go out together, switch both off together. Twelve months of bills arrive. The
landlord can predict next month's bill perfectly from "how many hours were the heaters on".
But ask him which heater is the expensive one and he has nothing. Every single bill was
produced by *both* heaters running. There is no month in the file where one ran without the
other. The **total** is knowable; the **split** is not — not because the data is noisy, but
because the question was never asked of the data.

**Case two.** One weekend Sunil goes to his cousin's wedding. Ravi stays and runs his heater
alone. That single weekend is now the *only* piece of the file that speaks about Ravi's
heater by itself, and the landlord's entire estimate of the split rests on it. If that
weekend was cold, or if the meter reader was sloppy, the whole split is wrong — while the
prediction of the total bill remains excellent.

**Case three.** They differ constantly: different schedules, different habits, weeks apart.
Now the file is full of evidence about each heater separately, and the split is solid.

Three things fall out of the story, and they are the whole level:

1. **The split lives entirely in the disagreements.** Days the two behaved identically carry
   no information about who is expensive. Only the days they differed do.
2. **Fewer disagreements do not make the prediction worse. They make the split wilder.**
   In case one the landlord predicts the bill perfectly and cannot answer the question at all.
3. **The naive reading blames the wrong heater.** "Bills are high when Ravi's heater is on"
   is true in every case above — including the case where Sunil's heater is the monster and
   Ravi's is efficient, because Sunil's was on at the same time.

---

## 2. Mapping the story onto the fit, line by line

| In the story | In the fit |
|---|---|
| a month's bill | a stock's return `r` |
| hours Ravi's heater ran | that stock's score on column 1, `x₁` |
| hours Sunil's heater ran | that stock's score on column 2, `x₂` |
| cost per hour of Ravi's heater | `b₁` |
| cost per hour of Sunil's heater | `b₂` |
| "they always run together" | `x₂` is a multiple of `x₁` — the columns are the same column |
| the weekend Sunil was away | the assets where the two columns **disagree** |
| the landlord predicts the total bill well | small `Σe²`, high explained share |
| the landlord cannot split the bill | `b₁` and `b₂` are huge, opposite, unstable |
| how much they disagree, as one number | `det = AC − B²` |

The last row is the one to hold onto. `det` is a scoreboard for "how much did Sunil go away".

---

## 3. The dataset

Same five names. The cheapness column is the **identical** column from the cold open — the
player already knows `Σx² = 15/2` without computing it. The desk has now added a second
characteristic, an analyst **quality score**, and a fresh month of returns.

| Stock | cheapness `x₁` | quality `x₂` | return `r` |
|---|---:|---:|---:|
| AXL | −1.5 | −1 | −4.0% |
| BRN | −0.5 | −1 | +2.0% |
| CHR | 0.0 | 0 | +1.0% |
| DLT | +1.0 | +1 | +3.0% |
| EMK | +2.0 | +2 | +1.0% |

Look at the two columns before doing any arithmetic. **They agree on CHR, DLT and EMK
exactly, and disagree only on AXL and BRN.** Those two names are the weekend Sunil was away.
Make the columns agree there too and there is no split left to find at all — that is Section
7d. Section 6a will show something sharper: on this dataset `b₁` depends on **nothing but
AXL's and BRN's two returns**. Change DLT's return or EMK's and `b₂` moves; `b₁` does not
move by a hair. (`b₂` is not so clean — it uses all five names. The asymmetry is real and
Section 6b shows where it comes from.)

The five numbers that run the whole level:

```
A = Σx₁² = 9/4 + 1/4 + 0 + 1 + 4              = 15/2        (Level 0 already had this)
B = Σx₁x₂ = 3/2 + 1/2 + 0 + 1 + 4             = 7
C = Σx₂²  = 1 + 1 + 0 + 1 + 4                 = 7
p = Σx₁r  = 6 − 1 + 0 + 3 + 2                 = 10
q = Σx₂r  = 4 − 2 + 0 + 3 + 2                 = 7
                                       Σr²   = 31
```

**Predict-then-reveal, before any solving.** Ask the player: the two columns are nearly the
same column, and each of them has a clearly positive relationship with return. Commit to a
rough size and sign for `b₁` and `b₂` — *with a reason*. Almost every player says "both
smallish and positive, maybe 1 to 2 each". Write the guess down. It will be wrong by a
factor of about five and by a sign.

---

## 4. The correct answer, twice, by hand

### 4a. Cramer's rule (the formula from Level 3)

```
det = A·C − B² = (15/2)(7) − 7²  =  105/2 − 49  =  7/2  =  3.5

b₁ = (C·p − B·q) / det = (7·10 − 7·7) / (7/2) = 21 / (7/2) = 6
b₂ = (A·q − B·p) / det = ((15/2)·7 − 7·10) / (7/2) = (−35/2) / (7/2) = −5
```

**`b₁ = +6`, `b₂ = −5`.** Not 1 to 2 each. Two large coefficients of opposite sign on two
columns that look nearly identical. And note:

```
b₁ + b₂ = 1
```

Hold that number. Section 7 shows it is the only part of the answer that is actually stable.

### 4b. The same thing by elimination, which shows *where* the 6 comes from

Write the two balance equations out:

```
(15/2)·b₁ + 7·b₂ = 10          (balance against cheapness)
    7·b₁ + 7·b₂ = 7            (balance against quality)
```

The second divides by 7 on sight:

```
b₁ + b₂ = 1
```

Substitute `b₂ = 1 − b₁` into the first:

```
(15/2)·b₁ + 7(1 − b₁) = 10
(15/2 − 7)·b₁ = 10 − 7
    (1/2)·b₁ = 3
          b₁ = 3 / (1/2) = 6            and     b₂ = 1 − 6 = −5
```

**This is the sentence the whole level turns on.** Look at the number multiplying `b₁` after
the elimination: `1/2`. It started life as `A = 15/2`. Eliminating `b₂` destroyed fourteen
fifteenths of it, because column 2 had already claimed that much of column 1. A right-hand
side of `3` divided by a leftover of `1/2` is what produces a coefficient of `6`.

The general version of that shrunken number is the determinant. Doing the elimination
symbolically, `C·(eq 1) − B·(eq 2)` gives

```
(A·C − B²)·b₁ = C·p − B·q       i.e.      det · b₁ = 21,   det = 7/2,   b₁ = 6
```

**The determinant is the pivot.** It is the number you end up dividing by. Everything else
in this level is a consequence of that one fact.

### 4c. The audit (Level 3's, run without being asked)

```
fitted = 6·x₁ − 5·x₂ = [−4, +2, 0, +1, +2]
e = r − fitted        = [ 0,  0, +1, +2, −1]

Σx₁·e = 0·(−3/2) + 0·(−1/2) + 1·0 + 2·1 + (−1)·2 = 0     ✓ balance 1
Σx₂·e = 0·(−1)   + 0·(−1)   + 1·0 + 2·1 + (−1)·2 = 0     ✓ balance 2
Σe    = 2   ← still not zero. No intercept yet. Level 5.
Σe²   = 6
Σfitted² = 25        and     25 + 6 = 31 = Σr²    ✓ the decomposition closes
```

Explained share `25/31` = **80.65% (rounded)**. Remember that number; the naive method is
about to destroy it.

`Σe = 2` is the same `Σe = 2` from the cold open, and for the same reason: neither column
is a column of ones, so nothing forces the misses to cancel. Level 5.

---

## 5. The wrong answers, and exactly what each one returns

These are not straw men. Every one of them is what a capable person actually does when they
meet a second column for the first time.

### 5a. ONE-AT-A-TIME — run Level 1's formula twice

```
b₁ᵒⁿᵉ = p / A = 10 / (15/2) = 4/3 = 1.3333 (rounded)
b₂ᵒⁿᵉ = q / C = 7 / 7       = 1
```

Against the truth `(+6, −5)`:

| | true | one-at-a-time | how wrong |
|---|---:|---:|---|
| `b₁` | **+6** | +4/3 | **4.5× too small** (`6 ÷ 4/3 = 9/2`) |
| `b₂` | **−5** | **+1** | **sign flipped**, and 5× too small in size |

The one-at-a-time answer says quality is *rewarded*. The joint fit says quality is the
second-strongest force in the data and it is *punished*. That is not a rounding difference;
it is the opposite conclusion.

**Why the audit kills it instantly.** Fit `4/3·x₁ + 1·x₂` and look at the misses:

```
one-at-a-time fitted = [−3, −5/3, 0, 7/3, 14/3]
misses               = [−1, 11/3, 1, 2/3, −11/3]

Σx₁·miss = −7        ← should be 0
Σx₂·miss = −28/3     ← should be 0
```

Both planks are tipped. Level 2 and Level 3 already gave the player the test that rejects
this answer without knowing the right one. **That is what the balance conditions are for.**

**What it costs, in Level 0's currency.**

```
SS(4/3, 1) = 88/3  = 29.3333 (rounded)
SS(6, −5)  = 6
ratio      = 44/9  = 4.8889  (rounded)
SS(0, 0)   = Σr² = 31        ← predicting zero for everybody
```

Read that last line twice. **Giving up entirely and forecasting 0% for all five stocks
scores 31. The one-at-a-time answer scores 29.33 (rounded).** It captures

```
31 − 88/3 = 5/3      of the 31 available, i.e. 5/93 = 5.38% (rounded)
```

against the correct fit's `25/31 = 80.65% (rounded)`. Of the 25 that was actually there to
be found, the naive method found `5/3` — one fifteenth — and threw away the other fourteen
fifteenths, `93.3% (rounded)`, while reporting two confident-looking numbers. Hold the
fraction `1/15`: Section 7b shows it is not a coincidence of this dataset.

The split of `SS` into two exact pieces, so no step is unexplained. With
`δ₁ = 4/3 − 6 = −14/3` and `δ₂ = 1 − (−5) = +6`:

```
excess = A·δ₁² + 2B·δ₁δ₂ + C·δ₂²
       = (15/2)(196/9) + 2(7)(−14/3)(6) + 7(36)
       = 490/3 − 392 + 252  =  70/3
SS(naive) = SS(min) + excess = 6 + 70/3 = 88/3     ✓
```

That identity — *the extra loss is a quadratic form in how far you are from the answer* — is
the two-column version of Level 1's parabola, and it is where Level 6's standard errors will
come from.

### 5b. SEQUENTIAL — fit column 1, then fit the leftover *return* on column 2

This is the sophisticated wrong answer, and it is nearly right. It is what a careful person
invents when they realise one-at-a-time double-counts.

```
step 1:  b₁ = p/A = 4/3
         leftover return  r − (4/3)x₁ = [−2, 8/3, 1, 5/3, −5/3]
step 2:  regress that leftover on x₂ (raw x₂):
         Σ x₂ · leftover = −7/3
         b₂ˢᵉ𐞥 = (−7/3) / C = (−7/3)/7 = −1/3
```

`(4/3, −1/3)`. The **sign is now right**. The size is not: the truth is `−5`.

```
true b₂ / sequential b₂ = (−5) / (−1/3) = 15
```

**Fifteen. Exactly.** Not approximately. And 15 is `A·C/det = (15/2)(7)/(7/2)` — a quantity
that has now appeared twice and will be named in Section 7, not before. This is a general
theorem, proved in Section 6c and brute-forced over 3,983 datasets by the verifier: *the
sequential method understates the second coefficient by exactly the factor `A·C/det`,
always.* It is the cleanest possible statement of what the shortcut leaves out.

`SS(4/3, −1/3) = 152/9 = 16.8889 (rounded)`.

### 5c. DROP ONE COLUMN

```
keep cheapness only:  b = 4/3,   SS = Σr² − p²/A = 31 − 100/(15/2) = 53/3 = 17.6667 (rounded)
keep quality only:    b = 1,     SS = Σr² − q²/C = 31 − 49/7       = 24
```

Worth showing because it is the honest fallback, and because it beats one-at-a-time
(`53/3 = 17.6667 < 88/3 = 29.3333`, both rounded). **Dropping a column is a defensible
response to a collision. Reporting two one-at-a-time numbers is not.**

### 5d. The full scoreboard

| method | `b₁` | `b₂` | `SS` | `SS` (rounded) |
|---|---:|---:|---:|---:|
| **joint, both columns at once** | **6** | **−5** | **6** | 6.000 |
| sequential (leftover return on raw `x₂`) | 4/3 | −1/3 | 152/9 | 16.889 |
| drop quality | 4/3 | — | 53/3 | 17.667 |
| drop cheapness | — | 1 | 24 | 24.000 |
| **one-at-a-time** | 4/3 | **+1** | **88/3** | **29.333** |
| give up, predict 0 for everyone | 0 | 0 | 31 | 31.000 |

The method a beginner reaches for first is the second-worst thing on the list, and it beats
doing nothing at all by a margin of only `31 − 88/3 = 5/3 = 1.6667 (rounded)`.

---

## 6. What a coefficient actually means — build it, then name it

This is the heart of the level. The claim:

> `b₁` is not "the effect of cheapness". It is **what cheapness explains that quality has
> not already explained**, divided by **how much of cheapness is left over after quality
> has taken its share.**

That is a sentence about arithmetic, and it can be checked to the last fraction.

### 6a. Do it in the easy direction first

**Step 1 — ask how much of cheapness quality can already account for.** Fit one column to
the other, using Level 1's formula with `x₂` playing the role of the exposure and `x₁`
playing the role of the "return":

```
slope of x₁ on x₂  =  Σx₁x₂ / Σx₂²  =  B / C  =  7 / 7  =  1
```

Quality reproduces cheapness at a rate of exactly 1-for-1.

**Step 2 — take the leftover.**

```
w = x₁ − 1·x₂ = [−3/2 − (−1), −1/2 − (−1), 0 − 0, 1 − 1, 2 − 2]
              = [−1/2, +1/2, 0, 0, 0]
```

**Look at what survived: AXL and BRN, and nothing else.** Exactly the two names the two
rulers disagreed about. The rest of column 1 was, arithmetically, already inside column 2.
This is the weekend Sunil was away, computed rather than noticed.

Two checks:

```
Σ x₂·w = (−1)(−1/2) + (−1)(1/2) + 0 + 0 + 0 = 0    ✓ nothing of quality remains in w
Σ w²   = 1/4 + 1/4 = 1/2                            and   det/C = (7/2)/7 = 1/2   ✓
```

`Σw² = det/C` is not a coincidence and it is where the determinant gets its meaning
(Section 7).

**Step 3 — fit the return on the leftover, with Level 1's formula, one column, no tricks.**

```
Σ w·r = (−1/2)(−4) + (1/2)(2) + 0 + 0 + 0 = 2 + 1 = 3

b₁ = Σw·r / Σw² = 3 / (1/2) = 6          ← the joint answer, recovered exactly
```

**Six.** Identical to the two-column solve in Section 4, obtained by a one-column
calculation the player has been able to do since Level 1.

*(Optional refinement, also exact: you may strip quality out of the return first, using
`r − 1·x₂`, and the numerator is unchanged at 3 — because `w` has no quality left in it, so
subtracting a multiple of `x₂` cannot change `Σw·r`. Both versions are verified.)*

### 6b. The same thing in the other direction

```
slope of x₂ on x₁ = B / A = 7 / (15/2) = 14/15
v = x₂ − (14/15)x₁ = [2/5, −8/15, 0, 1/15, 2/15]

Σ x₁·v = 0                                   ✓
Σ v²   = 7/15         and   det/A = (7/2)/(15/2) = 7/15    ✓
Σ v·r  = (−24 − 16 + 0 + 3 + 2)/15 = −35/15 = −7/3

b₂ = (−7/3) / (7/15) = −5                    ← recovered exactly
```

**This construction has a name, unlocked now that it has been built: the
Frisch–Waugh–Lovell theorem.** It is one of the most useful facts in applied statistics and
one of the least often explained. The verifier checks it on 4,092 datasets; it never fails.

### 6c. And now the sequential method's error is obvious

Compare, on the main dataset:

```
sequential:      numerator  Σ x₂ · (r − (4/3)x₁) = −7/3      denominator  C     = 7
Frisch–Waugh:    numerator  Σ v  · (r − (4/3)x₁) = −7/3      denominator  Σv²   = 7/15
```

**The numerators are identical.** The sequential method gets the top of the fraction exactly
right — it correctly strips column 1 out of the *return*. Its single error is the bottom:
it divides by the *whole* of column 2, when the only part of column 2 that did any work was
the leftover `v`. The ratio of the two denominators is

```
C / Σv² = 7 / (7/15) = 15
```

and that is why the sequential answer is exactly 15 times too small. One forgotten
residualisation, one exact factor.

### 6d. What this buys the player, stated plainly

- A regression coefficient is always a **partial** quantity. There is no such thing as
  "the effect of a column" without saying *holding what else fixed*.
- The denominator of a coefficient is not the size of the column. It is the size of the
  column's **leftover**. Collinearity attacks coefficients through their denominators.
- Two columns that agree everywhere leave a leftover of zero, and a zero denominator is not
  a large answer — it is no answer.

---

## 7. The determinant, and what happens when it goes to zero

### 7a. Three readings of the same number

```
det = A·C − B²
```

| Reading | On this dataset |
|---|---|
| **the pivot** — the number left multiplying `b₁` after `b₂` is eliminated (Section 4b) | `det·b₁ = 21`, so `b₁ = 21 ÷ 3.5 = 6` |
| **the leftover size** — `det = A · Σv² = C · Σw²` : "size of one column × size of what's left of the other" | `(15/2)(7/15) = 7/2` and `7·(1/2) = 7/2` |
| **the disagreement gap** — `det = A·C·(1 − cos²θ)`, where `cosθ = B/√(AC)` measures how parallel the columns are | `cos² = 49/(105/2) = 14/15`, `1 − cos² = 1/15`, `(15/2)(7)(1/15) = 7/2` |

All three are verified identically on hundreds of datasets by the script. `det ≥ 0` always
(that is the Cauchy–Schwarz inequality), and `det = 0` exactly when one column is a multiple
of the other.

The reciprocal of that last bracket has a name that the paper itself uses, so it is worth
earning here:

```
VIF = 1 / (1 − cos²θ) = A·C / det = (15/2)(7) / (7/2) = 15
```

On this dataset the VIF is **15**, and it has shown up three times already without being
named: it is `A ÷ Σw²`, it is `C ÷ Σv²`, and it is the exact factor by which the sequential
method understates `b₂`.

> **Honesty note.** The textbook variance inflation factor is computed after centring each
> column (subtracting its mean), because a textbook regression carries an intercept. There
> is no intercept in this game yet — that is Level 5 — so everything here is the
> **uncentred** version. The arithmetic and the meaning are identical; only the pivot point
> moves. Tell the player this now, so they are not ambushed by the discrepancy later.

### 7b. A fourth, sharper reading — VIF is a ratio of *explained variation*

The verifier proves the following identity on every dataset it sweeps (4,092 of them, zero
failures), and it is two lines of algebra:

```
variation explained by the joint fit    = (C·p² − 2B·p·q + A·q²) / det
variation explained by one-at-a-time    = (C·p² − 2B·p·q + A·q²) / (A·C)
```

Same numerator. Therefore

```
explained(joint) = VIF × explained(one-at-a-time)          exactly, always
```

Check it on the main dataset: `25 = 15 × 5/3`. ✓
Check it on the boss dataset in Section 12: `20 = 10 × 2`. ✓

So the VIF is not an abstract diagnostic. **It is the exact multiple by which the naive
method under-explains the data.** A VIF of 15 means one-at-a-time will find one-fifteenth of
what is there.

### 7c. Now push the columns together and watch

Define the disagreement direction and slide the quality column along it:

```
d = x₂ − x₁ = [+1/2, −1/2, 0, 0, 0]          x₂(t) = x₁ + t·d
```

`t = 1` is the dataset above. `t = 1/2` halves the disagreement between AXL and BRN.
`t = 0` makes the quality column *identical* to the cheapness column.

Three facts, provable in two lines each, and then a table.

**Fact 1 — the determinant falls with the square of `t`.**
With `S = Σx₁·d = −1/2` and `D = Σd² = 1/2`:

```
B(t) = A + tS                     C(t) = A + 2tS + t²D
det(t) = A·C − B² = t²·(A·D − S²) = t²·((15/2)(1/2) − 1/4) = (7/2)·t²
```

Halve the disagreement, **quarter** the determinant.

**Fact 2 — the fit does not change at all.**
`x₂(t) = x₁ + t·d`, so any combination `b₁x₁ + b₂x₂(t)` equals `(b₁+b₂)x₁ + (t·b₂)d`. For
every `t ≠ 0` the two columns span the *same* two directions, `x₁` and `d`. The best
achievable prediction is therefore identical for every `t`, and so are the misses and `Σe²`.

**Fact 3 — the split explodes like `1/t`.**
Matching the two ways of writing the fitted vector, `b₁ + b₂ = c₁` and `t·b₂ = c₂`, where
`c₁` and `c₂` do not depend on `t`. At `t = 1` we found `b₁ + b₂ = 1` and `b₂ = −5`, so
`c₁ = 1` and `c₂ = −5`, giving

```
b₂(t) = −5/t             b₁(t) = 1 + 5/t             b₁ + b₂ = 1  for every t ≠ 0
```

| `t` | quality of AXL | quality of BRN | `det` | `cosθ` (rounded) | `VIF` (rounded) | `b₁` | `b₂` | `b₁+b₂` | `Σe²` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | −1 | −1 | 7/2 = 3.5 | 0.966092 | 15 | 6 | −5 | 1 | 6 |
| 1/2 | −1.25 | −0.75 | 7/8 = 0.875 | 0.991779 | 61.07 | 11 | −10 | 1 | 6 |
| 1/4 | −1.375 | −0.625 | 7/32 = 0.21875 | 0.997995 | 249.64 | 21 | −20 | 1 | 6 |
| 1/10 | −1.45 | −0.55 | 7/200 = 0.035 | 0.999685 | 1586.79 | 51 | −50 | 1 | 6 |
| 1/100 | −1.495 | −0.505 | 7/20000 = 0.00035 | 0.999997 | 160501.07 | 501 | −500 | 1 | 6 |

*(Exact VIFs: 15, 855/14, 3495/14, 22215/14, 2247015/14. The `det` decimals terminate and
are exact; the `cosθ` and `VIF` decimals are rounded.)*

**Read the table across, then down.** Down the `b₁` and `b₂` columns: numbers running away to
±500 on data where every return is between −4% and +3%. Down the `Σe²` column: 6, 6, 6, 6, 6.
Down the `b₁+b₂` column: 1, 1, 1, 1, 1.

> **The one sentence of this level.** Collinearity does not damage the model's predictions.
> It damages the model's **attribution**. The forecast is untouched; the story about *why*
> becomes nonsense.

For the sceptic, `t = 1/2` done the long way, assuming nothing:

```
x₂(1/2) = [−5/4, −3/4, 0, 1, 2]
A = 15/2        B = 15/8 + 3/8 + 0 + 1 + 4 = 29/4        C = 25/16 + 9/16 + 0 + 1 + 4 = 57/8
det = (15/2)(57/8) − (29/4)² = 855/16 − 841/16 = 14/16 = 7/8              ✓ = (7/2)(1/4)
p = 10 (unchanged)          q = 5 − 3/2 + 0 + 3 + 2 = 17/2
b₁ = (C·p − B·q)/det = (570/8 − 493/8)/(7/8) = 77/7 = 11                  ✓
b₂ = (A·q − B·p)/det = (255/4 − 290/4)/(7/8) = (−35/4)(8/7) = −10         ✓
fitted = 11·x₁ − 10·x₂(1/2) = [−4, +2, 0, +1, +2]                         ✓ identical
```

And the naive method at `t = 1/2` still says quality pays:
`b₂ᵒⁿᵉ = q/C = (17/2)/(57/8) = 68/57 = 1.1930 (rounded)`, against a truth of `−10`.

How much does that pair explain? Section 7b's closed form answers it without fitting
anything:

```
C·p² − 2B·p·q + A·q² = (57/8)(100) − 2(29/4)(10)(17/2) + (15/2)(289/4)
                     = 5700/8 − 9860/8 + 4335/8  =  175/8
explained(one-at-a-time) = (175/8) / (A·C) = (175/8) / (855/16) = 70/171
SS = Σr² − explained = 31 − 70/171 = 5231/171 = 30.5906 (rounded)
```

Against `31` for predicting zero for every stock, the naive two-column answer is now better
than doing nothing at all by `70/171 = 0.4094 (rounded)`. The tighter the collision, the
closer the naive answer gets to being worth precisely nothing.

### 7d. `t = 0` exactly: the cliff

Set the quality column equal to the cheapness column. Then:

```
A = C = B = 15/2          det = (15/2)² − (15/2)² = 0
```

Cramer's rule now divides by zero, and the two balance equations have collapsed into one:

```
(15/2)·b₁ + (15/2)·b₂ = 10        i.e.       b₁ + b₂ = 4/3
```

**Every** pair on that line fits equally well. The verifier checks four of them —
`(4/3, 0)`, `(0, 4/3)`, `(100, −296/3)`, `(−1000, 3004/3)` — and all four return

```
SS = 53/3 = 17.6667 (rounded)
```

Two things a sharp player will notice, and both are worth full bps:

1. **There is no "very large answer" at `t = 0`.** For tiny `t` the answers are enormous;
   at `t = 0` they are *absent*. Different failures. A computer will not report absence — it
   will report whatever the round-off in its arithmetic happens to produce, which is why
   real risk systems check the determinant instead of trusting the output.
2. **The limit is discontinuous, and the fit actually gets worse.** For every `t > 0`,
   `b₁ + b₂ = 1` and `Σe² = 6`. At `t = 0` exactly, `b₁ + b₂ = 4/3` and the best possible
   `Σe² = 53/3 = 17.6667 (rounded)` — the fit is `53/18 = 2.9444 (rounded)` times worse,
   because a whole direction of explanation (`d`, the disagreement) has vanished from the
   design. Near-collinearity costs you nothing in fit and everything in attribution;
   *perfect* collinearity costs you the fit as well.

---

## 8. Instability — the thing a desk actually feels

The table in 7c is static. A working model is refitted every day on data that moves. Take
the main dataset and change **one number**: BRN's return, from +2.0% to +3.0%. One stock,
one percentage point. Nothing else.

| `t` | `b₁` before → after | `b₁` change | `b₂` before → after | `b₂` change | change in `b₁+b₂` |
|---:|---|---:|---|---:|---:|
| 1 | 6 → 7 | +1 | −5 → −43/7 | −8/7 | −1/7 |
| 1/2 | 11 → 92/7 | +15/7 | −10 → −86/7 | −16/7 | −1/7 |
| 1/4 | 21 → 178/7 | +31/7 | −20 → −172/7 | −32/7 | −1/7 |

The `b₂` responses are `−8/7`, `−16/7`, `−32/7`: **exactly doubling each time the columns
are pushed twice as close.** And the last column never moves: the *sum* responds by `−1/7`
at every tightness, because the sum is a property of the span, which `t` does not touch.

This is the concrete meaning of the phrase the BFRE paper uses on p.32 — *"significant
instability in the factor return estimates through time"*. It is not vagueness. It is
`1/t`.

---

## 9. Traps, and what each wrong belief returns numerically

| Wrong belief | What it produces here | The one-line refutation |
|---|---|---|
| "Two columns, so run the formula twice." | `(4/3, +1)` — sign wrong on `b₂` | `Σx₁·miss = −7`, `Σx₂·miss = −28/3`. Fails Level 3's audit. |
| "The columns are almost the same, so the answers will be almost the same." | truth `(6, −5)`, and they sum to 1 | Nearly-equal columns force *opposite* coefficients, not equal ones. |
| "Big coefficients mean big effects." | `b₁ = 501` at `t = 1/100` | Same prediction as `b₁ = 6`. Size here measures ill-conditioning, not importance. |
| "High correlation ruins the forecast." | `Σe² = 6` at every `t > 0` | The forecast is untouched. Only the split breaks. |
| "If the fit is good, the coefficients are trustworthy." | 80.65% explained (rounded) at every `t` | Explained share says nothing at all about whether the split is identified. |
| "Small determinant? Just delete one of the columns." | `SS` 6 → 53/3 (17.6667, rounded) | Legitimate, but it costs real fit. Say what you are paying. |
| "Fit `x₁`, then fit the leftover return on `x₂`." | `(4/3, −1/3)` | Right sign, exactly `VIF = 15` times too small. Residualise the *column* too. |
| "Both coefficients could have the wrong sign." | never happens | See 9a. |
| "det = 0 gives huge coefficients." | it gives *none* | At `t = 0` every pair with `b₁+b₂ = 4/3` is equally optimal. |

### 9a. A thing that *cannot* go wrong (worth teaching, because it bounds the damage)

**At most one of the two one-at-a-time coefficients can have the wrong sign.**

Proof. A wrong sign on column 1 means `b₁·(p/A) < 0`. Since `p = A·b₁ + B·b₂`, that is
`A·b₁² + B·b₁b₂ < 0`, i.e. `B·b₁b₂ < −A·b₁²`. Likewise a wrong sign on column 2 requires
`B·b₁b₂ < −C·b₂²`. Both right-hand sides are negative, so both would force `B·b₁b₂ < 0`;
multiplying the two inequalities (both sides negative, so the product inequality flips into
`>`) gives

```
B²·b₁²b₂²  >  A·C·b₁²b₂²      ⟹      B² > A·C      ⟹      det < 0
```

which is impossible, because `det ≥ 0` always. The verifier sweeps 4,092 datasets: 849 have
exactly one sign flip, **zero** have two. ∎

Use this in the boss round. A player who claims "both my numbers might be backwards" is
wrong, and can be shown why in four lines.

---

## 10. Names unlocked at the end of this level

Locked until now on purpose — except the two marked *(recalled)*, which were unlocked in
earlier levels and turn up here in new clothes. Say so when they do; a name the player
already owns, reappearing in a bigger setting, is a call-back to make out loud, not a fresh
unlock to hand over twice. Each name below is attached to something the player built.

| Name | What it actually is, in this level's terms |
|---|---|
| **multicollinearity** | two columns that nearly agree, so `det` is small |
| **orthogonal** *(recalled — Level 2's word, applied between two columns in Level 3)* | `Σ u·v = 0` — e.g. `Σx₂·w = 0`, "no quality left in the leftover" |
| **to partial out / partialling** | subtracting from one column what another column can already reproduce, i.e. building `w` or `v` |
| **partial regression coefficient** | what every coefficient in a multi-column fit already is: an effect *holding the other columns fixed* |
| **Frisch–Waugh–Lovell theorem** | Section 6: residualise the column, residualise (optionally) the return, run a one-column fit, get the identical number |
| **determinant** *(recalled — Level 3's `D`, written `det` here)* | the pivot; `A·C − B²`; the disagreement gap |
| **singular / ill-conditioned** | `det = 0` / `det` small |
| **identification** | whether the data can distinguish the split at all. At `t = 0` the model is *not identified* |
| **variance inflation factor (VIF)** | `A·C/det`; how much the leftover denominator shrank; the exact factor the naive method loses by |

Rule F round: hand the player *"the two style exposures are collinear so the factor returns
aren't identified"* and require plain English plus a fresh sentence of their own.

---

## 11. Difficulty, honestly

- Sections 1–5 are hard but ordinary — arithmetic the player can already do, in a new shape.
- **Section 6 (Frisch–Waugh) is graduate material.** It is normally proved with projection
  matrices. Here it is one column of fractions. If a player derives it unaided, they are
  ahead of most first-year PhD students.
- **Section 7d (the discontinuity at `t = 0`) is genuinely subtle** and it is acceptable for
  a player to reach tier 3 (derive) and not tier 4 (defend) on it this level.
- The thing that is *not* optional: the player must be able to say, unprompted, that a
  coefficient is a leftover. Everything downstream — `F`, the two-pass structure, the
  critique in Level 12 — assumes it.

---

# 12. BOSS ROUND — The Collision

Round type: **E. INTERROGATION**, with a **B. SABOTAGE** opening. Play a Chief Risk Officer
with thirty years on the desk who has been handed a research note and does not believe it.

## 12.1 The setup, as the player receives it

> *A junior researcher has sent you this note. The firm is about to switch its value screen
> on the strength of it. You have twenty minutes.*
>
> **"Value does not work in this universe."**
> *"I regressed one month of returns on our value score across the estimation universe. The
> coefficient is **−1.0% per unit of value exposure**. Cheap stocks lost money. I also ran
> the quality score separately: **−2.0% per unit**. Both screens are destroying value and I
> recommend we invert the value signal."*

The data behind the note — a fresh five-name universe, both columns integer-scored:

| Stock | value `x₁` | quality `x₂` | return `r` |
|---|---:|---:|---:|
| AXL | −2 | −1 | +1.0% |
| BRN | −1 | −1 | +4.0% |
| CHR | 0 | 0 | +1.0% |
| DLT | +1 | +1 | −2.0% |
| EMK | +2 | +1 | −1.0% |

The player's task, stated as the CRO would state it: **"Tell me whether to invert the value
signal, and show me your arithmetic. If you tell me his number is 'a bit off' I will end the
meeting."**

## 12.2 The five cross-products (thirty seconds by hand)

```
A = Σx₁² = 4 + 1 + 0 + 1 + 4  = 10          p = Σx₁r = −2 − 4 + 0 − 2 − 2 = −10
B = Σx₁x₂ = 2 + 1 + 0 + 1 + 2 = 6           q = Σx₂r = −1 − 4 + 0 − 2 − 1 = −8
C = Σx₂²  = 1 + 1 + 0 + 1 + 1 = 4                            Σr² = 23
```

The researcher's two numbers are confirmed immediately, and they are arithmetically correct
*as one-column fits*:

```
p / A = −10/10 = −1          q / C = −8/4 = −2
```

**He did not make a mistake. He answered a different question from the one he thinks he
answered.** That distinction is the whole boss round.

## 12.3 The health check, before the answer

```
det = A·C − B² = 40 − 36 = 4
cos²θ = B²/(A·C) = 36/40 = 9/10          cosθ = 0.948683 (rounded)
VIF   = A·C/det = 40/4 = 10
```

A VIF of 10 says: **the one-at-a-time method will find one-tenth of what is there** (Section
7b). Before solving anything, the player already knows the researcher's numbers are an order
of magnitude short.

## 12.4 The correct answer

```
b₁ = (C·p − B·q)/det = (4(−10) − 6(−8))/4 = (−40 + 48)/4 = +2
b₂ = (A·q − B·p)/det = (10(−8) − 6(−10))/4 = (−80 + 60)/4 = −5
```

**Value earns +2.0% per unit of exposure. Quality costs −5.0% per unit.**
The researcher reported value at −1.0%. **The sign is wrong.**

The audit, run before the answer leaves the desk:

```
fitted = 2·x₁ − 5·x₂ = [+1, +3, 0, −3, −1]
e = r − fitted       = [ 0, +1, +1, +1,  0]

Σx₁·e = 0 − 1 + 0 + 1 + 0 = 0     ✓
Σx₂·e = 0 − 1 + 0 + 1 + 0 = 0     ✓
Σe  = 3      Σe² = 3      Σfitted² = 20      20 + 3 = 23 = Σr²     ✓
explained = 20/23 = 86.96% (rounded)
```

And the same answer from the leftover construction, as a second, independent route
(Section 6):

```
slope of x₁ on x₂ = B/C = 6/4 = 3/2
w = x₁ − (3/2)x₂  = [−1/2, +1/2, 0, −1/2, +1/2]
Σx₂·w = 0   ✓        Σw² = 1   ( = det/C = 4/4 )        Σw·r = −1/2 + 2 + 1 − 1/2 = 2
b₁ = 2 / 1 = +2      ✓ recovered

slope of x₂ on x₁ = B/A = 6/10 = 3/5
v = x₂ − (3/5)x₁  = [+1/5, −2/5, 0, +2/5, −1/5]
Σx₁·v = 0   ✓        Σv² = 2/5 ( = det/A = 4/10 )       Σv·r = (1 − 8 − 4 + 1)/5 = −2
b₂ = (−2)/(2/5) = −5 ✓ recovered
```

Note the shrinkage the leftover reveals: column 1 started with `Σx₁² = 10` and ends with
`Σw² = 1`. **Nine-tenths of the value column was already inside the quality column.** That
ratio, `10/1`, is the VIF, and it is why the researcher's number came out ten times too
small — small enough that the residue changed sign.

## 12.5 Quantifying "catastrophically wrong" — six numbers, not one adjective

| Measure | Researcher | Truth | Exactly how wrong |
|---|---:|---:|---|
| **1. value coefficient** | −1.0% | **+2.0%** | **sign flipped.** Ratio `−1/2`. Error of 3.0 percentage points per unit of exposure |
| **2. quality coefficient** | −2.0% | −5.0% | right sign, **2.5× too small** |
| **3. sum of squared misses** | 21 | **3** | the naive pair misses **exactly 7× more** |
| **4. variation explained** | 2 of 23 | 20 of 23 | **exactly 10× less** — the VIF, as predicted before solving |
| **5. balance audit** | `Σx₁·miss = 12`, `Σx₂·miss = 6` | 0 and 0 | fails both conditions outright |
| **6. a live trade** | see below | see below | priced at **exactly 0%** instead of **+9%** |

**Measure 3, in full.** Naive fitted `= −1·x₁ − 2·x₂ = [4, 3, 0, −3, −4]`, misses
`= [−3, +1, +1, +1, +3]`, `Σmiss² = 9+1+1+1+9 = 21`, against `Σe² = 3`. Ratio **7**.
The excess splits exactly as in Section 5a, with `δ₁ = −1 − 2 = −3` and `δ₂ = −2 − (−5) = +3`:

```
A·δ₁² + 2B·δ₁δ₂ + C·δ₂² = 10(9) + 2(6)(−3)(3) + 4(9) = 90 − 108 + 36 = 18
SS(naive) = SS(min) + excess = 3 + 18 = 21     ✓
```

**Measure 4.** `23 − 21 = 2` explained by the naive pair; `20` by the correct one. Predicting
zero for every stock scores 23, so the researcher's model is worth **2 points out of 23** —
he has recommended inverting a firm-wide signal on the strength of a fit that explains
`2/23 = 8.70% (rounded)` of what is there.

**Measure 6 — the one that gets a CRO's attention.** Two names not in the estimation set:

| Name | value | quality | correct forecast | researcher's forecast |
|---|---:|---:|---:|---:|
| GRV | +2 | 0 | **+4.0%** | **−2.0%** |
| JDE | 0 | +1 | −5.0% | −2.0% |

GRV is forecast to *gain* 4% by the correct model and to *lose* 2% by the note — opposite
directions, 6 percentage points apart, on a single position. And the long-GRV/short-JDE pair:

```
correct:  (+4.0) − (−5.0) = +9.0%
note:     (−2.0) − (−2.0) =  0.0%      ← the note prices this trade at exactly zero
```

The note cannot see the trade at all. Not "underestimates it" — cannot see it.

## 12.6 The trap the good players fall into (have this ready)

A strong player will not do one-at-a-time. They will do **sequential**: fit value, take the
leftover return, fit that on quality.

```
b₁ = p/A = −1                leftover return  r − (−1)x₁ = [−1, +3, +1, −1, +1]
Σx₁·leftover = 0     ✓ balanced against value
Σx₂·leftover = −2    ✗ NOT balanced against quality — the tell
b₂ˢᵉ𐞥 = −2/4 = −1/2
```

`(−1, −1/2)`. Its `SS` is 12, better than 21 and far worse than 3. And

```
true b₂ / sequential b₂ = (−5)/(−1/2) = 10 = the VIF, exactly
```

Award full bps only if the player finds the error themselves: **the return was residualised,
the column was not.** Push them to `v = x₂ − (3/5)x₁` and make them see that the numerator
`Σv·(leftover) = −2` is unchanged — only the denominator was wrong.

## 12.7 The interrogation script (real objections, in escalating order)

1. *"His arithmetic checks out. Show me where the error is."* — It is not in the arithmetic.
   `p/A` is a correct answer to "what single number best turns value into return **when
   quality is not in the room**". The firm's question has quality in the room.
2. *"Value and quality are 0.95 correlated. Isn't one of them redundant?"*
   (`cosθ = 0.948683`, rounded.) — No. Dropping
   quality takes `Σe²` from 3 to `23 − 100/10 = 13`; dropping value takes it from 3 to
   `23 − 64/4 = 7`. The disagreements are small but they are load-bearing.
3. *"Both his numbers could be backwards then."* — Impossible. Section 9a: at most one of
   the two one-at-a-time coefficients can carry the wrong sign, because both would require
   `det < 0`.
4. *"Your `b₂ = −5` is enormous. Nothing in equities pays −5% a unit."* — Correct instinct,
   and it is the diagnostic. Large opposite-signed coefficients on near-identical columns are
   the *symptom* of a small determinant, not a finding. Point at `det = 4` against
   `A·C = 40`, and at `VIF = 10`. Then say what you would do about it: merge the two scores
   into one column, or drop one and disclose the cost. (This is exactly what BFRE did in
   EMEA — Section 14.)
5. *"So can I trust your +2 or not?"* — The honest answer, and the one that earns promotion:
   *the joint fit is the only answer that satisfies both balance conditions, so it is the
   right answer to the right question; but with `VIF = 10` its split is fragile, and I would
   report it with that caveat, not as a firm-wide signal inversion.* A player who claims the
   `+2` is bankable has not understood Section 8.

## 12.8 Pass conditions

Promote to **Researcher** only if all five hold:

1. They identify that the researcher answered a different question, not that he miscomputed.
2. They produce `(+2, −5)` by hand and run **both** balance checks before reporting.
3. They quantify the failure with at least three of the six measures in 12.5, using numbers,
   not adjectives.
4. They can state what `det = 4` against `A·C = 40` means without using the word
   "multicollinearity" as an explanation. (Naming it is fine. Naming it *instead of*
   explaining it is a bps penalty.)
5. Under objection 4 they neither defend `−5` as an economic finding nor abandon it as an
   error. It is the correct split of an ill-conditioned system, and both halves of that
   sentence are required.

**Failure protocol trigger.** If the player cannot see why `p/A` is not `b₁`, do not
re-explain Section 6. Go back to the flatmates and add a third case with numbers: bills,
hours, one weekend apart. Rebuild from the story, not from the algebra.

---

## 13. Ladder position after this level

| Concept | Target tier |
|---|---|
| two balance conditions as a 2×2 system (Level 3) | 5 — rebuild on new data |
| coefficient = leftover ("partial") | 4 — defend under attack |
| Frisch–Waugh construction, run by hand | 4 |
| determinant as pivot / leftover size / disagreement gap | 4 |
| VIF as the exact factor lost by one-at-a-time | 3 — derive |
| fit invariant, split explodes as `1/t` | 4 |
| discontinuity at exact collinearity | 3 |
| "at most one sign can flip" | 2 — compute |

---

## 14. Back to BFRE — what this machinery does in the real model

Levels 1–3 tied the *estimator* to p.24 eq. (1.7) and the weighting paragraph on p.25. This
section is different material: it is about what BFRE does when its columns collide, and the
paper is unusually explicit about it in two places and unusually quiet about it in a third.

### 14a. p.32 — the paper names this level's problem and its diagnostic

**p.32, MODEL ESTIMATION DIAGNOSTICS:** *"Several standard diagnostics were appraised during
this process to check the overall explanatory power of the models, individual factor efficacy
and also multicollinearity."* The third of the three is this level.

Verbatim, p.32: *"The final set of diagnostics are **variance inflation factors**. These help
diagnose issues relating to multicollinearity between the style factors. If style exposures
are too closely correlated then the regression procedure will encounter problems in
apportioning the factor return between them. This can result in significant instability in
the factor return estimates through time¹⁶. In order to guard against these effects,
variance inflation factors were reviewed over the research history and were found to be well
within suitable thresholds."*

Every clause of that has now been built:

| The paper's words | This level's arithmetic |
|---|---|
| "too closely correlated" | `cosθ → 1`, so `det → 0` |
| "problems in **apportioning** the factor return between them" | Section 7c: the fit is untouched (`Σe² = 6` at every `t`), only the *split* breaks — "apportioning" is precisely the right word and it is not the same word as "forecasting" |
| "significant instability … through time" | Section 8: halve the disagreement and a one-stock, one-percentage-point data change moves the split twice as far. `−8/7`, `−16/7`, `−32/7` |
| "variance inflation factors" | `VIF = A·C/det`; 15 on the main dataset, 10 on the boss dataset |

**Footnote 16, p.32:** *"In the most extreme case, where factor exposures are perfectly
correlated, identification issues will exist causing the estimation process to fail."*
That is Section 7d, exactly: `det = 0`, no unique solution, and the *estimation process
fails* rather than returning a large number.

**The honesty note the player must carry.** The notes record explicitly that **no numeric VIF
values and no numeric thresholds are printed anywhere in the paper** — "well within suitable
thresholds" is the entire quantitative content. On p.32 the paper does quote a number for the
neighbouring diagnostic (t-statistics: *"The majority of factors are significant more than
10% of time over the research history"*), which makes the silence on VIFs conspicuous rather
than accidental. That is a Level 12 entry: *a document that names its multicollinearity
diagnostic, states it passed, and never reports a single value or threshold.*

### 14b. p.26 — BFRE has an **exactly** singular design, on purpose, and says so

This is the sharpest tie-back in the level, because it is not a hypothetical.

**p.26:** *"This specification is not uniquely identified as there are an infinite number of
possible solutions. The reason for this lies in the fact that, for each asset, there exist
three intercept terms – the market factor, an industry factor, and a country factor. **Every
asset has unit exposure to these three factors.** This can be resolved by adding two linear
restrictions on the definition of the factor returns, which reduces the intercept terms from
three to one."*

Read that against Section 7d. Every asset has exposure 1 to market, 1 to its industry, 1 to
its country. Sum the industry columns and you get a column of ones. Sum the country columns
and you get the same column of ones. That is the market column. **Three parts of the design
matrix add up to each other: `det = 0` exactly, not approximately.** "Infinite number of
possible solutions" is the paper's own phrase for the line `b₁ + b₂ = 4/3` in Section 7d.

**Equation (1.10), p.26** — the fix:

```
Σ_j ω_CInd,j · f_CInd,j = 0            Σ_k ω_CCty,k · f_CCty,k = 0
```

*(The second sum is printed in the source with index `j` over a summand subscripted `k`;
`notes/chunk_19-27.md` re-verified this at 6× and records it as a typo in the original. It is
written here corrected, as `Σ_k`.)* Footnote 15 defines the average as a square-root-of-
market-capitalisation weighted return. Two restrictions, exactly enough to remove the two
redundant dimensions.

And then the sentence that this entire level exists to make comprehensible:

**p.26:** *"This identification simply represents a rotation of the factor returns. **It does
not impact the efficacy of the risk model.**"*

A player who has not done Level 4 has to take that on faith. A player who has done Section 7c
can *prove* it: the fitted vector `[−4, +2, 0, +1, +2]` and `Σe² = 6` were identical for every
`t`, while `b₁` ran from 6 to 501. Choosing a restriction picks one point on the line of
equally-good splits. It changes the attribution and cannot change the fit. The paper's claim
is true, and now the player knows *why* it is true rather than that it was asserted.

Make them say the converse too, because it is the part the paper does not spell out: since
the restriction is a free choice, **the industry and country factor returns mean nothing on
their own** — only relative to the chosen normalisation. The paper does draw out the
consequence: *"As a result of these restrictions, the industry and country factors are net of
the market factor return, which impacts their interpretation. To illustrate, if asset returns
across EMEA are mostly positive on a given day and UK assets are also up but by less than the
average return over the region, then the UK factor return will be negative."*

### 14c. p.20 — the surgical fix, performed on a live model

**p.20:** earnings yield and dividend yield are separate factors in the BFRE models **except
in the EMEA model**, where they *"were found to be highly correlated over the research
history and so were combined into a single factor, referred to as yield."*

That is objection 4 in the boss round, answered by BlackRock in production: when two columns
collide, merge them into one column and forecast the sum you can actually identify. In this
level's language, they stopped trying to estimate `b₁` and `b₂` separately and estimated
`b₁ + b₂` — the only part that was stable at every `t` in Section 7c.

**The caveat the notes attach, which the player should carry:** the evidence offered is Figure
1.15 (EMEA substyle exposure correlations, Mar 1996 – Dec 2010), whose strongest cell is
E-to-P vs Normalised E-to-P at **0.85**, while **dividend yield's correlations to the earnings
substyles are only 0.28 to 0.50**. So for the dividend-yield pairing specifically, "highly
correlated" is asserted rather than demonstrated by the figure cited. Another Level 12 entry.

### 14d. p.11 — the real collisions in the live NAMR model

**Figure 1.3, p.11 (style exposure correlations, NAMR model, Dec 2013)** gives the actual
numbers a BFRE modeller is managing:

| Pair | Correlation |
|---|---:|
| Size – Liquidity | **0.74** (the largest off-diagonal in the 12×12 matrix) |
| Earnings Yield – Profitability | 0.64 |
| Volatility – Dividend Yield | −0.46 |
| Size – Volatility | −0.36 |

Put 0.74 into this level's machinery, treating it as the `cosθ` of Section 7a:
`VIF = 1/(1 − 0.74²) = 1/(1131/2500) = 2500/1131 = 2.21 (rounded)`. That is a mild
collision — the split is still identified, but a Size coefficient's leftover denominator is
`2.21` times smaller than an uncorrelated factor's would be.

**Do not read that 2.21 as "twice as jumpy", and this is a trap worth walking the player
into.** A coefficient's *sensitivity* to a data change scales with the square root of the
`VIF`, not the `VIF` itself, because the `VIF` compares squared sizes — `A` against `Σw²` —
while a nudge in one return moves `b` linearly. Section 8 already proved it and nobody
noticed: going from `t = 1` to `t = 1/2` multiplied the `VIF` by `(855/14)/15 = 57/14 ≈ 4.07`
and multiplied the response `−8/7 → −16/7` by exactly **2**. So the honest sentence for
Size–Liquidity is: *roughly one and a half times the sensitivity* (`√2.21 = 1.49, rounded`),
not twice.

**This is a rounded, illustrative calculation on a figure-derived correlation, not a number
printed in the paper. Label it as such to the player.** BFRE reports no VIFs, so this is our
arithmetic on their correlation, nothing more.

### 14e. p.10–p.11 — the paper's substyle screen is a one-at-a-time procedure

This is where the level bites hardest, and it should be handled carefully rather than
triumphantly.

**p.10, equations (1.3) and (1.4)**, with the text *"for i = 1, 2, …, N (where N ≥ 200 is the
number of candidate substyles) we run the following two-step regression"*:

```
(1.3)   r = X_Mkt f_Mkt + Σ_{k∈CCty} X_CCty,k f_CCty,k + Σ_{j∈CInd} X_CInd,j f_CInd,j + ε
(1.4)   ε = X_subSty,i f_subSty,i + ε̃_i
```

Read (1.4) with Section 6 in hand. It is the **sequential** method of Section 5b, applied
across 200-plus candidate columns: the *return* is residualised on market, country and
industry, and then each candidate substyle is fitted **one at a time, against the raw
candidate column, with the other candidates not in the room.**

Two things are true at once and the player must hold both:

1. **It is legitimate as a screen.** Section 6c proved the sequential numerator is exactly
   right; only its denominator is inflated. The ranking of candidates by explanatory power
   against `ε` is a defensible way to shortlist from 200+, and the paper is explicit that
   this is a *selection* stage, followed by aggregation and by re-estimation with the chosen
   style inside the first-step regression.
2. **It cannot say what any candidate is worth in the presence of the others.** Each
   candidate's coefficient from (1.4) is not the coefficient it would carry alongside the
   other candidates. Be precise about how much Section 5b actually licenses here: the
   *exactly-`VIF`* result needs the return to have been residualised on the omitted column
   as well as the kept one, and (1.4) residualises `ε` on market, country and industry but
   **not** on the other 200-odd candidates. So the shortfall is real and it is of that kind,
   but "exactly the `VIF`" is a two-column theorem and does not transfer to (1.4) as an
   equality. Say the weaker true thing, not the stronger false one. When the top-ranked candidates all
   "revolve around a common theme" — as p.11 says of the UK model's top four, *Sales, Market
   Cap, Broker Coverage, Total Assets*, all of them size — that is a collision, and the
   one-at-a-time ranking is being applied precisely where it is weakest.

The paper's own response is aggregation: p.11 says those four *"should all be aggregated
together to form the size factor"*, and that *"we run additional univariate regressions on
various combinations of these four candidate substyles as in Equation (1.4)"*. That is the
p.20 EMEA fix again — merge the colliding columns. The notes flag that the exact combination
criterion and threshold are **not stated on that page**. Level 12 entry.

### 14f. Where the machinery ends up in the finished model

**p.24, equation (1.7):** `r = X f + u`. The `f` this level fought over is that `f`.
**p.24, equation (1.8):** `Σ = X F Xᵀ + Δ`.

Follow the damage through: an unstable split does not merely produce a wrong `f` on one day.
`F` is the covariance matrix of the `f` **time series** (Level 8), so a collision between two
columns injects a large spurious *negative* covariance between their factor returns — in
**Section 8**, `b₁` and `b₂` moved in opposite directions on a one-stock data change, `+1`
against `−8/7`, `+15/7` against `−16/7`. Two factors that are nearly the same thing appear in
`F` as two factors that hedge each other almost perfectly.

**Now stop, because the obvious next sentence is false and it is worth catching in public.**
The tempting sentence is *"so a portfolio loaded on both gets reported as less risky than it
is."* It does not. Check it on Section 7c's own family. Take a portfolio equally weighted on
AXL and DLT, `w = (½, 0, 0, ½, 0)`. Its cheapness exposure is `a₁ = ½(−3/2) + ½(1) = −1/4`,
and its quality exposure is `a₂(t) = a₁ + t·(w·d) = −1/4 + t/4`:

| `t` | `a₂` | `b₁` | `b₂` | contribution `a₁b₁` | contribution `a₂b₂` | total |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 6 | −5 | −3/2 | 0 | **−3/2** |
| 1/2 | −1/8 | 11 | −10 | −11/4 | +5/4 | **−3/2** |
| 1/4 | −3/16 | 21 | −20 | −21/4 | +15/4 | **−3/2** |
| 1/100 | −99/400 | 501 | −500 | −501/4 | +495/4 | **−3/2** |

The two *contributions* run away to ±125 on a portfolio of two stocks whose returns are −4%
and +3%. The *total* does not move at all. One line of algebra says why: with `b₁ = c₁ − c₂/t`
and `b₂ = c₂/t` from Section 7c, and `a₂ = a₁ + t·δ` where `δ = w·d`,

```
a₁·b₁ + a₂·b₂ = a₁·c₁ + δ·c₂          ← no t anywhere
```

and the exposures of any real portfolio to two nearly-identical columns are themselves nearly
identical, for the same reason the columns are. **So the risk number survives the collision.**
That is p.26's *"it does not impact the efficacy of the risk model"* arriving a second time,
one layer up — at the covariance matrix rather than at the factor returns.

What does not survive is the **decomposition**. The report hands the desk a sensible total
built out of two vast offsetting factor contributions, and every sentence anyone then says
about *which* factor is driving the book is noise. That is the specific mechanism by which
this level's abstraction reaches a risk number, and it is why p.32's word is **apportioning**
and not *forecasting*. The one book whose *total* is genuinely fragile is the one built long
one colliding factor and short the other — the only kind whose `δ` is not small — and `δ` is
assembled from nothing but the names where the two columns disagree.

### 14g. What the notes do NOT support

Searched all 65 transcribed pages in `notes/`:

- **`determinant`** — **zero hits.**
- **`Frisch`**, **`Waugh`**, **`Lovell`** — **zero hits.** The theorem in Section 6 is nowhere
  in the paper, even though equations (1.4) and (1.11) are both residualise-then-regress
  constructions of exactly the kind it governs. Say it that way and not "both applications of
  it": Section 14e showed (1.4) is the *sequential* method, which is the theorem's incomplete
  half — the return residualised, the column not.
- **`singular`**, **`condition number`**, **`matrix inversion`** — **zero hits.**
- **`orthogonal`** — one hit, and it is the transcriber's own commentary on p.52, **not** a
  sentence from the paper.
- **`variance inflation`** — two hits, both on p.32, both quoted in 14a. **No numeric VIF
  value and no numeric threshold appears anywhere.**
- **`multicollinear*`** — three hits, all in the p.32 passage.

So: **no BFRE anchor was found in `notes/` for the determinant, for Frisch–Waugh, or for any
numeric collinearity threshold.** The paper names the disease (p.32), names one exact case of
it (p.26), and twice performs the cure (p.20, p.11) — but never writes down the quantity that
measures it. Do not invent one. Say to the player, in these words: *the machinery of this
level is underneath four separate decisions in the paper and is written down in none of them.*

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level4.py     # 277 exact-rational assertions, exits 0
```

The script recomputes every figure on this page from the raw `x₁`, `x₂` and `r` vectors in
`fractions.Fraction`: both datasets' cross-products, determinants, cosines and VIFs; the joint
fit by Cramer and by elimination; both balance conditions; every wrong method's exact numeric
output and its `SS`; the excess-loss quadratic form; both Frisch–Waugh directions on both
datasets; the whole `t`-family with its invariant fitted vector, invariant residuals and
`1/t` split; the four equally-optimal solutions at `t = 0`; the one-stock sensitivity at three
tightnesses; and brute-force sweeps over 4,092 datasets confirming Frisch–Waugh, the
sequential-VIF identity, the explained-variation identity and the "at most one sign flips"
theorem. If any printed value ever disagrees with this markdown, the markdown is wrong.
