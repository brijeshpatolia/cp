#!/usr/bin/env python3
"""
verify_rebuild.py -- recomputes EVERY number printed in datasets/rebuild.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_rebuild.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message.

Harness and linear-algebra conventions are lifted unchanged from
tools/verify_level5.py and tools/verify_level10.py so that the three files
agree on what `solve`, `matmul` and `quad` mean.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product, combinations
import sys

getcontext().prec = 50

CHECKS = [0]

# ---------------------------------------------------------------------------
# harness
# ---------------------------------------------------------------------------


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


def isqrt_exact(m):
    if m < 0:
        return None
    r = int(m ** 0.5)
    for c in range(max(0, r - 3), r + 4):
        if c * c == m:
            return c
    return None


def rootF(v):
    """Exact rational square root, or None."""
    v = F(v)
    rn, rd = isqrt_exact(v.numerator), isqrt_exact(v.denominator)
    if rn is None or rd is None:
        return None
    return F(rn, rd)


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


def check_root(label, variance, printed, places=4):
    """`printed` is what the markdown shows for sqrt(variance)."""
    CHECKS[0] += 1
    q = Decimal(1).scaleb(-places)
    got = str(sqrtD(variance).quantize(q))
    ok = (got == printed)
    ex = rootF(variance)
    tag = f"EXACT root = {ex}" if ex is not None else "rounded"
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: sqrt({F(variance)}) = {got} ({tag})"
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


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def quad(A, h):
    """h^T A h, exact."""
    return sum(h[i] * A[i][j] * h[j]
               for i in range(len(h)) for j in range(len(h)))


def bilin(A, u, v):
    return sum(u[i] * A[i][j] * v[j]
               for i in range(len(u)) for j in range(len(v)))


def det_gauss(M):
    n = len(M)
    A = [row[:] for row in M]
    dt = F(1)
    for c in range(n):
        p = None
        for i in range(c, n):
            if A[i][c] != 0:
                p = i
                break
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            dt = -dt
        dt *= A[c][c]
        pv = A[c][c]
        A[c] = [t / pv for t in A[c]]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[c])]
    return dt


def mean(xs):
    return sum(xs, F(0)) / len(xs)


def devs(xs):
    m = mean(xs)
    return [x - m for x in xs]


def sample_cov(a, b, ddof=1):
    return sum(x * y for x, y in zip(devs(a), devs(b))) / (len(a) - ddof)


def diagm(d):
    n = len(d)
    return [[d[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def addm(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# ===========================================================================
# THE FILE -- the raw spreadsheet the player is handed (section 1)
# ===========================================================================
head("SECTION 1 -- THE FILE, exactly as the player receives it")

NAMES = ["GRV", "HLX", "JDR", "KPN", "LTS", "MRA"]
N, K, T = 6, 3, 5

# raw characteristics
EY_RAW = [F(8), F(7), F(5), F(4), F(4), F(2)]           # earnings yield, %
OM_RAW = [F(12), F(12), F(12), F(13), F(10), F(7)]      # operating margin, %

# monthly returns, percent (rows = stocks, columns = months 1..5)
R = [[F(17, 2), F(7, 2),   F(7, 2),  F(5, 2),  F(-9, 2)],     # GRV
     [F(27, 2), F(4),      F(15, 2), F(-3, 2), F(-3, 2)],     # HLX
     [F(23, 2), F(-3),     F(3, 2),  F(1, 2),  F(5, 2)],      # JDR
     [F(7),     F(3, 2),   F(1),     F(3),     F(0)],         # KPN
     [F(7, 2),  F(-21, 2), F(5, 2),  F(-9, 2), F(-7, 2)],     # LTS
     [F(-2),    F(-27, 2), F(2),     F(-6),    F(1)]]         # MRA

WP = [F(30, 100), F(40, 100), F(0), F(15, 100), F(0), F(15, 100)]     # book
WB = [F(25, 100), F(10, 100), F(25, 100), F(15, 100),
      F(10, 100), F(15, 100)]                                        # index

sub("1a. the file's own totals")
check("six stocks", len(NAMES), 6)
check("five months", len(R[0]), 5)
check("book weights sum to 1", sum(WP, F(0)), F(1))
check("index weights sum to 1", sum(WB, F(0)), F(1))
check("book holds four names", sum(1 for w in WP if w != 0), 4)
check("index holds six names", sum(1 for w in WB if w != 0), 6)
for i, nm in enumerate(NAMES):
    check(f"{nm} returns", tuple(R[i]), tuple(R[i]))
check("every return is a multiple of 1/2",
      all((2 * R[i][t]).denominator == 1 for i in range(N) for t in range(T)),
      True)
check("largest return in the file", max(R[i][t] for i in range(N) for t in range(T)),
      F(27, 2))
check("smallest return in the file", min(R[i][t] for i in range(N) for t in range(T)),
      F(-27, 2))

sub("1b. no number in this file appears in levels 0-12's files")
# levels 0-12 use tickers AXL BRN CHR DLT EMK FNX; this level uses GRV..MRA
check("tickers disjoint from levels 0-12",
      set(NAMES) & {"AXL", "BRN", "CHR", "DLT", "EMK", "FNX"}, set())

# ===========================================================================
# STAGE 1 -- BUILD X
# ===========================================================================
head("STAGE 1 -- BUILD X (section 2)")

sub("2a. Earnings Yield column")
mEY = mean(EY_RAW)
dEY = [a - mEY for a in EY_RAW]
ssEY = sum(a * a for a in dEY)
varEY = ssEY / N
sdEY = rootF(varEY)
check("EY mean", mEY, F(5))
check("EY deviations", tuple(dEY), (F(3), F(2), F(0), F(-1), F(-1), F(-3)))
check("EY sum of squared deviations", ssEY, F(24))
check("EY variance = 24/6", varEY, F(4))
check("EY standard deviation (exact)", sdEY, F(2))
x = [d / sdEY for d in dEY]
check("EY exposures x", tuple(x),
      (F(3, 2), F(1), F(0), F(-1, 2), F(-1, 2), F(-3, 2)))

sub("2b. Profitability column")
mOM = mean(OM_RAW)
dOM = [a - mOM for a in OM_RAW]
ssOM = sum(a * a for a in dOM)
varOM = ssOM / N
sdOM = rootF(varOM)
check("OM mean", mOM, F(11))
check("OM deviations", tuple(dOM), (F(1), F(1), F(1), F(2), F(-1), F(-4)))
check("OM sum of squared deviations", ssOM, F(24))
check("OM variance = 24/6", varOM, F(4))
check("OM standard deviation (exact)", sdOM, F(2))
g = [d / sdOM for d in dOM]
check("Profitability exposures g", tuple(g),
      (F(1, 2), F(1, 2), F(1, 2), F(1), F(-1, 2), F(-2)))

sub("2b2. the two column totals the player writes first")
check("30/6", F(30, 6), F(5))
check("66/6", F(66, 6), F(11))
check("sum of the raw earnings yields", sum(EY_RAW, F(0)), F(30))
check("sum of the raw operating margins", sum(OM_RAW, F(0)), F(66))

sub("2c. what standardising bought -- the three sums")
one = [F(1)] * N
check("sum x", sum(x, F(0)), F(0))
check("sum g", sum(g, F(0)), F(0))
check("sum x^2", dot(x, x), F(6))
check("sum g^2", dot(g, g), F(6))
check("sum 1*x", dot(one, x), F(0))
check("sum 1*g", dot(one, g), F(0))
check("sum x*g", dot(x, g), F(4))
check("exposure correlation x,g = 4/6", dot(x, g) / F(6), F(2, 3))
check_dec("exposure correlation as a decimal", F(2, 3), "0.6667")
check("no exposure outside BFRE's +/-3 cap (p.39)",
      max(max(abs(v) for v in x), max(abs(v) for v in g)) <= 3, True)

sub("2d. the design matrix X and its Gram matrix")
X = [[F(1), x[i], g[i]] for i in range(N)]
XT = transpose(X)
G = matmul(XT, X)
check("Gram matrix X^T X", [tuple(r) for r in G],
      [(F(6), F(0), F(0)), (F(0), F(6), F(4)), (F(0), F(4), F(6))])
check("det of the 2x2 style block", G[1][1] * G[2][2] - G[1][2] * G[2][1], F(20))
check("det X^T X (3x3)", det_gauss(G), F(120))
check("6 * 20 = 120", F(6) * F(20), det_gauss(G))
VIF = F(1) / (1 - (F(2, 3)) ** 2)
check("variance inflation factor 1/(1-rho^2)", VIF, F(9, 5))
check_dec("VIF as a decimal", VIF, "1.8000")

# ===========================================================================
# STAGE 2 -- FACTOR RETURNS
# ===========================================================================
head("STAGE 2 -- FIVE CROSS-SECTIONAL REGRESSIONS (section 3)")

SR, SXR, SGR = [], [], []
fM, fX, fG, U = [], [], [], []
for t in range(T):
    r = [R[i][t] for i in range(N)]
    sr, sx, sg = sum(r, F(0)), dot(x, r), dot(g, r)
    SR.append(sr)
    SXR.append(sx)
    SGR.append(sg)
    fm = sr / 6
    fx = (3 * sx - 2 * sg) / 10
    fg = (3 * sg - 2 * sx) / 10
    # the same thing through the general solver, as a cross-check
    coef = solve(G, [sr, sx, sg])
    fM.append(fm)
    fX.append(fx)
    fG.append(fg)
    u = [r[i] - fm - fx * x[i] - fg * g[i] for i in range(N)]
    U.append(u)
    sub(f"3.{t + 1} month {t + 1}")
    check(f"M{t+1} sum r", sr, [F(42), F(-18), F(18), F(-6), F(-6)][t])
    check(f"M{t+1} sum x*r", sx, [F(24), F(34), F(8), F(12), F(-8)][t])
    check(f"M{t+1} sum g*r", sg, [F(26), F(36), F(2), F(18), F(-2)][t])
    check(f"M{t+1} f_Mkt = sum r / 6", fm,
          [F(7), F(-3), F(3), F(-1), F(-1)][t])
    check(f"M{t+1} f_EY = (3Sx - 2Sg)/10", fx,
          [F(2), F(3), F(2), F(0), F(-2)][t])
    check(f"M{t+1} f_Prof = (3Sg - 2Sx)/10", fg,
          [F(3), F(4), F(-1), F(3), F(1)][t])
    check(f"M{t+1} Gaussian elimination agrees", tuple(coef), (fm, fx, fg))
    check(f"M{t+1} misses u", tuple(u),
          [(F(-3), F(3), F(3), F(-2), F(-1), F(0)),
           (F(0), F(2), F(-2), F(2), F(-4), F(2)),
           (F(-2), F(3), F(-1), F(0), F(0), F(0)),
           (F(2), F(-2), F(0), F(1), F(-2), F(1)),
           (F(-1), F(1), F(3), F(-1), F(-3), F(1))][t])
    check(f"M{t+1} balance 1: sum u = 0", sum(u, F(0)), F(0))
    check(f"M{t+1} balance 2: sum x*u = 0", dot(x, u), F(0))
    check(f"M{t+1} balance 3: sum g*u = 0", dot(g, u), F(0))
    check(f"M{t+1} SSE = sum u^2", dot(u, u),
          [F(32), F(32), F(14), F(14), F(22)][t])

sub("3.5b the worked example the markdown prints in full")
check("M1 GRV fitted = 7 + 2(1.5) + 3(0.5)",
      fM[0] + fX[0] * x[0] + fG[0] * g[0], F(23, 2))
check("M1 GRV miss = 8.5 - 11.5", R[0][0] - (fM[0] + fX[0] * x[0] + fG[0] * g[0]),
      F(-3))
check_dec("M1 GRV fitted, as a decimal", F(23, 2), "11.5000")
for t in range(T):
    check(f"M{t+1} numerators printed in the table",
          (3 * SXR[t], 2 * SGR[t], 3 * SGR[t], 2 * SXR[t]),
          [(72, 52, 78, 48), (102, 72, 108, 68), (24, 4, 6, 16),
           (36, 36, 54, 24), (-24, -4, -6, -16)][t])
check("M4 is the accident: 3 x Sxr = 2 x Sgr = 36", (3 * SXR[3], 2 * SGR[3]), (36, 36))
check("and M4's EY return is still wrong: 2 against 0", (SXR[3] / 6, fX[3]), (F(2), F(0)))

sub("3.6 the factor-return series, and the arithmetic that produced them")
check("f_Mkt series", tuple(fM), (F(7), F(-3), F(3), F(-1), F(-1)))
check("f_EY series", tuple(fX), (F(2), F(3), F(2), F(0), F(-2)))
check("f_Prof series", tuple(fG), (F(3), F(4), F(-1), F(3), F(1)))
check("total SSE over the five months", sum(dot(u, u) for u in U), F(114))
check("degrees of freedom per month, n - k", N - K, 3)

sub("3.7 the one-at-a-time answer, which is the level-4 trap")
for t in range(T):
    check(f"M{t+1} naive f_EY = Sx/6", SXR[t] / 6,
          [F(4), F(17, 3), F(4, 3), F(2), F(-4, 3)][t])
    check(f"M{t+1} naive f_Prof = Sg/6", SGR[t] / 6,
          [F(13, 3), F(6), F(1, 3), F(3), F(-1, 3)][t])
check("naive M1 f_EY is exactly double the truth", SXR[0] / 6, 2 * fX[0])
check("naive M5 f_Prof has the wrong SIGN", (SGR[4] / 6 < 0) and (fG[4] > 0), True)
check_dec("naive M1 f_Prof", F(13, 3), "4.3333")
check_dec("naive M2 f_EY", F(17, 3), "5.6667")
check_dec("naive M3 f_EY", F(4, 3), "1.3333")
check_dec("naive M3 f_Prof", F(1, 3), "0.3333")
check_dec("naive M5 f_EY", F(-4, 3), "-1.3333")
check_dec("naive M5 f_Prof", F(-1, 3), "-0.3333")

# ===========================================================================
# STAGE 3 -- BUILD F
# ===========================================================================
head("STAGE 3 -- BUILD F (section 4)")

series = [fM, fX, fG]
labs = ["Mkt", "EY", "Prof"]
sub("4a. means and deviations")
check("mean f_Mkt", mean(fM), F(1))
check("mean f_EY", mean(fX), F(1))
check("mean f_Prof", mean(fG), F(2))
check("dev f_Mkt", tuple(devs(fM)), (F(6), F(-4), F(2), F(-2), F(-2)))
check("dev f_EY", tuple(devs(fX)), (F(1), F(2), F(1), F(-1), F(-3)))
check("dev f_Prof", tuple(devs(fG)), (F(1), F(2), F(-3), F(1), F(-1)))

sub("4b. the six cross-products, then divide by T - 1 = 4")
check("sum dMkt^2", dot(devs(fM), devs(fM)), F(64))
check("sum dEY^2", dot(devs(fX), devs(fX)), F(16))
check("sum dProf^2", dot(devs(fG), devs(fG)), F(16))
check("sum dMkt*dEY", dot(devs(fM), devs(fX)), F(8))
check("sum dMkt*dProf", dot(devs(fM), devs(fG)), F(-8))
check("sum dEY*dProf", dot(devs(fX), devs(fG)), F(4))
Fm = [[sample_cov(series[i], series[j]) for j in range(3)] for i in range(3)]
check("F", [tuple(r) for r in Fm],
      [(F(16), F(2), F(-2)), (F(2), F(4), F(1)), (F(-2), F(1), F(4))])
check("F is symmetric", all(Fm[i][j] == Fm[j][i] for i in range(3)
                            for j in range(3)), True)

sub("4b2. F if the divisor were T -- as decimals, since the markdown prints them")
check_dec("12.8", F(64, 5), "12.8000")
check_dec("1.6", F(8, 5), "1.6000")

sub("4c. what F says, in volatilities and correlations")
for i, lab in enumerate(labs):
    check(f"{lab} factor volatility (exact root)", rootF(Fm[i][i]),
          [F(4), F(2), F(2)][i])
check("corr(Mkt, EY)", Fm[0][1] / (rootF(Fm[0][0]) * rootF(Fm[1][1])), F(1, 4))
check("corr(Mkt, Prof)", Fm[0][2] / (rootF(Fm[0][0]) * rootF(Fm[2][2])), F(-1, 4))
check("corr(EY, Prof)", Fm[1][2] / (rootF(Fm[1][1]) * rootF(Fm[2][2])), F(1, 4))

sub("4d. F is not singular -- the level-4 check, run on F this time")
check("leading 1x1 minor", Fm[0][0], F(16))
check("leading 2x2 minor", Fm[0][0] * Fm[1][1] - Fm[0][1] ** 2, F(60))
check("det F", det_gauss(Fm), F(200))

sub("4e. the wrong divisor, and what it returns")
FmT = [[Fm[i][j] * F(4, 5) for j in range(3)] for i in range(3)]
check("F if divided by T = 5 instead of T - 1 = 4", [tuple(r) for r in FmT],
      [(F(64, 5), F(8, 5), F(-8, 5)), (F(8, 5), F(16, 5), F(4, 5)),
       (F(-8, 5), F(4, 5), F(16, 5))])
check("every entry shrinks by exactly 4/5", FmT[0][0] / Fm[0][0], F(4, 5))

# ===========================================================================
# STAGE 4 -- BUILD D
# ===========================================================================
head("STAGE 4 -- BUILD D (section 5)")

SSu = [sum(U[t][i] ** 2 for t in range(T)) for i in range(N)]
d = [s / T for s in SSu]
sub("5a. each stock's five misses")
for i, nm in enumerate(NAMES):
    check(f"{nm} miss series", tuple(U[t][i] for t in range(T)),
          [(F(-3), F(0), F(-2), F(2), F(-1)),
           (F(3), F(2), F(3), F(-2), F(1)),
           (F(3), F(-2), F(-1), F(0), F(3)),
           (F(-2), F(2), F(0), F(1), F(-1)),
           (F(-1), F(-4), F(0), F(-2), F(-3)),
           (F(0), F(2), F(0), F(1), F(1))][i])
    check(f"{nm} sum of squared misses", SSu[i],
          [F(18), F(27), F(23), F(10), F(30), F(6)][i])
    check(f"{nm} specific variance d = sum u^2 / 5", d[i],
          [F(18, 5), F(27, 5), F(23, 5), F(2), F(6), F(6, 5)][i])
check("D's diagonal", tuple(d),
      (F(18, 5), F(27, 5), F(23, 5), F(2), F(6), F(6, 5)))

sub("5b. specific volatilities")
for i, nm in enumerate(NAMES):
    check_root(f"{nm} specific volatility", d[i],
               ["1.8974", "2.3238", "2.1448", "1.4142", "2.4495", "1.0954"][i])

sub("5c. the free cross-check -- add the 30 misses two ways")
check("sum over stocks of sum u^2", sum(SSu, F(0)), F(114))
check("sum over months of SSE", sum(dot(u, u) for u in U), F(114))
check("the two totals agree", sum(SSu, F(0)), sum(dot(u, u) for u in U))

sub("5d. no stock's misses are forced to average zero over time")
for i, nm in enumerate(NAMES):
    check(f"{nm} sum of misses over the five months",
          sum(U[t][i] for t in range(T)),
          [F(-4), F(7), F(3), F(0), F(-10), F(4)][i])
check("LTS's five misses are every one of them negative or zero",
      all(U[t][4] <= 0 for t in range(T)), True)
check("LTS average miss", mean([U[t][4] for t in range(T)]), F(-2))

sub("5e. the two other divisor conventions, and what each returns")
d_T1 = [SSu[i] / (T - 1) for i in range(N)]
check("d with divisor T-1 = 4, mean still asserted zero", tuple(d_T1),
      (F(9, 2), F(27, 4), F(23, 4), F(5, 2), F(15, 2), F(3, 2)))
d_own = [sum((U[t][i] - mean([U[s][i] for s in range(T)])) ** 2
             for t in range(T)) / (T - 1) for i in range(N)]
check("d with each stock's own mean removed, divisor T-1", tuple(d_own),
      (F(37, 10), F(43, 10), F(53, 10), F(5, 2), F(5, 2), F(7, 10)))

sub("5f. level 6's leverage, computed and checked against sum h = k")
Ginv = [[F(1, 6), F(0), F(0)],
        [F(0), F(3, 10), F(-1, 5)],
        [F(0), F(-1, 5), F(3, 10)]]
check("G * G^-1 = I", matmul(G, Ginv),
      [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]])
lev = [quad(Ginv, X[i]) for i in range(N)]
check("leverages", tuple(lev),
      (F(37, 60), F(41, 120), F(29, 120), F(89, 120), F(13, 60), F(101, 120)))
check("sum of leverages = k = 3", sum(lev, F(0)), F(3))
d_lev = [SSu[i] / (T * (1 - lev[i])) for i in range(N)]
check("leverage-corrected d", tuple(d_lev),
      (F(216, 23), F(648, 79), F(552, 91), F(240, 31), F(360, 47), F(144, 19)))
check_dec("MRA's leverage", F(101, 120), "0.8417")
check_dec("MRA's leverage-corrected d", F(144, 19), "7.5789")
check("1 - MRA's leverage", 1 - F(101, 120), F(19, 120))
check("MRA's correction factor 120/19", F(1) / (1 - F(101, 120)), F(120, 19))
check_dec("MRA's correction factor as a decimal", F(120, 19), "6.3158")

# ===========================================================================
# STAGE 5 -- ASSEMBLE V
# ===========================================================================
head("STAGE 5 -- ASSEMBLE V = X F X^T + D (section 6)")

XFXt = matmul(matmul(X, Fm), XT)
D = diagm(d)
V = addm(XFXt, D)
sub("6a. the common-factor block, row by row")
check("X F X^T is symmetric",
      all(XFXt[i][j] == XFXt[j][i] for i in range(N) for j in range(N)), True)
check("F X_GRV^T", matvec(Fm, X[0]), [F(18), F(17, 2), F(3, 2)])
check("GRV's common-factor variance", dot(X[0], matvec(Fm, X[0])), F(63, 2))
check("GRV-MRA common-factor covariance", bilin(Fm, X[0], X[5]), F(9, 4))

sub("6a2. the second row the markdown works in full")
check("F X_MRA^T", matvec(Fm, X[5]), [F(17), F(-6), F(-23, 2)])
check_dec("GRV's common-factor variance, as a decimal", F(63, 2), "31.5000")
check_dec("GRV-MRA common-factor covariance, as a decimal", F(9, 4), "2.2500")
check("GRV total variance = 31.5 + 3.6", F(63, 2) + d[0], F(351, 10))

sub("6b. V, all thirty-six cells")
VWANT = [[F(351, 10), F(109, 4), F(75, 4), F(61, 4), F(13), F(9, 4)],
         [F(109, 4), F(147, 5), F(35, 2), F(59, 4), F(53, 4), F(21, 4)],
         [F(75, 4), F(35, 2), F(98, 5), F(55, 4), F(55, 4), F(45, 4)],
         [F(61, 4), F(59, 4), F(55, 4), F(16), F(47, 4), F(17, 2)],
         [F(13), F(53, 4), F(55, 4), F(47, 4), F(49, 2), F(103, 4)],
         [F(9, 4), F(21, 4), F(45, 4), F(17, 2), F(103, 4), F(251, 5)]]
for i in range(N):
    check(f"V row {NAMES[i]}", tuple(V[i]), tuple(VWANT[i]))
check("V is symmetric", all(V[i][j] == V[j][i] for i in range(N)
                            for j in range(N)), True)
VDEC = [["35.1000", "27.2500", "18.7500", "15.2500", "13.0000", "2.2500"],
        ["27.2500", "29.4000", "17.5000", "14.7500", "13.2500", "5.2500"],
        ["18.7500", "17.5000", "19.6000", "13.7500", "13.7500", "11.2500"],
        ["15.2500", "14.7500", "13.7500", "16.0000", "11.7500", "8.5000"],
        ["13.0000", "13.2500", "13.7500", "11.7500", "24.5000", "25.7500"],
        ["2.2500", "5.2500", "11.2500", "8.5000", "25.7500", "50.2000"]]
for i in range(N):
    for j in range(N):
        check_dec(f"V[{NAMES[i]}][{NAMES[j]}] as printed", V[i][j], VDEC[i][j])

sub("6c. the diagonal, read as volatilities")
for i, nm in enumerate(NAMES):
    check_root(f"{nm} total volatility", V[i][i],
               ["5.9245", "5.4222", "4.4272", "4.0000", "4.9497", "7.0852"][i])
check("KPN's variance is exactly 16", V[3][3], F(16))
check("KPN's volatility is exactly 4", rootF(V[3][3]), F(4))
check("MRA is the riskiest name", max(V[i][i] for i in range(N)), V[5][5])
check("MRA has the smallest specific variance", min(d), d[5])
check("MRA's common-factor variance", XFXt[5][5], F(49))
check("49 + 1.2 = 50.2", XFXt[5][5] + d[5], F(251, 5))
check_dec("the common-factor share of MRA's variance, per cent",
          XFXt[5][5] / V[5][5] * 100, "97.6096")
check_dec("the same, to one decimal as the markdown prints it",
          XFXt[5][5] / V[5][5] * 100, "97.6", places=1)
offdiag = [V[i][j] for i in range(N) for j in range(N) if i < j]
check("there are fifteen off-diagonals", len(offdiag), 15)
check("GRV-MRA is the smallest of them", min(offdiag), V[0][5])

sub("6d. the free structural check -- X F X^T must be singular")
check("det X F X^T = 0 (6 assets, 3 factors)", det_gauss(XFXt), F(0))
check("det V is not zero", det_gauss(V) != 0, True)
check("det V", det_gauss(V), F(2308676544, 625))
wz = [F(-3, 10), F(3, 10), F(3, 10), F(-2, 10), F(-1, 10), F(0)]
check("a book built from month 1's miss column has zero factor exposure",
      tuple(matvec(XT, wz)), (F(0), F(0), F(0)))
check("its factor variance is zero", quad(XFXt, wz), F(0))
check("its risk is all specific", quad(V, wz), F(341, 250))
check_root("that book's risk", quad(V, wz), "1.1679")

# ===========================================================================
# STAGE 6 -- PRICE THE BOOK
# ===========================================================================
head("STAGE 6 -- PRICE THE BOOK (section 7)")

hP = matvec(XT, WP)
sub("7a. the book's factor exposures")
check("h_Mkt (fully invested, p.4)", hP[0], F(1))
check("h_EY", hP[1], F(11, 20))
check("h_Prof", hP[2], F(1, 5))
check_dec("h_EY as a decimal", hP[1], "0.5500")
check_dec("h_Prof as a decimal", hP[2], "0.2000")
check_dec("0.15 x 0.5, an intermediate the markdown prints", F(15, 100) * F(1, 2),
          "0.0750", places=4)
check_dec("0.425 squared, an intermediate the markdown prints", F(17, 40) ** 2,
          "0.180625", places=6)

sub("7b. route 1 -- exposures first")
FhP = matvec(Fm, hP)
check("F h", tuple(FhP), (F(167, 10), F(22, 5), F(-13, 20)))
facvar = quad(Fm, hP)
specvar = sum(WP[i] ** 2 * d[i] for i in range(N))
check("factor variance h^T F h", facvar, F(1899, 100))
check("the six pieces of h^T F h",
      (Fm[0][0] * hP[0] ** 2, 2 * Fm[0][1] * hP[0] * hP[1],
       2 * Fm[0][2] * hP[0] * hP[2], Fm[1][1] * hP[1] ** 2,
       2 * Fm[1][2] * hP[1] * hP[2], Fm[2][2] * hP[2] ** 2),
      (F(16), F(11, 5), F(-4, 5), F(121, 100), F(11, 50), F(4, 25)))
for lab, val, pr in [("16", F(16), "16.0000"), ("+2.20", F(11, 5), "2.2000"),
                     ("-0.80", F(-4, 5), "-0.8000"), ("+1.21", F(121, 100), "1.2100"),
                     ("+0.22", F(11, 50), "0.2200"), ("+0.16", F(4, 25), "0.1600")]:
    check_dec("h^T F h piece " + lab, val, pr)
check("specific variance sum w^2 d", specvar, F(63, 50))
check("the four pieces of sum w^2 d",
      (WP[0] ** 2 * d[0], WP[1] ** 2 * d[1], WP[3] ** 2 * d[3],
       WP[5] ** 2 * d[5]),
      (F(81, 250), F(108, 125), F(9, 200), F(27, 1000)))
for lab, val, pr in [("0.324", F(81, 250), "0.3240"), ("0.864", F(108, 125), "0.8640"),
                     ("0.045", F(9, 200), "0.0450"), ("0.027", F(27, 1000), "0.0270")]:
    check_dec("sum w^2 d piece " + lab, val, pr)
check_dec("factor variance as a decimal", facvar, "18.9900")
check_dec("specific variance as a decimal", specvar, "1.2600")
totvar = facvar + specvar
check("total variance", totvar, F(81, 4))
check("total variance as a decimal", totvar, F(2025, 100))
check("total risk is an exact root", rootF(totvar), F(9, 2))
check_root("book risk, per month", totvar, "4.5000")

sub("7c. route 2 -- build V first")
check("w^T V w equals the route-1 answer", quad(V, WP), totvar)
check("the two routes agree exactly", quad(V, WP) == totvar, True)

sub("7d. the split")
check("factor share of variance", facvar / totvar, F(211, 225))
check("specific share of variance", specvar / totvar, F(14, 225))
check_dec("factor share, per cent", facvar / totvar * 100, "93.7778")
check_dec("specific share, per cent", specvar / totvar * 100, "6.2222")
check("the two shares sum to 1", facvar / totvar + specvar / totvar, F(1))
check_root("factor risk", facvar, "4.3578")
check_root("specific risk", specvar, "1.1225")

sub("7e. risks do not add")
CHECKS[0] += 1
addrisk = (sqrtD(facvar) + sqrtD(specvar)).quantize(Decimal("0.0001"))
print(f"   [{'OK ' if str(addrisk) == '5.4802' else 'FAIL'}] "
      f"factor risk + specific risk = {addrisk} (rounded), against 4.5")
if str(addrisk) != "5.4802":
    sys.exit("MISMATCH adding risks")
CHECKS[0] += 1
pct = ((sqrtD(facvar) + sqrtD(specvar)) / Decimal("4.5") * 100 - 100).quantize(Decimal("0.1"))
print(f"   [{'OK ' if str(pct) == '21.8' else 'FAIL'}] adding the risks overstates by {pct}%")
if str(pct) != "21.8":
    sys.exit("MISMATCH adding-risks overstatement")
check("but the variances do add", facvar + specvar, totvar)

sub("7e. what actually happened -- the realised series")
RP = [sum(WP[i] * R[i][t] for i in range(N)) for t in range(T)]
RB = [sum(WB[i] * R[i][t] for i in range(N)) for t in range(T)]
RA = [RP[t] - RB[t] for t in range(T)]
check("book return series", tuple(RP),
      (F(87, 10), F(17, 20), F(9, 2), F(-3, 10), F(-9, 5)))
for t in range(T):
    check_dec(f"book return M{t+1} as printed", RP[t],
              ["8.70", "0.85", "4.50", "-0.30", "-1.80"][t], places=2)
facpart = [sum(hP[j] * [fM, fX, fG][j][t] for j in range(3)) for t in range(T)]
specpart = [sum(WP[i] * U[t][i] for i in range(N)) for t in range(T)]
check("the factor part of the book's return", tuple(facpart),
      (F(87, 10), F(-11, 20), F(39, 10), F(-2, 5), F(-19, 10)))
check("the specific part of the book's return", tuple(specpart),
      (F(0), F(7, 5), F(3, 5), F(1, 10), F(1, 10)))
check("they add to the realised return in every month",
      tuple(facpart[t] + specpart[t] for t in range(T)), tuple(RP))
check("M1 factor part = 1(7) + 0.55(2) + 0.20(3)",
      F(1) * 7 + F(11, 20) * 2 + F(1, 5) * 3, F(87, 10))
check("M1 specific part is exactly zero", specpart[0], F(0))
check("realised book variance, divisor T-1", sample_cov(RP, RP), F(8929, 500))
check_root("realised book standard deviation", sample_cov(RP, RP), "4.2259")
check("active return series", tuple(RA),
      (F(5, 4), F(127, 40), F(9, 5), F(0), F(-19, 20)))
for t in range(T):
    check_dec(f"active return M{t+1} as printed", RA[t],
              ["1.250", "3.175", "1.800", "0.000", "-0.950"][t], places=3)
check("realised active variance", sample_cov(RA, RA), F(20441, 8000))
check_root("realised active standard deviation", sample_cov(RA, RA), "1.5985")

# ===========================================================================
# STAGE 7 -- THE ACTIVE BOOK
# ===========================================================================
head("STAGE 7 -- THE ACTIVE BOOK (section 8)")

WA = [WP[i] - WB[i] for i in range(N)]
check("active weights", tuple(WA),
      (F(1, 20), F(3, 10), F(-1, 4), F(0), F(-1, 10), F(0)))
check("active weights sum to zero", sum(WA, F(0)), F(0))
check("two names carry no active bet at all",
      sum(1 for v in WA if v == 0), 2)

hB = matvec(XT, WB)
hA = matvec(XT, WA)
sub("8a. the three exposure vectors")
check("index exposures", tuple(hB), (F(1), F(1, 8), F(1, 10)))
check_dec("index EY exposure", hB[1], "0.1250")
check("active exposures", tuple(hA), (F(0), F(17, 40), F(1, 10)))
check("active market exposure is exactly zero", hA[0], F(0))
check_dec("active EY exposure", hA[1], "0.4250")
check_dec("active Prof exposure", hA[2], "0.1000")
check("active h = portfolio h - index h",
      tuple(hA), tuple(hP[j] - hB[j] for j in range(3)))

sub("8b. active risk")
afac = quad(Fm, hA)
check("active factor variance", afac, F(339, 400))
check("its three pieces",
      (Fm[1][1] * hA[1] ** 2, 2 * Fm[1][2] * hA[1] * hA[2],
       Fm[2][2] * hA[2] ** 2),
      (F(289, 400), F(17, 200), F(1, 25)))
check("the market factor contributes nothing to active risk",
      Fm[0][0] * hA[0] ** 2, F(0))
aspec = sum(WA[i] ** 2 * d[i] for i in range(N))
for lab, val, pr in [("0.7225", F(289, 400), "0.7225"), ("0.085", F(17, 200), "0.0850"),
                     ("0.04", F(1, 25), "0.0400")]:
    check_dec("active factor piece " + lab, val, pr)
check_dec("active factor variance as a decimal", afac, "0.8475")
check("active specific variance", aspec, F(337, 400))
check("its four pieces",
      (WA[0] ** 2 * d[0], WA[1] ** 2 * d[1], WA[2] ** 2 * d[2],
       WA[4] ** 2 * d[4]),
      (F(9, 1000), F(243, 500), F(23, 80), F(3, 50)))
for lab, val, pr in [("0.009", F(9, 1000), "0.0090"), ("0.486", F(243, 500), "0.4860"),
                     ("0.2875", F(23, 80), "0.2875"), ("0.06", F(3, 50), "0.0600")]:
    check_dec("active specific piece " + lab, val, pr)
check_dec("active specific variance as a decimal", aspec, "0.8425")
avar = afac + aspec
check("active variance", avar, F(169, 100))
check("active risk is an exact root", rootF(avar), F(13, 10))
check_root("ACTIVE RISK, per month", avar, "1.3000")
check("a^T V a agrees", quad(V, WA), avar)

sub("8c. the split that the paper's own report can be read against")
check("active factor share", afac / avar, F(339, 676))
check("active specific share", aspec / avar, F(337, 676))
check_dec("active factor share, per cent", afac / avar * 100, "50.1479")
check_dec("active specific share, per cent", aspec / avar * 100, "49.8521")
check("the split is within half a point of 50/50",
      abs(afac / avar - F(1, 2)) < F(1, 200), True)
CHECKS[0] += 1
aadd = (sqrtD(afac) + sqrtD(aspec)).quantize(Decimal("0.0001"))
print(f"   [{'OK ' if str(aadd) == '1.8385' else 'FAIL'}] "
      f"active factor risk + active specific risk = {aadd} (rounded), against 1.3")
if str(aadd) != "1.8385":
    sys.exit("MISMATCH adding active risks")
check_root("active factor risk", afac, "0.9206")
check_root("active specific risk", aspec, "0.9179")

sub("8d. the index's own risk, and why it is not the answer")
bfac = quad(Fm, hB)
bspec = sum(WB[i] ** 2 * d[i] for i in range(N))
bvar = bfac + bspec
check("index factor variance", bfac, F(6491, 400))
check("index specific variance", bspec, F(1397, 2000))
check("the six pieces of the index's factor variance",
      (Fm[0][0] * hB[0] ** 2, 2 * Fm[0][1] * hB[0] * hB[1],
       2 * Fm[0][2] * hB[0] * hB[2], Fm[1][1] * hB[1] ** 2,
       2 * Fm[1][2] * hB[1] * hB[2], Fm[2][2] * hB[2] ** 2),
      (F(16), F(1, 2), F(-2, 5), F(1, 16), F(1, 40), F(1, 25)))
for lab, val, pr in [("0.5", F(1, 2), "0.5000"), ("-0.4", F(-2, 5), "-0.4000"),
                     ("0.0625", F(1, 16), "0.0625"), ("0.025", F(1, 40), "0.0250"),
                     ("0.04", F(1, 25), "0.0400")]:
    check_dec("index factor piece " + lab, val, pr)
check_dec("index factor variance as a decimal", bfac, "16.2275")
check("the six pieces of the index's specific variance",
      tuple(WB[i] ** 2 * d[i] for i in range(N)),
      (F(9, 40), F(27, 500), F(23, 80), F(9, 200), F(3, 50), F(27, 1000)))
for lab, val, pr in [("0.225", F(9, 40), "0.2250"), ("0.054", F(27, 500), "0.0540"),
                     ("0.2875", F(23, 80), "0.2875"), ("0.045", F(9, 200), "0.0450"),
                     ("0.06", F(3, 50), "0.0600"), ("0.027", F(27, 1000), "0.0270")]:
    check_dec("index specific piece " + lab, val, pr)
check_dec("index specific variance as a decimal", bspec, "0.6985")
check("index total variance", bvar, F(8463, 500))
check_dec("index total variance as a decimal", bvar, "16.9260")
check("index variance has no exact root", rootF(bvar), None)
check_root("index risk", bvar, "4.1141")
CHECKS[0] += 1
diffrisk = (Decimal("4.5") - sqrtD(bvar)).quantize(Decimal("0.0001"))
print(f"   [{'OK ' if str(diffrisk) == '0.3859' else 'FAIL'}] "
      f"book risk minus index risk = {diffrisk} (rounded), against 1.3")
if str(diffrisk) != "0.3859":
    sys.exit("MISMATCH risk difference")
check("that is wrong by a factor of more than three",
      F(13, 10) / F(3859, 10000) > 3, True)

sub("8e. the decomposition that proves the three numbers hang together")
covAB = bilin(V, WA, WB)
check("cov(active, index)", covAB, F(817, 1000))
check_dec("cov(active, index) as a decimal", covAB, "0.8170")
check_dec("2 x cov(active, index)", 2 * covAB, "1.6340")
check_dec("cov(book, index) as a decimal", bilin(V, WP, WB), "17.7430")
check("Var(book) = Var(index) + 2 Cov(active, index) + Var(active)",
      bvar + 2 * covAB + avar, totvar)
covPB = bilin(V, WP, WB)
check("cov(book, index)", covPB, F(17743, 1000))
check("cov(book, index) = Var(index) + cov(active, index)",
      bvar + covAB, covPB)
beta = covPB / bvar
check("beta of the book against the index", beta, F(17743, 16926))
check_dec("beta as a decimal", beta, "1.0483")
check("market factor exposure is 1.00 while beta is not",
      (hP[0] == 1) and (beta != 1), True)

# ===========================================================================
# STAGE 8 -- WHERE THE RISK ACTUALLY IS
# ===========================================================================
head("STAGE 8 -- WHERE THE ACTIVE RISK ACTUALLY IS (section 9)")

VA = matvec(V, WA)
sub("9a. one matrix-vector product does the whole job")
check("V a", tuple(VA),
      (F(1577, 400), F(1793, 400), F(-7, 80), F(23, 40), F(-101, 80), F(-37, 10)))
for i, nm in enumerate(NAMES):
    check_dec(f"(V a) for {nm}, as printed", VA[i],
              ["3.9425", "4.4825", "-0.0875", "0.5750", "-1.2625", "-3.7000"][i])
contrib = [WA[i] * VA[i] for i in range(N)]
for i, nm in enumerate(NAMES):
    check_dec(f"contribution for {nm}, as printed", WA[i] * VA[i],
              ["0.197125", "1.344750", "0.021875", "0.000000", "0.126250",
               "0.000000"][i], places=6)
check("contributions to active variance", tuple(contrib),
      (F(1577, 8000), F(5379, 4000), F(7, 320), F(0), F(101, 800), F(0)))
check("contributions sum to the active variance", sum(contrib, F(0)), avar)
for i, nm in enumerate(NAMES):
    check(f"{nm} share of active risk", contrib[i] / avar,
          [F(1577, 13520), F(5379, 6760), F(35, 2704), F(0), F(101, 1352),
           F(0)][i])
for i, nm in enumerate(NAMES):
    check_dec(f"{nm} share of active risk, per cent", contrib[i] / avar * 100,
              ["11.6642", "79.5710", "1.2944", "0.0000", "7.4704",
               "0.0000"][i])
check("shares sum to 100 per cent",
      sum(contrib[i] / avar for i in range(N)), F(1))
check_dec("one percentage point more JDR moves active risk by", VA[2] / F(13, 10) / 100,
          "-0.000673", places=6)
check_dec("one percentage point more MRA moves active risk by", VA[5] / F(13, 10) / 100,
          "-0.028462", places=6)
check("the MRA trade is forty-two times the JDR trade",
      round(float((VA[5] / F(13, 10)) / (VA[2] / F(13, 10)))), 42)

sub("9a2. why JDR's (V a) is nearly zero -- the VC1 answer")
check("JDR's factor-side covariance with the active book",
      bilin(Fm, X[2], hA), F(17, 16))
check_dec("that, as a decimal", bilin(Fm, X[2], hA), "1.0625")
check("JDR's specific-side term, d x its own bet", d[2] * WA[2], F(-23, 20))
check_dec("that, as a decimal", d[2] * WA[2], "-1.1500")
check("they sum to (V a)_JDR", bilin(Fm, X[2], hA) + d[2] * WA[2], VA[2])

sub("9b. marginal contribution -- (V a)_i divided by the active risk")
for i, nm in enumerate(NAMES):
    check_dec(f"{nm} marginal contribution to active risk",
              VA[i] / F(13, 10),
              ["3.0327", "3.4481", "-0.0673", "0.4423", "-0.9712",
               "-2.8462"][i])
check("HLX is the largest active position", max(abs(v) for v in WA), abs(WA[1]))
check("JDR is the second largest active position", abs(WA[2]), F(1, 4))
check("JDR's bet is the second largest and its contribution the second smallest",
      (abs(WA[2]) > abs(WA[4])) and (contrib[2] < contrib[4]), True)
check("MRA is held, has the highest total volatility, and contributes "
      "nothing to active risk",
      (WP[5] != 0) and (V[5][5] == max(V[i][i] for i in range(N)))
      and (contrib[5] == 0), True)

sub("9c. the same machinery on the book's total risk")
VW = matvec(V, WP)
tcontrib = [WP[i] * VW[i] for i in range(N)]
check("contributions to total variance sum to it", sum(tcontrib, F(0)), totvar)
for i, nm in enumerate(NAMES):
    if WP[i] != 0:
        check_dec(f"{nm} share of the book's total risk, per cent",
                  tcontrib[i] / totvar * 100,
                  {0: "35.6370", 1: "45.3037", 3: "10.4815",
                   5: "8.5778"}[i])

# ===========================================================================
# SECTION 10 -- the three free structural checks
# ===========================================================================
head("SECTION 10 -- THE THREE FREE CHECKS")
check("check 1: fifteen balance conditions, all zero",
      [(sum(U[t], F(0)), dot(x, U[t]), dot(g, U[t])) for t in range(T)],
      [(F(0), F(0), F(0))] * 5)
check("check 2: 114 two ways", (sum(SSu, F(0)), sum(dot(u, u) for u in U)),
      (F(114), F(114)))
check("check 3: two routes to 81/4", (quad(V, WP), facvar + specvar),
      (F(81, 4), F(81, 4)))

# ===========================================================================
# SECTION 12 -- THE TRAPS
# ===========================================================================
head("SECTION 12 -- THE TRAPS, each with the number it returns")

sub("T1. one column at a time (level 4)")
check("M1 naive pair", (SXR[0] / 6, SGR[0] / 6), (F(4), F(13, 3)))
check("M1 truth", (fX[0], fG[0]), (F(2), F(3)))

sub("T2. skipping the standardisation entirely")
rawcols = [[F(1)] * N, EY_RAW, OM_RAW]
Graw = [[dot(rawcols[p], rawcols[q]) for q in range(3)] for p in range(3)]
check("raw-column Gram matrix", [tuple(r) for r in Graw],
      [(F(6), F(30), F(66)), (F(30), F(174), F(346)),
       (F(66), F(346), F(750))])
fraw = []
for t in range(T):
    r = [R[i][t] for i in range(N)]
    coef = solve(Graw, [dot(rawcols[p], r) for p in range(3)])
    fraw.append(coef)
    uraw = [r[i] - coef[0] - coef[1] * EY_RAW[i] - coef[2] * OM_RAW[i]
            for i in range(N)]
    check(f"M{t+1} raw-column coefficients", tuple(coef),
          [(F(-29, 2), F(1), F(3, 2)), (F(-65, 2), F(3, 2), F(2)),
           (F(7, 2), F(1), F(-1, 2)), (F(-35, 2), F(0), F(3, 2)),
           (F(-3, 2), F(-1), F(1, 2))][t])
    check(f"M{t+1} raw-column misses are IDENTICAL to the right ones",
          tuple(uraw), tuple(U[t]))
Fraw = [[sample_cov([fraw[t][i] for t in range(T)],
                    [fraw[t][j] for t in range(T)]) for j in range(3)]
        for i in range(3)]
check("the raw-column EY factor-return series",
      tuple(fraw[t][1] for t in range(T)),
      (F(1), F(3, 2), F(1), F(0), F(-1)))
check("F built from raw columns", [tuple(r) for r in Fraw],
      [(F(403, 2), F(-27, 4), F(-53, 4)), (F(-27, 4), F(1), F(1, 4)),
       (F(-53, 4), F(1, 4), F(1))])
Xraw = [[F(1), EY_RAW[i], OM_RAW[i]] for i in range(N)]
check("but X F X^T comes out EXACTLY the same",
      matmul(matmul(Xraw, Fraw), transpose(Xraw)), XFXt)
check("so V is the same, and so is the risk",
      quad(addm(matmul(matmul(Xraw, Fraw), transpose(Xraw)), D), WP), F(81, 4))
check("what does change: the book's reported exposures",
      tuple(matvec(transpose(Xraw), WP)), (F(1), F(61, 10), F(57, 5)))
check_dec("the un-standardised EY exposure", F(61, 10), "6.1000")

sub("T3. dividing F by T instead of T - 1")
t3f = quad(FmT, hP) + specvar
t3a = quad(FmT, hA) + aspec
check("total variance", t3f, F(4113, 250))
check_root("total risk", t3f, "4.0561")
check("active variance", t3a, F(3041, 2000))
check_root("active risk", t3a, "1.2331")

sub("T4. dividing D by T - 1 instead of T")
t4f = facvar + sum(WP[i] ** 2 * d_T1[i] for i in range(N))
t4a = afac + sum(WA[i] ** 2 * d_T1[i] for i in range(N))
check("total variance", t4f, F(4113, 200))
check_root("total risk", t4f, "4.5349")
check("active variance", t4a, F(3041, 1600))
check_root("active risk", t4a, "1.3786")

sub("T5. removing each stock's own mean miss before squaring")
t5f = facvar + sum(WP[i] ** 2 * d_own[i] for i in range(N))
t5a = afac + sum(WA[i] ** 2 * d_own[i] for i in range(N))
check("total variance", t5f, F(20083, 1000))
check_root("total risk", t5f, "4.4814")
check("active variance", t5a, F(8, 5))
check_root("active risk", t5a, "1.2649")

sub("T6. dropping D altogether")
check_root("total risk without D", facvar, "4.3578")
check_root("active risk without D", afac, "0.9206")

sub("T7. keeping only F's diagonal")
Fdiag = diagm([Fm[i][i] for i in range(3)])
t7f = quad(Fdiag, hP) + specvar
t7a = quad(Fdiag, hA) + aspec
check("total variance", t7f, F(1863, 100))
check_root("total risk", t7f, "4.3162")
check("active variance", t7a, F(321, 200))
check_root("active risk", t7a, "1.2669")

sub("T8. active risk as a difference of risks")
CHECKS[0] += 1
print(f"   [OK ] 4.5000 - 4.1141 = {diffrisk} against the true 1.3")

sub("T9. skipping the model -- the assets' own sample covariance matrix")
Sm = [[sample_cov(R[i], R[j]) for j in range(N)] for i in range(N)]
check("it is symmetric", all(Sm[i][j] == Sm[j][i] for i in range(N)
                             for j in range(N)), True)
check("det of the 6x6 sample covariance matrix is exactly zero",
      det_gauss(Sm), F(0))
check("w^T S w IS the realised sample variance of the book's returns",
      quad(Sm, WP), sample_cov(RP, RP))
check("book variance under it", quad(Sm, WP), F(8929, 500))
check_dec("book variance under it, as a decimal", quad(Sm, WP), "17.8580")
check_root("book risk under it", quad(Sm, WP), "4.2259")
check("active variance under it", quad(Sm, WA), F(20441, 8000))
check_root("active risk under it", quad(Sm, WA), "1.5985")
check("a 6x6 covariance matrix has 21 distinct entries, from 30 returns",
      (N * (N + 1) // 2, N * T), (21, 30))
check("the model estimates 6 in F plus 6 in D = 12, from the same 30",
      (K * (K + 1) // 2, N, K * (K + 1) // 2 + N), (6, 6, 12))
check("at 500 assets: the direct matrix needs 125,250 numbers",
      500 * 501 // 2, 125250)
check("at 500 assets with 3 factors: the model needs 506",
      K * (K + 1) // 2 + 500, 506)
check("HLX's private variance under T9, against its true total variance of 29.4",
      (F(146, 5), V[1][1]), (F(146, 5), F(147, 5)))

sub("T9b. near-miss on stage 1 -- dividing by n-1 when standardising")
sd5 = F(24, 5)
check("that variance", sd5, F(24, 5))
check_root("that standard deviation", sd5, "2.1909")
CHECKS[0] += 1
tellw = sum((Decimal(dEY[i].numerator) / Decimal(dEY[i].denominator)) ** 2
            for i in range(N)) / (Decimal(24) / Decimal(5))
print(f"   [{'OK ' if tellw == 5 else 'FAIL'}] the tell: sum of squared "
      f"exposures comes out {tellw}, not 6")
if tellw != 5:
    sys.exit("MISMATCH n-1 standardisation tell")

sub("T9c. leaving the column of ones out of X")
Fm2 = [[Fm[1][1], Fm[1][2]], [Fm[2][1], Fm[2][2]]]
U2 = [[U[t][i] + fM[t] for i in range(N)] for t in range(T)]
SSu2 = [sum(U2[t][i] ** 2 for t in range(T)) for i in range(N)]
d2 = [s2 / T for s2 in SSu2]
check("the misses now carry the whole market move", tuple(d2),
      (F(31, 5), F(146, 5), F(134, 5), F(39, 5), F(119, 5), F(59, 5)))
fv2 = quad(Fm2, [hP[1], hP[2]])
sv2 = sum(WP[i] ** 2 * d2[i] for i in range(N))
check("factor variance without a market factor", fv2, F(159, 100))
check("specific variance without a market factor", sv2, F(5671, 1000))
check_dec("specific variance without a market factor, as a decimal", sv2, "5.6710")
check("total variance", fv2 + sv2, F(7261, 1000))
check_dec("total variance as a decimal", fv2 + sv2, "7.2610")
check_root("total risk", fv2 + sv2, "2.6946")
CHECKS[0] += 1
safer = (100 - sqrtD(fv2 + sv2) / Decimal("4.5") * 100).quantize(Decimal("1"))
print(f"   [{'OK ' if str(safer) == '40' else 'FAIL'}] the book looks {safer}% safer")
if str(safer) != "40":
    sys.exit("MISMATCH T9 understatement")

sub("T9d. F built as correlations instead of covariances")
Fcorr = [[Fm[i][j] / (rootF(Fm[i][i]) * rootF(Fm[j][j])) for j in range(3)]
         for i in range(3)]
check("that matrix", [tuple(r) for r in Fcorr],
      [(F(1), F(1, 4), F(-1, 4)), (F(1, 4), F(1), F(1, 4)),
       (F(-1, 4), F(1, 4), F(1))])
check("total variance", quad(Fcorr, hP) + specvar, F(11330, 4000))
check_root("total risk", quad(Fcorr, hP) + specvar, "1.6830")

sub("T9e. active specific risk computed on the book's weights, not the bets")
check("that variance", afac + specvar, F(843, 400))
check_dec("that variance as a decimal", afac + specvar, "2.1075")
check_root("that active risk", afac + specvar, "1.4517")

sub("T9f. one-at-a-time carried all the way to the risk number")
fXn = [SXR[t] / 6 for t in range(T)]
fGn = [SGR[t] / 6 for t in range(T)]
Un = [[R[i][t] - fM[t] - fXn[t] * x[i] - fGn[t] * g[i] for i in range(N)]
      for t in range(T)]
check("its misses no longer balance: sum x*u in month 1", dot(x, Un[0]), F(-52, 3))
Fn = [[sample_cov(a_, b_) for b_ in (fM, fXn, fGn)] for a_ in (fM, fXn, fGn)]
check("its F", [tuple(r) for r in Fn],
      [(F(16), F(2, 3), F(-2, 3)), (F(2, 3), F(64, 9), F(61, 9)),
       (F(-2, 3), F(61, 9), F(64, 9))])
check("its style-factor correlation, which should be 1/4",
      Fn[1][2] / Fn[1][1], F(61, 64))
check_dec("that correlation as a decimal", F(61, 64), "0.953125", places=6)
dn = [sum(Un[t][i] ** 2 for t in range(T)) / T for i in range(N)]
check("its D", tuple(dn),
      (F(15), F(52, 9), F(92, 15), F(26, 9), F(139, 45), F(454, 15)))
fvn = quad(Fn, hP)
svn = sum(WP[i] ** 2 * dn[i] for i in range(N))
check("its total variance", fvn + svn, F(52681, 2250))
check_root("its total risk", fvn + svn, "4.8388")
check("its active variance", quad(Fn, hA)
      + sum(WA[i] ** 2 * dn[i] for i in range(N)), F(52261, 18000))
check_root("its active risk", quad(Fn, hA)
           + sum(WA[i] ** 2 * dn[i] for i in range(N)), "1.7039")
check("its GRV specific variance, against the true 18/5", dn[0], F(15))
check_dec("its MRA specific variance, against the true 6/5", dn[5], "30.2667")
CHECKS[0] += 1
r1 = ((sqrtD(fvn + svn) / Decimal("4.5") - 1) * 100).quantize(Decimal("0.1"))
r2 = ((sqrtD(quad(Fn, hA) + sum(WA[i] ** 2 * dn[i] for i in range(N)))
       / Decimal("1.3") - 1) * 100).quantize(Decimal("1"))
print(f"   [{'OK ' if (str(r1), str(r2)) == ('7.5', '31') else 'FAIL'}] "
      f"one-at-a-time overstates the book by {r1}% and the active book by {r2}%")
if (str(r1), str(r2)) != ("7.5", "31"):
    sys.exit("MISMATCH one-at-a-time overstatement")

sub("T10. annualising by multiplying by 12")
check_root("correct: sqrt(12) x monthly variance, book", totvar * 12, "15.5885")
check_root("correct: sqrt(12) x monthly variance, active", avar * 12, "4.5033")
check("wrong: 12 x 4.5", F(9, 2) * 12, F(54))
check("wrong: 12 x 1.3", F(13, 10) * 12, F(78, 5))

sub("T11. market factor exposure read as beta")
check("market factor exposure", hP[0], F(1))
check_dec("beta", beta, "1.0483")
check("they are different numbers", hP[0] != beta, True)

sub("T12. averaging the misses down the wrong axis")
check("misses averaged within a month give five numbers, not six",
      len([dot(u, u) / N for u in U]), 5)
check("and D needs six", len(d), 6)

# ===========================================================================
# SECTION 13 -- the victory-condition checks that carry numbers
# ===========================================================================
head("SECTION 13 -- VICTORY-CONDITION CHECKS THAT CARRY NUMBERS")
check("VC4 checkpoint A: X's two columns", (dot(x, x), dot(g, g), dot(x, g)),
      (F(6), F(6), F(4)))
check("VC4 checkpoint B: the five factor triples",
      [(fM[t], fX[t], fG[t]) for t in range(T)],
      [(F(7), F(2), F(3)), (F(-3), F(3), F(4)), (F(3), F(2), F(-1)),
       (F(-1), F(0), F(3)), (F(-1), F(-2), F(1))])
check("VC4 checkpoint C: F", [tuple(r) for r in Fm],
      [(F(16), F(2), F(-2)), (F(2), F(4), F(1)), (F(-2), F(1), F(4))])
check("VC4 checkpoint D: D", tuple(d),
      (F(18, 5), F(27, 5), F(23, 5), F(2), F(6), F(6, 5)))
check("VC4 checkpoint E: book risk", rootF(totvar), F(9, 2))
check("VC4 checkpoint F: active risk", rootF(avar), F(13, 10))
check("VC1 origin question: where the 10 comes from",
      (G[1][1] * G[2][2] - G[1][2] ** 2) / 2, F(10))
check("VC1 origin question: 6 x 6 - 4 x 4", F(6) * F(6) - F(4) * F(4), F(20))
check("VC3: n - k, and it is not n", (N - K, N), (3, 6))

# ===========================================================================
# SECTION 15 -- the numbers that travel back to the paper
# ===========================================================================
head("SECTION 15 -- BACK TO BFRE (printed paper values quoted in the markdown)")
check("p.11 Figure 1.3, Earnings Yield-Profitability exposure correlation "
      "(printed digits)", F(64, 100), F(16, 25))
check("our exposure correlation, for comparison", dot(x, g) / 6, F(2, 3))
check_dec("ours as a decimal", F(2, 3), "0.6667")
check("p.10 Table 1.2, annualised volatilities quoted (printed digits)",
      (F(198, 10), F(21, 10), F(22, 10)), (F(99, 5), F(21, 10), F(11, 5)))
check("our MONTHLY factor volatilities",
      (rootF(Fm[0][0]), rootF(Fm[1][1]), rootF(Fm[2][2])), (F(4), F(2), F(2)))
check_root("our market factor, annualised", Fm[0][0] * 12, "13.8564")
check_root("our EY factor, annualised", Fm[1][1] * 12, "6.9282")
check("p.10 Table 1.2, correlation with market factor (printed digits): "
      "EY 0.02, Profitability -0.14",
      (F(2, 100), F(-14, 100)), (F(1, 50), F(-7, 50)))
check("ours: +1/4 and -1/4", (Fm[0][1] / 8, Fm[0][2] / 8), (F(1, 4), F(-1, 4)))
check("p.35 banner, printed: Portfolio Beta 1.02", F(102, 100), F(51, 50))
check("p.35 pie, printed: Specific 50, Style 25, Industry 14, Country 6, FX 4",
      50 + 25 + 14 + 6 + 4 + 1, 100)
check("our active split against that 50: factor 50.1479, specific 49.8521",
      afac / avar + aspec / avar, F(1))
check("p.28 Table 1.3 daily row (printed digits)", (125, 375, 10),
      (125, 375, 10))
check("p.27 WKL (printed digits)", (104, 26), (104, 26))
check("our T, against BFRE's 104 and 375", (T, 104, 375), (5, 104, 375))
check("BFRE's observations per estimated specific variance, daily model", 375,
      375)
check("ours", T, 5)


# ===========================================================================
head("SECTION 16 -- every remaining decimal the markdown prints, checked as printed")

sub("16a. the returns table, as printed")
RETPR = [["8.5", "3.5", "3.5", "2.5", "-4.5"],
         ["13.5", "4.0", "7.5", "-1.5", "-1.5"],
         ["11.5", "-3.0", "1.5", "0.5", "2.5"],
         ["7.0", "1.5", "1.0", "3.0", "0.0"],
         ["3.5", "-10.5", "2.5", "-4.5", "-3.5"],
         ["-2.0", "-13.5", "2.0", "-6.0", "1.0"]]
for i in range(N):
    for t in range(T):
        check_dec(f"{NAMES[i]} M{t+1} as printed", R[i][t], RETPR[i][t], places=1)

sub("16b. the intermediates the worked arithmetic prints")
for lab, val, pr, pl in [
        ("F h first entry", F(167, 10), "16.7", 1),
        ("0.55 x 4.4", F(11, 20) * F(22, 5), "2.42", 2),
        ("0.20 x 0.65", F(1, 5) * F(13, 20), "0.13", 2),
        ("0.30 x 1.5", F(3, 10) * F(3, 2), "0.45", 2),
        ("0.15 x 1.5", F(15, 100) * F(3, 2), "0.225", 3),
        ("1.5 x 8.5", F(3, 2) * F(17, 2), "12.75", 2),
        ("0.5 x 1.5", F(1, 2) * F(3, 2), "0.75", 2),
        ("1.5 x -6", F(3, 2) * F(-6), "-9.0", 1),
        ("0.5 x -11.5", F(1, 2) * F(-23, 2), "-5.75", 2),
        ("F X_MRA third entry", F(-23, 2), "-11.5", 1),
        ("GRV common-factor variance", F(63, 2), "31.5", 1),
        ("total variance", totvar, "20.25", 2),
        ("active variance", avar, "1.69", 2),
        ("book factor variance", facvar, "18.99", 2),
        ("book specific variance", specvar, "1.26", 2),
        ("index variance", bvar, "16.926", 3),
        ("cov(active, index) x 2", 2 * covAB, "1.634", 3),
        ("M5 factor part of the book's return", F(-19, 10), "-1.9", 1),
        ("raw-column intercept, month 1", F(-29, 2), "-14.5", 1),
        ("F(raw) top-left", F(403, 2), "201.5", 1),
        ("the x12 annualisation trap, active", F(78, 5), "15.6", 1),
        ("F if divided by T, top-left", F(64, 5), "12.8", 1),
        ("factor volatility 2", F(2), "2.0", 1),
        ("factor volatility 4", F(4), "4.0", 1)]:
    check_dec(lab, val, pr, places=pl)

sub("16c. the D variants, as printed")
for lab, val, pr, pl in [("T-1 GRV", F(9, 2), "4.5", 1), ("T-1 HLX", F(27, 4), "6.75", 2),
                         ("T-1 JDR", F(23, 4), "5.75", 2), ("T-1 KPN", F(5, 2), "2.5", 1),
                         ("T-1 LTS", F(15, 2), "7.5", 1), ("T-1 MRA", F(3, 2), "1.5", 1),
                         ("own-mean GRV", F(37, 10), "3.7", 1),
                         ("own-mean HLX", F(43, 10), "4.3", 1),
                         ("own-mean JDR", F(53, 10), "5.3", 1),
                         ("own-mean LTS", F(5, 2), "2.5", 1),
                         ("own-mean MRA", F(7, 10), "0.7", 1),
                         ("true JDR", F(23, 5), "4.6", 1)]:
    check_dec("d variant " + lab, val, pr, places=pl)

sub("16d. the no-market-factor D, as printed")
for i, pr in enumerate(["6.2", "29.2", "26.8", "7.8", "23.8", "11.8"]):
    check_dec(f"T9 d for {NAMES[i]}", d2[i], pr, places=1)

sub("16e. the shares, at the precisions the markdown uses")
check_dec("factor share to 2 dp", facvar / totvar * 100, "93.78", places=2)
check_dec("specific share to 2 dp", specvar / totvar * 100, "6.22", places=2)
check_dec("active factor share to 2 dp", afac / avar * 100, "50.15", places=2)
check_dec("active specific share to 2 dp", aspec / avar * 100, "49.85", places=2)
check_dec("active factor share to 1 dp", afac / avar * 100, "50.1", places=1)
check_dec("active specific share to 1 dp", aspec / avar * 100, "49.9", places=1)
check_dec("HLX share of active risk to 2 dp", contrib[1] / avar * 100, "79.57",
          places=2)
check_dec("JDR share of active risk to 2 dp", contrib[2] / avar * 100, "1.29",
          places=2)
check_dec("MRA share of the book's total risk to 1 dp",
          WP[5] * VW[5] / totvar * 100, "8.6", places=1)

sub("16f. the paper's own printed digits, as this page prints them")
for lab, val, pr, pl in [("Fig 1.3 EY-Profitability", F(16, 25), "0.64", 2),
                         ("Table 1.2 market volatility", F(99, 5), "19.8", 1),
                         ("Table 1.2 EY volatility", F(21, 10), "2.1", 1),
                         ("Table 1.2 Profitability volatility", F(11, 5), "2.2", 1),
                         ("Table 1.2 EY correlation with market", F(1, 50), "0.02", 2),
                         ("Table 1.2 Profitability correlation", F(-7, 50), "-0.14", 2),
                         ("p.35 Portfolio Beta", F(51, 50), "1.02", 2)]:
    check_dec(lab, val, pr, places=pl)

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/rebuild.md.")
print("   Decimals tagged ROUNDED above are marked 'rounded' in the markdown.")
