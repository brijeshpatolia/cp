#!/usr/bin/env python3
"""
verify_level3.py -- recomputes EVERY number printed in datasets/level3.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level3.py
Exits 0 if every assertion holds; exits non-zero (with the offending value) otherwise.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from itertools import product
import sys

# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def frac(*a):
    return [F(v) for v in a]


def S(v):
    """exact display: integers as integers, else a/b; tuples/lists bracketed"""
    if isinstance(v, (tuple, list)):
        return "[" + ", ".join(S(t) for t in v) + "]"
    return str(v)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def dec(v, n=4):
    """rounded decimal display of a Fraction, half-up, sign preserved"""
    neg = v < 0
    v = -v if neg else v
    scaled = (v * 10 ** n)
    whole = scaled.numerator // scaled.denominator
    rem = scaled - whole
    if rem * 2 >= 1:
        whole += 1
    s = str(whole).rjust(n + 1, "0")
    out = (s[:-n] + "." + s[-n:]) if n else s
    return ("-" if neg else "") + out


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


def show(label, v, n=4):
    print(f"        {label} = {S(v)} = {dec(v, n)} (rounded)")


# ----------------------------------------------------------------------------
# generic two-column machinery, used by both datasets
# ----------------------------------------------------------------------------

def sums(x, s, r):
    """the six cross-products the whole level runs on, plus Sr and Srr"""
    return dict(
        Sx=sum(x), Ss=sum(s), Sr=sum(r),
        Sxx=dot(x, x), Sss=dot(s, s), Sxs=dot(x, s),
        Sxr=dot(x, r), Ssr=dot(s, r), Srr=dot(r, r),
    )


def solve2(S_):
    """Cramer on   Sxx b1 + Sxs b2 = Sxr ;  Sxs b1 + Sss b2 = Ssr"""
    det = S_["Sxx"] * S_["Sss"] - S_["Sxs"] ** 2
    b1 = (S_["Sxr"] * S_["Sss"] - S_["Ssr"] * S_["Sxs"]) / det
    b2 = (S_["Sxx"] * S_["Ssr"] - S_["Sxs"] * S_["Sxr"]) / det
    return b1, b2, det


def resid(x, s, r, b1, b2):
    return [ri - b1 * xi - b2 * si for xi, si, ri in zip(x, s, r)]


def SS(x, s, r, b1, b2):
    return sum(e * e for e in resid(x, s, r, b1, b2))


def SS_expanded(S_, b1, b2):
    """the same number, from the six sums only -- never from the residuals"""
    return (S_["Srr"] - 2 * b1 * S_["Sxr"] - 2 * b2 * S_["Ssr"]
            + b1 ** 2 * S_["Sxx"] + 2 * b1 * b2 * S_["Sxs"] + b2 ** 2 * S_["Sss"])


def balances(S_, b1, b2):
    """(B1, B2) = (Sum x*e, Sum s*e) computed from the sums only"""
    B1 = S_["Sxr"] - b1 * S_["Sxx"] - b2 * S_["Sxs"]
    B2 = S_["Ssr"] - b1 * S_["Sxs"] - b2 * S_["Sss"]
    return B1, B2


def Qform(S_, p, q):
    return p ** 2 * S_["Sxx"] + 2 * p * q * S_["Sxs"] + q ** 2 * S_["Sss"]


def passes_to_1pc(rr):
    """how many full passes of the chase bring the relative error below 1%.
    Only ever called with rr comfortably below 1, so the loop is short."""
    if rr == 0:
        return 1
    k = 1
    while rr ** k >= F(1, 100):
        k += 1
    return k


def backfit(S_, passes):
    """one-at-a-time chase, starting from 'pretend the size column is absent'.
    Each pass: refit b1 holding b2, then refit b2 holding the new b1."""
    out = []
    b2 = F(0)
    for _ in range(passes):
        b1 = (S_["Sxr"] - b2 * S_["Sxs"]) / S_["Sxx"]
        mid = (b1, b2)
        b2 = (S_["Ssr"] - b1 * S_["Sxs"]) / S_["Sss"]
        out.append((mid, (b1, b2)))
    return out


# ============================================================================
# SECTION 1 -- the derivation dataset: the cold open plus a size column
# ============================================================================
head("SECTION 1  Derivation dataset (cold-open month + the size file)")

names = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x = frac('-3/2', '-1/2', '0', '1', '2')          # cheapness, from Level 0
s = frac('1', '-1', '2', '0', '-2')              # size, new at Level 3
r = frac('-2', '-2', '1/2', '4', '7/2')          # returns, from Level 0

print("   stock :   x     s     r")
for n_, xi, si, ri in zip(names, x, s, r):
    print(f"   {n_}   : {S(xi):>5} {S(si):>5} {S(ri):>5}")

D = sums(x, s, r)

check("Sum x", D["Sx"], F(1))
check("Sum s", D["Ss"], F(0))
check("Sum r", D["Sr"], F(4))
check("Sum x^2", D["Sxx"], F(15, 2))
check("Sum s^2", D["Sss"], F(10))
check("Sum x*s", D["Sxs"], F(-5))
check("Sum x*r", D["Sxr"], F(15))
check("Sum s*r", D["Ssr"], F(-6))
check("Sum r^2", D["Srr"], F(73, 2))

print("   Level 0/1 carry-over, re-derived here:")
check("cheapness-alone b = Sxr/Sxx", D["Sxr"] / D["Sxx"], F(2))
check("cheapness-alone SS = Srr - Sxr^2/Sxx",
      D["Srr"] - D["Sxr"] ** 2 / D["Sxx"], F(13, 2))
e_cold = [ri - 2 * xi for xi, ri in zip(x, r)]
check("cheapness-alone residuals", e_cold, frac('1', '-1', '1/2', '2', '-1/2'))
check("cheapness-alone Sum e", sum(e_cold), F(2))
check("cheapness-alone Sum x*e", dot(x, e_cold), F(0))
check("cheapness-alone Sum s*e (the plank that is NOT level)", dot(s, e_cold), F(4))

# ============================================================================
# SECTION 2 -- the two-column nudge identity
# ============================================================================
head("SECTION 2  The two-column nudge identity")

print("   SS(b1+p, b2+q) = SS(b1,b2) - 2p*B1 - 2q*B2 + p^2*Sxx + 2pq*Sxs + q^2*Sss")
print("   verified exactly on a grid of (b1, b2, p, q):")

grid_b = frac('0', '1', '2', '12/5', '-1', '7/3')
grid_pq = frac('0', '1', '-1', '1/2', '-1/3', '2', '1/10')
n_grid = 0
for b1g, b2g in product(grid_b, repeat=2):
    B1g, B2g = balances(D, b1g, b2g)
    base = SS(x, s, r, b1g, b2g)
    for p, q in product(grid_pq, repeat=2):
        lhs = SS(x, s, r, b1g + p, b2g + q)
        rhs = base - 2 * p * B1g - 2 * q * B2g + Qform(D, p, q)
        if lhs != rhs:
            sys.exit(f"NUDGE IDENTITY FAILED at b=({b1g},{b2g}) step=({p},{q})")
        n_grid += 1
CHECKS[0] += 1
print(f"   [OK ] two-column nudge identity exact on {n_grid} (b1,b2,p,q) combinations")

print()
print("   Two one-dial corollaries (set q=0, then p=0):")
print("     q=0 :  SS(b1+p, b2) - SS = -2p*B1 + p^2*Sxx   -> best p = B1/Sxx, gain B1^2/Sxx")
print("     p=0 :  SS(b1, b2+q) - SS = -2q*B2 + q^2*Sss   -> best q = B2/Sss, gain B2^2/Sss")

# demonstrated at the cheapness-only fit (b1, b2) = (2, 0)
B1_20, B2_20 = balances(D, F(2), F(0))
check("at (2,0): B1 = Sum x*e", B1_20, F(0))
check("at (2,0): B2 = Sum s*e", B2_20, F(4))
best_q = B2_20 / D["Sss"]
check("best single q from (2,0) = B2/Sss", best_q, F(2, 5))
check("gain from that step = B2^2/Sss", B2_20 ** 2 / D["Sss"], F(8, 5))
check("SS(2,0)", SS(x, s, r, F(2), F(0)), F(13, 2))
check("SS(2,2/5)", SS(x, s, r, F(2), F(2, 5)), F(49, 10))
check("SS(2,0) - SS(2,2/5) equals the gain", F(13, 2) - F(49, 10), F(8, 5))

# ============================================================================
# SECTION 3 -- the two balance conditions ARE the two normal equations
# ============================================================================
head("SECTION 3  Two balance conditions -> two normal equations")

print("   B1 = Sum x*e = Sxr - b1*Sxx - b2*Sxs = 0   ->   Sxx b1 + Sxs b2 = Sxr")
print("   B2 = Sum s*e = Ssr - b1*Sxs - b2*Sss = 0   ->   Sxs b1 + Sss b2 = Ssr")
print()
print(f"   (1)   {S(D['Sxx'])} b1 + ({S(D['Sxs'])}) b2 = {S(D['Sxr'])}")
print(f"   (2)  ({S(D['Sxs'])}) b1 + {S(D['Sss'])} b2 = {S(D['Ssr'])}")

# elimination, exactly as done by hand in the markdown
lhs1 = [D["Sxx"] * 2, D["Sxs"] * 2, D["Sxr"] * 2]
check("(1) x 2  ->  coefficient of b1", lhs1[0], F(15))
check("(1) x 2  ->  coefficient of b2", lhs1[1], F(-10))
check("(1) x 2  ->  right-hand side", lhs1[2], F(30))
add = [lhs1[0] + D["Sxs"], lhs1[1] + D["Sss"], lhs1[2] + D["Ssr"]]
check("add (2): b1 coefficient", add[0], F(10))
check("add (2): b2 coefficient (must vanish)", add[1], F(0))
check("add (2): right-hand side", add[2], F(24))
b1_hand = add[2] / add[0]
check("b1 by elimination", b1_hand, F(12, 5))
b2_hand = (D["Ssr"] - D["Sxs"] * b1_hand) / D["Sss"]
check("b2 by back-substitution into (2)", b2_hand, F(3, 5))

b1, b2, det = solve2(D)
check("b1 by Cramer", b1, F(12, 5))
check("b2 by Cramer", b2, F(3, 5))
check("elimination and Cramer agree on b1", b1_hand, b1)
check("elimination and Cramer agree on b2", b2_hand, b2)
check("determinant Sxx*Sss - Sxs^2", det, F(50))
show("b1", b1)
show("b2", b2)

print()
print("   Neither condition alone pins anything down: each is a LINE of (b1,b2) pairs.")
print("   L1 (cheapness plank level):  15/2 b1 - 5 b2 = 15   ->  b1 = 2 + (2/3) b2")
print("   L2 (size plank level):        -5 b1 + 10 b2 = -6   ->  b2 = -3/5 + (1/2) b1")
for pt in [(F(2), F(0)), (F(12, 5), F(3, 5)), (F(4), F(3)), (F(8, 3), F(1))]:
    check(f"L1 contains {S(pt)}", balances(D, *pt)[0], F(0))
for pt in [(F(0), F(-3, 5)), (F(2), F(2, 5)), (F(12, 5), F(3, 5)), (F(4), F(7, 5))]:
    check(f"L2 contains {S(pt)}", balances(D, *pt)[1], F(0))
check("the two lines meet only at the joint solve",
      [t for t in [(F(2), F(0)), (F(0), F(-3, 5)), (F(4), F(3)), (F(12, 5), F(3, 5))]
       if balances(D, *t) == (F(0), F(0))], [(F(12, 5), F(3, 5))])
print("   Perpendicularity test: normals (Sxx, Sxs) and (Sxs, Sss); dot = Sxs*(Sxx+Sss)")
check("derivation data: normals dot product (NOT zero)",
      D["Sxs"] * (D["Sxx"] + D["Sss"]), F(-175, 2))
print("   L1 is vertical (b1 fixed regardless of b2) exactly when Sxs = 0; here Sxs = -5,")
print("   so moving b2 tips the cheapness plank straight back off level.")

# ============================================================================
# SECTION 4 -- the fit, its residuals, and both planks level
# ============================================================================
head("SECTION 4  The joint fit and its residuals")

fit = [b1 * xi + b2 * si for xi, si in zip(x, s)]
check("fitted values", fit, frac('-3', '-9/5', '6/5', '12/5', '18/5'))
e = resid(x, s, r, b1, b2)
check("residuals e", e, frac('1', '-1/5', '-7/10', '8/5', '-1/10'))
check("CHECK 1  Sum x*e", dot(x, e), F(0))
check("CHECK 2  Sum s*e", dot(s, e), F(0))
check("Sum e  (NOT forced to zero -- no column of ones)", sum(e), F(8, 5))
check("Sum e^2", sum(ei * ei for ei in e), F(41, 10))
check("Sum e^2 from the sums only (Srr - b1*Sxr - b2*Ssr)",
      D["Srr"] - b1 * D["Sxr"] - b2 * D["Ssr"], F(41, 10))
check("SS_expanded agrees", SS_expanded(D, b1, b2), F(41, 10))
show("Sum e", sum(e))
show("Sum e^2", sum(ei * ei for ei in e))

print("   per-stock turning forces:")
print("     x*e =", S([xi * ei for xi, ei in zip(x, e)]))
print("     s*e =", S([si * ei for si, ei in zip(s, e)]))

# ============================================================================
# SECTION 5 -- uniqueness: completing the square, and the determinant
# ============================================================================
head("SECTION 5  Uniqueness -- completing the square")

print("   Q(p,q) = Sum (p*x + q*s)^2 = p^2*Sxx + 2pq*Sxs + q^2*Sss")
n_q = 0
for p, q in product(frac('0', '1', '-1', '1/2', '-2/3', '3', '-1/4'), repeat=2):
    lhs = sum((p * xi + q * si) ** 2 for xi, si in zip(x, s))
    if lhs != Qform(D, p, q):
        sys.exit(f"Q-form mismatch at (p,q)=({p},{q})")
    n_q += 1
CHECKS[0] += 1
print(f"   [OK ] Q(p,q) = Sum (px+qs)^2 exact on {n_q} (p,q) pairs")

print("   completed square:  Q = Sxx*(p + (Sxs/Sxx) q)^2 + (det/Sxx)*q^2")
coef = D["Sxs"] / D["Sxx"]
check("Sxs/Sxx", coef, F(-2, 3))
check("det/Sxx", det / D["Sxx"], F(20, 3))
n_c = 0
for p, q in product(frac('0', '1', '-1', '1/2', '-2/3', '3', '-1/4'), repeat=2):
    lhs = Qform(D, p, q)
    rhs = D["Sxx"] * (p + coef * q) ** 2 + (det / D["Sxx"]) * q ** 2
    if lhs != rhs:
        sys.exit(f"completed square mismatch at (p,q)=({p},{q})")
    n_c += 1
CHECKS[0] += 1
print(f"   [OK ] completed-square form exact on {n_c} (p,q) pairs")
print("   det = 50 > 0, so Q(p,q) = 0 only when q = 0 and then p = 0: the minimum is unique.")

print()
print("   PENALTY FORM:  SS(b1*+d1, b2*+d2) - SS* = Q(d1, d2)")
n_p = 0
for d1, d2 in product(frac('0', '1', '-1', '1/2', '-2/5', '-1/5', '3'), repeat=2):
    lhs = SS(x, s, r, b1 + d1, b2 + d2) - SS(x, s, r, b1, b2)
    if lhs != Qform(D, d1, d2):
        sys.exit(f"penalty form mismatch at (d1,d2)=({d1},{d2})")
    n_p += 1
CHECKS[0] += 1
print(f"   [OK ] penalty form exact on {n_p} (d1,d2) pairs")

# ============================================================================
# SECTION 6 -- what each way of getting b1 and b2 actually returns
# ============================================================================
head("SECTION 6  Derivation dataset: the answers each method returns")

b1_uni = D["Sxr"] / D["Sxx"]
b2_uni = D["Ssr"] / D["Sss"]
check("cheapness alone (size column ignored)", b1_uni, F(2))
check("size alone (cheapness column ignored)", b2_uni, F(-3, 5))
check("joint b1", b1, F(12, 5))
check("joint b2", b2, F(3, 5))
check("b2 alone is the exact negative of joint b2", b2_uni, -b2)
check("b1 moved by joint b1 - univariate b1", b1 - b1_uni, F(2, 5))
check("b1 moved by, as a fraction of the univariate value", (b1 - b1_uni) / b1_uni, F(1, 5))

rows6 = [
    ("joint solve (both conditions at once)", b1, b2),
    ("cheapness alone, size dropped", b1_uni, F(0)),
    ("size alone, cheapness dropped", F(0), b2_uni),
    ("two separate one-column fits, both used", b1_uni, b2_uni),
    ("one pass of the chase (cheapness, then size)", F(2), F(2, 5)),
    ("give up: predict zero for everyone", F(0), F(0)),
]
SS_star = SS(x, s, r, b1, b2)
print()
print("   method                                        b1        b2        SS       SS/SS*")
for lbl, u, v in rows6:
    val = SS(x, s, r, u, v)
    CHECKS[0] += 1
    if val != SS_expanded(D, u, v):
        sys.exit(f"SS route disagreement for {lbl}")
    print(f"   {lbl:<44} {dec(u):>8} {dec(v):>9} {dec(val):>9} {dec(val / SS_star):>8}")
check("SS at the joint solve", SS_star, F(41, 10))
check("SS cheapness alone", SS(x, s, r, b1_uni, F(0)), F(13, 2))
check("SS size alone", SS(x, s, r, F(0), b2_uni), F(329, 10))
check("SS two separate one-column fits", SS(x, s, r, b1_uni, b2_uni), F(149, 10))
check("SS one pass of the chase", SS(x, s, r, F(2), F(2, 5)), F(49, 10))
check("SS predict zero = Srr", SS(x, s, r, F(0), F(0)), F(73, 2))
check("two separate fits are WORSE than cheapness alone",
      SS(x, s, r, b1_uni, b2_uni) > SS(x, s, r, b1_uni, F(0)), True)
check("penalty of the one-pass answer, Q(-2/5,-1/5)", Qform(D, F(-2, 5), F(-1, 5)), F(4, 5))
check("...and it equals SS(2,2/5) - SS*", F(49, 10) - F(41, 10), F(4, 5))
check("relative error of the one-pass b1 = (2 - 12/5)/(12/5)", (F(2) - b1) / b1, F(-1, 6))
check("relative error of the one-pass b2 = (2/5 - 3/5)/(3/5)  [= -rho^2, Section 7]",
      (F(2, 5) - b2) / b2, F(-1, 3))
print("   SS ratios against the joint solve, exactly:")
for lbl, u, v in rows6:
    show(f"SS/SS*  [{lbl}]", SS(x, s, r, u, v) / SS_star)

# ============================================================================
# SECTION 7 -- the one-at-a-time chase on the derivation data
# ============================================================================
head("SECTION 7  The chase: one condition at a time never lands in one pass")

rho2 = D["Sxs"] ** 2 / (D["Sxx"] * D["Sss"])
check("rho^2 = Sxs^2 / (Sxx*Sss)", rho2, F(1, 3))
check("1 - rho^2 = det/(Sxx*Sss)", 1 - rho2, det / (D["Sxx"] * D["Sss"]))

print()
print("   state (b1,b2)          Sum x*e     Sum s*e          SS")
seq = backfit(D, 4)
# alternate: start at (2,0), then after each size step, then after each cheapness step
states = []
b2c = F(0)
for _ in range(4):
    b1c = (D["Sxr"] - b2c * D["Sxs"]) / D["Sxx"]
    if (b1c, b2c) not in states:
        states.append((b1c, b2c))
    b2c = (D["Ssr"] - b1c * D["Sxs"]) / D["Sss"]
    if (b1c, b2c) not in states:
        states.append((b1c, b2c))
states.append((b1, b2))
for (u, v) in states:
    B1s, B2s = balances(D, u, v)
    CHECKS[0] += 1
    ev = resid(x, s, r, u, v)
    if (dot(x, ev), dot(s, ev)) != (B1s, B2s):
        sys.exit("balance route disagreement")
    print(f"   ({S(u):>7}, {S(v):>6})  {S(B1s):>9}  {S(B2s):>10}   {S(SS(x, s, r, u, v)):>9}"
          f"  = {dec(SS(x, s, r, u, v))}")

check("pass 1 lands on b1", F(2), F(2))
check("pass 1 lands on b2", F(2, 5), F(2, 5))
check("pass 2 b1", seq[1][1][0], F(34, 15))
check("pass 2 b2", seq[1][1][1], F(8, 15))
check("pass 3 b1", seq[2][1][0], F(106, 45))
check("pass 3 b2", seq[2][1][1], F(26, 45))
check("pass 4 b1", seq[3][1][0], F(322, 135))
check("pass 4 b2", seq[3][1][1], F(16, 27))
check("truth b1 as /135", b1, F(324, 135))
check("truth b2 as /135", b2, F(81, 135))

print()
print("   error in b2 after each pass, and the ratio between consecutive errors:")
prev = None
for i, (_, end) in enumerate(seq, start=1):
    d2 = end[1] - b2
    line = f"     pass {i}: b2 = {S(end[1]):>9} = {dec(end[1])}   error {S(d2):>9} = {dec(d2)}"
    if prev is not None:
        ratio = d2 / prev
        CHECKS[0] += 1
        if ratio != rho2:
            sys.exit(f"contraction ratio not rho^2 at pass {i}: {ratio}")
        line += f"   ratio {S(ratio)}"
    prev = d2
    print(line)
CHECKS[0] += 1
print("   [OK ] every consecutive error ratio equals rho^2 = 1/3 exactly")

print()
print("   the two error recursions, checked step by step:")
print("     after a cheapness step:  d1 <- -(Sxs/Sxx)*d2")
print("     after a size step:       d2 <- -(Sxs/Sss)*d1  =  k*d2")
b2c = F(0)
for i in range(1, 5):
    d2_before = b2c - b2
    b1c = (D["Sxr"] - b2c * D["Sxs"]) / D["Sxx"]
    check(f"   pass {i}: d1 = -(Sxs/Sxx)*d2_before",
          b1c - b1, -(D["Sxs"] / D["Sxx"]) * d2_before)
    b2c = (D["Ssr"] - b1c * D["Sxs"]) / D["Sss"]
    check(f"   pass {i}: d2 = -(Sxs/Sss)*d1",
          b2c - b2, -(D["Sxs"] / D["Sss"]) * (b1c - b1))
check("derivation: passes to bring b2 within 1%", passes_to_1pc(rho2), 5)
show("(1/3)^5", rho2 ** 5, 6)

print()
print("   the imbalance being knocked from one plank into the other:")
print("     after a cheapness step, Sum x*e = 0 and Sum s*e = 4, 4/3, 4/9, 4/27, ...")
print("     after a size step,      Sum s*e = 0 and Sum x*e = 2, 2/3, 2/9, 2/27, ...")
b2c = F(0)
sx_after_s, ss_after_x = [], []
for _ in range(4):
    b1c = (D["Sxr"] - b2c * D["Sxs"]) / D["Sxx"]
    check("   after a cheapness step, Sum x*e", balances(D, b1c, b2c)[0], F(0))
    ss_after_x.append(balances(D, b1c, b2c)[1])
    b2c = (D["Ssr"] - b1c * D["Sxs"]) / D["Sss"]
    check("   after a size step,      Sum s*e", balances(D, b1c, b2c)[1], F(0))
    sx_after_s.append(balances(D, b1c, b2c)[0])
check("Sum s*e after each cheapness step", ss_after_x, frac('4', '4/3', '4/9', '4/27'))
check("Sum x*e after each size step", sx_after_s, frac('2', '2/3', '2/9', '2/27'))

# ============================================================================
# SECTION 8 -- the case where one pass IS exact: Sxs = 0
# ============================================================================
head("SECTION 8  When the columns do not interfere, one pass is exact")

m2 = frac('1', '1', '1', '1', '1')                     # Level 2 boss: market column
x2 = frac('-2', '-1', '0', '1', '2')                   # Level 2 boss: cheapness
r2 = frac('-5/2', '-9/2', '5/2', '7/2', '7/2')         # Level 2 boss: returns
D2 = sums(m2, x2, r2)
check("Level 2 boss: Sum m^2 (= number of stocks)", D2["Sxx"], F(5))
check("Level 2 boss: Sum m*r (= Sum r)", D2["Sxr"], F(5, 2))
check("Level 2 boss: Sum x^2", D2["Sss"], F(10))
check("Level 2 boss: Sum x*r", D2["Ssr"], F(20))
check("Level 2 boss: Sum m*x (the interference term)", D2["Sxs"], F(0))
a2, c2, det2 = solve2(D2)
check("Level 2 boss: a (market)", a2, F(1, 2))
check("Level 2 boss: b (cheapness)", c2, F(2))
check("Level 2 boss: a from the one-column formula Sum r / n", D2["Sxr"] / D2["Sxx"], F(1, 2))
check("Level 2 boss: b from the one-column formula Sxr/Sxx", D2["Ssr"] / D2["Sss"], F(2))
bf2 = backfit(D2, 1)
check("Level 2 boss: one pass reaches the joint answer exactly", bf2[0][1], (a2, c2))
check("Level 2 boss: rho^2 = 0", D2["Sxs"] ** 2 / (D2["Sxx"] * D2["Sss"]), F(0))
check("Level 2 boss: residuals", resid(m2, x2, r2, a2, c2), frac('1', '-3', '2', '1', '-1'))
check("Level 2 boss: Sum e^2", SS(m2, x2, r2, a2, c2), F(16))
print("   Sxs = 0  =>  the two normal-equation lines are perpendicular")
print("   normal vectors (Sxx, Sxs) and (Sxs, Sss); their dot product is Sxs*(Sxx + Sss)")
check("perpendicularity test on Level 2 boss data",
      D2["Sxx"] * D2["Sxs"] + D2["Sxs"] * D2["Sss"], F(0))
check("same test on the Level 3 derivation data (NOT zero)",
      D["Sxx"] * D["Sxs"] + D["Sxs"] * D["Sss"], F(-175, 2))

# ============================================================================
# SECTION 9 -- BOSS ROUND data
# ============================================================================
head("SECTION 9  BOSS ROUND -- a new month, two columns, solve by hand")

xb = frac('-2', '-1', '0', '1', '2')
sb = frac('0', '-1', '-1', '1', '2')
rb = frac('-2', '-2', '3', '2', '2')

print("   stock :   x     s     r      x*x   s*s   x*s   x*r   s*r")
for n_, xi, si, ri in zip(names, xb, sb, rb):
    print(f"   {n_}   : {S(xi):>5} {S(si):>5} {S(ri):>5}"
          f"   {S(xi * xi):>3}   {S(si * si):>3}   {S(xi * si):>3}"
          f"   {S(xi * ri):>3}   {S(si * ri):>3}")

B = sums(xb, sb, rb)
check("Sum x", B["Sx"], F(0))
check("Sum s", B["Ss"], F(1))
check("Sum r", B["Sr"], F(3))
check("Sum x^2", B["Sxx"], F(10))
check("Sum s^2", B["Sss"], F(7))
check("Sum x*s", B["Sxs"], F(6))
check("Sum x*r", B["Sxr"], F(12))
check("Sum s*r", B["Ssr"], F(5))
check("Sum r^2", B["Srr"], F(25))

# ============================================================================
# SECTION 10 -- boss solve, both elimination routes
# ============================================================================
head("SECTION 10  BOSS ROUND -- the solve, in fractions")

print("   (1)  10 b1 + 6 b2 = 12")
print("   (2)   6 b1 + 7 b2 =  5")
print()
print("   Route A: kill b1.  (1)x3 -> 30 b1 + 18 b2 = 36 ;  (2)x5 -> 30 b1 + 35 b2 = 25")
check("Route A  (1)x3 b2-coefficient", B["Sxs"] * 3, F(18))
check("Route A  (1)x3 rhs", B["Sxr"] * 3, F(36))
check("Route A  (2)x5 b2-coefficient", B["Sss"] * 5, F(35))
check("Route A  (2)x5 rhs", B["Ssr"] * 5, F(25))
check("Route A  subtract: b2 coefficient", B["Sss"] * 5 - B["Sxs"] * 3, F(17))
check("Route A  subtract: rhs", B["Ssr"] * 5 - B["Sxr"] * 3, F(-11))
b2_A = (B["Ssr"] * 5 - B["Sxr"] * 3) / (B["Sss"] * 5 - B["Sxs"] * 3)
check("Route A  b2", b2_A, F(-11, 17))
check("Route A  back into (1): 6*b2 = ", B["Sxs"] * b2_A, F(-66, 17))
check("Route A  back into (1): 10*b1 = 12 + 66/17", B["Sxr"] - B["Sxs"] * b2_A, F(270, 17))
b1_A = (B["Sxr"] - B["Sxs"] * b2_A) / B["Sxx"]
check("Route A  b1 by back-substitution into (1)", b1_A, F(27, 17))

print()
print("   Route B: kill b2.  (1)x7 -> 70 b1 + 42 b2 = 84 ;  (2)x6 -> 36 b1 + 42 b2 = 30")
check("Route B  (1)x7 b1-coefficient", B["Sxx"] * 7, F(70))
check("Route B  (2)x6 b1-coefficient", B["Sxs"] * 6, F(36))
check("Route B  subtract: b1 coefficient (= the determinant)",
      B["Sxx"] * 7 - B["Sxs"] * 6, F(34))
check("Route B  subtract: rhs", B["Sxr"] * 7 - B["Ssr"] * 6, F(54))
b1_B = (B["Sxr"] * 7 - B["Ssr"] * 6) / (B["Sxx"] * 7 - B["Sxs"] * 6)
check("Route B  b1", b1_B, F(27, 17))
check("Route B  (1)x7 rhs", B["Sxr"] * 7, F(84))
check("Route B  (2)x6 rhs", B["Ssr"] * 6, F(30))
check("Route B  back into (2): 6*b1 = ", B["Sxs"] * b1_B, F(162, 17))
check("Route B  back into (2): 7*b2 = 5 - 162/17", B["Ssr"] - B["Sxs"] * b1_B, F(-77, 17))
b2_B = (B["Ssr"] - B["Sxs"] * b1_B) / B["Sss"]
check("Route B  b2 by back-substitution into (2)", b2_B, F(-11, 17))

bb1, bb2, detb = solve2(B)
check("Cramer b1", bb1, F(27, 17))
check("Cramer b2", bb2, F(-11, 17))
check("determinant", detb, F(34))
check("all three routes agree", (b1_A, b2_A, b1_B, b2_B), (bb1, bb2, bb1, bb2))
show("b1", bb1)
show("b2", bb2)
check("Cramer numerator for b1 (Sxr*Sss - Ssr*Sxs)",
      B["Sxr"] * B["Sss"] - B["Ssr"] * B["Sxs"], F(54))
check("Cramer numerator for b2 (Sxx*Ssr - Sxs*Sxr)",
      B["Sxx"] * B["Ssr"] - B["Sxs"] * B["Sxr"], F(-22))
check("54/34 in lowest terms", F(54, 34), F(27, 17))
check("-22/34 in lowest terms", F(-22, 34), F(-11, 17))

# residuals
fb = [bb1 * xi + bb2 * si for xi, si in zip(xb, sb)]
check("fitted values", fb, frac('-54/17', '-16/17', '11/17', '16/17', '32/17'))
eb = resid(xb, sb, rb, bb1, bb2)
check("residuals e", eb, frac('20/17', '-18/17', '40/17', '18/17', '2/17'))
check("CHECK 1  Sum x*e", dot(xb, eb), F(0))
check("CHECK 2  Sum s*e", dot(sb, eb), F(0))
check("Sum e (not forced to zero)", sum(eb), F(62, 17))
check("Sum e^2", sum(ei * ei for ei in eb), F(156, 17))
check("Sum e^2 as 2652/289 before reducing", F(2652, 289), F(156, 17))
check("Sum e^2 numerator 400+324+1600+324+4", 400 + 324 + 1600 + 324 + 4, 2652)
check("Sum e^2 from the sums (Srr - b1*Sxr - b2*Ssr)",
      B["Srr"] - bb1 * B["Sxr"] - bb2 * B["Ssr"], F(156, 17))
check("...via 25 - 324/17 + 55/17 = 25 - 269/17", F(25) - F(269, 17), F(156, 17))
show("Sum e", sum(eb))
show("Sum e^2", sum(ei * ei for ei in eb))
print("   per-stock turning forces:")
print("     x*e =", S([xi * ei for xi, ei in zip(xb, eb)]))
print("     s*e =", S([si * ei for si, ei in zip(sb, eb)]))
check("Sum of x*e terms", sum(xi * ei for xi, ei in zip(xb, eb)), F(0))
check("Sum of s*e terms", sum(si * ei for si, ei in zip(sb, eb)), F(0))

# ============================================================================
# SECTION 11 -- boss round: every wrong method, priced
# ============================================================================
head("SECTION 11  BOSS ROUND -- the wrong methods, and what each returns")

b1u = B["Sxr"] / B["Sxx"]
b2u = B["Ssr"] / B["Sss"]
check("cheapness alone", b1u, F(6, 5))
check("size alone", b2u, F(5, 7))
check("size alone has the OPPOSITE SIGN to the joint answer",
      (b2u > 0, bb2 < 0), (True, True))
onepass = backfit(B, 1)[0][1]
check("one pass of the chase: b1", onepass[0], F(6, 5))
check("one pass of the chase: b2", onepass[1], F(-11, 35))

SSb_star = SS(xb, sb, rb, bb1, bb2)
rows11 = [
    ("joint solve -- both conditions at once", bb1, bb2, F(156, 17)),
    ("one pass of the chase (cheapness then size)", onepass[0], onepass[1], F(1734, 175)),
    ("cheapness alone, size column dropped", b1u, F(0), F(53, 5)),
    ("two separate one-column fits, both reported", b1u, b2u, F(606, 35)),
    ("size alone, cheapness column dropped", F(0), b2u, F(150, 7)),
    ("give up: predict zero for everyone", F(0), F(0), F(25)),
]
print()
print("   method                                          b1        b2         SS      SS/SS*   penalty")
for lbl, u, v, want in rows11:
    val = SS(xb, sb, rb, u, v)
    check(f"SS[{lbl}]", val, want)
    CHECKS[0] += 1
    if val != SS_expanded(B, u, v):
        sys.exit(f"SS route disagreement for {lbl}")
    pen = Qform(B, u - bb1, v - bb2)
    CHECKS[0] += 1
    if pen != val - SSb_star:
        sys.exit(f"penalty form failed for {lbl}")
    print(f"   {lbl:<44} {dec(u):>8} {dec(v):>9} {dec(val):>10} {dec(val / SSb_star):>8}"
          f"  {dec(pen):>8}")

check("penalty, cheapness alone", F(53, 5) - F(156, 17), F(121, 85))
check("penalty, one pass", F(1734, 175) - F(156, 17), F(2178, 2975))
check("penalty, two separate fits", F(606, 35) - F(156, 17), F(4842, 595))
check("penalty, size alone", F(150, 7) - F(156, 17), F(1458, 119))
check("penalty, predict zero", F(25) - F(156, 17), F(269, 17))
check("two separate fits are WORSE than using cheapness alone",
      F(606, 35) > F(53, 5), True)
check("...by how much: (606/35) / (53/5)", F(606, 35) / F(53, 5), F(606, 371))
show("two separate fits vs dropping the size column", F(606, 35) / F(53, 5))
print("   what a desk would publish, rounded to the nearest 0.01%:")
show("   size factor return, columns fitted separately", b2u, 2)
show("   size factor return, columns fitted jointly", bb2, 2)
show("SS ratio, two separate fits", F(606, 35) / F(156, 17))
show("SS ratio, one pass", F(1734, 175) / F(156, 17))
show("SS ratio, cheapness alone", F(53, 5) / F(156, 17))
show("SS ratio, size alone", F(150, 7) / F(156, 17))
show("SS ratio, predict zero", F(25) / F(156, 17))

print()
print("   The two sign-flips are NOT the same shape -- do not let the player over-learn:")
check("derivation: size-alone b2 is the exact negative of the joint b2", b2_uni, -b2)
check("boss: size-alone b2 magnitude", b2u, F(5, 7))
check("boss: joint b2 magnitude", -bb2, F(11, 17))
check("boss: the two magnitudes are NOT equal", b2u != -bb2, True)
check("boss: |size-alone b2| - |joint b2|", b2u - (-bb2), F(8, 119))
show("boss: |size-alone b2| - |joint b2|", b2u - (-bb2))

print()
print("   How wrong is the one-pass SIZE number, which is what a risk model actually reports?")
check("one-pass b2 / true b2", onepass[1] / bb2, F(17, 35))
show("one-pass b2 / true b2", onepass[1] / bb2)
check("true b2 / one-pass b2", bb2 / onepass[1], F(35, 17))
show("true b2 / one-pass b2", bb2 / onepass[1])
check("relative error of the one-pass b2 = rho^2",
      (onepass[1] - bb2) / abs(bb2), B["Sxs"] ** 2 / (B["Sxx"] * B["Sss"]))
check("relative error of the one-pass b1", (onepass[0] - bb1) / bb1, F(-11, 45))
show("relative error of the one-pass b1", (onepass[0] - bb1) / bb1)

# ============================================================================
# SECTION 12 -- boss round: the chase, pass by pass
# ============================================================================
head("SECTION 12  BOSS ROUND -- the chase, pass by pass")

rho2b = B["Sxs"] ** 2 / (B["Sxx"] * B["Sss"])
check("rho^2 = Sxs^2/(Sxx*Sss)", rho2b, F(18, 35))
check("1 - rho^2 = det/(Sxx*Sss)", 1 - rho2b, F(17, 35))
show("rho^2", rho2b)

seqb = backfit(B, 5)
print()
print("   pass    b1                       b2                       Sum x*e   Sum s*e      SS")
prev = None
for i, (mid, end) in enumerate(seqb, start=1):
    Bx, Bs = balances(B, *end)
    check(f"pass {i}: after the size step, Sum s*e", Bs, F(0))
    print(f"    {i}    {S(end[0]):>22} {S(end[1]):>24}  {S(Bx):>8}  {S(Bs):>7}"
          f"   {dec(SS(xb, sb, rb, *end))}")
    print(f"         = {dec(end[0], 6)}                = {dec(end[1], 6)}")
    d2 = end[1] - bb2
    if prev is not None:
        CHECKS[0] += 1
        if d2 / prev != rho2b:
            sys.exit(f"boss contraction ratio wrong at pass {i}")
    prev = d2

check("pass 1 b1", seqb[0][1][0], F(6, 5))
check("pass 1 b2", seqb[0][1][1], F(-11, 35))
check("pass 2 b1", seqb[1][1][0], F(243, 175))
check("pass 2 b2", seqb[1][1][1], F(-583, 1225))
check("pass 3 b1", seqb[2][1][0], F(9099, 6125))
check("pass 3 b2", seqb[2][1][1], F(-23969, 42875))
check("pass 4 b1", seqb[3][1][0], F(329157, 214375))
check("pass 4 b2", seqb[3][1][1], F(-903067, 1500625))
check("pass 5 b1", seqb[4][1][0], F(11712951, 7503125))
check("pass 5 b2", seqb[4][1][1], F(-32762081, 52521875))
CHECKS[0] += 1
print("   [OK ] every consecutive b2 error ratio equals rho^2 = 18/35 exactly")

print()
print("   the cheapness imbalance left standing at the end of each pass:")
imb = [balances(B, *end)[0] for _, end in seqb]
check("Sum x*e after passes 1, 2, 3", imb[:3], frac('66/35', '1188/1225', '21384/42875'))
check("ratio of pass-2 imbalance to pass-1", imb[1] / imb[0], rho2b)
check("ratio of pass-3 imbalance to pass-2", imb[2] / imb[1], rho2b)
for i, v in enumerate(imb[:3], start=1):
    show(f"   pass {i}: Sum x*e", v)

print()
print("   relative error of b2 after n passes is exactly (rho^2)^n:")
for n in range(1, 9):
    bn = backfit(B, n)[-1][1][1]
    relerr = abs((bn - bb2) / bb2)
    check(f"   n = {n}: relative error", relerr, rho2b ** n)
    print(f"          = {dec(relerr, 6)}")
n_needed = 1
while rho2b ** n_needed >= F(1, 100):
    n_needed += 1
check("passes needed to bring b2 within 1% of the truth", n_needed, 7)
check("...and 6 passes is not enough", rho2b ** 6 >= F(1, 100), True)
check("...while 7 passes is", rho2b ** 7 < F(1, 100), True)
show("(rho^2)^6", rho2b ** 6, 6)
show("(rho^2)^7", rho2b ** 7, 6)

# ============================================================================
# SECTION 13 -- how correlated are the two columns, really
# ============================================================================
head("SECTION 13  Column-to-column correlation, and the BFRE calibration")


def isqrt_dec(v, n=4):
    """rounded decimal square root of a non-negative Fraction, n places,
    computed by integer square root so no floating point is involved.
    Two guard digits are taken, then the result is rounded half-up."""
    g = n + 2
    scaled = v * 10 ** (2 * g)
    num = scaled.numerator // scaled.denominator
    lo, hi = 0, 1
    while hi * hi <= num:
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= num:
            lo = mid
        else:
            hi = mid - 1
    return dec(F(lo, 10 ** g), n)


check("derivation: rho^2", rho2, F(1, 3))
print(f"        derivation |rho| = sqrt(1/3) = {isqrt_dec(rho2)} (rounded)")
check("boss: rho^2", rho2b, F(18, 35))
print(f"        boss       |rho| = sqrt(18/35) = {isqrt_dec(rho2b)} (rounded)")

# centred version of the boss size column (Level 5 preview)
sbar = B["Ss"] / 5
sc = [si - sbar for si in sb]
check("boss: mean of s", sbar, F(1, 5))
check("boss: centred s", sc, frac('-1/5', '-6/5', '-6/5', '4/5', '9/5'))
check("boss: Sum x*s_centred (Sum x = 0, so unchanged)", dot(xb, sc), F(6))
check("boss: Sum s_centred^2", dot(sc, sc), F(34, 5))
rho2_c = dot(xb, sc) ** 2 / (B["Sxx"] * dot(sc, sc))
check("boss: centred rho^2", rho2_c, F(9, 17))
print(f"        boss centred |rho| = sqrt(9/17) = {isqrt_dec(rho2_c)} (rounded)")

print()
print("   BFRE Figure 1.3 (p.11, NAMR Dec 2013) off-diagonal exposure correlations, as")
print("   transcribed in notes/chunk_10-18.md -- the real numbers this level is calibrated against:")
fig13 = [("Size-Liquidity", F(74, 100)), ("Earnings Yield-Profitability", F(64, 100)),
         ("Volatility-Dividend Yield", F(-46, 100)), ("Size-Volatility", F(-36, 100)),
         ("Size-Value", F(0, 100))]
for lbl, v in fig13:
    print(f"        {lbl:<30} rho = {dec(v, 2)}   rho^2 = {dec(v * v, 4)}")
check("Size-Liquidity rho^2", F(74, 100) ** 2, F(1369, 2500))
check("boss rho^2 sits just below the paper's worst measured pair",
      rho2b < F(74, 100) ** 2, True)
check("Size-Value rho^2 is exactly zero -> one pass would be exact there",
      F(0, 100) ** 2, F(0))

print()
print("   passes of the chase needed to get within 1% at each of those real correlations:")
for lbl, v in fig13:
    check(f"   {lbl}: passes", passes_to_1pc(v * v),
          {"Size-Liquidity": 8, "Earnings Yield-Profitability": 6,
           "Volatility-Dividend Yield": 3, "Size-Volatility": 3, "Size-Value": 1}[lbl])

# ============================================================================
# SECTION 14 -- the exact-collision end of the scale (Level 4's door)
# ============================================================================
head("SECTION 14  The determinant going to zero -- a look through Level 4's door")

print("   Keep x fixed; slide s toward a multiple of x and watch det collapse.")
print("   s(t) = (1-t)*s + t*(3/2)*x   on the DERIVATION data, t = 0 .. 1")
print()
print("       t          Sum x*s(t)          det                     rho^2")

for t in frac('0', '1/4', '4/13', '1/2', '3/4', '9/10', '99/100', '1'):
    st = [(1 - t) * si + t * F(3, 2) * xi for xi, si in zip(x, s)]
    Dt = sums(x, st, r)
    dt = Dt["Sxx"] * Dt["Sss"] - Dt["Sxs"] ** 2
    rt = Dt["Sxs"] ** 2 / (Dt["Sxx"] * Dt["Sss"])
    print(f"     {S(t):>7}   {S(Dt['Sxs']):>12}   {S(dt):>14} = {dec(dt, 4):>9}"
          f"   {dec(rt, 6):>9}")
    if t == 0:
        check("t = 0 is the level's own data: Sum x*s", Dt["Sxs"], F(-5))
        check("t = 0: det", dt, F(50))
        check("t = 0: rho^2", rt, F(1, 3))
    if t == F(1, 4):
        check("t = 1/4: Sum x*s", Dt["Sxs"], F(-15, 16))
        check("t = 1/4: det", dt, F(225, 8))
    if t == F(4, 13):
        check("t = 4/13: the interference term hits exactly zero", Dt["Sxs"], F(0))
        check("t = 4/13: rho^2", rt, F(0))
        check("t = 4/13: det = Sxx*Sss, its largest possible value",
              dt, Dt["Sxx"] * Dt["Sss"])
    if t == F(1, 2):
        check("t = 1/2: Sum x*s", Dt["Sxs"], F(25, 8))
        check("t = 1/2: det", dt, F(25, 2))
    if t == F(3, 4):
        check("t = 3/4: Sum x*s", Dt["Sxs"], F(115, 16))
        check("t = 3/4: det", dt, F(25, 8))
    if t == F(9, 10):
        check("t = 9/10: det still strictly positive", dt > 0, True)
        check("t = 9/10: Sum x*s", Dt["Sxs"], F(77, 8))
        check("t = 9/10: det", dt, F(1, 2))
    if t == F(99, 100):
        check("t = 99/100: Sum x*s", Dt["Sxs"], F(887, 80))
        check("t = 99/100: det", dt, F(1, 200))
    if t == 1:
        check("t = 1: Sum x*s", Dt["Sxs"], F(45, 4))
        check("t = 1: the columns are exactly proportional, det", dt, F(0))
        check("t = 1: rho^2", rt, F(1))
        check("t = 1: s(1) really is (3/2)*x", st, [F(3, 2) * xi for xi in x])

print()
print("   passes needed to bring the second dial within 1%, at three interference levels:")


check("rho^2 = 0    (columns do not interfere): passes", 1, 1)
check("rho^2 = 1/3  (this level's derivation data): passes", passes_to_1pc(F(1, 3)), 5)
check("rho^2 = 18/35 (this level's boss data): passes", passes_to_1pc(F(18, 35)), 7)
check("rho^2 = 0.74^2 (BFRE's worst measured pair): passes",
      passes_to_1pc(F(74, 100) ** 2), 8)
print("   rho^2 = 1    (exact collision): never -- the chase does not converge at all")
print()
print("   Two things to read off that table, and only two:")
print("     * det -> 0 as the second column slides onto the first. At det = 0 the two")
print("       normal-equation lines are parallel and the system stops having one answer.")
print("     * at t = 4/13 the interference vanishes by accident and one pass is exact.")
print("       Both of those are Level 4's material. Do not walk through that door yet.")

# ============================================================================
head(f"ALL DONE -- {CHECKS[0]} exact-rational checks passed")
print()
print("Every value printed above is computed from the raw x, s and r columns in")
print("fractions.Fraction. If any of them disagrees with datasets/level3.md, the")
print("markdown is wrong.")
sys.exit(0)
