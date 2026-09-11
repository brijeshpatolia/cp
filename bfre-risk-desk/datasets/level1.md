# Level 1 — The Dial

Every number below is recomputed in exact rational arithmetic by `tools/verify_level1.py`
(173 exact checks, standard library only). Nothing here is rounded by hand; every decimal shown
is the rounded display of an exact fraction that the verifier computes and checks.

**What the player must walk out able to do:** derive `b = Σxr / Σx²` from nothing, with no
calculus and no derivatives — only *"what happens to the total squared miss if I nudge b by a
small amount h"*.

---

## The story first (no mathematics)

> You are standing somewhere on the floor of a valley, in fog thick enough that you can see your
> own boots and nothing else. You cannot see the shape of the valley. You cannot see the bottom.
> The only thing you can do is take one step and feel whether you ended up higher or lower.
>
> That is enough. Here is the whole argument. **If a step in some direction takes you downhill,
> then you were not standing at the bottom.** So the bottom is the one place on the whole valley
> floor where *every* step, in *either* direction, takes you up. You do not need to see the valley
> to certify that you have found its lowest point. You only need to check the two steps.
>
> And there is a second thing your boots can tell you. Far from the bottom, the ground under you
> is tilted: a small step changes your height a lot, and the tilt tells you which way to go. Near
> the bottom the ground goes almost level — you have to take a big step before you feel any rise
> at all. The bottom is the place where the tilt has run out completely.

Map it, line by line:

| In the fog | On the desk |
|---|---|
| where you are standing | the setting `b` of the one dial |
| your altitude | the total squared miss `SS(b)` — Level 0's scorecard |
| taking a step of size `h` | nudging the dial: `b → b + h` |
| the tilt you feel underfoot | the **pull** `P(b)` — a number we are about to construct |
| the ground going level at the bottom | the pull hitting exactly zero |
| every step goes up | the certificate that the minimum is real, and unique |

One thing the fog story gets *better* than reality: our valley's cross-section is exactly a
parabola. Not approximately — exactly. So we will not have to grope. Two steps will tell us
everything.

(Callback to Level 0: if we had kept `Σ|e|` instead of `Σe²`, the valley floor would be a
**V with a kink**, not a bowl. At a kink the "tilt" jumps rather than passing through zero, and
this whole argument dies. That is a second, independent reason the loss is squared.)

---

## Part 1 — turning the dial

### The dataset (the one the player has already seen)

| Stock | Cheapness score `x` | Return `r` |
|---|---:|---:|
| AXL | −1.5 | −2.0% |
| BRN | −0.5 | −2.0% |
| CHR | 0.0 | +0.5% |
| DLT | +1.0 | +4.0% |
| EMK | +2.0 | +3.5% |

```
Σx  = 1        Σx² = 15/2 = 7.5        Σxr = 15        Σr = 4        Σr² = 73/2 = 36.5
```

The rule under test is `predicted return = b × x`, and the scorecard from Level 0 is

```
SS(b) = Σ(r − bx)²  =  Σr² − 2b·Σxr + b²·Σx²  =  73/2 − 30b + (15/2)b²
```

The player has **not** yet been told the answer is `b = 2` in any way they could reconstruct. They
were shown it. Level 1 is where they earn it.

### The one identity this whole game is built on

Take any setting `b`, and nudge it by any amount `h`. Then:

```
SS(b + h) − SS(b)  =  −2h · Σx(r − bx)  +  h² · Σx²
```

**This is not an approximation.** It is an exact algebraic identity, true for every `b` and every
`h`, and the player should derive it themselves in three lines — expand `(r − (b+h)x)²`, subtract
`(r − bx)²`, and collect. `verify_level1.py` checks it exactly on 96 `(b, h)` pairs of this
dataset and 60 more on the boss data; not one of them is off by a rational hair.

Two pieces, and they behave completely differently:

| Piece | Size | Sign | What it is |
|---|---|---|---|
| `−2h · Σx(r − bx)` | proportional to `h` | flips when `h` flips | the **reward** for stepping downhill |
| `h² · Σx²` | proportional to `h²` | always ≥ 0 | the **tax**, charged whichever way you step |

Name the first one's guts, because it is about to do all the work:

```
P(b) = Σ x·(r − bx) = Σxr − b·Σx²        "the pull"
```

Note what `r − bx` is: the leftover miss on each stock at this dial setting. So **`P(b)` is
`Σx·e`** — the misses, each weighted by that stock's own cheapness score. Hold onto that; it is
the entire content of Level 2.

For this dataset `P(b) = 15 − 7.5b`, so:

| `b` | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| `P(b)` | 15 | 7.5 | **0** | −7.5 |

### Turning the dial from b = 0

Start with the dial at zero — predict nothing for everybody. `SS(0) = Σr² = 36.5`. Now nudge:

```
SS(0 + h) − SS(0)  =  −30h + 7.5h²
```

| `h` | reward `−2h·P(0)` | tax `h²·Σx²` | net change | `SS(0+h)` |
|---:|---:|---:|---:|---:|
| 0.1 | −3.0000 | +0.0750 | **−2.9250** | 33.5750 |
| 0.5 | −15.0000 | +1.8750 | **−13.1250** | 23.3750 |
| 1 | −30.0000 | +7.5000 | **−22.5000** | 14.0000 |
| 2 | −60.0000 | +30.0000 | **−30.0000** | 6.5000 |
| 3 | −90.0000 | +67.5000 | **−22.5000** | 14.0000 |
| 4 | −120.0000 | +120.0000 | **0.0000** | 36.5000 |
| 5 | −150.0000 | +187.5000 | **+37.5000** | 74.0000 |

Read the last two columns as a race. The reward grows in a straight line; the tax grows like a
square. For small `h` the reward is miles ahead. At `h = 4` the tax has caught up exactly — that
is `h = 2P(0)/Σx² = 30/7.5 = 4` — and past there the tax wins and you are climbing again.

A beginner reads this table and says "so `b = 2`, that's where the net change is most negative."
**That reasoning earns zero bps.** They read it off a table. The table only exists because someone
already knew where to look. Make them do it without the table.

### Turning from b = 1: watch the two terms fight

```
SS(1 + h) − SS(1)  =  −15h + 7.5h²
```

| `h` | reward | tax | net change | `SS(1+h)` | reward ÷ tax |
|---:|---:|---:|---:|---:|---:|
| 0.001 | −0.0150000 | +0.0000075 | −0.0149925 | 13.9850075 | **2000** |
| 0.01 | −0.1500000 | +0.0007500 | −0.1492500 | 13.8507500 | **200** |
| 0.1 | −1.5000000 | +0.0750000 | −1.4250000 | 12.5750000 | **20** |
| 1 | −15.0000000 | +7.5000000 | −7.5000000 | 6.5000000 | 2 |
| 2 | −30.0000000 | +30.0000000 | **0.0000000** | 14.0000000 | 1 |
| 3 | −45.0000000 | +67.5000000 | +22.5000000 | 36.5000000 | 2/3 |

**This is the load-bearing column.** Halve `h` and the reward halves but the tax quarters. Divide
`h` by ten and the reward drops 10× while the tax drops 100×. The ratio 2 → 20 → 200 → 2000 has no
ceiling: *for small enough h, the tax is irrelevant and the sign of the whole change is the sign of
the reward alone.*

That sentence is the entire idea of a derivative, built out of arithmetic, with the word still
locked in a drawer.

Also note `h = 2` gives net change exactly zero: `SS(1) = SS(3) = 14`. The dial has two settings of
equal badness on either side of the good one. That symmetry is a free gift — and it will hand the
player a self-check in the boss round.

### Turning from b = 2: the reward is gone

`P(2) = 15 − 7.5(2) = 0`, so the reward term is **exactly zero for every `h`**, and:

```
SS(2 + h) − SS(2)  =  0 + 7.5h²
```

| `h` | reward | tax | net change | `SS(2+h)` |
|---:|---:|---:|---:|---:|
| +1 | 0.000000 | 7.500000 | **+7.500000** | 14.000000 |
| −1 | 0.000000 | 7.500000 | **+7.500000** | 14.000000 |
| +0.5 | 0.000000 | 1.875000 | **+1.875000** | 8.375000 |
| −0.5 | 0.000000 | 1.875000 | **+1.875000** | 8.375000 |
| +0.1 | 0.000000 | 0.075000 | **+0.075000** | 6.575000 |
| −0.1 | 0.000000 | 0.075000 | **+0.075000** | 6.575000 |
| +0.01 | 0.000000 | 0.000750 | **+0.000750** | 6.500750 |

Every entry in the reward column is `0`. Not small — **zero**, exactly, as a fraction. Every entry
in the net-change column is positive. Both directions go up. By the fog argument, we are at the
bottom, and we knew it without ever seeing the valley.

Note `SS(1.5) = SS(2.5) = 67/8 = 8.375`, which is the symmetry the player met in Level 0's table.
It was never a coincidence: `SS(b*+h)` and `SS(b*−h)` differ only through `h²`, which cannot tell
the two apart.

### The derivation (this is the level)

Now run it backwards, and the formula falls out with no table and no guessing.

**Step 1.** Suppose the dial sits at some `b` with `P(b) ≠ 0`. Choose `h` with the **same sign as
`P(b)`**, so the reward `−2h·P(b)` is negative. Then choose `|h|` small enough that the tax cannot
cover it:

```
|h| · Σx²  <  2|P(b)|        i.e.        |h|  <  2|P(b)| / Σx²
```

**Step 2.** With that `h`, the net change `−2h·P(b) + h²·Σx²` is strictly negative. `SS` went down.
So `b` was **not** the minimum. Checked exactly at nine different starting points:

| start `b` | `P(b)` | any \|h\| below | `h` used | `SS(b)` | `SS(b+h)` |
|---:|---:|---:|---:|---:|---:|
| 0 | +15.00 | 4.0 | +2.0 | 36.5000 | **6.5000** |
| 0.5 | +11.25 | 3.0 | +1.5 | 23.3750 | **6.5000** |
| 1 | +7.50 | 2.0 | +1.0 | 14.0000 | **6.5000** |
| 1.5 | +3.75 | 1.0 | +0.5 | 8.3750 | **6.5000** |
| 2.5 | −3.75 | 1.0 | −0.5 | 8.3750 | **6.5000** |
| 3 | −7.50 | 2.0 | −1.0 | 14.0000 | **6.5000** |
| 4 | −15.00 | 4.0 | −2.0 | 36.5000 | **6.5000** |
| −1 | +22.50 | 6.0 | +3.0 | 74.0000 | **6.5000** |
| −2 | +30.00 | 8.0 | +4.0 | 126.5000 | **6.5000** |

**Step 3.** Step 2 rules out every `b` with a non-zero pull. There is nothing left to be the
minimum except a `b` with `P(b) = 0`. So set the pull to zero and solve — one linear equation, no
calculus anywhere in sight:

```
Σxr − b·Σx² = 0
                    ⟹     b = Σxr / Σx²
15 − 7.5b = 0                            b = 15 / 7.5 = 2       exactly
```

**That is the level.** Everything after this is consequence.

**Bedrock check.** Where does the chain stop? At the *definition* of `SS` — "score a rule by the
total of its squared misses" — which Level 0 argued for and did not prove, because it cannot be
proved. It is a choice. Everything from here down is forced; that one thing up top is not.

### Why the h² term matters: uniqueness, and a bonus formula

Step 3 found *a* place where the pull vanishes. Is it the only one? Yes, and the tax term is the
proof. Put `b*` = the solution. Since `P(b*) = 0`, the identity collapses to one term:

```
SS(b) − SS(b*)  =  Σx² · (b − b*)²
```

Read it as a **penalty formula**: *being wrong about the dial by an amount costs you `Σx²` times
the square of how wrong you were.* Checked exactly:

| your `b` | `b − b*` | penalty `Σx²(b−b*)²` | `SS(b)` | `SS(b*) + penalty` |
|---:|---:|---:|---:|---:|
| 0 | −2.0000 | 30.0000 | 36.5000 | 36.5000 |
| 1 | −1.0000 | 7.5000 | 14.0000 | 14.0000 |
| 1.5 | −0.5000 | 1.8750 | 8.3750 | 8.3750 |
| **2** | 0.0000 | **0.0000** | **6.5000** | **6.5000** |
| 2.5 | +0.5000 | 1.8750 | 8.3750 | 8.3750 |
| 133/48 ≈ 2.7708 | +0.7708 | 4.4564 | 10.9564 | 10.9564 |
| 3 | +1.0000 | 7.5000 | 14.0000 | 14.0000 |
| 4 | +2.0000 | 30.0000 | 36.5000 | 36.5000 |
| −1 | −3.0000 | 67.5000 | 74.0000 | 74.0000 |

`Σx²` is a sum of squares and at least one `x` is non-zero, so `Σx² > 0` — here `15/2`. A strictly
positive number times a strictly positive square is strictly positive. **Every other `b` scores
strictly worse. The minimum is unique.** No calculus, no second derivatives, no hand-waving.

Two of those rows are Level 0's wrong methods, priced by the same formula:

- `Σr/Σx = 4` → penalty `7.5 × 2² = 30` → `SS = 36.5`. Exactly as bad as giving up and predicting
  zero for everyone, which is a genuinely funny result worth showing the player.
- `mean(r/x) = 133/48 ≈ 2.7708` → penalty `4.4564` → `SS = 10.9564`, i.e. `16829/9984` of the
  minimum — **68.56% worse** (rounded).

Bank the penalty formula. `Σx²` in the denominator of `b` and `Σx²` as the multiplier on your
error are the same `Σx²`, and at Level 6 that single fact turns into the number that says how far
`b` is to be trusted.

### Build-the-shape check (do this *before* revealing the formula)

Give the player only the units and the job. The whole check turns on giving `x` a **unit** and
refusing to drop it: write `C` for one unit of cheapness score and `%` for one percentage point of
return. Then:

- `x` is measured in `C`. `r` is measured in `%`.
- So the five sums the player has are: `Σx` in `C`, `Σx²` in `C²`, `Σxr` in `%·C`, `Σr` in `%`,
  `Σr²` in `%²`.
- The answer multiplies a cheapness score to give a return, so `b` must be in `%/C` —
  *percent per unit of cheapness*.
- `%/C = (%·C)/C²`. The only sum in `%·C` is `Σxr`; the only sum in `C²` is `Σx²`.

`Σxr/Σx²` is the only ratio of two sums with that shape. This kills two wrong answers before any
arithmetic happens: `Σr/Σx²` is `%/C²` and `Σxr/Σx` is plain `%` — see the shape-error rows in the
boss table.

Be honest with the player about what the check does **not** do. `Σr/Σx` is also `%/C`, so units
alone cannot kill it; it dies on the arithmetic instead (it is the worst non-shape method in the
boss table). And if `x` is treated as a bare pure number, `C` disappears, every candidate collapses
to `%`, and the check kills nothing at all. The unit on `x` is doing all the work — say so.

---

## Part 2 — the boss round

**Round type: PREDICT-THEN-REVEAL, then INTERROGATION.** The player commits to an order of
magnitude *with a reason*, out loud, before a calculator is allowed within reach. A correct guess
with a bad reason earns **nothing**.

### The data — same five names, one month later

| Stock | Cheapness score `x` | Return `r` |
|---|---:|---:|
| AXL | −2.0 | −2.5% |
| BRN | −1.0 | −1.0% |
| CHR | 0.0 | +0.6% |
| DLT | +1.5 | +3.0% |
| EMK | +2.5 | +4.2% |

CHR again has `x = 0` and again has a non-zero return. That is deliberate and it is not noise —
see below.

### Step 1 — commit, before the calculator

Ask: **is `b` about 0.015, 0.15, 1.5, 15, or 150 percent per unit of cheapness?** State the rung
*and the reason* before touching anything.

The reason that earns full bps:

```
biggest return − smallest return   =   +4.2% − (−2.5%)   =   6.7 percentage points
biggest x      − smallest x        =   +2.5  − (−2.0)    =   4.5 units
so the dial is roughly              6.7 / 4.5  =  67/45  ≈  1.4889   (rounded)
```

→ **the 1.5 rung.**

Reasons that do *not* earn full bps, and why:

- *"Returns are a few percent and scores are about 1, so `b` is a few."* Right rung, no mechanism.
  It never uses the fact that `r` and `x` move **together**; it would give the same answer if the
  returns were shuffled between the stocks.
- *"It was 2 last month."* Persistence is a real and defensible instinct — but it is a prior, not a
  reading of *this* data, and here it lands on the wrong rung's edge.
- Anything arriving after a calculator has been touched. Zero bps, no appeal.

What the rungs actually cost, for the interrogation:

| rung | `SS` at that rung | exact |
|---:|---:|---|
| 0.015 | 33.6230 | 2689843/80000 |
| 0.15 | 28.2538 | 22603/800 |
| **1.5** | **1.6250** | **13/8** |
| 15 | 2441.7500 | 9767/4 |
| 150 | 297484.2500 | 1189937/4 |

(decimals rounded). The right rung beats its neighbours by `22603/1300 = 17.387×` and `19534/13 = 1502.62×`
(rounded). Order
of magnitude is not a soft question — it is most of the answer.

### Step 2 — now the arithmetic, by hand

Two columns, five rows, no calculator needed:

| Stock | `x` | `r` | `x·r` | `x²` |
|---|---:|---:|---:|---:|
| AXL | −2.0 | −2.5 | +5.00 | 4.00 |
| BRN | −1.0 | −1.0 | +1.00 | 1.00 |
| CHR | 0.0 | +0.6 | 0.00 | 0.00 |
| DLT | +1.5 | +3.0 | +4.50 | 2.25 |
| EMK | +2.5 | +4.2 | +10.50 | 6.25 |
| | **Σx = 1** | **Σr = 4.3** | **Σxr = 21** | **Σx² = 13.5** |

```
b = Σxr / Σx² = 21 / 13.5 = 42/27 = 14/9 = 1.5555…   (1.5 recurring)
```

The guess was `67/45`. The truth is `70/45`. Over a common denominator they are three
forty-fifths apart:

```
gap = 14/9 − 67/45 = 1/15 = 0.0667      the eyeball was low by 3/70 = 4.286%   (rounded)
```

**That is the designed lesson of this boss round.** The rough size was readable straight off the
table by a 12th-standard student in ten seconds. The exact value is `14/9` — a repeating decimal
that no amount of squinting produces. Five stocks all had to vote, and the vote was weighted by
`x²`. If the player's guess landed within a few percent, say so and give the bps; if they claim
they "basically had it", show them the missing `3/45` and make them say which stocks it came from.

### Step 3 — the checks the player runs before submitting

**Check A — the pull is zero.** This is the same arithmetic backwards, and it catches division
slips instantly:

```
P(b) = Σxr − b·Σx² = 21 − (14/9)(27/2) = 21 − 21 = 0     ✓
```

**Check B — the residuals.**

| Stock | `x` | `r` | `b·x` | `e = r − b·x` | `e` (rounded) |
|---|---:|---:|---:|---:|---:|
| AXL | −2.0 | −2.5 | −28/9 | **+11/18** | 0.6111 |
| BRN | −1.0 | −1.0 | −14/9 | **+5/9** | 0.5556 |
| CHR | 0.0 | +0.6 | 0 | **+3/5** | 0.6000 |
| DLT | +1.5 | +3.0 | +7/3 | **+2/3** | 0.6667 |
| EMK | +2.5 | +4.2 | +35/9 | **+14/45** | 0.3111 |

```
Σe   = 247/90 = 2.7444     ← NOT zero — and every single residual is POSITIVE
Σx·e = 0                   ← zero. The pull has vanished. This is the fit.
Σe²  = 19/12 = 1.5833
```

**Every stock beat the model.** Not one is below the line. That looks broken and it is not: the
rule `r = b·x` is forced through the origin, so a shift that lifts *every* stock by the same amount
cannot be represented at all — there is no knob for "the whole market moved". The model has one
dial and the month needed two.

(Note for the game master, so this is not overstated at the table: it is **not** the case that
every stock went up this month — AXL returned `−2.5%` and BRN `−1.0%`. What is true is that every
stock came in *above what cheapness alone predicts for it*, which is the thing a second dial would
absorb.)

Do not fix this here. Two locked doors are visible through it:

- Level 5 adds a second dial that *can* say "everything rose", and the day it appears `Σe` is
  forced to zero as well. `Σe ≠ 0` here is not a bug; it is the **fingerprint** of the missing
  dial. Do not call it the missing dial's *size*: fitting a second dial re-fits the first one too,
  and the two-dial answer on this data is `a = 39/70 = 0.5571` with `b = 53/35 = 1.5143`, whereas
  `Σe/5 = 247/450 = 0.5489`. Close, deliberately not equal — and the gap is Level 5's opening
  question, so do not spend it here.
- BFRE's answer is a **market factor** to which every equity has unit exposure, p.4 — see the
  tie-back.

**Check C — symmetry.** `SS(b* + h) = SS(b* − h)`, so the player can verify their answer by
finding two settings with equal scores and halving:

```
14/9 − 1/2 = 19/18 = 1.0556        14/9 + 1/2 = 37/18 = 2.0556
SS(19/18) = SS(37/18) = 119/24 = 4.9583        (equal, so the minimum is midway)
```

**Check D — the scorecard, both ways.**

```
SS(b) = Σr² − 2b·Σxr + b²·Σx² = 137/4 − 42b + (27/2)b²  = 34.25 − 42b + 13.5b²
   SS(0)    = 137/4 = 34.2500      ( = Σr², "give up and predict zero" )
   SS(1)    = 23/4  = 5.7500
   SS(14/9) = 19/12 = 1.5833       ( = Σe² above, so the two routes agree )
   SS(2)    = 17/4  = 4.2500
   SS(3)    = 119/4 = 29.7500
```

And the nudge identity, re-run on this dataset with the reward term dead:

| `h` | reward | tax `13.5h²` | `SS(14/9 + h)` | rounded |
|---:|---:|---:|---:|---:|
| +0.5 | 0 | 27/8 | 119/24 | 4.95833 |
| −0.5 | 0 | 27/8 | 119/24 | 4.95833 |
| +0.1 | 0 | 27/200 | 1031/600 | 1.71833 |
| −0.1 | 0 | 27/200 | 1031/600 | 1.71833 |
| +0.01 | 0 | 27/20000 | 95081/60000 | 1.58468 |

### The wrong methods, and exactly what each one returns

Penalty column is `Σx²·(b − 14/9)² = 13.5(b − 14/9)²`; the last column is `SS(b) ÷ SS(14/9)`.

| Method | `b` exact | `b` (rounded) | `SS(b)` | penalty | × worse |
|---|---:|---:|---:|---:|---:|
| **the nudge answer `Σxr/Σx²`** | **14/9** | **1.5556** | **1.5833** | **0** | **1.000** |
| "total return ÷ total score" `Σr/Σx` | 43/10 | 4.3000 | 103.2650 | 101.6817 | 65.220 |
| average the per-stock slopes `mean(r/x)` | 593/400 | 1.4825 | 1.6554 | 0.0721 | 1.046 |
| median of the per-stock slopes | 293/200 | 1.4650 | 1.6940 | 0.1107 | 1.070 |
| line through the two extreme stocks | 67/45 | 1.4889 | 1.6433 | 0.0600 | 1.038 |
| "just use the biggest name" `r_EMK/x_EMK` | 42/25 | 1.6800 | 1.7924 | 0.2091 | 1.132 |
| shape error `Σr/Σx²` | 43/135 | 0.3185 | 22.2419 | 20.6585 | 14.047 |
| shape error `Σxr/Σx` | 21 | 21.0000 | 5105.7500 | 5104.1667 | 3224.684 |

Notes the game master must actually make:

- **`Σr/Σx = 4.3` is a fluke of a small `Σx`.** Here `Σx = 1`, so this method returns literally
  `Σr = 43/10`, and scores `61959/950 = 65.220×` worse than the answer. Ask what it would return if `Σx` had
  been `0.1`, or `0`. It is not merely inaccurate, it is unstable — and Level 5 explains why
  (centring makes `Σx = 0` on purpose, and this method then divides by zero forever).
- **`mean(r/x) = 1.4825` is the dangerous one.** It lands 4.696% from the truth and only 4.55% worse
  on the scorecard (both rounded). It is *nearly right, by luck*. The per-stock slopes are
  `1.2500, 1.0000, 2.0000, 1.6800` — they disagree by a factor of two, so averaging them is a
  choice, not a reading. And the choice is a bad one: it gives BRN, whose score is `−1.0`, the
  same vote as EMK, whose score is `+2.5`. The nudge answer gives EMK `6.25/1 = 6.25` times the
  vote, because vote weight is `x²`. Ask the player to explain *why* `x²` and not `|x|`; if they
  cannot, the right answer is worth zero bps under the house rule.
- **The two shape errors are already dead before arithmetic.** `Σr/Σx²` is percent over cheapness
  *squared* — one power of cheapness too many — and it returns `0.3185`, on the wrong rung.
  `Σxr/Σx` is plain percent, with no "per unit of cheapness" left in it at all, and returns `21`,
  two rungs out. The build-the-shape check in Part 1 catches both without computing anything. It
  does **not** catch `Σr/Σx`: that one has the right units and survives, and it is the worst
  of the six methods that do survive.
- **The median row is a Level 0 over-learn.** A player who took "squares are sensitive to
  outliers" as "so use the robust thing" reaches for the median of the slopes and scores 7% worse.
  Level 0's point was that a risk model *wants* that sensitivity. Charge bps for the inversion.

### The CHR question (the one a sharp player asks)

*"CHR has `x = 0`. No dial setting can ever predict it. Should I drop it?"*

Make them predict first. Then show both halves:

| | five stocks | four stocks (CHR dropped) |
|---|---:|---:|
| `Σxr` | 21 | **21** |
| `Σx²` | 13.5 | **13.5** |
| `b` | 14/9 = 1.5556 | **14/9 = 1.5556 — identical** |
| `Σr²` | 137/4 = 34.2500 | 3389/100 = 33.8900 |
| `Σe²` | 19/12 = 1.5833 | 367/300 = 1.2233 |

The dial **does not move by a hair**, because CHR contributed `0 × 0.6 = 0` to `Σxr` and
`0² = 0` to `Σx²`. It was never voting. But the reported fit quality moves a lot: `Σe²` falls by
exactly `0.36`, which is `0.6²` — CHR's entire return was also its entire miss, so its entire
return leaves the scorecard with it.

So dropping it changes nothing about the answer and flatters the diagnostic. That is the shape of
a real research fraud, and it is worth naming as such. It is also the cleanest possible statement
of what the model is going to call **specific return** later: a move no common characteristic can
reach, invisible to the factor estimate and fully present in the risk.

---

## Overtime — the version BFRE actually runs

The dial the player just built weights every stock equally. **BFRE does not.** From p.25: *"Assets
are weighted in the regression using square-root of market capitalisation."*

The nudge argument does not care. Score with weights `w` attached:

```
SS_w(b) = Σ w(r − bx)²
SS_w(b + h) − SS_w(b) = −2h·Σ w·x·(r − bx) + h²·Σ w·x²
```

Same two pieces, same argument, same conclusion — set the pull to zero:

```
b_w = Σ w·x·r / Σ w·x²
```

The unweighted formula is the special case `w = 1` for everybody. Suppose EMK is a mega-cap, 16×
the market capitalisation of its four peers, so its square-root-of-cap weight is `√16 = 4`:

```
w        = 1, 1, 1, 1, 4
Σ w·x·r  = 5 + 1 + 0 + 4.5 + 4(10.5) = 105/2 = 52.5
Σ w·x²   = 4 + 1 + 0 + 2.25 + 4(6.25) = 129/4 = 32.25
b_w      = (105/2)/(129/4) = 70/43 = 1.62791    (rounded)
```

Compare: unweighted `14/9 = 1.55556`, EMK's own slope `42/25 = 1.6800`. Up-weighting EMK dragged
the dial **toward EMK's own slope**, and it had to — that is what a weight *is*.

Weighted residuals `65/86, 27/43, 3/5, 24/43, 28/215`, and the balance that now holds is the
weighted one:

```
Σ w·x·e = 0            ← the weighted fit forces this
Σ   x·e = −42/43 = −0.9767     ← the UNWEIGHTED balance is now broken
```

Each dial wins on its own scorecard and loses on the other, exactly as it must:

| | `SS_w` (weighted) | `SS` (unweighted) |
|---|---:|---:|
| at `b_w = 70/43` | **7331/4300 = 1.70488** | 12233/7396 = 1.65400 |
| at `b = 14/9` | 5059/2700 = 1.87370 | **19/12 = 1.58333** |

and the penalty formula survives the generalisation intact:
`SS_w(b) − SS_w(b_w) = Σw·x² · (b − b_w)² = 196/1161 = 0.168820`.

There is no new idea here. There is one more symbol in every sum. That is the honest size of the
step from the classroom version to the production version, and the player should be told so.

---

## Difficulty, honestly

**Nothing in this level is graduate-level.** Every step is 12th-standard algebra: expand a square,
collect terms, solve a linear equation. If it felt hard, the framing was bad, not the player.

Four honest caveats the player is owed:

1. **The identity is exact, and that is a gift specific to squares.** `SS(b)` is a polynomial of
   degree exactly 2 in `b`, so the split into an `h` piece and an `h²` piece is complete — there is
   no `h³`, no remainder, nothing swept under a rug. This is precisely why Level 1 needs no
   calculus. For a smooth loss that is not a square (the outlier-down-weighting "robust methods"
   BFRE mentions on p.27 for cleansing specific returns) the same split is only an *approximation*
   valid for small `h`, and making that rigorous requires limits. For the absolute-value loss of
   Level 0 it is worse than that: at a kink there is no single `h`-coefficient at all — the reward
   term has one value for `h > 0` and another for `h < 0`, which is exactly why the argument on
   this page dies there. Say both of these plainly rather than letting the player think calculus
   is never needed.
2. **The player has just built a derivative and has not been told.** "For small enough `h`, the
   sign of the change is the sign of the `h`-coefficient" is the definition. The name gets unlocked
   only if they ask. Do not volunteer it as if it explained something.
3. **One column is easy; the difficulty is in the next three levels, and it is real.** With two
   columns the same argument produces one pull-equals-zero equation per column, which is Level 3's
   2×2 system. Level 4 then asks what happens when two columns nearly duplicate each other, and
   *that* — multicollinearity, and the Frisch–Waugh reading of a coefficient — is genuinely
   graduate-level material. Warn the player at the start of Level 3 so they calibrate.
4. **Production scale changes nothing conceptual and everything practical.** BFRE's first-pass
   regression (p.25, eq. 1.9) runs on the whole estimation universe against market, style,
   core-industry and core-country columns simultaneously — thousands of assets: the NAMR industry
   schema on p.57 lists `# Assets` industry by industry, and those printed rows total **2,193**
   (counted from the rows; the page prints no total) — with weights, plus two linear restrictions to make the
   answer unique at all (p.26, eq. 1.10). The idea in that machine is the one on this page. The
   bookkeeping is not.

---

## Jargon unlocked at the end of this level

Locked until now; hand them over only once the mechanism above is built, and make the player use
each in a new sentence of their own (round type F).

| Plain thing they built | The name |
|---|---|
| the cheapness score column `x` | **exposure** (equivalently, **loading**) |
| the dial setting `b` | **factor return** |
| `b·x`, the number the rule predicts | **fitted value** |
| the rule "pick `b` to minimise `Σe²`" | **least squares** (weighted least squares, with `w`) |
| `b = Σxr/Σx²` | the **least-squares estimator** |
| doing this across stocks at one date | **cross-sectional** — full force at Level 7 |

**Still locked.** Do not use these yet: *normal equation*, *orthogonal*, *design matrix*,
*degrees of freedom*, *standard error*, *R²*, *heteroskedasticity*. (The last appears verbatim
inside the p.25 quotation below; quote it, flag it as a word they will build at Level 9, and move
on without defining it.)

---

## What this level does inside BFRE

**The dial is `f`.** BFRE p.24, equation **(1.7)**, is the whole model in five symbols:

```
r = X f + u
```

with `r` = asset returns in excess of the local risk-free rate, `X` = factor exposures built from
asset characteristics, `f` = the return to each factor, `u` = asset specific return. Level 1 built
the one-column case of exactly this: `x` is a single column of `X`, `b` is a single entry of `f`,
and `e` is `u`. The page's own words: *"`X f` is termed the common factor return and `u` is the
asset specific, or idiosyncratic, return."*

**The operation is BFRE's estimation step.** p.24: the estimation phase is *"a series of
cross-sectional regressions of asset returns against asset factor exposures, which provides
estimates of factor returns and asset specific returns."* Same page: those regressions run
**daily** for country and regional models and **weekly** for the World model. So the arithmetic the
player just did by hand — five stocks, two columns of products, one division — is the arithmetic
BlackRock runs every business day, at scale.

**The weights are on p.25**, with the paper's own justification, quoted in full because the game
forbids paraphrasing a methodological choice:

> *"Assets are weighted in the regression using square-root of market capitalisation. This provides
> a good compromise between a weighting scheme that places equal weight on all assets, and one that
> is weighted by market capitalisation. The former can place too much emphasis on smaller assets in
> the regression and can lead to a poor fit for mega-cap and large-cap securities… More
> technically, square-root of market capitalisation adjusts for heteroskedasticity based on the
> observation that higher residual (specific) risk is typically correlated with smaller market
> capitalisation assets."*

That is the `w` of the Overtime section, and footnote 14 on the same page concedes the alternative:
*"Other regression weighting schemes exist which explicitly use the reciprocal of each asset's
residual (specific) variance, however, in practice these provide similar results to using
square-root of market capitalisation weights."*

**The real first pass is p.25, equation (1.9)** — the multi-column version, market plus style plus
core industry plus core country:

```
r = X_Mkt·f_Mkt + Σ_{i∈Sty} X_Sty,i·f_Sty,i + Σ_{j∈CInd} X_CInd,j·f_CInd,j
                + Σ_{k∈CCty} X_CCty,k·f_CCty,k + u
```

Two structural facts from p.26 that this level's dataset already gestures at:

- Because every asset has unit exposure to a market factor, an industry factor **and** a country
  factor, equation (1.9) has *three intercept terms* and is **not uniquely identified** — *"there
  are an infinite number of possible solutions."* BFRE fixes it with two linear restrictions,
  equation **(1.10)**, forcing the (square-root-of-cap weighted) average industry and country
  returns to zero. Contrast this with Level 1, where uniqueness came free from `Σx² > 0`. Losing
  uniqueness is the price of extra columns, and Level 4 is where the player pays it.
- The residuals `u` from (1.9) are not thrown away: p.26, equation **(1.11)**, regresses them again
  on extended-industry and extended-country exposures. Level 0's `Σe` and this level's `e` column
  are the input to a second regression in the real model.

**The month where every residual was positive is BFRE's market factor.** p.4: all BFRE models are
specified with a market factor, *"all equity assets have a unit exposure"* to it, and its factor
return is *"the cross-sectional average return across all assets in the model estimation"*
(footnote 2: *"Average return based on regression weights, i.e. square-root of market
capitalisation"*). Our boss month had every stock beating a cheapness-only rule because the market
rose and there was no column to say so. BFRE puts that column in first.

**The cheapness score is BFRE's value factor.** p.19 defines value by standard valuation ratios —
**book-to-price, sales-to-price and cash-flow-to-price** — and reports the NAMR value factor with a
Sharpe ratio of 1.43 and a correlation of 0.45 with Fama–French HML. When Level 7 strings the
player's monthly `b` values into a series, that series *accumulated* is what Figure 1.14 plots —
the caption is "cumulative performance of value in the NAMR model, Mar 1996 – Dec 2013" (figure
referenced on p.19, printed on p.20). The `b` values themselves are the increments of that curve,
not the curve.

**Where the `f` goes next.** p.24, equation **(1.8)**: `Σ = X F Xᵀ + Δ`. The `b` estimated here,
repeated across days, becomes a row of the factor covariance matrix `F` (Level 8); the `e` column
becomes the specific risk matrix `Δ` (Level 9); and the assembly is Level 10.

### What the notes do **not** support

The transcribed pages **never print the least-squares estimator itself**. There is no
`b = Σwxr/Σwx²` in the paper, no normal equation, no `(XᵀWX)⁻¹XᵀWr`. The paper says *"regression"*,
names the weighting scheme (p.25), states the identifying restrictions (p.26, eq. 1.10), and
appeals to precedent — p.24: *"The approach taken for BFRE is similar to that used in the
fundamental factor risk model literature"*, footnote 13 citing Rudd and Clasing [24], Grinold and
Kahn [25], Connor et al. [17].

So: **the formula on this page is not quoted from BFRE, it is reconstructed.** It is the standard
estimator the paper's language implies and the one its weighting discussion only makes sense
under — but the player should know that the derivation they just did fills a gap the source leaves
open rather than reproducing a printed equation. **No anchor was found in `notes/` for the
estimator's closed form.** That gap is itself Level 12 material: a methodology document that
specifies the regression weights to two clauses of justification but never writes down what is
being minimised.

---

## Verify

```bash
python3 bfre-risk-desk/tools/verify_level1.py     # 173 exact-rational checks, exits 0
```
