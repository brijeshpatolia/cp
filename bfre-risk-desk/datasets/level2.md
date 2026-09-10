# Level 2 — The Balance

Every number below is recomputed in exact rational arithmetic by `tools/verify_level2.py`
(206 assertions, exits 0). Nothing here is rounded by hand. Every fraction used in this level
terminates, so **every decimal on this page is exact, not rounded** — `15/2` really is `7.5` and
`67/8` really is `8.375`.

---

## 0. What the player is already holding, and what is actually new

**From Level 0** — the cold-open dataset and the scorecard:

```
x = [−1.5, −0.5, 0, +1, +2]        r = [−2.0%, −2.0%, +0.5%, +4.0%, +3.5%]
Σx = 1     Σx² = 15/2     Σx·r = 15     Σr = 4     Σr² = 73/2 = 36.5
b = 2 exactly        e at b=2:  +1, −1, +0.5, +2, −0.5
Σe = 2      Σx·e = 0      Σe² = 13/2 = 6.5
SS(b) = 36.5 − 30b + 7.5b²,  symmetric about b = 2,  SS(1.5) = SS(2.5) = 8.375
```

**From Level 1** — the exact nudge identity, and the quantity that drives it:

```
SS(b + h) − SS(b)  =  −2h·P(b)  +  h²·Σx²          exact, every b, every h
P(b) = Σ x·(r − bx) = Σxr − b·Σx²                  Level 1 called it "the pull"
```

Level 1 already noticed the crucial thing and said so explicitly: **`r − bx` is the miss, so
`P(b) IS Σx·e`.** It then set `P(b) = 0` and solved, which is how `b = Σxr/Σx²` was derived without
calculus. Level 1's own words: *"Hold onto that; it is the entire content of Level 2."*

**So Level 2 does not discover a new fact.** It does three things to a fact the player already has:

| | What Level 2 adds |
|---|---|
| **A new reading** | `P(b)` was a *pull* — a force along a line, pointing at the answer. Level 2 re-reads the same number as a **turning force about a pivot**. That reading is what survives when there are many columns, because many pulls just add up into a mess, whereas many planks each balance separately. |
| **The converse** | Level 1 proved *best ⟹ pull is zero*. Level 2 proves the other direction too, so the balance becomes an **if and only if** — which is what licenses using it as a test. |
| **A change of job** | Level 1 used the zero **once**, as a step in a derivation, and then discarded it. Level 2 keeps it forever as a **permanent, auditable invariant of the output**. That is the whole boss round: you are handed a file and must decide whether it is real. |

State this to the player before starting. They will otherwise feel they are being shown the same
thing twice, resent it, and stop paying attention exactly when the new part arrives.

---

## 1. The story (no mathematics)

A carpenter has a long plank resting on a single stone. The stone is at the mark labelled zero.
Along the plank, at the marks −1.5, −0.5, 0, +1 and +2 metres, there are hooks.

She hangs a weight on each hook. Some are lead blocks pulling the plank down. Some are helium
balloons pulling it up. She lets go.

If the plank tips, she has learned something: the weights on one side are winning. If the plank
sits dead level, she has learned something else — the weights have *fought to a draw*.

Note what "a draw" does **not** mean. It does not mean the weights are small. She could hang a
hundred-kilo block at +2 and a hundred-kilo balloon at −2 and the plank would sit perfectly level
while being under enormous strain. Level is not the same as light.

And note what makes a draw: it is not the weights that matter, it is *weight times distance from
the stone*. A one-kilo block far out beats a five-kilo block sitting almost on the stone. The thing
that has to cancel is the **turning force**, and turning force is distance × weight.

---

## 2. Mapping the story onto the fit, line by line

| In the story | In the fit |
|---|---|
| the stone (the pivot) | the point `x = 0` |
| a hook at distance `x` from the stone | a stock with cheapness score `x` |
| the weight hanging there | that stock's miss, `e = r − b·x` |
| a lead block (pulls down) | a positive miss — the stock beat the model |
| a helium balloon (pulls up) | a negative miss — the stock lagged the model |
| turning force of one weight | `x · e` |
| total turning force | `P(b) = Σ x·e` — Level 1's pull, seen sideways |
| the plank sits level | `Σ x·e = 0` |
| the plank is heavy but level | `Σe ≠ 0` while `Σx·e = 0` |

The last row is the cold open, exactly. `Σe = 2` and `Σx·e = 0`. Heavy plank, level plank.

**The claim to be nailed down:**

> `b` is the best possible dial setting **if and only if** the plank is level. Not usually — always,
> as a matter of arithmetic, on any data whatsoever.

---

## 3. The proof, in the balance reading

Write `Q = Σx²` and `P = Σx·e`, the misses at the current setting `b`. Both are numbers you compute
straight off the table.

### 3a. The identity, re-derived in three lines (Level 1 already has this)

Nudge the dial from `b` to `b + h`. Every miss changes:

```
e_i(b+h) = r_i − (b+h)·x_i = (r_i − b·x_i) − h·x_i = e_i − h·x_i
```

Square it — this is just `(A − C)² = A² − 2AC + C²`, with `A = e_i` and `C = h·x_i`:

```
(e_i − h·x_i)² = e_i² − 2·h·x_i·e_i + h²·x_i²
```

Add over all five stocks. `h` and `h²` come out of the sums because they are the same for every
stock:

```
SS(b + h) = Σe² − 2h·Σx·e + h²·Σx²
          = SS(b) − 2h·P + h²·Q                     ← Level 1's nudge identity
```

If the player cannot reproduce these three lines unaided, stop and go back to Level 1. Level 2 is
not the place to repair it.

### 3b. Forward: best ⟹ level (the contradiction, sharpened)

Level 1's version chose a small enough `h` and argued the reward beats the tax. Here is the tighter
version, which the boss round needs because it produces a *number* rather than an existence claim.

Suppose `b` is the best setting **and**, for contradiction, that `P ≠ 0`.

`Q = Σx² > 0` — it is a sum of squares, zero only if every stock has `x = 0`, in which case there
is no model to fit. So we may divide by `Q`. Choose this specific nudge:

```
h = P / Q
```

Substitute into the identity:

```
SS(b + P/Q) = SS(b) − 2·(P/Q)·P + (P/Q)²·Q
            = SS(b) − 2P²/Q + P²/Q
            = SS(b) − P²/Q
```

`P ≠ 0` makes `P² > 0`, and `Q > 0`, so `P²/Q > 0`. The total squared miss went **strictly down**.
So `b` was not the best after all — contradiction. Therefore `P = 0`. ∎

Two things this sharper version buys that Level 1's did not:

- The nudge is not merely *some* improving step, it is the **best** one — no `h` does better, since
  `−2hP + h²Q` is a parabola in `h` with its own minimum at `h = P/Q`.
- The improvement is **exactly `P²/Q`**. The imbalance is not a vague warning light; it is a
  quantity of lost quality, in the same units as `SS`.

Read the choice in words: *nudge in the direction the imbalance is pointing.* If the plank tips
right, push the dial right. The fact that the imbalance can tell you which way to move is itself
the proof you were not yet at the bottom.

### 3c. Reverse: level ⟹ best

Usually skipped, and skipping it is why students file the balance condition under "side effect".
It is not a side effect. It is the definition.

If `P = 0`, the identity collapses to:

```
SS(b + h) = SS(b) + h²·Q
```

`h²·Q ≥ 0` for every `h`, and it is zero only when `h = 0`. So *every* nudge in *either* direction
makes things strictly worse. `b` is the best, and it is the only best. ∎

(Level 1 has this same content in a different dress — the penalty formula
`SS(b) − SS(b*) = Σx²·(b − b*)²`. Point that out: it is the identity with `P(b*) = 0` substituted
in. Same fact, and the player has now seen it twice from two directions, which is the point.)

Put the halves together:

> **`Σx·e = 0` if and only if `b` is the least-squares fit.**
> The balance is not a consequence of the answer. The balance *is* the answer, written differently.
> And because it runs both ways, it can be used as a **test**: a file that fails it was not produced
> by a least-squares fit of that data, full stop.

That last sentence is the licence for everything in the boss round.

### 3d. Honesty about difficulty

This proof is complete — not a sketch, nothing hidden. It uses `(A−C)² = A² − 2AC + C²` and the
fact that a square is never negative. A 12th-standard algebra student has every tool required.

It is also *the* standard derivation. A university course would set the derivative of `SS(b)` to
zero and get `−2Σx·e = 0` in one line — the same equation, after spending a term building
derivatives first. The nudge argument buys it with no calculus and generalises to many dials
without changing shape (Level 3).

---

## 4. The numbers: watch a bad dial repair itself

Start deliberately at the **wrong** setting `b = 1`.

```
e = r − 1·x  =  −0.5, −1.5, +0.5, +3, +1.5
Σe   = 3       (= Σr − b·Σx = 4 − 1 — nothing forces this to be anything)
P(1) = Σx·e  = (−1.5)(−0.5) + (−0.5)(−1.5) + 0 + (1)(3) + (2)(1.5)
             = 0.75 + 0.75 + 0 + 3 + 3 = 15/2 = 7.5     ← the plank is tipping
Q    = 15/2 = 7.5
SS(1) = 14
```

`P > 0` means "nudge right". How far? `ΔSS = −2h·P + h²·Q`, which with `P = Q = 15/2` is exactly
`ΔSS = (15/2)(h² − 2h)`:

| nudge `h` | lands on `b =` | `ΔSS = (15/2)(h²−2h)` | `SS(1+h)` | |
|---:|---:|---:|---:|---|
| −1 | 0 | +22.5 | 36.5 | worse — moved *away* from the tip |
| 0 | 1 | 0 | 14 | stayed |
| +0.5 | 1.5 | −5.625 | 8.375 | better |
| **+1** | **2** | **−7.5** | **6.5** | **best possible single nudge** |
| +1.5 | 2.5 | −5.625 | 8.375 | better, overshot a bit |
| +2 | 3 | 0 | 14 | overshot exactly enough to break even |
| +3 | 4 | +22.5 | 36.5 | worse |

Three things to make the player say out loud:

1. **The best nudge is `h = P/Q = (15/2)/(15/2) = 1`, and it lands exactly on `b = 2`.** From a
   wrong start, one step reaches the right answer. (One dial, one step. Level 3 is where that stops
   being true.)
2. **The improvement is exactly `P²/Q` = `(15/2)²/(15/2)` = `15/2` = 7.5**, and 14 − 7.5 = 6.5.
3. **Nudges help only while `0 < h < 2P/Q = 2`.** At `h = 2` (`b = 3`) you break exactly even:
   `SS(3) = SS(1) = 14`. Past that you are worse off. Overshoot is real.

And now the symmetry Level 0 spotted for free is *explained*. At `b = 2` we have `P = 0`, so:

```
SS(2 + h) = 6.5 + 7.5·h²        depends on h² only  →  symmetric about b = 2
h = ±0.5 → 6.5 + 1.875 = 8.375        (= SS(1.5) = SS(2.5), exactly as Level 0 reported)
h = ±1   → 6.5 + 7.5    = 14          (= SS(1)   = SS(3))
```

Name that call-back to the player: they *observed* the symmetry at Level 0 and were told it was a
freebie. `P = 0` is why.

---

## 5. What the balance does NOT say — the professional point

This is the paragraph students skip, and it is the reason the level exists.

`Σx·e = 0` **holds for every least-squares fit, including catastrophically bad ones.** It is
produced by the arithmetic, not by the data cooperating. So it can never, under any circumstances,
be evidence that a model is any good.

Level 0's desks, dragged back in:

| Desk | misses `e` on `x = [−2, −1, +1, +2]` | `Σx·e` | `Σe²` |
|---|---|---:|---:|
| A — tight | +0.5, −0.5, −0.5, +0.5 | **0** | 1 |
| B — blown out | +6, −6, −6, +6 | **0** | 144 |

Desk B's model is **144 times worse** than Desk A's, and the balance condition reports both as
perfect. Heavy plank, level plank. A quant who says *"my residuals are orthogonal to my factors, so
the model is well specified"* has said nothing at all and should be told so. (`orthogonal` is the
name for this condition and stays locked until Section 8 — it is previewed here only so the game
master can put it in a hostile CRO's mouth during a boss round.)

The correct use of the balance condition is the opposite one:

> It is a check that the **arithmetic ran**, not a check that the **model is right**.
> If it fails, something is broken — a bug, a corrupted file, a mis-aligned join, a stale exposure.
> If it holds, you have learned precisely nothing about the world.

That is what the boss round is built on, and it is what BFRE p.16 works around when it hunts for a
missing factor (Section 12).

---

## 6. Traps, and what each wrong belief returns numerically

| Wrong belief | What it actually equals on the cold-open data | Why it is wrong |
|---|---:|---|
| "the misses sum to zero" | `Σe = 2` | Only `Σx·e` is forced. `Σe = Σr − b·Σx = 4 − b`, which is 2 at `b = 2` and 3 at `b = 1`. To force `Σe = 0` you need a column of 1s in the fit — Level 5, and the reason BFRE has a market factor. |
| "the misses are unrelated to the returns" | `Σr·e = 13/2 = 6.5` | The miss balances against the **fitted** values, not the raw ones. `Σ(2x)·e = 0`, but `Σr·e = Σ(bx + e)·e = b·0 + Σe² = Σe²`. It equalling 6.5 rather than 0 is not a bug, it is a *theorem* — and 6.5 is `Σe²` itself. |
| "balance means the misses cancel out" | `Σe = 2 ≠ 0` while `Σx·e = 0` | Torque cancels; weight does not. The plank is level *and* heavy. |
| "`Σx·e = 0` means the fit is good" | Desk B: `Σx·e = 0`, `Σe² = 144` | Guaranteed by construction. Zero information about quality. |
| "the balance is broken, so re-fit" | from `b = 1`, `P = 7.5`, best nudge `h = 1` | Right here, but only because the *data* is trusted. In the boss round the data is what is wrong, and re-fitting would launder the corruption into the answer. This is the real production failure mode. |

---

## 7. Which plank are you auditing? (weights)

Level 1 already built the weighted dial `b_w = Σw·x·r / Σw·x²` from the same nudge argument, and
already showed on its boss data that `Σ w·x·e = 0` while `Σ x·e = −42/43 ≠ 0`. Do not re-teach it.
The Level 2 point is narrower and is about **the audit, not the estimator**:

> A balance check only fires correctly if it carries the same weights the fit did. Run an
> unweighted check on a weighted fit and it will report a broken file that is perfectly clean.

Here it is on the data the player knows best, with `w = [11, 1, 1, 1, 1]` — one mega-cap next to
four minnows (a square-root-of-cap ratio of 11 is a market-cap ratio of 121, an ordinary spread for
a real universe):

```
Σw = 15        Σw·x² = 30        Σw·x·r = 45        b_w = 45/30 = 3/2
e at b_w = 3/2:   +0.25, −1.25, +0.5, +2.5, +0.5
```

| | `Σ w·x·e` | `Σ x·e` |
|---|---:|---:|
| at the weighted fit `b_w = 3/2` | **0** | 15/4 = 3.75 |
| at the unweighted fit `b = 2` | −15 | **0** |

Both files above are *clean*. Both would be flagged as sabotaged by the wrong check. And the
weights are not cosmetic: they moved the answer from 2 to 1.5, a 25% swing in the factor return.

---

## 8. Names unlocked (Level 1 locked these on purpose; they are earned now)

| The thing the player just built | The name it goes by |
|---|---|
| `Σx·e = 0`, one per column | the **normal equation** for that column |
| that zero, seen as a sum of products of two paired lists | the residual is **orthogonal** to the exposure — a dot product equal to zero, i.e. perpendicular |
| the whole list `e` | the **residual vector** |
| "the fit is the setting whose plank balances" | the **first-order condition** of least squares |

Still locked after this level: *design matrix*, *degrees of freedom*, *standard error*, *R²*,
*heteroskedasticity*, *multicollinearity*.

A sentence the player should now be able to produce unprompted, in a quant's register:

> *"By construction the residuals are orthogonal to every column of the design matrix, so the
> normal equations hold exactly — which makes them a check on the estimation, not evidence of
> specification."*

Round type F. The **second clause is the one that scores**. Anyone can say "orthogonal"; only
someone who built it knows the condition is uninformative about model quality. Awarding full bps
for the first clause alone is exactly the mimicry failure Victory Condition 2 is designed to catch.

---

# 9. BOSS ROUND — Sabotage

## 9.1 The setup

Same five stocks, **a new month**. New exposures, new returns — no number from the cold open or
from Level 1's boss round is reused here.

This month the desk fits **two** things at once: a market column `m` where every stock has exposure
1 (BFRE p.26: *"Every asset has unit exposure to these three factors"*), and the cheapness column
`x`. The fit is `r̂ = a·1 + b·x`, so there are now **two planks and both must be level**.

**The clean truth (not shown to the player):**

| Stock | market `m` | cheapness `x` | return `r` | fitted `r̂ = 0.5 + 2x` | miss `e` |
|---|---:|---:|---:|---:|---:|
| AXL | 1 | −2 | −2.5% | −3.5% | **+1** |
| BRN | 1 | −1 | −4.5% | −1.5% | **−3** |
| CHR | 1 | 0 | +2.5% | +0.5% | **+2** |
| DLT | 1 | +1 | +3.5% | +2.5% | **+1** |
| EMK | 1 | +2 | +3.5% | +4.5% | **−1** |

Confirming the fit by hand, which the player should do:

```
Σx = 0     so the two dials do not interfere and each has a one-line answer
Σx² = 4 + 1 + 0 + 1 + 4 = 10
Σx·r = (−2)(−2.5) + (−1)(−4.5) + 0 + (1)(3.5) + (2)(3.5) = 5 + 4.5 + 0 + 3.5 + 7 = 20
b = Σx·r / Σx² = 20 / 10 = 2
Σr = −2.5 − 4.5 + 2.5 + 3.5 + 3.5 = 2.5      a = r̄ = 2.5 / 5 = 0.5   (valid ONLY because Σx = 0)

Both planks are level:
  CHECK 1   Σm·e = Σe = 1 − 3 + 2 + 1 − 1 = 0
  CHECK 2   Σx·e      = (−2)(1) + (−1)(−3) + (0)(2) + (1)(1) + (2)(−1) = −2 + 3 + 0 + 1 − 2 = 0
  Σe² = 1 + 9 + 4 + 1 + 1 = 16
```

*Design note for the game master:* `Σx = 0` was chosen deliberately so the two dials decouple and
`a = r̄`, `b = Σxr/Σx²` each read off in one step. Making the columns interfere is Level 3's entire
job and must not be smuggled in here. Say so out loud — otherwise the player will file `a = r̄` as
a general law. It is not.

## 9.2 What the player actually receives

The specific-risk desk downstream does **not** get returns. It gets the exposure file and the
residual file — true of BFRE too: specific returns are what the specific-risk model consumes
(p.27: *"Specific returns are calculated using local asset excess returns, factor exposures and
(estimated) factor returns"*). And in production you cannot re-run the model on every file you are
handed. All you have is the file, and the identities it is supposed to satisfy.

**THE FILE AS RECEIVED. Exactly one residual has been overwritten. Find it.**

| Stock | `x` | residual `e` |
|---|---:|---:|
| AXL | −2 | +1 |
| BRN | −1 | −3 |
| CHR | 0 | +2 |
| DLT | +1 | +1 |
| EMK | +2 | 0 |

---

## 9.3 The answer

### Step 1 — run both checks

```
CHECK 1   Σe   = 1 − 3 + 2 + 1 + 0 = 1        should be 0     ✗ BROKEN
CHECK 2   Σx·e = (−2)(1) + (−1)(−3) + (0)(2) + (1)(1) + (2)(0)
               = −2 + 3 + 0 + 1 + 0 = 2       should be 0     ✗ BROKEN

per-stock turning forces  x·e  =  −2,  +3,  0,  +1,  0
```

### Step 2 — write down what a single corruption does

Exactly one cell `k` was overwritten. Call the amount it moved `δ`. The received residuals are the
true ones plus `δ` sitting in one place:

```
e_received = e_true          for every stock except k
e_received = e_true + δ      at stock k
```

Feed that through both checks. The true residuals contribute **zero to both** — that is exactly
what Section 3 proved, and it is why the proof had to run both directions — so only `δ` survives:

```
Σ e_received   = 0 + δ         →   δ = Σe = 1
Σ x·e_received = 0 + x_k·δ     →   x_k·δ = Σx·e = 2
```

### Step 3 — divide

```
x_k = (Σx·e) / (Σe) = 2 / 1 = 2
```

Only one stock in the file has `x = +2`. **The culprit is EMK.** Its true residual is `0 − 1 = −1`.

### Step 4 — repair and re-check (never skip this)

```
e_repaired = +1, −3, +2, +1, −1
Σe   = 0                              ✓
Σx·e = −2 + 3 + 0 + 1 − 2 = 0         ✓
```

Both planks level again. The chain is closed.

---

## 9.4 Why ONE check could never have done it

Suppose the file had no market column and all the player had was `Σx·e = 2`. Then `x_k·δ = 2` is
one equation in two unknowns, and **every stock with `x ≠ 0` is a live suspect**:

| suspect `k` | `x_k` | `δ` it would need (`= 2/x_k`) | repaired `e_k` | repaired vector | `Σe` | verdict |
|---|---:|---:|---:|---|---:|---|
| AXL | −2 | −1 | +2 | `[+2, −3, +2, +1, 0]` | 2 | reject |
| BRN | −1 | −2 | −1 | `[+1, −1, +2, +1, 0]` | 3 | reject |
| CHR | 0 | — | — | impossible: `0·δ = 0`, never 2 | — | cleared |
| DLT | +1 | +2 | −1 | `[+1, −3, +2, −1, 0]` | −1 | reject |
| **EMK** | **+2** | **+1** | **−1** | `[+1, −3, +2, +1, −1]` | **0** | **survives** |

Four live suspects on one check; exactly one survivor on two. The rule the player should be able to
recite:

> **One check detects. Two checks locate.**
> With one column you learn *that* something is wrong. With two columns whose `x` values are all
> different, you learn *where* — because `x_k = (Σx·e)/(Σe)` reads off the culprit's exposure
> directly, and one exposure names one stock.

This is also the honest preview of Level 3: more columns means more simultaneous balance
conditions, and the reason that is powerful rather than merely tedious is visible right here.

---

## 9.5 The wrong methods, and what each returns

| Method a player actually reaches for | What it returns | Verdict |
|---|---|---|
| "the biggest residual is the fake" — `\|e\| = 1, 3, 2, 1, 0` | **BRN** (3) | **Wrong stock.** Force BRN to carry the whole `δ = 1`: `e → [+1, −4, +2, +1, 0]`. Now `Σe = 0` ✓ but `Σx·e = −2 + 4 + 0 + 1 + 0 = 3` ✗. Fixing one check by hand while breaking the other is the signature of a guess. |
| "the biggest turning force is the fake" — `\|x·e\| = 2, 3, 0, 1, 0` | **BRN** (3) | **Wrong stock**, same failure. And note the corrupted cell EMK contributes `2 × 0 = 0` — the *smallest* turning force in the file. The saboteur is invisible on precisely the diagnostic that looks most relevant. |
| "the residual that is exactly 0 looks fake" | **EMK** | **Right stock, no reasoning — award zero bps.** Hard rule: never accept a right answer with wrong reasoning. Proof it is a coin-flip: in the near-miss below the corrupted cell is the **largest** number on the page, and this heuristic points confidently the other way. |
| "`Σe²` will show it" | corrupted **15**, clean **16** | **The check points backwards.** The sabotaged file scores *better* on sum of squares than the truth — of course it does, since the truth is the minimum for the real returns, so any tampering that drags a residual toward zero improves the metric. Fit quality is not a data-integrity check. |
| "re-fit `b` from the file" | there is no `r` in the file | Nothing to re-fit from. And if there were, re-fitting would silently absorb the corruption into `a` and `b` and return a beautifully balanced, wrong model. |

---

## 9.6 The near miss — the corruption the balance check cannot see

Same clean file. This time the saboteur hits **CHR**, moving its residual from `+2` to `+5`
(`δ = +3`).

| Stock | `x` | received `e` | turning force `x·e` |
|---|---:|---:|---:|
| AXL | −2 | +1 | −2 |
| BRN | −1 | −3 | +3 |
| **CHR** | **0** | **+5** | **0** |
| DLT | +1 | +1 | +1 |
| EMK | +2 | −1 | −2 |

```
CHECK 2   Σx·e = −2 + 3 + 0 + 1 − 2 = 0        ← PASSES. Completely blind.
CHECK 1   Σe   = 1 − 3 + 5 + 1 − 1 = 3         ← caught, by the market column alone
```

The cheapness balance is structurally incapable of seeing this. `x_CHR = 0`, so CHR's residual is
multiplied by zero before it is ever added up:

> **A check multiplies each error by that stock's exposure — so it is blind, by construction, to
> any stock whose exposure is zero.**

The market column saves the day, and in fact still identifies the culprit:

```
δ   = Σe = 3
x_k = (Σx·e)/(Σe) = 0/3 = 0        →  the only stock with x = 0 is CHR
repaired: 5 − 3 = +2   ✓
```

A balance sum of exactly zero *alongside a broken* `Σe` is itself a fingerprint: it says **the
culprit is sitting on the pivot.**

### The version with no escape: one column only

Go back to the cold open, where there was **no market column** — nothing forces `Σe` to anything,
so `Σe` is not a check, it is just a number. Corrupt CHR there, from `+0.5` to `+4`:

```
e = +1, −1, +4, +2, −0.5
Σx·e = (−1.5)(1) + (−0.5)(−1) + (0)(4) + (1)(2) + (2)(−0.5) = −1.5 + 0.5 + 0 + 2 − 1 = 0
```

`Σx·e` is **unchanged**. It was 0 before and it is 0 now. `Σe` moved from 2 to 5.5, but 2 was never
required in the first place, so that movement proves nothing. In a one-column world this corruption
is **undetectable, permanently, by any structural check available.**

Which is Level 0's CHR hook arriving with teeth. CHR was the stock no `b` could ever predict. It is
also the stock no exposure-weighted check can ever police. **The thing the model cannot see and the
thing the audit cannot see are the same stock, for the same reason** — and that reason is a zero in
the exposure column, which is also precisely what makes CHR's return *specific* (Level 9).

---

## 9.7 What NEITHER check can see — the honest limit

Give the player the general question: *which corruptions get through both checks?*

Let `Δ` be the vector of changes made to the residual file. The checks report `Σe` and `Σx·e`, so a
corruption is invisible exactly when

```
ΣΔ = 0        and        Σx·Δ = 0
```

**One cell.** `ΣΔ = Δ_k = 0` forces `Δ_k = 0`. No single-cell corruption ever escapes both checks —
which is why the boss round is solvable at all.

**Two cells `i, j`.** `Δ_i + Δ_j = 0` and `x_iΔ_i + x_jΔ_j = 0` give `Δ_i(x_i − x_j) = 0`. All five
`x` values in this file are different, so `Δ_i = 0`. No two-cell corruption escapes either.

**Three cells — and now it breaks.** Take `Δ = [+1, −2, +1, 0, 0]`:

```
ΣΔ   = 1 − 2 + 1 + 0 + 0 = 0                          ✓ invisible to CHECK 1
Σx·Δ = (−2)(1) + (−1)(−2) + 0 + 0 + 0 = −2 + 2 = 0    ✓ invisible to CHECK 2

sabotaged file:  e = +2, −5, +3, +1, −1
   Σe   = 0                                ✓ passes
   Σx·e = −4 + 5 + 0 + 1 − 2 = 0           ✓ passes
   Σe²  = 4 + 25 + 9 + 1 + 1 = 40          vs. the clean 16
```

**The file is 2.5× worse — a 150% increase in total squared miss — and both checks report perfect
health.** A brute-force sweep over every `Δ` with entries in `{−2,−1,0,1,2}` finds **30** non-zero
invisible corruption vectors, none supported on fewer than three cells (`verify_level2.py`,
Section 10).

Stated plainly: there are 5 residuals and 2 checks. The checks see 2 directions out of 5. **The
remaining 3 directions are invisible by construction, and no amount of care changes that** — you
would need more columns, or information from outside the file.

*Difficulty flag:* "3 directions out of 5" is first-year-university vector-space language
(`n` residuals minus `k` columns leaves `n − k` invisible dimensions). The player does not need it
to pass this level, and the three worked cases above prove the point without it. Say the sentence
anyway, and say it is graduate vocabulary for a fact they just verified by hand — they will meet
the same number again at Level 6 as **degrees of freedom**. Same quantity, same reason, different
clothes. Flag the call-back now so it lands later.

---

## 10. Boss-round pass conditions

Do not promote on the right stock alone. Promote when all four hold:

1. The player computes **both** `Σe` and `Σx·e` before guessing, and says why each should be zero.
2. They derive `δ = Σe` and `x_k = (Σx·e)/(Σe)` from the one-corrupted-cell model — not by trying
   stocks one at a time until one works. Trial-and-error reaching EMK is partial credit, and must
   be told so.
3. Under interrogation (*"your balance check passed, so the file's fine, yes?"*) they refuse the
   bait and produce the CHR case: the check is blind wherever the exposure is zero.
4. They can state what the checks cannot see, and are not upset about it.

**Failure protocol trigger.** If the player insists `Σe = 0` is a law of nature, stop the level. Go
back to the cold open, where `Σe = 2`, and rebuild from there. That is a Level 5 gap wearing a
Level 2 costume, and pushing forward will not fix it.

---

## 11. Ladder position after this level

| Concept | Target tier |
|---|---|
| residual / miss | 5 — rebuild on new data |
| `Σx·e = 0` as a turning-force condition | 4 — defend under attack |
| the nudge identity `SS(b+h) = SS(b) − 2hP + h²Q` | 4 (was 3 at Level 1) |
| proof by contradiction, both directions | 4 |
| balance as an integrity check, not a quality check | 4 |
| weighted balance `Σw·x·e = 0` and matching the audit to the fit | 3 — derive |
| invisible-corruption dimension count | 1 — recognise |

---

## 12. Back to BFRE — what this machinery does in the real model

Level 1 already tied the *estimator* to p.24 eq. (1.7), p.25's weighting paragraph and p.24
eq. (1.8). Do not repeat that. What follows is what the **balance condition** specifically buys,
and it is different material.

### The split in equation (1.7) is *defined* by the balance conditions

**p.24, equation (1.7):** `r = X f + u`, where *"`X f` is termed the common factor return and `u`
is the asset specific, or idiosyncratic, return."*

Nothing in that equation says how to divide a stock's return into the two parts. You could put
anything in `f` and dump the remainder in `u`, and the equation would still hold. **The balance
conditions are what pin it down:** `f` is the one choice for which `u` has zero turning force
against every column of `X`, one condition per factor. Every column is a plank; `u` is the weights
hanging on all of them; all balance simultaneously. The player has now built exactly one plank of
that structure by hand, and — via the boss round's market column — two.

### The second pass only makes sense because the first pass balanced

**p.26, equation (1.11):** `u = Σ_{j∈EInd} X_EInd,j f_EInd,j + Σ_{k∈ECty} X_ECty,k f_ECty,k + ε` —
the second pass regresses the **first-pass residuals** on Extended Industry and Extended Country
exposures.

This architecture is coherent only because `u` already has zero balance against every first-pass
column. The second pass cannot undo the first pass's work; it can only find structure in directions
the first pass never looked. The same shape appears at least four times in the paper:

| Where | First step leaves | Second step regresses those residuals on |
|---|---|---|
| p.7, eqs (1.1)–(1.2) | `u` from market + core country + Level-`n` industries | Level-`n+1` industries, to price the extra granularity |
| p.11, eqs (1.3)–(1.4) | `ε` from market + core country + core industry | one candidate substyle at a time (`N ≥ 200` of them) |
| p.26, eq (1.11) | `u` from the first pass | Extended Industry and Extended Country factors |
| p.52, eq (1.49) | `lê` from the beta regression (1.12), p.42 | one macro-economic factor's returns |

The notes flag the p.52 case in exactly this level's language: *"The macro betas are estimated on
the residuals of (1.12), not on raw returns — so they are orthogonal to whatever (1.12) already
explains."*

### The boss round's real-world twin: p.16

This is the sharpest tie-back and worth real time.

**p.16:** *"For each decile, a set of model residuals were regressed against 0/1 dummy variables
indicating decile membership."* The printed result: before a small-cap factor was added, deciles 9
and 10 showed explanatory power *"in excess of the 10% threshold used to determine whether styles
are eligible for inclusion in the model"*; after adding it, *"the proportion of t-statistics for
these deciles is no longer statistically significant."*

Ask the player why BlackRock had to **build a brand-new column of 0/1 dummies** to run that test.
The answer is Section 5 of this level: the balance conditions of the factors already in the model
are zero *by construction* and could never have revealed the missing small-cap effect. To find a
missing factor you must test the residual against a direction the fit has never seen.

And Section 9.7 is the same fact with the sign flipped: what the fitted columns cannot see, they
cannot see *at all*. A missing factor and an undetected corruption are the same geometric event.

*Numbers, with their provenance:* the notes give Figure 1.10's bar heights as deciles 9 and 10 at
**10.8%** and **21.1%** before the small-cap factor, falling to **2.1%** and **3.4%** after, against
a dashed 10% threshold. These are **measured off the scanned bar chart — the figure carries no
printed data labels** — and `notes/chunk_10-18.md` flags them as readings rather than printed
values. The *claim* they support (only deciles 9 and 10 breach the line before; neither does after)
is printed body text and is firm. Quote the claim; quote the numbers with the caveat attached.

### One contrast the player must not blur: guaranteed vs imposed

**p.26, equation (1.10):** `Σ_j ω_CInd,j · f_CInd,j = 0` and `Σ_k ω_CCty,k · f_CCty,k = 0` — *"The
restrictions force the average industry and country returns to be zero"*, footnote 15 defining the
average as square-root-of-market-cap weighted. (The second sum is printed in the source with index
`j` over a summand subscripted `k`; `notes/chunk_19-27.md` re-verified this at 6× and records it as
a typo in the original. It is written here as `Σ_k`, corrected.)

These *look* like balance conditions and are **the opposite kind of object**:

| | `Σ w·X·u = 0` (this level) | eq. (1.10) |
|---|---|---|
| where it comes from | forced by the arithmetic of minimising | chosen by the modeller |
| can it fail? | never — failure means a bug | it is imposed, so it holds by fiat |
| what it sums over | **assets** | **factors** |
| what it is about | residuals vs exposures | factor returns vs each other |
| could it have been otherwise? | no | yes — the paper says so |

The paper states the motive outright: *"for each asset, there exist three intercept terms — the
market factor, an industry factor, and a country factor. Every asset has unit exposure to these
three factors… This can be resolved by adding two linear restrictions."* And it is candid that the
choice is free: *"This identification simply represents a rotation of the factor returns. It does
not impact the efficacy of the risk model."*

Separating what least squares hands you free from what BFRE decided is the spine of Level 9. Level 2
is where the distinction first becomes visible. Plant it here.

### What the notes do NOT support

Searched all 65 transcribed pages in `notes/` for `least squares`, `normal equation`,
`first-order condition` and `minimis*` — **zero hits.** `orthogonal` returns exactly one hit, and it
is the transcriber's own commentary on p.52 (*"so they are orthogonal to whatever (1.12) already
explains"*), **not a sentence quoted from the paper**. (The only `first-order` matches are
"first-order autocorrelation" in the factor tables, an unrelated quantity.)

The paper states its regressions (1.1, 1.2, 1.3, 1.4, 1.9, 1.11, 1.12, 1.49), states the weighting
scheme, and states the imposed restrictions (1.10) — but **never writes the balance conditions and
never names the estimator.**

So: **no BFRE anchor was found in `notes/` for `Σ w·x·u = 0` as an equation.** It is unstated
machinery underneath every regression the paper runs. Say that to the player in exactly those
words. Level 1 already flagged the neighbouring gap — the estimator's closed form is never printed
either — and the two together make one Level 12 entry: a methodology document that spends a full
paragraph justifying its regression weights, but never once writes down what is being minimised or
what the minimisation forces to be true.

---

## Verification

```bash
python3 bfre-risk-desk/tools/verify_level2.py     # 206 exact-rational assertions, exits 0
```

The script recomputes every figure on this page from the raw `x`, `r`, `w` and residual vectors in
`fractions.Fraction`: the nudge identity over a grid of `(b, h)` pairs, the two-column nudge
identity over a grid of `(p, q)` pairs, the weighted and unweighted balances at both fits, all four
suspects with their required `δ`, every wrong method's numeric output, the near miss, and a
brute-force enumeration of the invisible corruption vectors. If any printed value ever disagrees
with this markdown, the markdown is wrong.
