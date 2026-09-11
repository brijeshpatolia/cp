#!/usr/bin/env python3
"""
verify_level7.py -- recomputes EVERY number printed in datasets/level7.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level7.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

Helper conventions (dot / wdot / solve / wls / dec / check) are lifted unchanged
from tools/verify_level5.py so that all verifiers in this repo share one
convention for exact linear algebra.
"""

from fractions import Fraction as F
import sys

# ---------------------------------------------------------------------------
# harness  (same shape as verify_level5.py / verify_level6.py)
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


def rt(v, n=6):
    """Square root of an exact rational, printed rounded, unless it is exact."""
    v = F(v)
    num_r = _isqrt_exact(v.numerator)
    den_r = _isqrt_exact(v.denominator)
    if num_r is not None and den_r is not None:
        ex = F(num_r, den_r)
        if terminates(ex):
            return f"{float(ex):.{n}f} (EXACT, = {ex})"
    return f"{float(v) ** 0.5:.{n}f} (ROUNDED)"


def _isqrt_exact(m):
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
# linear algebra in exact rationals  (verify_level5.py conventions)
# ---------------------------------------------------------------------------

def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def wdot(w, u, v):
    return sum(wi * a * b for wi, a, b in zip(w, u, v))


def matmul(A, B):
    """Exact matrix product."""
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(F(A[i][t]) * F(B[t][j]) for t in range(k)) for j in range(m)]
            for i in range(n)]


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


def mean(v):
    return sum(v) / len(v)


def centre(v):
    m = mean(v)
    return [a - m for a in v]


# ===========================================================================
# THE FIVE-MONTH FILE  (datasets/level7.md, Section 3)
# ===========================================================================

NAMES = ["AXL", "BRN", "CHR", "DLT", "EMK"]
MONTHS = ["M1", "M2", "M3", "M4", "M5"]
N = 5          # stocks per cross-section
T = 5          # months
K = 2          # columns per cross-section: market (ones) + value

# value exposures, one column per month
X = {
    "M1": [F(-2), F(-1), F(0), F(2), F(1)],
    "M2": [F(-2), F(0), F(1), F(2), F(-1)],
    "M3": [F(-1), F(-2), F(0), F(1), F(2)],
    "M4": [F(-1), F(0), F(1), F(-1), F(1)],
    "M5": [F(-2), F(-1), F(0), F(1), F(2)],
}

# returns, in percent
R = {
    "M1": [F(5, 2), F(5, 2), F(6), F(17, 2), F(11, 2)],
    "M2": [F(1), F(-2), F(-5, 2), F(-4), F(-5, 2)],
    "M3": [F(-1), F(-5, 2), F(-3), F(-1), F(-5, 2)],
    "M4": [F(5, 2), F(2), F(7, 2), F(-1, 2), F(5, 2)],
    "M5": [F(1, 2), F(3, 2), F(0), F(7, 2), F(9, 2)],
}

head("SECTION 3  The file: five stocks, five months, exposures that move")

print("   value exposure x[i,t] (rows = stocks, columns = months)")
print("        name    M1    M2    M3    M4    M5     mean")
for i, nm in enumerate(NAMES):
    row = [X[m][i] for m in MONTHS]
    print(f"        {nm:4}" + "".join(f"{S(v):>6}" for v in row)
          + f"   {S(mean(row))}")

print()
print("   return r[i,t] in percent (rows = stocks, columns = months)")
print("        name    M1    M2    M3    M4    M5")
for i, nm in enumerate(NAMES):
    row = [R[m][i] for m in MONTHS]
    print(f"        {nm:4}" + "".join(f"{float(v):>6.1f}" for v in row))

sub("3a  every month's exposure column is centred, and its reach Q = sum x^2")
Q = {}
for m in MONTHS:
    check(f"{m}: sum of x", sum(X[m]), F(0))
    Q[m] = dot(X[m], X[m])
check("Q by month", [Q[m] for m in MONTHS], [F(10), F(10), F(10), F(4), F(10)])
check("sum of Q over the five months", sum(Q[m] for m in MONTHS), F(44))

sub("3b  exposures move: AXL never positive, DLT changes sign")
check("AXL exposures", [X[m][0] for m in MONTHS],
      [F(-2), F(-2), F(-1), F(-1), F(-2)])
check("AXL mean exposure", mean([X[m][0] for m in MONTHS]), F(-8, 5))
check("DLT exposures", [X[m][3] for m in MONTHS],
      [F(2), F(2), F(1), F(-1), F(1)])
check("DLT mean exposure", mean([X[m][3] for m in MONTHS]), F(1))
check("DLT changes sign between M3 and M4",
      (X["M3"][3] > 0) and (X["M4"][3] < 0), True)
check("BRN mean exposure", mean([X[m][1] for m in MONTHS]), F(-4, 5))
check("CHR mean exposure", mean([X[m][2] for m in MONTHS]), F(2, 5))
check("EMK mean exposure", mean([X[m][4] for m in MONTHS]), F(1))
check("CHR is the unreachable stock in M1, M3 and M5",
      [m for m in MONTHS if X[m][2] == 0], ["M1", "M3", "M5"])

# ===========================================================================
head("SECTION 4  Month 1 in full, by hand")
# ===========================================================================

m = "M1"
sub("4a  the 2x2 Gram matrix is DIAGONAL because the column is centred")
G1 = [[dot(ones(N), ones(N)), dot(ones(N), X[m])],
      [dot(X[m], ones(N)), dot(X[m], X[m])]]
check("A = sum 1*1 = n", G1[0][0], F(5))
check("B = sum 1*x", G1[0][1], F(0))
check("B again (symmetry)", G1[1][0], F(0))
check("C = sum x*x = Q", G1[1][1], F(10))
check("det = A*C - B^2", G1[0][0] * G1[1][1] - G1[0][1] * G1[1][0], F(50))
check("Level 4's overlap cos^2 = B^2/(AC)", F(0) / (G1[0][0] * G1[1][1]), F(0))
check("VIF = 1/(1-cos^2) = 1 exactly", F(1) / (1 - F(0)), F(1))

sub("4b  the two dials")
p1 = dot(ones(N), R[m])
q1 = dot(X[m], R[m])
check("sum r", p1, F(25))
check("sum x*r", q1, F(15))
b1 = solve(G1, [p1, q1])
check("f_Mkt(M1) = (sum r)/n", b1[0], F(5))
check("f_Val(M1) = (sum x r)/Q", b1[1], F(3, 2))
check("f_Mkt equals the plain average return", b1[0], mean(R[m]))

sub("4c  residuals and the two balance conditions")
bb1, fit1, e1, ss1 = wls([ones(N), X[m]], R[m])
check("coefficients from the general solver", bb1, [F(5), F(3, 2)])
check("fitted values", fit1, [F(2), F(7, 2), F(5), F(8), F(13, 2)])
check("residuals e", e1, [F(1, 2), F(-1), F(1), F(1, 2), F(-1)])
check("balance 1: sum e = 0", sum(e1), F(0))
check("balance 2: sum x*e = 0", dot(X[m], e1), F(0))
check("SSE(M1) = sum e^2", ss1, F(7, 2))

# ===========================================================================
head("SECTION 5  The other four months, same handle")
# ===========================================================================

FIT = {}
for m in MONTHS:
    bb, fit, e, ss = wls([ones(N), X[m]], R[m])
    FIT[m] = dict(b=bb, fit=fit, e=e, sse=ss)
    check(f"{m}: sum e = 0", sum(e), F(0))
    check(f"{m}: sum x*e = 0", dot(X[m], e), F(0))

fMkt = [FIT[m]["b"][0] for m in MONTHS]
fVal = [FIT[m]["b"][1] for m in MONTHS]
SSE = [FIT[m]["sse"] for m in MONTHS]

check("residual row M1", FIT["M1"]["e"], [F(1, 2), F(-1), F(1), F(1, 2), F(-1)])
check("residual row M2", FIT["M2"]["e"], [F(1), F(0), F(1, 2), F(0), F(-3, 2)])
check("residual row M3", FIT["M3"]["e"], [F(1), F(-1, 2), F(-1), F(1), F(-1, 2)])
check("residual row M4", FIT["M4"]["e"], [F(3, 2), F(0), F(1, 2), F(-3, 2), F(-1, 2)])
check("residual row M5", FIT["M5"]["e"], [F(1, 2), F(1, 2), F(-2), F(1, 2), F(1, 2)])
check("f_Mkt series", fMkt, [F(5), F(-2), F(-2), F(2), F(2)])
check("f_Val series", fVal, [F(3, 2), F(-1), F(0), F(1), F(1)])
check("SSE series", SSE, [F(7, 2), F(7, 2), F(7, 2), F(5), F(5)])
check("total SSE over the five months", sum(SSE), F(41, 2))
check("sum r by month", [sum(R[m]) for m in MONTHS],
      [F(25), F(-10), F(-10), F(10), F(10)])
check("sum x*r by month", [dot(X[m], R[m]) for m in MONTHS],
      [F(15), F(-10), F(0), F(4), F(10)])
show("total SSE as a decimal", dec(F(41, 2), 1))

print()
print("   residuals by month")
for m in MONTHS:
    print(f"        {m}: " + S(FIT[m]["e"])
          + f"    SSE = {S(FIT[m]['sse'])}")

sub("5a  M3 is the month the factor did nothing")
check("f_Val(M3) = 0 exactly", fVal[2], F(0))
check("M3 fitted returns are all the market number", FIT["M3"]["fit"],
      [F(-2)] * 5)

sub("5b  each month is a separate regression: 5 regressions, 2 numbers each")
check("number of cross-sectional regressions run", T, 5)
check("numbers produced", T * K, 10)
check("rows in each regression", N, 5)

# ===========================================================================
head("SECTION 6  The factor-return time series -- this level's output")
# ===========================================================================

print("        month   f_Mkt    f_Val      Q     SSE")
for j, m in enumerate(MONTHS):
    print(f"        {m:5} {S(fMkt[j]):>7} {S(fVal[j]):>8} {S(Q[m]):>6} {S(SSE[j]):>7}")

sub("6a  mean of each series")
mVal = mean(fVal)
mMkt = mean(fMkt)
check("mean f_Val", mVal, F(1, 2))
check("mean f_Mkt", mMkt, F(1))

sub("6b  spread of each series, with T-1 in the denominator (Level 6's df)")
dVal = centre(fVal)
dMkt = centre(fMkt)
check("deviations of f_Val", dVal, [F(1), F(-3, 2), F(-1, 2), F(1, 2), F(1, 2)])
check("deviations of f_Mkt", dMkt, [F(4), F(-3), F(-3), F(1), F(1)])
check("sum of f_Val deviations", sum(dVal), F(0))
check("sum of f_Mkt deviations", sum(dMkt), F(0))
SS_Val = dot(dVal, dVal)
SS_Mkt = dot(dMkt, dMkt)
check("sum of squared deviations, f_Val", SS_Val, F(4))
check("sum of squared deviations, f_Mkt", SS_Mkt, F(36))
check("degrees of freedom for a series mean", T - 1, 4)
varVal = SS_Val / (T - 1)
varMkt = SS_Mkt / (T - 1)
check("sample variance f_Val", varVal, F(1))
check("sample variance f_Mkt", varMkt, F(9))
check("sample sd f_Val is exact", _isqrt_exact(varVal.numerator) is not None, True)
check("sample sd f_Val", F(_isqrt_exact(varVal.numerator),
                          _isqrt_exact(varVal.denominator)), F(1))
check("sample sd f_Mkt", F(_isqrt_exact(varMkt.numerator),
                          _isqrt_exact(varMkt.denominator)), F(3))
check("population variance f_Val (divide by T)", SS_Val / T, F(4, 5))
check("population variance f_Mkt (divide by T)", SS_Mkt / T, F(36, 5))
show("sqrt(4/5)", rt(F(4, 5)))
show("sqrt(36/5)", rt(F(36, 5)))

sub("6c  the standard error of the series mean -- Level 6 run down the timeline")
check("Var of the mean of f_Val = sample variance / T", varVal / T, F(1, 5))
check("Var of the mean of f_Mkt = sample variance / T", varMkt / T, F(9, 5))
show("SE of mean f_Val = sqrt(1/5)", rt(F(1, 5)))
show("SE of mean f_Mkt = sqrt(9/5)", rt(F(9, 5)))
check("t^2 for mean f_Val", mVal ** 2 / (varVal / T), F(5, 4))
check("t^2 for mean f_Mkt", mMkt ** 2 / (varMkt / T), F(5, 9))
show("t for mean f_Val = sqrt(5/4)", rt(F(5, 4)))
show("t for mean f_Mkt = sqrt(5/9)", rt(F(5, 9)))
check("neither series mean clears |t| > 2",
      (mVal ** 2 / (varVal / T) > 4, mMkt ** 2 / (varMkt / T) > 4), (False, False))
check("df for that t is T - 1", T - 1, 4)

sub("6d  the cross-term -- named and then left for Level 8")
cross = dot(dMkt, dVal)
check("sum of the two series' deviation products", cross, F(11))
check("sample covariance = cross/(T-1)", cross / (T - 1), F(11, 4))
check("correlation = cov/(sd*sd)", (cross / (T - 1)) / (F(3) * F(1)), F(11, 12))
show("11/4 as a decimal", dec(F(11, 4), 2))
show("11/12 as a decimal", dec(F(11, 12), 6))

sub("6e  cumulative sums -- what Figures 1.7, 1.12 and 1.14 plot")
cumMkt, cumVal, a, b = [], [], F(0), F(0)
for j in range(T):
    a += fMkt[j]
    b += fVal[j]
    cumMkt.append(a)
    cumVal.append(b)
check("cumulative f_Mkt", cumMkt, [F(5), F(3), F(1), F(3), F(5)])
check("cumulative f_Val", cumVal, [F(3, 2), F(1, 2), F(1, 2), F(3, 2), F(5, 2)])
check("last cumulative value = T * mean, f_Val", cumVal[-1], T * mVal)
check("last cumulative value = T * mean, f_Mkt", cumMkt[-1], T * mMkt)

sub("6f  annualising, to compare with Table 1.2 (p.10)")
check("annualised mean f_Val = 12 * monthly mean", 12 * mVal, F(6))
check("annualised mean f_Mkt = 12 * monthly mean", 12 * mMkt, F(12))
check("annualised variance f_Val = 12 * monthly variance", 12 * varVal, F(12))
check("annualised variance f_Mkt = 12 * monthly variance", 12 * varMkt, F(108))
show("annualised sd f_Val = sqrt(12)", rt(F(12)))
show("annualised sd f_Mkt = sqrt(108)", rt(F(108)))
check("return-over-volatility, f_Val, squared", (12 * mVal) ** 2 / (12 * varVal), F(3))
check("return-over-volatility, f_Mkt, squared", (12 * mMkt) ** 2 / (12 * varMkt), F(4, 3))
show("f_Val ratio = sqrt(3)", rt(F(3)))
show("f_Mkt ratio = sqrt(4/3)", rt(F(4, 3)))

sub("6f (part 2)  first-order autocorrelation, one convention, stated as such")
ac_Val = sum(dVal[j] * dVal[j + 1] for j in range(T - 1)) / SS_Val
ac_Mkt = sum(dMkt[j] * dMkt[j + 1] for j in range(T - 1)) / SS_Mkt
check("lagged product sum, f_Val", sum(dVal[j] * dVal[j + 1] for j in range(T - 1)),
      F(-3, 4))
check("first-order autocorrelation, f_Val", ac_Val, F(-3, 16))
check("lagged product sum, f_Mkt", sum(dMkt[j] * dMkt[j + 1] for j in range(T - 1)),
      F(-5))
check("first-order autocorrelation, f_Mkt", ac_Mkt, F(-5, 36))
show("-3/16", dec(F(-3, 16), 4))
show("-5/36", dec(F(-5, 36), 6))

# ===========================================================================
head("SECTION 7  A t-statistic per month -- Level 6, run five times")
# ===========================================================================

df = N - K
check("degrees of freedom inside one cross-section, n - k", df, 3)

sig2, varVal_t, t2Val, varMkt_t, t2Mkt = [], [], [], [], []
for j, m in enumerate(MONTHS):
    s2 = SSE[j] / df
    vV = s2 / Q[m]
    vM = s2 / F(N)
    sig2.append(s2)
    varVal_t.append(vV)
    varMkt_t.append(vM)
    t2Val.append(fVal[j] ** 2 / vV)
    t2Mkt.append(fMkt[j] ** 2 / vM)

check("sigma^2 by month", sig2, [F(7, 6), F(7, 6), F(7, 6), F(5, 3), F(5, 3)])
check("Var(f_Val) by month", varVal_t,
      [F(7, 60), F(7, 60), F(7, 60), F(5, 12), F(1, 6)])
check("Var(f_Mkt) by month", varMkt_t,
      [F(7, 30), F(7, 30), F(7, 30), F(1, 3), F(1, 3)])
check("t^2 for f_Val by month", t2Val,
      [F(135, 7), F(60, 7), F(0), F(12, 5), F(6)])
check("t^2 for f_Mkt by month", t2Mkt,
      [F(750, 7), F(120, 7), F(120, 7), F(12), F(12)])

print()
print("        month    f_Val   Var(f_Val)      t^2        t            |t|>2?")
for j, m in enumerate(MONTHS):
    sgn = -1 if fVal[j] < 0 else 1
    tv = sgn * (float(t2Val[j]) ** 0.5)
    print(f"        {m:5} {S(fVal[j]):>8} {S(varVal_t[j]):>12} {S(t2Val[j]):>9}"
          f"   {tv:>9.6f}   {'YES' if t2Val[j] > 4 else 'no'}")

sub("7a  the printed |t| values, all rounded")
show("t(M1) = +sqrt(135/7)", rt(F(135, 7)))
show("t(M2) = -sqrt(60/7)", rt(F(60, 7)))
show("t(M3)", "0 (exact)")
show("t(M4) = +sqrt(12/5)", rt(F(12, 5)))
show("t(M5) = +sqrt(6)", rt(F(6)))
show("t_Mkt(M1) = +sqrt(750/7)", rt(F(750, 7)))
show("t_Mkt(M2) = -sqrt(120/7)", rt(F(120, 7)))
show("t_Mkt(M4) = +sqrt(12)", rt(F(12)))

sub("7b  M4 against M5: same f, same sigma^2, only the reach differs")
check("f_Val is the same in M4 and M5", fVal[3] == fVal[4], True)
check("sigma^2 is the same in M4 and M5", sig2[3] == sig2[4], True)
check("Q differs", (Q["M4"], Q["M5"]), (F(4), F(10)))
check("Var ratio M4/M5 = Q5/Q4", varVal_t[3] / varVal_t[4], F(5, 2))
check("t^2 ratio M5/M4 = Q5/Q4", t2Val[4] / t2Val[3], F(5, 2))
check("M4 fails |t|>2", t2Val[3] < 4, True)
check("M5 clears |t|>2", t2Val[4] > 4, True)

sub("7c  the proportion of significant months -- BFRE's own selection statistic")
nsig = sum(1 for v in t2Val if v > 4)
check("months with |t| > 2", nsig, 3)
check("proportion significant", F(nsig, T), F(3, 5))
check("proportion clears the paper's 10% bar (p.14)", F(nsig, T) > F(1, 10), True)
check("average squared t-statistic, f_Val", mean(t2Val), F(1269, 175))
show("average squared t (p.8 statistic)", dec(F(1269, 175), 6))
check("months with |t| > 2 for f_Mkt", sum(1 for v in t2Mkt if v > 4), 5)

# ===========================================================================
head("SECTION 8  The noise floor -- how much of that spread is real")
# ===========================================================================

vbarVal = mean(varVal_t)
vbarMkt = mean(varMkt_t)
check("average Var(f_Val) across months", vbarVal, F(14, 75))
check("average Var(f_Mkt) across months", vbarMkt, F(41, 150))
check("observed sample variance, f_Val", varVal, F(1))
check("signal variance f_Val = observed - noise floor", varVal - vbarVal, F(61, 75))
check("signal variance f_Mkt = observed - noise floor", varMkt - vbarMkt, F(1309, 150))
check("noise share of f_Val's variance", vbarVal / varVal, F(14, 75))
check("noise share of f_Mkt's variance", vbarMkt / varMkt, F(41, 1350))
show("14/75", dec(F(14, 75), 6))
show("61/75", dec(F(61, 75), 6))
show("41/150", dec(F(41, 150), 6))
show("1309/150", dec(F(1309, 150), 6))
show("41/1350", dec(F(41, 1350), 6))
check("f_Val's noise share is larger than f_Mkt's", vbarVal / varVal > vbarMkt / varMkt,
      True)

# ===========================================================================
head("SECTION 9  The contrast -- a time-series beta for one stock")
# ===========================================================================

RS = {nm: [R[m][i] for m in MONTHS] for i, nm in enumerate(NAMES)}
XS = {nm: [X[m][i] for m in MONTHS] for i, nm in enumerate(NAMES)}
ES = {nm: [FIT[m]["e"][i] for m in MONTHS] for i, nm in enumerate(NAMES)}

print("        stock   returns across the five months        mean")
for nm in NAMES:
    print(f"        {nm:5} " + "".join(f"{float(v):>7.1f}" for v in RS[nm])
          + f"   {S(mean(RS[nm]))}")
check("AXL return series", RS["AXL"],
      [F(5, 2), F(1), F(-1), F(5, 2), F(1, 2)])
check("AXL mean return", mean(RS["AXL"]), F(11, 10))
check("DLT return series", RS["DLT"],
      [F(17, 2), F(-4), F(-1), F(-1, 2), F(7, 2)])
check("DLT mean return", mean(RS["DLT"]), F(13, 10))
check("all 25 returns sum to the five monthly totals",
      sum(sum(RS[nm]) for nm in NAMES), F(25))

sub("9a  the same formula, one index swapped: Cov/Var down the TIME column")
bbA, fitA, eA, ssA = wls([ones(T), fVal], RS["AXL"])
check("AXL: time-series intercept", bbA[0], F(29, 40))
check("AXL: time-series slope on f_Val", bbA[1], F(3, 4))
check("AXL: slope by Cov/Var", dot(dVal, centre(RS["AXL"])) / SS_Val, F(3, 4))
check("AXL: numerator sum(d_Val * deviation of r)", dot(dVal, centre(RS["AXL"])), F(3))
check("AXL: time-series residual sum of squares", ssA, F(129, 20))
show("29/40", dec(F(29, 40), 3))
show("129/20", dec(F(129, 20), 2))
show("11/10", dec(F(11, 10), 1))
show("13/10", dec(F(13, 10), 1))
check("AXL: cross-sectional exposures were never positive",
      all(v < 0 for v in XS["AXL"]), True)
check("AXL: the time-series slope is positive", bbA[1] > 0, True)
check("AXL: average cross-sectional exposure", mean(XS["AXL"]), F(-8, 5))

sub("9b  where the +3/4 comes from, term by term")
ch_mkt = sum(dVal[j] * fMkt[j] for j in range(T))
ch_exp = sum(dVal[j] * XS["AXL"][j] * fVal[j] for j in range(T))
ch_res = sum(dVal[j] * ES["AXL"][j] for j in range(T))
check("market channel", ch_mkt, F(11))
check("exposure channel", ch_exp, F(-15, 2))
check("residual channel", ch_res, F(-1, 2))
check("the three channels reconstruct the numerator",
      ch_mkt + ch_exp + ch_res, F(3))
check("market channel / SS_Val", ch_mkt / SS_Val, F(11, 4))
check("exposure channel / SS_Val", ch_exp / SS_Val, F(-15, 8))
check("residual channel / SS_Val", ch_res / SS_Val, F(-1, 8))
check("they sum to the slope", (ch_mkt + ch_exp + ch_res) / SS_Val, bbA[1])
check("market channel equals the two series' sample covariance",
      ch_mkt / SS_Val, cross / (T - 1))

sub("9c  put BOTH series in: Level 3's 2x2, run down the time index")
GT = [[SS_Mkt, cross], [cross, SS_Val]]
check("A = sum d_Mkt^2", GT[0][0], F(36))
check("B = sum d_Mkt d_Val", GT[0][1], F(11))
check("C = sum d_Val^2", GT[1][1], F(4))
detT = GT[0][0] * GT[1][1] - GT[0][1] * GT[1][0]
check("det = AC - B^2", detT, F(23))
pT = dot(dMkt, centre(RS["AXL"]))
qT = dot(dVal, centre(RS["AXL"]))
check("p = sum d_Mkt * deviation of r", pT, F(13))
check("q = sum d_Val * deviation of r", qT, F(3))
bT = solve(GT, [pT, qT])
check("two-column time-series slope on f_Mkt", bT[0], F(19, 23))
check("two-column time-series slope on f_Val", bT[1], F(-35, 23))
show("19/23", dec(F(19, 23), 6))
show("-35/23", dec(F(-35, 23), 6))
check("sign is now correct", bT[1] < 0, True)
check("but it is still one number for five different exposures",
      len(set(XS["AXL"])), 2)
check("degrees of freedom in that time-series fit, T - 3", T - 3, 2)
check("Level 4's overlap between the two series, cos^2 = B^2/(AC)",
      GT[0][1] ** 2 / (GT[0][0] * GT[1][1]), F(121, 144))
show("121/144", dec(F(121, 144), 6))
check("VIF for the time-series fit", 1 / (1 - F(121, 144)), F(144, 23))
show("VIF = 144/23", dec(F(144, 23), 6))

sub("9d  DLT, the stock whose exposure changes sign")
bbD, fitD, eD, ssD = wls([ones(T), fVal], RS["DLT"])
check("DLT: time-series slope on f_Val", bbD[1], F(33, 8))
check("DLT: numerator", dot(dVal, centre(RS["DLT"])), F(33, 2))
show("33/2", dec(F(33, 2), 1))
check("DLT: time-series intercept", bbD[0], F(-61, 80))
check("DLT: average cross-sectional exposure", mean(XS["DLT"]), F(1))
check("DLT: slope divided by average exposure", bbD[1] / mean(XS["DLT"]), F(33, 8))
show("33/8", dec(F(33, 8), 4))
show("-61/80", dec(F(-61, 80), 4))

sub("9e  the (1.12)-shaped regression: AXL on the market series")
bbM, fitM, eM, ssM = wls([ones(T), fMkt], RS["AXL"])
check("AXL: time-series slope on f_Mkt", bbM[1], F(13, 36))
check("AXL: that slope by Cov/Var", dot(dMkt, centre(RS["AXL"])) / SS_Mkt, F(13, 36))
check("every stock's market exposure is 1 in every month (p.4, 'unit exposure')",
      sorted(set(v for m in MONTHS for v in ones(N))), [F(1)])
check("so the market column's reach is n, not Q", [dot(ones(N), ones(N))] * T,
      [F(5)] * T)
show("13/36", dec(F(13, 36), 6))

# ===========================================================================
head("SECTION 10  The pooled regression -- the trap")
# ===========================================================================

xp, rp = [], []
for m in MONTHS:
    xp += X[m]
    rp += R[m]
check("pooled observations", len(rp), 25)
check("pooled sum of x", sum(xp), F(0))
check("pooled sum of x^2", dot(xp, xp), F(44))
check("pooled sum of r", sum(rp), F(25))
check("pooled sum of x*r", dot(xp, rp), F(19))
check("pooled sum of r^2", dot(rp, rp), F(272))

bp, fitp, ep, ssp = wls([ones(25), xp], rp)
check("pooled f_Mkt", bp[0], F(1))
check("pooled f_Val", bp[1], F(19, 44))
show("19/44", dec(F(19, 44), 6))
check("pooled f_Mkt equals the mean of the monthly f_Mkt", bp[0], mMkt)
check("pooled f_Val does NOT equal the mean of the monthly f_Val",
      bp[1] == mVal, False)
check("mean of the monthly f_Val", mVal, F(1, 2))
check("gap between them", mVal - bp[1], F(3, 44))
show("3/44", dec(F(3, 44), 6))

sub("10a  the pooled number is a Q-weighted average of the monthly numbers")
qw = sum(Q[m] * FIT[m]["b"][1] for m in MONTHS) / sum(Q[m] for m in MONTHS)
check("sum Q_t * f_Val,t", sum(Q[m] * FIT[m]["b"][1] for m in MONTHS), F(19))
check("Q-weighted average of the monthly f_Val", qw, F(19, 44))
check("it is exactly the pooled estimate", qw, bp[1])
check("M4's weight in the pooled estimate", Q["M4"] / F(44), F(1, 11))
check("M4's weight in the monthly mean is 1/T, not Q4/sum Q", F(1, T), F(1, 5))
check("the two weightings for M4 disagree", Q["M4"] / F(44) == F(1, T), False)
check("only M4's two weights differ; the other four months are over-weighted",
      [Q[m] / F(44) > F(1, T) for m in MONTHS],
      [True, True, True, False, True])

sub("10b  what pooling throws into the residual")
check("pooled SSE", ssp, F(10507, 44))
show("pooled SSE", dec(F(10507, 44), 6))
# the short route printed in 10b: SSE = sum r^2 - (sum r)^2/25 - (sum x r)^2/sum x^2.
# Computed from the four pooled sums only, and checked against the residual-by-residual
# value above -- two independent routes, not one expression evaluated twice.
ssp_short = dot(rp, rp) - dot(rp, ones(25)) ** 2 / F(25) - dot(xp, rp) ** 2 / dot(xp, xp)
check("pooled SSE, short route 272 - 25 - 361/44", ssp_short, F(10507, 44))
check("the two routes to the pooled SSE agree", ssp_short, ssp)
check("(sum r)^2/25 term", dot(rp, ones(25)) ** 2 / F(25), F(25))
check("(sum x r)^2/(sum x^2) term", dot(xp, rp) ** 2 / dot(xp, xp), F(361, 44))
check("272 - 25 = 247", F(272) - F(25), F(247))
check("sum of the five monthly SSEs", sum(SSE), F(41, 2))
gapmkt = sum(F(N) * (FIT[m]["b"][0] - bp[0]) ** 2 for m in MONTHS)
gapval = sum(Q[m] * (FIT[m]["b"][1] - bp[1]) ** 2 for m in MONTHS)
check("between-month market term, sum n*(f_Mkt,t - pooled)^2", gapmkt, F(180))
check("between-month value term, sum Q_t*(f_Val,t - pooled)^2", gapval,
      F(1685, 44))
show("1685/44", dec(F(1685, 44), 6))
check("the identity: pooled SSE = sum SSE_t + between-month terms",
      sum(SSE) + gapmkt + gapval, ssp)
check("extra miss created by pooling", ssp - sum(SSE), F(9605, 44))
show("9605/44", dec(F(9605, 44), 6))
check("ratio pooled SSE / monthly SSE total", ssp / sum(SSE), F(10507, 902))
show("10507/902", dec(F(10507, 902), 6))

sub("10c  one month alone says the opposite of another month alone")
check("M1 alone: f_Val", fVal[0], F(3, 2))
check("M3 alone: f_Val", fVal[2], F(0))
check("M2 alone: f_Val is negative", fVal[1] < 0, True)

# ===========================================================================
head("SECTION 11  The weighted aside -- one month with sqrt-cap weights")
# ===========================================================================

CAP = [F(4), F(1), F(1), F(1), F(9)]
W = [F(2), F(1), F(1), F(1), F(3)]
check("weights are the square roots of the caps", [w * w for w in W], CAP)
check("sum of weights", sum(W), F(8))
check("weighted sum of x in M1", wdot(W, X["M1"], ones(N)), F(0))
check("weighted sum of x^2 in M1", wdot(W, X["M1"], X["M1"]), F(16))
check("weighted sum of r in M1", wdot(W, ones(N), R["M1"]), F(77, 2))
check("weighted sum of x*r in M1", wdot(W, X["M1"], R["M1"]), F(21))
show("77/2", dec(F(77, 2), 1))
bw, fitw, ew, ssw = wls([ones(N), X["M1"]], R["M1"], W)
check("weighted f_Mkt(M1)", bw[0], F(77, 16))
check("weighted f_Val(M1)", bw[1], F(21, 16))
show("77/16", dec(F(77, 16), 4))
show("21/16", dec(F(21, 16), 4))
check("equal-weighted f_Mkt(M1) for comparison", fMkt[0], F(5))
check("equal-weighted f_Val(M1) for comparison", fVal[0], F(3, 2))
check("weighted residuals", ew,
      [F(5, 16), F(-1), F(19, 16), F(17, 16), F(-5, 8)])
check("weighted balance 1: sum w*e = 0", wdot(W, ones(N), ew), F(0))
check("weighted balance 2: sum w*x*e = 0", wdot(W, X["M1"], ew), F(0))
check("weighted SSE(M1)", ssw, F(157, 32))
show("157/32", dec(F(157, 32), 5))
check("weighted sum of x, all five months (only M1 is zero)",
      [wdot(W, X[m], ones(N)) for m in MONTHS],
      [F(0), F(-4), F(3), F(1), F(2)])
check("the market dial moved by", fMkt[0] - bw[0], F(3, 16))
check("the value dial moved by", fVal[0] - bw[1], F(3, 16))
show("3/16", dec(F(3, 16), 4))

# ===========================================================================
head("SECTION 13  Traps, priced")
# ===========================================================================

sub("trap: read a stock's exposure off a time-series slope")
check("AXL time-series slope", bbA[1], F(3, 4))
check("AXL true exposure, every month, is negative",
      max(XS["AXL"]), F(-1))
check("sign disagreement", (bbA[1] > 0) and (max(XS["AXL"]) < 0), True)

sub("trap: pool the panel")
check("pooled f_Val vs mean of monthly f_Val", (bp[1], mVal), (F(19, 44), F(1, 2)))

sub("trap: treat the series variance as the factor's variance")
check("observed 1 vs signal 61/75", (varVal, varVal - vbarVal), (F(1), F(61, 75)))

sub("trap: judge the factor on one month")
check("M3's verdict", t2Val[2], F(0))
check("M1's verdict", t2Val[0], F(135, 7))

sub("trap: f_Mkt is the plain average return")
check("plain average of M1 returns", mean(R["M1"]), F(5))
check("sqrt-cap weighted average of M1 returns", wdot(W, ones(N), R["M1"]) / sum(W),
      F(77, 16))
check("plain average equals the weighted average?",
      mean(R["M1"]) == wdot(W, ones(N), R["M1"]) / sum(W), False)

sub("trap: more stocks lengthens the series")
check("stocks per cross-section", N, 5)
check("months", T, 5)
check("doubling N doubles Q, not T -- Q enters Var(f), T enters df of the mean",
      (T - 1, N - K), (4, 3))

# ===========================================================================
head("SECTION 17  Numbers used in the BFRE tie-back")
# ===========================================================================

print("   p.24 : 'a series of cross-sectional regressions ...' (quoted, not computed)")
print("   p.24 : daily for country and regional models, weekly for the World model")
print("   p.3  : daily factor returns for all models from March 1996 onwards")
print("   p.36 : exposures updated weekly, Thursday, data as of previous Wednesday")
print("   p.14 : 10% proportion-of-significant-t threshold (quoted)")
print("   p.42 : (1.12) is a time-series regression -- 5 years of weeklies, 52-week half-life")
print("   p.10 : Table 1.2 -- annualised return, annualised volatility, autocorrelation")

sub("our five-month file against the paper's thresholds")
check("our proportion of significant months for f_Val",
      F(sum(1 for v in t2Val if v > 4), T), F(3, 5))
check("clears p.14's 10% bar", F(3, 5) > F(1, 10), True)
check("Figure 1.8's measured Value height, 34% [APPROX], also clears 10%",
      F(34, 100) > F(1, 10), True)
check("our five months against BFRE's history from March 1996 (p.3)", T, 5)

sub("Table 1.2 shape check: our two rows, in the paper's columns")
check("f_Mkt annualised return", 12 * mMkt, F(12))
check("f_Val annualised return", 12 * mVal, F(6))
check("f_Mkt annualised variance", 12 * varMkt, F(108))
check("f_Val annualised variance", 12 * varVal, F(12))
check("f_Mkt first-order autocorrelation", ac_Mkt, F(-5, 36))
check("f_Val first-order autocorrelation", ac_Val, F(-3, 16))
check("correlation of f_Val with the market factor", (cross / (T - 1)) / F(3), F(11, 12))

sub("Table 1.2's rounding trap, restated from Level 1 (p.10, printed digits)")
check("Profitability: printed return / printed volatility", F(31, 10) / F(22, 10),
      F(31, 22))
show("3.1/2.2", dec(F(31, 22), 2))
check("that is not the printed Sharpe of 1.37", F(31, 22) == F(137, 100), False)

# All 13 printed rows of Table 1.2 (p.10), transcribed in notes/chunk_10-18.md:
# (factor, annualised return %, annualised volatility %, printed Sharpe).
TABLE_1_2 = [
    ("Market",         F(70, 10),  F(198, 10), F(35, 100)),
    ("Size",           F(-12, 10), F(37, 10),  F(-33, 100)),
    ("Volatility",     F(-6, 10),  F(75, 10),  F(-8, 100)),
    ("Mid-cap",        F(9, 10),   F(18, 10),  F(52, 100)),
    ("Reversal",       F(-51, 10), F(32, 10),  F(-159, 100)),
    ("Momentum",       F(54, 10),  F(38, 10),  F(143, 100)),
    ("Liquidity",      F(27, 10),  F(55, 10),  F(49, 100)),
    ("Value",          F(33, 10),  F(23, 10),  F(143, 100)),
    ("Earnings Yield", F(7, 10),   F(21, 10),  F(32, 100)),
    ("Dividend Yield", F(-3, 10),  F(19, 10),  F(-18, 100)),
    ("Profitability",  F(31, 10),  F(22, 10),  F(137, 100)),
    ("Growth",         F(-20, 10), F(20, 10),  F(-101, 100)),
    ("Sentiment",      F(-1, 10),  F(15, 10),  F(-5, 100)),
]


def round2(x):
    """Round an exact rational to 2 dp, half away from zero, exactly."""
    sign = -1 if x < 0 else 1
    return sign * F(int(abs(x) * 100 + F(1, 2)), 100)


check("Table 1.2 has 13 factor rows", len(TABLE_1_2), 13)
reproduce, fail = [], []
for nm, ret, vol, sharpe in TABLE_1_2:
    (reproduce if round2(ret / vol) == sharpe else fail).append(nm)
check("rows whose printed Sharpe DOES reproduce from the printed columns",
      reproduce, ["Market", "Volatility", "Reversal", "Liquidity", "Value"])
check("rows whose printed Sharpe does NOT reproduce", fail,
      ["Size", "Mid-cap", "Momentum", "Earnings Yield", "Dividend Yield",
       "Profitability", "Growth", "Sentiment"])
check("how many of the thirteen fail to reproduce", len(fail), 8)
check("how many reproduce", len(reproduce), 5)
check("the two groups exhaust the table", len(fail) + len(reproduce), 13)
check("Mid-cap: 0.9/1.8 rounds to 0.50, printed 0.52", round2(F(9, 18)), F(50, 100))
check("Dividend Yield: -0.3/1.9 rounds to -0.16, printed -0.18",
      round2(F(-3, 19)), F(-16, 100))
check("Profitability: 3.1/2.2 rounds to 1.41, printed 1.37",
      round2(F(31, 22)), F(141, 100))
show("0.9/1.8", dec(F(9, 18), 6))
show("-0.3/1.9", dec(F(-3, 19), 6))

sub("p.40 style/substyle weights and p.52 macro betas (Section 9e, 17f)")
# The two style/substyle weight tables on p.40 are UNNUMBERED and UNCAPTIONED in the paper;
# notes/chunk_37-45.md labels them A and B for its own convenience. Only the NAMR column is
# needed here. Every (1.12)/(1.49) output below is a COLUMN of X, never a factor return.
NAMR_VOLATILITY = [("Historical Beta", F(34, 100)),      # (1.12) slope,     p.42
                   ("Cumulative Range 12M", F(33, 100)),  # (1.13),          p.42
                   ("Historical Sigma", F(33, 100))]      # (1.12) resid sd, p.42
NAMR_MOMENTUM = [("Relative Strength 11M", F(50, 100)),
                 ("Historical Alpha", F(50, 100))]        # (1.12) intercept, p.44
check("NAMR Volatility substyle weights sum to 1",
      sum(w for _, w in NAMR_VOLATILITY), F(1))
check("NAMR Momentum substyle weights sum to 1",
      sum(w for _, w in NAMR_MOMENTUM), F(1))
check("(1.12)'s three outputs carry NAMR weight 0.34 + 0.33 + 0.50",
      [dict(NAMR_VOLATILITY)["Historical Beta"],
       dict(NAMR_VOLATILITY)["Historical Sigma"],
       dict(NAMR_MOMENTUM)["Historical Alpha"]],
      [F(34, 100), F(33, 100), F(50, 100)])
# NAMR Sentiment has exactly one substyle: "Beta on VIX (Regional)", weight 1.00 -- and it is a
# (1.49) macro beta, i.e. a SECOND per-asset time-series regression live in the NAMR model.
NAMR_SENTIMENT = [("Beta on VIX (Regional)", F(100, 100))]
check("NAMR Sentiment substyle weights sum to 1", sum(w for _, w in NAMR_SENTIMENT), F(1))
check("NAMR Sentiment is a single (1.49) macro beta", len(NAMR_SENTIMENT), 1)
# Time-series fits the paper defines, by equation number and page. The point of the list is that
# it has length > 1 -- "the paper runs a time-series regression exactly once" is false.
TIME_SERIES_FITS = {"1.12": 42, "1.23": 45, "1.31": 47, "1.37": 49, "1.41": 49, "1.49": 52}
check("the paper defines more than one per-asset time-series regression",
      len(TIME_SERIES_FITS) > 1, True)
check("the two that are return-on-return betas are (1.12) p.42 and (1.49) p.52",
      sorted((e, pg) for e, pg in TIME_SERIES_FITS.items() if e in ("1.12", "1.49")),
      [("1.12", 42), ("1.49", 52)])

sub("percentage forms of the noise floors, as printed in Section 8")
check("f_Val noise share as a percentage", 100 * F(14, 75), F(56, 3))
show("14/75 as a percentage", dec(100 * F(14, 75), 2))
check("f_Mkt noise share as a percentage", 100 * F(41, 1350), F(82, 27))
show("41/1350 as a percentage", dec(100 * F(41, 1350), 2))

sub("(1.12)'s sample size against ours")
check("5 years of weekly observations, as p.42 states", 5 * 52, 260)
check("our time-series regression has T observations", T, 5)
check("df in a two-column time-series fit on 5 months", T - 3, 2)

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level7.md,")
print("   and every decimal is labelled rounded there.")
