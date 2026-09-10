#!/usr/bin/env python3
"""
verify_level2.py -- recomputes EVERY number printed in datasets/level2.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
Run:  python3 tools/verify_level2.py
Exits 0 if every internal consistency assertion holds.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from itertools import combinations, product
import sys

# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def frac(*a):
    return [F(v) for v in a]

def S(v):
    """exact display: integers as integers, else a/b; tuples/lists as [a, b, ...]"""
    if isinstance(v, (tuple, list)):
        return "[" + ", ".join(S(t) for t in v) + "]"
    return str(v)

def row(v):
    return "[" + ", ".join(S(t) for t in v) + "]"

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)

CHECKS = [0]

def check(label, got, want):
    CHECKS[0] += 1
    ok = (got == want)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: {S(got)}"
          + ("" if ok else f"   EXPECTED {S(want)}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': got {got}, expected {want}")

# ============================================================================
# SECTION 1 -- the cold-open dataset, carried over from Level 0
# ============================================================================
head("SECTION 1  The cold-open dataset (Level 0 carry-over)")

names0 = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x0 = frac('-3/2', '-1/2', '0', '1', '2')
r0 = frac('-2', '-2', '1/2', '4', '7/2')

Sx0   = sum(x0)
Q0    = dot(x0, x0)          # sum x^2
Sxr0  = dot(x0, r0)          # sum x*r
Sr0   = sum(r0)
Srr0  = dot(r0, r0)          # sum r^2
b0    = Sxr0 / Q0

print("   x =", row(x0))
print("   r =", row(r0))
check("sum x",   Sx0,  F(1))
check("sum x^2 (call it Q)", Q0, F('15/2'))
check("sum x*r", Sxr0, F(15))
check("sum r",   Sr0,  F(4))
check("sum r^2", Srr0, F('73/2'))
check("b = sum x*r / sum x^2", b0, F(2))
print(f"   Q = {S(Q0)} = {float(Q0)}   sum r^2 = {S(Srr0)} = {float(Srr0)} (rounded display)")

def resid(b, x=x0, r=r0):
    return [ri - b * xi for xi, ri in zip(x, r)]

e_at2 = resid(F(2))
check("residuals at b=2 -> e", tuple(e_at2), tuple(frac('1', '-1', '1/2', '2', '-1/2')))
check("sum e   at b=2  (= sum r - b*sum x = 4 - 2)", sum(e_at2), F(2))
check("sum x*e at b=2 (the balance)", dot(x0, e_at2), F(0))
check("sum e^2 at b=2", dot(e_at2, e_at2), F('13/2'))

# fitted values are orthogonal to the residual; raw returns are NOT
rhat0 = [b0 * xi for xi in x0]
check("fitted rhat = 2x", tuple(rhat0), tuple(frac('-3', '-1', '0', '2', '4')))
check("sum rhat*e  (must be 0)", dot(rhat0, e_at2), F(0))
check("sum r*e     (equals sum e^2, NOT 0)", dot(r0, e_at2), F('13/2'))

# ============================================================================
# SECTION 2 -- the balance as a function of the dial, and the nudge identity
# ============================================================================
head("SECTION 2  P(b) = sum x*e  and the nudge identity (Level 1 carry-over)")

print("   P(b) = sum x*(r - b x) = sum x*r - b * sum x^2 = 15 - (15/2) b"
      "   [Level 1 calls P(b) 'the pull']")
for bb in [F(0), F(1), F('3/2'), F(2), F('5/2'), F(3), F(4)]:
    e = resid(bb)
    lhs = dot(x0, e)
    rhs = Sxr0 - bb * Q0
    check(f"P({S(bb)}) direct == 15 - (15/2)*{S(bb)}", lhs, rhs)

def SS(b, x=x0, r=r0):
    e = resid(b, x, r)
    return dot(e, e)

print()
print("   SS(b) = sum r^2 - 2b sum x*r + b^2 sum x^2 = 73/2 - 30 b + (15/2) b^2")
for bb in [F(0), F(1), F('3/2'), F(2), F('5/2'), F(3), F(4)]:
    poly = Srr0 - 2 * bb * Sxr0 + bb * bb * Q0
    check(f"SS({S(bb)}) direct == polynomial", SS(bb), poly)

print()
print("   NUDGE IDENTITY (Level 1's):  SS(b+h) = SS(b) - 2 h P(b) + h^2 Q")
for bb, dd in product([F(0), F(1), F(2), F('5/2')],
                      [F('-1'), F('-1/2'), F(0), F('1/2'), F(1), F(2), F(3)]):
    B = dot(x0, resid(bb))
    pred = SS(bb) - 2 * dd * B + dd * dd * Q0
    check(f"SS({S(bb)}+{S(dd)}) == SS({S(bb)}) - 2*{S(dd)}*P + {S(dd)}^2*Q", SS(bb + dd), pred)

# ============================================================================
# SECTION 3 -- the nudge table printed in the markdown (starting from b = 1)
# ============================================================================
head("SECTION 3  The nudge table: start at the WRONG dial b = 1")

b_bad = F(1)
e_bad = resid(b_bad)
B_bad = dot(x0, e_bad)
check("residuals at b=1", tuple(e_bad), tuple(frac('-1/2', '-3/2', '1/2', '3', '3/2')))
check("sum e   at b=1  (= sum r - b*sum x = 4 - 1)", sum(e_bad), F(3))
check("P(1) = sum x*e at b=1", B_bad, F('15/2'))
check("SS(1)", SS(b_bad), F(14))

print()
print("   h      b=1+h    Delta SS = (15/2)(h^2 - 2h)     SS(1+h)")
for dd in [F(-1), F(0), F('1/2'), F(1), F('3/2'), F(2), F(3)]:
    dSS = -2 * dd * B_bad + dd * dd * Q0
    closed = Q0 * (dd * dd - 2 * dd)
    check(f"  Delta SS at h={S(dd)} == (15/2)(h^2-2h)", dSS, closed)
    check(f"  SS(1+{S(dd)}) == SS(1) + Delta", SS(b_bad + dd), SS(b_bad) + dSS)

print()
best_d = B_bad / Q0
check("best single nudge h* = P/Q", best_d, F(1))
check("b + h* lands on the least-squares b", b_bad + best_d, b0)
check("drop achieved = P^2/Q", SS(b_bad) - SS(b_bad + best_d), B_bad * B_bad / Q0)
check("   ... numerically", B_bad * B_bad / Q0, F('15/2'))
print("   helping band: Delta SS < 0  <=>  0 < h < 2P/Q = 2, i.e. b in (1, 3)")
check("endpoint h=2 gives Delta SS exactly 0", -2 * F(2) * B_bad + F(4) * Q0, F(0))
check("SS(3) == SS(1)", SS(F(3)), SS(F(1)))

print()
print("   At the fit (b=2, P=0) every nudge HURTS: SS(2+h) = 13/2 + (15/2) h^2")
for dd in [F('-1'), F('-1/2'), F('1/2'), F(1)]:
    check(f"  SS(2+{S(dd)}) == 13/2 + (15/2)*{S(dd)}^2",
          SS(F(2) + dd), F('13/2') + Q0 * dd * dd)
check("SS(3/2) == SS(5/2) == 67/8", SS(F('3/2')), F('67/8'))
check("   and 67/8 as a decimal is 8.375 (exact)", F('67/8'), F(8375, 1000))

# ============================================================================
# SECTION 4 -- Level 0 callback: balance holds even for a catastrophic model
# ============================================================================
head("SECTION 4  Balance is NOT a quality metric (Level 0 desks A and B)")

xd = frac('-2', '-1', '1', '2')
deskA = frac('1/2', '-1/2', '-1/2', '1/2')
deskB = frac('6', '-6', '-6', '6')
for nm, ed in [("Desk A (tight)", deskA), ("Desk B (blown out)", deskB)]:
    print(f"   {nm}: e = {row(ed)}")
    check(f"  {nm} sum x*e", dot(xd, ed), F(0))
    print(f"          sum e^2 = {S(dot(ed, ed))}")
check("Desk A sum e^2", dot(deskA, deskA), F(1))
check("Desk B sum e^2", dot(deskB, deskB), F(144))
check("Desk B is this many times worse", dot(deskB, deskB) / dot(deskA, deskA), F(144))

# ============================================================================
# SECTION 4B -- the WEIGHTED balance (the version BFRE actually runs, p.25)
# ============================================================================
head("SECTION 4B  Weighted balance: sum w*x*e = 0, on the cold-open data")

w = frac('11', '1', '1', '1', '1')      # e.g. sqrt(market cap): one mega-cap, four minnows
check("sum w", sum(w), F(15))
wx2 = sum(wi * xi * xi for wi, xi in zip(w, x0))
wxr = sum(wi * xi * ri for wi, xi, ri in zip(w, x0, r0))
check("sum w*x^2", wx2, F(30))
check("sum w*x*r", wxr, F(45))
b_w = wxr / wx2
check("b_w = sum w*x*r / sum w*x^2 = 45/30", b_w, F('3/2'))

e_w = resid(b_w)
check("residuals at b_w = 3/2", tuple(e_w), tuple(frac('1/4', '-5/4', '1/2', '5/2', '1/2')))
check("  sum w*x*e at b_w  -- the WEIGHTED see-saw balances",
      sum(wi * xi * ei for wi, xi, ei in zip(w, x0, e_w)), F(0))
check("  sum x*e   at b_w  -- the UNWEIGHTED one does NOT",
      dot(x0, e_w), F('15/4'))
check("  sum w*x*e at b = 2 -- and vice versa",
      sum(wi * xi * ei for wi, xi, ei in zip(w, x0, e_at2)), F(-15))
check("  sum x*e   at b = 2", dot(x0, e_at2), F(0))
print("   Each fit balances its OWN see-saw and nobody else's. Weights are part of")
print("   the definition of the answer, not a cosmetic afterthought.")

# ============================================================================
# SECTION 5 -- BOSS ROUND: the clean month-2 file
# ============================================================================
head("SECTION 5  BOSS ROUND -- the clean file")

names = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x = frac('-2', '-1', '0', '1', '2')          # cheapness column
m = frac('1', '1', '1', '1', '1')            # market column: unit exposure for all
e_clean = frac('1', '-3', '2', '1', '-1')    # residuals, designed first
a_true, b_true = F('1/2'), F(2)
r = [a_true * mi + b_true * xi + ei for mi, xi, ei in zip(m, x, e_clean)]

n = len(x)
check("n assets", F(n), F(5))
check("sum m (= n)", sum(m), F(5))
check("sum x", sum(x), F(0))
check("sum x^2 (call it Q)", dot(x, x), F(10))
check("sum m*x (the two columns do not interfere)", dot(m, x), F(0))

print("   x =", row(x))
print("   e_clean =", row(e_clean), "  <- chosen first, so every other number is exact")
print("   r = (1/2)*1 + 2*x + e =", row(r))
check("returns r", tuple(r), tuple(frac('-5/2', '-9/2', '5/2', '7/2', '7/2')))
check("sum r", sum(r), F('5/2'))
check("rbar = sum r / n", sum(r) / n, F('1/2'))
check("sum x*r", dot(x, r), F(20))
check("b = sum x*r / sum x^2 = 20/10", dot(x, r) / dot(x, x), b_true)
check("a = rbar (valid ONLY because sum x = 0)", sum(r) / n, a_true)

rhat = [a_true * mi + b_true * xi for mi, xi in zip(m, x)]
check("fitted rhat", tuple(rhat), tuple(frac('-7/2', '-3/2', '1/2', '5/2', '9/2')))
check("e = r - rhat reproduces e_clean",
      tuple(ri - hi for ri, hi in zip(r, rhat)), tuple(e_clean))

check("CHECK 1: sum m*e = sum e", dot(m, e_clean), F(0))
check("CHECK 2: sum x*e", dot(x, e_clean), F(0))
check("sum e^2", dot(e_clean, e_clean), F(16))
check("sum r^2", dot(r, r), F('229/4'))
check("sum rhat^2", dot(rhat, rhat), F('165/4'))
check("Pythagoras: sum rhat^2 + sum e^2 == sum r^2",
      dot(rhat, rhat) + dot(e_clean, e_clean), dot(r, r))
print(f"   decimals (rounded display): sum r^2 = {float(dot(r,r))}, "
      f"sum rhat^2 = {float(dot(rhat,rhat))}")

# two-column nudge identity: SS(a+p, b+q) = SS - 2p*sum(e) - 2q*sum(x e)
#                                            + p^2 n + 2pq sum(x) + q^2 sum(x^2)
def SS2(aa, bb):
    return sum((ri - aa * mi - bb * xi) ** 2 for mi, xi, ri in zip(m, x, r))

print()
print("   TWO-COLUMN NUDGE IDENTITY (verified over a grid):")
print("   SS(a+p, b+q) = SS(a,b) - 2p*(sum e) - 2q*(sum x e) + p^2 n + 2pq(sum x) + q^2 Q")
grid = [F(-1), F('-1/2'), F(0), F('1/2'), F(1), F(2)]
for p, q in product(grid, grid):
    pred = (SS2(a_true, b_true)
            - 2 * p * dot(m, e_clean) - 2 * q * dot(x, e_clean)
            + p * p * n + 2 * p * q * sum(x) + q * q * dot(x, x))
    check(f"  SS(1/2+{S(p)}, 2+{S(q)})", SS2(a_true + p, b_true + q), pred)
print("   Since sum e = 0 and sum x*e = 0, every term left is >= 0: the fit is the minimum.")

# ============================================================================
# SECTION 6 -- BOSS ROUND: the corrupted file
# ============================================================================
head("SECTION 6  BOSS ROUND -- one cell corrupted")

CULPRIT = 4          # EMK
DELTA = F(1)         # e_EMK: -1 -> 0
e_bad_file = list(e_clean)
e_bad_file[CULPRIT] = e_clean[CULPRIT] + DELTA

print("   received e =", row(e_bad_file))
check("received e", tuple(e_bad_file), tuple(frac('1', '-3', '2', '1', '0')))

S_obs = dot(m, e_bad_file)
B_obs = dot(x, e_bad_file)
check("CHECK 1 fails: sum e   (should be 0)", S_obs, F(1))
check("CHECK 2 fails: sum x*e (should be 0)", B_obs, F(2))
print("   per-asset turning forces x_i*e_i =",
      row([xi * ei for xi, ei in zip(x, e_bad_file)]))
check("turning forces", tuple(xi * ei for xi, ei in zip(x, e_bad_file)),
      tuple(frac('-2', '3', '0', '1', '0')))

print()
print("   DEDUCTION: e_received = e_true + delta at cell k, so")
print("     sum e   = 0 + delta        -> delta   = sum e")
print("     sum x*e = 0 + x_k * delta  -> x_k*delta = sum x*e")
check("  delta = sum e", S_obs, DELTA)
check("  x_k = (sum x*e)/(sum e) = 2/1", B_obs / S_obs, x[CULPRIT])
matches = [names[i] for i in range(n) if x[i] == B_obs / S_obs]
print(f"   assets with x = {S(B_obs / S_obs)}: {matches}")
check("  exactly one asset matches", F(len(matches)), F(1))
print(f"   CULPRIT = {names[CULPRIT]}")
check("  repaired value = received - delta", e_bad_file[CULPRIT] - DELTA, e_clean[CULPRIT])
repaired = list(e_bad_file); repaired[CULPRIT] -= DELTA
check("  repaired vector sum e",   dot(m, repaired), F(0))
check("  repaired vector sum x*e", dot(x, repaired), F(0))
check("  repaired vector == clean", tuple(repaired), tuple(e_clean))

# the trap: the corrupted file scores BETTER on the fit-quality metric
check("sum e^2 of the CORRUPTED file", dot(e_bad_file, e_bad_file), F(15))
check("sum e^2 of the CLEAN file",     dot(e_clean, e_clean),       F(16))
print("   -> the sabotaged file looks BETTER (15 < 16) by sum of squares.")

# ============================================================================
# SECTION 7 -- why ONE check is not enough: the four suspects
# ============================================================================
head("SECTION 7  Balance check alone: four live suspects")

print("   Solve x_k * delta = 2 for each candidate k, then test sum e = 0.")
print("   k     x_k   delta = 2/x_k   repaired e_k   repaired vector          sum e")
survivors = []
for k in range(n):
    if x[k] == 0:
        print(f"   {names[k]:4s}  {S(x[k]):>3}   IMPOSSIBLE (0*delta = 0, never 2)")
        continue
    d_k = B_obs / x[k]
    rep = list(e_bad_file)
    rep[k] = e_bad_file[k] - d_k
    s = dot(m, rep)
    flag = "OK" if s == 0 else "reject"
    print(f"   {names[k]:4s}  {S(x[k]):>3}   {S(d_k):>12}   {S(rep[k]):>12}   "
          f"{row(rep):24s} {S(s):>4}  {flag}")
    if s == 0:
        survivors.append(names[k])
check("survivors after BOTH checks", F(len(survivors)), F(1))
print(f"   survivor: {survivors[0]}")

# exact suspect deltas quoted in the markdown
check("AXL would need delta", B_obs / x[0], F(-1))
check("BRN would need delta", B_obs / x[1], F(-2))
check("DLT would need delta", B_obs / x[3], F(2))
check("EMK would need delta", B_obs / x[4], F(1))
check("AXL repaired -> sum e", dot(m, [F(2), F(-3), F(2), F(1), F(0)]), F(2))
check("BRN repaired -> sum e", dot(m, [F(1), F(-1), F(2), F(1), F(0)]), F(3))
check("DLT repaired -> sum e", dot(m, [F(1), F(-3), F(2), F(-1), F(0)]), F(-1))

# ============================================================================
# SECTION 8 -- the wrong methods a player actually reaches for
# ============================================================================
head("SECTION 8  Wrong methods, and what each returns numerically")

abs_e = [abs(ei) for ei in e_bad_file]
i_bige = max(range(n), key=lambda i: abs_e[i])
print(f"   (a) 'biggest |residual| is the fake'  -> |e| = {row(abs_e)} -> "
      f"{names[i_bige]}  (WRONG)")
check("  biggest |e| is BRN with 3", abs_e[i_bige], F(3))
check("  ...and BRN is not the culprit", F(i_bige == CULPRIT), F(0))
# quantify the failure: force BRN to carry the whole delta = 1
rep_b = list(e_bad_file); rep_b[1] -= S_obs
print(f"       repairing BRN instead: e -> {row(rep_b)}")
check("  sum e  after wrong repair (fixed by construction)", dot(m, rep_b), F(0))
check("  sum x*e after wrong repair (STILL BROKEN)", dot(x, rep_b), F(3))

tf = [abs(xi * ei) for xi, ei in zip(x, e_bad_file)]
i_bigtf = max(range(n), key=lambda i: tf[i])
print(f"   (b) 'biggest |x*e| term is the fake'  -> |x*e| = {row(tf)} -> "
      f"{names[i_bigtf]}  (WRONG)")
check("  biggest |x*e| is BRN with 3", tf[i_bigtf], F(3))
check("  ...and BRN is not the culprit", F(i_bigtf == CULPRIT), F(0))

print(f"   (c) 'the residual that is exactly 0 must be the fake' -> {names[4]}  "
      f"(right stock, no reasoning)")
print(f"   (d) 'use only the cheapness balance'  -> 4 live suspects, no unique answer")
print(f"   (e) 'sum e^2 will reveal it'          -> corrupted 15 < clean 16, "
      f"the check points the wrong way")

# ============================================================================
# SECTION 9 -- the near miss: corrupting the asset with x = 0
# ============================================================================
head("SECTION 9  The near miss -- corrupt CHR, where x = 0")

NEAR_K, NEAR_D = 2, F(3)     # CHR: e 2 -> 5
e_near = list(e_clean); e_near[NEAR_K] += NEAR_D
print("   received e =", row(e_near))
check("received e", tuple(e_near), tuple(frac('1', '-3', '5', '1', '-1')))
check("CHEAPNESS BALANCE sum x*e -- COMPLETELY BLIND", dot(x, e_near), F(0))
check("MARKET CHECK sum e -- catches it", dot(m, e_near), F(3))
check("  delta = sum e", dot(m, e_near), NEAR_D)
check("  x_k = (sum x*e)/(sum e) = 0/3", dot(x, e_near) / dot(m, e_near), F(0))
near_matches = [names[i] for i in range(n) if x[i] == 0]
check("  exactly one asset has x = 0", F(len(near_matches)), F(1))
print(f"   CULPRIT = {near_matches[0]} -- located by the market column alone")
check("  repaired value", e_near[NEAR_K] - NEAR_D, e_clean[NEAR_K])
check("  the corrupted cell is the LARGEST number on the page",
      F(max(abs(v) for v in e_near) == abs(e_near[NEAR_K])), F(1))
print("   -> so heuristic (c) 'the odd-looking cell' is worthless: here it is the "
      "biggest, there it was 0.")
check("sum e^2 of the near-miss file", dot(e_near, e_near), F(37))

print()
print("   ONE-COLUMN WORLD (the cold open: no market column, nothing forces sum e):")
e_cold_bad = list(e_at2); e_cold_bad[2] += F('7/2')      # CHR: 1/2 -> 4
print("   corrupt CHR from 1/2 to 4:", row(e_cold_bad))
check("  sum x*e unchanged -- UNDETECTABLE, forever", dot(x0, e_cold_bad), F(0))
check("  sum e moves 2 -> 11/2, but nothing forces sum e, so it proves nothing",
      sum(e_cold_bad), F('11/2'))
check("  (clean sum e was)", sum(e_at2), F(2))

# ============================================================================
# SECTION 10 -- what NO number of these checks can see
# ============================================================================
head("SECTION 10  The corruptions that are invisible to BOTH checks")

print("   A corruption vector D is invisible iff  sum D = 0  AND  sum x*D = 0.")
print("   1 cell: sum D = D_k = 0 forces D = 0. No single-cell corruption escapes.")

pairs_ok = all(x[i] != x[j] for i, j in combinations(range(n), 2))
check("all x values distinct (so no 2-cell corruption escapes)", F(pairs_ok), F(1))
print("   2 cells i,j: D_i + D_j = 0 and x_i D_i + x_j D_j = 0 give D_i (x_i - x_j) = 0,")
print("                and x_i != x_j for every pair, so D_i = 0.")

D = frac('1', '-2', '1', '0', '0')
check("3 cells: D = [1,-2,1,0,0] -> sum D", dot(m, D), F(0))
check("                            -> sum x*D", dot(x, D), F(0))
e_inv = [ei + di for ei, di in zip(e_clean, D)]
print("   sabotaged file =", row(e_inv))
check("invisible file", tuple(e_inv), tuple(frac('2', '-5', '3', '1', '-1')))
check("  CHECK 1 sum e   -- passes", dot(m, e_inv), F(0))
check("  CHECK 2 sum x*e -- passes", dot(x, e_inv), F(0))
check("  sum e^2 of the sabotaged file", dot(e_inv, e_inv), F(40))
check("  sum e^2 of the clean file",     dot(e_clean, e_clean), F(16))
check("  ratio", F(40, 16), F('5/2'))
print("   -> 2.5x worse (a 150% increase) and BOTH checks report perfect health.")

# brute force: how many small-integer invisible corruptions exist?
rng = [F(v) for v in range(-2, 3)]
invisible = [d for d in product(rng, repeat=5)
             if any(t != 0 for t in d) and sum(d) == 0 and dot(x, d) == 0]
print(f"   brute force over D_i in {{-2..2}}^5: "
      f"{len(invisible)} non-zero invisible corruption vectors exist")
check("  D=[1,-2,1,0,0] is among them", F(tuple(D) in invisible), F(1))
check("  none of them is supported on 1 cell",
      F(any(sum(1 for t in d if t != 0) == 1 for d in invisible)), F(0))
check("  none of them is supported on 2 cells",
      F(any(sum(1 for t in d if t != 0) == 2 for d in invisible)), F(0))
print("   Dimension count: 5 residuals, 2 linear checks -> the checks see 2 directions")
print("   out of 5. The other 3 dimensions are invisible by construction.")
check("invisible dimensions = n - (number of columns)", F(n) - F(2), F(3))

# ============================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level2.md.")
