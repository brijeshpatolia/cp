# Level 6 — The Verdict

Every number below is recomputed in exact rational arithmetic by `tools/verify_level6.py`
(288 assertions, exits 0). Nothing here is rounded by hand. Where a decimal does not
terminate it is written with the word **rounded** next to it; every other decimal on this
page is exact.

> **Difficulty warning, stated up front because the rulebook demands it.**
>
> Three things on this page are **graduate-level** and are normally skipped even in good
> textbooks:
> - **Section 6c** — the proof that `E[e_i²] = (1 − h_i)·σ²`. Textbooks state this and
>   move on, or prove it with projection matrices the player has never seen. It is done
>   here with four lines of algebra and then *checked by enumerating all 32 worlds*.
> - **Section 6e** — why `n = k` breaks the estimate. This is the origin of the whole
>   degrees-of-freedom idea and almost nobody is shown it.
> - **Section 8f** — Markov's inequality, used to build a bar that BFRE's own Figure 1.8
>   can be measured against without assuming any distribution at all.
>
> Everything else on this page is ordinary algebra done carefully. If the player finds
> Section 6 heavy, that is correct calibration, not failure. Tell them so once, and keep
> going.
>
> **This is also the level the rulebook calls the hardest origin question in the game**
> (Victory Condition 3): *where does a standard error come from.* There is no way to answer
> it by turning a handle. It has to be built.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the cold-open file, reused here unchanged:

```
x = [−3/2, −1/2, 0, +1, +2]      Σx = 1     Σx² = 15/2     Σxr = 15     Σr = 4
r = [−2, −2, +1/2, +4, +7/2]  (percent)     Σr² = 73/2 = 36.5
b = Σxr/Σx² = 15/(15/2) = 2 exactly
e = r − 2x = [+1, −1, +1/2, +2, −1/2]       Σe = 2      Σx·e = 0      Σe² = 13/2
```

Also from Level 0, and used again in Section 7b: `SS(b) = 36.5 − 30b + 7.5b²`, with
`SS(0) = 36.5`, `SS(2) = 6.5`, and `SS(3/2) = SS(5/2) = 67/8 = 8.375` — the symmetry that
let the player find the minimum without calculus.

**From Level 1** — `b = Σxr/Σx²`, derived by nudging.
**From Level 2** — `Σx·e = 0`, the balance condition, forced by the arithmetic of minimising.
**From Level 3** — two columns need two balance conditions at once; the 2×2 system.
**From Level 4** — a coefficient is a *leftover*; near-duplicate columns wreck the split
while leaving the fit intact; `det = AC − B²`; VIF.
**From Level 5** — the intercept, centering, and the pivot moving to `x̄`.

Level 6 asks a question none of those levels can answer:

> `b = 2`. **So what?** Is 2 a real number or is it noise? How would we tell?

Three genuinely new things:

| | What Level 6 adds |
|---|---|
| **A second number for every coefficient** | Not just `b`, but *how far `b` would have moved if the world had rolled differently*. Built in Section 5 by enumerating 32 alternative worlds by hand — no formula assumed. |
| **A denominator nobody explains** | Why `Σe²` is divided by `n − k` and not by `n`. Proved in Section 6, and shown to be catastrophically wrong at `n = k`. |
| **One number that carries the verdict** | `t² = (S²/Q)/σ²`, with every piece named. Section 8 shows this is the same fact as `R²`, the same fact as the drop in the miss, and the same fact as "how many free directions' worth of miss did this column earn". |

---

## 1. The story — no mathematics

A man wants to know the going rate for a rickshaw, in rupees per kilometre.

He cannot ask, because nobody quotes a rate; they quote a fare. So he takes six rides,
notes the distance and the fare each time, and works out the single rate that best explains
all six fares at once. He gets ₹18 per kilometre.

Now: **is ₹18 the rate, or is ₹18 what this particular Tuesday happened to produce?**

He did not take six *random* rides out of the universe of possible rides. He took the six
rides he took. Each fare carried its own accidents — a driver who rounded up to the nearest
ten, a passenger who haggled, a diversion round a blocked lane, a monsoon surcharge that was
not mentioned. If he took six *different* rides tomorrow, every fare would be a little
different, and his answer would not be ₹18. It would be ₹17, or ₹19, or ₹22.

He wants to know how wide that "or" is. And here is the trap: **he cannot find out by taking
more rides**, because if he could take more rides he would just use them and have a better
answer. He has to work out the width of the "or" *from the six rides he already has.*

He can. The raggedness is visible in the file itself: the six fares do not sit exactly on any
single rate, and the size of the leftovers tells him how accident-prone a fare is. That is
half the answer.

The other half is subtler and it is the half people miss. Suppose all six rides were 200
metres long. Then each ride's accidents — a ₹10 rounding, say — get divided by 0.2 km to
become ₹50 per kilometre of apparent rate. Six short rides produce a rate estimate that
flails. Now suppose all six rides were 20 kilometres long. The same ₹10 rounding becomes
₹0.50 per kilometre. The estimate barely moves.

So:

> **The precision of a rate does not come from how many rides you took. It comes from how
> far apart the distances were.** Long rides pin a per-kilometre rate down. Short rides
> cannot, no matter how many of them you take.

And one more, which is the whole boss round:

> If every ride was 200 metres, you may still compute a rate — a very large one, per
> kilometre — and it will mean almost nothing, because nothing in your file ever travelled
> a kilometre.

Two things in the story are **assumptions**, and the player must be told so plainly before
anything is mapped:

1. The accidents on one ride have nothing to do with the accidents on another. (If the whole
   city had a fuel-price rise that Tuesday, this is false, and every number below is wrong.)
2. The accidents are about the same size on a short ride as on a long one. (If long rides
   are also more chaotic, this is false — and BFRE says on **p.25** that in equities it *is*
   false, and does something about it. Section 9 and Section 16d.)

---

## 2. Mapping the story onto the fit, line by line

| In the story | In the fit |
|---|---|
| one ride | one stock |
| the distance of that ride | that stock's exposure `x_i` |
| the fare | that stock's return `r_i` |
| the going rate, ₹/km | the factor return `b` |
| the accidents on ride *i* | that stock's miss `e_i` |
| "how accident-prone is a fare" | `σ²`, the typical squared miss |
| "how far apart were the distances" | `Q = Σx²` |
| "how wide is the *or*" | `Var(b)` — the thing this level builds |
| a 200-metre ride | a stock with `x` near zero |
| **a ride of exactly zero metres** | **CHR**, `x = 0`. Its fare is pure accident and it changes the rate not at all. |
| "you cannot find the width by taking more rides" | you only ever get one cross-section per month |

That CHR row is the one to point at. CHR was Level 0's hook — the stock no `b` can predict.
In Level 6 it earns a second job: **CHR's miss carries zero weight in the answer.** Whatever
happens to CHR, `b` does not move. Section 4c proves it with a return of +100.5%.

---

## 3. The dataset

Unchanged from the cold open. The player already owns every number in the first block.

| Stock | Cheapness score `x` | Return `r` | Miss at `b = 2`, `e = r − 2x` |
|---|---:|---:|---:|
| AXL | −1.5 | −2.0% | **+1.0** |
| BRN | −0.5 | −2.0% | **−1.0** |
| CHR | 0.0 | +0.5% | **+0.5** |
| DLT | +1.0 | +4.0% | **+2.0** |
| EMK | +2.0 | +3.5% | **−0.5** |

```
n = 5 stocks        k = 1 column        Q = Σx² = 15/2        S = Σxr = 15
b = S/Q = 2         Σe = 2              Σx·e = 0              SSE = Σe² = 13/2
Σ|e| = 5            Σr² = 73/2 = 36.5
```

---

## 4. Where the wobble comes from — the algebra, before any probability

### 4a. The one line the whole level rests on

Write the return of each stock as *the part a dial can reach* plus *everything else*:

```
r_i  =  b·x_i  +  e_i
```

That is not a model assumption yet — it is the definition of `e_i`. Now push it through the
Level 1 formula:

```
b̂  =  Σx r / Σx²
    =  Σ x(bx + e) / Σx²
    =  b·(Σx²)/(Σx²)  +  Σ x e / Σx²
```

so

```
        ┌──────────────────────────────┐
        │   b̂  =  b  +  Σ x·e / Σx²   │
        └──────────────────────────────┘
```

**The estimate is the truth plus a weighted sum of the misses.** Nothing else. If the misses
had come out differently, `b̂` would have come out differently — by exactly that second term.

The verifier checks this on the actual file: `Σxr = 2·Q + Σx·e`, i.e. `15 = 15 + 0`.

### 4b. The weights, and CHR's zero

Write the second term as `Σ w_i e_i` with

```
w_i = x_i / Q            w = [ −1/5,  −1/15,  0,  +2/15,  +4/15 ]
```

Three facts, all exact, all checked:

```
Σ w_i x_i = 1            ← a pure signal passes through untouched
Σ w_i     = 2/15         ← NOT zero (no intercept; Level 5 lives here)
Σ w_i²    = 2/15 = 1/Q   ← this is the number that becomes the standard error
```

`Σ w x = 1` is the defining property of the weights: if every `e_i` were zero, `b̂` returns
`b` exactly. `Σw² = 1/Q` is the one to underline — it will be the entire formula in Section 5d.

**CHR's weight is exactly 0.** Its miss cannot move the answer.

### 4c. Nudge one return and watch `b` move by exactly `w_i`

This is a **round type A (predict-then-reveal)**. Ask for a direction and a rough size first.

| Change | New `S = Σxr` | New `b` | Move | Equals `w_i` |
|---|---:|---:|---:|---|
| add +1.0% to **DLT** (`x = +1`) | 16 | 32/15 = 2.1333 (rounded) | +2/15 | `w₄ = 2/15` ✓ |
| add +1.0% to **EMK** (`x = +2`) | 17 | 34/15 = 2.2667 (rounded) | +4/15 | `w₅ = 4/15` ✓ |
| add **+100.0%** to **CHR** (`x = 0`) | 15 | **2** | **0** | `w₃ = 0` ✓ |

CHR's return could be **+100.5%** and `b` would still be exactly 2. That is the sentence to
make the player say back.

### 4d. Leverage, and a fact that will matter enormously in Section 6

Define `h_i = w_i·x_i = x_i²/Q`:

```
h = [ 3/10,  1/30,  0,  2/15,  8/15 ]          Σ h = 1
```

`h_i` is stock *i*'s share of the total spread — how much of the column's "long rides" it
personally supplies. EMK alone supplies 8/15 of it. CHR supplies none.

**The leverages sum to `k`, the number of columns.** Here `k = 1` and `Σh = 1`. Hold onto
that: it is the entire reason the denominator is `n − k`.

*(The name for `h_i` is unlocked in Section 12.)*

---

## 5. The 32 worlds — computing a standard error by enumeration, not by formula

The rulebook forbids handing over a formula. So this section does not use one. It counts.

### 5a. The experiment

We cannot re-run the month. But we can ask a sharply-defined question that the file *can*
answer:

> **The five misses came out `+1, −1, +0.5, +2, −0.5`. Suppose the sizes were fated but the
> directions were coin flips. In how many different places could `b` have landed?**

That is 2⁵ = **32 alternative worlds**. World `s = (s₁ … s₅)` has returns
`r_i = 2x_i + s_i·e_i`, and we refit from scratch in each one.

The arithmetic per world is trivial, because Section 4a already did it:

```
b̂(s) = 2 + Σ s_i x_i e_i / Q ,        x_i e_i = [ −3/2, +1/2, 0, +2, −1 ]
```

Note `Σ x_i e_i = 0` — that is Level 2's balance, and it is why the *observed* world sits at
exactly `b = 2`.

### 5b. All 32 answers

| `b̂` | 4/3 | 22/15 | 8/5 | 26/15 | 28/15 | **2** | 32/15 | 34/15 | 12/5 | 38/15 | 8/3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| decimal *(rounded)* | 1.3333 | 1.4667 | 1.6000 | 1.7333 | 1.8667 | **2.0000** | 2.1333 | 2.2667 | 2.4000 | 2.5333 | 2.6667 |
| how many of the 32 | 2 | 2 | 2 | 4 | 4 | **4** | 4 | 4 | 2 | 2 | 2 |

Eleven distinct answers, spread from **4/3 to 8/3**. The same five stocks, the same five miss
*sizes*, and `b` ranges from 1.33 to 2.67.

**Every count is even.** That is CHR again: flipping CHR's miss changes the returns and
changes nothing else, so the 32 worlds are really 16 answers, each arriving twice. The
verifier confirms both `(+,+,+,+,+)` and `(+,+,−,+,+)` give `b = 2` while CHR's own residual
flips from `+1/2` to `−1/2`.

### 5c. The two numbers that summarise the 32

```
average of b̂ over the 32 worlds                = 2        exactly
average of (b̂ − 2)² over the 32 worlds         = 2/15     exactly
√(2/15)                                        = 0.365148 (rounded)
```

The average is the truth — the procedure is not tilted. The average squared deviation is the
answer to "how wide is the *or*". **That is a standard error, computed by counting.**

### 5d. Now the formula falls out, and it is not a new idea

Why did it come to `2/15`? Because the cross terms cancelled. In
`(Σ s_i x_i e_i)²` every term `s_i s_j (x_ie_i)(x_je_j)` with `i ≠ j` is `+` in exactly half
the worlds and `−` in the other half, so it contributes nothing to the average. Only the
squares survive:

```
average of (b̂ − 2)²  =  Σ (x_i e_i)² / Q²  =  Σ x_i² e_i² / Q²
```

and on this file `Σ x_i² e_i² = 9/4 + 1/4 + 0 + 4 + 1 = 15/2`, so the answer is
`(15/2)/(15/2)² = 2/15`. ✓ *(checked against the enumeration.)*

Now add the second assumption from the story — **every miss is about the same size**, call
that common size `σ²` — and `Σ x_i²e_i²` becomes `σ²·Σx_i² = σ²·Q`, so

```
        ┌───────────────────────────┐
        │     Var(b̂)  =  σ² / Q     │
        └───────────────────────────┘
```

Read it as the story: **accident-proneness on top, spread-of-distances underneath.**
More raggedness → wider. More spread in `x` → narrower. Number of stocks appears nowhere,
except through `Q`.

### 5e. The two assumptions, named as assumptions

The rulebook says name the bedrock when you reach it. This is bedrock.

| Assumption | What breaks if it is false | Where the game deals with it |
|---|---|---|
| **the misses are unrelated to each other** (cross terms average to zero) | if two stocks miss together, the wobble is bigger than `σ²/Q` says and every t-stat is overstated | this is *exactly* the "`D` is diagonal" assumption — **Level 9** |
| **the misses are all about the same size** | high-`x` stocks with big misses dominate, and `σ²/Q` is the wrong width | **Section 9** below, and BFRE **p.25** |

Neither is proved. Neither can be. They are choices, and a working quant knows they are
choices.

---

## 6. Degrees of freedom — why `n − k` and not `n`

We now need `σ²`, the typical squared miss. The obvious candidate is `Σe²/n = (13/2)/5 = 13/10`.
It is wrong, and this section shows exactly how wrong, and why.

### 6a. The misses are not free

Level 2 forced `Σx·e = 0`. So the five residuals are **not** five independent numbers. Give
me any four of them and the fifth is arithmetic:

```
x₁e₁ + x₂e₂ + x₃e₃ + x₄e₄ = (−3/2)(1) + (−1/2)(−1) + 0·(1/2) + (1)(2) = 1
so  2·e₅ = −1  →  e₅ = −1/2      ← which is the residual we actually have ✓
```

One column, one balance condition, one residual determined. `k` columns, `k` conditions,
`k` determined. Only `n − k` of the misses were ever free to be anything.

*(Note: the pinned one need not be a particular stock. CHR's residual is not pinned at all —
its `x` is 0, so it does not appear in the condition. The constraint removes one **direction**,
not one named stock.)*

### 6b. A world where we know `σ²` exactly, so we can catch the error red-handed

Take the same five stocks and the same column `x`. Let the true dial be `b = 2` and let each
stock's miss be **exactly ±1**, direction by coin flip. Then `σ² = 1` **exactly, by
construction** — we are no longer estimating it, we know it. Enumerate all 32 worlds again:

```
average of b̂                     = 2        ✓ (unbiased)
average of (b̂ − 2)²              = 2/15     ✓ = σ²/Q = 1/(15/2)
```

The formula from 5d survives contact. Now look at the residuals *after fitting*.

### 6c. `E[e_i²] = (1 − h_i)·σ²` — the shrinkage, proved and then counted

**The algebra** (this is the graduate-level bit; it is four lines).

After fitting, stock *i*'s residual is not its true miss `ε_i`. It is

```
e_i = ε_i − x_i(b̂ − b) = ε_i − x_i·Σ_j w_j ε_j
    = ε_i(1 − x_i w_i) − x_i·Σ_{j≠i} w_j ε_j
    = ε_i(1 − h_i)     − x_i·Σ_{j≠i} w_j ε_j
```

Square it and average. Cross terms vanish (assumption 1). So

```
E[e_i²] = (1 − h_i)²σ² + x_i²·(Σw² − w_i²)·σ²
        = σ²[ (1 − h_i)² + h_i − h_i² ]          using x_i²Σw² = x_i²/Q = h_i and x_i²w_i² = h_i²
        = σ²[ 1 − 2h_i + h_i² + h_i − h_i² ]
        = σ²(1 − h_i)                                                        ∎
```

**The count.** Averaging `e_i²` over the 32 equal-size worlds, stock by stock:

| Stock | `h_i` | `1 − h_i` | measured `E[e_i²]` over 32 worlds |
|---|---:|---:|---:|
| AXL | 3/10 | 7/10 | **7/10** ✓ |
| BRN | 1/30 | 29/30 | **29/30** ✓ |
| **CHR** | **0** | **1** | **1** ✓ |
| DLT | 2/15 | 13/15 | **13/15** ✓ |
| EMK | 8/15 | 7/15 | **7/15** ✓ |

Read the table, because it says something a working quant needs to know:

- **CHR is untouched.** `h = 0`, so its residual is never shrunk. The fit cannot reach it, so
  the fit cannot hide its error either.
- **EMK's residual is shrunk hardest.** Its average squared miss is only `7/15` of the true
  `σ² = 1`. It supplies `8/15` of the spread, so the line swings towards it, and **it hides
  more than half its own error**. High-leverage stocks flatter the model fitted to them.

### 6d. And therefore the denominator

```
E[SSE] = Σ E[e_i²] = Σ (1 − h_i)·σ² = (n − Σh)·σ² = (n − k)·σ²
```

because `Σh = k` (Section 4d). On this file:

```
E[SSE] over the 32 worlds  =  4        exactly       and n − k = 5 − 1 = 4 ✓

divide by n = 5     →  4/5 = 0.8       but σ² = 1.   Understated by 1/5 = 20%.
divide by n − k = 4 →  4/4 = 1         = σ²           exactly right.
```

That is the whole justification. It is not a convention and not a fudge: **fitting steals
exactly `h_i` of each stock's error, and the thefts add to exactly `k`.**

### 6e. The degenerate case: `n = k`, where `/n` becomes absurd

Four stocks. Four columns, chosen so they do not overlap at all:

```
c₁ = [+1, +1, −1, −1]      c₂ = [+1, −1, +1, −1]
c₃ = [+1, −1, −1, +1]      c₄ = [+1, +1, +1, +1]
```

*(New letter on purpose: `h` is already taken by leverage. These are columns.)*
Every `Σc_j² = 4`; every pair has `Σc_i·c_j = 0`. True dials all zero, misses `ε_i = ±1`,
so again `σ² = 1` exactly. All 2⁴ = **16 worlds**, fitted with the first `k` columns:

| `k` | `E[SSE]` | `n − k` | `E[SSE]/n` | vs the true `σ² = 1` | worlds (of 16) with `SSE` exactly 0 |
|---:|---:|---:|---:|---|---:|
| 1 | **3** | 3 | 3/4 | 25% too small | 2 |
| 2 | **2** | 2 | 1/2 | 50% too small | 4 |
| 3 | **1** | 1 | 1/4 | 75% too small | 6 |
| 4 | **0** | 0 | 0 | **100% too small** | **16** |

The last row is the punchline. With four columns and four stocks:

- `SSE = 0` in **every single one of the 16 worlds**. The fit is perfect, always.
- The `/n` rule reports `σ̂² = 0/4 = 0`: *"the world never wobbles."* We know for a fact that
  every miss was ±1. The answer is not approximately wrong, it is **maximally wrong**.
- The `/(n − k)` rule reports `0/0` — **undefined**. Which is the honest answer: this file
  contains no information whatsoever about `σ²`, and any procedure that returns a number here
  is lying.

Notice also that each extra column costs exactly **one**: 3 → 2 → 1 → 0. Not "a bit". Exactly
one. That is `Σh = k` again, seen from the other side.

### 6f. Two traps that live in this exact spot

**Trap 1 — "so it's `n − 1`."** On the cold open, `n − k = 4` and `n − 1 = 4`. They coincide
**only because `k = 1`.** A player who reads off "subtract one" has learned nothing, and the
boss round will punish it: there `n = 6`, `k = 2`, `n − k = 4`, while `n − 1 = 5`.

**Trap 2 — "the intercept is free."** It is not. An intercept is a column of ones. It costs a
degree of freedom like any other column. In Section 8's `√n` example `k = 1` and the one
column *is* the intercept, which is why `n − 1` is correct **there**.

---

## 7. The standard error, and the number

### 7a. Build the shape before seeing it (round type C)

Hand the player only the units:

- `b` is in **percent per unit of score**.
- `σ` is in **percent**.
- `Q = Σx²` is a **pure number** (scores squared).

> *You need a number in the same units as `b`. You have a percent and a pure-number-squared.
> What must the formula look like?*

There is only one shape: `SE = σ/√Q`. And `Var(b) = σ²/Q`, exactly Section 5d.

### 7b. The arithmetic, on the file

```
SSE = Σe²          = 13/2
df  = n − k        = 5 − 1 = 4
σ̂²  = SSE/df       = (13/2)/4 = 13/8   = 1.625            exact
σ̂                 = √(13/8)           = 1.274755          (rounded)   ← "typical miss ≈ 1.27%"
Var(b) = σ̂²/Q      = (13/8)/(15/2) = 13/60 = 0.216667      (rounded)
SE(b)  = √(13/60)                     = 0.465475           (rounded)
t = b/SE = 2/0.465475                 = 4.296689           (rounded)
t² = b²/Var(b) = 4/(13/60)            = 240/13 = 18.461538 (rounded)   ← exact as a fraction
```

**`b = 2` sits 4.30 standard errors away from zero.** Under the paper's own rule on **p.8**
(`|t| > 2`), that is a keeper.

### 7c. More data, for calibration (round type A)

Ask the player to predict before revealing: *the same five names, replicated so we have 25
stocks with the identical pattern. What happens to `b`, and to `t`?*

```
n = 25    Q = 5·(15/2) = 75/2    S = 5·15 = 75    b = 2          ← unchanged, exactly
SSE = 5·(13/2) = 65/2            df = n − k = 25 − 1 = 24         ← still k = 1; NOT 5·4 = 20
σ̂² = (65/2)/24 = 65/48           Var(b) = 13/360
SE = √(13/360) = 0.190029 (rounded)      t² = 1440/13      t = 10.524696 (rounded)
```

`t²` went up by exactly **6**, so `t` went up by `√6 = 2.449490` (rounded). Not by `√5`.
Where the sixth comes from, exactly: `Q` grew by 5, but `SSE` also grew by 5 while `df` grew
by **6** (4 → 24), so `σ̂²` *fell* by `5/6` — from `13/8` to `65/48`. Multiply: `Var(b)` shrank
by `5 × 6/5 = 6`. A player who says "√5" has the right instinct and has forgotten that `df`
grows faster than `SSE` when `k` stays put; give partial bps and show them the 6.

---

## 8. `t`, and the identity `t² = (S²/Q)/σ²`

### 8a. The identity, with every piece named

Start from what is already built and substitute:

```
b = S/Q                       Var(b) = σ²/Q

        b²        (S/Q)²        S²/Q²        S²
t²  =  ─────  =  ────────  =  ────────  =  ──────
       Var(b)      σ²/Q         σ²/Q        Q·σ²
```

```
        ┌────────────────────────────┐
        │     t²  =  (S² / Q) / σ²   │
        └────────────────────────────┘
```

**The pieces, named — this is the part of the level the rulebook is testing.**

| Piece | Formula | What it is, in words |
|---|---|---|
| `S` | `Σ x·r` | **the signal sum** — how strongly the column and the returns move together |
| `Q` | `Σ x²` | **the leverage sum** — how far apart the "ride distances" were |
| `S²/Q` | `= b²Q` | **the earned miss** — how much of the total miss the dial actually removed |
| `σ²` | `SSE/(n − k)` | **the going rate** — how much miss one free direction is worth |
| `t²` | earned ÷ going rate | **how many free directions' worth of miss this one dial earned** |

On the file:

```
S = 15      S² = 225      Q = 15/2      S²/Q = 30      σ̂² = 13/8
t² = 30 / (13/8) = 240/13 = 18.461538 (rounded)      ✓ same as Section 7b
```

### 8b. `S²/Q` is a number the player computed three levels ago

From Level 0's parabola: `SS(0) = 36.5`, `SS(2) = 6.5`.

```
drop in the miss = SS(0) − SS(2) = 36.5 − 6.5 = 30 = S²/Q      ✓ exactly
```

So `t²` is literally **"the drop in the miss, divided by the going rate per free direction."**
Level 0's `36.5 − 6.5 = 30` was the numerator of Level 6's verdict, sitting in plain sight
for six levels.

### 8c. `R²` and `t²` are the same fact twice (CALL BACK)

```
R² = (drop)/(total) = 30/36.5 = 60/73 = 0.821918 (rounded)     1 − R² = 13/73

(n − k)·R²/(1 − R²) = 4·(60/73)/(13/73) = 240/13               ✓ = t²
```

Not "related to". **Equal.** A player who has `R²` and `df` already has `t²` and does not know
it, and vice versa. For one column this quantity has a second name (Section 12).

Be precise about the scope, because it matters at the boss round: this identity is exact for
**one** column. BFRE's `R²` on **p.32** is the *whole-model* figure — "the proportion of
cross-sectional variation in asset returns explained by the set of common factors" — while the
t-statistics on **p.8** and **p.14** are *per-factor*. So they are not literally the same
number in the paper; they are the same *machine*, run once on all columns together and once on
each column separately. The multi-column version of `t²` is a topic this level does not open.

### 8d. `t` is scale-free; `b` is not

Multiply a column by 100 (report it in percent instead of as a decimal). Then `b` divides by
100 and `SE` divides by 100, so **`t` does not move at all**. Verified numerically on the boss
data in Section 14.6, row 1: `b_g = 40 → 0.4`, `SE = 38.729833 → 0.387298` (both rounded), `t² = 16/15`
in both.

This is the single most important sentence in the boss round:

> **A coefficient's size is partly a fact about the world and partly a fact about the units.
> A t-statistic is only a fact about the world.**

### 8e. What `t = 1` actually means — the baseline nobody states

Go back to the 32 equal-size worlds of Section 6b, where `σ² = 1` is known. In each world,
compute how much miss the fitted dial earned *beyond the true dial*: `(b̂ − b)²·Q`. That is the
part the column earned **purely by luck**, because the true dial was already accounted for.

```
average of (b̂ − b)²·Q over the 32 worlds  =  1  =  σ²        exactly
```

Which is the same statement as `E[SSE] = (n−k)σ²`, seen from the other end: the one degree of
freedom the column consumed is worth exactly `σ²` of miss, and a column with no real effect
collects exactly that much on average.

> **`t² = 1` means: this column earned back exactly what a coin-flip column earns on average.
> `t = 1` is not weak evidence. It is the definition of no evidence.**

Honest small print, because the rulebook demands it. That `E[t²] = 1` uses the **true** `σ²`.
If you use the **estimated** `σ̂²` — which is what anyone actually does — `σ̂²` is itself
wobbling, and in these 32 worlds the exact average comes out to

```
E[t²] with σ̂² and df = 4   =  6700356/3995947  =  1.676788   (rounded)
```

bigger than 1. As `df` grows, `σ̂²` stops wobbling and `E[t²]` returns to 1 — **that step is
the law of large numbers and this level does not build it. Flag it to the player as an IOU.**
With BFRE's cross-sections (thousands of stocks) `df` is enormous and `E[t²] ≈ 1` is safe.

### 8f. A bar that needs no distribution at all (graduate-level, and worth it)

The player has no bell curve, no tables, no p-values, and does not need them for this.

**Markov's inequality, proved in two lines for a 12th-standard student.** Let `Z ≥ 0` and let
a fraction `φ` of the worlds have `Z ≥ 4`. Those worlds alone contribute at least `4φ` to the
average of `Z`; the rest contribute at least 0. So `E[Z] ≥ 4φ`, i.e.

```
φ  ≤  E[Z]/4
```

Put `Z = t²`. If a factor is worthless then `E[t²] = 1` — using the true `σ²`, so this needs
`df` large enough that `σ̂²` has settled down (8e); BFRE's cross-sections easily qualify. Then

```
        ┌──────────────────────────────────────────────────────────────┐
        │  A worthless factor cannot show |t| > 2 in more than 1/4     │
        │  = 25% of months. No distribution assumed.                    │
        └──────────────────────────────────────────────────────────────┘
```

Check it against the 32-world enumeration: 4 worlds out of 32 have `t² ≥ 4`, i.e. `1/8 = 12.5%`,
comfortably under the bound (which is `1.676788/4 = 0.419197`, rounded, at `df = 4`). The bound
is valid and loose — say so; a bound that is never violated and rarely tight is exactly what a
bound is.

This is used against the paper itself in Section 16c.

---

## 9. Unequal wobble sizes (graduate-level aside — flag it, then do it)

Section 5c computed a wobble using **each stock's own observed miss size**. Section 7b computed
one using **a single shared `σ̂²`**. On this file they happen to agree in a way that could
mislead:

```
Σ x_i² e_i² = 15/2      and      Σ x_i² = Q = 15/2       ← equal, by accident of this data
```

so the enumerated wobble is `(15/2)/(15/2)² = 2/15 = 8/60`, while the shared-`σ̂²` route gives
`13/60`. The ratio is exactly `13/8 = 1.625` — and that `13/8` is `σ̂²` itself, which is the tell
that the agreement was arithmetic luck, not a law.

The enumerated version corresponds to `t² = b²/(2/15) = 30` exactly, `t = √30 = 5.477226`
(rounded) — noticeably bigger than 4.296689.

**A three-asset file where they disagree by a factor of 3**, small enough to check on paper:

```
x = [+1, +1, −2]      r = [+2, 0, −2]
Q = 6      S = 6      b = 1      e = [+1, −1, 0]      Σx·e = 0 ✓      SSE = 2
df = 3 − 1 = 2        σ̂² = 1

shared-σ̂² route :  Var(b) = σ̂²/Q          = 1/6   ≈ 0.1667 (rounded)
own-size route  :  Var(b) = Σx²e²/Q² = 2/36 = 1/18 ≈ 0.0556 (rounded)
ratio           :  exactly 3
```

Two defensible answers, three times apart, from the same six numbers. Which one is right
depends entirely on whether you believe assumption 2 of Section 5e. **Names for both are
unlocked in Section 12.** BFRE's position on this is explicit and is quoted in Section 16d.

---

## 10. Traps, and exactly what each wrong belief returns numerically

All on the cold open, `b = 2`, `Q = 15/2`, `SSE = 13/2`.

| Wrong belief | What it returns | The refutation |
|---|---|---|
| "divide by `n`": `σ̂² = (13/2)/5 = 13/10` | `SE = 0.416333`, **`t = 4.803845`** (both rounded) | `t²` ratio is exactly `5/4`, so `t` is too big by `√(5/4) = 1.118034` (rounded) — 11.8%. Section 6e shows this rule returning `0` when the truth is `1`. |
| "always divide by `n − 2`": `σ̂² = 13/6` | `SE = 0.537484`, **`t = 3.721042`** (rounded) | `t²` ratio `3/4`, too small by `√(3/4) = 0.866025` (rounded). The `2` came from nowhere. |
| "always `n − 1`" | on this file, right by luck (`n−k = n−1 = 4`) | On the boss file it gives `t_g = 1.1547` instead of `1.0328` (rounded). It is `n − k`. |
| "`SE` is just the typical miss": `SE = σ̂ = 1.274755` | `t² = 32/13`, **`t = 1.568929`** (rounded) | Units. `σ̂` is in percent; `b` is percent per unit of score. Never divided by `√Q`. |
| "`SE = σ̂/√n`" (the school formula, applied blind) | `√(13/40) = 0.570088`, `t² = 160/13`, **`t = 3.508232`** (rounded) | Right only when `Q = n`. Here `Q = 15/2 ≠ 5`. Section 8 shows the case where it *is* right. |
| "use average absolute miss": `Σ|e|/(n−k) = 5/4` | `SE = √(5/24) = 0.456435`, `t² = 96/5`, **`t = 4.381780`** (rounded) | Level 0 settled which loss function a risk model uses. Changing it here quietly changes the loss function. |
| "a bigger `b` means a stronger factor" | `b_g = 40` with `t = 1.03` in Section 14 | `b` carries the column's units; `t` does not (8d). |
| "`t` near 1 is weak evidence for the factor" | — | It is exactly *no* evidence: a worthless column scores `E[t²] = 1` (8e). |
| "insignificant means zero" | boss round: `b_g ∈ [−37.46, +117.46]` (rounded) | The same data are consistent with `b_g` being **three times larger**. (14.6) |
| "more stocks always sharpens `b`" | 25 copies → `t` up by `√6` | Adding stocks at `x = 0` adds **nothing**: `Q` is unchanged, so `Var(b)` is unchanged. Spread, not count. |
| "the residuals are `n` independent numbers" | `σ̂²` understated by `k/n` | Give me four of the five and I compute the fifth (6a). |
| "a perfect fit means a precise estimate" | `n = k`: `SSE = 0` in all 16 worlds | Perfect fit with `n = k` means **zero information**, not infinite precision (6e). |

---

## 11. A sabotage round (round type B) to run before the boss

Hand the player this desk file, told it is a finished piece of work, and say one number in it
is corrupted:

```
n = 5     k = 1     b = 2      SSE = 13/2      df = 4
σ̂² = 13/8         Q = 15/2         Var(b) = 13/60        SE = 0.465475 (rounded)
t = 4.296689 (rounded)                 R² = 0.75
```

`R²` is the lie. The player should catch it **without** recomputing `Σr²`, via 8c:

```
t² = 240/13 = 18.461538 (rounded)   ⇒   R²/(1−R²) = t²/df = 60/13   ⇒   R² = 60/73 = 0.821918
```

`0.75` is impossible given the other numbers on the page. This is the structural check a real
desk runs: `t²`, `R²` and `df` are three views of two numbers, and they must agree.

---

## 12. Names unlocked at the end of this level

Locked until now on purpose. Each is now attached to something the player built.

| Name | What it actually is, in this level's terms |
|---|---|
| **standard error** | `√Var(b̂)` — the width of the spread of the 32 answers in 5b |
| **sampling distribution** | the table in 5b itself: the set of answers the procedure could have produced |
| **unbiased** | the average of that table is the truth (`= 2`, exactly) |
| **residual variance / mean squared error** | `σ̂² = SSE/(n − k)` |
| **degrees of freedom** | `n − k` — how many of the misses were free to be anything (6a) |
| **leverage `h_i`** | `x_i²/Q` — stock *i*'s share of the spread; `Σh = k`; shrinks its own residual to `(1−h_i)σ²` |
| **t-statistic** | `b/SE` — how many wobble-widths the answer sits from zero |
| **the null** | "this column's true dial is zero" — the world in which `E[t²] = 1` |
| **statistically significant** | BFRE's own convention, **p.8**: `|t| > 2` |
| **confidence interval** | `b ± 2·SE` — the values that would not have been rejected |
| **F-statistic** | `t²` when one column is tested: earned miss ÷ going rate (8a) |
| **power** | the ability to detect a real effect. `df = 4` and low `Q` means almost none — 14.6 |
| **homoskedasticity** | assumption 2 of 5e: all misses the same typical size |
| **heteroskedasticity** | its failure — Section 9, and BFRE **p.25** |
| **robust / sandwich / White standard error** | the "own-size" route of Section 9: `Σx²e²/Q²` instead of `σ̂²/Q` |
| **omitted-variable bias** | 14.6: dropping `g` moves `b_x` by exactly `b_g·B/C` |

Run a **round type F (vocabulary under fire)** on: *"the coefficient is economically large but
statistically insignificant, and the standard errors aren't robust."* Plain English, then a
fresh sentence of their own.

---

## 13. Ladder position after this level

| Concept | Tier to demand |
|---|---|
| `b̂ = b + Σxe/Σx²` | 3 (derive) — must be reproducible from nothing |
| `Var(b) = σ²/Q` | 4 (defend) — including *why* `n` does not appear |
| degrees of freedom, `n − k` | 4 (defend) — including the `n = k` case |
| `E[e_i²] = (1 − h_i)σ²` | 3 (derive) is enough; tier 4 is a bonus |
| `t² = (S²/Q)/σ²` with pieces named | **5 (rebuild)** — this is the level's gate |
| `t² = df·R²/(1−R²)` | 3 (derive) |
| heteroskedasticity / robust SE | 2 (compute) is acceptable this level |
| Markov bar | 3 (derive) |

Do not mark Level 6 complete unless the player can produce Section 8a's table of named pieces
**unprompted**, on a column they have never seen.

---

# 14. BOSS ROUND — The Verdict

Round type: **E. INTERROGATION**. Play a Chief Risk Officer with thirty years on the desk.
The player must argue **for** dropping the factor, then **against**, and both arguments must
come out of the file — not out of adjectives.

## 14.1 The setup, as the player receives it

A junior researcher has submitted a note. It says:

> *"The buyback ratio is the most powerful factor on the desk. Its coefficient is **40** —
> forty times the size of the cheapness coefficient. Recommend adding it to the model."*

Six stocks, one month, two columns. `g` is the buyback ratio, reported **in its raw units, as
a decimal fraction** — it has not been standardised. `x` is the familiar cheapness score.

| Stock | Buyback ratio `g` | Cheapness `x` | Return `r` |
|---|---:|---:|---:|
| PRM | −0.02 | −3 | −4.3% |
| QNT | −0.01 | −2 | −2.9% |
| ROV | +0.01 | −1 | +0.4% |
| SLT | −0.01 | +1 | +1.6% |
| TDR | +0.01 | +2 | +1.9% |
| URS | +0.02 | +3 | +3.3% |

Both columns sum to zero. `n = 6`, `k = 2`.

## 14.2 The cross-products (a minute by hand)

```
A = Σg²  = (4+1+1+1+1+4)/10000 = 12/10000 = 3/2500 = 0.0012
B = Σg·x = (6+2−1−1+2+6)/100   = 14/100   = 7/50   = 0.14
C = Σx²  = 9+4+1+1+4+9         = 28
p = Σg·r = 0.086+0.029+0.004−0.016+0.019+0.066 = 0.188 = 47/250
q = Σx·r = 12.9+5.8−0.4+1.6+3.8+9.9           = 33.6  = 168/5
Σr²      = 18.49+8.41+0.16+2.56+3.61+10.89    = 44.12 = 1103/25

det = AC − B² = 84/2500 − 49/2500 = 35/2500 = 7/500 = 0.014
```

## 14.3 The fit (Level 3's machinery, unchanged)

```
b_g = (Cp − Bq)/det = (5.264 − 4.704)/0.014 = 0.56/0.014  = 40      exactly
b_x = (Aq − Bp)/det = (0.04032 − 0.02632)/0.014 = 0.014/0.014 = 1   exactly

e = r − 40g − 1·x = [ −1/2, −1/2, +1, +1, −1/2, −1/2 ]
Σe = 0        Σg·e = 0 ✓        Σx·e = 0 ✓        SSE = Σe² = 3
```

Both balance conditions hold, so the fit is genuine and the file is not sabotaged.

## 14.4 The verdict numbers

```
df = n − k = 6 − 2 = 4              (NOT n − 1 = 5)
σ̂² = SSE/df = 3/4 = 0.75            σ̂ = √(3/4) = 0.866025 (rounded)

Var(b_g) = σ̂²·C/det = (3/4)(28)/(7/500) = 1500        SE(b_g) = √1500 = 38.729833 (rounded)
Var(b_x) = σ̂²·A/det = (3/4)(3/2500)/(7/500) = 9/140   SE(b_x) = √(9/140) = 0.253546 (rounded)

t_g² = 40²/1500  = 16/15  = 1.066667 (rounded)    t_g = 1.032796 (rounded)
t_x² = 1²/(9/140)= 140/9  = 15.555556 (rounded)   t_x = 3.944053 (rounded)
```

**The coefficient is 40 times bigger and the t-statistic is 3.82 times smaller**
(`t_x/t_g = √(175/12) = 3.818813`, rounded).

Where it comes from, in one line, using the two-column form of Section 8a's identity —
each column's `t²` is *its own* earned miss over the going rate:

```
t_g² = b_g²·(det/C)/σ̂²        det/C = 1/2000 = 0.0005      ← g's effective leverage
t_x² = b_x²·(det/A)/σ̂²        det/A = 35/3 = 11.666667 (rounded)   ← x's effective leverage
```

`det/C` versus `det/A`: `C/A = 70000/3 ≈ 23333.333` (rounded). **The cheapness column carries
about twenty-three thousand times the leverage of the buyback column, because buyback is
reported in units where nobody in the file moves very far.** Every ride was 200 metres long.

Two supporting numbers for the interrogation:

```
overlap:  cos² = B²/(AC) = 7/12 = 0.583333 (rounded)    cos = 0.763763 (rounded)
          VIF  = 1/(1 − cos²) = 12/5 = 2.4              ← Level 4's number, moderate
leverages h = [13/35, 1/7, 17/35, 17/35, 1/7, 13/35]    Σh = 2 = k  ✓
```

## 14.5 THE CASE FOR DROPPING `g` — every claim a number

Drop `g`, refit on `x` alone:

```
b_x alone = q/C = 33.6/28 = 6/5 = 1.2
SSE       = Σr² − q²/C = 44.12 − 40.32 = 3.8 = 19/5
```

| Argument | The number |
|---|---|
| **1. It fails the paper's own test.** | `t_g = 1.032796` (rounded). BFRE, **p.8**: significance is `\|t\| > 2`. |
| **2. It earned almost nothing.** | Adding `g` cut the miss from `19/5 = 3.8` to `3`. The gain is `4/5 = 0.8`, which is exactly `t_g²·σ̂² = (16/15)(3/4)`. |
| **3. That gain is the going rate.** | A worthless column earns `σ̂² = 0.75` on average (8e). `g` earned `0.8` — a multiple of `16/15 = 1.066667` (rounded). It performed **6.7% better than a coin flip.** |
| **4. `R²` barely moves.** | `1028/1103 = 0.932004` with `g`, `1008/1103 = 0.913871` without (both rounded). **1.8132 percentage points** (rounded). |
| **5. Keeping it damages the factor that works.** | Without `g`: `df` rises 4 → 5, the overlap disappears, and `t_x` goes from `3.944053` to `√(1008/19) = 7.283724` (rounded). Nearly double. |
| **6. Its interval contains zero.** | `b_g ± 2·SE = 40 ± 77.459667` → `[−37.4597, +117.4597]` (rounded). The data cannot rule out that buybacks *hurt*. |
| **7. The wrong denominator would not save it.** | `df = 5` → `t_g = 1.1547`; `df = 6` → `t_g = 1.2649` (rounded). None of them reaches 2. |

## 14.6 THE CASE AGAINST DROPPING `g` — every claim a number

| Argument | The number |
|---|---|
| **1. "40" was never a claim about strength.** | `t` is scale-free, `b` is not (8d). Report `g` in percent instead of as a decimal and `b_g` becomes `0.4` with `SE = 0.387298` (rounded) — identical `t² = 16/15`. **The junior researcher's headline was a units artefact and so is the CRO's scorn.** |
| **2. In return terms `g` is not trivial.** | Fitted contributions: `g` gives `[−0.8, −0.4, +0.4, −0.4, +0.4, +0.8]`, a spread of `1.6` percentage points; `x` gives `[−3,−2,−1,+1,+2,+3]`, spread `6`. Ratio `15/4 = 3.75`. Not 40×, not 1/40×. **`g` is worth `4/15 = 0.266667` (rounded) of `x`.** |
| **3. Dropping it contaminates `x`.** | `b_x` moves from `1` to `6/5 = 1.2` — and the move is exactly `b_g·B/C = 40·(7/50)/28 = 1/5`. **One sixth of the "cheapness" premium reported without `g` is actually buyback wearing cheapness's coat.** |
| **4. "Insignificant" is not "zero".** | The same interval that contains 0 also contains `+117.4597` (rounded), which is `2.936492` (rounded) times `b_g`. The file is equally consistent with `g` being **nearly three times stronger** than estimated. Absence of evidence, in a file with `df = 4`, is not evidence of absence. |
| **5. There is no power here to speak of.** | `n = 6`, `k = 2`, `df = 4`. Section 8e: even a truly worthless column posts `E[t²] = 1.676788` (rounded) at this `df`. A single month of six stocks cannot settle anything. |
| **6. It is one month.** | BFRE does not judge a factor on one cross-section. **p.14**: a factor is eligible when the *proportion of significant t-statistics* exceeds **10%**; footnote 11 says those t-statistics are per-month cross-sectional. **p.32** repeats it. One `t = 1.03` is one dot in a fifteen-year series. |
| **7. Overlap, not irrelevance, may be the diagnosis.** | `cos = 0.763763`, `VIF = 2.4` (rounded). Level 4's lesson: when columns overlap, the *split* is unstable while the *fit* is fine. The paper's remedy for that (**p.11**) is to **aggregate** colliding substyles into one style — not to delete one. |
| **8. This is a risk model, not a return forecast.** | `g` moves the six predicted returns over a 1.6-point range. That dispersion enters `V = XFXᵀ + D` (Level 10) whether or not this month's mean effect is distinguishable from zero. Dropping a dispersion-generating column pushes its variance into `D` and reports it as diversifiable when it is not (Level 9). |

## 14.7 The trap the good players fall into — have this ready

A player defending `g` will eventually reach for Level 1 and fit `g` **on its own**:

```
b_g alone = p/A = 0.188/0.0012 = 470/3 = 156.666667 (rounded)
SSE       = Σr² − p²/A = 44.12 − 29.453333 = 44/3 = 14.666667 (rounded)      (p²/A = 2209/75, 2209 = 47²)
σ̂²        = (44/3)/5 = 44/15                        ← df = n − 1 = 5, one column
t_g²      = (p²/A)/σ̂² = 2209/220 = 10.040909 (rounded)
t_g       = 3.168739 (rounded)          ← CLEARS |t| > 2
R²        = 2209/3309 = 0.667573 (rounded)
```

**On its own, `g` is significant at `t = 3.17`. In the joint fit it is not, at `t = 1.03`.**

Both numbers are correct arithmetic. The player must say which one answers the question, and
why, using Level 4's vocabulary: the univariate `b_g = 156.67` is `40` **plus** whatever
cheapness it is standing in front of; the univariate `t` is measured against a denominator
that has not been told cheapness exists. A player who reports `t = 3.17` as evidence for
adding `g` **to a model that already contains `x`** has failed the level regardless of any
other answer.

The mirror check, which the player should run unprompted: dropping `x` instead raises the miss
from `3` to `44/3`, a rise of `35/3 = 11.666667` (rounded) — exactly `t_x²·σ̂² = (140/9)(3/4)`.
Dropping `g` cost `4/5 = 0.8`. Dropping `x` costs `(35/3)/(4/5) = 175/12 = 14.583333` (rounded)
times as much.

## 14.8 The scoreboard

| Model | `b_g` | `b_x` | `SSE` | `R²` *(rounded)* | `t_g` *(rounded)* | `t_x` *(rounded)* |
|---|---:|---:|---:|---:|---:|---:|
| both columns | **40** | **1** | **3** | 0.9320 | 1.033 | 3.944 |
| `x` only | — | 6/5 | 19/5 | 0.9139 | — | 7.284 |
| `g` only | 470/3 | — | 44/3 | 0.6676 | 3.169 | — |

## 14.9 The interrogation script (real objections, escalating)

1. *"Forty. That's the biggest number on the page. Why are you telling me it's nothing?"*
   → wants 14.6.1 (units) **and** 14.6.2 (return spread). Units alone is half an answer.
2. *"Fine, so multiply it out — 1.6 points of spread. That's real money. Keep it."*
   → wants 14.5.2 and 14.5.3: real spread, but indistinguishable from luck **in this file**.
3. *"Your junior ran it on its own and got a t of three. Explain that."*
   → 14.7. If the player cannot separate the univariate from the joint number, stop the level
   and go back to Level 4.
4. *"So drop it. Cheapness gets a t of seven without it. Clean model. Done."*
   → wants 14.6.3: the 1.2 is contaminated; `1/5` of it is buyback. A clean-looking model that
   attributes buyback's effect to cheapness is worse, not better.
5. *"You've told me both. Which is it?"*
   → The only acceptable answer names the decision the file cannot make: **six stocks and one
   month cannot decide this, and BFRE does not try to.** The decision is made on a history of
   t-statistics (p.14, p.32), and the correct action here is to log the month and keep
   collecting — while noting that if `g` is kept, its overlap with `x` (VIF 2.4) argues for
   aggregation rather than a separate factor.
6. *"Your standard errors assume every stock is equally noisy. Are they?"*
   → Section 9. Player should say it is an assumption, name what breaks it, and know that
   BFRE **p.25** addresses it with square-root-of-market-cap weights.

## 14.10 Pass conditions

Deny promotion unless **all** of these happen:

- [ ] `df = 4` is stated as `n − k`, and the player rejects `n − 1 = 5` **out loud**.
- [ ] `t² = (S²/Q)/σ²` produced with all four pieces named, unprompted.
- [ ] Both cases argued, each with at least three numbers from the file.
- [ ] The `t = 3.17` univariate trap is identified and correctly disarmed.
- [ ] The player says, in some form: *`t ≈ 1` is not weak evidence, it is the definition of no
      evidence* — and can justify it with `E[t²] = 1`.
- [ ] The player refuses to make the call from one month, and cites the paper's actual
      criterion rather than inventing one.

---

## 15. What this level does NOT settle, stated so the player is not misled

- **Where "2" comes from in `|t| > 2`.** This level derives a *distribution-free* bar of 25%
  (8f). The familiar "about 5% by chance" figure requires a normal distribution and a table,
  and **is not built here**. Flag it as an IOU, do not use it in any derivation.
- **Why `E[t²] → 1` as `df` grows.** Law of large numbers. Not built here. IOU.
- **Multiple testing.** BFRE screens 200-plus candidate substyles (p.10–p.11). Testing many
  columns and keeping the ones with big `t` is a different problem from testing one column.
  Level 12 territory; do not pretend this level covers it.
- **Autocorrelation in the factor-return *time series*.** This level is inside one month.
  Level 7 onwards.

---

## 16. Back to BFRE — what this machinery does in the real model

### 16a. p.8 — the paper's threshold, and the reason it also tracks `t²`

The BFRE paper, **p.8**, states its convention in one sentence:

> *"We consider an absolute t-statistics in excess of **2** as statistically significant."*
> *(the grammatical slip is in the original)*

That is `|t| > 2`, i.e. `t² > 4` — the exact quantity Section 8a builds and Section 8f bounds.

Same page, and this is the anchor for the whole of Section 8: BFRE also computes the
**average squared t-statistic**, explicitly

> *"to distinguish between factors with t-statistics close to +/- 2 and those that are
> significantly higher"*

`t²`, averaged. Section 8a is that number's origin: `t² =` earned miss ÷ going rate. Section
8e is why averaging it is the right move — because the average of `t²` for a factor that does
nothing is **1**, so the average squared t-statistic is directly readable as *"how many times
a worthless factor's performance did this factor deliver?"* The paper does not say that; it is
what its own statistic means.

Also p.8: an industry becomes a candidate factor on four criteria, of which the first two are
**(a)** a large proportion of significant t-statistics and **(b)** a high average squared
t-statistic. Both are this level's number.

### 16b. p.14 and p.32 — one t-statistic is never the decision

**p.14**, on style eligibility:

> *"A value in excess of **10%** [proportion of significant t-statistics] indicates a
> statistically significant style effect, and would be considered for inclusion in the models."*

with **footnote 11**: *"t-statistics are based on **monthly cross-sectional regressions**."*

**p.32**, in the model-estimation diagnostics:

> *"Individual factor efficacy is assessed using a history of t-statistics for each common
> factor by calculating the proportion of significant t-statistics over different periods.
> This metric serves as a good proxy for the persistence of individual factor effects. The
> majority of factors are significant more than 10% of time over the research history, with
> most well in excess of this threshold."*

**p.12** gives the recursive substyle search a stopping rule in the same currency: repeat
*"until the largest proportion of t-statistics from the second step univariate regression is
no larger than **10% – 15%**."*

This is the paper's own answer to the boss round. BFRE never keeps or kills a factor on one
month's `t`. It keeps a fifteen-year history of exactly the number Section 7 builds, and reads
the **proportion**. The boss round is unwinnable on the file precisely because BFRE would not
try to win it on the file.

### 16c. Turning this level's arithmetic on the paper's own figure

**p.15, Figure 1.8** ranks the NAMR style factors by proportion of significant t-statistics.
**The notes record that the figure carries no printed data labels** — the heights below were
*measured off the scanned axis* by the transcriber and are explicitly flagged as measurements,
not printed values. Everything downstream is therefore our arithmetic on a reading, and must
be presented to the player that way.

Measured heights: Volatility ≈ 63%, Momentum ≈ 50%, Size ≈ 42%, Reversal ≈ 37%, Value ≈ 34%,
Liquidity ≈ 32%, Dividend Yield ≈ 23%, MidCap ≈ 20%, Growth ≈ 18%, Profitability ≈ 14%,
Sentiment ≈ 7%, Earnings Yield ≈ 4–5%.

Apply Section 8f's bar — a worthless factor cannot exceed **25%**, with no distribution
assumed:

| Clears the distribution-free bar (> 25%) | Does not clear it (≤ 25%) |
|---|---|
| Volatility, Momentum, Size, Reversal, Value, Liquidity | Dividend Yield, MidCap, Growth, Profitability, Sentiment, Earnings Yield |
| **6 factors** | **6 factors** |

Two honest readings, and the player should hold both:

- Six of the twelve NAMR styles are established as non-worthless by an argument that assumes
  **nothing** about distributions. That is a strong result for very little machinery.
- The paper's own inclusion threshold is **10%** (p.14), which is **below** the 25% bar. So a
  factor admitted at 10–15% has not been shown by that criterion alone to beat chance in a
  distribution-free sense. This is not a refutation — a sharper bound follows once a
  distribution is assumed, and the paper is entitled to assume one — but it is a real question
  to put to the authors, and it is **Level 12 ammunition, earned here.**

Say plainly: the 25% figure is *ours*, derived in 8f; the 10% figure is *theirs*, quoted from
p.14. Do not let the player merge them.

### 16d. p.25 — BFRE says assumption 2 is false, and prices it in

Section 5e's second assumption is that every stock's miss is about the same size. **p.25**
states the opposite and acts on it:

> *"Assets are weighted in the regression using square-root of market capitalisation. This
> provides a good compromise between a weighting scheme that places equal weight on all
> assets, and one that is weighted by market capitalisation… More technically, square-root of
> market capitalisation **adjusts for heteroskedasticity** based on the observation that
> higher residual (specific) risk is typically correlated with smaller market capitalisation
> assets."*

and **footnote 14**:

> *"Other regression weighting schemes exist which explicitly use the reciprocal of each
> asset's residual (specific) variance, however, in practice these provide similar results to
> using square-root of market capitalisation weights."*

That footnote is Section 9 in the paper's own words: the "right" weight is one over each
asset's own wobble size — the own-size route — and sqrt-cap is a workable stand-in. So the
three-asset example in 9b, where the two routes differ by a factor of 3, is the small version
of the exact problem p.25 is solving. Every `b` in BFRE is a **weighted** least-squares
estimate, and every standard error behind every t-statistic on p.8, p.14 and p.32 inherits
that weighting.

### 16e. Where the machinery ends up in the finished model

Follow the chain the player has now built end to end:

1. Each month, `t` is computed for every factor in a cross-sectional regression (p.14 fn 11).
2. The proportion of months with `|t| > 2`, plus the average `t²`, decides which factors exist
   at all (p.8, p.14, p.32, p.12's stopping rule).
3. The surviving factors define the columns of `X`.
4. `X` and the estimated `f` produce the risk matrix. **p.24, equation (1.7):** `r = X f + u`
   — the `f` this level puts on trial is that `f`. **p.24, equation (1.8):** `Σ = X F Xᵀ + Δ`
   (Level 10).

So **Section 7's standard error is upstream of the entire covariance matrix.** A factor
admitted on a mis-computed `t` puts a spurious column into `X` forever; a real factor rejected
on a low-power `t` has its variance dumped into `D` and reported as diversifiable. The `n − k`
in Section 6 is not a technicality — it is the difference between a factor being in the model
and not.

### 16f. What the notes do NOT support — searched across all 65 transcribed pages

- **No formula for a standard error appears anywhere in the paper.** Not `σ²/Q`, not
  `σ²(XᵀX)⁻¹`, not in any form. The t-statistics are reported; their construction is not shown.
- **The words "degrees of freedom" do not appear.** `n`, `k` and `n − k` are never given for
  any regression in the paper.
- **No sample sizes are stated** for the cross-sectional regressions, so the `df` behind any
  reported t-statistic cannot be reconstructed from the paper.
- **The phrase "standard error" appears in no transcribed sentence of the paper.** The single
  hit anywhere in `notes/` is the transcriber's own commentary on p.65, noting that reference
  **[26] Newey–West** is *consistent with* HAC standard errors behind the factor-return
  t-statistics. That is an **inference by the transcriber, not a statement in the paper**, and
  must be flagged as such to the player. Where the paper does put Newey–West to work — p.27–p.28
  — it is for the **covariance and specific-risk** estimation (10-day lag daily, 2-week lag
  weekly), which is a different use entirely.
- **No p-value and no power calculation appear anywhere.**
- **One confidence interval does appear, and it is not this one.** p.38 flags bias-statistic
  exceptions using a **95% confidence interval**, and the tail-risk test uses a **99%** 1-day
  VaR confidence level. Those are forecast-accuracy tests (Level 12), not intervals on a factor
  return. **No interval is ever reported for any estimated `f`.**
- **No numeric VIF value or threshold** is given (p.32 says only that they "were found to be
  well within suitable thresholds").

So: **no BFRE anchor was found in `notes/` for the standard-error formula, for degrees of
freedom, for any sample size, or for a confidence interval on a factor return.** The paper reports the verdict on every page and never shows
the trial. Tell the player exactly that. It is the cleanest example in the game of a number
whose origin the reader is simply expected to take on trust — which is the habit this whole
level exists to break.

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level6.py     # 288 exact-rational assertions, exits 0
```

The script recomputes every figure on this page from the raw `x`, `g` and `r` vectors in
`fractions.Fraction`: the cold open's sums, residuals, weights and leverages; the `+100%` CHR
nudge; **all 32 sign-flip worlds twice over** (observed miss sizes, then equal miss sizes) with
the full distribution of `b̂`, the per-stock `E[e_i²] = (1 − h_i)σ²`, `E[SSE] = n − k` and
`E[t²] = 1`; the 4×4 Hadamard degrees-of-freedom ladder over all 16 worlds for `k = 1,2,3,4`
including the all-zero `SSE` at `n = k`; every wrong denominator and wrong shape with the exact
`t` each returns; the `√n` special case; the replicated 25-stock file; the three-asset
heteroskedasticity counterexample; and the entire boss round — Gram matrix, Cramer solution,
both balance conditions, both standard errors, both `t²`, the leverages summing to `k`, all
three sub-models, the exact omitted-variable bias `b_g·B/C`, the scale-invariance of `t`, and
the Markov bar applied to the twelve measured Figure 1.8 heights.

If any printed value ever disagrees with this markdown, the markdown is wrong.
