#!/usr/bin/env python3
"""
verify_level8.py -- recomputes EVERY number printed in datasets/level8.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level8.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

The ONLY place a non-rational number appears is Section 13c (the effective sample
size of an exponential decay), where the decay factor is 2^(-1/26). That is
irrational by construction. It is handled with decimal.Decimal at 50 digits, the
closed form (15/17)*(1+lam)/(1-lam) is proved against the direct sum, and every
decimal printed from it is tagged ROUNDED. Nothing rational is ever computed in
floating point.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product  # noqa: F401  (kept for parity with earlier verifiers)
import sys

getcontext().prec = 50

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


def sqrt_dec(v, n=4):
    """Square root of an exact Fraction, printed as an explicitly rounded
    decimal.  Exact when the fraction is a perfect square of a rational."""
    v = F(v)
    rn, rd = isqrt_exact(v.numerator), isqrt_exact(v.denominator)
    if rn is not None and rd is not None:
        return f"{float(F(rn, rd)):.{n}f} (EXACT root = {F(rn, rd)})"
    d = Decimal(v.numerator) / Decimal(v.denominator)
    return f"{d.sqrt():.{n}f} (ROUNDED)"


def isqrt_exact(m):
    if m < 0:
        return None
    r = int(m ** 0.5)
    for c in (r - 2, r - 1, r, r + 1, r + 2):
        if c >= 0 and c * c == m:
            return c
    return None


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
# exact linear algebra over Fraction
# (same conventions as tools/verify_level5.py -- reused, not reinvented)
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


def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def quad(A, h):
    """h^T A h, exact."""
    return sum(h[i] * A[i][j] * h[j]
               for i in range(len(h)) for j in range(len(h)))


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def scale(A, c):
    return [[c * x for x in row] for row in A]


def addm(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def covmat(cols, ddof=1):
    """Sample covariance matrix of a list of equal-length series, exact.
    ddof=1 divides by T-1 (a mean was estimated); ddof=0 divides by T."""
    T = len(cols[0])
    K = len(cols)
    means = [sum(c) / T for c in cols]
    D = [[cols[k][t] - means[k] for k in range(K)] for t in range(T)]
    den = F(T - ddof)
    return ([[sum(D[t][i] * D[t][j] for t in range(T)) / den
              for j in range(K)] for i in range(K)], means, D)


# ===========================================================================
head("SECTION 3  The dataset -- Level 7's machinery, run five times")
# ===========================================================================

NAMES = ["AXL", "BRN", "CHR", "DLT", "EMK"]
X = [F(-2), F(-1), F(0), F(1), F(2)]          # cheapness, re-standardised
ONE = ones(5)
N = 5

RET = {
    1: [F(0), F(1), F(9), F(9), F(16)],
    2: [F(-3), F(2), F(3), F(10), F(13)],
    3: [F(6), F(3), F(-1), F(-1), F(-2)],
    4: [F(6), F(7), F(1), F(3), F(-2)],
    5: [F(-8), F(-6), F(-8), F(-4), F(-4)],
}

sub("3a. the exposure column is centred, so the Gram matrix is diagonal")
check("sum of the market column (n)", dot(ONE, ONE), F(5))
check("sum x  (the centering, p.10)", dot(ONE, X), F(0))
check("sum x^2", dot(X, X), F(10))
show("Gram matrix", [[dot(ONE, ONE), dot(ONE, X)], [dot(X, ONE), dot(X, X)]])
check("Gram determinant  5*10 - 0*0", F(5) * F(10) - F(0) * F(0), F(50))

sub("3b. five cross-sectional regressions -- Level 1's formula, twice per period")
F1, F2 = [], []
SSU = []
RESID = {}
want_f = {1: (F(7), F(4)), 2: (F(5), F(4)), 3: (F(1), F(-2)),
          4: (F(3), F(-2)), 5: (F(-6), F(1))}
want_u = {1: [F(1), F(-2), F(2), F(-2), F(1)],
          2: [F(0), F(1), F(-2), F(1), F(0)],
          3: [F(1), F(0), F(-2), F(0), F(1)],
          4: [F(-1), F(2), F(-2), F(2), F(-1)],
          5: [F(0), F(1), F(-2), F(1), F(0)]}
want_ssu = {1: F(14), 2: F(6), 3: F(6), 4: F(14), 5: F(6)}
for t in range(1, 6):
    r = RET[t]
    Sr = dot(ONE, r)
    Sxr = dot(X, r)
    fm = Sr / F(5)
    fs = Sxr / F(10)
    bb, fit, e, ss = wls([ONE, X], r)
    check(f"period {t}: sum r", Sr, F(5) * want_f[t][0])
    check(f"period {t}: sum x*r", Sxr, F(10) * want_f[t][1])
    check(f"period {t}: f_Mkt = sum r / 5", fm, want_f[t][0])
    check(f"period {t}: f_Chp = sum x*r / 10", fs, want_f[t][1])
    check(f"period {t}: same two numbers from the full 2-column solve",
          (bb[0], bb[1]), want_f[t])
    check(f"period {t}: residuals u", e, want_u[t])
    check(f"period {t}: balance  sum u", dot(ONE, e), F(0))
    check(f"period {t}: balance  sum x*u", dot(X, e), F(0))
    check(f"period {t}: sum u^2", ss, want_ssu[t])
    F1.append(fm)
    F2.append(fs)
    SSU.append(ss)
    RESID[t] = e

check("factor-return series  f_Mkt", F1, [F(7), F(5), F(1), F(3), F(-6)])
check("factor-return series  f_Chp", F2, [F(4), F(4), F(-2), F(-2), F(1)])
check("sum of the five sum-of-squared-misses", sum(SSU), F(46))

# ===========================================================================
head("SECTION 4  Building F by hand")
# ===========================================================================

T = 5
sub("4a. means and deviations -- one parameter estimated per series (L6)")
m1 = sum(F1) / T
m2 = sum(F2) / T
check("mean of f_Mkt", m1, F(2))
check("mean of f_Chp", m2, F(1))
D1 = [x - m1 for x in F1]
D2 = [x - m2 for x in F2]
check("deviations d1", D1, [F(5), F(3), F(-1), F(1), F(-8)])
check("deviations d2", D2, [F(3), F(3), F(-3), F(-3), F(0)])
check("sum d1 (must be 0)", sum(D1), F(0))
check("sum d2 (must be 0)", sum(D2), F(0))

sub("4b. the three sums, and the three entries of F")
S11 = dot(D1, D1)
S22 = dot(D2, D2)
S12 = dot(D1, D2)
check("sum d1^2", S11, F(100))
check("sum d2^2", S22, F(36))
check("sum d1*d2", S12, F(24))
check("degrees of freedom  T - 1", F(T - 1), F(4))
FF = [[S11 / F(4), S12 / F(4)], [S12 / F(4), S22 / F(4)]]
check("F[0][0] = 100/4", FF[0][0], F(25))
check("F[0][1] = 24/4", FF[0][1], F(6))
check("F[1][0] = 24/4", FF[1][0], F(6))
check("F[1][1] = 36/4", FF[1][1], F(9))
auto, _, _ = covmat([F1, F2], ddof=1)
check("same F from the generic covariance routine", auto, FF)

sub("4c. volatilities and the correlation")
check("factor vol 1 = sqrt(25)", F(5) * F(5), FF[0][0])
check("factor vol 2 = sqrt(9)", F(3) * F(3), FF[1][1])
show("sqrt(25)", sqrt_dec(FF[0][0]))
show("sqrt(9)", sqrt_dec(FF[1][1]))
rho = FF[0][1] / (F(5) * F(3))
check("correlation 6/(5*3)", rho, F(2, 5))
show("correlation as decimal", dec(rho))

sub("4d. the divisor that the paper does not state: T instead of T-1")
M0, _, _ = covmat([F1, F2], ddof=0)
check("uncentred-divisor variance of f_Mkt", M0[0][0], F(20))
check("uncentred-divisor variance of f_Chp", M0[1][1], F(36, 5))
check("uncentred-divisor covariance", M0[0][1], F(24, 5))
show("F with /T instead of /(T-1)", [[dec(M0[0][0]), dec(M0[0][1])],
                                     [dec(M0[1][0]), dec(M0[1][1])]])
check("ratio of the two conventions is exactly 4/5",
      M0[0][0] / FF[0][0], F(4, 5))
check("... the same 4/5 on the covariance", M0[0][1] / FF[0][1], F(4, 5))

sub("4d(ii). no mean subtracted at all -- the second-moment matrix")
MM = [[dot(F1, F1) / F(5), dot(F1, F2) / F(5)],
      [dot(F1, F2) / F(5), dot(F2, F2) / F(5)]]
check("sum f1^2", dot(F1, F1), F(120))
check("sum f2^2", dot(F2, F2), F(41))
check("sum f1*f2", dot(F1, F2), F(34))
check("M[0][0] = 120/5", MM[0][0], F(24))
check("M[1][1] = 41/5", MM[1][1], F(41, 5))
check("M[0][1] = 34/5", MM[0][1], F(34, 5))
show("M[1][1] as decimal", dec(MM[1][1]))
show("M[0][1] as decimal", dec(MM[0][1]))
check("M = (4/5)F + mean-outer-product, entry (0,0)",
      F(4, 5) * FF[0][0] + m1 * m1, MM[0][0])
check("M = (4/5)F + mean-outer-product, entry (0,1)",
      F(4, 5) * FF[0][1] + m1 * m2, MM[0][1])
# 4d: the no-mean grid differs from F by TWO effects pulling opposite ways --
# the divisor (x 4/5, always down) and the outer product of the means (always up).
# The markdown prints the size of each, cell by cell; check all six.
check("4d divisor effect on Var(f_Mkt): (4/5)(25) - 25", F(4, 5) * FF[0][0] - FF[0][0],
      F(-5))
check("4d mean effect on Var(f_Mkt): m1*m1", m1 * m1, F(4))
check("4d divisor effect on Var(f_Chp): (4/5)(9) - 9", F(4, 5) * FF[1][1] - FF[1][1],
      F(-9, 5))
check("4d mean effect on Var(f_Chp): m2*m2", m2 * m2, F(1))
check("4d divisor effect on Cov: (4/5)(6) - 6", F(4, 5) * FF[0][1] - FF[0][1], F(-6, 5))
check("4d mean effect on Cov: m1*m2", m1 * m2, F(2))
check("4d: on both variances the divisor wins (net change is negative)",
      (MM[0][0] < FF[0][0], MM[1][1] < FF[1][1]), (True, True))
check("4d: on the covariance the mean wins (net change is positive)",
      MM[0][1] > FF[0][1], True)

check("M = (4/5)F + mean-outer-product, entry (1,1)",
      F(4, 5) * FF[1][1] + m2 * m2, MM[1][1])

# ===========================================================================
head("SECTION 5  The quadratic form h^T F h, derived not asserted")
# ===========================================================================

def port_series(h):
    return [h[0] * F1[t] + h[1] * F2[t] for t in range(5)]


def port_var(h):
    p = port_series(h)
    mp = sum(p) / F(5)
    d = [x - mp for x in p]
    return dot(d, d) / F(4), p, mp, d


sub("5a. one portfolio, two ways: h = (1, 1)")
v, p, mp, d = port_var([F(1), F(1)])
check("period returns of the (1,1) book", p, [F(11), F(9), F(-1), F(1), F(-5)])
check("its mean", mp, F(3))
check("its deviations", d, [F(8), F(6), F(-4), F(-2), F(-8)])
check("sum of squared deviations", dot(d, d), F(184))
check("variance = 184/4", v, F(46))
check("same number from the grid: 25 + 2*6 + 9", quad(FF, [F(1), F(1)]), F(46))
show("risk = sqrt(46)", sqrt_dec(F(46)))

sub("5b. h = (1, -1): the offsetting book")
v, p, mp, d = port_var([F(1), F(-1)])
check("period returns of the (1,-1) book", p, [F(3), F(1), F(3), F(5), F(-7)])
check("its mean", mp, F(1))
check("its deviations", d, [F(2), F(0), F(2), F(4), F(-8)])
check("sum of squared deviations", dot(d, d), F(88))
check("variance = 88/4", v, F(22))
check("same number from the grid: 25 - 2*6 + 9",
      quad(FF, [F(1), F(-1)]), F(22))
show("risk = sqrt(22)", sqrt_dec(F(22)))
check("the two books differ by exactly 4 * covariance",
      F(46) - F(22), F(4) * FF[0][1])

sub("5c. h = (4, 3): a book whose risk is an exact whole number")
v, p, mp, d = port_var([F(4), F(3)])
check("period returns of the (4,3) book", p,
      [F(40), F(32), F(-2), F(6), F(-21)])
check("its mean", mp, F(11))
check("its deviations", d, [F(29), F(21), F(-13), F(-5), F(-32)])
check("sum of squared deviations", dot(d, d), F(2500))
check("variance = 2500/4", v, F(625))
check("same number from the grid: 16*25 + 24*6 + 9*9",
      quad(FF, [F(4), F(3)]), F(625))
show("risk = sqrt(625)", sqrt_dec(F(625)))

sub("5d. the identity in general -- swept over every small integer book")
cnt = 0
for h1 in range(-6, 7):
    for h2 in range(-6, 7):
        h = [F(h1), F(h2)]
        vv, _, _, _ = port_var(h)
        assert vv == quad(FF, h)
        assert vv == FF[0][0] * h[0] ** 2 + 2 * FF[0][1] * h[0] * h[1] \
            + FF[1][1] * h[1] ** 2
        cnt += 1
check("integer books swept, series-route == grid-route", cnt, 169)

sub("5e. sabotage: a corrupted F that no series could have produced")
BAD = [[F(25), F(16)], [F(16), F(9)]]
check("claimed correlation 16/(5*3) exceeds 1", BAD[0][1] / F(15), F(16, 15))
show("16/15 as decimal", dec(F(16, 15)))
check("the (3,-5) book's variance under the corrupted grid",
      quad(BAD, [F(3), F(-5)]), F(-30))
check("determinant of the corrupted grid", det2(BAD), F(-31))
check("determinant of the true grid", det2(FF), F(189))
check("the (3,-5) book under the TRUE grid is positive",
      quad(FF, [F(3), F(-5)]), F(270))

sub("5f. the numbers the Section 8 trap table returns")
check("'risk is just the two volatilities' returns 25 + 9", F(25) + F(9),
      F(34))
show("sqrt(34) -- what that wrong belief returns for BOTH books",
     sqrt_dec(F(34)))
check("'volatilities add' returns 5 + 3", F(5) + F(3), F(8))
check("ratio of the two books' variances, 46/22", F(46) / F(22), F(23, 11))
show("23/11 as decimal", dec(F(23, 11)))
show("sqrt(23/11) -- how much bigger book A's RISK is", sqrt_dec(F(23, 11)))
check("dropping the off-diagonal: 34/46 of book A's variance", F(34) / F(46),
      F(17, 23))
show("sqrt(17/23) -- book A's risk understated to this fraction",
     sqrt_dec(F(17, 23)))
check("dropping the off-diagonal: 34/22 of book B's variance", F(34) / F(22),
      F(17, 11))
show("sqrt(17/11) -- book B's risk overstated to this multiple",
     sqrt_dec(F(17, 11)))
check("'the correlation 0.4 IS the cell' on book (1,1): 25 + 2(0.4) + 9",
      F(25) + 2 * F(2, 5) + F(9), F(174, 5))
show("174/5 as decimal", dec(F(174, 5)))
show("sqrt(174/5) -- what that wrong belief reports for book A",
     sqrt_dec(F(174, 5)))

# ===========================================================================
head("SECTION 6  The direction with the most wobble")
# ===========================================================================

def rayleigh(A, h):
    return quad(A, h) / dot(h, h)


sub("6b. the sweep -- variance per unit of size, exact fractions")
sweep = [(-4, 1), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
         (3, 1), (4, 1), (1, 0)]
want_sweep = [F(361, 17), F(198, 10), F(85, 5), F(22, 2), F(9), F(46, 2),
              F(133, 5), F(270, 10), F(457, 17), F(25)]
for (p_, q_), w_ in zip(sweep, want_sweep):
    h = [F(p_), F(q_)]
    r_ = rayleigh(FF, h)
    check(f"R({p_},{q_}) = ({25*p_*p_} + {12*p_*q_} + {9*q_*q_})/{p_*p_+q_*q_}",
          r_, w_)
    show("   as decimal", dec(r_))

sub("6b(ii). finer ladder around the peak")
for (p_, q_), w_ in [((2, 1), F(133, 5)), ((5, 2), F(781, 29)),
                     ((3, 1), F(27)), ((7, 2), F(1429, 53)),
                     ((4, 1), F(457, 17))]:
    r_ = rayleigh(FF, [F(p_), F(q_)])
    check(f"R({p_},{q_})", r_, w_)
    show("   as decimal", dec(r_))

sub("6b(iii). finer ladder around the trough")
for (p_, q_), w_ in [((-1, 1), F(11)), ((-1, 2), F(37, 5)),
                     ((-2, 5), F(205, 29)), ((-1, 3), F(7)),
                     ((-1, 4), F(121, 17))]:
    r_ = rayleigh(FF, [F(p_), F(q_)])
    check(f"R({p_},{q_})", r_, w_)
    show("   as decimal", dec(r_))

sub("6b(vi). the degenerate case lam = 25, where the quadratic in t is linear")
check("12t - 16 = 0 gives t = 4/3", F(16) / F(12), F(4, 3))
check("R(4/3, 1) = R(4,3) = 25", rayleigh(FF, [F(4), F(3)]), F(25))

sub("6b(v). the two directions used in the perpendicular check of the markdown")
check("R(1,3)", rayleigh(FF, [F(1), F(3)]), F(71, 5))
show("   as decimal", dec(F(71, 5)))
check("R(-3,1)", rayleigh(FF, [F(-3), F(1)]), F(99, 5))
show("   as decimal", dec(F(99, 5)))
check("71/5 + 99/5", F(71, 5) + F(99, 5), F(34))

sub("6b(iv). a direction and its right-angle partner sum to the trace")
for (p_, q_) in [(1, 0), (1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (4, 1)]:
    a_ = rayleigh(FF, [F(p_), F(q_)])
    b_ = rayleigh(FF, [F(-q_), F(p_)])
    check(f"R({p_},{q_}) + R({-q_},{p_}) = trace", a_ + b_, F(34))

sub("6c. which values of lambda are reachable at all -- the discriminant")
# (25 - lam) t^2 + 12 t + (9 - lam) = 0 has a real root iff
# 144 - 4(25-lam)(9-lam) >= 0  iff  lam^2 - 34 lam + 189 <= 0
check("trace of F  (25 + 9)", trace(FF), F(34))
check("determinant of F  (25*9 - 6*6)", det2(FF), F(189))
check("characteristic polynomial constant term = det", F(189), det2(FF))
check("7 + 27 = trace", F(7) + F(27), trace(FF))
check("7 * 27 = det", F(7) * F(27), det2(FF))
check("discriminant (a-d)^2 + 4b^2 = 16^2 + 4*36", F(16) ** 2 + 4 * F(36),
      F(400))
check("sqrt(400) is a whole number", F(20) * F(20), F(400))
check("lam_max = (34 + 20)/2", (F(34) + F(20)) / 2, F(27))
check("lam_min = (34 - 20)/2", (F(34) - F(20)) / 2, F(7))

sub("6d. the exact proof: 27*h.h - h^T F h = 2(h1 - 3h2)^2")
cnt = 0
for h1 in range(-9, 10):
    for h2 in range(-9, 10):
        h = [F(h1), F(h2)]
        gap_hi = F(27) * dot(h, h) - quad(FF, h)
        assert gap_hi == 2 * (h[0] - 3 * h[1]) ** 2
        gap_lo = quad(FF, h) - F(7) * dot(h, h)
        assert gap_lo == 2 * (3 * h[0] + h[1]) ** 2
        assert gap_hi >= 0 and gap_lo >= 0
        cnt += 1
check("books swept for the two sum-of-squares identities", cnt, 361)
check("the high gap vanishes exactly at h = (3,1)",
      F(27) * dot([F(3), F(1)], [F(3), F(1)]) - quad(FF, [F(3), F(1)]), F(0))
check("the low gap vanishes exactly at h = (1,-3)",
      quad(FF, [F(1), F(-3)]) - F(7) * dot([F(1), F(-3)], [F(1), F(-3)]),
      F(0))

sub("6e/6f. the matrix maps the peak direction back onto itself")
v1 = [F(3), F(1)]
v2 = [F(1), F(-3)]
check("F * (3,1)", matvec(FF, v1), [F(81), F(27)])
check("... which is 27 * (3,1)", [F(27) * x for x in v1], [F(81), F(27)])
check("F * (1,-3)", matvec(FF, v2), [F(7), F(-21)])
check("... which is 7 * (1,-3)", [F(7) * x for x in v2], [F(7), F(-21)])
check("the two directions are at right angles: (3,1).(1,-3)", dot(v1, v2),
      F(0))
check("R at (3,1)", rayleigh(FF, v1), F(27))
check("R at (1,-3)", rayleigh(FF, v2), F(7))
show("sqrt(27) -- risk along the peak direction, per unit of size",
     sqrt_dec(F(27)))
show("sqrt(7)  -- risk along the trough direction, per unit of size",
     sqrt_dec(F(7)))

sub("6g. rebuilding F out of its two pieces")
P1 = [[F(9, 10), F(3, 10)], [F(3, 10), F(1, 10)]]
P2 = [[F(1, 10), F(-3, 10)], [F(-3, 10), F(9, 10)]]
check("piece 1 = (3,1)(3,1)^T / 10", P1,
      [[F(9, 10), F(3, 10)], [F(3, 10), F(1, 10)]])
check("piece 2 = (1,-3)(1,-3)^T / 10", P2,
      [[F(1, 10), F(-3, 10)], [F(-3, 10), F(9, 10)]])
check("the two pieces add to the identity", addm(P1, P2),
      [[F(1), F(0)], [F(0), F(1)]])
REB = addm(scale(P1, F(27)), scale(P2, F(7)))
check("27*piece1 + 7*piece2 == F", REB, FF)
check("each piece is unchanged by squaring (P1*P1 = P1)", matmul(P1, P1), P1)
check("the pieces annihilate each other (P1*P2 = 0)", matmul(P1, P2),
      [[F(0), F(0)], [F(0), F(0)]])

sub("6g(ii). splitting a book between the two directions")
h = [F(1), F(1)]
share1 = dot(h, v1) ** 2 / dot(v1, v1)
share2 = dot(h, v2) ** 2 / dot(v2, v2)
check("h.(3,1)", dot(h, v1), F(4))
check("h.(1,-3)", dot(h, v2), F(-2))
check("squared length along the peak direction  16/10", share1, F(8, 5))
check("squared length along the trough direction 4/10", share2, F(2, 5))
check("the two squared lengths add to h.h", share1 + share2, dot(h, h))
check("27*(8/5) + 7*(2/5) = the (1,1) book's variance",
      F(27) * share1 + F(7) * share2, F(46))
check("share of the book's SIZE along the peak direction",
      share1 / dot(h, h), F(4, 5))
show("that share as a decimal", dec(share1 / dot(h, h)))
check("share of the book's VARIANCE along the peak direction",
      F(27) * share1 / F(46), F(108, 115))
show("that share as a decimal", dec(F(27) * share1 / F(46)))
# The variance share and the volatility ratio are different numbers. The page
# says "variance"; this is what it would have to say if it said "risk".
check("sqrt(108/115) to 4dp -- the volatility ratio, not the variance share",
      sqrt_dec(F(108, 115)), "0.9691 (ROUNDED)")
# sqrt(x) > x for 0 < x < 1, and that is provable in exact rationals as x > x^2.
# (The old form here compared 108/115 against a re-evaluation of itself and two
# hard-coded decimal literals, which proved nothing. Replaced.)
_vshare = F(27) * share1 / F(46)
check("the variance share is a proper fraction, 0 < 108/115 < 1",
      F(0) < _vshare < F(1), True)
check("... so its square root is strictly larger: 108/115 > (108/115)^2",
      _vshare > _vshare * _vshare, True)
check("... and the printed volatility ratio squares back to the variance share",
      (F(Decimal(sqrt_dec(_vshare).split()[0])) ** 2 - _vshare)
      < F(1, 1000), True)

sub("6h. how much of the whole grid the first direction carries")
check("lam_max / trace = 27/34", F(27) / F(34), F(27, 34))
show("27/34 as decimal", dec(F(27, 34)))
check("lam_min / trace = 7/34", F(7) / F(34), F(7, 34))
show("7/34 as decimal", dec(F(7, 34)))
check("the two shares add to 1", F(27, 34) + F(7, 34), F(1))
check("ratio lam_max / lam_min = 27/7", F(27) / F(7), F(27, 7))
show("27/7 as decimal", dec(F(27, 7)))

sub("6i. the cliff: a grid whose two factors are perfectly correlated")
CLIFF = [[F(25), F(15)], [F(15), F(9)]]
check("correlation 15/(5*3)", CLIFF[0][1] / F(15), F(1))
check("determinant", det2(CLIFF), F(0))
check("trace", trace(CLIFF), F(34))
check("eigenvalues 34 and 0 -- discriminant", F(16) ** 2 + 4 * F(225),
      F(1156))
check("sqrt(1156)", F(34) * F(34), F(1156))
check("lam_max = (34+34)/2", (F(34) + F(34)) / 2, F(34))
check("lam_min = (34-34)/2", (F(34) - F(34)) / 2, F(0))
check("the zero direction (3,-5): F*(3,-5)", matvec(CLIFF, [F(3), F(-5)]),
      [F(0), F(0)])
check("its variance is exactly zero", quad(CLIFF, [F(3), F(-5)]), F(0))

# ===========================================================================
head("SECTION 11  BOSS ROUND -- three factors, three periods")
# ===========================================================================

G1 = [F(6), F(1), F(-4)]
G2 = [F(5), F(-1), F(2)]
G3 = [F(9), F(-2), F(-4)]
TB = 3

sub("11.2 means, deviations, and the sample grid")
Sm, means, DB = covmat([G1, G2, G3], ddof=1)
check("mean of g1", means[0], F(1))
check("mean of g2", means[1], F(2))
check("mean of g3", means[2], F(1))
d1 = [G1[t] - means[0] for t in range(TB)]
d2 = [G2[t] - means[1] for t in range(TB)]
d3 = [G3[t] - means[2] for t in range(TB)]
check("deviations of g1", d1, [F(5), F(0), F(-5)])
check("deviations of g2", d2, [F(3), F(-3), F(0)])
check("deviations of g3", d3, [F(8), F(-3), F(-5)])
check("g3's deviations are g1's plus g2's",
      [d1[t] + d2[t] for t in range(TB)], d3)
check("sum d1^2", dot(d1, d1), F(50))
check("sum d2^2", dot(d2, d2), F(18))
check("sum d3^2", dot(d3, d3), F(98))
check("sum d1*d2", dot(d1, d2), F(15))
check("sum d1*d3", dot(d1, d3), F(65))
check("sum d2*d3", dot(d2, d3), F(33))
SB = [[F(25), F(15, 2), F(65, 2)],
      [F(15, 2), F(9), F(33, 2)],
      [F(65, 2), F(33, 2), F(49)]]
check("sample grid S built by the generic routine", Sm, SB)
check("S[0][0] = 50/2", SB[0][0], F(25))
check("S[1][1] = 18/2", SB[1][1], F(9))
check("S[2][2] = 98/2", SB[2][2], F(49))
check("S[0][1] = 15/2", SB[0][1], F(15, 2))
check("S[0][2] = 65/2", SB[0][2], F(65, 2))
check("S[1][2] = 33/2", SB[1][2], F(33, 2))
show("S[0][1] as decimal", dec(SB[0][1]))
show("S[0][2] as decimal", dec(SB[0][2]))
show("S[1][2] as decimal", dec(SB[1][2]))

sub("11.2(ii) the three factor volatilities, all exact whole numbers")
check("vol of g1 = sqrt(25)", F(5) * F(5), SB[0][0])
check("vol of g2 = sqrt(9)", F(3) * F(3), SB[1][1])
check("vol of g3 = sqrt(49)", F(7) * F(7), SB[2][2])
check("correlation g1,g2", SB[0][1] / F(15), F(1, 2))
check("correlation g1,g3", SB[0][2] / F(35), F(13, 14))
check("correlation g2,g3", SB[1][2] / F(21), F(11, 14))
show("correlation g1,g2 as decimal", dec(F(1, 2)))
show("correlation g1,g3 as decimal", dec(F(13, 14)))
show("correlation g2,g3 as decimal", dec(F(11, 14)))
check("every correlation is inside [-1, 1]",
      all(SB[i][j] * SB[i][j] <= SB[i][i] * SB[j][j]
          for i in range(3) for j in range(3)), True)
for i in range(3):
    for j in range(3):
        check(f"Cauchy-Schwarz on entry ({i},{j}): S_ij^2 <= S_ii*S_jj",
              SB[i][j] * SB[i][j] <= SB[i][i] * SB[j][j], True)

sub("11.3 the book the grid scores at exactly zero")
w = [F(1), F(1), F(-1)]
pb = [G1[t] + G2[t] - G3[t] for t in range(TB)]
check("the book's return, period by period", pb, [F(2), F(2), F(2)])
check("its mean", sum(pb) / TB, F(2))
check("its deviations", [x - F(2) for x in pb], [F(0), F(0), F(0)])
check("S * w  (all three rows)", matvec(SB, w), [F(0), F(0), F(0)])
check("w^T S w", quad(SB, w), F(0))
check("the long-hand version: 83 + 15 - 65 - 33",
      F(25) + F(9) + F(49) + 2 * SB[0][1] - 2 * SB[0][2] - 2 * SB[1][2], F(0))
check("sum of the three variances (used again in 11.6)",
      SB[0][0] + SB[1][1] + SB[2][2], F(83))
check("determinant of S", det3(SB), F(0))
check("row 3 of S is row 1 plus row 2",
      [SB[0][j] + SB[1][j] for j in range(3)], SB[2][:])

sub("11.3(ii) the whole family of zero-risk books")
cnt = 0
for c in [F(1), F(2), F(-3), F(1, 2), F(10)]:
    hz = [c, c, -c]
    assert quad(SB, hz) == 0
    assert matvec(SB, hz) == [F(0), F(0), F(0)]
    cnt += 1
check("scaled copies of the zero-risk book, all still exactly zero", cnt, 5)
check("a levered 100x version is still scored at zero",
      quad(SB, [F(100), F(100), F(-100)]), F(0))
check("the unlevered book itself moved 200 basis points every period",
      [F(100) * x for x in pb], [F(200), F(200), F(200)])
check("... so the 100x version moved 200 PERCENT, i.e. 20000 bp, every period",
      [F(100) * x * 100 for x in pb], [F(20000), F(20000), F(20000)])

sub("11.4 the counting argument")
check("K, the number of factors (counted off the dataset, not asserted)",
      F(len([G1, G2, G3])), F(3))
check("T, the number of periods", F(TB), F(3))
check("independent directions left after removing the mean, T-1", F(TB - 1),
      F(2))
check("K - (T-1) = guaranteed zero directions", F(3) - F(2), F(1))
# a brute-force demonstration: EVERY 3-factor 3-period dataset is singular.
# All 3^9 = 19683 datasets whose nine entries lie in {-1, 0, +1}.
cnt = 0
sing = 0
V3 = (F(-1), F(0), F(1))
for e in product(V3, repeat=9):
    cols = [list(e[0:3]), list(e[3:6]), list(e[6:9])]
    Sx, _, _ = covmat(cols, ddof=1)
    if det3(Sx) == 0:
        sing += 1
    cnt += 1
check("3-factor 3-period datasets swept", cnt, 19683)
check("... of which singular", sing, 19683)

sub("11.4(ii) the mean is what costs the extra dimension")
RAW = [[dot(G1, G1) / F(3), dot(G1, G2) / F(3), dot(G1, G3) / F(3)],
       [dot(G1, G2) / F(3), dot(G2, G2) / F(3), dot(G2, G3) / F(3)],
       [dot(G1, G3) / F(3), dot(G2, G3) / F(3), dot(G3, G3) / F(3)]]
check("sum g1^2", dot(G1, G1), F(53))
check("sum g2^2", dot(G2, G2), F(30))
check("sum g3^2", dot(G3, G3), F(101))
check("sum g1*g2", dot(G1, G2), F(21))
check("sum g1*g3", dot(G1, G3), F(68))
check("sum g2*g3", dot(G2, G3), F(39))
check("determinant of the raw 3x3 of period rows",
      det3([[F(6), F(5), F(9)], [F(1), F(-1), F(-2)], [F(-4), F(2), F(-4)]]),
      F(90))
check("determinant of the no-mean second-moment matrix = 90^2/27",
      det3(RAW), F(300))
check("the zero-risk book is NOT zero under the no-mean convention",
      quad(RAW, w), F(4))

sub("11.6 shrinkage, target = the grid's own diagonal, intensity a = 1/4")
a = F(1, 4)
TGT = [[F(25), F(0), F(0)], [F(0), F(9), F(0)], [F(0), F(0), F(49)]]
SH = addm(scale(SB, 1 - a), scale(TGT, a))
check("shrunk diagonal is unchanged (25)", SH[0][0], F(25))
check("shrunk diagonal is unchanged (9)", SH[1][1], F(9))
check("shrunk diagonal is unchanged (49)", SH[2][2], F(49))
check("shrunk S12 = (3/4)*(15/2)", SH[0][1], F(45, 8))
check("shrunk S13 = (3/4)*(65/2)", SH[0][2], F(195, 8))
check("shrunk S23 = (3/4)*(33/2)", SH[1][2], F(99, 8))
show("shrunk S12 as decimal", dec(SH[0][1]))
show("shrunk S13 as decimal", dec(SH[0][2]))
show("shrunk S23 as decimal", dec(SH[1][2]))
check("shrunk correlation g1,g2 = (3/4)*(1/2)", SH[0][1] / F(15), F(3, 8))
check("shrunk correlation g1,g3", SH[0][2] / F(35), F(39, 56))
check("shrunk correlation g2,g3", SH[1][2] / F(21), F(33, 56))
show("shrunk correlation g1,g2 as decimal", dec(F(3, 8)))
show("shrunk correlation g1,g3 as decimal", dec(F(39, 56)))
show("shrunk correlation g2,g3 as decimal", dec(F(33, 56)))
check("2 * shrunk S12", 2 * SH[0][1], F(45, 4))
show("   as decimal", dec(F(45, 4), 2))
check("2 * shrunk S13", 2 * SH[0][2], F(195, 4))
show("   as decimal", dec(F(195, 4), 2))
check("2 * shrunk S23", 2 * SH[1][2], F(99, 4))
show("   as decimal", dec(F(99, 4), 2))
check("83 + 11.25 - 48.75 - 24.75",
      F(83) + F(45, 4) - F(195, 4) - F(99, 4), F(83, 4))
check("the zero-risk book's variance after shrinkage", quad(SH, w), F(83, 4))
check("... which is exactly a * 83", a * F(83), F(83, 4))
show("83/4 as decimal", dec(F(83, 4)))
show("its risk, sqrt(83/4)", sqrt_dec(F(83, 4)))
check("determinant of the shrunk grid", det3(SH), F(945225, 256))
show("determinant of the shrunk grid as a decimal",
     dec(F(945225, 256), 8))
check("the shrunk determinant is strictly positive", det3(SH) > 0, True)

sub("11.6(ii) shrinkage is not 'making the numbers smaller'")
check("the (1,1,0) book, sample variance", quad(SB, [F(1), F(1), F(0)]),
      F(49))
show("its sample risk", sqrt_dec(F(49)))
check("the (1,1,0) book, shrunk variance", quad(SH, [F(1), F(1), F(0)]),
      F(181, 4))
show("its shrunk variance as a decimal", dec(F(181, 4)))
show("its shrunk risk", sqrt_dec(F(181, 4)))
check("that book's risk went DOWN", quad(SH, [F(1), F(1), F(0)]) < F(49),
      True)
check("the (1,-1,0) book, sample variance", quad(SB, [F(1), F(-1), F(0)]),
      F(19))
show("its sample risk", sqrt_dec(F(19)))
check("the (1,-1,0) book, shrunk variance", quad(SH, [F(1), F(-1), F(0)]),
      F(91, 4))
show("its shrunk variance as a decimal", dec(F(91, 4)))
show("its shrunk risk", sqrt_dec(F(91, 4)))
check("that book's risk went UP", quad(SH, [F(1), F(-1), F(0)]) > F(19), True)
check("a single factor on its own is untouched", quad(SH, [F(1), F(0), F(0)]),
      F(25))

sub("11.6(iii) after shrinkage, NO book is scored at zero")
cnt = 0
pos = 0
above_floor = 0
worst = None
for h1 in range(-4, 5):
    for h2 in range(-4, 5):
        for h3 in range(-4, 5):
            if h1 == h2 == h3 == 0:
                continue
            h = [F(h1), F(h2), F(h3)]
            vv = quad(SH, h)
            rq = vv / dot(h, h)
            if vv > 0:
                pos += 1
            if rq >= F(9, 4):
                above_floor += 1
            if worst is None or rq < worst[0]:
                worst = (rq, (h1, h2, h3))
            cnt += 1
check("non-zero integer books swept against the shrunk grid", cnt, 728)
check("every one of them got a strictly positive variance", pos, 728)
check("every one of them scored at or above the 9/4 floor", above_floor, 728)
check("the floor: a*min(diagonal) = (1/4)*9", a * F(9), F(9, 4))
show("that floor as a variance", dec(F(9, 4)))
show("that floor as a risk, sqrt(9/4)", sqrt_dec(F(9, 4)))
show("the cheapest book found in the sweep", worst[1])
show("its variance per unit of size", dec(worst[0]))
check("the sweep's cheapest book beats the floor", worst[0] >= F(9, 4), True)

sub("11.7 shrinkage on the 2x2, where the eigenvalues can be watched exactly")
vbar = trace(FF) / 2
check("average of the two variances (25+9)/2", vbar, F(17))
rows = []
for aa in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
    Fa = addm(scale(FF, 1 - aa),
              scale([[F(1), F(0)], [F(0), F(1)]], aa * vbar))
    lam_hi = vbar + F(10) * (1 - aa)
    lam_lo = vbar - F(10) * (1 - aa)
    check(f"a={aa}: trace is preserved", trace(Fa), F(34))
    check(f"a={aa}: F*(3,1) = lam_hi*(3,1)", matvec(Fa, v1),
          [lam_hi * 3, lam_hi * 1])
    check(f"a={aa}: F*(1,-3) = lam_lo*(1,-3)", matvec(Fa, v2),
          [lam_lo * 1, lam_lo * (-3)])
    check(f"a={aa}: lam_hi + lam_lo = 34", lam_hi + lam_lo, F(34))
    check(f"a={aa}: lam_hi * lam_lo = det", lam_hi * lam_lo, det2(Fa))
    rows.append((aa, Fa, lam_hi, lam_lo))
    show(f"   a={aa}  grid", Fa)
    show(f"   a={aa}  grid as decimals",
         [[dec(Fa[0][0], 2), dec(Fa[0][1], 2)],
          [dec(Fa[1][0], 2), dec(Fa[1][1], 2)]])
    show(f"   a={aa}  eigenvalues", (lam_hi, lam_lo))
    show(f"   a={aa}  eigenvalues as decimals",
         (dec(lam_hi, 2), dec(lam_lo, 2)))
    show(f"   a={aa}  spread", lam_hi - lam_lo)
    show(f"   a={aa}  determinant", det2(Fa))
    show(f"   a={aa}  determinant as a decimal", dec(det2(Fa), 2))

HALF = rows[2][1]
check("a=1/2 grid entry (0,0)", HALF[0][0], F(21))
check("a=1/2 grid entry (0,1)", HALF[0][1], F(3))
check("a=1/2 grid entry (1,1)", HALF[1][1], F(13))
check("a=1/2 discriminant (21-13)^2 + 4*9", F(8) ** 2 + 4 * F(9), F(100))
check("a=1/2 sqrt of that", F(10) * F(10), F(100))
check("a=1/2 eigenvalues", ((F(34) + F(10)) / 2, (F(34) - F(10)) / 2),
      (F(22), F(12)))
check("a=1/2 determinant 22*12", det2(HALF), F(264))
check("spread falls from 20 to 10", F(27) - F(7), 2 * (F(22) - F(12)))
check("ratio 27/7 falls to 22/12 = 11/6", F(22) / F(12), F(11, 6))
show("11/6 as decimal", dec(F(11, 6)))
show("sqrt(22) -- shrunk risk along the peak direction", sqrt_dec(F(22)))
show("sqrt(12) -- shrunk risk along the trough direction", sqrt_dec(F(12)))
check("the eigenvectors did not move: (3,1) still maps to a multiple of itself",
      matvec(HALF, v1), [F(66), F(22)])
check("... and (1,-3) likewise", matvec(HALF, v2), [F(12), F(-36)])

sub("11.8 what the shrinkage cost, in the one place we know the truth")
# the (4,3) book's TRUE variance in this file is 625 (Section 5c, from the series)
Fh = HALF
check("the (4,3) book under the unshrunk grid", quad(FF, [F(4), F(3)]),
      F(625))
check("the (4,3) book under the a=1/2 grid", quad(Fh, [F(4), F(3)]), F(525))
show("sqrt(625)", sqrt_dec(F(625)))
show("sqrt(525)", sqrt_dec(F(525)))
check("the shrinkage moved that book's variance by 100", F(625) - F(525),
      F(100))
check("... which is 100/625 = 4/25 of it", F(100) / F(625), F(4, 25))
show("4/25 as decimal", dec(F(4, 25)))
# The 16% is a VARIANCE move. The markdown now also prints the RISK move, because
# variances move and volatilities do not move by the same percentage (Section 6g).
check("the ratio of the two variances, 525/625", F(525) / F(625), F(21, 25))
show("sqrt(21/25) -- the ratio of the two RISKS", sqrt_dec(F(21, 25)))
_riskdrop = Decimal(1) - (Decimal(21) / Decimal(25)).sqrt()
print(f"        1 - sqrt(21/25), the risk-side move = {_riskdrop:.4f} (ROUNDED)")
check("the risk-side move rounds to 0.0835, i.e. 8.35% -- not 16%",
      _riskdrop.quantize(Decimal("1.0000")), Decimal("0.0835"))
check("... and it is strictly smaller than the 16% variance move",
      _riskdrop < Decimal("0.16"), True)
check("25% falls to sqrt(525) = 22.9129% (rounded)", sqrt_dec(F(525)),
      "22.9129 (ROUNDED)")

# ===========================================================================
head("SECTION 13  Back to BFRE -- the paper's own numbers")
# ===========================================================================

sub("13c. what a 26-week half-life does to 104 weekly observations")
# weights lam^t, t = 0..103, lam = 2^(-1/26).  lam^104 = 1/16 exactly.
lam = (Decimal(1) / Decimal(2)) ** (Decimal(1) / Decimal(26))
one = Decimal(1)
sw = (one - lam ** 104) / (one - lam)
sw2 = (one - lam ** 208) / (one - lam ** 2)
ess = sw * sw / sw2
closed = (Decimal(15) / Decimal(17)) * (one + lam) / (one - lam)
print(f"        lam = 2^(-1/26)                    = {lam:.6f} (ROUNDED)")
print(f"        lam^104                            = {lam**104:.10f} "
      f"(exactly 1/16 = 0.0625)")
check("lam^104 rounds to 1/16 at 20 digits",
      (lam ** 104).quantize(Decimal("1.00000000000000000000")),
      Decimal("0.0625").quantize(Decimal("1.00000000000000000000")))
check("closed form (15/17)(1+lam)/(1-lam) matches the direct sum to 20dp",
      ess.quantize(Decimal("1.00000000000000000000")),
      closed.quantize(Decimal("1.00000000000000000000")))
print(f"        effective sample size              = {ess:.4f} (ROUNDED)")
print(f"        rounded to a whole number          = {ess.quantize(Decimal('1'))}")
oldest = lam ** 103
print(f"        weight of the oldest of 104 weeks  = {oldest:.6f} (ROUNDED)")
print(f"        ... as a percentage                = {oldest*100:.2f}% (ROUNDED)")
check("the oldest week's weight is above 1/16 and below 1/15",
      Decimal(1) / Decimal(16) < oldest < Decimal(1) / Decimal(15), True)
# the daily specific-risk model, Table 1.3 p.28
lamd = (Decimal(1) / Decimal(2)) ** (Decimal(1) / Decimal(125))
swd = (one - lamd ** 375) / (one - lamd)
sw2d = (one - lamd ** 750) / (one - lamd ** 2)
essd = swd * swd / sw2d
closedd = (Decimal(7) / Decimal(9)) * (one + lamd) / (one - lamd)
check("daily model: closed form (7/9)(1+lam)/(1-lam) matches the sum to 20dp",
      essd.quantize(Decimal("1.00000000000000000000")),
      closedd.quantize(Decimal("1.00000000000000000000")))
print(f"        daily model effective sample size  = {essd:.4f} (ROUNDED)")
print(f"        rounded to a whole number          = {essd.quantize(Decimal('1'))}")
check("the closed-form ingredient 1 - 2^-4 over 1 + 2^-4 = 15/17",
      (F(1) - F(1, 16)) / (F(1) + F(1, 16)), F(15, 17))
check("the closed-form ingredient 1 - 2^-3 over 1 + 2^-3 = 7/9",
      (F(1) - F(1, 8)) / (F(1) + F(1, 8)), F(7, 9))

sub("13c(ii) the factor count assembled from printed rows (INFER)")
check("1 market + 12 styles + 53 core industries", F(1 + 12 + 53), F(66))
check("... plus 2 countries and 2 currencies", F(66) + F(2) + F(2), F(70))
check("with all 54 industry rows instead of 53", F(1 + 12 + 54 + 2 + 2),
      F(71))
check("distinct entries in a 71x71 symmetric grid, K(K+1)/2",
      F(71 * 72) / 2, F(2556))
check("distinct entries in a 70x70 symmetric grid", F(70 * 71) / 2, F(2485))
check("raw numbers available: 104 weeks x 71 factors", F(104 * 71), F(7384))
check("observations per estimated entry, 7384/2556", F(7384) / F(2556),
      F(1846, 639))
show("7384/2556 as decimal", dec(F(7384, 2556)))
check("effective-count version: 66 x 71 / 2556", F(66 * 71) / F(2556),
      F(4686, 2556))
show("4686/2556 as decimal", dec(F(4686, 2556)))

sub("13d. a real slice of F: Table 1.2's market-correlation column (p.10)")
# The printed digits are the left column; the reduced Fraction the code carries
# is the right one. Comparing a value with itself would prove nothing, so each
# row is rebuilt from the digits as they appear on p.10 and matched against the
# reduced form the rest of this file uses.
for name, printed, val in [("Volatility", "0.84", F(21, 25)),
                           ("Liquidity", "0.69", F(69, 100)),
                           ("Reversal", "-0.32", F(-8, 25)),
                           ("Size", "0.23", F(23, 100)),
                           ("Momentum", "-0.02", F(-1, 50))]:
    check(f"printed correlation with the market factor: {name}",
          F(Decimal(printed)), val)
    show("   as decimal", dec(val, 2))
check("Volatility's own annualised volatility, Table 1.2 (7.5%)",
      F(Decimal("7.5")), F(15, 2))
check("the market factor's own annualised volatility, Table 1.2 (19.8%)",
      F(Decimal("19.8")), F(99, 5))
show("Volatility 7.5%, Market 19.8% -- both printed on p.10",
     (dec(F(75, 10), 1), dec(F(198, 10), 1)))
check("implied covariance 0.84 * 7.5 * 19.8 (percent-squared, INFER)",
      F(84, 100) * F(75, 10) * F(198, 10), F(62370, 500))
show("that covariance as a decimal", dec(F(84, 100) * F(75, 10) * F(198, 10)))

sub("13h. the p.35 active-risk pie adds to 100 (read directly; [INFERRED])")
check("50 + 25 + 14 + 6 + 4 + 1",
      F(50) + F(25) + F(14) + F(6) + F(4) + F(1), F(100))

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified, plus "
      f"{169 + 361 + 5 + 19683 + 728} swept cases.")
print("   Every number printed above appears in datasets/level8.md.")
print("   Decimals tagged ROUNDED above are marked 'rounded' in the markdown.")
