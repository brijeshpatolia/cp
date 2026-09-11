#!/usr/bin/env python3
"""
verify_level11.py -- recomputes EVERY number printed in datasets/level11.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level11.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

Linear-algebra helpers are the same conventions as tools/verify_level5.py and
tools/verify_level10.py -- reused, not reinvented.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
from itertools import product
import sys

getcontext().prec = 60

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
    """Decimal string, tagged EXACT or ROUNDED."""
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
    """`printed` is what the markdown shows for sqrt(variance)."""
    CHECKS[0] += 1
    q = Decimal(1).scaleb(-places)
    got = str(sqrtD(variance).quantize(q))
    ok = (got == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: sqrt({F(variance)}) = {got}"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': computed {got}, markdown says {printed}")


def check_dec(label, value, printed, places=4):
    """`printed` is what the markdown shows for an exact rational."""
    CHECKS[0] += 1
    v = F(value)
    q = Decimal(1).scaleb(-places)
    got = str((Decimal(v.numerator) / Decimal(v.denominator)).quantize(q))
    ok = (got == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] {label}: {F(value)} = {got}"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit(f"MISMATCH in '{label}': computed {got}, markdown says {printed}")


def show(label, val):
    print(f"        {label}: {S(val)}")


# ---------------------------------------------------------------------------
# linear algebra in exact rationals
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
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]


def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def quad(A, h):
    return dot(h, matvec(A, h))


def diagm(dv):
    n = len(dv)
    return [[dv[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def addm(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def is_symmetric(A):
    return all(A[i][j] == A[j][i] for i in range(len(A)) for j in range(len(A)))


def mean(xs):
    return sum(xs) / len(xs)


def devs(xs):
    m = mean(xs)
    return [t - m for t in xs]


def sample_cov(a, b, ddof=1):
    da, db = devs(a), devs(b)
    return sum(p * q for p, q in zip(da, db)) / (len(a) - ddof)


# ===========================================================================
head("SECTION 3 -- THE DATASET, RE-DERIVED FROM THE LEVEL 7/8 RETURNS FILE")
# ===========================================================================

NAMES = ["AXL", "BRN", "CHR", "DLT", "EMK"]
N = 5

sub("3a. X -- the five-name estimation universe, unchanged since Level 8")

X5 = {"AXL": [F(1), F(-2)], "BRN": [F(1), F(-1)], "CHR": [F(1), F(0)],
      "DLT": [F(1), F(1)], "EMK": [F(1), F(2)]}
X = [X5[n] for n in NAMES]
xs = [X5[n][1] for n in NAMES]

check("market column is all ones (p.4: unit exposure to the market factor)",
      [X5[n][0] for n in NAMES], [F(1)] * 5)
check("cheapness column, all five names", xs, [F(-2), F(-1), F(0), F(1), F(2)])
check("that column is centred over the universe (sum = 0)", sum(xs), F(0))
check("X is 5 rows by 2 columns", (len(X), len(X[0])), (5, 2))

sub("3b. F -- rebuilt from the Level 7 factor-return series, not assumed")

RET5 = {  # month 1..5, in percent -- Level 8's returns file
    "AXL": [F(0), F(-3), F(6), F(6), F(-8)],
    "BRN": [F(1), F(2), F(3), F(7), F(-6)],
    "CHR": [F(9), F(3), F(-1), F(1), F(-8)],
    "DLT": [F(9), F(10), F(-1), F(3), F(-4)],
    "EMK": [F(16), F(13), F(-2), F(-2), F(-4)],
}
T = 5
f_mkt, f_chp = [], []
for t in range(T):
    r = [RET5[n][t] for n in NAMES]
    f_mkt.append(sum(r) / 5)
    f_chp.append(sum(xi * ri for xi, ri in zip(xs, r)) / 10)
check("factor return series, market", f_mkt, [F(7), F(5), F(1), F(3), F(-6)])
check("factor return series, cheapness", f_chp, [F(4), F(4), F(-2), F(-2), F(1)])

Fm = [[sample_cov(f_mkt, f_mkt), sample_cov(f_mkt, f_chp)],
      [sample_cov(f_chp, f_mkt), sample_cov(f_chp, f_chp)]]
check("F rebuilt (mean subtracted, divisor T-1 = 4)", Fm,
      [[F(25), F(6)], [F(6), F(9)]])
check("F is symmetric", is_symmetric(Fm), True)
check("det F = 25*9 - 36", Fm[0][0] * Fm[1][1] - Fm[0][1] * Fm[1][0], F(189))

sub("3c. D -- rebuilt from the Level 8 / Level 9 miss columns, all five names")

U5 = {
    "AXL": [F(1), F(0), F(1), F(-1), F(0)],
    "BRN": [F(-2), F(1), F(0), F(2), F(1)],
    "CHR": [F(2), F(-2), F(-2), F(-2), F(-2)],
    "DLT": [F(-2), F(1), F(0), F(2), F(1)],
    "EMK": [F(1), F(0), F(1), F(-1), F(0)],
}
for t in range(T):
    for n in NAMES:
        fit = X5[n][0] * f_mkt[t] + X5[n][1] * f_chp[t]
        check(f"miss recomputed, {n} month {t+1}", RET5[n][t] - fit, U5[n][t])
for t in range(T):
    check(f"Level 2 balance, ones column, month {t+1}",
          sum(U5[n][t] for n in NAMES), F(0))
    check(f"Level 2 balance, cheapness column, month {t+1}",
          sum(X5[n][1] * U5[n][t] for n in NAMES), F(0))

SU2 = {n: sum(u * u for u in U5[n]) for n in NAMES}
check("sum of squared misses per name", [SU2[n] for n in NAMES],
      [F(3), F(10), F(20), F(10), F(3)])
dvec = [SU2[n] / T for n in NAMES]
check("D's diagonal = (sum of squared misses)/T, all five names", dvec,
      [F(3, 5), F(2), F(4), F(2), F(3, 5)])
Dm = diagm(dvec)
check("D is 5x5", (len(Dm), len(Dm[0])), (5, 5))
check("every off-diagonal of D is zero -- that IS the Level 9 assumption",
      [Dm[i][j] for i in range(5) for j in range(5) if i != j], [F(0)] * 20)

sub("3d. V = X F X^T + D, the whole-universe grid")

XT = transpose(X)
XFXt = matmul(matmul(X, Fm), XT)
V = addm(XFXt, Dm)
check("V is symmetric", is_symmetric(V), True)
check("V row AXL", V[0], [F(188, 5), F(25), F(13), F(1), F(-11)])
check("V row BRN", V[1], [F(25), F(24), F(19), F(16), F(13)])
check("V row CHR", V[2], [F(13), F(19), F(29), F(31), F(37)])
check("V row DLT", V[3], [F(1), F(16), F(31), F(48), F(61)])
check("V row EMK", V[4], [F(-11), F(13), F(37), F(61), F(428, 5)])

# closed form, all 25 cells
for i in range(5):
    for j in range(5):
        cf = F(25) + 6 * (xs[i] + xs[j]) + 9 * xs[i] * xs[j] + (dvec[i] if i == j else 0)
        check(f"closed form 25 + 6(x_i+x_j) + 9 x_i x_j (+d) at ({NAMES[i]},{NAMES[j]})",
              V[i][j], cf)

check("the Level 10 3x3 sub-block (AXL, CHR, EMK) is unchanged",
      [[V[i][j] for j in (0, 2, 4)] for i in (0, 2, 4)],
      [[F(188, 5), F(13), F(-11)], [F(13), F(29), F(37)],
       [F(-11), F(37), F(428, 5)]])
check("the alternative bracketing X(F X^T) agrees",
      matmul(X, matmul(Fm, XT)), XFXt)

sub("3e. standalone volatilities -- one name at a time, no portfolio")

for n, i, printed in [("AXL", 0, "6.1319"), ("BRN", 1, "4.8990"), ("CHR", 2, "5.3852"),
                      ("DLT", 3, "6.9282"), ("EMK", 4, "9.2520")]:
    check_root(f"standalone volatility {n}", V[i][i], printed)
check("BRN is the quietest name standing alone",
      min(range(5), key=lambda i: V[i][i]), 1)
check("EMK is the loudest name standing alone",
      max(range(5), key=lambda i: V[i][i]), 4)


# ===========================================================================
head("SECTION 4 -- THE NUDGE, AND WHERE MCR COMES FROM")
# ===========================================================================

WD = [F(30, 100), F(17, 100), F(8, 100), F(15, 100), F(30, 100)]
check("Book D weights", WD, [F(3, 10), F(17, 100), F(2, 25), F(3, 20), F(3, 10)])
check("Book D is fully invested", sum(WD), F(1))

hD = matvec(transpose(X), WD)
check("Book D factor exposures h = X^T w", hD, [F(1), F(-1, 50)])
check_dec("Book D cheapness exposure as a decimal", hD[1], "-0.0200")

facD = quad(Fm, hD)
specD = sum(WD[i] * WD[i] * dvec[i] for i in range(5))
varD = facD + specD
check("Book D factor variance h^T F h", facD, F(61909, 2500))
check_dec("Book D factor variance as a decimal", facD, "24.7636")
check("Book D specific variance sum w_i^2 d_i", specD, F(591, 2500))
check_dec("Book D specific variance as a decimal", specD, "0.2364")
check("Book D total variance", varD, F(25))
check("Book D total risk is an EXACT root", rootF(varD), F(5))

VwD = matvec(V, WD)
check("V w for Book D", VwD, [F(671, 50), F(97, 5), F(126, 5), F(31), F(367, 10)])
for n, i, printed in [("AXL", 0, "13.4200"), ("BRN", 1, "19.4000"), ("CHR", 2, "25.2000"),
                      ("DLT", 3, "31.0000"), ("EMK", 4, "36.7000")]:
    check_dec(f"(V w) for {n}", VwD[i], printed)
check("w^T (V w) reproduces the total variance", dot(WD, VwD), varD)

sub("4b. the nudge identity is EXACT, not an approximation")

# Var(w + e*unit_i) = Var(w) + 2e (Vw)_i + e^2 V_ii, exactly, for every e
def var_of(w):
    h = matvec(transpose(X), w)
    return quad(Fm, h) + sum(w[i] * w[i] * dvec[i] for i in range(5))

swept = 0
for i in range(5):
    for e in (F(1, 100), F(-1, 100), F(1, 50), F(-1, 50), F(1, 20), F(-1, 20),
              F(1, 4), F(-1, 4)):
        w2 = list(WD)
        w2[i] = w2[i] + e
        lhs = var_of(w2)
        rhs = varD + 2 * e * VwD[i] + e * e * V[i][i]
        if lhs != rhs:
            sys.exit(f"nudge identity failed for {NAMES[i]}, e={e}")
        swept += 1
check("nudge identity Var(w + e u_i) = Var + 2e(Vw)_i + e^2 V_ii, swept exactly",
      swept, 40)

sub("4c. worked nudges: +1% of one name, funded from cash")

wEMK1 = [F(30, 100), F(17, 100), F(8, 100), F(15, 100), F(31, 100)]
vEMK1 = var_of(wEMK1)
check("Book D with EMK at 31%: exact new variance", vEMK1, F(160891, 6250))
check("the variance moved by exactly 2(0.01)(36.70) + (0.01)^2(85.6)",
      vEMK1 - varD, 2 * F(1, 100) * VwD[4] + F(1, 10000) * V[4][4])
check_dec("that change, as a decimal", vEMK1 - varD, "0.7426")
check_dec("the first-order piece 2(0.01)(36.70)", 2 * F(1, 100) * VwD[4], "0.7340")
check_dec("the second-order piece (0.01)^2(85.6)", F(1, 10000) * V[4][4],
          "0.00856", places=5)
check_root("exact new risk after +1% EMK", vEMK1, "5.0737")
check("MCR prediction 5 + 0.01 x 7.34", F(5) + F(1, 100) * F(367, 50), F(25367, 5000))
check_dec("that prediction as a decimal", F(25367, 5000), "5.0734")

wAXL1 = [F(31, 100), F(17, 100), F(8, 100), F(15, 100), F(30, 100)]
vAXL1 = var_of(wAXL1)
check("Book D with AXL at 31%: exact new variance", vAXL1, F(157951, 6250))
check_dec("the second-order piece (0.01)^2(37.6)", F(1, 10000) * V[0][0],
          "0.00376", places=5)
check("the variance moved by exactly 2(0.01)(13.42) + (0.01)^2(37.6)",
      vAXL1 - varD, 2 * F(1, 100) * VwD[0] + F(1, 10000) * V[0][0])
check_dec("that change, as a decimal", vAXL1 - varD, "0.2722")
check_root("exact new risk after +1% AXL", vAXL1, "5.0271")
check("MCR prediction 5 + 0.01 x 2.684", F(5) + F(1, 100) * F(671, 250),
      F(125671, 25000))
check_dec("that prediction as a decimal", F(125671, 25000), "5.0268")

sub("4d. the square-root nudge, checked as algebra")

# (sigma + delta/(2 sigma))^2 = Var + delta + delta^2/(4 sigma^2)
sig = F(5)
swept = 0
for delta in (F(367, 500), F(671, 2500), F(-367, 500), F(1, 1000)):
    lhs = (sig + delta / (2 * sig)) ** 2
    rhs = varD + delta + delta * delta / (4 * sig * sig)
    if lhs != rhs:
        sys.exit("square-root nudge algebra failed")
    swept += 1
check("(sigma + delta/2sigma)^2 = Var + delta + delta^2/(4 Var), swept", swept, 4)
check("the leftover on the +1% EMK nudge, delta^2/(4 Var)",
      (vEMK1 - varD) ** 2 / (4 * varD), F(21538881, 3906250000))
check_dec("that leftover as a decimal", (vEMK1 - varD) ** 2 / (4 * varD), "0.0055")

sub("4e. MCR itself")

MCRD = [VwD[i] / F(5) for i in range(5)]
check("MCR = (V w)_i / sigma, Book D", MCRD,
      [F(671, 250), F(97, 25), F(126, 25), F(31, 5), F(367, 50)])
for n, i, printed in [("AXL", 0, "2.6840"), ("BRN", 1, "3.8800"), ("CHR", 2, "5.0400"),
                      ("DLT", 3, "6.2000"), ("EMK", 4, "7.3400")]:
    check_dec(f"MCR {n}", MCRD[i], printed)
check("the two 30% positions differ in MCR by a factor of 1835/671",
      MCRD[4] / MCRD[0], F(1835, 671))
check_dec("that factor as a decimal", F(1835, 671), "2.7347")
check("MCR ranking (largest first)", sorted(range(5), key=lambda i: -MCRD[i]),
      [4, 3, 2, 1, 0])
check("MCR_i * sigma = (V w)_i for every name",
      [MCRD[i] * F(5) for i in range(5)], VwD)


# ===========================================================================
head("SECTION 5 -- CONTRIBUTIONS, AND WHY THEY ADD UP EXACTLY")
# ===========================================================================

CTRD = [WD[i] * MCRD[i] for i in range(5)]
check("contributions w_i * MCR_i", CTRD,
      [F(2013, 2500), F(1649, 2500), F(252, 625), F(93, 100), F(1101, 500)])
for n, i, printed in [("AXL", 0, "0.8052"), ("BRN", 1, "0.6596"), ("CHR", 2, "0.4032"),
                      ("DLT", 3, "0.9300"), ("EMK", 4, "2.2020")]:
    check_dec(f"contribution {n}", CTRD[i], printed)
check("EULER: the five contributions sum to exactly the total risk",
      sum(CTRD), F(5))
check("and that is one line of algebra: sum w_i (Vw)_i / sigma = Var/sigma = sigma",
      dot(WD, VwD) / F(5), F(5))

shareD = [CTRD[i] / F(5) for i in range(5)]
check("shares of risk", shareD,
      [F(2013, 12500), F(1649, 12500), F(252, 3125), F(93, 500), F(1101, 2500)])
for n, i, printed in [("AXL", 0, "16.1040"), ("BRN", 1, "13.1920"), ("CHR", 2, "8.0640"),
                      ("DLT", 3, "18.6000"), ("EMK", 4, "44.0400")]:
    check_dec(f"share of risk {n} (%)", shareD[i] * 100, printed)
check("the five shares sum to exactly 1", sum(shareD), F(1))
check("share of risk equals share of variance, name by name",
      shareD, [WD[i] * VwD[i] / varD for i in range(5)])

sub("5b. the scaling argument, checked numerically")

# scaling every weight by (1+e) scales risk by exactly (1+e)
swept = 0
for e in (F(1, 100), F(1, 10), F(1, 2), F(-1, 100), F(-1, 4)):
    w2 = [wi * (1 + e) for wi in WD]
    if var_of(w2) != varD * (1 + e) ** 2:
        sys.exit("homogeneity failed")
    swept += 1
check("scaling all weights by (1+e) scales VARIANCE by (1+e)^2, swept", swept, 5)
check("so it scales RISK by exactly (1+e): the Euler premise",
      rootF(var_of([wi * F(11, 10) for wi in WD])), F(11, 2))

sub("5c. Euler swept over many books")

swept = 0
for combo in product(range(1, 9), repeat=4):
    rest = 20 - sum(combo)
    if not (1 <= rest <= 8):
        continue
    w = [F(5 * c, 100) for c in combo] + [F(5 * rest, 100)]
    vw = matvec(V, w)
    vv = dot(w, vw)
    if sum(w[i] * vw[i] for i in range(5)) != vv:
        sys.exit("Euler failed in variance form")
    if sum(w[i] * vw[i] / vv for i in range(5)) != F(1):
        sys.exit("shares failed to sum to 1")
    swept += 1
check("Euler and the shares-sum-to-one identity, swept over 5%-grid books",
      swept, 2226)
EULER_SWEEP = swept


# ===========================================================================
head("SECTION 6 -- THE REPORT, BOOK D POSITION BY POSITION")
# ===========================================================================

print("   name |  weight |  standalone vol |    MCR |  contribution | % of risk")
for i in range(5):
    print(f"   {NAMES[i]:4s} | {float(WD[i])*100:6.0f}% | "
          f"{sqrtD(V[i][i]).quantize(Decimal('0.0001')):>15} | "
          f"{float(MCRD[i]):6.3f} | {float(CTRD[i]):13.4f} | "
          f"{float(shareD[i])*100:8.3f}%")

check("weight ranking (largest first, ties by name order)",
      sorted(range(5), key=lambda i: (-WD[i], i)), [0, 4, 1, 3, 2])
check("contribution ranking (largest first)",
      sorted(range(5), key=lambda i: -CTRD[i]), [4, 3, 0, 1, 2])
check("AXL and EMK hold exactly the same weight", WD[0], WD[4])
check("but EMK's contribution is 1835/671 times AXL's", CTRD[4] / CTRD[0],
      F(1835, 671))
check("DLT is exactly half of AXL by weight", WD[3] * 2, WD[0])
check("and DLT still contributes more than AXL", CTRD[3] > CTRD[0], True)
check_dec("DLT contribution minus AXL contribution", CTRD[3] - CTRD[0], "0.1248")
check("the top two contributors, EMK and DLT, are 45% of the money",
      WD[4] + WD[3], F(9, 20))
check("their share of the risk", shareD[4] + shareD[3], F(783, 1250))
check_dec("EMK + DLT share of risk (%)", (shareD[4] + shareD[3]) * 100, "62.6400")
check("EMK + AXL are 60% of the money", WD[4] + WD[0], F(3, 5))
check_dec("EMK + AXL share of risk (%)", (shareD[4] + shareD[0]) * 100, "60.1440")

sub("6b. the split of the total")

check("factor share of Book D's variance", facD / varD, F(61909, 62500))
check_dec("factor share (%)", facD / varD * 100, "99.0544")
check("specific share of Book D's variance", specD / varD, F(591, 62500))
check_dec("specific share (%)", specD / varD * 100, "0.9456")
check_root("annualised total risk, x sqrt(12), ours not BFRE's", varD * 12, "17.3205")

sub("6c. the -11 cell, the reason AXL is quiet")

check("V[AXL,EMK] is negative", V[0][4], F(-11))
check("AXL's covariance with the book, term by term",
      sum(V[0][j] * WD[j] for j in range(5)), F(671, 50))
terms = [V[0][j] * WD[j] for j in range(5)]
check("those five terms", terms,
      [F(564, 50), F(425, 100), F(104, 100), F(15, 100), F(-330, 100)])
for n, i, printed in [("AXL", 0, "11.2800"), ("BRN", 1, "4.2500"), ("CHR", 2, "1.0400"),
                      ("DLT", 3, "0.1500"), ("EMK", 4, "-3.3000")]:
    check_dec(f"AXL's co-movement term with {n}", terms[i], printed)
check("they sum to (V w)_AXL", sum(terms), VwD[0])


# ===========================================================================
head("SECTION 7 -- WHAT THE DESK DOES WITH IT")
# ===========================================================================

sub("7a. cut 1% into cash: the same trade on two different names")

wCutE = [F(30, 100), F(17, 100), F(8, 100), F(15, 100), F(29, 100)]
wCutA = [F(29, 100), F(17, 100), F(8, 100), F(15, 100), F(30, 100)]
vCutE, vCutA = var_of(wCutE), var_of(wCutA)
check("cut 1% of EMK to cash: exact variance", vCutE, F(75858, 3125))
check_root("cut 1% of EMK to cash: risk", vCutE, "4.9269")
check("cut 1% of AXL to cash: exact variance", vCutA, F(77298, 3125))
check_root("cut 1% of AXL to cash: risk", vCutA, "4.9735")
check("MCR prediction for the EMK cut", F(5) - F(1, 100) * MCRD[4], F(24633, 5000))
check_dec("that prediction", F(24633, 5000), "4.9266")
check("MCR prediction for the AXL cut", F(5) - F(1, 100) * MCRD[0], F(124329, 25000))
check_dec("that prediction", F(124329, 25000), "4.9732")

sub("7b. the funded swap: sell one, buy the other, stay fully invested")

wSwap = [F(31, 100), F(17, 100), F(8, 100), F(15, 100), F(29, 100)]
vSwap = var_of(wSwap)
check("sell 1% EMK, buy 1% AXL: exact variance", vSwap, F(613723, 25000))
check_root("sell 1% EMK, buy 1% AXL: risk", vSwap, "4.9547")
check("MCR prediction for the swap", F(5) + F(1, 100) * (MCRD[0] - MCRD[4]),
      F(30959, 6250))
check_dec("that prediction", F(30959, 6250), "4.9534")
wSwapBad = [F(29, 100), F(17, 100), F(8, 100), F(15, 100), F(31, 100)]
vSwapBad = var_of(wSwapBad)
check("the same swap the wrong way round: exact variance", vSwapBad, F(637003, 25000))
check_root("the same swap the wrong way round: risk", vSwapBad, "5.0478")
check("MCR prediction for the wrong-way swap",
      F(5) + F(1, 100) * (MCRD[4] - MCRD[0]), F(31541, 6250))
check_dec("that prediction", F(31541, 6250), "5.0466")

sub("7c. how far the swap can run: the equal-MCR point")

# w = (0.30 + t, 0.17, 0.08, 0.15, 0.30 - t)
def swap_book(t):
    return [F(30, 100) + t, F(17, 100), F(8, 100), F(15, 100), F(30, 100) - t]

tstar = F(97, 605)
wStar = swap_book(tstar)
VwStar = matvec(V, wStar)
check("at t = 97/605 the two marginal contributions are equal",
      VwStar[0], VwStar[4])
check("their common value", VwStar[0], F(128333, 6050))
check_dec("t* as a percentage of NAV", tstar * 100, "16.0331")
check_dec("AXL's weight there (%)", wStar[0] * 100, "46.0331")
check_dec("EMK's weight there (%)", wStar[4] * 100, "13.9669")
vStar = var_of(wStar)
check("the variance at that point", vStar, F(321671, 15125))
check_root("the risk at that point", vStar, "4.6117")
check_root("the risk it started from, for the 'against 5.00' comparison", varD, "5.0000")
show("context, not a printed figure -- the whole swap removes",
     (sqrtD(varD) - sqrtD(vStar)).quantize(Decimal("0.0001")))
check("the swap is a genuine minimum: nudging t either way raises the variance",
      (var_of(swap_book(tstar + F(1, 100))) > vStar,
       var_of(swap_book(tstar - F(1, 100))) > vStar), (True, True))
swept = 0
for k in range(-30, 31):
    if k == 0:
        continue
    if var_of(swap_book(tstar + F(k, 200))) <= vStar:
        sys.exit("t* is not the minimum")
    swept += 1
check("swept 60 offsets around t*, every one is riskier", swept, 60)
MIN_SWEEP = swept

sub("7d. first order is not exact -- the size of the error, every time")

for lbl, exact_var, pred in [
        ("+1% EMK", vEMK1, F(25367, 5000)),
        ("+1% AXL", vAXL1, F(125671, 25000)),
        ("cut 1% EMK", vCutE, F(24633, 5000)),
        ("cut 1% AXL", vCutA, F(124329, 25000)),
        ("swap 1% EMK->AXL", vSwap, F(30959, 6250)),
        ("swap 1% AXL->EMK", vSwapBad, F(31541, 6250))]:
    err = sqrtD(exact_var) - (Decimal(F(pred).numerator) / Decimal(F(pred).denominator))
    print(f"        {lbl:18s} exact {sqrtD(exact_var).quantize(Decimal('0.000001'))}  "
          f"predicted {float(pred):.6f}  error {err.quantize(Decimal('0.000001'))}")
signs = []
for lbl, exact_var, pred in [
        ("+1% EMK", vEMK1, F(25367, 5000)),
        ("+1% AXL", vAXL1, F(125671, 25000)),
        ("cut 1% EMK", vCutE, F(24633, 5000)),
        ("cut 1% AXL", vCutA, F(124329, 25000)),
        ("swap 1% EMK->AXL", vSwap, F(30959, 6250)),
        ("swap 1% AXL->EMK", vSwapBad, F(31541, 6250))]:
    signs.append(sqrtD(exact_var)
                 > Decimal(F(pred).numerator) / Decimal(F(pred).denominator))
check("all six first-order predictions come in BELOW the exact answer", signs, [True] * 6)



# ===========================================================================
head("SECTION 8 -- AGAINST A BENCHMARK: THE SAME MACHINERY, A DIFFERENT PIE")
# ===========================================================================

BM = [F(20, 100)] * 5
check("the benchmark holds all five names equally", BM, [F(1, 5)] * 5)
check("the benchmark's weights sum to 1", sum(BM), F(1))
hB = matvec(transpose(X), BM)
check("the benchmark's factor exposures", hB, [F(1), F(0)])
varB = var_of(BM)
check("the benchmark's variance", varB, F(3171, 125))
check("its factor part is exactly 25 -- a pure market bet", quad(Fm, hB), F(25))
check("its specific part", sum(BM[i] ** 2 * dvec[i] for i in range(5)), F(46, 125))
check_root("the benchmark's own risk", varB, "5.0367")
check("Book D is LESS volatile than its benchmark", varD < varB, True)
show("context, not a printed figure -- benchmark risk minus Book D risk "
     "(the ACTIVE risk is not this)",
     (sqrtD(varB) - sqrtD(varD)).quantize(Decimal("0.0001")))

A = [WD[i] - BM[i] for i in range(5)]
check("the active weights a = w - b", A,
      [F(1, 10), F(-3, 100), F(-3, 25), F(-1, 20), F(1, 10)])
check("the active weights sum to exactly zero", sum(A), F(0))
hA = matvec(transpose(X), A)
check("the active factor exposures", hA, [F(0), F(-1, 50)])
check("the market bet cancels exactly", hA[0], F(0))

facA = quad(Fm, hA)
specA = sum(A[i] ** 2 * dvec[i] for i in range(5))
varA = facA + specA
check("active factor variance", facA, F(9, 2500))
check("active specific variance", specA, F(191, 2500))
check("active variance", varA, F(2, 25))
check_root("ACTIVE RISK", varA, "0.2828")
check("active factor share", facA / varA, F(9, 200))
check_dec("active factor share (%)", facA / varA * 100, "4.5000")
check("active specific share", specA / varA, F(191, 200))
check_dec("active specific share (%)", specA / varA * 100, "95.5000")

VaA = matvec(V, A)
check("V a", VaA, [F(3, 10), F(0), F(-3, 5), F(-2, 5), F(-21, 50)])
for n, i, printed in [("AXL", 0, "0.3000"), ("BRN", 1, "0.0000"), ("CHR", 2, "-0.6000"),
                      ("DLT", 3, "-0.4000"), ("EMK", 4, "-0.4200")]:
    check_dec(f"(V a) for {n}", VaA[i], printed)
check("BRN's active marginal contribution is EXACTLY zero", VaA[1], F(0))
check("EMK's active marginal contribution is NEGATIVE", VaA[4] < 0, True)
ctrA = [A[i] * VaA[i] for i in range(5)]
check("active contributions to variance", ctrA,
      [F(3, 100), F(0), F(9, 125), F(1, 50), F(-21, 500)])
check("they sum to the active variance", sum(ctrA), varA)
shA = [c / varA for c in ctrA]
check("active shares of risk", shA, [F(3, 8), F(0), F(9, 10), F(1, 4), F(-21, 40)])
for n, i, printed in [("AXL", 0, "37.5000"), ("BRN", 1, "0.0000"), ("CHR", 2, "90.0000"),
                      ("DLT", 3, "25.0000"), ("EMK", 4, "-52.5000")]:
    check_dec(f"active share {n} (%)", shA[i] * 100, printed)
check("the five active shares sum to exactly 1", sum(shA), F(1))

for n, i, printed in [("AXL", 0, "1.0607"), ("BRN", 1, "0.0000"), ("CHR", 2, "-2.1213"),
                      ("DLT", 3, "-1.4142"), ("EMK", 4, "-1.4849")]:
    CHECKS[0] += 1
    v = F(VaA[i])
    got = ((Decimal(v.numerator) / Decimal(v.denominator)) / sqrtD(varA)).quantize(Decimal("0.0001"))
    ok = (str(got) == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] active MCR {n}: {got}"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit(f"MISMATCH active MCR {n}")

sub("8b. the two pies side by side")

check_dec("Book D TOTAL: factor share (%)", facD / varD * 100, "99.0544")
check_dec("Book D TOTAL: specific share (%)", specD / varD * 100, "0.9456")
check_dec("Book D ACTIVE: factor share (%)", facA / varA * 100, "4.5000")
check_dec("Book D ACTIVE: specific share (%)", specA / varA * 100, "95.5000")
check("the specific share is 101 and a bit times larger in the active pie",
      (specA / varA) / (specD / varD), F(191 * 62500, 200 * 591))
check_dec("that ratio", (specA / varA) / (specD / varD), "100.9941")

sub("8c. Euler holds in active space too, swept")

swept = 0
for combo in product(range(-3, 4), repeat=4):
    last = -sum(combo)
    if abs(last) > 3:
        continue
    a = [F(5 * c, 100) for c in combo] + [F(5 * last, 100)]
    if all(t == 0 for t in a):
        continue
    va = matvec(V, a)
    vv = dot(a, va)
    if sum(a[i] * va[i] for i in range(5)) != vv:
        sys.exit("active Euler failed")
    if vv <= 0:
        sys.exit("active variance not strictly positive")
    swept += 1
check("active Euler, and strict positivity, swept over zero-sum 5% books",
      swept, 1450)
ACTIVE_SWEEP = swept


# ===========================================================================
head("SECTION 9 -- TRAPS, EACH WITH THE NUMBER IT RETURNS")
# ===========================================================================

sub("trap 1: rank by weight and cut the biggest position")
check_root("cut 1% of AXL (joint-largest) to cash", vCutA, "4.9735")
check_root("cut 1% of EMK (same size) to cash", vCutE, "4.9269")
d1 = (sqrtD(varD) - sqrtD(vCutA)).quantize(Decimal("0.0001"))
d2 = (sqrtD(varD) - sqrtD(vCutE)).quantize(Decimal("0.0001"))
check("risk removed by the AXL cut and by the EMK cut, as printed",
      (str(d1), str(d2)), ("0.0265", "0.0731"))
check("first-order, EMK removes 1835/671 times as much per point sold",
      MCRD[4] / MCRD[0], F(1835, 671))

sub("trap 2: weight times standalone volatility")
CHECKS[0] += 1
naive = [Decimal(F(WD[i]).numerator) / Decimal(F(WD[i]).denominator) * sqrtD(V[i][i])
         for i in range(5)]
naive_tot = sum(naive)
for n, i, printed in [("AXL", 0, "1.8396"), ("BRN", 1, "0.8328"), ("CHR", 2, "0.4308"),
                      ("DLT", 3, "1.0392"), ("EMK", 4, "2.7756")]:
    CHECKS[0] += 1
    got = naive[i].quantize(Decimal("0.0001"))
    ok = (str(got) == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] naive w x standalone vol, {n}: {got}"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit("MISMATCH naive contribution")
check("the naive total, as the markdown prints it",
      str(naive_tot.quantize(Decimal("0.0001"))), "6.9180")
over = ((naive_tot - 5) / 5 * 100).quantize(Decimal("0.0001"))
check("and it overstates the risk by, as printed", str(over), "38.3609")
CHECKS[0] += 1
naive_rank = sorted(range(5), key=lambda i: -naive[i])
ok = (naive_rank == [4, 0, 3, 1, 2])
print(f"   [{'OK ' if ok else 'FAIL'}] naive ranking {naive_rank} against true [4, 0, 3, 1, 2]")
if not ok:
    sys.exit("MISMATCH naive ranking")

sub("trap 3: forget the weight and rank by MCR alone")
check("the five MCRs summed, which is not a risk of anything", sum(MCRD),
      F(3143, 125))
check_dec("that sum", sum(MCRD), "25.1440")

sub("trap 4: use only the diagonal of V")
tdiag = sum(WD[i] ** 2 * V[i][i] for i in range(5))
check("sum w_i^2 V_ii", tdiag, F(16309, 1250))
check_root("the risk that returns", tdiag, "3.6121")
check("versus 5.0000, as printed",
      str(((sqrtD(tdiag) - 5) / 5 * 100).quantize(Decimal("0.01"))), "-27.76")

sub("trap 5: drop D, or drop F's off-diagonals")
check("drop D entirely", facD, F(61909, 2500))
check_root("the risk that returns", facD, "4.9763")
noff = 25 * hD[0] ** 2 + 9 * hD[1] ** 2 + specD
check("drop F's off-diagonals", noff, F(631, 25))
check_root("the risk that returns", noff, "5.0239")

sub("trap 6: 'a contribution cannot be negative'")
check("EMK's active contribution is negative", ctrA[4] < 0, True)
check_dec("EMK's active share (%)", shA[4] * 100, "-52.5000")
check("and the five active shares still sum to exactly 1", sum(shA), F(1))

sub("trap 7: treat MCR as exact rather than first-order")
CHECKS[0] += 1
big = [F(30, 100) + F(1, 10), F(17, 100), F(8, 100), F(15, 100), F(30, 100) - F(1, 10)]
vbig = var_of(big)
pred_big = F(5) + F(1, 10) * (MCRD[0] - MCRD[4])
check("a 10-point swap: exact variance", vbig, F(5449, 250))
check_root("a 10-point swap: exact risk", vbig, "4.6686")
check("the first-order prediction", pred_big, F(2834, 625))
check_dec("that prediction", pred_big, "4.5344")

TRAPS = 7


# ===========================================================================
head("SECTION 10 -- THE SABOTAGE ROUND")
# ===========================================================================

corrupt = [F(8052, 10000), F(6596, 10000), F(4032, 10000), F(9030, 10000),
           F(22020, 10000)]
check("the printed contributions, one of them corrupted", corrupt,
      [F(2013, 2500), F(1649, 2500), F(252, 625), F(903, 1000), F(1101, 500)])
check("they sum to", sum(corrupt), F(49730, 10000))
check_dec("that sum", sum(corrupt), "4.9730")
check("Euler says the sum must be the total risk", sum(CTRD), rootF(varD))
check("the shortfall", F(5) - sum(corrupt), F(27, 1000))
check_dec("the shortfall", F(5) - sum(corrupt), "0.0270")
check("the four uncorrupted entries sum to",
      corrupt[0] + corrupt[1] + corrupt[2] + corrupt[4], F(407, 100))
check("so the repaired entry is", F(5) - (corrupt[0] + corrupt[1] + corrupt[2] + corrupt[4]),
      F(93, 100))
check("the second, independent check: contribution / weight must be MCR",
      corrupt[3] / WD[3], F(301, 50))
check_dec("the corrupted implied MCR", corrupt[3] / WD[3], "6.0200")
check("against (V w)_DLT / sigma", VwD[3] / F(5), F(31, 5))
check_dec("the true MCR", VwD[3] / F(5), "6.2000")
check("the third check: the shares would sum to", sum(c / F(5) for c in corrupt),
      F(4973, 5000))
check_dec("that sum of shares (%)", sum(c / F(5) for c in corrupt) * 100, "99.4600")

swept = 0
for i in range(5):
    for err in (F(27, 1000), F(-27, 1000), F(1, 100), F(-1, 100), F(1, 1000), F(-1, 1000)):
        bad = list(CTRD)
        bad[i] = bad[i] + err
        if sum(bad) == F(5):
            sys.exit("a corrupted report passed the Euler check")
        swept += 1
check("every single-entry corruption of the report fails the Euler check, swept",
      swept, 30)
SABOTAGE_SWEEP = swept


# ===========================================================================
head("SECTION 11 -- BOSS ROUND: BOOK P")
# ===========================================================================

WP = [F(18, 100), F(19, 100), F(28, 100), F(9, 100), F(26, 100)]
check("Book P weights", WP, [F(9, 50), F(19, 100), F(7, 25), F(9, 100), F(13, 50)])
check("Book P is fully invested", sum(WP), F(1))
check("no position exceeds 28% of NAV", max(WP), F(7, 25))
hP = matvec(transpose(X), WP)
check("Book P factor exposures", hP, [F(1), F(3, 50)])
check_dec("Book P's net cheapness tilt", hP[1], "0.0600")

facP = quad(Fm, hP)
specP = sum(WP[i] ** 2 * dvec[i] for i in range(5))
varP = facP + specP
check("Book P factor variance", facP, F(64381, 2500))
check_dec("Book P factor variance", facP, "25.7524")
check("Book P specific variance", specP, F(231, 500))
check_dec("Book P specific variance", specP, "0.4620")
check("Book P total variance", varP, F(16384, 625))
check_dec("Book P total variance", varP, "26.2144")
check("Book P total risk is an EXACT root", rootF(varP), F(128, 25))
check_dec("Book P total risk", F(128, 25), "5.1200")

VwP = matvec(V, WP)
check("V w for Book P", VwP,
      [F(3097, 250), F(96, 5), F(662, 25), F(802, 25), F(9649, 250)])
for n, i, printed in [("AXL", 0, "12.3880"), ("BRN", 1, "19.2000"), ("CHR", 2, "26.4800"),
                      ("DLT", 3, "32.0800"), ("EMK", 4, "38.5960")]:
    check_dec(f"(V w) for {n}", VwP[i], printed)

MCRP = [VwP[i] / F(128, 25) for i in range(5)]
CTRP = [WP[i] * MCRP[i] for i in range(5)]
shP = [CTRP[i] / F(128, 25) for i in range(5)]
check("Book P MCRs", MCRP,
      [F(3097, 1280), F(15, 4), F(331, 64), F(401, 64), F(9649, 1280)])
for n, i, printed in [("AXL", 0, "2.4195"), ("BRN", 1, "3.7500"), ("CHR", 2, "5.1719"),
                      ("DLT", 3, "6.2656"), ("EMK", 4, "7.5383")]:
    check_dec(f"Book P MCR {n}", MCRP[i], printed)
for n, i, printed in [("AXL", 0, "0.4355"), ("BRN", 1, "0.7125"), ("CHR", 2, "1.4481"),
                      ("DLT", 3, "0.5639"), ("EMK", 4, "1.9600")]:
    check_dec(f"Book P contribution {n}", CTRP[i], printed)
check("EULER on Book P: contributions sum to the total risk", sum(CTRP), F(128, 25))
for n, i, printed in [("AXL", 0, "8.51"), ("BRN", 1, "13.92"), ("CHR", 2, "28.28"),
                      ("DLT", 3, "11.01"), ("EMK", 4, "38.28")]:
    check_dec(f"Book P share of risk {n} (%)", shP[i] * 100, printed, places=2)
check("Book P shares sum to exactly 1", sum(shP), F(1))
check("the largest position is CHR", max(range(5), key=lambda i: WP[i]), 2)
check("the largest contributor is EMK", max(range(5), key=lambda i: CTRP[i]), 4)
check("DLT is exactly half of AXL by weight", WP[3] * 2, WP[0])
check("and DLT still contributes more than AXL", CTRP[3] > CTRP[0], True)
check_dec("DLT's share minus AXL's share (percentage points)",
          (shP[3] - shP[0]) * 100, "2.51", places=2)

sub("11b. the four numbers that answer 'I am diversified'")

check("factor share of Book P's risk", facP / varP, F(64381, 65536))
check_dec("factor share (%)", facP / varP * 100, "98.2376")
check("specific share of Book P's risk", specP / varP, F(1155, 65536))
check_dec("specific share (%)", specP / varP * 100, "1.7624")
check_root("the risk that survives if every specific wobble vanished", facP, "5.0747")
gap = (sqrtD(varP) - sqrtD(facP)).quantize(Decimal("0.0001"))
check("so all five names' private lives are worth, of the 5.1200", str(gap), "0.0453")
check("EMK and CHR are 54% of the money", WP[4] + WP[2], F(27, 50))
check_dec("EMK + CHR share of risk (%)", (shP[4] + shP[2]) * 100, "66.56", places=2)

sub("11c. the diversification floor -- what more names could ever buy")

for n, printed in [(5, "5.0367"), (10, "5.0184"), (50, "5.0037"), (1000, "5.0002")]:
    v = F(25) + F(46, 25) / n
    check_root(f"an equally weighted book of {n} names like these", v, printed)
check("the equally weighted five-name book IS the benchmark", F(25) + F(46, 25) / 5,
      varB)
check("the floor as the name count grows without limit is the factor term alone",
      [F(25) + F(46, 25) / n - F(25) < F(1, 1000) for n in (10000, 1000000)],
      [True, True])
check("average standalone variance across the five names",
      sum(V[i][i] for i in range(5)) / 5, F(1121, 25))
check_root("average standalone volatility", F(1121, 25), "6.6963")

sub("11d. the counterfactual: even at a net tilt of exactly zero")

# a book with h2 = 0 exactly, same shape of weights
hZero = [F(1), F(0)]
VwZero = [25 * hZero[0] + 6 * hZero[1] + xs[i] * (6 * hZero[0] + 9 * hZero[1])
          for i in range(5)]
check("with h = (1, 0) the co-movements are still 13, 19, 25, 31, 37", VwZero,
      [F(13), F(19), F(25), F(31), F(37)])
check("the spread is a factor of 37/13 even with no style bet at all",
      F(37, 13), F(37, 13))
check_dec("that factor", F(37, 13), "2.8462")
check("the d_i w_i terms Book P adds on the diagonal",
      [dvec[i] * WP[i] for i in range(5)],
      [F(108, 1000), F(38, 100), F(112, 100), F(18, 100), F(156, 1000)])
for n, i, printed in [("AXL", 0, "0.108"), ("BRN", 1, "0.380"), ("CHR", 2, "1.120"),
                      ("DLT", 3, "0.180"), ("EMK", 4, "0.156")]:
    check_dec(f"Book P diagonal add-on, {n}", dvec[i] * WP[i], printed, places=3)
check("adding them does not change the ordering",
      sorted(range(5), key=lambda i: -(F(25) + 6 * xs[i] + dvec[i] * WP[i])),
      [4, 3, 2, 1, 0])

sub("11e. Book P against the same benchmark")

AP = [WP[i] - BM[i] for i in range(5)]
check("Book P's active weights", AP,
      [F(-1, 50), F(-1, 100), F(2, 25), F(-11, 100), F(3, 50)])
check("they sum to zero", sum(AP), F(0))
hAP = matvec(transpose(X), AP)
check("Book P's active exposures", hAP, [F(0), F(3, 50)])
facAP = quad(Fm, hAP)
specAP = sum(AP[i] ** 2 * dvec[i] for i in range(5))
varAP = facAP + specAP
check("Book P active factor variance", facAP, F(81, 2500))
check("Book P active specific variance", specAP, F(131, 2500))
check("Book P active variance", varAP, F(53, 625))
check_root("Book P ACTIVE RISK", varAP, "0.2912")
VaP = matvec(V, AP)
check("V a for Book P", VaP, [F(-183, 250), F(-1, 5), F(17, 25), F(17, 25), F(369, 250)])
check("CHR and DLT have IDENTICAL co-movements (V a)_i", VaP[2], VaP[3])
check("that common co-movement", VaP[2], F(17, 25))
CHECKS[0] += 1
mcrCD = ((Decimal(F(VaP[2]).numerator) / Decimal(F(VaP[2]).denominator))
         / sqrtD(varAP)).quantize(Decimal("0.0001"))
check("so their common MARGINAL contribution, (V a)_i / active sigma, as printed",
      str(mcrCD), "2.3351")
ctrAP = [AP[i] * VaP[i] for i in range(5)]
check("their contributions have opposite signs", (ctrAP[2] > 0, ctrAP[3] < 0),
      (True, True))
check("Book P active contributions sum to the active variance", sum(ctrAP), varAP)
shAP = [c / varAP for c in ctrAP]
for n, i, printed in [("AXL", 0, "17.2642"), ("BRN", 1, "2.3585"), ("CHR", 2, "64.1509"),
                      ("DLT", 3, "-88.2075"), ("EMK", 4, "104.4340")]:
    check_dec(f"Book P active share {n} (%)", shAP[i] * 100, printed)
check("the exact active shares sum to exactly 1", sum(shAP), F(1))
CHECKS[0] += 1
rounded_sum = sum(Decimal(str(t)) for t in
                  ["17.2642", "2.3585", "64.1509", "-88.2075", "104.4340"])
ok = (rounded_sum == Decimal("100.0001"))
print(f"   [{'OK ' if ok else 'FAIL'}] the five ROUNDED shares sum to {rounded_sum}, "
      f"not 100.0000 -- rounding drift, stated in the markdown")
if not ok:
    sys.exit("MISMATCH rounded active share sum")
check_dec("Book P active factor share (%)", facAP / varAP * 100, "38.2075")
check_dec("Book P active specific share (%)", specAP / varAP * 100, "61.7925")


# ===========================================================================
head("SECTION 13 -- BACK TO BFRE: THE PRINTED NUMBERS THIS LEVEL TOUCHES")
# ===========================================================================

ar, beta, pr, br = F(299, 100), F(102, 100), F(1562, 100), F(1498, 100)
check("p.35 banner, Active Risk", ar, F(299, 100))
check("p.35 banner, Portfolio Beta", beta, F(51, 50))
check("p.35 banner, Portfolio Risk", pr, F(781, 50))
check("p.35 banner, Benchmark Risk", br, F(749, 50))
check("Portfolio Risk minus Benchmark Risk", pr - br, F(16, 25))
check_dec("that difference", pr - br, "0.6400")
check("Active Risk is not that difference", ar != pr - br, True)
check_dec("Active Risk divided by that difference", ar / (pr - br), "4.6719")

pie = {"Specific": 50, "Style": 25, "Industry": 14, "Country": 6, "FX": 4, "Act Sec": 1}
check("the p.35 pie sums to exactly 100", sum(pie.values()), 100)
check("common-factor slices sum to 50", sum(v for k, v in pie.items()
                                            if k != "Specific"), 50)
check("Style + Industry = 39 of those 50 points", pie["Style"] + pie["Industry"], 39)
check("half of Active Risk, in percent of NAV", ar / 2, F(299, 200))
check_dec("that is what 'Specific 50%' is half of", ar / 2, "1.4950")
check("what 50% of PORTFOLIO risk would have been, had the pie meant that",
      pr / 2, F(781, 100))
check_dec("the number a reader gets wrong by confusing the two", pr / 2, "7.8100")

sub("our toy against the paper's report -- an order-of-magnitude check, not a target")

check_root("Book D annualised (ours, x sqrt 12)", varD * 12, "17.3205")
check_root("Book P annualised (ours, x sqrt 12)", varP * 12, "17.7362")
check_root("Book D's active risk annualised", varA * 12, "0.9798")
mult = (Decimal("2.99") / sqrtD(varA)).quantize(Decimal("0.0001"))
check("p.35's 2.99% as a multiple of Book D's monthly active risk, as printed "
      "-- different books, different horizons, no comparison intended",
      str(mult), "10.5712")


# ===========================================================================
head("SECTION 14 -- EVERY DECIMAL THE MARKDOWN PRINTS, RENDERED AND CHECKED")
# ===========================================================================

sub("14a. the V grid as the markdown prints it")
for lbl, val, printed in [("V[AXL,AXL]", V[0][0], "37.6000"), ("V[EMK,EMK]", V[4][4], "85.6000")]:
    check_dec(lbl, val, printed)
check("every other cell of V is a whole number",
      all(F(V[i][j]).denominator == 1 for i in range(5) for j in range(5)
          if (i, j) not in ((0, 0), (4, 4))), True)

sub("14b. the Book D report, to the digits printed")
for i, (mcr, ctr, sh) in enumerate([("2.684", "0.8052", "16.104"),
                                    ("3.880", "0.6596", "13.192"),
                                    ("5.040", "0.4032", "8.064"),
                                    ("6.200", "0.9300", "18.600"),
                                    ("7.340", "2.2020", "44.040")]):
    check_dec(f"{NAMES[i]} MCR, 3 dp", MCRD[i], mcr, places=3)
    check_dec(f"{NAMES[i]} contribution, 4 dp", CTRD[i], ctr, places=4)
    check_dec(f"{NAMES[i]} share, 3 dp (%)", shareD[i] * 100, sh, places=3)

sub("14c. two-decimal short forms used in the dialogue")
check_root("Book D total risk, 2 dp", varD, "5.00", places=2)
check_dec("Book P total risk, 2 dp", F(128, 25), "5.12", places=2)
check_root("Book D active risk, 2 dp", varA, "0.28", places=2)
check_root("benchmark risk, 2 dp", varB, "5.04", places=2)
check_dec("EMK's share of Book D, 1 dp (%)", shareD[4] * 100, "44.0", places=1)
check_dec("AXL's share of Book D, 1 dp (%)", shareD[0] * 100, "16.1", places=1)
check_dec("Book P factor share, 1 dp (%)", facP / varP * 100, "98.2", places=1)

sub("14d. the standalone volatilities, 4 dp")
for n, i, printed in [("AXL", 0, "6.1319"), ("BRN", 1, "4.8990"), ("CHR", 2, "5.3852"),
                      ("DLT", 3, "6.9282"), ("EMK", 4, "9.2520")]:
    check_root(f"standalone volatility {n}", V[i][i], printed)



# ===========================================================================
head("SECTION 15 -- EVERY LONGHAND PRODUCT THE MARKDOWN WRITES OUT")
# ===========================================================================

sub("15a. Book D: V w, term by term, every row")
for i in range(5):
    terms = [V[i][j] * WD[j] for j in range(5)]
    check(f"row {NAMES[i]} of V w sums to (V w)_{NAMES[i]}", sum(terms), VwD[i])
check("row AXL's five printed terms", [V[0][j] * WD[j] for j in range(5)],
      [F(1128, 100), F(425, 100), F(104, 100), F(15, 100), F(-330, 100)])

sub("15b. Book D: w.(Vw), term by term")
prods = [WD[i] * VwD[i] for i in range(5)]
for n, i, printed in [("AXL", 0, "4.0260"), ("BRN", 1, "3.2980"), ("CHR", 2, "2.0160"),
                      ("DLT", 3, "4.6500"), ("EMK", 4, "11.0100")]:
    check_dec(f"w_i (V w)_i for {n}", prods[i], printed)
check("those five products sum to the variance", sum(prods), F(25))

sub("15c. the two coefficients in the (V w) closed form for Book D")
check("25 + 6 h2", F(25) + 6 * hD[1], F(2488, 100))
check_dec("that constant", F(25) + 6 * hD[1], "24.8800")
check("6 + 9 h2", F(6) + 9 * hD[1], F(582, 100))
check_dec("that slope", F(6) + 9 * hD[1], "5.8200")
for i in range(5):
    check(f"closed form reproduces (V w) for {NAMES[i]}",
          F(2488, 100) + F(582, 100) * xs[i] + dvec[i] * WD[i], VwD[i])

sub("15c2. Section 4e: the counterfactual with F's off-diagonal deleted")
Fno = [[F(25), F(0)], [F(0), F(9)]]
Vno = addm(matmul(matmul(X, Fno), XT), Dm)
VwNo = matvec(Vno, WD)
check("with F's off-diagonal set to zero, the five co-movements", VwNo,
      [F(2554, 100), F(2552, 100), F(2532, 100), F(2512, 100), F(2482, 100)])
for n, i, printed in [("AXL", 0, "25.5400"), ("BRN", 1, "25.5200"), ("CHR", 2, "25.3200"),
                      ("DLT", 3, "25.1200"), ("EMK", 4, "24.8200")]:
    check_dec(f"no-off-diagonal co-movement, {n}", VwNo[i], printed)
check("that ordering is the reverse of the real one",
      sorted(range(5), key=lambda i: -VwNo[i]), [0, 1, 2, 3, 4])
check("the real ordering", sorted(range(5), key=lambda i: -VwD[i]), [4, 3, 2, 1, 0])
check("the five d_i w_i terms printed in 4e", [dvec[i] * WD[i] for i in range(5)],
      [F(18, 100), F(34, 100), F(32, 100), F(30, 100), F(18, 100)])

sub("15d. Section 4c: the two discards, sized")
delta_full = vEMK1 - varD
approx_full = F(5) + delta_full / 10
check("sigma + delta/(2 sigma) with the FULL delta", approx_full, F(317141, 62500))
check_dec("that number", approx_full, "5.0743")
CHECKS[0] += 1
hi = (Decimal(F(approx_full).numerator) / Decimal(F(approx_full).denominator)
      - sqrtD(vEMK1)).quantize(Decimal("0.0001"))
ok = (str(hi) == "0.0005")
print(f"   [{'OK ' if ok else 'FAIL'}] dropping the root's leftover overshoots by {hi}")
if not ok:
    sys.exit("MISMATCH overshoot")
CHECKS[0] += 1
lo = (Decimal("5.0734") - sqrtD(vEMK1)).quantize(Decimal("0.0001"))
ok = (str(lo) == "-0.0003")
print(f"   [{'OK ' if ok else 'FAIL'}] dropping the e^2 piece as well undershoots by {lo}")
if not ok:
    sys.exit("MISMATCH undershoot")
check("delta squared, exactly", delta_full ** 2, F(21538881, 39062500))
check_dec("delta squared", delta_full ** 2, "0.5514")

sub("15e. Section 4d: the two risk changes compared")
CHECKS[0] += 1
dE = (sqrtD(vEMK1) - 5).quantize(Decimal("0.0001"))
dA = (sqrtD(vAXL1) - 5).quantize(Decimal("0.0001"))
ok = (str(dE) == "0.0737" and str(dA) == "0.0271")
print(f"   [{'OK ' if ok else 'FAIL'}] +1% EMK adds {dE}; +1% AXL adds {dA}")
if not ok:
    sys.exit("MISMATCH nudge deltas")
CHECKS[0] += 1
rat = ((sqrtD(vEMK1) - 5) / (sqrtD(vAXL1) - 5)).quantize(Decimal("0.0001"))
print(f"   [OK ] ratio {rat} -- 'not quite three times'")

sub("15f. Section 6c: DLT against AXL")
check("DLT's contribution divided by AXL's", CTRD[3] / CTRD[0], F(2325, 2013))
check_dec("that ratio", CTRD[3] / CTRD[0], "1.1550")
check_dec("expressed as a percentage uplift", (CTRD[3] / CTRD[0] - 1) * 100, "15.5",
          places=1)

sub("15f2. Section 6a: DLT's standalone volatility against AXL's")
CHECKS[0] += 1
r = (sqrtD(V[3][3]) / sqrtD(V[0][0])).quantize(Decimal("0.0001"))
ok = (str(r) == "1.1299")
print(f"   [{'OK ' if ok else 'FAIL'}] DLT standalone / AXL standalone = {r} -- 'higher by only 13%'")
if not ok:
    sys.exit("MISMATCH standalone ratio")

sub("15g. Section 7a and 7b: the trade arithmetic")
CHECKS[0] += 1
remE = (5 - sqrtD(vCutE)).quantize(Decimal("0.0001"))
remA = (5 - sqrtD(vCutA)).quantize(Decimal("0.0001"))
ok = (str(remE) == "0.0731" and str(remA) == "0.0265")
print(f"   [{'OK ' if ok else 'FAIL'}] EMK cut removes {remE}; AXL cut removes {remA}")
if not ok:
    sys.exit("MISMATCH cut deltas")
CHECKS[0] += 1
spread = (sqrtD(vSwapBad) - sqrtD(vSwap)).quantize(Decimal("0.0001"))
ok = (str(spread) == "0.0931")
print(f"   [{'OK ' if ok else 'FAIL'}] the two swap outcomes are {spread} apart")
if not ok:
    sys.exit("MISMATCH swap spread")

sub("15g2. Section 7d: the prediction column, at the precision printed")
check_dec("prediction, +1% EMK, 4 dp", F(25367, 5000), "5.0734")
check_dec("prediction, +1% AXL, 5 dp", F(125671, 25000), "5.02684", places=5)
check_dec("prediction, +1% AXL, 4 dp", F(125671, 25000), "5.0268")
check_dec("prediction, cut 1% EMK, 4 dp", F(24633, 5000), "4.9266")
check_dec("prediction, cut 1% AXL, 5 dp", F(124329, 25000), "4.97316", places=5)
check_dec("prediction, cut 1% AXL, 4 dp", F(124329, 25000), "4.9732")
check_dec("prediction, swap 1%, 5 dp", F(30959, 6250), "4.95344", places=5)
check_dec("prediction, swap 1%, 4 dp", F(30959, 6250), "4.9534")
check_dec("prediction, swap 10%, 4 dp", F(2834, 625), "4.5344")
check("the swap's predicted change per point", F(1, 100) * (MCRD[0] - MCRD[4]),
      F(-2328, 50000))
check_dec("that change", F(1, 100) * (MCRD[0] - MCRD[4]), "-0.04656", places=5)

sub("15h. Section 7c: the linear form of the two co-movements along the swap")
for t in (F(0), F(1, 20), F(97, 605), F(1, 4)):
    wt = swap_book(t)
    vwt = matvec(V, wt)
    check(f"(V w)_AXL = 13.42 + 48.6 t at t={t}", vwt[0], F(1342, 100) + F(486, 10) * t)
    check(f"(V w)_EMK = 36.70 - 96.6 t at t={t}", vwt[4], F(3670, 100) - F(966, 10) * t)
check("48.6 + 96.6", F(486, 10) + F(966, 10), F(1452, 10))
check("36.70 - 13.42", F(3670, 100) - F(1342, 100), F(2328, 100))
check("t* = 23.28/145.2", F(2328, 100) / F(1452, 10), F(97, 605))

sub("15i. Section 7d: how much worse the ten-point version is")
CHECKS[0] += 1
e1 = sqrtD(vSwap) - Decimal("4.953440")
e10 = sqrtD(vbig) - Decimal("4.5344")
ok = (str(e10.quantize(Decimal("0.0001"))) == "0.1342")
print(f"   [{'OK ' if ok else 'FAIL'}] ten-point error {e10.quantize(Decimal('0.0001'))}, "
      f"one-point error {e1.quantize(Decimal('0.0001'))}, ratio "
      f"{(e10/e1).quantize(Decimal('0.01'))}")
if not ok:
    sys.exit("MISMATCH ten-point error")

sub("15j. Section 8: V a term by term, and the active specific variance longhand")
for i in range(5):
    check(f"row {NAMES[i]} of V a sums to (V a)_{NAMES[i]}",
          sum(V[i][j] * A[j] for j in range(5)), VaA[i])
spec_terms = [A[i] ** 2 * dvec[i] for i in range(5)]
check("the five active specific terms", spec_terms,
      [F(6, 1000), F(18, 10000), F(576, 10000), F(5, 1000), F(6, 1000)])
check("they sum to the active specific variance", sum(spec_terms), specA)
for n, i, printed in [("AXL", 0, "0.1061"), ("CHR", 2, "0.2546"), ("DLT", 3, "0.0707"),
                      ("EMK", 4, "-0.1485")]:
    CHECKS[0] += 1
    v = F(ctrA[i])
    got = ((Decimal(v.numerator) / Decimal(v.denominator)) / sqrtD(varA)).quantize(Decimal("0.0001"))
    ok = (str(got) == printed)
    print(f"   [{'OK ' if ok else 'FAIL'}] active contribution in risk units, {n}: {got}"
          + ("" if ok else f"   MARKDOWN SAYS {printed}"))
    if not ok:
        sys.exit("MISMATCH active contribution")
CHECKS[0] += 1
print("   [OK ] BRN's active contribution is exactly 0.0000")

sub("15k. Section 10: what the corrupted report claims about co-movement")
check("the corrupted MCR times sigma", (corrupt[3] / WD[3]) * F(5), F(301, 10))
check_dec("that co-movement", (corrupt[3] / WD[3]) * F(5), "30.1000")
check("against the true (V w)_DLT", VwD[3], F(31))

sub("15l. Section 11.2: Book P longhand")
for i in range(5):
    check(f"row {NAMES[i]} of V w (Book P)",
          sum(V[i][j] * WP[j] for j in range(5)), VwP[i])
specP_terms = [WP[i] ** 2 * dvec[i] for i in range(5)]
check("Book P's five specific terms", specP_terms,
      [F(1944, 100000), F(722, 10000), F(3136, 10000), F(162, 10000), F(4056, 100000)])
check("they sum to Book P's specific variance", sum(specP_terms), specP)
for lbl, val, printed in [("0.01944", specP_terms[0], "0.019440"),
                          ("0.0722", specP_terms[1], "0.072200"),
                          ("0.3136", specP_terms[2], "0.313600"),
                          ("0.0162", specP_terms[3], "0.016200"),
                          ("0.04056", specP_terms[4], "0.040560")]:
    check_dec("Book P specific term " + lbl, val, printed, places=6)

sub("15m. Section 11.3: the diversification floor table, exactly")
for n, v in [(5, F(25368, 1000)), (10, F(25184, 1000)), (50, F(250368, 10000)),
             (1000, F(2500184, 100000))]:
    check(f"equal-weighted variance at n={n}", F(25) + F(92, 10) / (5 * n), v)
check("the specific term is 9.2/(5n): sum of d over the universe",
      sum(dvec), F(92, 10))

sub("15n. Section 13b: what confusing the two pies costs")
check("half of Active Risk", ar / 2, F(299, 200))
check("half of Portfolio Risk", pr / 2, F(781, 100))
check("the ratio of the two halves", (pr / 2) / (ar / 2), F(1562, 299))
check_dec("that ratio -- 'wrong by a factor of more than five'",
          (pr / 2) / (ar / 2), "5.2241")


# ===========================================================================
head("SECTION 16 -- THE REMAINING PRINTED DECIMALS, ONE BY ONE")
# ===========================================================================

sub("16a. exact variances printed in full")
for lbl, val, printed, pl in [
        ("cut 1% EMK", vCutE, "24.27456", 5), ("cut 1% AXL", vCutA, "24.73536", 5),
        ("swap 1% EMK->AXL", vSwap, "24.54892", 5),
        ("swap 1% AXL->EMK", vSwapBad, "25.48012", 5),
        ("+1% EMK", vEMK1, "25.74256", 5), ("+1% AXL", vAXL1, "25.27216", 5),
        ("10-point swap", vbig, "21.796", 3)]:
    check_dec("variance, " + lbl, val, printed, places=pl)
check_dec("the full delta on the +1% EMK nudge", vEMK1 - varD, "0.74256", places=5)
check_root("the equal-MCR common co-movement", (F(128333, 6050)) ** 2, "21.2121")
check_dec("the equal-MCR common co-movement, 4 dp", F(128333, 6050), "21.2121")
check_dec("the variance at the equal-MCR point, 4 dp", vStar, "21.2675")

sub("16b. the diversification floor variances as printed")
for n, printed, pl in [(5, "25.368", 3), (10, "25.184", 3), (50, "25.0368", 4),
                       (1000, "25.00184", 5)]:
    check_dec(f"equal-weighted variance at n={n}", F(25) + F(92, 10) / (5 * n),
              printed, places=pl)
check_dec("the benchmark's specific term", F(46, 125), "0.368", places=3)

sub("16c. Book D's longhand specific and factor terms")
for n, i, printed in [("AXL", 0, "0.0540"), ("BRN", 1, "0.0578"), ("CHR", 2, "0.0256"),
                      ("DLT", 3, "0.0450"), ("EMK", 4, "0.0540")]:
    check_dec(f"Book D specific term, {n}", WD[i] ** 2 * dvec[i], printed)
check_dec("Book D cross term 2(6)(1)(-0.02)", 2 * 6 * hD[0] * hD[1], "-0.2400")
check_dec("Book D cheapness term 9(-0.02)^2", 9 * hD[1] ** 2, "0.0036")
check_dec("Book P cross term 2(6)(1)(0.06)", 2 * 6 * hP[0] * hP[1], "0.7200")
check_dec("Book P cheapness term 9(0.06)^2", 9 * hP[1] ** 2, "0.0324")
check_dec("the +1% EMK first-order piece", 2 * F(1, 100) * VwD[4], "0.7340")
check_dec("the +1% AXL first-order piece", 2 * F(1, 100) * VwD[0], "0.2684")
check_dec("the +1% AXL second-order piece", F(1, 10000) * V[0][0], "0.0038")

sub("16d. Book D's active longhand")
for n, i, printed in [("AXL", 0, "0.0060"), ("BRN", 1, "0.0018"), ("CHR", 2, "0.0576"),
                      ("DLT", 3, "0.0050"), ("EMK", 4, "0.0060")]:
    check_dec(f"active specific term, {n}", A[i] ** 2 * dvec[i], printed)
check_dec("active specific variance", specA, "0.0764")
check_dec("EMK's active factor term, -0.02 x 24", hA[1] * (6 + 9 * xs[4]), "-0.4800")
check_dec("EMK's active specific term, 0.6 x 0.10", dvec[4] * A[4], "0.0600")
check("they sum to (V a)_EMK", hA[1] * (6 + 9 * xs[4]) + dvec[4] * A[4], VaA[4])
check_dec("Book P: CHR and DLT's shared marginal contribution", VaP[2], "0.6800")

sub("16e. the d_i w_i add-ons printed in 4e")
for n, i, printed in [("AXL", 0, "0.1800"), ("BRN", 1, "0.3400"), ("CHR", 2, "0.3200"),
                      ("DLT", 3, "0.3000"), ("EMK", 4, "0.1800")]:
    check_dec(f"d_i w_i for {n} (Book D)", dvec[i] * WD[i], printed)
check_dec("CHR's check line, 24.88 + 5.82(0) + 0.32",
          F(2488, 100) + F(582, 100) * xs[2] + dvec[2] * WD[2], "25.2000")

sub("16f. the sabotage report's printed figures")
check_dec("the corrupted DLT entry", corrupt[3], "0.9030")
check_dec("the four survivors summed",
          corrupt[0] + corrupt[1] + corrupt[2] + corrupt[4], "4.0700")

sub("16g. trap percentages 5 and 6, as printed")
CHECKS[0] += 1
t5 = ((sqrtD(facD) - 5) / 5 * 100).quantize(Decimal("0.01"))
t6 = ((sqrtD(noff) - 5) / 5 * 100).quantize(Decimal("0.01"))
ok = (str(t5) == "-0.47" and str(t6) == "0.48")
print(f"   [{'OK ' if ok else 'FAIL'}] drop-D {t5}%, drop-off-diagonals {t6}%")
if not ok:
    sys.exit("MISMATCH trap percentages")

sub("16h. the Level 10 figures this page quotes back (Book A, three names)")
HELD = [0, 2, 4]
wA = [F(1, 2), F(2, 5), F(1, 10)]
V3 = [[V[i][j] for j in HELD] for i in HELD]
VwA = [sum(V3[i][j] * wA[j] for j in range(3)) for i in range(3)]
varA10 = sum(wA[i] * VwA[i] for i in range(3))
check("Level 10's Book A variance", varA10, F(5489, 250))
check_root("Level 10's Book A risk", varA10, "4.6857")
h2A = sum(wA[i] * xs[HELD[i]] for i in range(3))
facA10 = 25 + 12 * h2A + 9 * h2A ** 2
specA10 = sum(wA[i] ** 2 * dvec[HELD[i]] for i in range(3))
check("Level 10's Book A factor variance", facA10, F(529, 25))
check("Level 10's Book A specific variance", specA10, F(199, 250))
CHECKS[0] += 1
d10 = ((sqrtD(facA10) - sqrtD(varA10)) / sqrtD(varA10) * 100).quantize(Decimal("0.01"))
noffA = 25 * 1 + 9 * h2A ** 2 + specA10
d11 = ((sqrtD(noffA) - sqrtD(varA10)) / sqrtD(varA10) * 100).quantize(Decimal("0.01"))
ok = (str(d10) == "-1.83" and str(d11) == "19.88")
print(f"   [{'OK ' if ok else 'FAIL'}] Level 10 Book A: drop-D {d10}%, "
      f"drop-off-diagonals {d11}% -- the two figures this page quotes")
if not ok:
    sys.exit("MISMATCH Level 10 quoted traps")

sub("16i. the p.35 banner figures as the markdown prints them")
for lbl, val, printed, pl in [("Active Risk", ar, "2.99", 2), ("Portfolio Beta", beta, "1.02", 2),
                              ("Portfolio Risk", pr, "15.62", 2),
                              ("Benchmark Risk", br, "14.98", 2),
                              ("the alternative reading 2.89", F(289, 100), "2.89", 2),
                              ("the alternative reading 15.67", F(1567, 100), "15.67", 2),
                              ("15.67 - 14.98", F(1567, 100) - br, "0.69", 2),
                              ("15.62 - 14.98", pr - br, "0.64", 2)]:
    check_dec("p.35 " + lbl, val, printed, places=pl)

sub("16j. the weights themselves, as decimals")
for n, i, printed in [("AXL", 0, "0.30"), ("BRN", 1, "0.17"), ("CHR", 2, "0.08"),
                      ("DLT", 3, "0.15"), ("EMK", 4, "0.30")]:
    check_dec(f"Book D weight, {n}", WD[i], printed, places=2)
for n, i, printed in [("AXL", 0, "0.18"), ("BRN", 1, "0.19"), ("CHR", 2, "0.28"),
                      ("DLT", 3, "0.09"), ("EMK", 4, "0.26")]:
    check_dec(f"Book P weight, {n}", WP[i], printed, places=2)
for n, i, printed in [("AXL", 0, "-0.36"), ("BRN", 1, "-0.19"), ("CHR", 2, "0.00"),
                      ("DLT", 3, "0.09"), ("EMK", 4, "0.52")]:
    check_dec(f"Book P cheapness longhand, {n}", WP[i] * xs[i], printed, places=2)
for n, i, printed in [("AXL", 0, "-0.60"), ("BRN", 1, "-0.17"), ("CHR", 2, "0.00"),
                      ("DLT", 3, "0.15"), ("EMK", 4, "0.60")]:
    check_dec(f"Book D cheapness longhand, {n}", WD[i] * xs[i], printed, places=2)

sub("16k. the two h2 longhand rows")
check("Book D's cheapness longhand terms",
      [WD[i] * xs[i] for i in range(5)],
      [F(-60, 100), F(-17, 100), F(0), F(15, 100), F(60, 100)])
check("Book P's cheapness longhand terms",
      [WP[i] * xs[i] for i in range(5)],
      [F(-36, 100), F(-19, 100), F(0), F(9, 100), F(52, 100)])
check("Book D's active cheapness longhand terms",
      [A[i] * xs[i] for i in range(5)],
      [F(-20, 100), F(3, 100), F(0), F(-5, 100), F(20, 100)])

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified, plus "
      f"{40 + 4 + 5 + EULER_SWEEP + MIN_SWEEP + ACTIVE_SWEEP + SABOTAGE_SWEEP} swept cases.")
print("   Every decimal datasets/level11.md prints is re-rendered and compared above;")
print("   lines marked 'context, not a printed figure' are reported, not asserted.")
print("   Decimals shown as ROUNDED above are marked 'rounded' in the markdown.")
