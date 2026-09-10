# Level 5 — The Intercept

Every number below is recomputed in exact rational arithmetic by `tools/verify_level5.py`
(341 assertions plus 11,950 brute-forced cases, exits 0). Nothing here is rounded by hand.
Where a decimal does not terminate it is written with the word **rounded** next to it; every
other decimal on this page is exact.

> **Difficulty, stated honestly, because the rulebook demands it.**
> Sections 1 to 11 are the **easiest level since Level 2**. After the multicollinearity fight of
> Level 4 this will feel like a holiday, and it should — the whole thing is one extra column of
> `1`s and one extra balance condition, and every proof here is completed by squaring a bracket.
> Say that to the player up front so they do not go looking for a difficulty that is not there.
>
> **Sections 12b and 12c are different.** Identification of a factor model — why three columns of
> `1`s cannot all be estimated, what a linear restriction on factor returns does, and why one
> particular restriction and no other makes the market factor mean what the paper says it means —
> is **graduate-level material**. It is normally met in a second econometrics course, if at all.
> It is built here from the same squared bracket, but the player should know they have crossed a
> line, and should be told when they cross it.

---

## 0. What the player is already holding, and the one question Level 0 left open

**From Level 0** — the cold-open file, reused here **unchanged**, so the player watches numbers
they already know cold change their meaning:

```
x = [−1.5, −0.5, 0, +1, +2]     Σx = 1      Σx² = 15/2 = 7.5
r = [−2, −2, +0.5, +4, +3.5]    Σr = 4      Σxr = 15      Σr² = 73/2 = 36.5
b = Σxr/Σx² = 15/(15/2) = 2     exactly
e = r − 2x = [+1, −1, +0.5, +2, −0.5]
Σe = 2   ← NOT zero        Σx·e = 0   ← zero        Σe² = 13/2 = 6.5
SS(b) = 36.5 − 30b + 7.5b² , symmetric about b = 2, SS(1.5) = SS(2.5) = 67/8 = 8.375
```

**From Level 1** — `b = Σxr/Σx²`, derived by nudging, no calculus.
**From Level 2** — the balance condition `Σx·e = 0`, read as a turning force about a pivot.
**From Level 3** — two columns need two balance conditions holding at the same time; the pair is
a 2×2 system solved in fractions.
**From Level 4** — a coefficient means *what this column explains that the other columns have not
already explained*, and the sequential shortcut (fit one column, then fit the next on the
leftovers) gets the numerator right and the denominator wrong.

**The open question.** Level 0 ended on a number nobody explained:

```
Σe = 2   but   Σx·e = 0
```

Why does least squares force one sum to zero and leave the other at 2? The player has been
carrying that for five levels. **This level answers it in one sentence, and the sentence is the
punchline: `Σe = 0` is not a property of least squares at all. It is a property of having a
second dial.** Without that dial, nothing in the arithmetic ever asks the misses to cancel.

---

## 1. The story (no mathematics)

A carpenter is hired to lay a long plank across a school yard so that it comes as close as
possible to touching the seats of a row of children sitting on stools of different heights.

**Job one.** The yard has a stone block cemented into the ground at one particular spot. The
plank must rest on that block. It can tilt as much as the carpenter likes — it pivots on the
block freely — but it cannot be lifted off it. The carpenter tilts the plank until it is as
close to the seats as he can get it. He does a genuinely good job of tilting. But when he stands
back, the plank sits low: most of the children are above it. He cannot fix this. Every tilt he
tries lifts one end and drops the other, and the plank still has to touch that block.

The block is doing something invisible. It is pushing up on the plank. The carpenter's tilt has
balanced all the *turning* forces — that is what "as close as I can get by tilting" means — but
the leftover *lifting* force, the fact that the plank as a whole wants to rise, is being quietly
absorbed by the cement.

**Job two.** The school buys a trolley: a wheeled stand whose height can be cranked up and down,
with a free pivot on top. The block is removed. Now the carpenter has two knobs, height and
tilt, and — this is the part that matters — **there is no cement left to absorb anything.** If
the plank as a whole still wanted to rise, nothing is holding it down, so he would crank it up.
He stops cranking exactly when the plank has no net wish to rise. He stops tilting exactly when
it has no net wish to turn.

**What he notices after doing this a hundred times.** Whatever tilt he happens to be using, the
best height always ends up putting the plank exactly at the *average seat height*, measured at
the *average child's position*. Every single one of his hundred planks passes through that one
point in the air. The point never moves. It belongs to the children, not to the plank. All that
changes from job to job is how steeply the plank tilts about it.

He starts calling that point **the balance point of the class**, and he finds it before he
touches the trolley, because once he knows it, the only thing left to decide is the tilt.

---

## 2. Mapping the story onto the fit, line by line

| In the story | In the fit |
|---|---|
| a child | a stock |
| where the child sits along the row | that stock's score `x` |
| the height of that child's seat | that stock's return `r` |
| the plank | the fitted line |
| tilt of the plank | the slope `b` |
| height of the trolley | the second dial, `a` |
| the cemented block | forcing the line through `(0, 0)` |
| the block's hidden upward push | the leftover `Σe = 2` that Level 0 could not explain |
| "no net wish to turn" | `Σx·e = 0` |
| "no net wish to rise" | `Σe = 0` |
| the balance point of the class | the point `(x̄, r̄)` |
| every plank passes through it | the boss round |

The one row to hold onto is the seventh. **The block was absorbing `Σe`.** Remove the block and
there is nothing left to absorb it, so it has to be zero. That is the entire level.

> **Name unlocked (mechanism first, name second).** The second dial `a` — the height knob, the
> thing that lets the line sit anywhere instead of being nailed to the origin — is called the
> **intercept**, or equivalently the **constant term**. Inside BFRE it has a third name, and
> Section 12 earns it. Do not give the player any of the three names before they have watched
> `Σe` collapse from 2 to 0.

---

## 3. The balance point of the cold-open file

Same five names, same two columns, nothing added.

| Stock | cheapness `x` | return `r` |
|---|---:|---:|
| AXL | −1.5 | −2.0% |
| BRN | −0.5 | −2.0% |
| CHR | 0.0 | +0.5% |
| DLT | +1.0 | +4.0% |
| EMK | +2.0 | +3.5% |

The balance point takes two divisions and no theory:

```
x̄ = Σx/n = 1/5 = 0.2                r̄ = Σr/n = 4/5 = 0.8%
```

**Now the reveal, and it should be run as a PREDICT-THEN-REVEAL round.** Ask the player, before
any arithmetic: *the Level 0 line is `r̂ = 2x`. Does it pass through the balance point (0.2, 0.8)?*
Most players say yes — it is the best line, the balance point is the middle of the data, of
course it goes through the middle. Make them commit, with a reason. Then:

```
line at x̄:      2 × (1/5) = 2/5 = 0.4%
balance point:              4/5 = 0.8%
vertical gap:   r̄ − b·x̄  = 4/5 − 2/5 = 2/5 = 0.4%
```

It misses by 0.4 percentage points. And now multiply that gap by the five stocks:

```
n × gap = 5 × 2/5 = 2 = Σe
```

**That is the answer to Level 0's open question, and it is exact, not approximate.** The
mysterious `Σe = 2` is nothing but *five times the height by which the origin-line sits below the
class's balance point*. It was never a statistical fact. It was a geometric one: a line nailed to
`(0, 0)` cannot also pass through `(0.2, 0.8)`, and the leftover shows up as an uncancelled sum of
misses. Equivalently the average miss is

```
ē = Σe/n = 2/5 = 0.4%   =   exactly the gap
```

The average miss *is* the gap. Say this to the player as the sentence they will remember: **the
sum of the misses measures how far the line is from the balance point, and nothing else.**

---

## 4. Building the second dial: two conditions, not one

The model is now

```
predicted return = a + b·x
miss             e = r − a − b·x
loss             SS(a, b) = Σ(r − a − b·x)²
```

Two dials, so two nudge arguments, run exactly as in Levels 1 and 2.

**Nudge `a` by a tiny amount `h`, holding `b` fixed.** Every miss changes by `−h`:

```
SS(a + h, b) = Σ(e − h)² = Σe² − 2h·Σe + n·h²
```

The `h²` term is positive and negligible for small `h`; the `h` term is `−2h·Σe`. If `Σe` were
anything but zero, a nudge in the right direction would strictly reduce the loss — so at the
bottom, `Σe = 0`. **This is the "no net wish to rise" condition, and it exists only because there
is a height knob to nudge.**

**Nudge `b` by `h`, holding `a` fixed.** Miss `i` changes by `−h·xᵢ`:

```
SS(a, b + h) = Σ(e − h·x)² = Σe² − 2h·Σx·e + h²·Σx²
```

so `Σx·e = 0` — the Level 2 turning-force condition, unchanged.

Write both out with `e = r − a − b·x`:

```
Σe   = 0   →   Σr − n·a − b·Σx   = 0   →   n·a  +  (Σx)·b  = Σr
Σx·e = 0   →   Σxr − a·Σx − b·Σx² = 0   →  (Σx)·a + (Σx²)·b = Σxr
```

On the cold-open numbers, with `n = 5, Σx = 1, Σx² = 15/2, Σr = 4, Σxr = 15`:

```
5a +      b  =  4
 a + (15/2)b = 15
```

**Read the first equation out loud before solving it.** It says the fitted line must reproduce
the totals: five copies of `a`, plus `b` times the total exposure, must equal the total return.
Divide it by 5 and it says `a + b·x̄ = r̄` — the boss round, already visible in the first line of
the system. Do not point that out yet. Let the player find it.

---

## 5. Solving, three ways, in exact fractions

### 5a. By elimination — the by-hand route

```
from row 1:   a = (4 − b)/5
into row 2:   (4 − b)/5 + (15/2)b = 15
multiply by 10:   2(4 − b) + 75b = 150
                  8 − 2b + 75b   = 150
                  8 + 73b        = 150
                       73b       = 142
```

```
b = 142/73        a = (4 − 142/73)/5 = (150/73)/5 = 30/73
```

### 5b. By Cramer's rule — the Level 3 formula, unchanged

```
det = n·Σx² − (Σx)²  = 5·(15/2) − 1² = 75/2 − 1 = 73/2

a = (Σr·Σx² − Σx·Σxr)/det = (4·(15/2) − 1·15)/(73/2) = 15/(73/2) = 30/73
b = (n·Σxr − Σx·Σr)  /det = (5·15 − 1·4)  /(73/2) = 71/(73/2) = 142/73
```

### 5c. The answer

```
a = 30/73  = 0.4110% (rounded)
b = 142/73 = 1.9452  (rounded)
```

**Both are exact fractions with an ugly denominator, and that is worth a sentence.** The `73` is
`det = 73/2` doubled; it came from `5·(15/2) − 1²`, which is `n·Σx² − (Σx)²`. The Level 0 answer
`b = 2` was clean only because the origin was nailed down and the `−(Σx)²` term never appeared.
The moment the line is allowed to move up and down, the denominator learns about `Σx`, and 2
becomes `142/73`.

---

## 6. Both balances at zero — the side-by-side the level exists for

Fitted values `a + b·x`, all over 146 so they can be compared by eye:

| Stock | `x` | `r` (×146) | fitted (×146) | `e` (×146) | `e` exact | `e` decimal |
|---|---:|---:|---:|---:|---:|---:|
| AXL | −1.5 | −292 | −366 | **+74** | 37/73 | +0.5068 (rounded) |
| BRN | −0.5 | −292 | −82 | **−210** | −105/73 | −1.4384 (rounded) |
| CHR | 0.0 | +73 | +60 | **+13** | 13/146 | +0.0890 (rounded) |
| DLT | +1.0 | +584 | +344 | **+240** | 120/73 | +1.6438 (rounded) |
| EMK | +2.0 | +511 | +628 | **−117** | −117/146 | −0.8014 (rounded) |

```
Σe   (×146) =  74 − 210 + 13 + 240 − 117            = 0
Σx·e (×146) = (−3/2)(74) + (−1/2)(−210) + 0 + 240 + 2(−117)
            = −111 + 105 + 240 − 234                = 0
Σe²         = 829/146 = 5.6781 (rounded)
```

### The whole level in one table

| | no intercept (Level 0) | with intercept (Level 5) |
|---|---:|---:|
| `a` | 0, forced | **30/73** |
| `b` | **2** | **142/73** |
| `Σe` | **2** | **0** |
| `Σx·e` | 0 | 0 |
| `Σe²` | 13/2 = 6.5 | **829/146 = 5.6781 (rounded)** |
| passes through (0, 0)? | yes, by force | no — it sits 30/73 above it |
| passes through (x̄, r̄) = (0.2, 0.8)? | no, misses by 0.4 | **yes, exactly** |

Two things to make the player say out loud:

1. **`Σx·e = 0` held in both columns.** Adding the intercept did not create the balance
   condition the player already knew. It added a *second, different* one.
2. **`Σe = 0` appeared only in the right-hand column.** So the folklore "least squares makes the
   errors sum to zero" is false as stated. It is true only of a fit that contains a constant
   term. Level 0's file was the counterexample all along.

The slope barely moved:

```
2 − 142/73 = 4/73 = 0.0548 (rounded)
```

which is the trap the level has to defuse: *the coefficient hardly changed, so the intercept
hardly matters.* Section 9e prices that belief.

---

## 7. Where the improvement came from — Frisch–Waugh, called back from Level 4

```
Σe² fell from 13/2 to 829/146:    13/2 − 829/146 = 949/146 − 829/146 = 120/146 = 60/73
                                                                     = 0.8219 (rounded)
```

**Where did `60/73` come from?** Level 4 built the machine that answers this, so use it rather
than re-deriving. The intercept is a *new column*: a column of five `1`s. Level 4's rule says a
new column is only worth what it explains **after** the columns already present have taken their
share. So residualise the ones-column on `x`:

```
coefficient of x in "fit the ones-column on x"   =  Σ(1·x)/Σx² = 1/(15/2) = 2/15
residualised ones-column   m = 1 − (2/15)x = [6/5, 16/15, 1, 13/15, 11/15]
m·m = n − (Σx)²/Σx² = 5 − 2/15 = 73/15
m·e = Σe − (2/15)·Σx·e = 2 − 0 = 2
m·r = Σr − (2/15)·Σxr  = 4 − (2/15)(15) = 4 − 2 = 2
```

and then, using Level 4's two identities:

```
a       = (m·r)/(m·m) = 2/(73/15)   = 30/73     ← the intercept, from Level 4's formula
SS drop = (m·e)²/(m·m) = 4/(73/15)  = 60/73     ← the improvement, exactly
```

Say this to the player in these words: **the intercept is the leftover average miss, divided by
how much of the constant column the `x` column had not already eaten.** The `73/15` in the
denominator is that "how much". If `x` had summed to zero, the ones-column would have been
untouched by `x`, `m·m` would have been the full `5`, and the two dials would not have interfered
at all. Hold that thought — it is the whole of Section 12.

> **Name still locked.** The share of the up-and-down movement in `r` that the line accounts for
> is `20164/24309 = 0.8295` (rounded), and it equals `Sxr²/(Sxx·Srr)` with the centred sums of
> Section 8. The name for that number is **not** unlocked until Level 6, where it turns out to be
> the same fact as the t-statistic. Compute it, do not name it.
>
> Warning against a false pattern: on *this* dataset `1 − (13/2)/(73/2)` also equals `60/73`, the
> same fraction as the SS drop. **That is an arithmetic coincidence of these five numbers, not a
> theorem.** Say so, or the player will build a rule out of it.

---

## 8. Centering — why `Σxr/Σx²` becomes Cov/Var

### 8a. Move the origin to the balance point

Subtract the balance point from both columns. Everything stays in tenths:

| Stock | `x` | `u = x − x̄` (×10) | `r` | `v = r − r̄` (×10) |
|---|---:|---:|---:|---:|
| AXL | −1.5 | −17 | −2.0 | −28 |
| BRN | −0.5 | −7 | −2.0 | −28 |
| CHR | 0.0 | −2 | +0.5 | −3 |
| DLT | +1.0 | +8 | +4.0 | +32 |
| EMK | +2.0 | +18 | +3.5 | +27 |

```
Σu = (−17 − 7 − 2 + 8 + 18)/10  = 0        ← by construction
Σv = (−28 − 28 − 3 + 32 + 27)/10 = 0        ← by construction

Σu²  = (289 + 49 + 4 + 64 + 324)/100   = 730/100  = 73/10  = 7.3
Σuv  = (476 + 196 + 6 + 256 + 486)/100 = 1420/100 = 71/5   = 14.2
Σv²  =                                              333/10 = 33.3
```

**Now run the Level 1 machine — the no-intercept one — on these two new columns:**

```
b = Σuv/Σu² = (71/5)/(73/10) = (71/5)(10/73) = 142/73
```

The same `142/73`. **This is the mechanical content of the level: fitting with an intercept on
the raw columns is the same arithmetic as fitting without one on the moved columns.** The
intercept's only job was to slide the origin to the balance point; once the player slides it by
hand, the second dial has nothing left to do.

And then the intercept comes back for free from the boss-round identity:

```
a = r̄ − b·x̄ = 4/5 − (142/73)(1/5) = 292/365 − 142/365 = 150/365 = 30/73
```

### 8b. Why the two sums collapse — the algebra, in full

Nothing is skipped here; this is the "origin test" step.

```
Σuv = Σ(x − x̄)(r − r̄)
    = Σxr − x̄·Σr − r̄·Σx + n·x̄·r̄
    = Σxr − x̄(n·r̄) − r̄(n·x̄) + n·x̄·r̄        because Σr = n·r̄ and Σx = n·x̄
    = Σxr − n·x̄·r̄

Σu² = Σ(x − x̄)²
    = Σx² − 2x̄·Σx + n·x̄²
    = Σx² − n·x̄²
```

Both times, two of the three correction terms are the same thing and one of them cancels. On the
file:

```
Σuv = 15 − 5·(1/5)(4/5) = 15 − 4/5   = 71/5
Σu² = 15/2 − 5·(1/25)   = 15/2 − 1/5 = 75/10 − 2/10 = 73/10
```

**The `2/10` is the whole story.** `Σx²` is `73/10` of honest spread about the balance point plus
`2/10` of "the column is not centred". The origin-fit divides by all `75/10`; the correct fit
divides by only the `73/10`.

### 8c. The divisor cancels — and the name unlocks

Divide top and bottom by the same number `k` and the ratio cannot change:

```
b = (Σuv/k) / (Σu²/k)      for any k ≠ 0
```

| `k` | top = `Σuv/k` | bottom = `Σu²/k` | ratio |
|---|---:|---:|---:|
| 1 | 71/5 = 14.2 | 73/10 = 7.3 | **142/73** |
| n = 5 | 71/25 = 2.84 | 73/50 = 1.46 | **142/73** |
| n − 1 = 4 | 71/20 = 3.55 | 73/40 = 1.825 | **142/73** |
| 7 (a nonsense divisor) | — | — | **142/73** |

> **Names unlocked, both at once, and only now.** `Σu²/k` — the average squared distance of the
> `x` column from its own balance point — is the **variance** of `x`. `Σuv/k` — the average
> product of the two columns' distances from their balance points — is the **covariance** of `x`
> and `r`. So the slope is
>
> ```
> b = Cov(x, r) / Var(x)
> ```
>
> and the player has just built both objects from nothing, in the right order: mechanism, then
> name. Tell them explicitly that the `n` versus `n − 1` argument they will meet in every
> textbook **cannot touch this formula**, because whichever convention is chosen appears in both
> the top and the bottom and cancels. It matters in Level 6, where it is not a ratio, and it will
> be built there. That is the honest boundary: name it, defer it, do not fudge it.

### 8d. Centre `x` only, or `r` only? These are not the same

A genuinely surprising pair of facts, and both are exam-grade traps:

```
centre x only:  Σ(u·r)/Σu²  =  (71/5)/(73/10)  = 142/73   ← CORRECT
centre r only:  Σ(x·v)/Σx²  =  (71/5)/(15/2)   = 142/75   ← WRONG (1.8933, rounded)
```

Why the first one works: once `Σu = 0`,

```
Σu·r = Σu(v + r̄) = Σuv + r̄·Σu = Σuv + 0 = Σuv
```

so centring `r` afterwards changes nothing. Check it on the file: `Σu·r = Σxr − x̄·Σr = 15 − 4/5
= 71/5`, the same `71/5`.

Why the second one fails: the numerator is *also* `71/5` — correct — but the denominator is
`Σx² = 15/2 = 75/10` instead of `73/10`. **The rule to memorise: centre the column whose squares
you are dividing by.** Centring the other one is optional; centring the wrong one is fatal.

---

## 9. The wrong methods, priced exactly

Every one of these is an answer a real player has produced. Each is given its exact number and
its exact cost, because "that's wrong" teaches nothing and "that's wrong and it costs you
`8/365`" teaches the structure.

Recall the target: **`a = 30/73`, `b = 142/73`, `Σe² = 829/146 = 5.6781 (rounded)`.**

### 9a. "Keep `b = 2` and just add the average miss as the intercept"

The most common answer by a distance. Level 0 gave `ē = 2/5`, so set `a = 2/5, b = 2`.

```
e = r − 2/5 − 2x  = [+6, −14, +1, +16, −9]/10
Σe   = (6 − 14 + 1 + 16 − 9)/10                                = 0     ✓ first balance holds
Σx·e = (−3/2)(6/10) + (−1/2)(−14/10) + 0 + 16/10 + 2(−9/10)
     = (−9 + 7 + 16 − 18)/10                                   = −2/5  ✗ second balance FAILS
Σe²  = (36 + 196 + 1 + 256 + 81)/100 = 570/100 = 57/10 = 5.7
```

**Cost:** `57/10 − 829/146 = 4161/730 − 4145/730 = 8/365 = 0.021918 (rounded)`.

Two things to make of it. First, it is *nearly right* — the excess is about two hundredths — and
that is exactly why it is dangerous: a player who does this will not notice from the loss. Second,
**this line does pass through the balance point**: `2/5 + 2(1/5) = 4/5 = r̄`. Adding the average
miss is precisely the operation that satisfies `Σe = 0`, and `Σe = 0` is precisely the condition
"passes through the balance point". What it does *not* do is fix the tilt. And the excess has a
closed form that says so:

```
excess = Σu² · (Δb)² = (73/10)(2 − 142/73)² = (73/10)(4/73)² = 8/365
```

The whole penalty is the squared slope error times the centred spread. A perfect setup for
Section 11, which is the boss round.

### 9b. "Fit the average first, then fit the slope on what is left" (the Level 4 shortcut, again)

```
step 1:  a = r̄ = 4/5                    step 2:  b = Σ(x·v)/Σx² = 142/75 = 1.8933 (rounded)

Σe   = 4 − 4 − 142/75 = −142/75   ✗ first balance FAILS
Σx·e = 15 − 4/5 − 71/5 = 0        ✓ second balance holds
Σe²  = 4811/750 = 6.4147 (rounded)
```

**Cost:** `4811/750 − 829/146 = 20164/27375 = 0.7366 (rounded)`. Thirty-four times the cost of
trap 9a.

The sharpest way to show the damage: having no intercept at all gives `Σe² = 6.5`. This method
spends a whole extra parameter and gets to `6.4147` (rounded) — a gain of `13/2 − 4811/750 =
32/375 = 0.0853 (rounded)` out of the `60/73 = 0.8219 (rounded)` that was available. **It
captures about a tenth of the benefit of the parameter it just spent.**

And the reason is exactly Level 4's, which the player should be made to state before being told:
the numerator `Σ(x·v) = 71/5` is *right*; the denominator `Σx² = 15/2` is *inflated*, by exactly
the `n·x̄² = 1/5` that the constant column had already accounted for. The deflation factor is

```
Sxx/Σx² = (73/10)/(15/2) = 73/75          and     (142/73)(73/75) = 142/75
```

which is the Level 4 variance-inflation story with the constant column playing the part of the
second factor. **Call this back explicitly.** Two levels, one mechanism.

Notice the symmetry between 9a and 9b: 9a satisfies the first balance and breaks the second, 9b
satisfies the second and breaks the first. Neither is the fit. **The fit is the only pair of
numbers that satisfies both at once**, which is what a 2×2 system means.

### 9c. Mismatched divisors inside Cov/Var

Having just unlocked the names, a player who computes covariance with `n − 1` and variance with
`n` (or the reverse) gets:

```
Cov(n−1)/Var(n)   = (71/20)/(73/50) = 355/146 = 2.4315 (rounded)     ← 5/4 times too big
Cov(n)/Var(n−1)   = (71/25)/(73/40) = 568/365 = 1.5562 (rounded)     ← 4/5 of the truth
```

Both are off by the ratio of the two divisors and nothing else. The lesson is not "use `n − 1`";
it is **"use the same one twice, and then stop worrying about which."**

### 9d. The Level 0 shortcuts, still wrong, now for a second reason

```
Σr/Σx        = 4/1               = 4.0000
mean of r/x  = (4/3 + 4 + 4 + 7/4)/4 = 133/48 = 2.7708 (rounded)   ← CHR excluded, x = 0
```

Level 0 rejected these because they are not minimising anything. Level 5 adds a second charge:
neither of them has an intercept either, so neither can pass through the balance point.

### 9e. "The line must go through the origin — it's a return model, zero exposure means zero return"

This one deserves respect rather than a correction, because it is an *economic* argument, and it
is the argument BFRE itself half-accepts. Answer it with the arithmetic:

- The fitted intercept is `30/73 = 0.4110% (rounded)`. That is a return the model is handing to
  every stock in the file for no reason connected to `x` at all.
- Forcing it to zero costs `60/73 = 0.8219 (rounded)` of `Σe²`. As a ratio,
  `(13/2)/(829/146) = 949/829 = 1.1448 (rounded)`, so the squared misses are
  `949/829 − 1 = 120/829 = 0.1448 (rounded)` larger — **about 14.5% too big (rounded)**.
- Anything built from those squared misses inherits the error. In standard-deviation units the
  overstatement is `√(949/829) = 1.0699…` — **irrational, so this decimal is a bound, not an
  exact value**; the verifier proves `1.0699² < 949/829 < 1.0700²`. Call it about 7% too high.
- Level 9 builds the specific-risk matrix `D` out of exactly these residuals. So the answer to
  "does the intercept matter, the slope only moved by `4/73`?" is: **the slope is not what it
  changed.** It changed the risk number by roughly 7%, in the direction of overstating it, and it
  did so on every single stock in the file.

The honest other half of the answer, which the player must also be able to give: *if the `x`
column is built so that its (weighted) average is zero, then the intercept and the slope stop
interfering, and the origin-fit and the balance-point-fit give the same slope.* That is not a
dodge. It is what BFRE actually does, and Section 12 proves it.

---

## 10. Rescaling the column: what moves and what does not

A one-line check that costs nothing and prevents a whole class of confusion later, when BFRE
divides its columns by a standard deviation.

Replace `x` by `c·x` for any `c ≠ 0`:

| `c` | `a` | `b` | residuals | `Σe²` |
|---:|---:|---:|---|---:|
| 1 | 30/73 | 142/73 | [37/73, −105/73, 13/146, 120/73, −117/146] | 829/146 |
| 2 | 30/73 | **71/73** | identical | 829/146 |
| 1/3 | 30/73 | **426/73** | identical | 829/146 |
| −1 | 30/73 | **−142/73** | identical | 829/146 |
| 10 | 30/73 | **71/365** | identical | 829/146 |

`a`, the fitted values, the residuals and the loss are untouched; only `b` rescales, as `b → b/c`.
**Units live in the coefficient, never in the fit.** So when BFRE divides a raw characteristic by
a standard deviation to make an exposure, it is choosing what "one unit" means and nothing more —
and that is why a factor return can be read as "the return to one standard deviation of this
characteristic".

---

## 11. BOSS ROUND — prove the fitted line passes through `(x̄, r̄)`

### 11a. Fresh data, four names

| Stock | `x` | `r` |
|---|---:|---:|
| FRT | 1 | +2.0% |
| GLM | 2 | +3.0% |
| HSK | 4 | +4.0% |
| JND | 5 | +7.0% |

```
n = 4      Σx = 1+2+4+5 = 12       Σx² = 1+4+16+25 = 46
           Σr = 2+3+4+7 = 16       Σxr = 2+6+16+35 = 59       Σr² = 4+9+16+49 = 78
x̄ = 12/4 = 3                        r̄ = 16/4 = 4
```

The system, and the by-hand solution:

```
4a + 12b = 16          →  a = 4 − 3b
12a + 46b = 59         →  12(4 − 3b) + 46b = 59
                          48 − 36b + 46b   = 59
                                   10b     = 11
```

```
b = 11/10 = 1.1        a = 4 − 3(11/10) = 4 − 33/10 = 7/10 = 0.7
```

(Cramer agrees: `det = 4·46 − 12² = 184 − 144 = 40`; `a = (16·46 − 12·59)/40 = 28/40 = 7/10`;
`b = (4·59 − 12·16)/40 = 44/40 = 11/10`.)

| Stock | `x` | `r` (×10) | fitted (×10) | `e` (×10) |
|---|---:|---:|---:|---:|
| FRT | 1 | 20 | 18 | **+2** |
| GLM | 2 | 30 | 29 | **+1** |
| HSK | 4 | 40 | 51 | **−11** |
| JND | 5 | 70 | 62 | **+8** |

```
Σe = (2 + 1 − 11 + 8)/10 = 0            Σx·e = (2 + 2 − 44 + 40)/10 = 0
Σe² = (4 + 1 + 121 + 64)/100 = 190/100 = 19/10 = 1.9
```

**The claim to be proved:** the line hits `(x̄, r̄) = (3, 4)`.

```
a + b·x̄ = 7/10 + (11/10)(3) = 7/10 + 33/10 = 40/10 = 4 = r̄      ✓
```

One instance is not a proof. Demand the proof.

### 11b. The proof the player must produce (no calculus, one squared bracket)

**Step 1. Freeze the tilt.** Pick *any* `b` whatsoever and hold it. Define, for each stock,

```
d = r − b·x
```

`d` is the height the line would have to sit at to hit that stock exactly, given the frozen tilt.
The loss becomes a function of one dial:

```
SS(a) = Σ(r − a − b·x)² = Σ(d − a)²
```

**Step 2. Complete the square — exactly, with no approximation.**

```
Σ(d − a)² = Σd² − 2a·Σd + n·a²
          = n[ a² − 2a·d̄ ] + Σd²                         where d̄ = Σd/n
          = n[ a² − 2a·d̄ + d̄² ] − n·d̄² + Σd²
          = n(a − d̄)²  +  Σ(d − d̄)²
```

The second term does not contain `a` at all. The first is `n` times a square, so it is never
negative and it is zero at exactly one place. Therefore, **for every frozen `b`**, the best height
is

```
a = d̄ = mean(r − b·x) = r̄ − b·x̄
```

**Step 3. Rearrange, and it is done.**

```
a = r̄ − b·x̄     ⟺     a + b·x̄ = r̄     ⟺     the point (x̄, r̄) is on the line.   ∎
```

**The crucial thing the player must notice, and must be pushed to notice.** Step 2 never used the
optimality of `b`. It froze `b` at *any* value. So the conclusion is stronger than the claim:

> **Every line that is best-at-its-own-tilt passes through the balance point.** The best line is
> merely one of them. `Σe = 0` and "passes through `(x̄, r̄)`" are the same statement, and both are
> properties of having a height knob — not of having found the right tilt.

Verify Step 2 numerically on FRT–JND with `b` frozen at `11/10`:

```
d = r − (11/10)x = [9, 8, −4, 15]/10          d̄ = (9 + 8 − 4 + 15)/40 = 28/40 = 7/10 = a   ✓
Σ(d − d̄)² = (4 + 1 + 121 + 64)/100 = 19/10                                                  ✓
so   SS(a) = 19/10 + 4(a − 7/10)²
```

| `a` | 0 | 1/2 | **7/10** | 9/10 | 7/5 | 2 |
|---|---:|---:|---:|---:|---:|---:|
| `SS(a)` | 3.86 | 2.06 | **1.90** | 2.06 | 3.86 | 8.66 |

Symmetric about `a = 7/10`, exactly as `SS(b)` was symmetric about `b = 2` in Level 0. **The
player has now seen the same parabola trick twice — call that back.**

And Step 2's independence from `b` is checkable directly:

| frozen `b` | 0 | 1 | 11/10 | 3/2 | −2 | 7/3 |
|---|---:|---:|---:|---:|---:|---:|
| best `a` = `r̄ − b·x̄` | 4 | 1 | 7/10 | −1/2 | 10 | −3 |
| `a + b·x̄` | **4** | **4** | **4** | **4** | **4** | **4** |

Six different lines, six different intercepts, all through `(3, 4)`.

### 11c. The other direction: what `Σe = 0` does *not* give you

Take the family of all lines through the balance point, `r̂ = 4 + m(x − 3)`, one for each tilt `m`:

```
SS(m) = Σ(v − m·u)² = Σv² − 2m·Σuv + m²·Σu² = 14 − 22m + 10m²
```

using the boss file's centred sums `Σu² = 46 − 4(9) = 10`, `Σuv = 59 − 4(3)(4) = 11`,
`Σv² = 78 − 4(16) = 14`.

| `m` | 0 | 1/2 | 1 | **11/10** | 6/5 | 2 |
|---|---:|---:|---:|---:|---:|---:|
| `Σe` | 0 | 0 | 0 | **0** | 0 | 0 |
| `SS(m)` | 14.0 | 5.5 | 2.0 | **1.9** | 2.0 | 10.0 |

Every one of them has `Σe = 0`. Symmetric about `m = 11/10`, and `SS(1) = SS(6/5) = 2` exactly.
Take `m = 1` and look at its misses:

```
e = [0, 0, −1, +1]      Σe = 0  ✓      Σ(x − x̄)e = 0 + 0 − 1 + 2 = 1  ✗      Σe² = 2
```

**So the two balance conditions do genuinely different jobs.** `Σe = 0` pins the *height* and
leaves the tilt completely free. `Σx·e = 0` pins the *tilt*. You need both, which is why the
system is 2×2 and not two separate one-dial problems — the Level 3 lesson, arriving from a new
direction.

Finally, the cost of leaving the balance point: shift the whole fitted line up by `c`, so every
residual becomes `e − c`. Since `Σe = 0`,

```
Σ(e − c)² = Σe² − 2c·Σe + n·c² = 19/10 + 4c²
```

| shift `c` | 1/10 | 1/2 | −1/2 | 1 |
|---|---:|---:|---:|---:|
| `Σe²` | 1.94 | 2.90 | 2.90 | 5.90 |

Strictly worse for every `c ≠ 0`, symmetric in `±c`, and quadratic. That is a second, independent
proof of the boss claim, and the player should be asked for it after the first.

### 11d. Boss sabotage round

Hand the player the boss fit with **one residual corrupted** and no other information:

```
reported:   e = [+0.2, +0.1, −0.8, +0.8]    for x = [1, 2, 4, 5]
```

Run the two audits:

```
Σe   = (2 + 1 − 8 + 8)/10  = 3/10       should be 0
Σx·e = (2 + 2 − 32 + 40)/10 = 12/10     should be 0
```

If exactly one residual `k` was shifted by `δ`, then `Σe = δ` and `Σx·e = xₖ·δ`. Two equations,
two unknowns:

```
xₖ = (Σx·e)/(Σe) = (12/10)/(3/10) = 4      →  HSK
δ  = Σe = 3/10
true residual = −8/10 − 3/10 = −11/10                        ✓ matches Section 11a
```

**The point of the round, which the player must state:** with only the no-intercept fit there is a
single audit equation, `Σx·e = 0`, and two unknowns — *which* asset and *by how much* — so the
culprit cannot be located at all. **The intercept did not just improve the fit. It bought a second
audit equation, and two equations are what make the file forensically checkable.** This is Level 2's
sabotage round, doubled, and it is the practical reason production risk desks always fit a market
factor: it is the diagnostic that catches a bad return file.

### 11e. INTERROGATION — the hostile CRO's five objections

Play this straight and hard. The player passes only if they answer all five from structure.

1. **"You proved it on four stocks. Show me it isn't an accident of your numbers."** — Wanted: the
   Section 11b proof, which never touched the data. Accept nothing else. (The verifier also
   brute-forces 7,680 three-asset files and 620 four-asset files; every one satisfies
   `a = r̄ − b·x̄`, `Σe = 0` and `Σx·e = 0`.)
2. **"Fine. I weight my regression by square root of market cap. Does your balance point
   survive?"** — Yes, and the proof is the same squared bracket with `w` carried through:
   `Σw(d − a)² = (Σw)(a − d̄_w)² + Σw(d − d̄_w)²`, where `d̄_w = Σw·d/Σw`. So the line passes
   through the **weighted** balance point `(Σwx/Σw, Σwr/Σw)`. Section 12a does it on numbers.
3. **"Your line is guaranteed to predict the average stock perfectly. Isn't that a rigged
   scoreboard?"** — Wanted: no, it is one constraint out of `n`, and it is *why* `Σe` is useless as
   a quality measure — which is Level 0's boss round arriving from the other side. Also: the
   average stock is not a stock. Nothing in the portfolio is at `(x̄, r̄)`.
4. **"Your slope moved from 2 to 1.9452. Half a percent. You wasted my morning."** — Wanted:
   Section 9e. The slope is not what changed. `Σe²` fell by `(60/73)/(13/2) = 120/949 = 0.1264`
   (rounded), the risk number built from it is about 7% too high without the intercept, and the
   fit was handing out `0.4110%` (rounded) of unexplained return to every asset in the file.
5. **"Then why does anyone ever fit without an intercept?"** — Wanted, and this is the promotion
   question: **because if the `x` column has already been centred, the intercept and the slope
   stop interfering.** Then the origin-fit slope and the balance-point-fit slope are the same
   number, and the intercept only carries the average return. That is not a hypothetical — it is
   what BFRE does to every exposure column before it estimates anything, and Section 12 shows it.

---

## 12. ALWAYS RETURN TO BFRE

Everything below is anchored to a page transcribed in `notes/`. Quotations are as transcribed.

### 12a. p.10 — BFRE centres its columns before it ever runs a regression

> **p.10, verbatim:** *"Substyles are standardised to a common scale… Conceptually, the
> standardisation process is similar to forming a z-score. **The mean is defined as the
> square-root of market capitalisation weighted average value so that the transformed substyles
> (and styles) have the property that their weighted average is zero.** Additionally, these
> values are divided by their equally-weighted standard deviation so that a value of +1 for a
> substyle or style can be interpreted as a security having an exposure of one standard deviation
> above the market average. An exposure of zero indicates that a security has the market average
> value for a given substyle, or style."*

The same procedure is restated as step 3 of the exposure pipeline on **p.39**: *"Huberisation…
standardised values are referred to as exposures and take values between +/− 3 and are
standardised to a square-root capitalisation mean of zero, with an equal-weighted standard
deviation of one."*

**That sentence is Section 8a, done in advance, with weights.** BFRE never fits a raw
characteristic. It fits `x − x̄_w`, and the "divided by their standard deviation" step is Section
10 — a change of units that moves `b` and nothing else.

To make it concrete, take the same five stocks and invent square-root-cap-style weights. **These
weights are invented for teaching; the paper prints no per-asset weights.**

| Stock | `w` | `x` | `r` |
|---|---:|---:|---:|
| AXL | 2 | −1.5 | −2.0% |
| BRN | 2 | −0.5 | −2.0% |
| CHR | 1 | 0.0 | +0.5% |
| DLT | 2 | +1.0 | +4.0% |
| EMK | 3 | +2.0 | +3.5% |

```
Σw = 10        Σw·x = −3 −1 +0 +2 +6 = 4          Σw·x² = 4.5 + 0.5 + 0 + 2 + 12 = 19
               Σw·r = −4 −4 +0.5 +8 +10.5 = 11    Σw·x·r = 6 + 2 + 0 + 8 + 21 = 37

x̄_w = 4/10 = 0.4        r̄_w = 11/10 = 1.1%
```

Weighted normal equations, and the elimination:

```
10a +  4b = 11
 4a + 19b = 37     →   44 − 16b + 190b = 370   →   174b = 326
```

```
b = 326/174 = 163/87 = 1.8736 (rounded)        a = r̄_w − b·x̄_w = 11/10 − (163/87)(2/5)
                                                 = 61/174 = 0.3506 (rounded)
Σw·e = 0      Σw·x·e = 0
```

Now standardise the column the way p.10 says — subtract the **weighted** mean:

```
x* = x − 2/5 = [−19, −9, −4, +6, +16]/10        Σw·x* = (−38 − 18 − 4 + 12 + 48)/10 = 0
```

and refit. The two dials come apart completely:

```
a = 11/10 = r̄_w        (the intercept is now just the weighted average return)
b = 163/87             (unchanged)
residuals unchanged, Σw·e² unchanged at 2057/174 = 11.8218 (rounded)
```

**That is what standardisation buys.** With `Σw·x* = 0`, the constant column and the exposure
column are weighted-orthogonal — Level 4's `det` is at its healthiest, `B = 0` — so neither
coefficient can contaminate the other. Drop the intercept entirely and `b` does not move:

```
no-intercept fit on x*:   b = 163/87        (identical)
but now Σw·e = 11 = Σw·r  (the level has nowhere to live, so the fit carries none of it)
```

**The slope becomes immune to the intercept; the need for an intercept does not go away.** That
distinction is the whole of Section 12b.

### 12b. p.4, p.25, p.26 — the intercept has a name in BFRE, and it is the market factor

> **p.4, verbatim fragments:** *"all equity assets have a unit exposure to this factor"*; market
> factor return = *"cross-sectional average return across all assets in the model estimation"*,
> with **footnote 2**: *"Average return based on regression weights, i.e. square-root of market
> capitalisation."*

A column in which every asset scores exactly `1` **is** the column of ones. So:

> **Name unlocked, and it is the third name for the same object.** The height knob of Section 4,
> the constant column of Section 7, and **the BFRE market factor** are one thing. Its coefficient
> `f_Mkt` is the `a` of this level.

**p.25, equation (1.9)** is the first-pass cross-sectional regression, with the market term
carrying no summation index — one column, not a block:

```
r = X_Mkt f_Mkt + Σ_{i∈Sty} X_Sty,i f_Sty,i + Σ_{j∈CInd} X_CInd,j f_CInd,j
                + Σ_{k∈CCty} X_CCty,k f_CCty,k + u
```

**p.26** then states the problem this level creates when you have more than one such column:

> *"This specification is not uniquely identified as there are an infinite number of possible
> solutions. The reason for this lies in the fact that, for each asset, there exist **three
> intercept terms** – the market factor, an industry factor, and a country factor. Every asset has
> unit exposure to these three factors. This can be resolved by adding two linear restrictions on
> the definition of the factor returns, which reduces the intercept terms from three to one. This
> identification simply represents a rotation of the factor returns. It does not impact the
> efficacy of the risk model."*

**Equation (1.10)**, the two restrictions, as transcribed:

```
Σ_j ω_CInd,j · f_CInd,j = 0            Σ_k ω_CCty,k · f_CCty,k = 0
```

with **footnote 15**: *"The average return is a square-root of market capitalisation weighted
return."*

> **Difficulty flag, as promised in the header. From here to the end of 12c is graduate-level.**
> The player should be told that plainly. What follows is factor-model identification, and it is
> not a harder kind of arithmetic — it is the same squared bracket — but it is a harder kind of
> *question*, and being told so is what stops a capable person concluding they are slow.

### 12c. Why restriction (1.10) has the shape it has — worked in fractions

Split the same five stocks into two industries — AXL, BRN, CHR in **MAT**; DLT, EMK in **TEC** —
and keep the weights and the standardised column `x*` from 12a.

```
aggregate weight of MAT = 2 + 2 + 1 = 5           aggregate weight of TEC = 2 + 3 = 5
average weight per asset, MAT = 5/3               average weight per asset, TEC = 5/2
```

The transcription of `ω` in (1.10) is glossed in the notes as *"The average (square-root of
capitalisation) weight for Core Industries"*, which is **ambiguous between two readings**. Work
both. They differ, and the difference is exactly this level's subject.

**Reading A — `ω` = the industry's aggregate weight.** Then `5·f_MAT + 5·f_TEC = 0`, so
`f_TEC = −f_MAT`, and the two industry columns collapse to one:

```
g = d_MAT − d_TEC = [+1, +1, +1, −1, −1]
Σw·g = 2 + 2 + 1 − 2 − 3 = 0        ← g is weighted-orthogonal to the constant column
Σw·x* = 0                            ← so is x*, by p.10
```

Both non-constant columns are weighted-orthogonal to the column of ones, so the constant's
coefficient decouples exactly as in 12a:

```
f_Mkt = Σw·r / Σw = 11/10 = 1.10%
```

and the remaining 2×2 block, using `Σw·g² = 10`, `Σw·g·x* = −12`, `Σw·x*² = 87/5`,
`Σw·g·r = −26`, `Σw·x*·r = 163/5`:

```
      10·f_MAT − 12·f_Sty = −26
     −12·f_MAT + (87/5)·f_Sty = 163/5

from row 1:   f_MAT = (−13 + 6·f_Sty)/5
into row 2 (×5):   156 − 72·f_Sty + 87·f_Sty = 163   →   15·f_Sty = 7
```

```
f_Sty = 7/15 = 0.4667% (rounded) per unit of standardised exposure
f_MAT = (−26 + 12·(7/15))/10 = (−102/5)/10 = −51/25 = −2.04%
f_TEC = +51/25 = +2.04%
```

All three balances hold: `Σw·e = 0`, `Σw·g·e = 0`, `Σw·x*·e = 0`, with residuals
`[−26, −96, +244, +87, −58]/150` and `Σw·e² = 697/150 = 4.6467 (rounded)`.

**`f_Mkt = 1.10% = Σw·r/Σw` exactly — the square-root-cap weighted average return of the file.
That is precisely what p.4 asserts the market factor return is.** The player has just derived the
paper's own sentence from two ingredients: p.10's centring, and p.26's restriction.

**Reading B — `ω` = the average weight per asset.** Then `(5/3)f_MAT + (5/2)f_TEC = 0`, so
`f_TEC = −(2/3)f_MAT`, and the reduced column is `g₂ = [1, 1, 1, −2/3, −2/3]` with

```
Σw·g₂ = 5 − (2/3)(5) = 5/3 ≠ 0        ← NOT orthogonal to the constant
```

Solving the same way:

```
f_Mkt = 377/250 = 1.508%       f_MAT = −306/125 = −2.448%       f_TEC = +204/125 = +1.632%
f_Sty = 7/15                    (unchanged)
```

**Two things fall out, and they are the payoff of the whole level.**

1. **p.26's claim about rotation is exactly right, and now verified.** The fitted values are
   identical under both readings, the residuals are identical, `Σw·e² = 697/150` under both. The
   risk model is untouched — *"It does not impact the efficacy of the risk model."* The style
   factor return is the same `7/15` either way.
2. **But `f_Mkt` moved, by `51/125 = 0.4080` percentage points**, from `1.10%` to `1.508%`. So the
   restriction does not choose the model; it chooses **what the market factor return means**. And
   only Reading A makes it mean what p.4 says it means. Reading B's factor returns fail Reading
   A's own restriction by `5·f_MAT + 5·f_TEC = −102/25 = −4.08`.

The general rule, which a player at tier 4 should be able to state: the reduced column
`g_j = d_j − (ω_j/ω_J)·d_J` has `Σw·g_j = W_j − (ω_j/ω_J)·W_J`, where `W_j` is industry `j`'s
**aggregate** weight. That is zero for every `j` **if and only if `ω` is proportional to the
aggregate weights `W`.** The verifier sweeps 729 (weights, restriction) combinations: in every
case where the reduced columns are weighted-orthogonal to the constant, `f_Mkt` came out exactly
equal to the weighted average return; in the 456 cases where they are not, it did not.

**So: p.4 disambiguates p.26.** The transcribed word "average" in the gloss of `ω` must be read as
the industry's aggregate square-root-cap weight (or anything proportional to it), because only
that reading reproduces p.4's own definition of the market factor return. **The paper does not say
this.** It is an inference this level's arithmetic forces, and it is a Level 12 entry: an
identification convention on which the interpretation of the largest factor in the model depends,
stated in a footnote, in words that admit two readings.

### 12d. p.42 (1.12), p.44, p.47 (1.31), p.52 (1.49) — Cov/Var in four places in the paper

The formula built in Section 8c is not decoration. It is the estimator behind four separate BFRE
descriptors, every one of which is a regression *with an intercept*:

| Page | Equation | Regression | This level's `a` | This level's `b` |
|---|---|---|---|---|
| **p.42** | **(1.12)** | `r_{i,s} = α_i + β_i·r^M_{i,s} + ε_{i,s}` | `α_i` = **Historical Alpha** (named on p.44) | `β_i` = **Historical Beta** |
| **p.47** | **(1.31)** | `EPS_{i,u} = α_i + β_i·u + ε_{i,u}` | trend level | trend slope |
| **p.52** | **(1.49)** | `lê_{i,s} = a_i + γ_i·f_s + u_{i,s}` | `a_i` | `γ_i` = **macro-economic beta** |
| **p.39** | Fill-Miss | substyle regressed on log market cap, market, country and industry factors | the market column | the rest |

Three notes the player should be able to make unprompted:

- **p.42 is `Cov/Var` literally.** `β̂` from a univariate regression of asset return on market
  return, with an intercept, *is* `Cov(r, r^M)/Var(r^M)` by Section 8c — with the wrinkle that
  (1.12) is exponentially weighted (*"half-life of 52 weeks, and uses 5 years of weekly
  observations"*, p.42), so the weighted version of Section 12a applies and the centring is a
  weighted centring. Same proof, `w` carried through.
- **p.42 and p.44 are the same regression read twice.** The slope becomes the Volatility substyle
  Historical Beta; the intercept becomes the Momentum substyle Historical Alpha (p.44: *"The
  Historical alpha from the exponentially weighted univariate regression (1.12)"*). **BFRE ships
  this level's intercept as a factor exposure in its own right.** If you had fitted (1.12) without
  an intercept, the Momentum style would be missing a descriptor and the Volatility style's would
  be wrong.
- **p.47 (1.30)–(1.31) is the boss round in production.** Normalised Earnings-to-Price replaces
  the latest EPS by `(α̂ + β̂·s)` — the fitted value of a five-year EPS-on-time regression at the
  most recent date. The boss round says that line passes through `(ū, EPS)`, the average time and
  the average EPS of the window. So "normalised EPS" is anchored on the five-year average EPS and
  tilted by the trend — which is why it smooths, and it is the reason the paper can call it
  normalised at all.

### 12e. Where it lands in the finished model

**p.24, equation (1.7):** `r = X f + u`. The column of ones is the market column, written first
in (1.9); the `a` of this level is its entry in `f`. **p.24, equation (1.8):** `Σ = X F Xᵀ + Δ`.

Follow the damage from getting this level wrong, concretely and in this order:

1. No intercept ⇒ `Σe ≠ 0` ⇒ the average return of the day has nowhere to go, so it is dumped into
   `u`. On the cold-open file that inflates `Σe²` by the factor `949/829 = 1.1448 (rounded)`.
2. `Δ` (Level 9) is built from `u`. Every asset's specific risk comes out about **7% too high** in
   standard-deviation units: `√(949/829) = 1.0699…`, an irrational number, and the verifier proves
   only the bracket `1.0699² < 949/829 < 1.0700²`.
3. There is now no market factor in `F` (Level 8), so the one source of covariance that touches
   every asset simultaneously has been reclassified as *idiosyncratic*. `Δ` is diagonal by
   assumption, so the common component of every pair of assets is silently set to zero.
4. Portfolio risk from (1.8) therefore comes out **too low for a diversified long book** — the
   market move that hits all of it at once has been modelled as `N` unrelated coin flips — while
   asset-level risk comes out too high. Both errors at once, in opposite directions, from one
   missing column of ones.

That is why the market factor is the first thing p.4 introduces and the first column of `X`.

### 12f. What the notes do NOT support

Searched all 65 transcribed pages in `notes/`:

- **`least squares`** — **zero hits** across all 65 pages. The paper never names the estimator it
  uses. (`OLS` appears three times — chunk_37-45 on (1.23), chunk_46-55 on (1.31) and on the
  Growth trend descriptors — and all three are the **transcriber's** symbol glosses, not quoted
  paper text.)
- **`covariance of`, `Cov(`, `centred`/`centered` in the estimation sense, `demeaned`,
  `column of ones`, `constant term`** — **zero hits.** Every mechanism in Sections 4 through 8 is
  used by BFRE and named by BFRE in none of them.
- **`intercept`** — six line-hits, on exactly **four pages**: p.26 (three lines — the
  identification passage, quoted in 12b), p.42 (α in 1.12), p.47 (α̂ in 1.31), p.52 (a_i in 1.49).
  All four pages are quoted above. **There is no page in `notes/` where the paper explains what an
  intercept does, or why it is there.**
- **A formula for `f_Mkt`** — **not printed anywhere.** p.4 gives it in words (*"cross-sectional
  average return… based on regression weights"*) and never as an equation. The identity
  `f_Mkt = Σw·r/Σw` verified in 12c is **our arithmetic on our invented weights**, reproducing the
  paper's verbal claim; it is not a number the paper prints.
- **The exact meaning of `ω` in (1.10)** — the transcription's gloss admits two readings, worked
  as A and B in 12c, and the two give different market factor returns (`1.10%` vs `1.508%` on our
  invented file). **No anchor in `notes/` resolves it directly.** p.4's verbal definition forces
  Reading A by implication, which is the inference made in 12c and flagged there as an inference.
- **Any statement that the fitted line passes through the weighted mean point** — **no anchor
  found.** The boss round's theorem is nowhere in the paper, although the paper depends on it in
  at least four places (12d).

So: the machinery of Level 5 sits underneath the market factor, the entire exposure
standardisation pipeline, the identification restrictions, Historical Alpha, Historical Beta,
Normalised Earnings-to-Price and every macro-economic beta — and the paper writes down none of it.
Say that to the player in these words: **this level is the most heavily used and least documented
piece of the whole model.**

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level5.py     # 341 exact-rational assertions, exits 0
```

The script recomputes every figure on this page from the raw `x`, `r` and `w` vectors in
`fractions.Fraction`, standard library only: the Level 0 recap and its parabola; the balance point
and the `Σe = n(r̄ − b·x̄)` identity; the 2×2 system solved by elimination, by Cramer and by a
generic weighted-least-squares solver; both residual vectors and both balance conditions; the
Frisch–Waugh derivation of `a` and of the `60/73` improvement; every centred sum and every
Cov/Var divisor; all six wrong methods with their exact outputs, their exact `Σe²` and their exact
excess over the optimum; the four column-rescalings; the entire boss round including the
`SS(a) = 19/10 + 4(a − 7/10)²` parabola, the `SS(m) = 14 − 22m + 10m²` family, the shift-cost
identity and the sabotage recovery; the weighted fit and the weighted standardised fit; and both
readings of restriction (1.10) with their factor returns, their identical residuals and their
different market factor returns.

It also brute-forces 11,950 cases: 7,680 three-asset files and 620 four-asset files confirming
`a = r̄ − b·x̄`, `Σe = 0` and `Σx·e = 0`; 49 `(a, b)` pairs confirming the completed square; 2,401
columns confirming `Σx² = Sxx + n·x̄²`; 81 weighted files confirming the weighted balance point;
729 (weights, restriction) pairs confirming that `f_Mkt` equals the weighted average return
exactly when the reduced industry columns are weighted-orthogonal to the constant, and does not
otherwise; and 390 (scale, column) pairs confirming `b → b/c` with `a` and the residuals fixed.

Every decimal printed by the script is tagged `exact` or `ROUNDED`; every value tagged `ROUNDED`
carries the word **rounded** on this page. If any printed value ever disagrees with this markdown,
the markdown is wrong.
