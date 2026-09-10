#!/usr/bin/env python3
"""
verify_level1.py — recompute EVERY number printed in datasets/level1.md.

Standard library only. Exact rational arithmetic throughout (fractions.Fraction);
decimals appear only for display and are always labelled as rounded.

Run:  python3 tools/verify_level1.py
Exits 0 if every internal cross-check passes; raises AssertionError otherwise.

Sections mirror the markdown headings one-for-one:
  A. Cold-open recap (the dataset the player has already seen)
  B. The nudge identity, with exact numbers, from b = 0, b = 1, b = 2
  C. Why the h-term must vanish (the derivation of b = sum(x*r)/sum(x^2))
  D. Why the h^2 term makes the minimum unique (the penalty identity)
  E. Boss round dataset: month 2
  F. Boss round: order-of-magnitude guess
  G. Boss round: exact answer and residuals
  H. Boss round: the wrong methods, and what each returns
  I. The CHR question: dropping the unfittable stock
  J. Overtime: weighted least squares (BFRE p.25 uses sqrt-of-market-cap weights)
"""

from fractions import Fraction as F

CHECKS = []


def check(label, got, want):
    """Assert an exact rational equality and record it."""
    assert got == want, f"MISMATCH {label}: got {got}, want {want}"
    CHECKS.append(label)


def d(v, n=4):
    """Rounded decimal for display only."""
    return f"{float(v):.{n}f}"


def frac(*a):
    return [F(v) for v in a]


def rule(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ----------------------------------------------------------------------------
# Generic machinery: everything below is derived from these four functions only.
# ----------------------------------------------------------------------------

def sums(x, r, w=None):
    """Return (Sw, Sx, Sxx, Sxr, Sr, Srr) with optional weights w."""
    if w is None:
        w = [F(1)] * len(x)
    Sw = sum(w)
    Sx = sum(wi * xi for wi, xi in zip(w, x))
    Sxx = sum(wi * xi * xi for wi, xi in zip(w, x))
    Sxr = sum(wi * xi * ri for wi, xi, ri in zip(w, x, r))
    Sr = sum(wi * ri for wi, ri in zip(w, r))
    Srr = sum(wi * ri * ri for wi, ri in zip(w, r))
    return Sw, Sx, Sxx, Sxr, Sr, Srr


def SS(b, x, r, w=None):
    """Total weighted squared miss at slope b, computed residual-by-residual."""
    if w is None:
        w = [F(1)] * len(x)
    return sum(wi * (ri - b * xi) ** 2 for wi, xi, ri in zip(w, x, r))


def pull(b, x, r, w=None):
    """P(b) = sum w*x*(r - b*x)  -- the coefficient the h-term carries."""
    if w is None:
        w = [F(1)] * len(x)
    return sum(wi * xi * (ri - b * xi) for wi, xi, ri in zip(w, x, r))


def resid(b, x, r):
    return [ri - b * xi for xi, ri in zip(x, r)]


# ============================================================================
# A. COLD-OPEN RECAP — the dataset already used in datasets/level0.md
# ============================================================================
rule("A. COLD-OPEN RECAP (dataset from level0.md; the player has seen this)")

names0 = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x0 = frac('-3/2', '-1/2', '0', '1', '2')
r0 = frac('-2', '-2', '1/2', '4', '7/2')

_, Sx0, Sxx0, Sxr0, Sr0, Srr0 = sums(x0, r0)

print("  stock :", "  ".join(f"{n:>6}" for n in names0))
print("  x     :", "  ".join(f"{d(v,1):>6}" for v in x0))
print("  r (%) :", "  ".join(f"{d(v,1):>6}" for v in r0))
print()
print(f"  sum x    = {Sx0}")
print(f"  sum x^2  = {Sxx0}  = {d(Sxx0,1)}")
print(f"  sum x*r  = {Sxr0}")
print(f"  sum r    = {Sr0}")
print(f"  sum r^2  = {Srr0}  = {d(Srr0,2)}")

check("cold sum x", Sx0, F(1))
check("cold sum x^2", Sxx0, F(15, 2))
check("cold sum x*r", Sxr0, F(15))
check("cold sum r", Sr0, F(4))
check("cold sum r^2", Srr0, F(73, 2))

b0 = Sxr0 / Sxx0
print(f"  b = sum(x*r)/sum(x^2) = ({Sxr0}) / ({Sxx0}) = {b0}")
check("cold b = 2", b0, F(2))

# SS as a polynomial in b, and SS computed residual-by-residual, must agree.
print()
print("  SS(b) = sum r^2 - 2b*sum(x*r) + b^2*sum(x^2)")
print(f"        = {Srr0} - {2*Sxr0}b + {Sxx0}b^2   "
      f"(= {d(Srr0,2)} - 30b + 7.5b^2)")
for bb in [F(0), F(1), F(2), F(3), F(4)]:
    poly = Srr0 - 2 * bb * Sxr0 + bb * bb * Sxx0
    direct = SS(bb, x0, r0)
    check(f"cold SS poly==direct at b={bb}", poly, direct)
    print(f"     SS({bb}) = {direct}  = {d(direct,4)}")

check("cold SS(0) == sum r^2", SS(F(0), x0, r0), Srr0)
check("cold SS(1) == 14", SS(F(1), x0, r0), F(14))
check("cold SS(2) == 13/2", SS(F(2), x0, r0), F(13, 2))
check("cold SS(3) == 14", SS(F(3), x0, r0), F(14))
check("cold SS(4) == 73/2", SS(F(4), x0, r0), F(73, 2))
check("cold SS(1)==SS(3)", SS(F(1), x0, r0), SS(F(3), x0, r0))
check("cold SS(0)==SS(4)", SS(F(0), x0, r0), SS(F(4), x0, r0))

e0 = resid(F(2), x0, r0)
print()
print("  residuals at b = 2 :", "  ".join(f"{d(v,1):>6}" for v in e0))
print(f"     sum e    = {sum(e0)}        (NOT zero)")
print(f"     sum x*e  = {sum(xi*ei for xi, ei in zip(x0, e0))}        (zero)")
print(f"     sum e^2  = {sum(ei*ei for ei in e0)} = {d(sum(ei*ei for ei in e0),4)}")
check("cold sum e", sum(e0), F(2))
check("cold sum x*e", sum(xi * ei for xi, ei in zip(x0, e0)), F(0))
check("cold sum e^2", sum(ei * ei for ei in e0), F(13, 2))


# ============================================================================
# B. THE NUDGE IDENTITY, WITH EXACT NUMBERS
#    SS(b+h) - SS(b) = -2h*sum(x*(r-bx)) + h^2*sum(x^2)
# ============================================================================
rule("B. THE NUDGE IDENTITY  SS(b+h) - SS(b) = -2h*P(b) + h^2*sum(x^2)")

# First: prove the identity holds exactly, for many (b, h) pairs, by brute force.
test_b = [F(0), F(1), F(2), F(3), F(-1), F(5, 2), F(14, 9), F(43, 10)]
test_h = [F(1), F(-1), F(2), F(3), F(4), F(1, 2), F(-1, 2), F(1, 10),
          F(1, 100), F(-1, 100), F(1, 1000), F(7, 3)]
n_id = 0
for bb in test_b:
    for hh in test_h:
        lhs = SS(bb + hh, x0, r0) - SS(bb, x0, r0)
        rhs = -2 * hh * pull(bb, x0, r0) + hh * hh * Sxx0
        assert lhs == rhs, f"identity broke at b={bb}, h={hh}"
        n_id += 1
print(f"  identity verified exactly on {n_id} (b,h) pairs of the cold-open data")
CHECKS.append("nudge identity, cold-open data")

print()
print("  P(b) = sum x*(r - b*x) = sum(x*r) - b*sum(x^2) = 15 - 7.5b")
for bb in [F(0), F(1), F(2), F(3)]:
    P = pull(bb, x0, r0)
    check(f"cold P({bb})", P, Sxr0 - bb * Sxx0)
    print(f"     P({bb}) = {P} = {d(P,4)}")

print()
print("  --- NUDGING FROM b = 0 :  SS(0+h) - SS(0) = -30h + 7.5h^2 ---")
print(f"  {'h':>8} | {'-2h*P(0)':>12} | {'h^2*sum x^2':>12} | {'total change':>13} | {'SS(0+h)':>10}")
for hh in [F(1, 10), F(1, 2), F(1), F(2), F(3), F(4), F(5)]:
    t1 = -2 * hh * pull(F(0), x0, r0)
    t2 = hh * hh * Sxx0
    tot = t1 + t2
    check(f"nudge0 h={hh}", SS(hh, x0, r0) - SS(F(0), x0, r0), tot)
    print(f"  {str(hh):>8} | {d(t1,4):>12} | {d(t2,4):>12} | {d(tot,4):>13} | {d(SS(hh,x0,r0),4):>10}")
print("  the single nudge from 0 stops paying at h = 2*P(0)/sum(x^2) = "
      f"{2*pull(F(0),x0,r0)/Sxx0} ; beyond that SS rises again")
check("cold breakeven from 0", 2 * pull(F(0), x0, r0) / Sxx0, F(4))

print()
print("  --- NUDGING FROM b = 1 :  SS(1+h) - SS(1) = -15h + 7.5h^2 ---")
print(f"  {'h':>8} | {'-2h*P(1)':>12} | {'h^2*sum x^2':>12} | {'total change':>13} | {'SS(1+h)':>10}")
for hh in [F(1, 1000), F(1, 100), F(1, 10), F(1), F(2), F(3)]:
    t1 = -2 * hh * pull(F(1), x0, r0)
    t2 = hh * hh * Sxx0
    tot = t1 + t2
    check(f"nudge1 h={hh}", SS(F(1) + hh, x0, r0) - SS(F(1), x0, r0), tot)
    ratio = abs(t1 / t2) if t2 != 0 else None
    print(f"  {str(hh):>8} | {d(t1,7):>12} | {d(t2,7):>12} | {d(tot,7):>13} | "
          f"{d(SS(F(1)+hh,x0,r0),7):>10}   |h-term| / |h^2-term| = {d(ratio,1)}")
check("cold breakeven from 1", 2 * pull(F(1), x0, r0) / Sxx0, F(2))
check("SS(1)==SS(3) via nudge h=2", SS(F(3), x0, r0), SS(F(1), x0, r0))
# The markdown's "reward / tax" column is exact at every row; the h = 3 entry is 2/3,
# not the 0.7 a one-decimal display would suggest.
_h3 = F(3)
check("cold reward/tax at h=3 is exactly 2/3",
      abs(-2 * _h3 * pull(F(1), x0, r0)) / (_h3 * _h3 * Sxx0), F(2, 3))

print()
print("  --- NUDGING FROM b = 2 :  P(2) = 0, so SS(2+h) - SS(2) = 7.5h^2 ---")
print(f"  {'h':>8} | {'-2h*P(2)':>12} | {'h^2*sum x^2':>12} | {'total change':>13} | {'SS(2+h)':>12}")
for hh in [F(1), F(-1), F(1, 2), F(-1, 2), F(1, 10), F(-1, 10), F(1, 100)]:
    t1 = -2 * hh * pull(F(2), x0, r0)
    t2 = hh * hh * Sxx0
    tot = t1 + t2
    check(f"nudge2 h={hh}", SS(F(2) + hh, x0, r0) - SS(F(2), x0, r0), tot)
    check(f"nudge2 h-term zero h={hh}", t1, F(0))
    print(f"  {str(hh):>8} | {d(t1,6):>12} | {d(t2,6):>12} | {d(tot,6):>13} | "
          f"{d(SS(F(2)+hh,x0,r0),6):>12}")
print("  every h-term is EXACTLY zero, and every total change is strictly positive")

# symmetry: SS(b*+h) == SS(b*-h) for the cold open
for hh in [F(1, 2), F(1), F(3, 2), F(2), F(1, 10)]:
    check(f"cold symmetry h={hh}", SS(F(2) + hh, x0, r0), SS(F(2) - hh, x0, r0))
print(f"  reflection check: SS(3/2) = {SS(F(3,2),x0,r0)} = {d(SS(F(3,2),x0,r0),4)}"
      f"   SS(5/2) = {SS(F(5,2),x0,r0)} = {d(SS(F(5,2),x0,r0),4)}")


# ============================================================================
# C. THE DERIVATION: the h-term must vanish
# ============================================================================
rule("C. DERIVATION -- if P(b) != 0 there is always a nudge that lowers SS")

print("  Claim: if P(b) != 0, pick h with the SAME SIGN as P(b) and")
print("         |h| < 2|P(b)|/sum(x^2).  Then SS strictly falls.")
print()
print("  Demonstrated at every b in the grid, with the largest safe h and with h/2:")
grid = [F(0), F(1, 2), F(1), F(3, 2), F(5, 2), F(3), F(4), F(-1), F(-2)]
print(f"  {'b':>6} | {'P(b)':>9} | {'safe |h| <':>10} | {'h used':>9} | {'SS(b)':>10} | {'SS(b+h)':>10} | falls?")
for bb in grid:
    P = pull(bb, x0, r0)
    if P == 0:
        continue
    lim = 2 * abs(P) / Sxx0
    hh = (lim / 2) if P > 0 else (-lim / 2)
    before, after = SS(bb, x0, r0), SS(bb + hh, x0, r0)
    assert after < before
    print(f"  {str(bb):>6} | {d(P,4):>9} | {d(lim,4):>10} | {d(hh,4):>9} | "
          f"{d(before,4):>10} | {d(after,4):>10} | {'YES' if after < before else 'no'}")
CHECKS.append("descent whenever P(b) != 0")

print()
print("  So the stopping point is exactly P(b) = 0:")
print("      sum(x*r) - b*sum(x^2) = 0   ->   b = sum(x*r)/sum(x^2)")
print(f"      15 - 7.5b = 0  ->  b = 15/7.5 = {Sxr0/Sxx0}")
check("solve P=0 gives b", Sxr0 / Sxx0, F(2))
check("P at solution is 0", pull(Sxr0 / Sxx0, x0, r0), F(0))
print("  and P(b) is literally sum(x*e), the h-term coefficient:")
eb = resid(b0, x0, r0)
check("P(b*) == sum x*e", pull(b0, x0, r0), sum(xi * ei for xi, ei in zip(x0, eb)))
print(f"      P(2) = sum x*e = {sum(xi*ei for xi, ei in zip(x0, eb))}")


# ============================================================================
# D. THE h^2 TERM: uniqueness, and the penalty identity
# ============================================================================
rule("D. THE h^2 TERM -- uniqueness and the penalty identity")

print("  With P(b*) = 0 the identity collapses to a single term:")
print("      SS(b) - SS(b*) = sum(x^2) * (b - b*)^2")
print()
print("  Checked exactly on the cold-open data for a spread of b:")
print(f"  {'b':>10} | {'b - b*':>10} | {'sum(x^2)*(b-b*)^2':>18} | {'SS(b)':>10} | {'SS(b*)+penalty':>15}")
for bb in [F(0), F(1), F(3, 2), F(2), F(5, 2), F(133, 48), F(3), F(4), F(-1)]:
    pen = Sxx0 * (bb - b0) ** 2
    check(f"penalty identity b={bb}", SS(bb, x0, r0), SS(b0, x0, r0) + pen)
    print(f"  {str(bb):>10} | {d(bb-b0,4):>10} | {d(pen,4):>18} | {d(SS(bb,x0,r0),4):>10} | "
          f"{d(SS(b0,x0,r0)+pen,4):>15}")
print()
print("  sum(x^2) > 0 (it is a sum of squares, and not every x is 0), so the")
print("  penalty is strictly positive for every b != b*.  Minimum is UNIQUE.")
print(f"  cold-open sum(x^2) = {Sxx0} > 0")

# The two level-0 wrong methods, re-derived through the penalty identity
naive_tot0 = Sr0 / Sx0
ratios0 = [ri / xi for xi, ri in zip(x0, r0) if xi != 0]
naive_avg0 = sum(ratios0) / len(ratios0)
print()
print("  Level-0's two wrong methods priced by the same identity:")
for lab, cand in [("sum r / sum x", naive_tot0), ("mean of r/x", naive_avg0)]:
    pen = Sxx0 * (cand - b0) ** 2
    check(f"cold trap {lab}", SS(cand, x0, r0), SS(b0, x0, r0) + pen)
    print(f"     {lab:<16} b = {cand} = {d(cand,4)}   SS = {d(SS(cand,x0,r0),4)}  "
          f"(= 6.5 + {d(pen,4)})")
print()
print("  markdown-quoted ratios derived from the rows above:")
_w1 = SS(naive_avg0, x0, r0) / SS(b0, x0, r0)
print(f"     mean(r/x) scorecard vs minimum: {SS(naive_avg0,x0,r0)}/{SS(b0,x0,r0)} = {_w1} "
      f"-> {d((_w1-1)*100,2)}% worse (markdown says 68.56%)")
# The literal 16829/9984 is what the markdown prints; assert against it, not against
# a re-evaluation of the same expression (that would check nothing at all).
check("cold mean-ratio SS ratio == 16829/9984", _w1, F(16829, 9984))
assert d((_w1 - 1) * 100, 2) == "68.56", "markdown's 68.56% claim"
CHECKS.append("cold mean-ratio is 68.56% worse")
_w2 = SS(naive_tot0, x0, r0) / SS(F(0), x0, r0)
print(f"     sum r/sum x scores {SS(naive_tot0,x0,r0)} = SS(0) = {SS(F(0),x0,r0)} exactly "
      f"(ratio {_w2}) -- as bad as predicting zero for everyone")
check("cold naive-total scores exactly SS(0)", SS(naive_tot0, x0, r0), SS(F(0), x0, r0))
check("cold mean-ratio is 133/48", naive_avg0, F(133, 48))
check("cold naive total is 4", naive_tot0, F(4))


# ============================================================================
# E. BOSS ROUND DATASET -- same five tickers, next month
# ============================================================================
rule("E. BOSS ROUND DATASET (month 2, same five tickers)")

names1 = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x1 = frac('-2', '-1', '0', '3/2', '5/2')
r1 = frac('-5/2', '-1', '3/5', '3', '21/5')

_, Sx1, Sxx1, Sxr1, Sr1, Srr1 = sums(x1, r1)

print("  stock :", "  ".join(f"{n:>6}" for n in names1))
print("  x     :", "  ".join(f"{d(v,1):>6}" for v in x1))
print("  r (%) :", "  ".join(f"{d(v,1):>6}" for v in r1))
print()
print("  the by-hand column, term by term:")
for n, xi, ri in zip(names1, x1, r1):
    print(f"     {n}:  x*r = ({d(xi,1)})*({d(ri,1)}) = {str(xi*ri):>6} = {d(xi*ri,2):>7}"
          f"      x^2 = {str(xi*xi):>6} = {d(xi*xi,2):>6}")
print(f"  sum x    = {Sx1}")
print(f"  sum x^2  = {Sxx1} = {d(Sxx1,2)}")
print(f"  sum x*r  = {Sxr1} = {d(Sxr1,2)}")
print(f"  sum r    = {Sr1} = {d(Sr1,2)}")
print(f"  sum r^2  = {Srr1} = {d(Srr1,2)}")

check("boss sum x", Sx1, F(1))
check("boss sum x^2", Sxx1, F(27, 2))
check("boss sum x*r", Sxr1, F(21))
check("boss sum r", Sr1, F(43, 10))
check("boss sum r^2", Srr1, F(137, 4))


# ============================================================================
# F. ORDER-OF-MAGNITUDE GUESS
# ============================================================================
rule("F. ORDER-OF-MAGNITUDE GUESS (before any calculator)")

dr = max(r1) - min(r1)
dx = max(x1) - min(x1)
guess = dr / dx
b1 = Sxr1 / Sxx1
print(f"  return spread   = {max(r1)} - ({min(r1)}) = {dr} = {d(dr,1)} percentage points")
print(f"  exposure spread = {max(x1)} - ({min(x1)}) = {dx} = {d(dx,1)} units")
print(f"  eyeball slope   = ({dr}) / ({dx}) = {guess} = {d(guess,4)} (rounded)")
print(f"  exact answer    = ({Sxr1}) / ({Sxx1}) = {b1} = {d(b1,4)} (rounded; 1.5 recurring)")
print()
print("  over a common denominator of 45:")
print(f"     eyeball = {guess.numerator*45//guess.denominator}/45     "
      f"exact = {b1.numerator*45//b1.denominator}/45")
print(f"  gap = {b1 - guess} = {d(b1-guess,4)} ; "
      f"the eyeball is low by {d((b1-guess)/b1*100,3)}% (rounded)")

check("boss eyeball slope", guess, F(67, 45))
check("boss exact b", b1, F(14, 9))
check("boss gap", b1 - guess, F(1, 15))
check("boss relative gap", (b1 - guess) / b1, F(3, 70))
check("14/9 == 70/45", b1, F(70, 45))
print()
print("  order-of-magnitude ladder the player must choose from:")
for cand in [F(15, 1000), F(15, 100), F(15, 10), F(15), F(150)]:
    print(f"     {d(cand,3):>8} %-per-unit   SS = {d(SS(cand,x1,r1),4):>12}   "
          f"exact {SS(cand,x1,r1)}")
print(f"  the winning rung is 1.5 ; SS at the exact b is {SS(b1,x1,r1)} = {d(SS(b1,x1,r1),4)}")
_r15 = SS(F(15, 10), x1, r1)
_lo = SS(F(15, 100), x1, r1) / _r15
_hi = SS(F(15), x1, r1) / _r15
print(f"  rung 1.5 beats its neighbours: rung 0.15 is {_lo} = {d(_lo,3)}x worse, "
      f"rung 15 is {_hi} = {d(_hi,2)}x worse (markdown rounds to 17 and 1500)")
assert F(17) < _lo < F(18) and F(1500) < _hi < F(1510)
CHECKS.append("boss rung 1.5 beats neighbours by ~17x and ~1500x")
check("boss SS at rung 1.5", SS(F(15, 10), x1, r1), F(13, 8))
check("boss SS at rung 15", SS(F(15), x1, r1), F(9767, 4))
check("boss SS at rung 150", SS(F(150), x1, r1), F(1189937, 4))
check("boss SS at rung 0.15", SS(F(15, 100), x1, r1), F(22603, 800))
check("boss SS at rung 0.015", SS(F(15, 1000), x1, r1), F(2689843, 80000))


# ============================================================================
# G. EXACT ANSWER AND RESIDUALS
# ============================================================================
rule("G. BOSS ROUND -- exact answer, residuals, checks")

print(f"  b = sum(x*r)/sum(x^2) = ({Sxr1}) / ({Sxx1}) = {2*Sxr1}/{2*Sxx1} = {b1}")
print(f"    = {d(b1,4)} % per unit of cheapness (rounded; the exact value is 14/9)")
print()
e1 = resid(b1, x1, r1)
print(f"  {'stock':>6} | {'x':>6} | {'r':>6} | {'b*x':>10} | {'e = r - b*x':>14} | {'e (dec)':>9}")
for n, xi, ri, ei in zip(names1, x1, r1, e1):
    print(f"  {n:>6} | {d(xi,1):>6} | {d(ri,1):>6} | {str(b1*xi):>10} | {str(ei):>14} | {d(ei,4):>9}")

check("boss e AXL", e1[0], F(11, 18))
check("boss e BRN", e1[1], F(5, 9))
check("boss e CHR", e1[2], F(3, 5))
check("boss e DLT", e1[3], F(2, 3))
check("boss e EMK", e1[4], F(14, 45))

Se1 = sum(e1)
Sxe1 = sum(xi * ei for xi, ei in zip(x1, e1))
See1 = sum(ei * ei for ei in e1)
print()
print(f"  sum e   = {Se1} = {d(Se1,4)}   <-- NOT zero, and every single e > 0")
print(f"  sum x*e = {Sxe1}                     <-- zero: the h-term has vanished")
print(f"  sum e^2 = {See1} = {d(See1,4)}")
check("boss sum e", Se1, F(247, 90))
check("boss sum x*e", Sxe1, F(0))
check("boss sum e^2", See1, F(19, 12))
check("boss sum e == sum r - b*sum x", Se1, Sr1 - b1 * Sx1)

# The markdown warns that sum(e) is the FINGERPRINT of the missing second dial, not its
# size.  Fit the two-dial model here once, purely to keep that warning honest: adding an
# intercept re-estimates the slope too, so the intercept it lands on is close to, but not
# equal to, the mean residual of the one-dial fit.
_n = len(x1)
_xbar, _rbar = Sx1 / _n, Sr1 / _n
_b_two = (Sxr1 - _n * _xbar * _rbar) / (Sxx1 - _n * _xbar * _xbar)
_a_two = _rbar - _b_two * _xbar
print()
print(f"  two-dial fit (Level 5's model, computed here only to bound a claim):")
print(f"     slope     = {_b_two} = {d(_b_two,4)}   (one-dial slope was {b1} = {d(b1,4)})")
print(f"     intercept = {_a_two} = {d(_a_two,4)}")
print(f"     mean residual of the ONE-dial fit = {Se1/_n} = {d(Se1/_n,4)}  -- close, NOT equal")
check("boss two-dial slope", _b_two, F(53, 35))
check("boss two-dial intercept", _a_two, F(39, 70))
check("boss one-dial mean residual", Se1 / _n, F(247, 450))
assert _a_two != Se1 / _n, "the markdown's 'fingerprint, not size' warning"
CHECKS.append("two-dial intercept != mean one-dial residual")
assert all(ei > 0 for ei in e1), "expected every boss residual to be positive"
CHECKS.append("every boss residual positive")

print()
print(f"  SS(b) = {Srr1} - {2*Sxr1}b + {Sxx1}b^2   "
      f"(= {d(Srr1,2)} - 42b + 13.5b^2)")
for bb in [F(0), F(1), b1, F(2), F(3)]:
    poly = Srr1 - 2 * bb * Sxr1 + bb * bb * Sxx1
    check(f"boss SS poly==direct b={bb}", poly, SS(bb, x1, r1))
    print(f"     SS({str(bb):>6}) = {str(SS(bb,x1,r1)):>12} = {d(SS(bb,x1,r1),4)}")
check("boss SS(b*) == sum e^2", SS(b1, x1, r1), See1)
check("boss SS(0) == sum r^2", SS(F(0), x1, r1), Srr1)

# nudge identity on the boss data
n_id2 = 0
for bb in [F(0), F(1), b1, F(2), F(43, 10)]:
    for hh in test_h:
        assert (SS(bb + hh, x1, r1) - SS(bb, x1, r1)
                == -2 * hh * pull(bb, x1, r1) + hh * hh * Sxx1)
        n_id2 += 1
print(f"  nudge identity verified exactly on {n_id2} (b,h) pairs of the boss data")
CHECKS.append("nudge identity, boss data")

print()
print("  nudging away from the answer: SS(14/9 + h) - SS(14/9) = 13.5h^2")
print(f"  {'h':>8} | {'-2h*P':>8} | {'h^2*sum x^2':>14} | {'SS(14/9 + h)':>16} | {'decimal':>10}")
for hh in [F(1, 2), F(-1, 2), F(1, 10), F(-1, 10), F(1, 100)]:
    t1 = -2 * hh * pull(b1, x1, r1)
    t2 = hh * hh * Sxx1
    check(f"boss nudge h={hh}", SS(b1 + hh, x1, r1) - SS(b1, x1, r1), t1 + t2)
    check(f"boss h-term zero h={hh}", t1, F(0))
    print(f"  {str(hh):>8} | {str(t1):>8} | {str(t2):>14} | {str(SS(b1+hh,x1,r1)):>16} | "
          f"{d(SS(b1+hh,x1,r1),5):>10}")
print(f"  the symmetric pair 14/9 - 1/2 = {b1-F(1,2)} and 14/9 + 1/2 = {b1+F(1,2)}")
print(f"  both give SS = {SS(b1+F(1,2),x1,r1)} = {d(SS(b1+F(1,2),x1,r1),4)}")
check("boss symmetric pair lo", b1 - F(1, 2), F(19, 18))
check("boss symmetric pair hi", b1 + F(1, 2), F(37, 18))
check("boss symmetric SS", SS(b1 + F(1, 2), x1, r1), F(119, 24))
check("boss symmetry equal", SS(b1 + F(1, 2), x1, r1), SS(b1 - F(1, 2), x1, r1))


# ============================================================================
# H. THE WRONG METHODS
# ============================================================================
rule("H. THE WRONG METHODS -- what each one actually returns")

ratios1 = [(n, ri / xi) for n, xi, ri in zip(names1, x1, r1) if xi != 0]
print("  per-stock slopes r/x (CHR excluded, x = 0):")
for n, v in ratios1:
    print(f"     {n}: {v} = {d(v,4)}")
vals = [v for _, v in ratios1]
mean_ratio = sum(vals) / len(vals)
srt = sorted(vals)
median_ratio = (srt[1] + srt[2]) / 2

wrong = [
    ("least squares  sum(x*r)/sum(x^2)", b1),
    ("total over total  sum(r)/sum(x)", Sr1 / Sx1),
    ("average the per-stock slopes  mean(r/x)", mean_ratio),
    ("median of the per-stock slopes", median_ratio),
    ("line through the two extreme stocks", guess),
    ("biggest exposure only  r_EMK/x_EMK", r1[4] / x1[4]),
    ("shape error  sum(r)/sum(x^2)", Sr1 / Sxx1),
    ("shape error  sum(x*r)/sum(x)", Sxr1 / Sx1),
]
print()
print(f"  {'method':<42} | {'b':>10} | {'b (dec)':>9} | {'SS(b)':>11} | {'penalty':>10} | {'x worse'}")
for lab, cand in wrong:
    pen = Sxx1 * (cand - b1) ** 2
    check(f"boss penalty identity: {lab}", SS(cand, x1, r1), See1 + pen)
    times = SS(cand, x1, r1) / See1
    print(f"  {lab:<42} | {str(cand):>10} | {d(cand,4):>9} | {d(SS(cand,x1,r1),4):>11} | "
          f"{d(pen,4):>10} | {d(times,3)}")

check("boss mean of ratios", mean_ratio, F(593, 400))
check("boss median of ratios", median_ratio, F(293, 200))
check("boss total/total", Sr1 / Sx1, F(43, 10))
check("boss EMK-only slope", r1[4] / x1[4], F(42, 25))
check("boss shape error r/x^2", Sr1 / Sxx1, F(43, 135))
check("boss shape error xr/x", Sxr1 / Sx1, F(21))

# The build-the-shape check in Part 1 kills exactly the two rows whose units are wrong.
# sum(r)/sum(x) has the RIGHT units (percent per unit of cheapness) and survives it -- and
# among the survivors it is the worst.  The markdown says both; assert both.
_right_units = [("least squares", b1), ("sum r / sum x", Sr1 / Sx1),
                ("mean(r/x)", mean_ratio), ("median(r/x)", median_ratio),
                ("two extremes", guess), ("EMK only", r1[4] / x1[4])]
_worst = max(_right_units, key=lambda kv: SS(kv[1], x1, r1))
assert _worst[0] == "sum r / sum x", _worst
print(f"  worst method the units check CANNOT kill: {_worst[0]}, b = {_worst[1]}, "
      f"SS = {d(SS(_worst[1],x1,r1),4)}")
CHECKS.append("sum r/sum x survives the units check and is the worst that does")
check("boss SS at 43/10", SS(F(43, 10), x1, r1), F(20653, 200))
check("boss ratio worse at 43/10", SS(F(43, 10), x1, r1) / See1, F(61959, 950))

print()
print("  how far the mean-of-slopes lands from the truth:")
print(f"     mean(r/x) = {mean_ratio} = {d(mean_ratio,4)}   vs   b = {b1} = {d(b1,4)}")
print(f"     difference = {b1 - mean_ratio} = {d(b1-mean_ratio,5)}  "
      f"({d((b1-mean_ratio)/b1*100,3)}% low, rounded)")
check("boss mean-ratio gap", b1 - mean_ratio, F(263, 3600))
_vote = (x1[4] ** 2) / (x1[1] ** 2)
print(f"  vote weight is x^2: EMK/BRN = ({x1[4]})^2 / ({x1[1]})^2 = {x1[4]**2}/{x1[1]**2} "
      f"= {_vote} = {d(_vote,2)} times the vote")
check("boss EMK vs BRN vote weight", _vote, F(25, 4))
_ssratio = SS(mean_ratio, x1, r1) / See1
print(f"  mean(r/x) scorecard vs minimum: {_ssratio} = {d(_ssratio,4)} "
      f"-> {d((_ssratio-1)*100,2)}% worse (markdown says 4.55%)")
check("boss mean-ratio SS ratio", SS(mean_ratio, x1, r1), See1 + Sxx1 * (mean_ratio - b1) ** 2)
check("boss mean-ratio SS ratio exact", _ssratio, F(1589169, 1520000))
CHECKS.append("boss mean-ratio is 4.55% worse on the scorecard")
print(f"  and sum(r)/sum(x) here IS just sum r, because sum x = {Sx1}: "
      f"{Sr1/Sx1} = {Sr1}")
check("boss total/total equals sum r since sum x = 1", Sr1 / Sx1, Sr1)


# ============================================================================
# I. DROPPING CHR
# ============================================================================
rule("I. DROPPING CHR (x = 0) -- what changes and what does not")

names2 = [n for n, xi in zip(names1, x1) if xi != 0]
x2 = [xi for xi in x1 if xi != 0]
r2 = [ri for xi, ri in zip(x1, r1) if xi != 0]
_, Sx2, Sxx2, Sxr2, Sr2, Srr2 = sums(x2, r2)
b2 = Sxr2 / Sxx2
print(f"  kept: {names2}")
print(f"  sum x*r  = {Sxr2}   (unchanged: CHR contributed 0*0.6 = 0)")
print(f"  sum x^2  = {Sxx2}   (unchanged: CHR contributed 0^2 = 0)")
print(f"  b        = {b2} = {d(b2,4)}   IDENTICAL to the five-stock answer")
check("dropping CHR leaves sum x*r", Sxr2, Sxr1)
check("dropping CHR leaves sum x^2", Sxx2, Sxx1)
check("dropping CHR leaves b", b2, b1)

e2 = resid(b2, x2, r2)
print(f"  sum e^2  = {sum(ei*ei for ei in e2)} = {d(sum(ei*ei for ei in e2),4)}   "
      f"(was {See1} = {d(See1,4)})")
print(f"  sum r^2  = {Srr2} = {d(Srr2,4)}   (was {Srr1} = {d(Srr1,4)})")
print(f"  the drop is exactly CHR's own squared return: {r1[2]}^2 = {r1[2]**2} = {d(r1[2]**2,4)}")
check("CHR-free sum e^2", sum(ei * ei for ei in e2), F(367, 300))
check("CHR-free sum r^2", Srr2, F(3389, 100))
check("sum e^2 drop == CHR r^2", See1 - sum(ei * ei for ei in e2), r1[2] ** 2)
check("sum r^2 drop == CHR r^2", Srr1 - Srr2, r1[2] ** 2)


# ============================================================================
# J. OVERTIME -- WEIGHTED LEAST SQUARES (what BFRE actually runs, p.25)
# ============================================================================
rule("J. OVERTIME -- weighted least squares (BFRE p.25: sqrt-of-market-cap weights)")

# EMK is 16x the market cap of the others, so its sqrt-cap weight is 4x.
w1 = frac('1', '1', '1', '1', '4')
_, Swx, Swxx, Swxr, Swr, Swrr = sums(x1, r1, w1)
bw = Swxr / Swxx
print(f"  weights w (sqrt of market cap, EMK 16x the cap of a peer): "
      f"{[str(v) for v in w1]}")
print(f"  sum w*x*r = {Swxr} = {d(Swxr,2)}")
print(f"  sum w*x^2 = {Swxx} = {d(Swxx,2)}")
print(f"  b_w = ({Swxr}) / ({Swxx}) = {bw} = {d(bw,5)} (rounded)")
print(f"  unweighted b was {b1} = {d(b1,5)} ; EMK's own slope is "
      f"{r1[4]/x1[4]} = {d(r1[4]/x1[4],4)}")
print("  -> up-weighting EMK drags b toward EMK's own slope, as it must")
check("weighted sum w*x*r", Swxr, F(105, 2))
check("weighted sum w*x^2", Swxx, F(129, 4))
check("weighted b", bw, F(70, 43))
assert b1 < bw < r1[4] / x1[4], "b_w should sit between b and EMK's slope"
CHECKS.append("b_w sits between b and EMK slope")

ew = resid(bw, x1, r1)
Swxe = sum(wi * xi * ei for wi, xi, ei in zip(w1, x1, ew))
Sxew = sum(xi * ei for xi, ei in zip(x1, ew))
print()
print(f"  weighted residuals: {[str(v) for v in ew]}")
print(f"  sum w*x*e = {Swxe}        <-- the balance the weighted fit forces")
print(f"  sum   x*e = {Sxew} = {d(Sxew,4)}   <-- NOT zero; the unweighted balance is broken")
check("weighted balance holds", Swxe, F(0))
check("unweighted balance broken", Sxew, F(-42, 43))

print(f"  weighted SS at b_w   = {SS(bw,x1,r1,w1)} = {d(SS(bw,x1,r1,w1),5)}")
print(f"  weighted SS at b     = {SS(b1,x1,r1,w1)} = {d(SS(b1,x1,r1,w1),5)}  (worse, by the weighted yardstick)")
print(f"  unweighted SS at b_w = {SS(bw,x1,r1)} = {d(SS(bw,x1,r1),5)}")
print(f"  unweighted SS at b   = {SS(b1,x1,r1)} = {d(SS(b1,x1,r1),5)}  (better, by the unweighted yardstick)")
assert SS(bw, x1, r1, w1) < SS(b1, x1, r1, w1)
assert SS(b1, x1, r1) < SS(bw, x1, r1)
CHECKS.append("each b wins on its own yardstick")
check("weighted penalty identity", SS(b1, x1, r1, w1),
      SS(bw, x1, r1, w1) + Swxx * (b1 - bw) ** 2)
print(f"  weighted penalty identity: SS_w(b) - SS_w(b_w) = sum(w*x^2)*(b-b_w)^2 = "
      f"{Swxx*(b1-bw)**2} = {d(Swxx*(b1-bw)**2,6)}")

# generic weighted nudge identity
n_id3 = 0
for bb in [F(0), F(1), bw, b1, F(2)]:
    for hh in test_h:
        assert (SS(bb + hh, x1, r1, w1) - SS(bb, x1, r1, w1)
                == -2 * hh * pull(bb, x1, r1, w1) + hh * hh * Swxx)
        n_id3 += 1
print(f"  weighted nudge identity verified exactly on {n_id3} (b,h) pairs")
CHECKS.append("weighted nudge identity")


# ============================================================================
rule("ALL CHECKS PASSED")
print(f"  {len(CHECKS)} exact-rational checks, 0 failures.")
print("  Every number printed above is a Fraction; every decimal shown is a")
print("  rounded display of one of them and is labelled as such in the markdown.")
