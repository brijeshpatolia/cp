# Level 0 — The Miss (and the cold open)

Every number below is recomputed in exact rational arithmetic by
`tools/verify_coldopen.py` and `tools/verify_level0_boss.py`. Nothing here is rounded by hand.

---

## Cold open — five stocks, one characteristic

Presented to the player before anything is taught. The characteristic is called a "cheapness
score" and nothing else: the words *exposure*, *factor* and *regression* stay locked until the
player has built the mechanism.

| Stock | Cheapness score `x` | Return `r` |
|---|---:|---:|
| AXL | −1.5 | −2.0% |
| BRN | −0.5 | −2.0% |
| CHR | 0.0 | +0.5% |
| DLT | +1.0 | +4.0% |
| EMK | +2.0 | +3.5% |

The player is asked to commit to a single `b` in `predicted return = b × x`, and to say how they
got it.

### The answer, and why the shortcuts fail

```
Σx   = 1          Σx² = 15/2 = 7.5        Σxr = 15        Σr = 4
b    = Σxr / Σx²  = 15 / 7.5 = 2          exactly
```

Three methods a beginner actually reaches for, and what each returns:

| Method | Value | Verdict |
|---|---:|---|
| least squares, `Σxr / Σx²` | **2.0000** | correct |
| "total return ÷ total exposure", `Σr / Σx` | 4.0000 | **100% too big** |
| "average the per-stock slopes", `mean(r/x)` | 2.7708 | 39% too big |

The per-stock slopes `r/x` are **1.3333, 4.0000, 4.0000, 1.7500** — they disagree wildly with each
other, which is the hook: there is no single ratio sitting in the data waiting to be read off. `b`
has to be *chosen* to minimise something, and Level 0 is about what that something is.

### The residuals at b = 2

```
e = r − 2x   =   +1,  −1,  +0.5,  +2,  −0.5
Σe    = 2      ← NOT zero. A no-intercept fit does not force the misses to cancel.
Σx·e  = 0      ← this is what least squares forces. Level 2 lives here.
Σe²   = 6.5
```

That `Σe = 2` while `Σx·e = 0` is worth holding onto — it is the whole content of Level 5 (what
changes when an intercept is added) sitting in plain sight at Level 0.

### The parabola, for free

`SS(b) = Σr² − 2b·Σxr + b²·Σx² = 36.5 − 30b + 7.5b²`

| `b` | 1.5 | 2.0 | 2.5 | 2.7708 | 4.0 |
|---|---:|---:|---:|---:|---:|
| `SS` | 8.3750 | **6.5000** | 8.3750 | 10.9564 | 36.5000 |

`SS(1.5) = SS(2.5)` exactly. Symmetric about `b = 2`, so the player can *see* the minimum without
calculus — which is how Level 1 derives `b = Σxr/Σx²` by nudging, before derivatives exist.

Also note `SS(0) = 36.5 = Σr²`: the total sum of squares is just "the miss you'd have if you gave
up and predicted zero for everyone." That is the denominator of R², arriving three levels early.

### The CHR trap

CHR has `x = 0.0` and `r = +0.5%`. No value of `b` can predict it — `b × 0 = 0` always. The player
must recognise this is not a flaw to be fixed but the definition of the thing the model calls
**specific return**: the part of a stock's move that no common characteristic can reach. In BFRE
that is `u` in the asset return equation and it is what the whole `D` matrix is built to forecast
(Level 9).

---

## Level 0 boss round — three desks, identical raw sum of misses

Three desks all fit the same rule `r = 2x` to four stocks with `x = [−2, −1, +1, +2]`. All three
report the same headline diagnostic: **the misses sum to zero**.

| Desk | Returns `r` | Misses `e` | `Σe` | `Σ\|e\|` | `Σe²` |
|---|---|---|---:|---:|---:|
| **A** tight | −3.5, −2.5, +1.5, +4.5 | +0.5, −0.5, −0.5, +0.5 | **0** | 2 | **1** |
| **B** blown out | +2, −8, −4, +10 | +6, −6, −6, +6 | **0** | 24 | **144** |
| **C** perfect | −4, −2, +2, +4 | 0, 0, 0, 0 | **0** | 0 | **0** |

`Σx·e = 0` for all three, so `b = 2` genuinely *is* the least-squares fit in every case — the
sabotage is not in the fit, it is in the diagnostic. A raw sum of misses cannot tell a perfect
model from a catastrophic one, because it reports cancellation, not size. Desk B's model is 144
times worse than Desk A's by the measure that matters and indistinguishable by the measure
reported.

### Why squares and not absolute values

Three stocks, all with `x = 1`, returns `r = [1, 2, 9]`:

| `b` | 1 | 2 | 3 | 4 | 9 |
|---|---:|---:|---:|---:|---:|
| `Σ\|e\|` | 9 | **8** | 9 | 10 | 15 |
| `Σe²` | 65 | 50 | 41 | **38** | 113 |

Least absolutes picks `b = 2`, the **median** — it throws the 9 away entirely, and would give the
same answer if that 9 were a 900. Least squares picks `b = 4`, the **mean**, which the outlier
moves. For a risk model this settles the argument in one line: a model whose job is to forecast how
badly things can go must be *more* sensitive to the big misses, not immune to them. Squaring is not
a mathematical convenience here — it is the choice that makes the loss function care about tails.
