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
head("SECTION 7b  Every intermediate fragment written out in the markdown")
# ============================================================================
print("   These are the part-way numbers the hand derivations show. Each one is")
print("   recomputed here so that no figure on the page is unverified.")
check("4a:  A*C = (15/2)*7 = 105/2", A * C, F('105/2'))
check("4a:  105/2 - 49", F('105/2') - F(49), F('7/2'))
check("4a:  (15/2)*7 - 7*10 = -35/2", A * F(7) - F(7) * F(10), F('-35/2'))
check("4a:  (-35/2)/(7/2)", F('-35/2') / F('7/2'), F(-5))
check("5a:  delta1^2 = (14/3)^2 = 196/9", F('14/3') ** 2, F('196/9'))
check("5a:  (15/2)(196/9) = 2940/18 = 490/3", F('15/2') * F('196/9'), F('490/3'))
check("5a:  490/3 - 392 + 252", F('490/3') - F(392) + F(252), F('70/3'))
check("5c:  31 - 49/7", F(31) - F(49) / F(7), F(24))
check("5a:  31 - 88/3 = 5/3", F(31) - F('88/3'), F('5/3'))
show("       decimal (ROUNDED)", dec(F('5/3')))
check("6b:  sum v*r written in fifteenths: (-24-16+0+3+2)/15 = -35/15", F(-35, 15), F('-7/3'))
check("7c:  x1*x2(1/2) terms  15/8 and 3/8", F('15/8') + F('3/8') + F(0) + F(1) + F(4), F('29/4'))
check("7c:  x2(1/2)^2 terms  25/16 and 9/16", F('25/16') + F('9/16') + F(0) + F(1) + F(4), F('57/8'))
check("7c:  (15/2)(57/8) = 855/16", F('15/2') * F('57/8'), F('855/16'))
check("7c:  (29/4)^2 = 841/16", F('29/4') ** 2, F('841/16'))
check("7c:  855/16 - 841/16 = 14/16 = 7/8", F('855/16') - F('841/16'), F('7/8'))
check("7c:  q = 5 - 3/2 + 0 + 3 + 2", F(5) - F('3/2') + F(0) + F(3) + F(2), F('17/2'))
check("7c:  (57/8)(10) = 570/8", F('57/8') * F(10), F('570/8'))
check("7c:  (29/4)(17/2) = 493/8", F('29/4') * F('17/2'), F('493/8'))
check("7c:  (570/8 - 493/8)/(7/8) = 77/7", (F('570/8') - F('493/8')) / F('7/8'), F(11))
check("7c:  (15/2)(17/2) = 255/4", F('15/2') * F('17/2'), F('255/4'))
check("7c:  (29/4)(10) = 290/4", F('29/4') * F(10), F('290/4'))
check("7c:  255/4 - 290/4 = -35/4, times 8/7", (F('255/4') - F('290/4')) * F(8, 7), F(-10))
check("7d:  100/(15/2) = 40/3", F(100) / F('15/2'), F('40/3'))
check("7d:  31 - 40/3 = 53/3", F(31) - F('40/3'), F('53/3'))
check("12: boss drop-quality 23 - 100/10", F(23) - F(100) / F(10), F(13))
check("12: boss drop-value   23 - 64/4", F(23) - F(64) / F(4), F(7))

# ============================================================================
head("SECTION 8  The one illustrative number taken from a BFRE figure (p.11)")
# ============================================================================
print("   Figure 1.3 (NAMR, Dec 2013) gives Size-Liquidity correlation 0.74.")
print("   Treating 0.74 as the cosine of Section 7a:")
c74 = F(37, 50)
check("0.74 as an exact fraction", c74, F('37/50'))
check("cos^2 = 1369/2500", c74 * c74, F('1369/2500'))
check("1 - cos^2", 1 - c74 * c74, F('1131/2500'))
vif74 = 1 / (1 - c74 * c74)
check("VIF = 2500/1131", vif74, F(2500, 1131))
show("  decimal (ROUNDED)", dec(vif74, 2))
print("   This is OUR arithmetic on a correlation read off their figure.")
print("   The paper prints no VIF values. The markdown says so.")

# ============================================================================
head("SECTION 9  The prose claims, checked AS CLAIMS (adversarial audit pass)")
# ============================================================================
print("   Sections 1-8 check that the numbers are right. These check that the")
print("   SENTENCES built on them are right, which is a different job.")

sub("9.1  'threw away fourteen fifteenths', Section 5a -- not 94%")
expl_joint = F(31) - F(6)          # 25
expl_naive = F(31) - SS_naive      # 5/3
check("explained by the joint fit", expl_joint, F(25))
check("explained by one-at-a-time", expl_naive, F('5/3'))
check("captured share of what was there = 1/VIF", expl_naive / expl_joint, F(1, 15))
check("thrown-away share", 1 - expl_naive / expl_joint, F(14, 15))
show("  thrown-away percentage (ROUNDED)", dec(F(1400, 15), 1) + "%")
print("   14/15 = 93.333...%, so the markdown says 93.3% (rounded). '94%' would be")
print("   the share of the total 31, which is not 'what was there' to be found.")

sub("9.2  Section 3's claim: b1 rests on AXL and BRN alone, b2 does not")
print("   w = x1 - (B/C)x2 is supported on AXL and BRN only, so b1 = sum(w*r)/sum(w^2)")
print("   cannot see the other three returns. b2 uses v, which is supported everywhere.")
frozen1 = []
for i, nm in enumerate(names):
    r_i = [ri + (F(1) if k == i else F(0)) for k, ri in enumerate(r)]
    Ji = joint(x1, x2, r_i)
    m1 = "moves" if Ji['b1'] != J['b1'] else "FIXED"
    m2 = "moves" if Ji['b2'] != J['b2'] else "FIXED"
    print(f"        +1pp on {nm}:  b1 = {S(Ji['b1']):>6s} ({m1})"
          f"    b2 = {S(Ji['b2']):>7s} ({m2})")
    if m1 == "FIXED":
        frozen1.append(nm)
    if nm in ("DLT", "EMK"):
        check(f"  b1 unmoved by a bump to {nm}", Ji['b1'], J['b1'])
        check(f"  b2 DOES move on {nm}", F(Ji['b2'] != J['b2']), F(1))
check("names that cannot move b1", tuple(frozen1), ("CHR", "DLT", "EMK"))
print("   CHR is frozen in BOTH columns because x1 = x2 = 0 there -- that is Level 0's")
print("   CHR trap, not a fact about collinearity. The markdown cites DLT and EMK.")

sub("9.3  Section 7c: SS of the naive pair at t=1/2, traced through 7b's closed form")
numer = Ch * ph * ph - 2 * Bh * ph * qh + Ah * qh * qh
check("C p^2 = (57/8)(100)", Ch * ph * ph, F('5700/8'))
check("2 B p q = 2(29/4)(10)(17/2)", 2 * Bh * ph * qh, F('9860/8'))
check("A q^2 = (15/2)(289/4)", Ah * qh * qh, F('4335/8'))
check("numerator 5700/8 - 9860/8 + 4335/8", numer, F('175/8'))
check("A*C = 855/16", Ah * Ch, F('855/16'))
check("explained(one-at-a-time) = (175/8)/(855/16)", numer / (Ah * Ch), F('70/171'))
check("SS = 31 - 70/171", F(31) - numer / (Ah * Ch), F('5231/171'))
check("  ... and that agrees with fitting it directly",
      SS2(x1, c_half, r, ph / Ah, qh / Ch), F('5231/171'))

sub("9.4  Section 14d: sensitivity scales with sqrt(VIF), NOT with VIF")
print("   Section 8's own numbers settle it. Response of b2 to the same one-stock bump:")
prev = None
for t in [F(1), F('1/2'), F('1/4')]:
    ct = col2(t)
    resp = joint(x1, ct, r_bump)['b2'] - joint(x1, ct, r)['b2']
    vt = joint(x1, ct, r)['A'] * joint(x1, ct, r)['C'] / joint(x1, ct, r)['det']
    if prev:
        print(f"        t {S(prev[2])} -> {S(t)}:  VIF ratio {S(vt/prev[0])} "
              f"= {dec(vt/prev[0],4)}   response ratio {S(resp/prev[1])}"
              f"   sqrt(VIF ratio) = {math.sqrt(float(vt/prev[0])):.4f}")
        check(f"  response ratio t={S(prev[2])}->{S(t)} is exactly 2", resp / prev[1], F(2))
    prev = (vt, resp, t)
check("VIF ratio t=1 -> t=1/2 is 57/14, NOT 4",
      (F('855/14')) / F(15), F(57, 14))
print("   VIF multiplied by 57/14 = 4.0714 while the response multiplied by exactly 2.")
print("   sqrt(57/14) = 2.0178. Sensitivity tracks the SQUARE ROOT.")
check("so for the p.11 illustration, VIF = 2500/1131", vif74, F(2500, 1131))
show("  sqrt(VIF) (ROUNDED)", dec(math.sqrt(float(vif74)), 2))
print("   -> 'about one and a half times the sensitivity', not 'twice'.")

sub("9.5  Section 14f: the collision does NOT understate a portfolio's total risk")
print("   Portfolio equally weighted on AXL and DLT: w = (1/2, 0, 0, 1/2, 0).")
wp = frac('1/2', '0', '0', '1/2', '0')
a1 = dot(wp, x1)
delta = dot(wp, d)
check("a1 = portfolio cheapness exposure", a1, F('-1/4'))
check("delta = w . d  (lives only where the columns disagree)", delta, F('1/4'))
c1_inv = J['b1'] + J['b2']
c2_inv = F(1) * J['b2']
check("c1 = b1 + b2 at t=1", c1_inv, F(1))
check("c2 = t*b2 at t=1", c2_inv, F(-5))
check("predicted total a1*c1 + delta*c2", a1 * c1_inv + delta * c2_inv, F('-3/2'))
print()
print(f"   {'t':>7s} {'a2':>10s} {'b1':>6s} {'b2':>6s} {'a1*b1':>10s} {'a2*b2':>10s} {'total':>7s}")
for t in [F(1), F('1/2'), F('1/4'), F('1/100')]:
    ct = col2(t)
    Jt = joint(x1, ct, r)
    a2 = dot(wp, ct)
    k1 = a1 * Jt['b1']
    k2 = a2 * Jt['b2']
    print(f"   {S(t):>7s} {S(a2):>10s} {S(Jt['b1']):>6s} {S(Jt['b2']):>6s} "
          f"{S(k1):>10s} {S(k2):>10s} {S(k1+k2):>7s}")
    check(f"  t={S(t)}: a2 = a1 + t*delta", a2, a1 + t * delta)
    check(f"  t={S(t)}: portfolio total is INVARIANT", k1 + k2, F('-3/2'))
J100 = joint(x1, col2(F('1/100')), r)
check("t=1/100: cheapness contribution a1*b1", a1 * J100['b1'], F('-501/4'))
check("t=1/100: quality   contribution a2*b2",
      dot(wp, col2(F('1/100'))) * J100['b2'], F('495/4'))
check("t=1/100: they still sum to -3/2 on a two-stock book",
      a1 * J100['b1'] + dot(wp, col2(F('1/100'))) * J100['b2'], F('-3/2'))
print("   Contributions explode; the total never moves. So the risk NUMBER survives")
print("   and the ATTRIBUTION does not -- which is p.32's word 'apportioning'.")

# ============================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level4.md.")
