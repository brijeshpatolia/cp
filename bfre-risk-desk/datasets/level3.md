# Level 3 — The Second Dial

Every number below is recomputed in exact rational arithmetic by `tools/verify_level3.py`
(340 exact checks, standard library only, exits 0). Nothing here is rounded by hand. Where a
decimal is not exact it is printed with the fraction beside it and labelled **rounded**.

Entering this level the player already holds, from Levels 0–2:

```
x = [−1.5, −0.5, 0, +1, +2]        r = [−2.0%, −2.0%, +0.5%, +4.0%, +3.5%]
Σx = 1     Σx² = 15/2     Σx·r = 15     Σr = 4     Σr² = 73/2

b = Σxr/Σx² = 15/(15/2) = 2 exactly                       (Level 1: derived by nudging)
e at b = 2:  +1, −1, +0.5, +2, −0.5     Σe = 2     Σx·e = 0     Σe² = 13/2

THE NUDGE IDENTITY (Level 1/2):  SS(b + d) = SS(b) − 2d·(Σx·e) + d²·(Σx²)
THE BALANCE      (Level 2):      b is the best setting  ⟺  Σx·e = 0
```

Level 2 proved that one column forces one balance condition. This level asks the only question
left: **what happens when there are two columns?**

The answer is not "do it twice."

---

## 1. The story (no mathematics)

> There is an old shower with two taps — hot on the left, cold on the right — and one spout.
>
> You want two things at once. You want the water at the right *temperature*, and you want it
> coming out at the right *flow*. Two things you care about, two taps to set. That sounds like two
> jobs.
>
> It is not two jobs. Open the hot tap and you have changed the temperature *and* the flow. Close
> the cold tap to bring the flow back down and you have changed the temperature *again*. Every
> tap moves every thing you care about. So you do what everyone does: you tweak the hot, then the
> cold, then the hot, then the cold, standing there shivering, spiralling in on the setting you
> wanted, never quite arriving in one go.
>
> Now imagine a different, better-engineered shower. One dial for temperature, a completely
> separate dial for flow. Set the temperature — the flow does not move. Set the flow — the
> temperature does not move. One turn each and you are done, forever.
>
> Same two goals. Same two controls. Completely different problem. The difference is not in what
> you want; it is in whether the controls **interfere**.

That story is the whole level. Finish it before any algebra.

---

## 2. Mapping the story, line by line

| In the shower | On the desk |
|---|---|
| the hot tap | the cheapness dial `b₁` |
| the cold tap | the size dial `b₂` |
| "temperature is right" | the cheapness plank is level: `Σ x·e = 0` |
| "flow is right" | the size plank is level: `Σ s·e = 0` |
| both right **at the same time** | both conditions hold simultaneously — the fit |
| the taps interfere | `Σ x·s ≠ 0` |
| the well-engineered shower | `Σ x·s = 0` — and one pass each is exact |
| shivering, tweak-tweak-tweak | fitting one column at a time and iterating |
| two taps that are secretly both hot | Level 4's collision — you can never get it right |

Level 2 gave the player one plank on one stone. This level hangs the **same weights** on **two
different planks with two different stones**, and demands that both sit level at once. Every weight
is on both planks. That is what makes it a system.

---

## 3. The dataset — the month the size file arrived

Same five stocks, the same month the player has already fitted. Nothing about the returns has
changed. The desk has simply been sent a second characteristic: a **size score** `s`, positive for
big companies, negative for small ones.

| Stock | cheapness `x` | size `s` | return `r` |
|---|---:|---:|---:|
| AXL | −1.5 | +1 | −2.0% |
| BRN | −0.5 | −1 | −2.0% |
| CHR | 0.0 | +2 | +0.5% |
| DLT | +1.0 | 0 | +4.0% |
| EMK | +2.0 | −2 | +3.5% |

The rule under test is now

```
predicted return  =  b₁ · x  +  b₂ · s
```

Six sums run the entire level. All six are computable by a 12th-standard student in under a minute:

```
Σx  = 1        Σs  = 0        Σr  = 4        Σr² = 73/2 = 36.5

Σx² = 15/2 = 7.5        Σs² = 10        Σx·s = −5
Σx·r = 15               Σs·r = −6
```

Two of those are new and one of them is the important one.

> **`Σ x·s = −5`. Not zero. The two taps interfere.**

Read the sign: big companies in this month tend to have low cheapness scores (AXL is small and
cheap-ish; EMK is the cheapest and the smallest). The two columns are pulling on each other before
any fitting has happened at all.

### First evidence that this is not two separate problems

Take the answer the player already owns — `b = 2` from cheapness alone — and check the size plank
against those residuals `e = [+1, −1, +0.5, +2, −0.5]`:

```
Σ x·e = 0        ✓ the cheapness plank is level, exactly as Level 2 promised
Σ s·e = (1)(1) + (−1)(−1) + (2)(0.5) + (0)(2) + (−2)(−0.5)
      = 1 + 1 + 1 + 0 + 1 = 4        ✗ the size plank is tipping, hard
```

The Level 1 answer is not wrong *at what it was asked*. It is incomplete. There is a second plank
in the room and nobody has looked at it.

---

## 4. The nudge argument, with two dials

Nothing new is needed. The Level 1/2 argument is repeated with two step sizes instead of one.

Sit at any pair `(b₁, b₂)`, with misses `e_i = r_i − b₁x_i − b₂s_i`. Nudge **both** dials: `b₁ → b₁ + p`
and `b₂ → b₂ + q`. Each miss changes:

```
e_i(b₁+p, b₂+q) = r_i − (b₁+p)x_i − (b₂+q)s_i = e_i − p·x_i − q·s_i
```

Square it. This is just `(A − B)² = A² − 2AB + B²` with `A = e_i` and `B = p·x_i + q·s_i`:

```
(e_i − p x_i − q s_i)²  =  e_i²  −  2 e_i (p x_i + q s_i)  +  (p x_i + q s_i)²
```

Add over all five stocks and pull `p` and `q` out of the sums (they are the same for every stock):

```
SS(b₁+p, b₂+q) = SS(b₁,b₂) − 2p·(Σx·e) − 2q·(Σs·e) + p²Σx² + 2pq·Σxs + q²Σs²
```

Write `B₁ = Σx·e` and `B₂ = Σs·e` — the two turning forces — and the identity is:

```
SS(b₁+p, b₂+q) = SS(b₁,b₂) − 2p·B₁ − 2q·B₂ + [ p²Σx² + 2pq·Σxs + q²Σs² ]     ← TWO-DIAL NUDGE
                 └─── the reward ───┘   └────────── the tax ──────────┘
```

**This is exact**, not an approximation, on any data. `verify_level3.py` checks it on **1,764**
`(b₁, b₂, p, q)` combinations of this dataset and does not miss by a rational hair.

Compare it with Level 1's version and notice that only one thing changed: the tax used to be
`d²·Σx²`, a single square. Now it has a cross-term `2pq·Σxs`. **That cross-term is the interference.
It is the entire content of this level.**

### 4a. Both conditions, and why both

Suppose `(b₁, b₂)` is the best pair. Take `q = 0` — nudge the cheapness dial only. The identity
collapses to Level 1's exactly:

```
SS(b₁+p, b₂) − SS(b₁,b₂) = −2p·B₁ + p²·Σx²
```

If `B₁ ≠ 0`, choose `p = B₁/Σx²` and the change is `−B₁²/Σx² < 0` — strictly better, so the pair was
not the best. Contradiction. Therefore `B₁ = 0`.

Now take `p = 0` and run the identical argument on the other dial:

```
SS(b₁, b₂+q) − SS(b₁,b₂) = −2q·B₂ + q²·Σs²        →  if B₂ ≠ 0, choose q = B₂/Σs², done
```

Therefore `B₂ = 0`.

```
Σ x·e = 0        AND        Σ s·e = 0
```

**Both. Simultaneously. On the same residual vector `e`.** Not one, then the other on a fresh set of
leftovers — the *same* five numbers `e` have to satisfy both sums at once.

Worked on this data, from the cheapness-only answer `(b₁, b₂) = (2, 0)`:

```
B₁ = 0,  B₂ = 4       best single q = B₂/Σs² = 4/10 = 2/5
gain  = B₂²/Σs² = 16/10 = 8/5 = 1.6
SS(2, 0)   = 13/2 = 6.5          ← the Level 1 answer's score
SS(2, 2/5) = 49/10 = 4.9         ← 6.5 − 1.6, exactly as the identity predicts
```

That single size step is worth **1.6** on the scorecard. Free money the one-column model was
leaving on the table.

---

## 5. The two balance conditions ARE two equations in two unknowns

Now open up `e = r − b₁x − b₂s` inside each condition. Nothing here is clever; it is one line of
distributing a sum.

```
B₁ = Σ x·(r − b₁x − b₂s) = Σxr − b₁·Σx² − b₂·Σxs = 0
B₂ = Σ s·(r − b₁x − b₂s) = Σsr − b₁·Σxs − b₂·Σs² = 0
```

Move the knowns to the right:

```
(1)     Σx²·b₁  +  Σxs·b₂  =  Σxr
(2)     Σxs·b₁  +  Σs²·b₂  =  Σsr
```

**That is the level.** Two balance conditions, written out, *are* two simultaneous linear equations
in `b₁` and `b₂`. The player has been solving pairs like this since Class 9. On this data:

```
(1)     (15/2) b₁  −  5 b₂  =  15
(2)        −5  b₁ + 10 b₂  =  −6
```

Notice where the interference sits: `Σxs = −5` is the **off-diagonal** number, and it appears in
*both* equations. If it were zero, equation (1) would contain only `b₁` and equation (2) only `b₂` —
two separate one-line problems, the well-engineered shower. It is not zero, so it is one problem.

### 5a. Why neither condition alone tells you anything

This is the sentence that separates "a system" from "two problems", and it is worth making the
player say it out loud.

Condition (1) on its own is satisfied by **infinitely many** pairs — it is a straight line:

```
L₁ :  (15/2)b₁ − 5b₂ = 15     ⟺     b₁ = 2 + (2/3)·b₂
      passes through  (2, 0),  (8/3, 1),  (12/5, 3/5),  (4, 3),  ...
```

Condition (2) on its own is also a line:

```
L₂ :  −5b₁ + 10b₂ = −6        ⟺     b₂ = −3/5 + (1/2)·b₁
      passes through  (0, −3/5),  (2, 2/5),  (12/5, 3/5),  (4, 7/5),  ...
```

Neither line is an answer. Each is a *whole family* of answers. **The fit is the single point where
the two lines cross**, and that point appears in both lists above: `(12/5, 3/5)`.

Say it in the shower's words: "the temperature is right" describes a whole family of tap settings,
and so does "the flow is right". Only the pair of statements together names one setting.

---

## 6. Solving it, by hand, in fractions

Elimination. No matrices, no formulas to remember.

```
(1)     (15/2) b₁  −  5 b₂  =  15
(2)        −5  b₁ + 10 b₂  =  −6

multiply (1) by 2:      15 b₁ − 10 b₂ =  30
add (2):                15 b₁ − 10 b₂ − 5 b₁ + 10 b₂ = 30 − 6
                        10 b₁          = 24
                                    b₁ = 24/10 = 12/5 = 2.4          exactly

back-substitute into (2):   −5(12/5) + 10 b₂ = −6
                                  −12 + 10 b₂ = −6
                                        10 b₂ = 6
                                           b₂ = 6/10 = 3/5 = 0.6     exactly
```

### The cross-multiplication check (a second, independent route)

Solve the general pair `Σx²·b₁ + Σxs·b₂ = Σxr`, `Σxs·b₁ + Σs²·b₂ = Σsr` once, symbolically. The `D`
that falls out is worth holding on to: it runs Section 8 (is the answer unique?), Section 10 (how
slow is the chase?), the whole of Level 4, and it reappears in Level 6 under a different name.

```
D  = Σx²·Σs² − (Σxs)²                          ← call it D for now; it is named in Section 13

b₁ = ( Σxr·Σs² − Σsr·Σxs ) / D
b₂ = ( Σx²·Σsr − Σxs·Σxr ) / D
```

On this data:

```
D  = (15/2)(10) − (−5)²  = 75 − 25 = 50
b₁ = ( 15·10 − (−6)(−5) ) / 50 = (150 − 30)/50 = 120/50 = 12/5     ✓ agrees
b₂ = ( (15/2)(−6) − (−5)(15) ) / 50 = (−45 + 75)/50 = 30/50 = 3/5  ✓ agrees
```

Two routes, one answer. That is the check to run before submitting anything.

---

## 7. The fit, and both planks level

```
fitted = b₁x + b₂s :   −3,  −9/5,  6/5,  12/5,  18/5
e = r − fitted     :   +1,  −1/5, −7/10, +8/5, −1/10
```

| Stock | `x` | `s` | `r` | fitted | `e` | `x·e` | `s·e` |
|---|---:|---:|---:|---:|---:|---:|---:|
| AXL | −1.5 | +1 | −2 | −3 | **+1** | −3/2 | +1 |
| BRN | −0.5 | −1 | −2 | −9/5 | **−1/5** | +1/10 | +1/5 |
| CHR | 0 | +2 | +1/2 | +6/5 | **−7/10** | 0 | −7/5 |
| DLT | +1 | 0 | +4 | +12/5 | **+8/5** | +8/5 | 0 |
| EMK | +2 | −2 | +7/2 | +18/5 | **−1/10** | −1/5 | +1/5 |
| | | | | | | **Σ = 0** | **Σ = 0** |

```
CHECK 1   Σ x·e = −3/2 + 1/10 + 0 + 8/5 − 1/5 = 0        ✓
CHECK 2   Σ s·e = 1 + 1/5 − 7/5 + 0 + 1/5    = 0        ✓
          Σ e   = 8/5 = 1.6      ← still NOT zero, and still nothing forces it to be
          Σ e²  = 41/10 = 4.1
```

Two independent things to point out here:

1. **`Σe = 8/5 ≠ 0`, still.** Adding a second column did not fix that, and it never will until a
   column of 1s arrives. That is Level 5, and it is still visible in plain sight, exactly as it was
   at Level 0.
2. **`Σe²` can be got two ways, and they must agree.** Directly from the residuals: `41/10`. Or from
   the six sums with no residuals at all:
   `Σe² = Σr² − b₁·Σxr − b₂·Σsr = 73/2 − (12/5)(15) − (3/5)(−6) = 36.5 − 36 + 3.6 = 4.1` ✓
   Make the player do both. Disagreement means an arithmetic slip, and it is the cheapest audit
   available.

### The headline: the first dial moved

```
Level 1's answer, cheapness alone :  b = 2
Level 3's answer, both columns    :  b₁ = 12/5 = 2.4
```

**Nothing about the cheapness column changed. Nothing about the returns changed.** A second column
walked into the room and the cheapness factor return moved by `2/5`, which is **20%** of its old
value (`(12/5 − 2)/2 = 1/5`).

This should be shocking, and if the player is not disturbed by it, they have not understood it.
Ask them, before revealing anything: *"if I hand you a number called 'the value factor return',
what do you need to know before it means anything?"* The answer is **the full list of what else was
in the regression** — and that answer is what Level 4 exists to explain properly.

---

## 8. Is it the only answer? (Uniqueness, and the number `D`)

Level 1 got uniqueness free from `Σx² > 0`. Here it costs one line of completing the square, and
that line is where `D` comes from.

The tax term in the nudge identity is

```
Q(p, q) = p²Σx² + 2pq·Σxs + q²Σs²
```

First, the thing nobody points out: **`Q` is itself a sum of squares.**

```
Q(p, q) = Σ (p·x_i + q·s_i)²
```

(expand it and you get the three terms back — checked exactly on 49 `(p, q)` pairs). So `Q ≥ 0`
always. But "≥ 0" is not enough; we need "> 0 unless `p = q = 0`". Complete the square:

```
Q(p,q) = Σx²·( p + (Σxs/Σx²)·q )²  +  ( D / Σx² )·q²          where D = Σx²Σs² − (Σxs)²
```

On this data `Σxs/Σx² = −5/(15/2) = −2/3` and `D/Σx² = 50/(15/2) = 20/3`, so

```
Q(p,q) = (15/2)·( p − (2/3)q )²  +  (20/3)·q²
```

(also checked exactly on 49 `(p, q)` pairs). Read it:

- `D = 50 > 0`, so the second term is zero **only** when `q = 0`;
- with `q = 0` the first term is `(15/2)p²`, zero **only** when `p = 0`.

So `Q(p,q) > 0` for every non-zero nudge. And because the two balance conditions hold at
`(12/5, 3/5)`, the reward terms vanish and the nudge identity becomes a **penalty formula**, the
two-dial version of the one the player banked at Level 1:

```
SS(b₁* + δ₁,  b₂* + δ₂)  −  SS*  =  Q(δ₁, δ₂)  >  0  for any non-zero (δ₁, δ₂)
```

**Every other pair scores strictly worse. The answer is unique.** Verified exactly on 49
`(δ₁, δ₂)` pairs.

*Hold on to `D`.* When `D` is large **next to `Σx²Σs²`** the bowl is steep in every direction and
the answer is firmly pinned. When `D` is small next to `Σx²Σs²` the bowl has a long shallow trough
and the answer wobbles. (Always next to `Σx²Σs²` — `D` on its own has no scale, and Section 8a
shows why.) When `D = 0` the second term vanishes entirely, `Q` is zero along a whole line of
nudges, and **there is no single answer at all.**

### 8a. One inch through Level 4's door — watch `D` collapse

Keep the cheapness column exactly as it is. Slide the size column, a fraction `t` at a time, towards
a multiple of the cheapness column — `s(t) = (1−t)·s + t·(3/2)·x` — until at `t = 1` the two columns
are literally the same column scaled. Recompute the three sums at each stop:

| `t` | `Σx·s(t)` | `D` | `D` rounded | `(Σxs)²/(Σx²Σs²)` rounded |
|---:|---:|---:|---:|---:|
| 0 (this level's data) | −5 | 50 | 50.0000 | 0.333333 |
| 1/4 | −15/16 | 225/8 | 28.1250 | 0.030303 |
| **4/13** | **0** | 4050/169 | 23.9645 | **0.000000** |
| 1/2 | 25/8 | 25/2 | 12.5000 | 0.438596 |
| 3/4 | 115/16 | 25/8 | 3.1250 | 0.942959 |
| 9/10 | 77/8 | 1/2 | 0.5000 | 0.994632 |
| 99/100 | 887/80 | 1/200 | 0.0050 | 0.999959 |
| **1** | 45/4 | **0** | 0.0000 | **1.000000** |

The last column has no name yet. It is just the ratio `(Σxs)²/(Σx²Σs²)` — the interference term,
squared, measured against the two diagonal sums. Compute it and nothing more; Section 10b derives
what it does and Section 13 names it.

Two things to read off it, and only two:

- **`D → 0` as the second column slides onto the first.** At `D = 0`, `Q` costs nothing along a
  whole direction and the system stops having one answer: `L₁` and `L₂` are no longer two lines
  crossing at a point, they are the **same line**, every point on which fits equally well. (Not two
  parallel lines that miss each other — these two equations can never contradict each other, only
  collapse into one. That is why the paper's phrase at Level 4 will be *"an infinite number of
  possible solutions"* and not *"no solution"*.) That is Level 4.
- **At `t = 4/13` the interference vanishes by accident** — `Σx·s(t) = 0`, the last column reads 0,
  and one pass of the chase would be exact. That a *different* version of the size column can be
  free of interference is the seed of Level 4's real machinery.

**A warning about `D` that this table makes unavoidable.** Read the `D` column downwards: it falls
from 50 to 23.96 between `t = 0` and `t = 4/13`, yet `t = 4/13` is the *easier* problem — its
interference is exactly zero. Both things are true because `D` is not a scale-free number. Double
the size column and every `Σs²` quadruples, `Σxs` doubles, and `D` comes out **four times bigger**
with nothing about the problem changed; the last column does not move at all. So `D = Σx²Σs²` at
`t = 4/13` means only "`D` has hit its ceiling *for these two columns*" — and that ceiling has
itself fallen, because `s(4/13)` is a shorter column than `s(0)`. **`D = 0` is the fact worth
carrying; the size of a non-zero `D` is only meaningful next to `Σx²Σs²`,** which is exactly the
comparison the last column is making.

**Do not walk through that door yet.** Both facts are Level 4's material; this level's job was to
show that the system exists, not to take it apart.

---

## 9. The traps — every wrong method, and what each returns

Scored with `SS = Σ(r − b₁x − b₂s)²`. The joint answer scores `41/10 = 4.1`.

| Method a player actually reaches for | `b₁` | `b₂` | `SS` | `SS` ÷ best |
|---|---:|---:|---:|---:|
| **solve both conditions at once** | **12/5 = 2.4** | **3/5 = 0.6** | **41/10 = 4.1** | **1.0000** |
| one pass of the chase: fit cheapness, then fit size to what's left | 2 | 2/5 = 0.4 | 49/10 = 4.9 | 49/41 = 1.1951 |
| cheapness alone, size dropped (the Level 1 answer) | 2 | 0 | 13/2 = 6.5 | 65/41 = 1.5854 |
| **two separate one-column fits, both reported** | 2 | **−3/5 = −0.6** | 149/10 = 14.9 | 149/41 = 3.6341 |
| size alone, cheapness dropped | 0 | −3/5 = −0.6 | 329/10 = 32.9 | 329/41 = 8.0244 |
| give up: predict zero for everyone | 0 | 0 | 73/2 = 36.5 | 365/41 = 8.9024 |

(ratios rounded; the fractions beside them are exact)

Three things in that table need saying out loud.

**(a) The "obviously sensible" method is the worst one that uses both columns.** Fit each column on
its own, report both numbers, go home. It scores `14.9` — **more than three times** the joint
answer, and **worse than throwing the size column in the bin** (`6.5`). Adding information made the
model worse, because the information was added wrong.

**(b) The size number came out with the wrong sign.** Fitted alone, `b₂ = Σsr/Σs² = −6/10 = −3/5`.
Fitted jointly, `b₂ = +3/5`. On this dataset they are **exact negatives of each other**. A desk that
ran the columns separately would report "big companies underperformed by 0.6% per unit of size"
when the truth in this month is "big companies **out**performed by 0.6% per unit of size".

> **Do not let the player over-learn this.** The sign flip is not a law. On the boss-round data
> below the sign also flips, but the magnitudes are *different* (`+5/7` alone versus `−11/17`
> jointly — a gap of `8/119 ≈ 0.0672`, rounded). The correct lesson is weaker and more useful:
> **the one-column number and the joint number are different numbers with no reliable relationship
> at all.** Anything stronger than that is Level 4's material, and Level 4 is where it gets
> explained rather than observed.

**(c) The one-pass chase is the *seductive* wrong answer** — it scores `4.9` against `4.1`, i.e.
`49/41 = 1.1951×`, under 20% worse, and it *looks* like it did the right thing. Section 10 is entirely about why it did not.

And the penalty formula prices the miss without re-fitting anything. The one-pass answer sits at
`δ₁ = 2 − 12/5 = −2/5`, `δ₂ = 2/5 − 3/5 = −1/5`:

```
Q(−2/5, −1/5) = (15/2)(4/25) + 2(−5)(−2/5)(−1/5) + 10(1/25)
              = 6/5 − 4/5 + 2/5 = 4/5 = 0.8

and indeed   SS(2, 2/5) − SS* = 4.9 − 4.1 = 0.8      ✓
```

---

## 10. The chase — one condition at a time, pass after pass

This is the section the level exists for. Do it slowly.

**The procedure a beginner invents unprompted.** Pretend the size column is not there. Fit cheapness.
Now fit size to whatever is left over. Now go back and re-fit cheapness given the size number you
just got. Repeat. Each individual step is a Level 1 problem with a one-line answer:

```
b₁ ← (Σxr − b₂·Σxs) / Σx²          (level the cheapness plank, holding b₂ fixed)
b₂ ← (Σsr − b₁·Σxs) / Σs²          (level the size plank, holding b₁ fixed)
```

Start with `b₂ = 0` — "there is no size column" — and turn the handle.

| state `(b₁, b₂)` | `Σ x·e` | `Σ s·e` | `SS` | `SS` rounded |
|---|---:|---:|---:|---:|
| (2, 0) | **0** | 4 | 13/2 | 6.5000 |
| (2, 2/5) | 2 | **0** | 49/10 | 4.9000 |
| (34/15, 2/5) | **0** | 4/3 | 131/30 | 4.3667 |
| (34/15, 8/15) | 2/3 | **0** | 377/90 | 4.1889 |
| (106/45, 8/15) | **0** | 4/9 | 223/54 | 4.1296 |
| (106/45, 26/45) | 2/9 | **0** | 3329/810 | 4.1099 |
| (322/135, 26/45) | **0** | 4/27 | 9971/2430 | 4.1033 |
| (322/135, 16/27) | 2/27 | **0** | 29897/7290 | 4.1011 |
| **(12/5, 3/5)** | **0** | **0** | **41/10** | **4.1000** |

**Look at the two balance columns.** In every single row, exactly one of them is zero. Never both,
until the last row. Levelling the cheapness plank knocks the size plank off level; levelling the
size plank knocks the cheapness plank off level. The imbalance is not being destroyed — it is being
**handed back and forth**, getting smaller each time:

```
Σ s·e right after every cheapness step :   4,   4/3,  4/9,  4/27,  ...
Σ x·e right after every size step      :   2,   2/3,  2/9,  2/27,  ...
```

Each is exactly one third of the one before. That one third is not a coincidence; the next section
derives it.

### 10a. Exactly how far short one pass falls

```
after one pass:   b₁ = 2,      b₂ = 2/5 = 0.4
the truth     :   b₁ = 12/5,   b₂ = 3/5 = 0.6

b₁ is short by (2 − 12/5)/(12/5) = −1/6      → 16.67% too small   (rounded)
b₂ is short by (2/5 − 3/5)/(3/5) = −1/3      → 33.33% too small   (rounded)
```

**One pass is not "nearly right". It is one third short on the new dial.**

### 10b. The contraction factor, and where it comes from

Track the error in `b₂` after each full pass:

| pass | `b₂` | error vs 3/5 | ratio to previous error |
|---:|---:|---:|---:|
| 1 | 2/5 = 0.4000 | −1/5 = −0.2000 | — |
| 2 | 8/15 = 0.5333 | −1/15 = −0.0667 | **1/3** |
| 3 | 26/45 = 0.5778 | −1/45 = −0.0222 | **1/3** |
| 4 | 16/27 = 0.5926 | −1/135 = −0.0074 | **1/3** |

(decimals rounded; the fractions are exact)

Every pass kills exactly two thirds of the remaining error and keeps one third. Where does `1/3`
come from? Subtract the fixed-point equations from the update equations and the algebra is three
lines of 12th-standard substitution:

```
b₁ error after a cheapness step :   δ₁ ← −(Σxs/Σx²)·δ₂
b₂ error after a size step      :   δ₂ ← −(Σxs/Σs²)·δ₁  =  (Σxs)²/(Σx²·Σs²) · δ₂
```

So the shrink factor per full pass is

```
k  =  (Σxs)² / (Σx²·Σs²)  =  25 / ( (15/2)·10 )  =  25/75  =  1/3        exactly
```

and, because `D = Σx²Σs² − (Σxs)²`, that same number is

```
k = 1 − D/(Σx²·Σs²)         here:  1 − 50/75 = 1/3      ✓
```

**One number controls everything in this level.** `k = 0` means the columns do not interfere, `D`
has hit its ceiling `Σx²Σs²`, and one pass is exact. `k` near 1 means `D` is near zero *next to that
ceiling*, the chase crawls, and the answer is barely pinned down at all. Note that `k` is the
scale-free one of the pair: rescale either column and `D` moves, `k` does not. On this data
`k = 1/3`, so five full passes bring `b₂` within 1% of the truth (`(1/3)⁵ = 1/243 ≈ 0.0041`).

`√k = √(1/3) = 0.5774` (rounded) is the **size** of the correlation between the two columns — **but
that name is not unlocked until Section 13.** Note "size": a square root is never negative, so `√k`
throws the sign away. The correlation here is `−0.5774`, negative, because `Σxs = −5` is negative;
`k` alone cannot tell you that. Flip the sign of every entry in the size column and `Σxs` becomes
`+5`, `b₂` becomes `−3/5`, and the chase's error sequence becomes `+1/5, +1/15, +1/45, …` — the same
magnitudes at the same `1/3` per pass. **The rate of the chase depends on `(Σxs)²`, so it cannot
see which way the columns lean, only how hard.** For now it is just `k`, "the overlap".

### 10c. Why it never lands, in one sentence

The chase moves **sideways** to reach line `L₁` (adjusting `b₁` with `b₂` held) and then **vertically**
to reach line `L₂` (adjusting `b₂` with `b₁` held). Sideways-then-vertical lands on the crossing point
in one go **if and only if `L₁` is a vertical line** — because only then does the vertical move fail
to knock you back off `L₁`.

`L₁` is `Σx²·b₁ + Σxs·b₂ = Σxr`. It is vertical (i.e. `b₁` does not depend on `b₂`) exactly when
`Σxs = 0`. Here `Σxs = −5`, so it is not, so you cannot. That is the whole proof.

---

## 11. When one pass IS exact — and the player has already seen it

Go back to Level 2's boss round, which the player passed: five stocks, a market column `m` of all
ones, a cheapness column `x = [−2, −1, 0, +1, +2]`, and returns `r = [−2.5, −4.5, +2.5, +3.5, +3.5]`.

```
Σ m·x = Σx = 0        ← the interference term is exactly zero
```

So the system decouples completely:

```
(1)  Σm²·a + Σmx·b = Σmr   →   5a + 0·b = 2.5    →   a = 1/2
(2)  Σmx·a + Σx²·b = Σxr   →   0·a + 10b = 20    →   b = 2
```

Each equation contains one unknown. One pass of the chase reaches `(1/2, 2)` **exactly** — verified —
because `k = 0²/(5·10) = 0`. The residuals are `[+1, −3, +2, +1, −1]` and `Σe² = 16`, exactly as the
player computed at Level 2.

**Tell the player plainly that this was rigged.** Level 2's design note said so: `Σx = 0` was chosen
on purpose so the two dials would not interfere, because making them interfere was this level's
job. `a = r̄` and `b = Σxr/Σx²` were not general laws; they were the well-engineered shower.

The perpendicularity test, one line:

```
L₁ has normal (Σx², Σxs);  L₂ has normal (Σxs, Σs²)
they are perpendicular  ⟺  Σx²·Σxs + Σxs·Σs² = Σxs·(Σx² + Σs²) = 0  ⟺  Σxs = 0
                            (because Σx² + Σs² is a sum of squares and cannot be zero)

Level 2 boss data     :  Σxs·(Σx²+Σs²) = 0            → perpendicular → one pass exact
Level 3 derivation    :  Σxs·(Σx²+Σs²) = −175/2 ≠ 0   → not perpendicular → staircase
```

---

## 12. Difficulty, honestly

**Nothing in Sections 3–11 is above 12th standard.** Expand a square; collect terms; solve two
simultaneous linear equations; complete a square. If it felt hard, the framing was bad, not the
player.

Four things they are owed:

1. **The identity is still exact.** `SS` is a polynomial of degree exactly 2 in `(b₁, b₂)`, so
   splitting it into a `p,q` piece and a `p²,pq,q²` piece is complete — no remainder, nothing hidden.
   This remains why no calculus is needed.
2. **Two columns generalises to fifty with no new idea and enormous new bookkeeping.** With `n`
   columns you get `n` balance conditions and `n` simultaneous equations. The *idea* is finished
   here. Solving a 50×50 system by hand is not a new concept, it is a different profession — which
   is what the phrase "the model is estimated numerically" is quietly covering for.
3. **The chase has a name and a literature, and both are graduate-level.** Sweeping one coordinate
   at a time until it settles is **Gauss–Seidel** in numerical linear algebra and **backfitting** in
   statistics; the fact that the error contracts by exactly `k` per pass is a first-year-graduate
   convergence result. **The player has just verified it by hand in fractions, which is a genuinely
   better way to meet it than being handed the theorem.** Say that.
4. **The thing this level *cannot* explain is Level 4, and it is genuinely hard.** *Why* does the
   joint `b₂` differ from the alone `b₂`? The honest answer — "a coefficient measures what its
   column explains that the other columns have not already explained" — needs a construction
   (regress one column on the other, keep the leftovers) that has a name, **Frisch–Waugh–Lovell**,
   and it is standard graduate econometrics. Warn the player now so they calibrate: Level 4 is the
   first genuinely postgraduate level in this game.

---

## 13. Names unlocked (only now, after the mechanism is built)

| The thing the player just built | The name it goes by |
|---|---|
| the table of exposure columns side by side | the **design matrix** `X` |
| the square of numbers `Σx², Σxs, Σxs, Σs²` | the **cross-product matrix** `XᵀX` |
| `Σx² b₁ + Σxs b₂ = Σxr` and its partner | the **normal equations** — plural now, one per column |
| `D = Σx²Σs² − (Σxs)²` | the **determinant** of `XᵀX` |
| the cross-multiplication formula in Section 6 | **Cramer's rule** (equivalently, inverting `XᵀX`) |
| fitting several columns in one solve | **multivariate** (or multiple) **regression** |
| `Σxs = 0` | the two columns are **orthogonal** — Level 2's word, now between two columns |
| `k = (Σxs)²/(Σx²Σs²)` | the **squared correlation** between the columns; `√k` is the *size* of that correlation, and `Σxs` supplies the sign it dropped (here `ρ = −√k = −0.5774`) |
| the one-at-a-time chase | **Gauss–Seidel** / **backfitting** (graduate vocabulary — flag it as such) |

A sentence the player should now be able to produce unprompted, in a quant's register:

> *"The factor returns come out of a single multivariate cross-sectional regression, so each
> coefficient is conditional on every other column in the design matrix — you can't read a value
> factor return without knowing what else was in the model that day."*

**Still locked, do not use yet:** *multicollinearity*, *variance inflation factor*,
*Frisch–Waugh–Lovell*, *partialling out*, *standard error*, *degrees of freedom*, *R²*. The first
four are Level 4; *standard error* and *degrees of freedom* are Level 6.

Three of those locked terms are nevertheless **heard** on this page, and the game master should know
where, so the player is not accidentally handed vocabulary they have not earned:

- *Frisch–Waugh–Lovell*, once, in Section 12, purely as a difficulty warning.
- *multicollinearity* and *variance inflation factors*, in Section 16, **only inside the quoted
  p.32 paragraph and its footnote** — the paper's words, reproduced because the tie-back needs
  them. The surrounding prose deliberately explains that footnote using `D = 0`, which the player
  built, and never uses either term to do explanatory work.

The rule in both cases is Level 2's: let the player *hear* a name they will meet, never *lean* on
it. Naming a theorem or a diagnostic the player will meet is honest; using it to explain anything
before Level 4 builds it is not. If the player picks up "multicollinearity" from the quote and
starts deploying it, that is the Victory-Condition-2 mimicry failure — dock bps and send them back
to `D`.

---

# 14. BOSS ROUND — solve the system by hand, in fractions

**Round types: PREDICT-THEN-REVEAL, then INTERROGATION.** No calculator until after the commit. The
elimination below is designed to be done mentally; the answer is designed so that no amount of
squinting produces it.

## 14.1 The data — a new month

Same five names, new month. Nothing is carried over from Sections 3–11.

| Stock | cheapness `x` | size `s` | return `r` |
|---|---:|---:|---:|
| AXL | −2 | 0 | −2.0% |
| BRN | −1 | −1 | −2.0% |
| CHR | 0 | −1 | +3.0% |
| DLT | +1 | +1 | +2.0% |
| EMK | +2 | +2 | +2.0% |

Two design notes for the game master, both worth saying at the table:

- **CHR has `x = 0` again** — and this time it is *not* unreachable, because `s = −1` gives the model
  a second way to touch it. Level 0's CHR trap was "no `b` can ever predict this stock". A second
  column dissolves that particular trap. It does not dissolve the *idea*: whatever no column reaches
  is still specific return.
- **`Σx = 0` but `Σs = 1`.** Do not let the player assume centring; it is not there, and `Σe` will not
  be zero.

## 14.2 The commit (before any arithmetic)

Ask for **three** things, out loud, with reasons:

1. The sign of `b₁`. (Returns rise with `x` across the table → positive.)
2. The sign of `b₂`. **This is the trap.** Eyeballing the size column alone, the two positive-`s`
   stocks (DLT, EMK) both returned +2 and the two negative-`s` stocks returned −2 and +3, so it
   *looks* positive. `Σs·r = 5 > 0` confirms the eyeball. The joint answer is **negative**.
3. Whether `b₁` will come out bigger or smaller than the cheapness-alone answer `Σxr/Σx² = 12/10 = 1.2`.

Full bps only for a reason that mentions the two columns pulling on each other. "It feels positive"
earns nothing.

## 14.3 The six sums

Two columns of products, five rows each. Do it as a table; every entry is an integer.

| Stock | `x` | `s` | `r` | `x²` | `s²` | `x·s` | `x·r` | `s·r` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AXL | −2 | 0 | −2 | 4 | 0 | 0 | +4 | 0 |
| BRN | −1 | −1 | −2 | 1 | 1 | +1 | +2 | +2 |
| CHR | 0 | −1 | +3 | 0 | 1 | 0 | 0 | −3 |
| DLT | +1 | +1 | +2 | 1 | 1 | +1 | +2 | +2 |
| EMK | +2 | +2 | +2 | 4 | 4 | +4 | +4 | +4 |
| | **Σx = 0** | **Σs = 1** | **Σr = 3** | **Σx² = 10** | **Σs² = 7** | **Σxs = 6** | **Σxr = 12** | **Σsr = 5** |

Also `Σr² = 4 + 4 + 9 + 4 + 4 = 25`.

`Σxs = 6`, and it is large: the columns overlap heavily. Flag it before solving.

## 14.4 The system, and two ways to eliminate

```
(1)   10 b₁ +  6 b₂  =  12
(2)    6 b₁ +  7 b₂  =   5
```

**Route A — kill `b₁`.** Multiply (1) by 3 and (2) by 5, so both have `30 b₁`:

```
(1)×3 :   30 b₁ + 18 b₂ = 36
(2)×5 :   30 b₁ + 35 b₂ = 25
subtract:         17 b₂ = −11        →      b₂ = −11/17

back into (1):  10 b₁ = 12 − 6(−11/17) = 12 + 66/17 = (204 + 66)/17 = 270/17
                                        →      b₁ = 27/17
```

**Route B — kill `b₂`.** Multiply (1) by 7 and (2) by 6, so both have `42 b₂`:

```
(1)×7 :   70 b₁ + 42 b₂ = 84
(2)×6 :   36 b₁ + 42 b₂ = 30
subtract: 34 b₁         = 54         →      b₁ = 54/34 = 27/17

back into (2):   7 b₂ = 5 − 6(27/17) = 5 − 162/17 = (85 − 162)/17 = −77/17
                                        →      b₂ = −11/17
```

**Route C — the cross-multiplication formula, as a check.**

```
D  = Σx²Σs² − (Σxs)² = 10·7 − 36 = 34
b₁ = (Σxr·Σs² − Σsr·Σxs)/D = (12·7 − 5·6)/34 = (84 − 30)/34 = 54/34 = 27/17
b₂ = (Σx²·Σsr − Σxs·Σxr)/D = (10·5 − 6·12)/34 = (50 − 72)/34 = −22/34 = −11/17
```

Notice Route B's leading coefficient, `34`, **is** `D`. That is not luck; eliminating one unknown
from a 2×2 system always leaves the determinant standing in front of the other.

```
b₁ = 27/17 = 1.5882    (rounded)
b₂ = −11/17 = −0.6471  (rounded)
```

Neither is a number a player could have guessed, and both denominators are 17 — a prime that appears
nowhere in the data and is manufactured entirely by the elimination.

## 14.5 The checks the player runs before submitting

**Check A — residuals, and both planks level.**

| Stock | `x` | `s` | `r` | fitted `b₁x + b₂s` | `e` | `x·e` | `s·e` |
|---|---:|---:|---:|---:|---:|---:|---:|
| AXL | −2 | 0 | −2 | −54/17 | **+20/17** | −40/17 | 0 |
| BRN | −1 | −1 | −2 | −16/17 | **−18/17** | +18/17 | +18/17 |
| CHR | 0 | −1 | +3 | +11/17 | **+40/17** | 0 | −40/17 |
| DLT | +1 | +1 | +2 | +16/17 | **+18/17** | +18/17 | +18/17 |
| EMK | +2 | +2 | +2 | +32/17 | **+2/17** | +4/17 | +4/17 |
| | | | | | | **Σ = 0** | **Σ = 0** |

```
CHECK 1   Σ x·e = (−40 + 18 + 0 + 18 + 4)/17 = 0/17 = 0     ✓
CHECK 2   Σ s·e = (  0 + 18 − 40 + 18 + 4)/17 = 0/17 = 0     ✓
```

Every residual has denominator 17. If the player's residuals do not, the arithmetic slipped.

**Check B — `Σe²` two ways.**

```
from the residuals :  (20² + 18² + 40² + 18² + 2²)/17² = (400+324+1600+324+4)/289
                    = 2652/289 = 156/17 = 9.1765     (rounded)
from the sums      :  Σr² − b₁Σxr − b₂Σsr = 25 − (27/17)(12) − (−11/17)(5)
                    = 25 − 324/17 + 55/17 = 25 − 269/17 = (425 − 269)/17 = 156/17     ✓
```

**Check C — `Σe` is not zero and must not be expected to be.**

```
Σe = (20 − 18 + 40 + 18 + 2)/17 = 62/17 = 3.6471    (rounded)
```

There is no column of ones, so nothing forces it. A player who "fixes" this has a Level 5 gap.

## 14.6 The wrong methods, priced

| Method | `b₁` | `b₂` | `SS` | `SS` ÷ best | penalty `Q(δ₁,δ₂)` |
|---|---:|---:|---:|---:|---:|
| **solve the system** | **27/17 = 1.5882** | **−11/17 = −0.6471** | **156/17 = 9.1765** | **1.0000** | **0** |
| one pass of the chase | 6/5 = 1.2 | −11/35 = −0.3143 | 1734/175 = 9.9086 | 1.0798 | 2178/2975 = 0.7321 |
| cheapness alone, size dropped | 6/5 = 1.2 | 0 | 53/5 = 10.6 | 1.1551 | 121/85 = 1.4235 |
| **two separate one-column fits** | 6/5 = 1.2 | **+5/7 = +0.7143** | 606/35 = 17.3143 | 1.8868 | 4842/595 = 8.1378 |
| size alone, cheapness dropped | 0 | +5/7 = +0.7143 | 150/7 = 21.4286 | 2.3352 | 1458/119 = 12.2521 |
| give up: predict zero | 0 | 0 | 25 | 2.7244 | 269/17 = 15.8235 |

(decimals rounded; every fraction exact. `Q(δ₁,δ₂) = 10δ₁² + 12δ₁δ₂ + 7δ₂²` with `δ` measured from
the true pair — checked to equal the SS gap in every row.)

**The one to interrogate is row 4.** Two separate one-column fits give `b₂ = +5/7`, and the truth
is `b₂ = −11/17`. Not a small error — **the wrong sign**. The reported model scores `1717/910 =
1.8868×` worse than the right one, and `606/371 = 1.6334×` worse than simply deleting the size
column. A risk desk that ran its columns one at a time would publish a size factor return of
`+0.71%` for a month in which the size factor actually returned `−0.65%` (both rounded to the
nearest 0.01%).

**The one to be frightened of is row 2.** One pass of the chase scores `9.9086` against `9.1765` —
`4913/4550 = 1.0798×`, under **8% worse** on the loss function. It looks fine. But the number a risk model actually *reports*
is the coefficient, not the loss, and:

```
one-pass b₂ = −11/35 = −0.3143      true b₂ = −11/17 = −0.6471      (both rounded)
ratio = 17/35 = 0.4857              the truth is 35/17 = 2.0588 times bigger
```

**One pass captured less than half of the size factor return, while the fit quality barely moved.**
`Σe²` is nearly blind to this; the coefficient is not. Say the general form plainly, because it is a
professional instinct rather than a fact about this dataset: *a small improvement in fit can sit on
top of a very large error in the individual coefficients, and a risk model consumes the
coefficients.*

The `b₁` error, for completeness: `(6/5 − 27/17)/(27/17) = −11/45 = −0.2444`, i.e. 24.4% too small
(rounded).

## 14.7 The chase on the boss data — five passes and still not there

```
k = (Σxs)²/(Σx²·Σs²) = 36/70 = 18/35 = 0.5143       (rounded)
1 − k = D/(Σx²Σs²) = 34/70 = 17/35
```

`k = 18/35` is much closer to 1 than the derivation set's `1/3`, so the chase is much slower.

| pass | `b₁` | `b₁` rounded | `b₂` | `b₂` rounded | `SS` rounded |
|---:|---:|---:|---:|---:|---:|
| 1 | 6/5 | 1.200000 | −11/35 | −0.314286 | 9.9086 |
| 2 | 243/175 | 1.388571 | −583/1225 | −0.475918 | 9.3701 |
| 3 | 9099/6125 | 1.485551 | −23969/42875 | −0.559044 | 9.2277 |
| 4 | 329157/214375 | 1.535426 | −903067/1500625 | −0.601794 | 9.1900 |
| 5 | 11712951/7503125 | 1.561076 | −32762081/52521875 | −0.623780 | 9.1801 |
| **∞** | **27/17** | **1.588235** | **−11/17** | **−0.647059** | **9.1765** |

The relative error in `b₂` after `n` passes is exactly `k^n = (18/35)^n`:

| `n` | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| relative error | 0.514286 | 0.264490 | 0.136023 | 0.069955 | 0.035977 | 0.018502 | **0.009515** |

**Seven full passes to get `b₂` within 1%.** Six is not enough — `0.018502`, i.e. 1.85%. And after
every single one of those passes one of the two planks is still off level: the cheapness imbalance
left standing at the end of pass 1, 2, 3 is `Σx·e = 66/35`, then `1188/1225`, then `21384/42875`,
each exactly `18/35` of the one before.

Meanwhile the elimination in Section 14.4 took about forty seconds and was exact.

> **The line the player must be able to say:** *"It is not two problems. Two conditions on the same
> five residuals is one system, and solving it one condition at a time converges to the answer
> instead of reaching it — geometrically, at a rate set by how much the two columns overlap."*

## 14.8 Boss-round pass conditions

Do not promote on `27/17` alone. Promote when all five hold:

1. They write down **both** balance conditions before solving, and can say why each must be zero
   (the nudge argument, with the other dial held fixed).
2. They turn the two conditions into two equations by expanding `e = r − b₁x − b₂s` — not by
   quoting a formula.
3. They solve by elimination in **fractions**, and check by a second route (the other elimination,
   or the cross-multiplication formula).
4. Under interrogation — *"just fit them separately, it's the same thing"* — they refuse, and can
   quantify: `+5/7` versus `−11/17`, a sign error, `1.8868×` worse than the joint fit and worse than
   dropping the column.
5. They can state what `Σxs = 0` would have bought them and why it is not available here.

**Failure protocol trigger.** If the player insists that `b₁` should be `Σxr/Σx²` regardless of the
size column, stop the level. Go back to Section 3's demonstration — `Σx·e = 0` and `Σs·e = 4` at the
Level 1 answer — and rebuild from there. That is a Level 2 gap (what a balance condition *is*), not a
Level 3 gap, and pushing forward will not fix it.

---

## 15. Ladder position after this level

| Concept | Target tier |
|---|---|
| two balance conditions holding simultaneously | 4 — defend under attack |
| turning balance conditions into normal equations | 4 |
| solving a 2×2 system by elimination, in fractions | 5 — rebuild on new data |
| the two-dial nudge identity, and its cross-term | 3 — derive from nothing |
| `D = Σx²Σs² − (Σxs)²` and what its size means | 3 |
| the one-at-a-time chase and why it converges rather than lands | 3 |
| the contraction factor `k = (Σxs)²/(Σx²Σs²)` | 2 — compute |
| why the joint and univariate coefficients differ | 1 — recognise (Level 4 owns this) |

---

## 16. Back to BFRE — what this machinery does in the real model

### The system is equation (1.9), p.25

**p.25, equation (1.9)** — the first pass of the factor return estimation, transcribed in
`notes/chunk_19-27.md` and re-verified there on a 5× crop:

```
r = X_Mkt·f_Mkt + Σ_{i∈Sty} X_Sty,i·f_Sty,i + Σ_{j∈CInd} X_CInd,j·f_CInd,j
                + Σ_{k∈CCty} X_CCty,k·f_CCty,k + u
```

Four blocks — market, style, core industry, core country — **in one regression, in one pass.** Every
one of those columns is a plank. Every one of them carries a balance condition against the same `u`.
They all have to be level at once, which makes them one simultaneous system exactly like the 2×2 the
player just solved, only with as many equations as there are factors.

The page also names the two-pass architecture and the weighting, so the conditions BFRE's `u`
actually satisfies are the **weighted** ones — `Σ w_i X_ij u_i = 0` per column `j`, with
`w_i = √(market cap)` (p.25's weighting paragraph is quoted in full at Level 1, and Level 2 put it
to work in its weighted balance check; the balance conditions themselves are **not** in the paper,
as Level 2 established and the closing section below re-confirms). Nothing in this level changes
under weights; every sum grows one `w`.

### p.5 is the paper saying this level's point in its own words

**p.5**, as recorded in `notes/chunk_1-9.md`. *Provenance flag, because it matters here:* the notes
carry this as a **claim entry with the key phrases bolded**, not as a fully quoted sentence — so the
phrases below are the paper's wording and the connective prose is the transcriber's. Quote the
phrases; do not quote the sentence as if it were printed that way.

> Country factor returns are estimated in a **"multivariate regression together with other common
> factors"**, and are therefore adjusted to be **"neutral with respect to market, style and industry
> effects"**.

The justification recorded on the same line is a country *"with a large concentration in a single
industry"* — which is, in the paper's own vocabulary, `Σ x·s ≠ 0` between a country column and an
industry column.

Read that sentence with this level in hand and it stops being a claim and becomes a consequence.
"Neutral with respect to industry effects" is precisely the industry balance conditions holding *at
the same time as* the country ones. Solve the country factors on their own and that neutrality is
simply gone — the country number would carry whatever the industry number should have carried, which
is Section 9's sign flip in production clothes. **The word doing all the work in the paper's
sentence is "together".**

There is a second, sharper consequence the paper states elsewhere and does not connect: p.26's
second pass, equation **(1.11)**, fits Extended Industry and Extended Country factors *to the
first-pass residuals `u`*. So any error in the first pass's joint solve is baked into `u` before the
emerging-market and frontier factors are ever estimated, and they are never re-estimated afterwards.
One-at-a-time error does not stay local.

### Where BFRE deliberately buys itself the well-engineered shower

**p.10** states the standardisation rule for exposures, word-for-word:

> *"The mean is defined as the square-root of market capitalisation weighted average value so that
> the transformed substyles (and styles) have the property that their **weighted average is zero**."*

That is **PAPER**. Here is the **INFER**, and it should be labelled as an inference at the table
because the paper never draws it: the market column is all ones, so the interference term between
the market column and any style column is

```
Σ w_i · 1 · X_Sty,i  =  (the weighted average of that style) × (Σ w)  =  0
```

**BFRE has engineered `Σxs = 0` between market and every style, on purpose, before the regression
runs.** That block of the system decouples exactly the way Level 2's boss round did. It is the same
trick, done deliberately, at production scale — and it is Level 5's subject.

What it does **not** buy: style-versus-style, industry-versus-country, or style-versus-industry
interference. Those are all still there, which is why (1.9) has to be one solve.

### How hard is the real problem? Figure 1.3, p.11

Figure 1.3 (NAMR model, Dec 2013) prints the correlations *between columns of `X`* — all 144 cells
re-read cell-by-cell in `notes/chunk_10-18.md`. Only the `ρ` column below is the paper's; `k = ρ²`
and the pass counts are **this level's arithmetic applied to the paper's numbers**, and the paper
computes neither:

| Pair | `ρ` (printed) | `k = ρ²` | passes of the chase to get within 1% |
|---|---:|---:|---:|
| Size – Liquidity | **0.74** | 0.5476 | **8** |
| Earnings Yield – Profitability | 0.64 | 0.4096 | 6 |
| Volatility – Dividend Yield | −0.46 | 0.2116 | 3 |
| Size – Volatility | −0.36 | 0.1296 | 3 |
| **Size – Value** | **0.00** | 0.0000 | **1 — one pass is exact** |

Two honest notes the game master must make:

- **This level's boss round is calibrated to the paper's hardest real pair.** The boss columns have
  `Σxs = +6 > 0`, so their correlation is `+√(18/35) = +0.7171` (rounded), sitting just under
  Size–Liquidity's `+0.74`. The seven passes the boss round needs and the eight the real worst pair
  would need are the same problem.
- **The two columns this level actually teaches with are, in the real NAMR model, the easy case.**
  Figure 1.3 reports Size–Value at **0.00**. Our teaching data makes them interfere strongly —
  `Σxs = −5`, so `ρ = −√(1/3) = −0.5774` (rounded) — because the mechanism needs to be visible; the
  real pair happens not to. (Compare signed numbers with signed numbers here: `√k` is only the
  size, and two of the five pairs listed above, `−0.46` and `−0.36`, are negative too.)
  Say this out loud rather than letting the player walk away believing value and size collide in
  BFRE. They do not. Size and *liquidity* do.

*One further caveat, flagged rather than smoothed over:* Figure 1.3's correlations are computed on
BFRE's standardised (weighted-mean-zero) exposures, while our `k` is computed on raw uncentred
columns, because our fit has no intercept. On the boss data the centred version is
`k = 9/17`, i.e. `√k = 0.7276` (rounded) against the uncentred `0.7171` — close enough to calibrate
with, different enough to name. Centring is Level 5.

### The alarm the desk actually runs, and the cliff at the end

**p.32**, on model estimation diagnostics:

> *"The final set of diagnostics are **variance inflation factors**. These help diagnose issues
> relating to multicollinearity between the style factors. If style exposures are too closely
> correlated then the regression procedure will encounter problems in **apportioning the factor
> return between them**. This can result in **significant instability in the factor return estimates
> through time**."*

and **footnote 16** on the same page:

> *"In the most extreme case, where factor exposures are **perfectly correlated**, identification
> issues will exist causing the estimation process to **fail**."*

That footnote is `D = 0`, in the paper's own words. Sections 8 and 8a are what it means: when `D`
hits zero the tax term `Q` stops being strictly positive, a whole line of nudges costs nothing, and
there is no unique best pair to find. **"Identification issues" is a polite way of saying the two
lines `L₁` and `L₂` have stopped crossing at a point and become one and the same line.**

Note which failure the paper is describing. The direct solve divides by `D`, so at `D = 0` it
divides by zero and *fails loudly* — which is what footnote 16 says. The chase does not fail loudly.
Run it on two exactly-proportional columns and it stops moving after a single step and hands back a
confident-looking pair of numbers; it is just that *which* pair depends entirely on the guess it
started from, and every one of them fits the data equally well. **The one-at-a-time method's real
danger is not that it is slow. It is that at the cliff edge it stops warning you.** That contrast —
loud failure versus silent arbitrariness — is Level 4's, and worth the player hearing once here.

The paper reports that VIFs *"were found to be well within suitable thresholds"* — and, as
`notes/chunk_28-36.md` records explicitly, **no numeric VIF values and no thresholds are printed
anywhere.** That is a Level 12 entry: a diagnostic asserted to pass, with neither the statistic nor
the bar disclosed.

### The exact collision BFRE ships with on purpose — p.26, equation (1.10)

**p.26:**

> *"This specification is not uniquely identified as there are an infinite number of possible
> solutions. The reason for this lies in the fact that, for each asset, there exist three intercept
> terms – the market factor, an industry factor, and a country factor. **Every asset has unit
> exposure to these three factors.** This can be resolved by adding two linear restrictions on the
> definition of the factor returns, which reduces the intercept terms from three to one."*

The player met this at Level 2 as "imposed versus guaranteed". They can now see *why* it is
unavoidable: three columns of ones are exactly proportional to each other, so `D = 0` exactly, and
"an infinite number of possible solutions" is the literal, arithmetical truth — the same statement as
`Q(p,q) = 0` along a line. Equation (1.10) does not estimate anything; it picks one point on that
line by decree:

```
Σ_j ω_CInd,j · f_CInd,j = 0        Σ_k ω_CCty,k · f_CCty,k = 0
```

(the second sum is printed in the source with index `j` over a summand subscripted `k`;
`notes/chunk_19-27.md` re-verified this at 6× and records it as a typo in the original, corrected
here.) The paper adds: *"This identification simply represents a rotation of the factor returns. It
does not impact the efficacy of the risk model."*

### What the notes do NOT support

Searched all 65 transcribed pages in `notes/`:

| Term | Hits |
|---|---:|
| `normal equation` | **0** |
| `least squares` | **0** |
| `simultaneous` | **0** |
| `system of equations` | **0** |
| `determinan`(t) | **0** |
| `invers`/`invert` | **0** |
| `multivariate` | 2 — p.5 (country factors) and p.8 (the industry-selection regressions) |
| `multicollinear` | 3 — all on p.32 (two in quoted paper text, one in the transcriber's terms list) |

So the paper **never writes the normal equations, never names the estimator, and never mentions a
determinant or a matrix inverse.** What it does give, and what this level's tie-back rests on, is:
(1.9) putting four factor blocks in a single regression (p.25); the word *"multivariate"* attached to
country factors with the consequence spelled out (p.5); the identification failure and its fix
(p.26, eq. 1.10); and the multicollinearity diagnostic with its footnote (p.32).

**No BFRE anchor was found in `notes/` for the 2×2 system itself, or for `D`, as printed
mathematics.** State that to the player in those words. The machinery on this page is the standard
machinery the paper's language requires and never writes down — which is the same gap Levels 1 and 2
found, now one level deeper, and a standing entry for Level 12 (The Critique).

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level3.py     # 340 exact-rational checks, exits 0
```

The script recomputes every figure on this page from the raw `x`, `s` and `r` columns in
`fractions.Fraction`: the six sums for both datasets, the two-column nudge identity over 1,764
`(b₁, b₂, p, q)` combinations, both elimination routes and the cross-multiplication formula, the
completed square and the penalty form over 49 `(p, q)` pairs each, every residual and both balance
sums, every wrong method's numeric output and its penalty, the full chase pass by pass with its
exact contraction ratio, the `(k)^n` error law, the number of passes needed at four interference
levels, and the determinant collapsing to zero as one column slides onto the other. If any printed
value ever disagrees with this markdown, the markdown is wrong.
