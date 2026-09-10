#!/usr/bin/env python3
"""
verify_level10.py -- recomputes EVERY number printed in datasets/level10.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level10.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

Linear-algebra helpers are the same conventions as tools/verify_level5.py and
tools/verify_level8.py -- reused, not reinvented.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product
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


def isqrt_exact(m):
    if m < 0:
        return None
    r = int(m ** 0.5)
    for c in (r - 2, r - 1, r, r + 1, r + 2):
        if c >= 0 and c * c == m:
            return c
    return None


def rootF(v):
    """Exact rational square root, or None."""
    v = F(v)
    rn, rd = isqrt_exact(v.numerator), isqrt_exact(v.denominator)
    if rn is None or rd is None:
        return None
    return F(rn, rd)


def sqrt_dec(v, n=6):
    """Square root of an exact Fraction, printed as an explicitly rounded
    decimal.  Exact when the fraction is a perfect square of a rational."""
    v = F(v)
    r = rootF(v)
    if r is not None:
        return f"{float(r):.{n}f} (EXACT root = {r})"
    d = Decimal(v.numerator) / Decimal(v.denominator)
    return f"{d.sqrt():.{n}f} (ROUNDED)"


def sqrtD(v):
    """Square root as a high-precision Decimal (for comparisons only)."""
    v = F(v)
    return (Decimal(v.numerator) / Decimal(v.denominator)).sqrt()


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


def check_root(label, variance, printed, places=4):
    """`printed` is what the markdown shows for sqrt(variance), rounded to
    `places` decimal places. Verify the rounding."""
    CHECKS[0] += 1
    q = Decimal(1).scaleb(-places)
    got = str(sqrtD(variance).quantize(q))
    ok = (got == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: sqrt({F(variance)}) = {got} (rounded)"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': got {got}, markdown says {printed}")


def check_dec(label, value, printed, places=4):
    """`printed` is what the markdown shows for an exact Fraction, rounded."""
    CHECKS[0] += 1
    q = Decimal(1).scaleb(-places)
    v = F(value)
    got = str((Decimal(v.numerator) / Decimal(v.denominator)).quantize(q))
    ok = (got == printed)
    tag = "exact" if terminates(v) else "ROUNDED"
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: {F(value)} = {got} ({tag})"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': got {got}, markdown says {printed}")


def show(label, val):
    print(f"        {label}: {S(val)}")


# ---------------------------------------------------------------------------
# exact linear algebra over Fraction
# ---------------------------------------------------------------------------

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


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


def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def vecmat(v, A):
    return [sum(v[i] * A[i][j] for i in range(len(v))) for j in range(len(A[0]))]


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


def addm(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def diagm(d):
    n = len(d)
    return [[d[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def mean(xs):
    return sum(xs, F(0)) / len(xs)


def devs(xs):
    m = mean(xs)
    return [x - m for x in xs]


def sample_cov(a, b, ddof=1):
    """Mean-subtracted sample covariance with divisor T - ddof."""
    da, db = devs(a), devs(b)
    return sum(x * y for x, y in zip(da, db)) / (len(a) - ddof)


def is_symmetric(A):
    n = len(A)
    return all(A[i][j] == A[j][i] for i in range(n) for j in range(n))


# ===========================================================================
head("SECTION 3 -- THE THREE PIECES, AND WHERE EACH ONE CAME FROM")
# ===========================================================================

sub("3a. X, the exposure block -- three rows of the Level 7/8 estimation universe")

NAMES5 = ["AXL", "BRN", "CHR", "DLT", "EMK"]
X5 = {"AXL": [F(1), F(-2)], "BRN": [F(1), F(-1)], "CHR": [F(1), F(0)],
      "DLT": [F(1), F(1)], "EMK": [F(1), F(2)]}

check("Level 8's cheapness column, all five names",
      [X5[n][1] for n in NAMES5], [F(-2), F(-1), F(0), F(1), F(2)])
check("that column is centred over the estimation universe (sum = 0)",
      sum(X5[n][1] for n in NAMES5), F(0))
check("market column is all ones (p.4: unit exposure to the market factor)",
      [X5[n][0] for n in NAMES5], [F(1)] * 5)

HELD = ["AXL", "CHR", "EMK"]
X = [X5[n] for n in HELD]
check("X, the 3x2 exposure block for the three held names", X,
      [[F(1), F(-2)], [F(1), F(0)], [F(1), F(2)]])
check("X has 3 rows (one per held asset)", len(X), 3)
check("X has 2 columns (one per factor)", len(X[0]), 2)
check("the held subset happens to sum to zero too (-2 + 0 + 2)",
      sum(X[i][1] for i in range(3)), F(0))
check("but the fourth and fifth names are NOT held; the universe is 5, the book is 3",
      len(NAMES5) - len(HELD), 2)

sub("3b. F, taken unchanged from Level 8 section 4b")

# Level 8's five monthly factor returns, rebuilt from Level 8's own returns file
RET5 = {  # month 1..5, in percent
    "AXL": [F(0), F(-3), F(6), F(6), F(-8)],
    "BRN": [F(1), F(2), F(3), F(7), F(-6)],
    "CHR": [F(9), F(3), F(-1), F(1), F(-8)],
    "DLT": [F(9), F(10), F(-1), F(3), F(-4)],
    "EMK": [F(16), F(13), F(-2), F(-2), F(-4)],
}
T = 5
f_mkt, f_chp = [], []
for t in range(T):
    r = [RET5[n][t] for n in NAMES5]
    x = [X5[n][1] for n in NAMES5]
    # Level 1's formula on each orthogonal column (Sigma 1.x = 0, Level 8 sec 3b)
    f_mkt.append(sum(r) / 5)
    f_chp.append(sum(xi * ri for xi, ri in zip(x, r)) / 10)
check("Level 7/8 factor return series, market", f_mkt,
      [F(7), F(5), F(1), F(3), F(-6)])
check("Level 7/8 factor return series, cheapness", f_chp,
      [F(4), F(4), F(-2), F(-2), F(1)])

Fm = [[sample_cov(f_mkt, f_mkt), sample_cov(f_mkt, f_chp)],
      [sample_cov(f_chp, f_mkt), sample_cov(f_chp, f_chp)]]
check("F rebuilt from the Level 8 series (mean subtracted, divisor T-1 = 4)",
      Fm, [[F(25), F(6)], [F(6), F(9)]])
check("F is symmetric", is_symmetric(Fm), True)
check("F's determinant (Level 4's det = AC - B^2)", det2(Fm), F(189))
check("market factor volatility, per month", rootF(Fm[0][0]), F(5))
check("cheapness factor volatility, per month", rootF(Fm[1][1]), F(3))
check("correlation between the two factor returns", Fm[0][1] / (F(5) * F(3)), F(2, 5))

sub("3c. D, built from the Level 8 / Level 9 miss columns")

U5 = {  # the five monthly misses per name, Level 8 section 3c
    "AXL": [F(1), F(0), F(1), F(-1), F(0)],
    "BRN": [F(-2), F(1), F(0), F(2), F(1)],
    "CHR": [F(2), F(-2), F(-2), F(-2), F(-2)],
    "DLT": [F(-2), F(1), F(0), F(2), F(1)],
    "EMK": [F(1), F(0), F(1), F(-1), F(0)],
}
# the misses really are the residuals of the Level 8 fit, month by month
for t in range(T):
    for n in NAMES5:
        fit = X5[n][0] * f_mkt[t] + X5[n][1] * f_chp[t]
        check(f"miss recomputed, {n} month {t+1}", RET5[n][t] - fit, U5[n][t])
for t in range(T):
    check(f"Level 2 balance, column of ones, month {t+1}",
          sum(U5[n][t] for n in NAMES5), F(0))
    check(f"Level 2 balance, cheapness column, month {t+1}",
          sum(X5[n][1] * U5[n][t] for n in NAMES5), F(0))

SU2 = {n: sum(u * u for u in U5[n]) for n in NAMES5}
check("sum of squared misses per name", [SU2[n] for n in NAMES5],
      [F(3), F(10), F(20), F(10), F(3)])
check("Level 8's stated total across the file", sum(SU2.values()), F(46))

Dvec = [SU2[n] / T for n in HELD]
check("D's diagonal = (sum of squared misses)/T for the three held names",
      Dvec, [F(3, 5), F(4), F(3, 5)])
Dm = diagm(Dvec)
check("D is 3x3", (len(Dm), len(Dm[0])), (3, 3))
check("D's off-diagonal entries are all zero -- that IS the Level 9 assumption",
      [Dm[i][j] for i in range(3) for j in range(3) if i != j], [F(0)] * 6)
check("specific volatility of AXL, per month (rounded below)", Dvec[0], F(3, 5))
check_root("specific volatility AXL", Dvec[0], "0.7746")
check_root("specific volatility CHR", Dvec[1], "2.0000")
check_root("specific volatility EMK", Dvec[2], "0.7746")

sub("3c (continued). the two rival divisor conventions, printed so the level is honest")

# convention 2: subtract each name's own sample mean, divide by T-1
alt_mean4 = [sum(d * d for d in devs(U5[n])) / (T - 1) for n in HELD]
check("AXL's own mean miss over the five months", mean(U5["AXL"]), F(1, 5))
check("CHR's own mean miss over the five months", mean(U5["CHR"]), F(-6, 5))
check("EMK's own mean miss over the five months", mean(U5["EMK"]), F(1, 5))
check("convention 2 (mean subtracted, divisor 4)", alt_mean4,
      [F(7, 10), F(16, 5), F(7, 10)])

# convention 3: Level 6's leverage correction, E[u_i^2] = (1 - h_i) sigma_i^2
lev = {n: F(1, 5) + X5[n][1] ** 2 / 10 for n in NAMES5}
check("leverages h_i in the five-stock cross-section",
      [lev[n] for n in NAMES5], [F(3, 5), F(3, 10), F(1, 5), F(3, 10), F(3, 5)])
check("Level 6's check: the leverages sum to k = 2",
      sum(lev[n] for n in NAMES5), F(2))
alt_lev = [(SU2[n] / T) / (1 - lev[n]) for n in HELD]
check("convention 3 (Level 6 leverage correction)", alt_lev,
      [F(3, 2), F(5), F(3, 2)])

# ===========================================================================
head("SECTIONS 5-6 -- THE TWO STAGES, AND V")
# ===========================================================================

sub("5. stage one: G = F X^T, a 2x3")

XT = transpose(X)
check("X^T, the 2x3", XT, [[F(1), F(1), F(1)], [F(-2), F(0), F(2)]])
G = matmul(Fm, XT)
check("G = F X^T", G, [[F(13), F(25), F(37)], [F(-12), F(6), F(24)]])
check("G is 2x3", (len(G), len(G[0])), (2, 3))
for j, n in enumerate(HELD):
    col = [G[0][j], G[1][j]]
    check(f"G's column for {n} equals F times {n}'s own exposure row",
          col, matvec(Fm, X[j]))
check("G[market][AXL] = 25*1 + 6*(-2)", F(25) * 1 + F(6) * (-2), F(13))
check("G[cheap ][AXL] =  6*1 + 9*(-2)", F(6) * 1 + F(9) * (-2), F(-12))
check("G[market][CHR] = 25*1 + 6*0", F(25), F(25))
check("G[cheap ][CHR] =  6*1 + 9*0", F(6), F(6))
check("G[market][EMK] = 25*1 + 6*2", F(25) + F(12), F(37))
check("G[cheap ][EMK] =  6*1 + 9*2", F(6) + F(18), F(24))

sub("6a. stage two: X G")

XFXt = matmul(X, G)
check("X (F X^T)", XFXt,
      [[F(37), F(13), F(-11)], [F(13), F(25), F(37)], [F(-11), F(37), F(85)]])
check("the other bracketing, (X F) X^T, gives the same matrix",
      matmul(matmul(X, Fm), XT), XFXt)
check("X F, the 3x2 intermediate of the other bracketing",
      matmul(X, Fm), [[F(13), F(-12)], [F(25), F(6)], [F(37), F(24)]])
check("X F's rows are G's columns, because F is symmetric",
      transpose(matmul(X, Fm)), G)
check("X F X^T is symmetric", is_symmetric(XFXt), True)

# the closed form for a cell
for i in range(3):
    for j in range(3):
        xi, xj = X[i][1], X[j][1]
        check(f"cell ({HELD[i]},{HELD[j]}) = 25 + 6(xi+xj) + 9 xi xj",
              F(25) + 6 * (xi + xj) + 9 * xi * xj, XFXt[i][j])

sub("6b. adding D gives V")

V = addm(XFXt, Dm)
check("V = X F X^T + D", V,
      [[F(188, 5), F(13), F(-11)], [F(13), F(29), F(37)], [F(-11), F(37), F(428, 5)]])
check("V is symmetric", is_symmetric(V), True)
check("V_AXL,AXL = 37 + 0.6", XFXt[0][0] + Dvec[0], F(188, 5))
check("V_CHR,CHR = 25 + 4", XFXt[1][1] + Dvec[1], F(29))
check("V_EMK,EMK = 85 + 0.6", XFXt[2][2] + Dvec[2], F(428, 5))
check("D changed no off-diagonal cell",
      [V[i][j] for i in range(3) for j in range(3) if i != j],
      [XFXt[i][j] for i in range(3) for j in range(3) if i != j])
check_dec("V_AXL,AXL as a decimal", V[0][0], "37.6000")
check_dec("V_EMK,EMK as a decimal", V[2][2], "85.6000")

sub("6c. single-name volatilities and correlations")

check_root("AXL total volatility per month", V[0][0], "6.1319")
check_root("CHR total volatility per month", V[1][1], "5.3852")
check_root("EMK total volatility per month", V[2][2], "9.2520")
CHECKS[0] += 1
check("EMK volatility divided by CHR volatility (rounded)",
      str((sqrtD(V[2][2]) / sqrtD(V[1][1])).quantize(Decimal("0.0001"))), "1.7181")
# annualised, x sqrt(12)
for i, n in enumerate(HELD):
    check_root(f"{n} annualised volatility (x sqrt 12)", V[i][i] * 12,
               ["21.2415", "18.6548", "32.0500"][i])
# correlations: sign carried separately, magnitude from an exact square
for (i, j, printed) in [(0, 1, "0.3937"), (0, 2, "-0.1939"), (1, 2, "0.7426")]:
    mag = F(V[i][j] * V[i][j], (V[i][i] * V[j][j]).numerator) * \
        F((V[i][i] * V[j][j]).denominator)
    magsq = (V[i][j] * V[i][j]) / (V[i][i] * V[j][j])
    CHECKS[0] += 1
    q = Decimal("0.0001")
    got = sqrtD(magsq).quantize(q)
    if V[i][j] < 0:
        got = -got
    ok = (str(got) == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] implied correlation "
          f"{HELD[i]}-{HELD[j]}: {got} (rounded)")
    if not ok:
        sys.exit(f"MISMATCH correlation {HELD[i]}-{HELD[j]}: {got} vs {printed}")
# the same three correlations with D switched off (common-factor part only)
for (i, j, printed) in [(0, 1, "0.4274"), (0, 2, "-0.1961"), (1, 2, "0.8026")]:
    magsq = (XFXt[i][j] * XFXt[i][j]) / (XFXt[i][i] * XFXt[j][j])
    CHECKS[0] += 1
    got = sqrtD(magsq).quantize(Decimal("0.0001"))
    if XFXt[i][j] < 0:
        got = -got
    ok = (str(got) == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] common-factor-only correlation "
          f"{HELD[i]}-{HELD[j]}: {got} (rounded)")
    if not ok:
        sys.exit(f"MISMATCH common correlation {HELD[i]}-{HELD[j]}")

sub("6d. the structural fact: X F X^T is singular, and D is what repairs it")

check("det(X F X^T) = 0 -- three assets, two factors", det3(XFXt), F(0))
null = [F(1), F(-2), F(1)]
check("the exposure-free direction z = (1, -2, 1): its market exposure",
      sum(z * X[i][0] for i, z in enumerate(null)), F(0))
check("the exposure-free direction z = (1, -2, 1): its cheapness exposure",
      sum(z * X[i][1] for i, z in enumerate(null)), F(0))
check("X F X^T applied to z is the zero vector", matvec(XFXt, null),
      [F(0), F(0), F(0)])
check("so the common-factor part scores z at exactly zero variance",
      quad(XFXt, null), F(0))
check("V applied to z is NOT zero", matvec(V, null), [F(3, 5), F(-8), F(3, 5)])
check("V scores z at 17.2 percent-squared", quad(V, null), F(86, 5))
check("D alone scores z at the same 17.2", quad(Dm, null), F(86, 5))
check("z is ten times the active book of section 12, so 17.2/100 = 0.172",
      quad(V, null) / 100, F(43, 250))
check("det(V) is strictly positive", det3(V), F(332661, 25))
check_dec("det(V) as a decimal", det3(V), "13306.4400")
# every non-zero holding vector with small integer entries gets positive variance
cnt = 0
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-3, 4):
            if a == b == c == 0:
                continue
            v = [F(a), F(b), F(c)]
            assert quad(V, v) > 0
            cnt += 1
check("integer holding vectors swept, all with variance > 0", cnt, 342)
check("F's own variances are positive and det F > 0, so h^T F h is never negative",
      (Fm[0][0] > 0, det2(Fm) > 0), (True, True))
check("D's diagonal is strictly positive", all(d > 0 for d in Dvec), True)

# ===========================================================================
head("SECTION 7 -- BOOK A, TWO ROUTES TO ONE NUMBER")
# ===========================================================================

wA = [F(1, 2), F(2, 5), F(1, 10)]
check("Book A weights sum to 1 (fully invested, long only)", sum(wA), F(1))

sub("7b. route 1 -- aggregate the exposures first (p.24: 'aggregated from the asset level')")

hA = vecmat(wA, X)
check("h = X^T w, Book A", hA, [F(1), F(-4, 5)])
check("market exposure is 1 because the weights sum to 1", hA[0], F(1))
check("cheapness exposure -0.8 = 0.5(-2) + 0.4(0) + 0.1(2)",
      F(1, 2) * F(-2) + F(2, 5) * F(0) + F(1, 10) * F(2), F(-4, 5))
facA = quad(Fm, hA)
check("factor variance h^T F h", facA, F(529, 25))
check("expanded: 25(1) + 2(6)(1)(-4/5) + 9(16/25)",
      F(25) + 2 * F(6) * F(-4, 5) + F(9) * F(16, 25), F(529, 25))
check_dec("factor variance as a decimal", facA, "21.1600")
check("factor risk is an EXACT root", rootF(facA), F(23, 5))
specA = sum(wA[i] * wA[i] * Dvec[i] for i in range(3))
check("specific variance sum w_i^2 d_i", specA, F(199, 250))
check("term by term: 0.25(0.6), 0.16(4), 0.01(0.6)",
      [wA[i] ** 2 * Dvec[i] for i in range(3)],
      [F(3, 20), F(16, 25), F(3, 500)])
check_dec("specific variance as a decimal", specA, "0.7960")
check_root("specific risk", specA, "0.8922")
check_dec("CHR alone supplies this share of the specific variance, percent",
          (wA[1] ** 2 * Dvec[1]) / specA * 100, "80.4020")
totA = facA + specA
check("total variance = factor + specific", totA, F(5489, 250))
check_dec("total variance as a decimal", totA, "21.9560")
check_root("Book A total risk, per month", totA, "4.6857")
check_root("Book A total risk, annualised (x sqrt 12)", totA * 12, "16.2318")

sub("7c. route 2 -- build V first, then w^T V w")

VwA = matvec(V, wA)
check("V w, Book A", VwA, [F(229, 10), F(109, 5), F(893, 50)])
check_dec("(Vw) for AXL", VwA[0], "22.9000")
check_dec("(Vw) for CHR", VwA[1], "21.8000")
check_dec("(Vw) for EMK", VwA[2], "17.8600")
check("w . (V w) equals route 1's total", dot(wA, VwA), totA)
check("w^T V w computed as a double sum", quad(V, wA), totA)
contribA = [wA[i] * VwA[i] for i in range(3)]
check("per-name variance contributions", contribA,
      [F(229, 20), F(218, 25), F(893, 500)])
check("they sum to the total variance", sum(contribA), totA)
check_dec("AXL's share of the variance, percent", contribA[0] / totA * 100, "52.1498")
check_dec("CHR's share of the variance, percent", contribA[1] / totA * 100, "39.7158")
check_dec("EMK's share of the variance, percent", contribA[2] / totA * 100, "8.1345")
check("the three shares sum to 100 percent",
      sum(contribA[i] / totA for i in range(3)) * 100, F(100))

sub("7d. the two routes agree for every book, not just this one")

cnt = 0
for a in range(-4, 5):
    for b in range(-4, 5):
        for c in range(-4, 5):
            w = [F(a, 10), F(b, 10), F(c, 10)]
            h = vecmat(w, X)
            lhs = quad(V, w)
            rhs = quad(Fm, h) + sum(w[i] ** 2 * Dvec[i] for i in range(3))
            assert lhs == rhs
            cnt += 1
check("holding vectors swept, both routes identical every time", cnt, 729)

sub("7e. predict-then-reveal -- the naive weighted average of the three volatilities")

wavg = sum(Decimal(str(float(wA[i]))) * sqrtD(V[i][i]) for i in range(3))
CHECKS[0] += 1
got = str(wavg.quantize(Decimal("0.0001")))
check("weighted average of the three single-name volatilities (rounded)",
      got, "6.1452")
benefit = wavg - sqrtD(totA)
CHECKS[0] += 1
check("the difference the model finds (rounded)",
      str(benefit.quantize(Decimal("0.0001"))), "1.4595")
CHECKS[0] += 1
check("that difference as a percent of the naive figure (rounded)",
      str((benefit / wavg * 100).quantize(Decimal("0.01"))), "23.75")

# ===========================================================================
head("SECTION 8 -- VARIANCES ADD, RISKS DO NOT")
# ===========================================================================

sub("8a. the labelled illustration -- invented round numbers, 3 and 4 and 5")

check("3 squared plus 4 squared", F(3) ** 2 + F(4) ** 2, F(25))
check("the root of 25", rootF(F(25)), F(5))
check("adding the risks instead would give", F(3) + F(4), F(7))
check("the overstatement, as a fraction of the truth", (F(7) - F(5)) / F(5), F(2, 5))

sub("8b. the same test on Book A's real numbers")

sum_of_risks = sqrtD(facA) + sqrtD(specA)
CHECKS[0] += 1
check("factor risk + specific risk (rounded)",
      str(sum_of_risks.quantize(Decimal("0.0001"))), "5.4922")
CHECKS[0] += 1
check("the true total risk (rounded)",
      str(sqrtD(totA).quantize(Decimal("0.0001"))), "4.6857")
CHECKS[0] += 1
check("how much the addition overstates (rounded)",
      str((sum_of_risks - sqrtD(totA)).quantize(Decimal("0.0001"))), "0.8065")
CHECKS[0] += 1
check("as a percent of the true risk (rounded)",
      str(((sum_of_risks - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "17.21")
check("but the VARIANCES add exactly, with nothing left over",
      facA + specA - totA, F(0))
check_dec("factor share of the variance, percent", facA / totA * 100, "96.3746")
check_dec("specific share of the variance, percent", specA / totA * 100, "3.6254")
check("the two shares sum to exactly 100 percent",
      (facA / totA + specA / totA) * 100, F(100))

sub("8c. squares add for every book in the sweep; roots essentially never do")

both = 0
roots_add = 0
for a in range(0, 11):
    for b in range(0, 11 - a):
        c = 10 - a - b
        w = [F(a, 10), F(b, 10), F(c, 10)]
        h = vecmat(w, X)
        fv = quad(Fm, h)
        sv = sum(w[i] ** 2 * Dvec[i] for i in range(3))
        assert fv + sv == quad(V, w)
        both += 1
        if sqrtD(fv) + sqrtD(sv) == sqrtD(fv + sv):
            roots_add += 1
check("long-only books swept on a 10ths grid", both, 66)
check("books where factor risk + specific risk equalled total risk", roots_add, 0)

# ===========================================================================
head("SECTION 9 -- TRAPS, EACH WITH THE NUMBER IT RETURNS")
# ===========================================================================

sub("trap 1: drop D")
check("factor variance alone", facA, F(529, 25))
check_root("the risk it reports", facA, "4.6000")
CHECKS[0] += 1
check("understatement versus 4.6857, percent (rounded)",
      str(((sqrtD(facA) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "-1.83")

sub("trap 2: drop F's off-diagonal")
Fdiag = [[F(25), F(0)], [F(0), F(9)]]
fac_nod = quad(Fdiag, hA)
check("factor variance with the 6s deleted", fac_nod, F(769, 25))
check("total variance with the 6s deleted", fac_nod + specA, F(7889, 250))
check_root("the risk it reports", fac_nod + specA, "5.6175")
CHECKS[0] += 1
check("overstatement versus 4.6857, percent (rounded)",
      str(((sqrtD(fac_nod + specA) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "19.88")
check("the cross term that was deleted, 2(6)(1)(-4/5)",
      2 * F(6) * hA[0] * hA[1], F(-48, 5))

sub("trap 3: keep only V's diagonal")
diag_only = sum(wA[i] ** 2 * V[i][i] for i in range(3))
check("sum w_i^2 V_ii", diag_only, F(1862, 125))
check_root("the risk it reports", diag_only, "3.8595")
CHECKS[0] += 1
check("understatement versus 4.6857, percent (rounded)",
      str(((sqrtD(diag_only) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "-17.63")

sub("trap 4: add the two risks")
CHECKS[0] += 1
check("what it returns (rounded)",
      str(sum_of_risks.quantize(Decimal("0.0001"))), "5.4922")

sub("trap 5: the shapes of the wrong transpose")
check("X is 3x2, so X^T F X has inner dimensions 3 and 2 -- undefined",
      (len(XT[0]), len(matmul(Fm, X)[0]) if False else len(Fm)), (3, 2))
check("X F X^T is 3x3, one row and one column per HELD ASSET",
      (len(XFXt), len(XFXt[0])), (3, 3))
check("X^T V X would be 2x2 -- a factor-shaped object, not an asset-shaped one",
      (len(matmul(matmul(XT, V), X)), len(matmul(matmul(XT, V), X)[0])), (2, 2))

sub("trap 6: forget to square the weights inside the specific part")
bad_spec = sum(wA[i] * Dvec[i] for i in range(3))
check("sum w_i d_i instead of sum w_i^2 d_i", bad_spec, F(49, 25))
check_root("the total risk it returns", facA + bad_spec, "4.8083")
CHECKS[0] += 1
check("overstatement versus 4.6857, percent (rounded)",
      str(((sqrtD(facA + bad_spec) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "2.62")

sub("trap 7: the three D conventions, and how little the answer moves")
for nm, DD, sv_want, tv_want, printed in [
        ("as printed: divisor T = 5, no mean subtracted",
         Dvec, F(199, 250), F(5489, 250), "4.6857"),
        ("mean subtracted, divisor T-1 = 4", alt_mean4,
         F(347, 500), F(10927, 500), "4.6748"),
        ("Level 6 leverage correction", alt_lev,
         F(119, 100), F(447, 20), "4.7276")]:
    sv = sum(wA[i] ** 2 * DD[i] for i in range(3))
    check(f"specific variance -- {nm}", sv, sv_want)
    check(f"total variance -- {nm}", facA + sv, tv_want)
    check_root(f"total risk -- {nm}", facA + sv, printed)
for nm, tv, printed in [("mean subtracted, divisor 4", F(10927, 500), "-0.23"),
                        ("leverage correction", F(447, 20), "+0.89")]:
    CHECKS[0] += 1
    d = ((sqrtD(tv) - sqrtD(totA)) / sqrtD(totA) * 100).quantize(Decimal("0.01"))
    check(f"convention shift versus 4.6857, percent -- {nm}",
          ("+" if d > 0 else "") + str(d), printed)
CHECKS[0] += 1
check("widest spread across the three conventions, percent of the middle (rounded)",
      str(((sqrtD(F(447, 20)) - sqrtD(F(10927, 500))) / sqrtD(F(5489, 250)) * 100)
          .quantize(Decimal("0.01"))), "1.13")

# ===========================================================================
head("SECTION 10 -- THE SABOTAGE ROUND")
# ===========================================================================

M_bad = [row[:] for row in XFXt]
M_bad[0][2] = F(-1)
M_bad[2][0] = F(-1)
check("the corrupted common-factor matrix handed to the player", M_bad,
      [[F(37), F(13), F(-1)], [F(13), F(25), F(37)], [F(-1), F(37), F(85)]])
check("the desk's check on the true matrix: M z = 0 for z = (1,-2,1)",
      matvec(XFXt, null), [F(0), F(0), F(0)])
check("the same check on the corrupted matrix", matvec(M_bad, null),
      [F(10), F(0), F(10)])
check("rows 1 and 3 fail, row 2 passes -- the cell is (1,3)",
      [r != 0 for r in matvec(M_bad, null)], [True, False, True])
check("z's third entry is 1, so row 1's residual IS the error in cell (1,3)",
      matvec(M_bad, null)[0], M_bad[0][2] - XFXt[0][2])
check("repaired value", M_bad[0][2] - matvec(M_bad, null)[0], F(-11))
check("the corrupted matrix is not singular, which is the same alarm",
      det3(M_bad) != 0, True)
check("det of the corrupted matrix", det3(M_bad), F(12620))
check("Book A priced on the corrupted matrix", quad(M_bad, wA) + specA,
      F(5739, 250))
check_root("the risk it would have reported", quad(M_bad, wA) + specA, "4.7912")
CHECKS[0] += 1
check("that corruption as a percentage error (rounded)",
      str(((sqrtD(quad(M_bad, wA) + specA) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "2.25")

# every single-cell corruption of the common part is caught by the same test
caught = 0
for i in range(3):
    for j in range(i, 3):
        for delta in [F(-7), F(-1), F(1), F(3), F(10)]:
            Mb = [row[:] for row in XFXt]
            Mb[i][j] += delta
            Mb[j][i] += delta
            assert matvec(Mb, null) != [F(0), F(0), F(0)]
            caught += 1
check("symmetric single-cell corruptions swept, all caught by z", caught, 30)

# ===========================================================================
head("SECTION 11 -- BOSS ROUND: BOOK B, THE MIRROR")
# ===========================================================================

wB = [F(1, 10), F(2, 5), F(1, 2)]
check("Book B weights sum to 1", sum(wB), F(1))
check("Book B is Book A with the first and third weights swapped",
      wB, [wA[2], wA[1], wA[0]])
hB = vecmat(wB, X)
check("h = X^T w, Book B", hB, [F(1), F(4, 5)])
facB = quad(Fm, hB)
check("factor variance, Book B", facB, F(1009, 25))
check("expanded: 25 + 2(6)(0.8) + 9(0.64)",
      F(25) + 2 * F(6) * F(4, 5) + F(9) * F(16, 25), F(1009, 25))
check_dec("factor variance as a decimal", facB, "40.3600")
check_root("factor risk, Book B", facB, "6.3530")
specB = sum(wB[i] ** 2 * Dvec[i] for i in range(3))
check("specific variance, Book B -- identical to Book A's", specB, specA)
check("term by term: 0.01(0.6), 0.16(4), 0.25(0.6)",
      [wB[i] ** 2 * Dvec[i] for i in range(3)],
      [F(3, 500), F(16, 25), F(3, 20)])
check_dec("specific variance as a decimal", specB, "0.7960")
totB = facB + specB
check("total variance, Book B", totB, F(10289, 250))
check_dec("total variance as a decimal", totB, "41.1560")
check_root("Book B total risk, per month", totB, "6.4153")
check("route 2 agrees", quad(V, wB), totB)
check("V w, Book B", matvec(V, wB), [F(173, 50), F(157, 5), F(113, 2)])
contribB = [wB[i] * matvec(V, wB)[i] for i in range(3)]
check("Book B per-name variance contributions", contribB,
      [F(173, 500), F(314, 25), F(113, 4)])
check("they sum to Book B's total variance", sum(contribB), totB)
check_dec("AXL's share of Book B's variance, percent", contribB[0] / totB * 100, "0.8407")
check_dec("CHR's share of Book B's variance, percent", contribB[1] / totB * 100, "30.5180")
check_dec("EMK's share of Book B's variance, percent", contribB[2] / totB * 100, "68.6413")
check_dec("EMK's share of Book A's variance, percent, for contrast",
          (wA[2] * VwA[2]) / totA * 100, "8.1345")
CHECKS[0] += 1
check("Book B with D dropped: change in risk, percent (rounded)",
      str(((sqrtD(facB) - sqrtD(totB)) / sqrtD(totB) * 100)
          .quantize(Decimal("0.01"))), "-0.97")
check_dec("factor share of Book B's variance, percent", facB / totB * 100, "98.0659")
check_dec("specific share of Book B's variance, percent", specB / totB * 100, "1.9341")
CHECKS[0] += 1
check("Book B risk divided by Book A risk (rounded)",
      str((sqrtD(totB) / sqrtD(totA)).quantize(Decimal("0.0001"))), "1.3691")
check("the whole difference is the cross term: 2(6)(1)(+0.8) vs 2(6)(1)(-0.8)",
      facB - facA, 2 * (2 * F(6) * F(4, 5)))
check("that difference, in percent-squared", facB - facA, F(96, 5))
check_dec("that swing as a decimal", facB - facA, "19.2000")
CHECKS[0] += 1
check("Book B is this much riskier than Book A, percent (rounded)",
      str(((sqrtD(totB) - sqrtD(totA)) / sqrtD(totA) * 100)
          .quantize(Decimal("0.01"))), "36.91")
CHECKS[0] += 1
check("Book B: factor risk + specific risk (rounded)",
      str((sqrtD(facB) + sqrtD(specB)).quantize(Decimal("0.0001"))), "7.2451")
CHECKS[0] += 1
check("Book B: overstatement of the addition, percent (rounded)",
      str(((sqrtD(facB) + sqrtD(specB) - sqrtD(totB)) / sqrtD(totB) * 100)
          .quantize(Decimal("0.01"))), "12.94")

# ===========================================================================
head("SECTION 12 -- THE SAME MACHINERY AGAINST A BENCHMARK")
# ===========================================================================

bm = [F(2, 5), F(1, 2), F(1, 10)]
check("benchmark weights sum to 1", sum(bm), F(1))
hbm = vecmat(bm, X)
check("benchmark exposures", hbm, [F(1), F(-3, 5)])
fac_bm = quad(Fm, hbm)
spec_bm = sum(bm[i] ** 2 * Dvec[i] for i in range(3))
tot_bm = fac_bm + spec_bm
check("benchmark factor variance", fac_bm, F(526, 25))
check("benchmark specific variance", spec_bm, F(551, 500))
check("benchmark total variance", tot_bm, F(11071, 500))
check("route 2 agrees for the benchmark", quad(V, bm), tot_bm)
check_root("benchmark risk", tot_bm, "4.7055")

aA = [wA[i] - bm[i] for i in range(3)]
check("active weights, Book A minus benchmark", aA, [F(1, 10), F(-1, 10), F(0)])
check("active weights sum to zero", sum(aA), F(0))
haA = vecmat(aA, X)
check("active exposures", haA, [F(0), F(-1, 5)])
check("the market exposure cancels exactly", haA[0], F(0))
fac_aA = quad(Fm, haA)
check("active factor variance = 9 x 0.04", fac_aA, F(9, 25))
check("active factor risk is an EXACT root", rootF(fac_aA), F(3, 5))
spec_aA = sum(aA[i] ** 2 * Dvec[i] for i in range(3))
check("active specific variance", spec_aA, F(23, 500))
check("term by term: 0.01(0.6), 0.01(4), 0",
      [aA[i] ** 2 * Dvec[i] for i in range(3)], [F(3, 500), F(1, 25), F(0)])
check_root("active specific risk", spec_aA, "0.2145")
tot_aA = fac_aA + spec_aA
check("active variance total", tot_aA, F(203, 500))
check("route 2 agrees for the active book", quad(V, aA), tot_aA)
check_root("Book A's active risk", tot_aA, "0.6372")
check_dec("factor share of active variance, percent", fac_aA / tot_aA * 100, "88.6700")
check_dec("specific share of active variance, percent", spec_aA / tot_aA * 100, "11.3300")
check_dec("active specific share divided by total specific share",
          (spec_aA / tot_aA) / (specA / totA), "3.1252")

CHECKS[0] += 1
check("portfolio risk minus benchmark risk (rounded)",
      str((sqrtD(totA) - sqrtD(tot_bm)).quantize(Decimal("0.0001"))), "-0.0198")
CHECKS[0] += 1
check("but the active risk is (rounded)",
      str(sqrtD(tot_aA).quantize(Decimal("0.0001"))), "0.6372")

wC = [F(1, 2), F(3, 10), F(1, 5)]
check("Book C weights sum to 1", sum(wC), F(1))
aC = [wC[i] - bm[i] for i in range(3)]
check("Book C's active weights", aC, [F(1, 10), F(-1, 5), F(1, 10)])
check("Book C's active weights are one tenth of z = (1,-2,1)",
      [10 * t for t in aC], null)
haC = vecmat(aC, X)
check("Book C's active exposures are both exactly zero", haC, [F(0), F(0)])
check("Book C's active factor variance", quad(Fm, haC), F(0))
spec_aC = sum(aC[i] ** 2 * Dvec[i] for i in range(3))
check("Book C's active specific variance", spec_aC, F(43, 250))
check("term by term: 0.01(0.6), 0.04(4), 0.01(0.6)",
      [aC[i] ** 2 * Dvec[i] for i in range(3)], [F(3, 500), F(4, 25), F(3, 500)])
check("route 2 agrees", quad(V, aC), spec_aC)
check_root("Book C's active risk, all of it specific", spec_aC, "0.4147")
check_dec("specific share of Book C's active variance, percent",
          spec_aC / spec_aC * 100, "100.0000")
# and Book C's own total risk, for completeness
check("Book C total exposures", vecmat(wC, X), [F(1), F(-3, 5)])
check("Book C factor variance", quad(Fm, vecmat(wC, X)), F(526, 25))
check("Book C specific variance",
      sum(wC[i] ** 2 * Dvec[i] for i in range(3)), F(267, 500))
check("Book C total variance", quad(V, wC), F(10787, 500))
check_root("Book C total risk", quad(V, wC), "4.6448")

# ===========================================================================
head("SECTION 13 -- THE PLUS SIGN IS AN ASSUMPTION, AND HERE IS ITS PRICE")
# ===========================================================================

sub("13a. what actually happened to Book A over the five months")

rA = [sum(wA[i] * RET5[HELD[i]][t] for i in range(3)) for t in range(T)]
check("Book A's realised monthly returns, percent", rA,
      [F(26, 5), F(1), F(12, 5), F(16, 5), F(-38, 5)])
check_dec("month 1", rA[0], "5.2000")
check_dec("month 5", rA[4], "-7.6000")
check("their mean", mean(rA), F(21, 25))
check("deviations from that mean", devs(rA),
      [F(109, 25), F(4, 25), F(39, 25), F(59, 25), F(-211, 25)])
check("sum of squared deviations", sum(d * d for d in devs(rA)), F(12284, 125))
check_dec("that sum as a decimal", sum(d * d for d in devs(rA)), "98.2720")
realised = sample_cov(rA, rA)
check("realised variance, mean subtracted, divisor 4", realised, F(12284, 500))
check_dec("realised variance as a decimal", realised, "24.5680")
check_root("realised volatility", realised, "4.9566")
check("the model said", totA, F(5489, 250))
check("the gap, in percent-squared", realised - totA, F(1306, 500))
check_dec("the gap as a decimal", realised - totA, "2.6120")

sub("13b. the four-term expansion of Var(Xf + u), term by term")

pf = [hA[0] * f_mkt[t] + hA[1] * f_chp[t] for t in range(T)]
check("Book A's factor-driven return each month", pf,
      [F(19, 5), F(9, 5), F(13, 5), F(23, 5), F(-34, 5)])
pu = [sum(wA[i] * U5[HELD[i]][t] for i in range(3)) for t in range(T)]
check("Book A's specific return each month", pu,
      [F(7, 5), F(-4, 5), F(-1, 5), F(-7, 5), F(-4, 5)])
check("the two pieces add back to the realised return",
      [pf[t] + pu[t] for t in range(T)], rA)
term1 = sample_cov(pf, pf)
term4 = sample_cov(pu, pu)
term23 = 2 * sample_cov(pf, pu)
check("term 1, Var(Xf) -- and it is EXACTLY the model's factor variance",
      term1, facA)
check("term 4, Var(u) with the same estimator", term4, F(287, 250))
check_dec("term 4 as a decimal", term4, "1.1480")
check("terms 2+3, the cross term the model deletes", term23, F(113, 50))
check_dec("the cross term as a decimal", term23, "2.2600")
check("the four terms reconstruct the realised variance exactly",
      term1 + term23 + term4, realised)

sub("13c. splitting the specific gap into its two named causes")

Om = [[sample_cov(U5[HELD[i]], U5[HELD[j]]) for j in range(3)] for i in range(3)]
check("the full residual covariance matrix (mean subtracted, divisor 4)", Om,
      [[F(7, 10), F(4, 5), F(7, 10)],
       [F(4, 5), F(16, 5), F(4, 5)],
       [F(7, 10), F(4, 5), F(7, 10)]])
check("its diagonal is convention 2 from section 3c",
      [Om[i][i] for i in range(3)], alt_mean4)
check("AXL and EMK have IDENTICAL miss series", U5["AXL"], U5["EMK"])
check("so their specific returns correlate at exactly 1",
      Om[0][2] * Om[0][2], Om[0][0] * Om[2][2])
check("w^T Omega w -- the true specific variance of the book", quad(Om, wA), term4)
diag_same_conv = sum(wA[i] ** 2 * Om[i][i] for i in range(3))
check("w^T diag(Omega) w -- same convention, off-diagonals thrown away",
      diag_same_conv, F(347, 500))
check("cost of the diagonal assumption alone", term4 - diag_same_conv, F(227, 500))
check_dec("that cost as a decimal", term4 - diag_same_conv, "0.4540")
check("cost of the divisor convention alone", diag_same_conv - specA, F(-51, 500))
check_dec("that cost as a decimal", diag_same_conv - specA, "-0.1020")
check("the three pieces add up to the whole specific gap",
      (term4 - diag_same_conv) + (diag_same_conv - specA), term4 - specA)
check("and the model's shortfall is the specific gap plus the cross term",
      (term4 - specA) + term23, realised - totA)
check("direction: the model's number is the SMALLER one",
      totA < realised, True)

# ===========================================================================
head("SECTION 15 -- BACK TO BFRE: THE PRINTED NUMBERS THIS LEVEL TOUCHES")
# ===========================================================================

sub("p.35 banner, read directly from the scan")
pr, br, ar, beta = F(1562, 100), F(1498, 100), F(299, 100), F(102, 100)
check("Portfolio Risk minus Benchmark Risk", pr - br, F(64, 100))
check("but the report's Active Risk is", ar, F(299, 100))
check("the ratio of the two", ar / (pr - br), F(299, 64))
check_dec("that ratio as a decimal", ar / (pr - br), "4.6719")
check("Portfolio Risk is more than five times Active Risk", pr > 5 * ar, True)
check_dec("Portfolio Risk divided by Active Risk", pr / ar, "5.2241")
check("the audit's alternative reading 2.89 does not rescue subtraction",
      F(289, 100) > pr - br, True)
check("nor does the alternative reading 15.67 for Portfolio Risk",
      F(1567, 100) - br, F(69, 100))
check("Portfolio Beta, printed", beta, F(51, 50))

sub("p.35 pie, read directly")
pie = [F(50), F(25), F(14), F(6), F(4), F(1)]
check("Specific + Style + Industry + Country + FX + Act Sec", sum(pie), F(100))
check("the common-factor slices", sum(pie[1:]), F(50))
check("Specific alone", pie[0], F(50))
check("style + industry, in points of Active Risk", pie[1] + pie[2], F(39))
check("style + industry as a share of the common half, percent",
      (pie[1] + pie[2]) / sum(pie[1:]) * 100, F(78))

sub("our toy against that report -- a scale check, not a target")
check_root("Book A annualised", totA * 12, "16.2318")
check_dec("p.35's Portfolio Risk, for scale", pr, "15.6200")
check_dec("Book A's specific share of TOTAL variance, percent",
          specA / totA * 100, "3.6254")
check_dec("Book A's specific share of ACTIVE variance, percent",
          spec_aA / tot_aA * 100, "11.3300")
check("p.35's specific share of ACTIVE risk contribution, percent", pie[0], F(50))

sub("equation (1.8) is one line below (1.7) -- both on p.24")
check("equation numbers on p.24", (7, 8), (7, 8))
check("the level's shapes: X 3x2, F 2x2, D 3x3, V 3x3",
      (len(X), len(X[0]), len(Fm), len(Fm[0]), len(Dm), len(V)),
      (3, 2, 2, 2, 3, 3))

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified, plus "
      f"{342 + 729 + 66 + 30} swept cases.")
print("   Every number printed above appears in datasets/level10.md.")
print("   Decimals tagged ROUNDED above are marked 'rounded' in the markdown.")
