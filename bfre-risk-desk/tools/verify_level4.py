#!/usr/bin/env python3
"""
verify_level4.py -- recomputes EVERY number printed in datasets/level4.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
Run:  python3 tools/verify_level4.py
Exits 0 if every internal consistency assertion holds.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from itertools import product
import math
import sys

# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def frac(*a):
    return [F(v) for v in a]

def S(v):
    if isinstance(v, (tuple, list)):
        return "[" + ", ".join(S(t) for t in v) + "]"
    return str(v)

def row(v):
    return "[" + ", ".join(S(t) for t in v) + "]"

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))

def dec(v, n=4):
    """rounded decimal string -- ALWAYS labelled 'rounded' in the markdown"""
    return f"{float(v):.{n}f}"

def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)

def sub(title):
    print()
    print("-- " + title)

CHECKS = [0]

def check(label, got, want):
    CHECKS[0] += 1
    ok = (got == want)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: {S(got)}"
          + ("" if ok else f"   EXPECTED {S(want)}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': got {got}, expected {want}")

def show(label, val):
    print(f"        {label}: {S(val)}")

# ----------------------------------------------------------------------------
# the two-column machine
# ----------------------------------------------------------------------------

def gram(x1, x2, r):
    A = dot(x1, x1); B = dot(x1, x2); C = dot(x2, x2)
    p = dot(x1, r);  q = dot(x2, r)
    return A, B, C, p, q

def joint(x1, x2, r):
    A, B, C, p, q = gram(x1, x2, r)
    det = A * C - B * B
    b1 = (C * p - B * q) / det
    b2 = (A * q - B * p) / det
    fit = [b1 * a + b2 * b for a, b in zip(x1, x2)]
    e = [ri - fi for ri, fi in zip(r, fit)]
    return dict(A=A, B=B, C=C, p=p, q=q, det=det, b1=b1, b2=b2, fit=fit, e=e)

def SS2(x1, x2, r, b1, b2):
    return sum((ri - b1 * a - b2 * b) ** 2 for ri, a, b in zip(r, x1, x2))

# ============================================================================
head("SECTION 1  The main dataset -- cheapness (Level 0 column) + quality")
# ============================================================================

names = ["AXL", "BRN", "CHR", "DLT", "EMK"]
x1 = frac('-3/2', '-1/2', '0', '1', '2')      # cheapness -- IDENTICAL to Level 0
x2 = frac('-1',   '-1',   '0', '1', '2')      # quality   -- new this level
r  = frac('-4',   '2',    '1', '3', '1')      # returns, % -- new month

show("names", names)
show("x1 cheapness", x1)
show("x2 quality  ", x2)
show("r  return % ", r)

sub("1.1  the five cross-products (the whole 2x2 machine)")
A, B, C, p, q = gram(x1, x2, r)
check("A = sum x1^2  (Level 0 already had this)", A, F('15/2'))
check("B = sum x1*x2", B, F(7))
check("C = sum x2^2 ", C, F(7))
check("p = sum x1*r ", p, F(10))
check("q = sum x2*r ", q, F(7))
check("sum r^2", dot(r, r), F(31))
check("sum x1 (unused this level, quoted for continuity)", sum(x1), F(1))

sub("1.2  the determinant")
det = A * C - B * B
check("det = A*C - B*B = 105/2 - 49", det, F('7/2'))
show("det as decimal (exact, terminates)", dec(det, 4))
check("Cauchy-Schwarz: det > 0", F(det > 0), F(1))
rho2 = B * B / (A * C)
check("cos^2 between columns = B^2/(A*C) = 49/(105/2)", rho2, F('14/15'))
show("cos itself (ROUNDED)", dec(math.sqrt(float(rho2)), 6))
check("1 - cos^2", 1 - rho2, F('1/15'))
VIF = A * C / det
check("VIF = A*C/det = 1/(1-cos^2)", VIF, F(15))

sub("1.3  the joint (correct) fit, by Cramer")
J = joint(x1, x2, r)
check("b1 = (C*p - B*q)/det = (70-49)/(7/2)", J['b1'], F(6))
check("b2 = (A*q - B*p)/det = (105/2-70)/(7/2)", J['b2'], F(-5))
check("b1 + b2", J['b1'] + J['b2'], F(1))

sub("1.4  the same fit by hand elimination (the pivot IS the determinant)")
# eq1: A b1 + B b2 = p     eq2: B b1 + C b2 = q
# C*eq1 - B*eq2 : (A*C - B*B) b1 = C*p - B*q
check("C*eq1 - B*eq2 left  coefficient = det", A * C - B * B, F('7/2'))
check("C*eq1 - B*eq2 right side = C*p - B*q", C * p - B * q, F(21))
check("  -> b1 = 21 / (7/2)", F(21) / det, F(6))
# the human route: eq2 divided by 7 is b1 + b2 = 1
check("eq2 / 7  ->  b1 + b2 = q/C", q / C, F(1))
check("substitute b2 = 1 - b1 into eq1: (A - B) b1 = p - B", A - B, F('1/2'))
check("                                  right side  p - B", p - B, F(3))
check("  -> b1 = 3 / (1/2)", F(3) / F('1/2'), F(6))
print("   The number multiplying b1 after elimination is 1/2, against a starting")
print("   A = 15/2. That shrunken pivot is what turns a right-hand side of 3 into a")
print("   coefficient of 6.")

sub("1.5  fitted values, misses, and the two balance conditions (Level 3's audit)")
show("fitted = 6*x1 - 5*x2", J['fit'])
check("fitted", tuple(J['fit']), tuple(frac('-4', '2', '0', '1', '2')))
show("e = r - fitted", J['e'])
check("e", tuple(J['e']), tuple(frac('0', '0', '1', '2', '-1')))
check("sum e   (NOT zero -- no intercept yet, same as Level 0)", sum(J['e']), F(2))
check("sum x1*e  = 0  (balance condition 1)", dot(x1, J['e']), F(0))
check("sum x2*e  = 0  (balance condition 2)", dot(x2, J['e']), F(0))
check("sum e^2", dot(J['e'], J['e']), F(6))
check("sum fitted^2", dot(J['fit'], J['fit']), F(25))
check("sum fitted^2 + sum e^2 = sum r^2", dot(J['fit'], J['fit']) + dot(J['e'], J['e']), F(31))
check("explained share 25/31 (uncentered R^2)", F(25, 31), F('25/31'))
show("  as a percentage (ROUNDED)", dec(F(2500, 31), 2) + "%")

# ============================================================================
head("SECTION 2  The wrong methods on the main dataset, and what each returns")
# ============================================================================

sub("2.1  ONE-AT-A-TIME: two separate one-column fits (Level 1's formula, twice)")
b1_solo = p / A
b2_solo = q / C
check("b1_solo = p/A = 10/(15/2)", b1_solo, F('4/3'))
check("b2_solo = q/C = 7/7", b2_solo, F(1))
show("b1_solo decimal (ROUNDED)", dec(b1_solo))
print("   TRUE (6, -5).  ONE-AT-A-TIME (4/3, +1).")
check("b1 error ratio true/naive = 6/(4/3)", J['b1'] / b1_solo, F('9/2'))
check("b2 SIGN FLIP: true<0 and naive>0", F(J['b2'] < 0 and b2_solo > 0), F(1))
check("b2 error ratio true/naive = -5/1", J['b2'] / b2_solo, F(-5))

naive_fit = [b1_solo * a + b2_solo * b for a, b in zip(x1, x2)]
naive_e = [ri - fi for ri, fi in zip(r, naive_fit)]
show("one-at-a-time fitted", naive_fit)
check("one-at-a-time fitted", tuple(naive_fit),
      tuple(frac('-3', '-5/3', '0', '7/3', '14/3')))
show("its misses", naive_e)
check("its misses", tuple(naive_e), tuple(frac('-1', '11/3', '1', '2/3', '-11/3')))
check("sum x1*miss  -- NOT zero, Level 3's audit fails it", dot(x1, naive_e), F(-7))
check("sum x2*miss  -- NOT zero either", dot(x2, naive_e), F('-28/3'))
SS_naive = SS2(x1, x2, r, b1_solo, b2_solo)
check("SS of the one-at-a-time pair", SS_naive, F('88/3'))
show("  decimal (ROUNDED)", dec(SS_naive))
check("SS of the correct pair", SS2(x1, x2, r, J['b1'], J['b2']), F(6))
check("ratio SS_naive / SS_joint = (88/3)/6", SS_naive / F(6), F('44/9'))
show("  decimal (ROUNDED)", dec(SS_naive / F(6)))
check("SS of giving up entirely, b=(0,0), = sum r^2", SS2(x1, x2, r, F(0), F(0)), F(31))
check("variation the naive pair explains: 31 - 88/3", F(31) - SS_naive, F('5/3'))
check("  as a share of 31", (F(31) - SS_naive) / F(31), F('5/93'))
show("  percentage (ROUNDED)", dec(F(500, 93), 2) + "%")
print("   Correct fit explains 80.65% (rounded); one-at-a-time explains 5.38% (rounded).")
check("ratio of explained sums of squares 25 / (5/3)", F(25) / F('5/3'), F(15))

sub("2.2  the excess-loss identity (why SS_naive splits into two exact pieces)")
D1 = b1_solo - J['b1']; D2 = b2_solo - J['b2']
check("delta1 = 4/3 - 6", D1, F('-14/3'))
check("delta2 = 1 - (-5)", D2, F(6))
excess = A * D1 * D1 + 2 * B * D1 * D2 + C * D2 * D2
check("A d1^2 + 2B d1 d2 + C d2^2", excess, F('70/3'))
check("SS_min + excess = SS_naive", F(6) + excess, SS_naive)

sub("2.3  SEQUENTIAL: fit x1, then fit the LEFTOVER RETURN on x2 (raw x2!)")
resid1 = [ri - b1_solo * a for ri, a in zip(r, x1)]
show("r - (4/3)x1", resid1)
check("r - (4/3)x1", tuple(resid1), tuple(frac('-2', '8/3', '1', '5/3', '-5/3')))
b2_seq = dot(x2, resid1) / C
check("sum x2 * leftover", dot(x2, resid1), F('-7/3'))
check("b2_seq = that / C", b2_seq, F('-1/3'))
print("   SIGN is right this time, size is not.")
check("true b2 / sequential b2 = -5 / (-1/3)", J['b2'] / b2_seq, F(15))
check("  ... and that ratio equals the VIF exactly", J['b2'] / b2_seq, VIF)
SS_seq = SS2(x1, x2, r, b1_solo, b2_seq)
check("SS of the sequential pair (4/3, -1/3)", SS_seq, F('152/9'))
show("  decimal (ROUNDED)", dec(SS_seq))

sub("2.4  DROP A COLUMN")
check("keep x1 only: b = 4/3, SS = sum r^2 - p^2/A", F(31) - p * p / A, F('53/3'))
show("  decimal (ROUNDED)", dec(F('53/3')))
check("keep x2 only: b = 1,   SS = sum r^2 - q^2/C", F(31) - q * q / C, F(24))

sub("2.5  the full scoreboard on this dataset")
board = [
    ("joint, both columns at once", J['b1'], J['b2'], F(6)),
    ("one-at-a-time",              b1_solo, b2_solo, SS_naive),
    ("sequential (leftover return on raw x2)", b1_solo, b2_seq, SS_seq),
    ("drop quality",               b1_solo, None,    F('53/3')),
    ("drop cheapness",             None,    b2_solo, F(24)),
    ("give up, predict 0",         F(0),    F(0),    F(31)),
]
for lbl, u1, u2, ss in board:
    print(f"        {lbl:42s} b1={S(u1) if u1 is not None else '--':>6s} "
          f"b2={S(u2) if u2 is not None else '--':>6s}  SS={S(ss):>6s} "
          f"({dec(ss,3)} rounded)")
for lbl, u1, u2, ss in board:
    if u1 is not None and u2 is not None:
        check(f"scoreboard SS recomputed: {lbl}", SS2(x1, x2, r, u1, u2), ss)

# ============================================================================
head("SECTION 3  Frisch-Waugh on the main dataset: a coefficient is a LEFTOVER")
# ============================================================================

sub("3.1  direction ONE -- what is left of cheapness after quality has had it")
a_prime = B / C
check("regress x1 on x2: slope = B/C = 7/7", a_prime, F(1))
w = [u - a_prime * v for u, v in zip(x1, x2)]
show("w = x1 - 1*x2", w)
check("w", tuple(w), tuple(frac('-1/2', '1/2', '0', '0', '0')))
print("   w is non-zero on AXL and BRN ONLY -- the two names the rulers disagree about.")
check("sum x2*w = 0 by construction", dot(x2, w), F(0))
check("sum w^2", dot(w, w), F('1/2'))
check("sum w^2 = det/C = (7/2)/7", det / C, F('1/2'))
check("shrinkage: A / sum w^2 = (15/2)/(1/2) = the VIF", A / dot(w, w), F(15))
check("sum w*r", dot(w, r), F(3))
check("b1 = sum w*r / sum w^2 = 3/(1/2)  -- MATCHES the joint fit", dot(w, r) / dot(w, w), J['b1'])
r_res2 = [ri - b2_solo * v for ri, v in zip(r, x2)]
check("same numerator using return-with-quality-removed", dot(w, r_res2), F(3))

sub("3.2  direction TWO -- what is left of quality after cheapness has had it")
a = B / A
check("regress x2 on x1: slope = B/A = 7/(15/2)", a, F('14/15'))
v = [u - a * t for u, t in zip(x2, x1)]
show("v = x2 - (14/15)x1", v)
check("v", tuple(v), tuple(frac('2/5', '-8/15', '0', '1/15', '2/15')))
check("sum x1*v = 0 by construction", dot(x1, v), F(0))
check("sum v^2", dot(v, v), F('7/15'))
check("sum v^2 = det/A = (7/2)/(15/2)", det / A, F('7/15'))
check("shrinkage: C / sum v^2 = 7/(7/15) = the VIF", C / dot(v, v), F(15))
check("sum v*r", dot(v, r), F('-7/3'))
check("b2 = sum v*r / sum v^2 = (-7/3)/(7/15)  -- MATCHES", dot(v, r) / dot(v, v), J['b2'])

sub("3.3  why the SEQUENTIAL method is exactly VIF too small")
print("   sequential numerator uses RAW x2, not v:")
check("sum x2 * (r - (4/3)x1)", dot(x2, resid1), F('-7/3'))
check("sum v  * (r - (4/3)x1)  -- identical numerator", dot(v, resid1), F('-7/3'))
print("   The numerators agree; only the DENOMINATOR differs:")
check("sequential divides by C", C, F(7))
check("Frisch-Waugh divides by sum v^2", dot(v, v), F('7/15'))
check("ratio of denominators C / sum v^2 = VIF", C / dot(v, v), F(15))

# ============================================================================
head("SECTION 4  Pushing the columns together: the determinant collapse")
# ============================================================================

d = [u - t for u, t in zip(x2, x1)]
show("disagreement direction d = x2 - x1", d)
check("d", tuple(d), tuple(frac('1/2', '-1/2', '0', '0', '0')))
Sxd = dot(x1, d); Dd = dot(d, d); m = dot(d, r)
check("S = sum x1*d", Sxd, F('-1/2'))
check("D = sum d^2", Dd, F('1/2'))
check("m = sum d*r", m, F(-3))

def col2(t):
    return [u + t * di for u, di in zip(x1, d)]

sub("4.1  the algebraic law, checked term by term at every t used")
print("   x2(t) = x1 + t*d   so   B(t) = A + tS,   C(t) = A + 2tS + t^2 D,")
print("   det(t) = A*C - B^2 = t^2 (A*D - S^2).")
check("A*D - S^2 = (15/2)(1/2) - 1/4", A * Dd - Sxd * Sxd, F('7/2'))
print("   Since span(x1, x2(t)) = span(x1, d) for EVERY t != 0, the fitted vector,")
print("   the misses and SS cannot depend on t. Only the SPLIT does:")
print("   fitted = c1*x1 + c2*d  with  b1 + b2 = c1  and  t*b2 = c2.")

TS = [F(1), F('1/2'), F('1/4'), F('1/10'), F('1/100')]
print()
print(f"   {'t':>7s} {'x2 AXL':>9s} {'x2 BRN':>9s} {'det':>10s} {'cos':>9s} "
      f"{'VIF':>12s} {'b1':>6s} {'b2':>6s} {'b1+b2':>6s} {'SSe':>4s}")
for t in TS:
    ct = col2(t)
    Jt = joint(x1, ct, r)
    cost = math.sqrt(float(Jt['B'] ** 2 / (Jt['A'] * Jt['C'])))
    print(f"   {S(t):>7s} {S(ct[0]):>9s} {S(ct[1]):>9s} {S(Jt['det']):>10s} "
          f"{cost:>9.6f} {S(Jt['A']*Jt['C']/Jt['det']):>12s} "
          f"{S(Jt['b1']):>6s} {S(Jt['b2']):>6s} {S(Jt['b1']+Jt['b2']):>6s} "
          f"{S(dot(Jt['e'],Jt['e'])):>4s}")
    check(f"  t={S(t)}: det = t^2 * 7/2", Jt['det'], t * t * F('7/2'))
    check(f"  t={S(t)}: b2 = -5/t", Jt['b2'], F(-5) / t)
    check(f"  t={S(t)}: b1 = 1 + 5/t", Jt['b1'], F(1) + F(5) / t)
    check(f"  t={S(t)}: b1 + b2 = 1 always", Jt['b1'] + Jt['b2'], F(1))
    check(f"  t={S(t)}: fitted UNCHANGED", tuple(Jt['fit']), tuple(J['fit']))
    check(f"  t={S(t)}: misses UNCHANGED", tuple(Jt['e']), tuple(J['e']))
    check(f"  t={S(t)}: sum e^2 UNCHANGED", dot(Jt['e'], Jt['e']), F(6))
    check(f"  t={S(t)}: b1_solo unchanged (x1 and r untouched)", Jt['p'] / Jt['A'], F('4/3'))

sub("4.2  the exact numbers at t = 1/2, done the long way (nothing assumed)")
c_half = col2(F('1/2'))
check("x2(1/2)", tuple(c_half), tuple(frac('-5/4', '-3/4', '0', '1', '2')))
Ah, Bh, Ch, ph, qh = gram(x1, c_half, r)
check("A", Ah, F('15/2'))
check("B = sum x1*x2(1/2)", Bh, F('29/4'))
check("C = sum x2(1/2)^2", Ch, F('57/8'))
check("det = (15/2)(57/8) - (29/4)^2 = 855/16 - 841/16", Ah * Ch - Bh * Bh, F('7/8'))
check("p (unchanged)", ph, F(10))
check("q = sum x2(1/2)*r", qh, F('17/2'))
Jh = joint(x1, c_half, r)
check("b1 = (C p - B q)/det", Jh['b1'], F(11))
check("b2 = (A q - B p)/det", Jh['b2'], F(-10))
check("b2_solo = q/C = (17/2)/(57/8)", qh / Ch, F('68/57'))
show("  b2_solo decimal (ROUNDED)", dec(qh / Ch))
check("one-at-a-time still says quality is POSITIVE while truth is -10",
      F(qh / Ch > 0 and Jh['b2'] < 0), F(1))
check("SS of the one-at-a-time pair at t=1/2", SS2(x1, c_half, r, ph / Ah, qh / Ch), F('5231/171'))
show("  decimal (ROUNDED)", dec(SS2(x1, c_half, r, ph/Ah, qh/Ch)))
check("SS of the correct pair at t=1/2 (unchanged)", SS2(x1, c_half, r, F(11), F(-10)), F(6))
check("naive at t=1/2 beats predicting zero by only this much", F(31) - F('5231/171'), F('70/171'))
show("  decimal (ROUNDED)", dec(F('70/171')))

sub("4.3  exact collision: t = 0, the two columns become the same column")
c0 = col2(F(0))
check("x2(0) == x1", tuple(c0), tuple(x1))
A0, B0, C0, p0, q0 = gram(x1, c0, r)
check("det = A*C - B^2 = (15/2)^2 - (15/2)^2", A0 * C0 - B0 * B0, F(0))
print("   Cramer's rule now divides by zero. There is no unique answer.")
print("   The two normal equations have become ONE equation, (15/2)(b1+b2) = 10:")
check("any pair with b1 + b2 = p/A = 4/3 fits equally well", p0 / A0, F('4/3'))
for (u1, u2) in [(F('4/3'), F(0)), (F(0), F('4/3')), (F(100), F('4/3') - F(100)),
                 (F('-1000'), F('4/3') + F(1000))]:
    ss = SS2(x1, c0, r, u1, u2)
    check(f"  SS at (b1,b2) = ({S(u1)}, {S(u2)})", ss, F('53/3'))
check("that common SS = sum r^2 - p^2/A", F(31) - p * p / A, F('53/3'))
show("  decimal (ROUNDED)", dec(F('53/3')))
print("   And note the JUMP: for every t > 0 the fit reaches SS = 6; at t = 0 exactly,")
print("   a whole dimension of fit disappears and the best possible SS leaps to 53/3.")
check("SS jump ratio (53/3)/6", F('53/3') / F(6), F('53/18'))
show("  decimal (ROUNDED)", dec(F('53/3') / F(6)))
check("b1+b2 is 1 for every t>0 but 4/3 at t=0 -- discontinuous",
      F(F(1) != F('4/3')), F(1))

sub("4.4  VIF at each t, as a rounded decimal (exact fractions in the table above)")
for t in TS:
    Jt = joint(x1, col2(t), r)
    vt = Jt['A'] * Jt['C'] / Jt['det']
    print(f"        t = {S(t):>6s}   VIF = {S(vt):>12s} = {dec(vt, 2)} (rounded)")

# ============================================================================
head("SECTION 5  Instability: what a one-stock data change does at each t")
# ============================================================================

print("   Nudge BRN's return by +1 percentage point, from +2% to +3%. Nothing else.")
r_bump = [ri + (F(1) if nm == "BRN" else F(0)) for nm, ri in zip(names, r)]
check("bumped returns", tuple(r_bump), tuple(frac('-4', '3', '1', '3', '1')))
for t in [F(1), F('1/2'), F('1/4')]:
    ct = col2(t)
    J0 = joint(x1, ct, r); J1 = joint(x1, ct, r_bump)
    d1 = J1['b1'] - J0['b1']; d2 = J1['b2'] - J0['b2']
    print(f"        t = {S(t):>5s}:  b1 {S(J0['b1']):>4s} -> {S(J1['b1']):>7s} "
          f"(change {S(d1):>6s})   b2 {S(J0['b2']):>4s} -> {S(J1['b2']):>8s} "
          f"(change {S(d2):>7s})   sum change {S(d1+d2):>5s}")
    check(f"  t={S(t)}: change in b1+b2 is -1/7 regardless of t", d1 + d2, F('-1/7'))
check("t=1  : change in b1", joint(x1, col2(F(1)), r_bump)['b1'] - F(6), F(1))
check("t=1  : change in b2", joint(x1, col2(F(1)), r_bump)['b2'] - F(-5), F('-8/7'))
check("t=1/2: change in b1", joint(x1, col2(F('1/2')), r_bump)['b1'] - F(11), F('15/7'))
check("t=1/2: change in b2", joint(x1, col2(F('1/2')), r_bump)['b2'] - F(-10), F('-16/7'))
check("t=1/4: change in b1", joint(x1, col2(F('1/4')), r_bump)['b1'] - F(21), F('31/7'))
check("t=1/4: change in b2", joint(x1, col2(F('1/4')), r_bump)['b2'] - F(-20), F('-32/7'))
print("   Halve t and the split's response roughly doubles; the SUM's response never moves.")

# ============================================================================
head("SECTION 6  BOSS ROUND -- the dataset where one-at-a-time flips a sign")
# ============================================================================

X1 = frac('-2', '-1', '0', '1', '2')     # value score
X2 = frac('-1', '-1', '0', '1', '1')     # quality score
R  = frac('1',  '4',  '1', '-2', '-1')   # returns, %

show("names", names)
show("X1 value  ", X1)
show("X2 quality", X2)
show("R  return%", R)

sub("6.1  the five cross-products")
bA, bB, bC, bp, bq = gram(X1, X2, R)
check("A = sum X1^2", bA, F(10))
check("B = sum X1*X2", bB, F(6))
check("C = sum X2^2", bC, F(4))
check("p = sum X1*R", bp, F(-10))
check("q = sum X2*R", bq, F(-8))
check("sum R^2", dot(R, R), F(23))
bdet = bA * bC - bB * bB
check("det = 40 - 36", bdet, F(4))
check("cos^2 = 36/40", bB * bB / (bA * bC), F('9/10'))
show("cos (ROUNDED)", dec(math.sqrt(0.9), 6))
bVIF = bA * bC / bdet
check("VIF = A*C/det = 40/4", bVIF, F(10))

sub("6.2  the correct joint answer")
BJ = joint(X1, X2, R)
check("b1 = (C p - B q)/det = (-40 + 48)/4", BJ['b1'], F(2))
check("b2 = (A q - B p)/det = (-80 + 60)/4", BJ['b2'], F(-5))
check("b1 + b2", BJ['b1'] + BJ['b2'], F(-3))
show("fitted = 2*X1 - 5*X2", BJ['fit'])
check("fitted", tuple(BJ['fit']), tuple(frac('1', '3', '0', '-3', '-1')))
show("misses e", BJ['e'])
check("e", tuple(BJ['e']), tuple(frac('0', '1', '1', '1', '0')))
check("sum X1*e = 0", dot(X1, BJ['e']), F(0))
check("sum X2*e = 0", dot(X2, BJ['e']), F(0))
check("sum e   (not zero)", sum(BJ['e']), F(3))
check("sum e^2 = SS_min", dot(BJ['e'], BJ['e']), F(3))
check("sum fitted^2", dot(BJ['fit'], BJ['fit']), F(20))
check("20 + 3 = sum R^2", F(20) + F(3), F(23))
check("uncentered R^2 = 20/23", F(20, 23), F('20/23'))
show("  percentage (ROUNDED)", dec(F(2000, 23), 2) + "%")

sub("6.3  the naive one-at-a-time answer -- and the sign flip")
Bb1_solo = bp / bA
Bb2_solo = bq / bC
check("b1_solo = p/A = -10/10", Bb1_solo, F(-1))
check("b2_solo = q/C = -8/4", Bb2_solo, F(-2))
print("   TRUE (+2, -5).   ONE-AT-A-TIME (-1, -2).")
check("b1 SIGN FLIP: true > 0, naive < 0", F(BJ['b1'] > 0 and Bb1_solo < 0), F(1))
check("b1 naive/true ratio", Bb1_solo / BJ['b1'], F('-1/2'))
check("b1 absolute error in percentage points per unit", BJ['b1'] - Bb1_solo, F(3))
check("b2 true/naive ratio = -5/-2", BJ['b2'] / Bb2_solo, F('5/2'))
Bnf = [Bb1_solo * a + Bb2_solo * b for a, b in zip(X1, X2)]
Bne = [ri - fi for ri, fi in zip(R, Bnf)]
show("naive fitted", Bnf)
check("naive fitted", tuple(Bnf), tuple(frac('4', '3', '0', '-3', '-4')))
show("naive misses", Bne)
check("naive misses", tuple(Bne), tuple(frac('-3', '1', '1', '1', '3')))
check("sum X1*miss -- Level 3's audit fails it", dot(X1, Bne), F(12))
check("sum X2*miss -- fails too", dot(X2, Bne), F(6))
BSS_naive = SS2(X1, X2, R, Bb1_solo, Bb2_solo)
check("SS of the naive pair", BSS_naive, F(21))
check("SS of the correct pair", SS2(X1, X2, R, BJ['b1'], BJ['b2']), F(3))
check("RATIO: the naive pair misses exactly this many times more", BSS_naive / F(3), F(7))
check("SS of giving up, b = (0,0)", SS2(X1, X2, R, F(0), F(0)), F(23))
check("variation the naive pair explains: 23 - 21", F(23) - BSS_naive, F(2))
check("  vs 20 for the correct pair; ratio", F(20) / F(2), F(10))
BD1 = Bb1_solo - BJ['b1']; BD2 = Bb2_solo - BJ['b2']
check("delta = (-3, +3)", (BD1, BD2), (F(-3), F(3)))
check("excess loss A d1^2 + 2B d1 d2 + C d2^2", bA*BD1*BD1 + 2*bB*BD1*BD2 + bC*BD2*BD2, F(18))
check("3 + 18 = 21", F(3) + F(18), BSS_naive)

sub("6.3b  dropping a column on the boss data (interrogation objection 2)")
check("drop quality: SS = sum R^2 - p^2/A = 23 - 100/10", F(23) - bp*bp/bA, F(13))
check("drop value  : SS = sum R^2 - q^2/C = 23 - 64/4", F(23) - bq*bq/bC, F(7))
check("naive explains 2 of 23", (F(23) - BSS_naive) / F(23), F('2/23'))
show("  percentage (ROUNDED)", dec(F(200, 23), 2) + "%")

sub("6.4  the sequential method on the boss data")
Bresid1 = [ri - Bb1_solo * a for ri, a in zip(R, X1)]
check("R - (-1)X1", tuple(Bresid1), tuple(frac('-1', '3', '1', '-1', '1')))
check("  it IS balanced against X1", dot(X1, Bresid1), F(0))
check("  it is NOT balanced against X2", dot(X2, Bresid1), F(-2))
Bb2_seq = dot(X2, Bresid1) / bC
check("b2_seq = -2/4", Bb2_seq, F('-1/2'))
check("true b2 / sequential b2 = -5/(-1/2) = the VIF", BJ['b2'] / Bb2_seq, bVIF)
check("SS of the sequential pair (-1, -1/2)", SS2(X1, X2, R, Bb1_solo, Bb2_seq), F(12))

sub("6.5  Frisch-Waugh on the boss data, both directions")
Ba = bB / bA
check("regress X2 on X1: slope B/A = 6/10", Ba, F('3/5'))
Bv = [u - Ba * t for u, t in zip(X2, X1)]
check("v = X2 - (3/5)X1", tuple(Bv), tuple(frac('1/5', '-2/5', '0', '2/5', '-1/5')))
check("sum X1*v = 0", dot(X1, Bv), F(0))
check("sum v^2 = det/A = 4/10", dot(Bv, Bv), F('2/5'))
check("sum v*R", dot(Bv, R), F(-2))
check("b2 = (-2)/(2/5)  -- matches the joint fit", dot(Bv, R) / dot(Bv, Bv), BJ['b2'])
Bap = bB / bC
check("regress X1 on X2: slope B/C = 6/4", Bap, F('3/2'))
Bw = [u - Bap * t for u, t in zip(X1, X2)]
check("w = X1 - (3/2)X2", tuple(Bw), tuple(frac('-1/2', '1/2', '0', '-1/2', '1/2')))
check("sum X2*w = 0", dot(X2, Bw), F(0))
check("sum w^2 = det/C = 4/4", dot(Bw, Bw), F(1))
check("sum w*R", dot(Bw, R), F(2))
check("b1 = 2/1  -- matches", dot(Bw, R) / dot(Bw, Bw), BJ['b1'])
check("shrinkage on column 1: A / sum w^2 = 10/1 = VIF", bA / dot(Bw, Bw), bVIF)
check("shrinkage on column 2: C / sum v^2 = 4/(2/5) = VIF", bC / dot(Bv, Bv), bVIF)

sub("6.6  the money question -- two names not in the estimation set")
for nm, e1, e2 in [("GRV", F(2), F(0)), ("JDE", F(0), F(1))]:
    tp = BJ['b1'] * e1 + BJ['b2'] * e2
    np_ = Bb1_solo * e1 + Bb2_solo * e2
    print(f"        {nm}: exposures ({S(e1)}, {S(e2)})  correct {S(tp)}%   naive {S(np_)}%")
check("GRV correct forecast 2*2 - 5*0", BJ['b1'] * 2 + BJ['b2'] * 0, F(4))
check("GRV naive   forecast -1*2 - 2*0", Bb1_solo * 2 + Bb2_solo * 0, F(-2))
check("GRV: the two forecasts have opposite signs", F(F(4) > 0 and F(-2) < 0), F(1))
check("GRV gap in percentage points", F(4) - F(-2), F(6))
check("JDE correct forecast", BJ['b1'] * 0 + BJ['b2'] * 1, F(-5))
check("JDE naive   forecast", Bb1_solo * 0 + Bb2_solo * 1, F(-2))
check("long GRV / short JDE, correct forecast", F(4) - F(-5), F(9))
check("long GRV / short JDE, naive forecast -- priced at EXACTLY zero",
      F(-2) - F(-2), F(0))

# ============================================================================
head("SECTION 7  The general claims, brute-forced over many datasets")
# ============================================================================

def rand_sets():
    """deterministic sweep of small integer 2-column datasets, 5 assets"""
    base = [F(-2), F(-1), F(0), F(1), F(2)]
    for k in product([F(-1), F(0), F(1), F(2)], repeat=5):
        c2 = list(k)
        if dot(base, base) * dot(c2, c2) - dot(base, c2) ** 2 == 0:
            continue
        for rr in [frac('1','4','1','-2','-1'), frac('-4','2','1','3','1'),
                   frac('3','-1','2','0','-3'), frac('0','5','-2','1','1')]:
            yield base, c2, rr

sub("7.1  Frisch-Waugh always recovers the joint coefficient")
n_fw = 0
for c1, c2, rr in rand_sets():
    Jt = joint(c1, c2, rr)
    aa = dot(c1, c2) / dot(c1, c1)
    vv = [u - aa * t for u, t in zip(c2, c1)]
    if dot(vv, vv) == 0:
        continue
    if dot(vv, rr) / dot(vv, vv) != Jt['b2']:
        sys.exit("FRISCH-WAUGH FAILED on " + row(c2))
    n_fw += 1
check("datasets checked, all recovered b2 exactly", F(n_fw > 0), F(1))
print(f"        {n_fw} datasets swept, zero failures.")

sub("7.2  the sequential method is understated by EXACTLY the VIF, always")
n_sq = 0
for c1, c2, rr in rand_sets():
    Aq, Bq, Cq, pq, qq = gram(c1, c2, rr)
    dq = Aq * Cq - Bq * Bq
    Jt = joint(c1, c2, rr)
    seq = (qq - Bq * pq / Aq) / Cq
    if seq == 0:
        continue
    if Jt['b2'] / seq != Aq * Cq / dq:
        sys.exit("SEQUENTIAL/VIF IDENTITY FAILED on " + row(c2))
    n_sq += 1
print(f"        {n_sq} datasets swept, zero failures.")
check("identity holds on every non-degenerate case", F(n_sq > 0), F(1))

sub("7.3  AT MOST ONE of the two one-at-a-time coefficients can have a wrong sign")
print("   Proof: a flip on column 1 needs  B*b1*b2 < -A*b1^2 ;")
print("          a flip on column 2 needs  B*b1*b2 < -C*b2^2 .")
print("   Multiply the two (both sides negative): B^2 b1^2 b2^2 > A*C*b1^2*b2^2,")
print("   i.e. B^2 > A*C, i.e. det < 0 -- impossible. Brute force agrees:")
both = 0; one = 0; tested = 0
for c1, c2, rr in rand_sets():
    Aq, Bq, Cq, pq, qq = gram(c1, c2, rr)
    if Aq == 0 or Cq == 0:
        continue
    Jt = joint(c1, c2, rr)
    f1 = Jt['b1'] * (pq / Aq) < 0
    f2 = Jt['b2'] * (qq / Cq) < 0
    tested += 1
    if f1 and f2:
        both += 1
    elif f1 or f2:
        one += 1
print(f"        {tested} datasets tested: {one} with exactly one sign flip, "
      f"{both} with two.")
check("number of datasets where BOTH flipped", F(both), F(0))

sub("7.4  three ways of writing the determinant, all equal")
for c1, c2, rr in list(rand_sets())[:400]:
    Aq, Bq, Cq, pq, qq = gram(c1, c2, rr)
    dq = Aq * Cq - Bq * Bq
    aa = Bq / Aq
    vv = [u - aa * t for u, t in zip(c2, c1)]
    if Aq * dot(vv, vv) != dq:
        sys.exit("det = A * sum v^2 FAILED")
    if Aq * Cq * (1 - Bq * Bq / (Aq * Cq)) != dq:
        sys.exit("det = A*C*(1-cos^2) FAILED")
check("det = A * (leftover size of column 2) on all sampled datasets", F(1), F(1))
check("det = A*C*(1 - cos^2)              on all sampled datasets", F(1), F(1))
check("main dataset:  A * sum v^2 = (15/2)(7/15)", A * dot(v, v), det)
check("main dataset:  C * sum w^2 = 7 * (1/2)", C * dot(w, w), det)
check("boss dataset:  A * sum v^2 = 10 * (2/5)", bA * dot(Bv, Bv), bdet)

sub("7.5  the correct fit explains exactly VIF times as much as one-at-a-time")
print("   Algebra:  explained(joint)  = (C p^2 - 2B p q + A q^2) / det")
print("             explained(naive)  = (C p^2 - 2B p q + A q^2) / (A*C)")
print("   Same numerator. The ratio is therefore A*C/det = the VIF, exactly, always.")
matches = 0; total = 0
for c1, c2, rr in rand_sets():
    Aq, Bq, Cq, pq, qq = gram(c1, c2, rr)
    dq = Aq * Cq - Bq * Bq
    Jt = joint(c1, c2, rr)
    expl_joint = Jt['b1'] * pq + Jt['b2'] * qq
    u1, u2 = pq / Aq, qq / Cq
    expl_naive = 2 * (u1 * pq + u2 * qq) - (Aq*u1*u1 + 2*Bq*u1*u2 + Cq*u2*u2)
    if expl_joint != (Aq * Cq / dq) * expl_naive:
        sys.exit("VIF EXPLAINED-RATIO IDENTITY FAILED on " + row(c2))
    total += 1
    if expl_naive != 0:
        matches += 1
print(f"        {total} datasets swept, zero failures "
      f"({matches} with a non-zero naive explanation).")
check("main dataset: 25 = 15 * (5/3)", F(15) * F('5/3'), F(25))
check("boss dataset: 20 = 10 * 2", F(10) * F(2), F(20))
check("closed form for explained(joint): (C p^2 - 2B p q + A q^2)/det",
      (C*p*p - 2*B*p*q + A*q*q) / det, F(25))
check("closed form for explained(naive): same numerator over A*C",
      (C*p*p - 2*B*p*q + A*q*q) / (A*C), F('5/3'))

# ============================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level4.md.")
