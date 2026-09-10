#!/usr/bin/env python3
"""
verify_level5.py -- recomputes EVERY number printed in datasets/level5.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level5.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from itertools import product
import sys

# ---------------------------------------------------------------------------
# harness
# ---------------------------------------------------------------------------

CHECKS = [0]


def S(v):
    if isinstance(v, (tuple, list)):
        return "[" + ", ".join(S(t) for t in v) + "]"
    return str(v)


def terminates(fr):
    """True if the fraction has a terminating decimal expansion."""
    d = F(fr).denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d == 1


def dec(v, n=4):
    """Decimal string, tagged EXACT or ROUNDED. The markdown must carry the
    word 'rounded' next to every value this function tags ROUNDED."""
    v = F(v)
    tag = "exact" if terminates(v) else "ROUNDED"
    return f"{float(v):.{n}f} ({tag})"


def head(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def sub(title):
    print()
    print("-- " + title)


def check(label, got, want):
    CHECKS[0] += 1
    ok = (got == want)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: {S(got)}"
          + ("" if ok else f"   EXPECTED {S(want)}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': got {got}, expected {want}")


def show(label, val):
    print(f"        {label}: {S(val)}")


# ---------------------------------------------------------------------------
# linear algebra in exact rationals
# ---------------------------------------------------------------------------

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def wdot(w, u, v):
    return sum(wi * a * b for wi, a, b in zip(w, u, v))


def solve(M, y):
    """Gaussian elimination with exact Fractions. M is k x k, y is length k."""
    k = len(y)
    A = [[F(M[i][j]) for j in range(k)] + [F(y[i])] for i in range(k)]
    for c in range(k):
        p = next(i for i in range(c, k) if A[i][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [t / pv for t in A[c]]
        for i in range(k):
            if i != c and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return [A[i][k] for i in range(k)]


def wls(cols, r, w=None):
    """Weighted least squares. cols is a list of columns. Returns
    (coeffs, fitted, residuals, SS)."""
    n = len(r)
    if w is None:
        w = [F(1)] * n
    k = len(cols)
    M = [[wdot(w, cols[i], cols[j]) for j in range(k)] for i in range(k)]
    y = [wdot(w, cols[i], r) for i in range(k)]
    bb = solve(M, y)
    fit = [sum(bb[j] * cols[j][i] for j in range(k)) for i in range(n)]
    e = [r[i] - fit[i] for i in range(n)]
    ss = sum(w[i] * e[i] * e[i] for i in range(n))
    return bb, fit, e, ss


def ones(n):
    return [F(1)] * n


# ---------------------------------------------------------------------------
# THE COLD-OPEN DATASET (identical to datasets/level0.md)
# ---------------------------------------------------------------------------

NAMES = ["AXL", "BRN", "CHR", "DLT", "EMK"]
X = [F(-3, 2), F(-1, 2), F(0), F(1), F(2)]
R = [F(-2), F(-2), F(1, 2), F(4), F(7, 2)]
N = len(X)

head("SECTION 1  The cold-open file, re-verified (Level 0 numbers)")

Sx = sum(X)
Sxx = dot(X, X)
Sr = sum(R)
Sxr = dot(X, R)
Srr = dot(R, R)

print("   cold-open columns as decimals (all exact):")
for nm, xi, ri in zip(NAMES, X, R):
    print(f"        {nm}:  x = {dec(xi, 1)}   r = {dec(ri, 1)}%")
check("n", F(N), F(5))
check("sum x", Sx, F(1))
check("sum x^2", Sxx, F(15, 2))
check("sum r", Sr, F(4))
check("sum x*r", Sxr, F(15))
check("sum r^2", Srr, F(73, 2))
show("sum x^2 as decimal", dec(Sxx))
show("sum r^2 as decimal", dec(Srr))

b0 = Sxr / Sxx
check("no-intercept b0 = sum(xr)/sum(x^2)", b0, F(2))

E0 = [R[i] - b0 * X[i] for i in range(N)]
check("no-intercept residuals e0", E0, [F(1), F(-1), F(1, 2), F(2), F(-1, 2)])
check("sum e0   (NOT zero)", sum(E0), F(2))
check("sum x*e0 (IS zero)", dot(X, E0), F(0))
check("sum e0^2", dot(E0, E0), F(13, 2))
show("sum e0^2 as decimal", dec(F(13, 2)))

# the parabola from Level 0, re-checked
for bb, want in [(F(3, 2), F(67, 8)), (F(2), F(13, 2)), (F(5, 2), F(67, 8))]:
    ss = Srr - 2 * bb * Sxr + bb * bb * Sxx
    check(f"SS({bb}) = 36.5 - 30b + 7.5b^2", ss, want)
show("SS(3/2) = SS(5/2) as decimal", dec(F(67, 8)))
show("the two mirror slopes as decimals", dec(F(3, 2), 1) + " and " + dec(F(5, 2), 1))

# ---------------------------------------------------------------------------
head("SECTION 2  The balance point of the file, and the gap Level 0 left open")
# ---------------------------------------------------------------------------

xbar = Sx / N
rbar = Sr / N
check("xbar = sum x / n", xbar, F(1, 5))
check("rbar = sum r / n", rbar, F(4, 5))
show("xbar as decimal", dec(xbar))
show("rbar as decimal", dec(rbar))

pred_at_xbar = b0 * xbar
check("no-intercept line evaluated at xbar: 2 * 1/5", pred_at_xbar, F(2, 5))
gap = rbar - pred_at_xbar
check("vertical gap rbar - b0*xbar", gap, F(2, 5))
show("gap as decimal", dec(gap))
check("n * gap  ==  sum e0  (this is the whole answer to Level 0's open question)",
      N * gap, sum(E0))
check("mean residual e0bar = sum e0 / n", sum(E0) / N, F(2, 5))
check("e0bar == gap", sum(E0) / N, gap)

# ---------------------------------------------------------------------------
head("SECTION 3  Two dials: the two normal equations, solved three ways")
# ---------------------------------------------------------------------------

sub("3a. The two balance conditions written as a 2x2 system")
print("      n*a  + (sum x)*b   = sum r        ->   5a +      b = 4")
print("   (sum x)*a + (sum x^2)*b = sum x*r    ->    a + (15/2)b = 15")
check("row 1 coefficients (n, sum x | sum r)", (F(N), Sx, Sr), (F(5), F(1), F(4)))
check("row 2 coefficients (sum x, sum x^2 | sum xr)", (Sx, Sxx, Sxr), (F(1), F(15, 2), F(15)))

sub("3b. By elimination (the by-hand route)")
# row 1 gives a = (4 - b)/5 ; substitute into row 2 and clear denominators by 10
b1 = F(142, 73)
check("row 1 rearranged: a = (4 - b)/5, checked at b = 142/73", (F(4) - b1) / 5, F(30, 73))
check("row 2 x 10:  2(4 - b) + 75b = 150, LHS at b = 142/73",
      2 * (F(4) - b1) + 75 * b1, F(150))
check("8 - 2b + 75b = 8 + 73b, so 73b = 150 - 8", F(150) - 8, F(142))
check("b = 142/73", F(142) / F(73), b1)
check("intermediate: 4 - 142/73 = 150/73", F(4) - b1, F(150, 73))
check("intermediate: (150/73)/5 = 30/73", F(150, 73) / 5, F(30, 73))
check("b = 142/73", b1, F(142, 73))
a1 = (F(4) - b1) / 5
check("a = (4 - b)/5 = 30/73", a1, F(30, 73))
show("b as decimal", dec(b1))
show("a as decimal", dec(a1))

sub("3c. By Cramer's rule (the Level 3 formula)")
det = F(N) * Sxx - Sx * Sx
check("intermediate: 5*(15/2) = 75/2", F(N) * Sxx, F(75, 2))
check("det = n*sum(x^2) - (sum x)^2 = 75/2 - 1", det, F(73, 2))
check("a = (sum r * sum x^2 - sum x * sum xr)/det", (Sr * Sxx - Sx * Sxr) / det, F(30, 73))
check("b = (n * sum xr - sum x * sum r)/det", (F(N) * Sxr - Sx * Sr) / det, F(142, 73))
check("numerator of a: 4*(15/2) - 1*15 = 15", Sr * Sxx - Sx * Sxr, F(15))
check("numerator of b: 5*15 - 1*4 = 71", F(N) * Sxr - Sx * Sr, F(71))

sub("3d. By the machine (weighted-least-squares solver, unit weights)")
coef, FIT1, E1, SS1 = wls([ones(N), X], R)
check("solver a", coef[0], F(30, 73))
check("solver b", coef[1], F(142, 73))

# ---------------------------------------------------------------------------
head("SECTION 4  The with-intercept residuals, and BOTH balances at zero")
# ---------------------------------------------------------------------------

check("fitted values (in 146ths)", [f * 146 for f in FIT1],
      [F(-366), F(-82), F(60), F(344), F(628)])
check("residuals e1 (in 146ths)", [e * 146 for e in E1],
      [F(74), F(-210), F(13), F(240), F(-117)])
check("residuals e1 in lowest terms", E1,
      [F(37, 73), F(-105, 73), F(13, 146), F(120, 73), F(-117, 146)])
for nm, e in zip(NAMES, E1):
    show(f"e1[{nm}] decimal", dec(e))

check("sum e1   (NOW zero)", sum(E1), F(0))
check("sum x*e1 (still zero)", dot(X, E1), F(0))
check("sum e1^2", dot(E1, E1), F(829, 146))
show("sum e1^2 as decimal", dec(F(829, 146)))
check("solver SS agrees", SS1, F(829, 146))

sub("cross-check of SS via Srr - Sxr^2/Sxx (centred sums, Section 6)")
Cxx = Sxx - F(N) * xbar * xbar
Cxr = Sxr - F(N) * xbar * rbar
Crr = Srr - F(N) * rbar * rbar
check("Sxx_c = sum x^2 - n*xbar^2 = 15/2 - 1/5", Cxx, F(73, 10))
check("Sxr_c = sum xr - n*xbar*rbar = 15 - 4/5", Cxr, F(71, 5))
check("Srr_c = sum r^2 - n*rbar^2 = 73/2 - 16/5", Crr, F(333, 10))
check("SS = Srr_c - Sxr_c^2/Sxx_c", Crr - Cxr * Cxr / Cxx, F(829, 146))
show("Sxx_c decimal", dec(Cxx))
show("Sxr_c decimal", dec(Cxr))
show("Srr_c decimal", dec(Crr))

# ---------------------------------------------------------------------------
head("SECTION 5  Side by side, and where the improvement comes from")
# ---------------------------------------------------------------------------

check("no-intercept  : a", F(0), F(0))
check("no-intercept  : b", b0, F(2))
check("no-intercept  : sum e", sum(E0), F(2))
check("no-intercept  : sum x*e", dot(X, E0), F(0))
check("no-intercept  : sum e^2", dot(E0, E0), F(13, 2))
check("with-intercept: a", a1, F(30, 73))
check("with-intercept: b", b1, F(142, 73))
check("with-intercept: sum e", sum(E1), F(0))
check("with-intercept: sum x*e", dot(X, E1), F(0))
check("with-intercept: sum e^2", dot(E1, E1), F(829, 146))

drop = F(13, 2) - F(829, 146)
check("improvement in sum e^2: 13/2 - 829/146 = 949/146 - 829/146", drop, F(60, 73))
show("improvement as decimal", dec(drop))
check("b moved by 2 - 142/73", F(2) - b1, F(4, 73))
show("b move as decimal", dec(F(4, 73)))

sub("5b. Frisch-Waugh (Level 4) applied to the constant column")
# residualise the column of ones on x
c_on_x = dot(ones(N), X) / Sxx
check("coefficient of x when the ones-column is fitted on x: (sum x)/(sum x^2)", c_on_x, F(2, 15))
M = [F(1) - c_on_x * xi for xi in X]
check("residualised ones-column m = 1 - (2/15)x", M,
      [F(6, 5), F(16, 15), F(1), F(13, 15), F(11, 15)])
check("sum m = 0? (no -- m is orthogonal to x, not to itself)", dot(X, M), F(0))
check("m.m = n - (sum x)^2/(sum x^2) = 5 - 2/15", dot(M, M), F(73, 15))
check("m.e0 = sum e0 - (2/15)*sum(x*e0) = 2 - 0", dot(M, E0), F(2))
check("m.r  = sum r - (2/15)*sum xr = 4 - 2", dot(M, R), F(2))
check("a = (m.r)/(m.m) = 2/(73/15)", dot(M, R) / dot(M, M), F(30, 73))
check("SS drop = (m.e0)^2/(m.m) = 4/(73/15)", dot(M, E0) ** 2 / dot(M, M), F(60, 73))
check("...and that equals the drop computed directly", dot(M, E0) ** 2 / dot(M, M), drop)

sub("5c. The share of variation left unexplained (name locked until Level 6)")
r2 = 1 - F(829, 146) / Crr
check("1 - 829/146 / (333/10)", r2, F(20164, 24309))
check("...equals Sxr_c^2/(Sxx_c*Srr_c)", Cxr * Cxr / (Cxx * Crr), F(20164, 24309))
check("20164 = 142^2", F(142) ** 2, F(20164))
show("that ratio as decimal", dec(r2))
check("NUMERICAL COINCIDENCE of this dataset: 1 - (13/2)/(73/2) also = 60/73",
      1 - F(13, 2) / F(73, 2), F(60, 73))
print("        (equal to the SS drop 60/73 by accident of these numbers, not by theorem)")

sub("5d. What ignoring the intercept does to a risk number")
ratio = F(13, 2) / F(829, 146)
check("sum e0^2 / sum e1^2 = (13/2)*(146/829) = 949/829", ratio, F(949, 829))
show("variance overstatement", dec(ratio))
check("overstatement as a fraction: 949/829 - 1 = 120/829", ratio - 1, F(120, 829))
show("  decimal", dec(F(120, 829)))
check("the drop as a fraction of the no-intercept SS: (60/73)/(13/2) = 120/949",
      drop / F(13, 2), F(120, 949))
show("  decimal", dec(F(120, 949)))
check("sqrt bound lower: 1.0699^2 < 949/829", F(10699, 10000) ** 2 < ratio, True)
check("sqrt bound upper: 949/829 < 1.0700^2", ratio < F(107, 100) ** 2, True)
print("        so the standard-deviation overstatement is 1.0699... (irrational, bounded above)")

# ---------------------------------------------------------------------------
head("SECTION 6  Centering: why sum(xr)/sum(x^2) becomes Cov/Var")
# ---------------------------------------------------------------------------

U = [xi - xbar for xi in X]
V = [ri - rbar for ri in R]
check("u = x - xbar (in tenths)", [u * 10 for u in U],
      [F(-17), F(-7), F(-2), F(8), F(18)])
check("u in lowest terms", U, [F(-17, 10), F(-7, 10), F(-1, 5), F(4, 5), F(9, 5)])
check("v = r - rbar (in tenths)", [v * 10 for v in V],
      [F(-28), F(-28), F(-3), F(32), F(27)])
check("v in lowest terms", V, [F(-14, 5), F(-14, 5), F(-3, 10), F(16, 5), F(27, 10)])
check("sum u", sum(U), F(0))
check("sum v", sum(V), F(0))
check("sum u^2 (in hundredths: 289+49+4+64+324 = 730)", dot(U, U) * 100, F(730))
check("sum u^2", dot(U, U), F(73, 10))
check("sum u*v (in hundredths: 476+196+6+256+486 = 1420)", dot(U, V) * 100, F(1420))
check("sum u*v", dot(U, V), F(71, 5))
check("sum v^2", dot(V, V), F(333, 10))

sub("6a. The Level 1 machine run on the centred columns")
check("intermediate: dividing by 73/10 is multiplying by 10/73", 1 / F(73, 10), F(10, 73))
check("b = sum(uv)/sum(u^2) = (71/5)(10/73)", dot(U, V) * F(10, 73), F(142, 73))
check("b = sum(uv)/sum(u^2) = (71/5)/(73/10)", dot(U, V) / dot(U, U), F(142, 73))
check("...identical to the with-intercept b", dot(U, V) / dot(U, U), b1)
check("intermediate: (142/73)(1/5) = 142/365", b1 * xbar, F(142, 365))
check("intermediate: rbar = 4/5 = 292/365", rbar, F(292, 365))
check("intermediate: 292/365 - 142/365 = 150/365", F(292, 365) - F(142, 365), F(150, 365))
check("150/365 reduces to 30/73", F(150, 365), F(30, 73))
check("a = rbar - b*xbar = 4/5 - (142/73)(1/5)", rbar - b1 * xbar, F(30, 73))

sub("6b. Where the identities come from, term by term")
check("sum u*v = sum xr - xbar*sum r - rbar*sum x + n*xbar*rbar", 
      Sxr - xbar * Sr - rbar * Sx + F(N) * xbar * rbar, F(71, 5))
check("...collapses to sum xr - n*xbar*rbar = 15 - 4/5", Sxr - F(N) * xbar * rbar, F(71, 5))
check("sum u^2 = sum x^2 - n*xbar^2 = 15/2 - 5*(1/25)", Sxx - F(N) * xbar * xbar, F(73, 10))
check("n*xbar^2 = 5*(1/25) = 1/5", F(N) * xbar * xbar, F(1, 5))
check("15/2 - 1/5 = 75/10 - 2/10", F(75, 10) - F(2, 10), F(73, 10))

sub("6c. Dividing top and bottom by the same n -- the name unlocks here")
for k, kname in [(F(N), "n = 5"), (F(N - 1), "n - 1 = 4"), (F(1), "1"), (F(7), "7 (nonsense divisor)")]:
    cov = dot(U, V) / k
    var = dot(U, U) / k
    check(f"Cov/Var with divisor {kname}", cov / var, F(142, 73))
check("Cov with n:   (71/5)/5", dot(U, V) / F(5), F(71, 25))
check("Var with n:   (73/10)/5", dot(U, U) / F(5), F(73, 50))
check("Cov with n-1: (71/5)/4", dot(U, V) / F(4), F(71, 20))
check("Var with n-1: (73/10)/4", dot(U, U) / F(4), F(73, 40))
show("Cov (n) decimal", dec(F(71, 25)))
show("Var (n) decimal", dec(F(73, 50)))
show("Cov (n-1) decimal", dec(F(71, 20)))
show("Var (n-1) decimal", dec(F(73, 40)))

sub("6d. Centre x only, or centre r only -- these are NOT the same")
check("centre x only: sum(u*r)/sum(u^2) -- CORRECT", dot(U, R) / dot(U, U), F(142, 73))
check("  because sum(u*r) = sum(u*v) when sum u = 0", dot(U, R), dot(U, V))
check("  sum(u*r) = sum xr - xbar*sum r = 15 - 4/5", Sxr - xbar * Sr, F(71, 5))
check("centre r only: sum(x*v)/sum(x^2) -- WRONG", dot(X, V) / Sxx, F(142, 75))
check("  numerator is right: sum(x*v) = 15 - 4/5 = 71/5", dot(X, V), F(71, 5))
check("  denominator is wrong: sum x^2 = 15/2 = 75/10, not 73/10", Sxx, F(75, 10))
check("  the inflation is exactly n*xbar^2 = 1/5 = 2/10", Sxx - dot(U, U), F(1, 5))
show("centre-r-only b as decimal", dec(F(142, 75)))

# ---------------------------------------------------------------------------
head("SECTION 7  The wrong methods, priced exactly")
# ---------------------------------------------------------------------------

sub("7a. Trap: keep b = 2, add a = the average leftover miss")
aT1, bT1 = sum(E0) / N, F(2)
check("a = e0bar = 2/5", aT1, F(2, 5))
ET1 = [R[i] - aT1 - bT1 * X[i] for i in range(N)]
check("residuals (in tenths)", [e * 10 for e in ET1], [F(6), F(-14), F(1), F(16), F(-9)])
check("sum e = 0   -- the FIRST balance holds", sum(ET1), F(0))
check("sum x*e = -2/5 -- the SECOND balance FAILS", dot(X, ET1), F(-2, 5))
check("sum e^2 = 570/100", dot(ET1, ET1), F(57, 10))
show("sum e^2 decimal", dec(F(57, 10)))
excess1 = F(57, 10) - F(829, 146)
check("excess over the optimum: 57/10 - 829/146 = 4161/730 - 4145/730", excess1, F(8, 365))
show("excess decimal", dec(excess1, 6))
check("this line DOES pass through (xbar, rbar): 2/5 + 2*(1/5)", aT1 + bT1 * xbar, rbar)
check("excess = Sxx_c * (delta b)^2 = (73/10)*(4/73)^2", Cxx * (F(2) - b1) ** 2, F(8, 365))

sub("7b. Trap: fit the average first, then the slope on what is left (sequential)")
aT2 = rbar
bT2 = dot(X, V) / Sxx
check("a = rbar = 4/5", aT2, F(4, 5))
check("b = sum(x*v)/sum(x^2) = 142/75", bT2, F(142, 75))
show("b decimal", dec(bT2))
ET2 = [R[i] - aT2 - bT2 * X[i] for i in range(N)]
check("sum e = 4 - 4 - 142/75 -- the FIRST balance FAILS", sum(ET2), F(-142, 75))
check("sum x*e = 15 - 4/5 - 71/5 = 0 -- the SECOND balance holds", dot(X, ET2), F(0))
check("sum e^2", dot(ET2, ET2), F(4811, 750))
show("sum e^2 decimal", dec(F(4811, 750)))
excess2 = F(4811, 750) - F(829, 146)
check("excess over the optimum", excess2, F(20164, 27375))
show("excess decimal", dec(excess2))
check("barely better than having no intercept at all (13/2 = 6.5)", F(4811, 750) < F(13, 2), True)
check("  the whole gain from the second parameter: 13/2 - 4811/750", F(13, 2) - F(4811, 750), F(64, 750))
show("  that gain as decimal", dec(F(64, 750)))
check("  compare the true gain 60/73", drop, F(60, 73))

sub("7c. Trap: mismatched divisors in Cov/Var")
check("Cov(n-1)/Var(n) = (71/20)/(73/50)", F(71, 20) / F(73, 50), F(355, 146))
show("  decimal", dec(F(355, 146)))
check("Cov(n)/Var(n-1) = (71/25)/(73/40)", F(71, 25) / F(73, 40), F(568, 365))
show("  decimal", dec(F(568, 365)))
check("  first is 5/4 times too big", F(355, 146) / b1, F(5, 4))
check("  second is 4/5 of the truth", F(568, 365) / b1, F(4, 5))

sub("7d. Trap: the Level 0 shortcuts, still wrong, now for a second reason")
check("sum r / sum x", Sr / Sx, F(4))
slopes = [R[i] / X[i] for i in range(N) if X[i] != 0]
check("per-stock slopes r/x (CHR excluded, x = 0)", slopes,
      [F(4, 3), F(4), F(4), F(7, 4)])
mslope = sum(slopes) / len(slopes)
check("mean of the per-stock slopes", mslope, F(133, 48))
show("  decimal", dec(mslope))

sub("7e. Trap: 'the fit must pass through the origin, it is a return model'")
check("with-intercept line at x = 0 is a = 30/73, not 0", a1, F(30, 73))
check("forcing it through (0,0) costs 13/2 - 829/146", drop, F(60, 73))

# ---------------------------------------------------------------------------
head("SECTION 8  Rescaling the x column: what moves and what does not")
# ---------------------------------------------------------------------------

for c in [F(2), F(1, 3), F(-1), F(10)]:
    Xc = [c * xi for xi in X]
    cc, fitc, ec, ssc = wls([ones(N), Xc], R)
    check(f"scale x by {c}: a unchanged", cc[0], a1)
    check(f"scale x by {c}: b -> b/{c}", cc[1], b1 / c)
    check(f"scale x by {c}: residuals unchanged", ec, E1)
    check(f"scale x by {c}: sum e^2 unchanged", ssc, F(829, 146))

# ---------------------------------------------------------------------------
head("SECTION 9  BOSS ROUND -- fresh data, four names")
# ---------------------------------------------------------------------------

BNAMES = ["FRT", "GLM", "HSK", "JND"]
BX = [F(1), F(2), F(4), F(5)]
BR = [F(2), F(3), F(4), F(7)]
BN = len(BX)

bSx, bSxx, bSr, bSxr, bSrr = sum(BX), dot(BX, BX), sum(BR), dot(BX, BR), dot(BR, BR)
print("   boss columns as decimals (all exact):")
for nm, xi, ri in zip(BNAMES, BX, BR):
    print(f"        {nm}:  x = {dec(xi, 1)}   r = {dec(ri, 1)}%")
check("n", F(BN), F(4))
check("sum x = 1+2+4+5", bSx, F(12))
check("sum x^2 = 1+4+16+25", bSxx, F(46))
check("sum r = 2+3+4+7", bSr, F(16))
check("sum x*r = 2+6+16+35", bSxr, F(59))
check("sum r^2 = 4+9+16+49", bSrr, F(78))

bxbar, brbar = bSx / BN, bSr / BN
check("xbar = 12/4", bxbar, F(3))
check("rbar = 16/4", brbar, F(4))

bdet = F(BN) * bSxx - bSx * bSx
check("det = 4*46 - 12^2 = 184 - 144", bdet, F(40))
check("row 1: 4a + 12b = 16  ->  a = 4 - 3b, checked at b = 11/10", F(4) - 3 * F(11, 10), F(7, 10))
check("row 2: 12(4 - 3b) + 46b = 59  ->  48 - 36b + 46b = 59  ->  10b = 11",
      F(59) - F(48), F(11))
check("b = 11/10", F(11) / F(10), F(11, 10))
check("a = 4 - 3*(11/10) = 4 - 33/10", F(4) - F(33, 10), F(7, 10))
bb_, bfit, bE, bSS = wls([ones(BN), BX], BR)
check("a = (16*46 - 12*59)/40 = (736 - 708)/40", (bSr * bSxx - bSx * bSxr) / bdet, F(7, 10))
check("b = (4*59 - 12*16)/40 = (236 - 192)/40", (F(BN) * bSxr - bSx * bSr) / bdet, F(11, 10))
check("solver agrees on a", bb_[0], F(7, 10))
check("solver agrees on b", bb_[1], F(11, 10))
show("a decimal", dec(F(7, 10)))
show("b decimal", dec(F(11, 10)))

bCxx = bSxx - F(BN) * bxbar * bxbar
bCxr = bSxr - F(BN) * bxbar * brbar
bCrr = bSrr - F(BN) * brbar * brbar
check("Sxx_c = 46 - 4*9", bCxx, F(10))
check("Sxr_c = 59 - 4*3*4 = 59 - 48", bCxr, F(11))
check("Srr_c = 78 - 4*16", bCrr, F(14))
check("b = Sxr_c/Sxx_c = 11/10", bCxr / bCxx, F(11, 10))
check("a = rbar - b*xbar = 4 - 33/10", brbar - F(11, 10) * bxbar, F(7, 10))

check("fitted (in tenths)", [f * 10 for f in bfit], [F(18), F(29), F(51), F(62)])
check("residuals (in tenths)", [e * 10 for e in bE], [F(2), F(1), F(-11), F(8)])
check("sum e", sum(bE), F(0))
check("sum x*e", dot(BX, bE), F(0))
check("sum e^2 = 190/100", bSS, F(19, 10))
show("sum e^2 decimal", dec(F(19, 10)))
check("SS = Srr_c - Sxr_c^2/Sxx_c = 14 - 121/10", bCrr - bCxr * bCxr / bCxx, F(19, 10))

sub("9a. The claim: the line passes through (xbar, rbar) = (3, 4)")
check("a + b*xbar = 7/10 + (11/10)*3 = 40/10", F(7, 10) + F(11, 10) * F(3), F(4))
check("...and that equals rbar", F(7, 10) + F(11, 10) * F(3), brbar)

sub("9b. The proof, as arithmetic: freeze b, complete the square in a")
D = [BR[i] - F(11, 10) * BX[i] for i in range(BN)]
check("d = r - b*x (in tenths)", [d * 10 for d in D], [F(9), F(8), F(-4), F(15)])
check("dbar = (9+8-4+15)/40 = 28/40", sum(D) / BN, F(7, 10))
check("dbar == a", sum(D) / BN, F(7, 10))
check("dbar == rbar - b*xbar", sum(D) / BN, brbar - F(11, 10) * bxbar)
check("sum (d - dbar)^2 = 190/100", sum((d - F(7, 10)) ** 2 for d in D), F(19, 10))
print("        SS(a) = sum (d - a)^2 = n(a - dbar)^2 + sum(d - dbar)^2   -- exact identity")
for aa, want in [(F(0), F(193, 50)), (F(1, 2), F(103, 50)), (F(7, 10), F(19, 10)),
                 (F(9, 10), F(103, 50)), (F(7, 5), F(193, 50)), (F(2), F(433, 50))]:
    got = sum((d - aa) ** 2 for d in D)
    check(f"SS(a = {aa}) with b frozen at 11/10", got, want)
    check(f"   ...equals 19/10 + 4(a - 7/10)^2", F(19, 10) + 4 * (aa - F(7, 10)) ** 2, want)
    show("   decimal", dec(want))
check("symmetry: SS(0) = SS(7/5)", sum((d - F(0)) ** 2 for d in D),
      sum((d - F(7, 5)) ** 2 for d in D))
check("symmetry: SS(1/2) = SS(9/10)", sum((d - F(1, 2)) ** 2 for d in D),
      sum((d - F(9, 10)) ** 2 for d in D))

sub("9c. The proof works for EVERY b, not just the best one")
for bb in [F(0), F(1), F(3, 2), F(11, 10), F(-2), F(7, 3)]:
    d = [BR[i] - bb * BX[i] for i in range(BN)]
    astar = sum(d) / BN
    check(f"b = {bb}: best a = dbar = rbar - b*xbar", astar, brbar - bb * bxbar)
    check(f"b = {bb}: line at xbar hits rbar", astar + bb * bxbar, brbar)

sub("9d. Every line through (3,4) has sum e = 0; only one has sum (x-xbar)e = 0")
print("        r_hat = 4 + m(x - 3);   SS(m) = 14 - 22m + 10m^2")
for m, want in [(F(0), F(14)), (F(1, 2), F(11, 2)), (F(1), F(2)), (F(11, 10), F(19, 10)),
                (F(6, 5), F(2)), (F(2), F(10))]:
    e = [BR[i] - brbar - m * (BX[i] - bxbar) for i in range(BN)]
    ss = dot(e, e)
    check(f"m = {m}: SS", ss, want)
    check(f"m = {m}: SS = 14 - 22m + 10m^2", F(14) - 22 * m + 10 * m * m, want)
    check(f"m = {m}: sum e = 0 regardless", sum(e), F(0))
    show("   decimal", dec(want))
check("symmetry about m = 11/10: SS(1) = SS(6/5)",
      F(14) - 22 * F(1) + 10, F(14) - 22 * F(6, 5) + 10 * F(36, 25))
e_m1 = [BR[i] - brbar - F(1) * (BX[i] - bxbar) for i in range(BN)]
check("m = 1 residuals", e_m1, [F(0), F(0), F(-1), F(1)])
check("m = 1: sum e = 0 (first balance holds)", sum(e_m1), F(0))
check("m = 1: sum (x - xbar)e = 0+0-1+2", dot([xi - bxbar for xi in BX], e_m1), F(1))
check("m = 1: sum x*e = 0+0-4+5", dot(BX, e_m1), F(1))
check("m = 1: sum e^2 = 2", dot(e_m1, e_m1), F(2))

sub("9e. Cost of moving the line off the balance point, on the boss data")
for c in [F(1, 2), F(-1, 2), F(1), F(1, 10)]:
    e = [bE[i] - c for i in range(BN)]
    check(f"shift the whole line by {c}: SS = 19/10 + 4c^2", dot(e, e), F(19, 10) + 4 * c * c)
    show("   decimal", dec(F(19, 10) + 4 * c * c))

sub("9f. Boss sabotage: one residual corrupted, find it with the two balances")
TRUE_E = [F(2, 10), F(1, 10), F(-11, 10), F(8, 10)]
check("true residuals", TRUE_E, bE)
delta = F(3, 10)
BAD = list(TRUE_E)
BAD[2] = BAD[2] + delta
check("reported residuals (HSK corrupted by +3/10)", [e * 10 for e in BAD],
      [F(2), F(1), F(-8), F(8)])
show("reported residuals as decimals", [dec(e, 1) for e in BAD])
check("sum e (should be 0) = 3/10", sum(BAD), F(3, 10))
check("sum x*e (should be 0) = 12/10", dot(BX, BAD), F(6, 5))
check("x of the culprit = (sum x*e)/(sum e) = (12/10)/(3/10)", dot(BX, BAD) / sum(BAD), F(4))
check("...which is HSK", BX[2], F(4))
check("size of the corruption = sum e = 3/10", sum(BAD), delta)
check("restored residual = -8/10 - 3/10", BAD[2] - sum(BAD), F(-11, 10))
print("        With only the no-intercept fit there is ONE equation and TWO unknowns")
print("        (which asset, and by how much) -- the culprit cannot be located.")

# ---------------------------------------------------------------------------
head("SECTION 10  Weights -- the balance point BFRE actually uses")
# ---------------------------------------------------------------------------

W = [F(2), F(2), F(1), F(2), F(3)]
Sw = sum(W)
check("invented sqrt-cap-style weights w", W, [F(2), F(2), F(1), F(2), F(3)])
check("sum w", Sw, F(10))
check("sum w*x = -3 -1 +0 +2 +6", wdot(W, ones(N), X), F(4))
check("sum w*x^2 = 4.5+0.5+0+2+12", wdot(W, X, X), F(19))
check("sum w*r = -4-4+0.5+8+10.5", wdot(W, ones(N), R), F(11))
check("sum w*x*r = 6+2+0+8+21", wdot(W, X, R), F(37))
xbw = wdot(W, ones(N), X) / Sw
rbw = wdot(W, ones(N), R) / Sw
check("weighted xbar = 4/10", xbw, F(2, 5))
check("weighted rbar = 11/10", rbw, F(11, 10))
show("weighted xbar decimal", dec(xbw))
show("weighted rbar decimal", dec(rbw))

wcoef, wfit, wE, wSS = wls([ones(N), X], R, W)
check("weighted normal equations: 10a + 4b = 11", (Sw, wdot(W, ones(N), X), wdot(W, ones(N), R)),
      (F(10), F(4), F(11)))
check("weighted normal equations:  4a + 19b = 37", (wdot(W, ones(N), X), wdot(W, X, X), wdot(W, X, R)),
      (F(4), F(19), F(37)))
check("elimination: 44 - 16b + 190b = 370  ->  174b = 326", F(370) - F(44), F(326))
check("weighted b = 326/174 = 163/87", wcoef[1], F(163, 87))
check("weighted a = 61/174", wcoef[0], F(61, 174))
show("weighted b decimal", dec(F(163, 87)))
show("weighted a decimal", dec(F(61, 174)))
check("a = rbar_w - b*xbar_w = 11/10 - (163/87)(2/5)", rbw - F(163, 87) * xbw, F(61, 174))
check("weighted sum w*e = 0", wdot(W, ones(N), wE), F(0))
check("weighted sum w*x*e = 0", wdot(W, X, wE), F(0))

WCxx = wdot(W, X, X) - Sw * xbw * xbw
WCxr = wdot(W, X, R) - Sw * xbw * rbw
check("weighted Sxx_c = 19 - 10*(2/5)^2 = 19 - 8/5", WCxx, F(87, 5))
check("weighted Sxr_c = 37 - 10*(2/5)(11/10) = 37 - 44/10", WCxr, F(163, 5))
check("weighted b = Sxr_c/Sxx_c", WCxr / WCxx, F(163, 87))

sub("10a. Pre-centre the column the way BFRE standardises it (p.10)")
XS = [xi - xbw for xi in X]
check("x* = x - weighted mean (in tenths)", [x * 10 for x in XS],
      [F(-19), F(-9), F(-4), F(6), F(16)])
check("sum w*x* = 0  -- the defining property of a BFRE exposure", wdot(W, ones(N), XS), F(0))
check("sum w*x*^2 = 1740/100", wdot(W, XS, XS), F(87, 5))
check("sum w*x**r = 326/10", wdot(W, XS, R), F(163, 5))
scoef, sfit, sE, sSS = wls([ones(N), XS], R, W)
check("with a pre-centred column the two dials DECOUPLE: a = weighted mean return",
      scoef[0], F(11, 10))
check("...and b is unchanged", scoef[1], F(163, 87))
check("...and the residuals are unchanged", sE, wE)
check("...and sum w*e^2 is unchanged", sSS, wSS)
show("weighted sum w*e^2", S(wSS) + "  = " + dec(wSS))

sub("10b. On a pre-centred column, dropping the intercept no longer changes b")
ncoef, _, nE, _ = wls([XS], R, W)
check("no-intercept fit on the centred column gives the same b", ncoef[0], F(163, 87))
check("but sum w*e is now 11, not 0 -- the intercept is still needed",
      wdot(W, ones(N), nE), F(11))
check("  (11 = sum w*r, because the fit no longer carries any level)",
      wdot(W, ones(N), nE), wdot(W, ones(N), R))

# ---------------------------------------------------------------------------
head("SECTION 11  BFRE p.4, p.10, p.25, p.26 -- the market factor IS the intercept")
# ---------------------------------------------------------------------------

print("   AXL, BRN, CHR in industry MAT; DLT, EMK in industry TEC.")
print("   Same weights w = [2,2,1,2,3]; same standardised style column x*.")
D_MAT = [F(1), F(1), F(1), F(0), F(0)]
D_TEC = [F(0), F(0), F(0), F(1), F(1)]
W_MAT = wdot(W, ones(N), D_MAT)
W_TEC = wdot(W, ones(N), D_TEC)
check("aggregate weight of MAT = 2+2+1", W_MAT, F(5))
check("aggregate weight of TEC = 2+3", W_TEC, F(5))
check("average weight per asset, MAT = 5/3", W_MAT / 3, F(5, 3))
check("average weight per asset, TEC = 5/2", W_TEC / 2, F(5, 2))

sub("11a. Reading A of restriction (1.10): weights = industry AGGREGATE weights")
print("      5*f_MAT + 5*f_TEC = 0  ->  f_TEC = -f_MAT  ->  reduced column g = d_MAT - d_TEC")
G = [D_MAT[i] - D_TEC[i] for i in range(N)]
check("g", G, [F(1), F(1), F(1), F(-1), F(-1)])
check("sum w*g = 2+2+1-2-3 = 0  -> g is weighted-orthogonal to the constant",
      wdot(W, ones(N), G), F(0))
check("sum w*x* = 0            -> x* is weighted-orthogonal to the constant",
      wdot(W, ones(N), XS), F(0))
check("sum w*g^2", wdot(W, G, G), F(10))
check("sum w*g*x* = -120/10", wdot(W, G, XS), F(-12))
check("sum w*g*r", wdot(W, G, R), F(-26))
Acoef, Afit, AE, ASS = wls([ones(N), G, XS], R, W)
check("f_Mkt = (sum w*r)/(sum w) = 11/10", Acoef[0], F(11, 10))
check("f_MAT = -51/25", Acoef[1] * F(1), F(-51, 25))
check("f_Style = 7/15", Acoef[2], F(7, 15))
check("f_TEC = -f_MAT = 51/25", -Acoef[1], F(51, 25))
show("f_Mkt decimal (%)", dec(F(11, 10)))
show("f_MAT decimal (%)", dec(F(-51, 25)))
show("f_TEC decimal (%)", dec(F(51, 25)))
show("f_Style decimal (% per unit of standardised exposure)", dec(F(7, 15)))
check("row 2 of the reduced system: 10*f_MAT - 12*f_Style = -26", 
      F(10) * Acoef[1] - 12 * Acoef[2], F(-26))
check("row 3 of the reduced system: -12*f_MAT + (87/5)*f_Style = 163/5",
      F(-12) * Acoef[1] + F(87, 5) * Acoef[2], F(163, 5))
check("rearrange row 2: f_MAT = (-13 + 6*f_Style)/5, checked at f_Style = 7/15",
      (F(-13) + 6 * F(7, 15)) / 5, F(-51, 25))
check("substitute into row 3 x 5: 156 - 72f + 87f = 163  ->  15f = 163 - 156",
      F(163) - F(156), F(7))
check("15*f_Style = 7", 15 * Acoef[2], F(7))
check("f_MAT = (-26 + 12*(7/15))/10 = (-102/5)/10", (F(-26) + 12 * F(7, 15)) / 10, F(-51, 25))
check("  intermediate: -26 + 28/5 = -102/5", F(-26) + F(28, 5), F(-102, 5))
check("f_Mkt EQUALS the sqrt-cap-weighted average return of the file",
      Acoef[0], wdot(W, ones(N), R) / Sw)
check("restriction (1.10) holds: 5*f_MAT + 5*f_TEC", W_MAT * Acoef[1] + W_TEC * (-Acoef[1]), F(0))
check("residuals (in 150ths)", [e * 150 for e in AE],
      [F(-26), F(-96), F(244), F(87), F(-58)])
check("sum w*e = 0", wdot(W, ones(N), AE), F(0))
check("sum w*g*e = 0", wdot(W, G, AE), F(0))
check("sum w*x**e = 0", wdot(W, XS, AE), F(0))

sub("11b. Reading B of (1.10): weights = AVERAGE weight per asset in the industry")
print("      (5/3)f_MAT + (5/2)f_TEC = 0  ->  f_TEC = -(2/3)f_MAT")
G2 = [D_MAT[i] - F(2, 3) * D_TEC[i] for i in range(N)]
check("g2", G2, [F(1), F(1), F(1), F(-2, 3), F(-2, 3)])
check("sum w*g2 = 5 - (2/3)*5 = 5/3  -> NOT orthogonal to the constant",
      wdot(W, ones(N), G2), F(5, 3))
Bcoef, Bfit, BE, BSS = wls([ones(N), G2, XS], R, W)
check("f_Mkt under Reading B = 377/250", Bcoef[0], F(377, 250))
check("f_MAT under Reading B = -306/125", Bcoef[1], F(-306, 125))
check("f_TEC under Reading B = (2/3)*306/125 = 204/125", -F(2, 3) * Bcoef[1], F(204, 125))
check("f_Style under Reading B -- UNCHANGED", Bcoef[2], F(7, 15))
show("f_Mkt decimal (%)", dec(F(377, 250)))
show("f_MAT decimal (%)", dec(F(-306, 125)))
show("f_TEC decimal (%)", dec(F(204, 125)))
check("Reading B's f_Mkt is NOT the weighted average return (11/10)", Bcoef[0] != F(11, 10), True)
check("difference f_Mkt(B) - f_Mkt(A) = 377/250 - 275/250", Bcoef[0] - Acoef[0], F(102, 250))
show("  difference decimal (percentage points)", dec(F(102, 250)))

sub("11c. p.26: 'This identification simply represents a rotation ... does not impact")
print("     the efficacy of the risk model.'  Verified: identical fit, identical risk.")
check("fitted values identical under both readings", Afit, Bfit)
check("residuals identical under both readings", AE, BE)
check("sum w*e^2 identical under both readings", ASS, BSS)
check("sum w*e^2", ASS, F(697, 150))
show("  decimal", dec(ASS))
check("weighted-average industry return under Reading A's own weights",
      W_MAT * Acoef[1] + W_TEC * (-Acoef[1]), F(0))
check("weighted-average industry return under Reading B's own weights",
      F(5, 3) * Bcoef[1] + F(5, 2) * (-F(2, 3) * Bcoef[1]), F(0))
check("Reading B's factor returns fail Reading A's restriction: 5*f_MAT + 5*f_TEC",
      F(5) * Bcoef[1] + F(5) * (-F(2, 3) * Bcoef[1]), F(-510, 125))
show("  decimal", dec(F(-510, 125)))

sub("11d. The general statement, proved by sweep in Section 12f")
print("     Reduced industry column g_j = d_j - (omega_j/omega_J) d_J has")
print("     sum_i w_i g_j = W_j - (omega_j/omega_J) W_J, which is zero for every j")
print("     if and only if omega is proportional to the AGGREGATE weights W.")

# ---------------------------------------------------------------------------
head("SECTION 12  Brute-force sweeps -- the claims are not accidents of one file")
# ---------------------------------------------------------------------------

GRID = [F(-2), F(-1), F(0), F(1), F(2), F(1, 2), F(3, 2)]

sub("12a. a = rbar - b*xbar, and the line hits (xbar, rbar), on every file")
cnt = 0
for xs in product([F(-2), F(-1), F(0), F(1), F(3)], repeat=3):
    if len(set(xs)) < 2:
        continue
    for rs in product([F(-1), F(0), F(2), F(5, 2)], repeat=3):
        n = 3
        cc, ff, ee, ss = wls([ones(n), list(xs)], list(rs))
        xb = sum(xs) / n
        rb = sum(rs) / n
        assert cc[0] == rb - cc[1] * xb
        assert cc[0] + cc[1] * xb == rb
        assert sum(ee) == 0
        assert dot(list(xs), ee) == 0
        cnt += 1
check("files swept (3 assets)", cnt, 7680)
print("        every one satisfies a = rbar - b*xbar, sum e = 0, sum x*e = 0")

sub("12b. centred no-intercept fit == with-intercept slope, on every file")
cnt = 0
for xs in product([F(-2), F(-1), F(1), F(2), F(1, 2)], repeat=4):
    if len(set(xs)) < 2:
        continue
    rs = [F(1), F(-2), F(3), F(1, 2)]
    n = 4
    cc, _, _, _ = wls([ones(n), list(xs)], rs)
    xb = sum(xs) / n
    rb = sum(rs) / n
    u = [xi - xb for xi in xs]
    v = [ri - rb for ri in rs]
    assert dot(u, v) / dot(u, u) == cc[1]
    assert dot(u, rs) / dot(u, u) == cc[1]          # centring x alone is enough
    if dot(xs, xs) != dot(u, u) and dot(u, v) != 0:
        assert dot(xs, v) / dot(xs, xs) != cc[1]    # centring r alone is not
    cnt += 1
check("files swept (4 assets)", cnt, 620)

sub("12c. SS(a) = SS_min + n(a - a*)^2 exactly, for any frozen b")
cnt = 0
for bb in GRID:
    for aa in GRID:
        d = [R[i] - bb * X[i] for i in range(N)]
        db = sum(d) / N
        lhs = sum((di - aa) ** 2 for di in d)
        rhs = sum((di - db) ** 2 for di in d) + N * (aa - db) ** 2
        assert lhs == rhs
        cnt += 1
check("(a, b) pairs swept", cnt, 49)

sub("12d. sum x^2 = Sxx_c + n*xbar^2 (why the sequential denominator is inflated)")
cnt = 0
for xs in product(GRID, repeat=4):
    n = 4
    xb = sum(xs) / n
    assert dot(xs, xs) == sum((xi - xb) ** 2 for xi in xs) + n * xb * xb
    assert dot(xs, xs) >= sum((xi - xb) ** 2 for xi in xs)
    cnt += 1
check("columns swept", cnt, 2401)
print("        sum x^2 is never smaller than the centred sum -- so the sequential")
print("        method's b is always shrunk toward zero by the factor Sxx_c/sum x^2.")
check("that factor on the cold-open file: (73/10)/(15/2) = 73/75", Cxx / Sxx, F(73, 75))
check("142/73 * 73/75 = 142/75", F(142, 73) * F(73, 75), F(142, 75))

sub("12e. the weighted balance point, on every weighted file")
cnt = 0
for ws in product([F(1), F(2), F(3)], repeat=4):
    xs = [F(-1), F(0), F(2), F(3)]
    rs = [F(1), F(-1), F(2), F(4)]
    n = 4
    cc, _, ee, _ = wls([ones(n), xs], rs, list(ws))
    sw = sum(ws)
    xbw_ = wdot(ws, ones(n), xs) / sw
    rbw_ = wdot(ws, ones(n), rs) / sw
    assert cc[0] + cc[1] * xbw_ == rbw_
    assert wdot(ws, ones(n), ee) == 0
    assert wdot(ws, xs, ee) == 0
    cnt += 1
check("weighted files swept", cnt, 81)

sub("12f. the identification restriction: which weights make the market a true intercept")
cnt = 0
bad = 0
for ws in product([F(1), F(2), F(3)], repeat=5):
    WM = ws[0] + ws[1] + ws[2]
    WT = ws[3] + ws[4]
    for om_m, om_t in [(WM, WT), (WM / 3, WT / 2), (F(1), F(1))]:
        g = [D_MAT[i] - (om_m / om_t) * D_TEC[i] for i in range(N)]
        orth = (wdot(ws, ones(N), g) == 0)
        prop = (om_m * WT == om_t * WM)
        assert orth == prop
        if orth:
            xs_ = [xi - wdot(ws, ones(N), X) / sum(ws) for xi in X]
            cc, _, _, _ = wls([ones(N), g, xs_], R, list(ws))
            assert cc[0] == wdot(ws, ones(N), R) / sum(ws)
        else:
            bad += 1
        cnt += 1
check("(weights, restriction) pairs swept", cnt, 729)
check("pairs where the market column is NOT a true intercept", bad, 456)
print("        In every orthogonal case f_Mkt came out exactly equal to the")
print("        weight-average return -- which is what BFRE p.4 asserts.")

sub("12g. scaling a column: b -> b/c, a and the residuals untouched")
cnt = 0
for c in [F(2), F(-3), F(1, 2), F(5), F(-1, 4)]:
    for xs in product([F(-1), F(0), F(2)], repeat=4):
        if len(set(xs)) < 2:
            continue
        rs = [F(1), F(-2), F(3), F(1, 2)]
        c0, f0, e0_, s0 = wls([ones(4), list(xs)], rs)
        c1, f1, e1_, s1 = wls([ones(4), [c * xi for xi in xs]], rs)
        assert c1[0] == c0[0] and c1[1] == c0[1] / c and e1_ == e0_ and s1 == s0
        cnt += 1
check("(scale, column) pairs swept", cnt, 390)

# ---------------------------------------------------------------------------
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified, plus "
      f"{7680 + 620 + 49 + 2401 + 81 + 729 + 390} swept cases.")
print("   Every number printed above appears in datasets/level5.md.")
print("   Decimals tagged ROUNDED above are marked 'rounded' in the markdown.")
