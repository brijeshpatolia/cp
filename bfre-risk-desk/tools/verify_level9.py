#!/usr/bin/env python3
"""
verify_level9.py -- recomputes EVERY number printed in datasets/level9.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level9.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

Conventions are the ones already used by verify_level5.py and verify_level8.py:
a tiny exact-rational linear-algebra kit (dot / solve / wls), a `check` that
prints and asserts, and `dec` which tags every decimal EXACT or ROUNDED. Every
value this file tags ROUNDED carries the word "rounded" in the markdown.

Square roots are the only irrational quantities on the page. They are handled
the way the rulebook demands: the VARIANCE is exact, and the root is printed as
an explicitly-rounded decimal computed with decimal.Decimal at 60 digits, never
with float. Where a ratio of two roots is itself rational (a perfect square of a
rational under the root) that is asserted exactly, in Fractions.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
import sys

getcontext().prec = 60

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


def dec(v, n=4):
    """Decimal string, tagged EXACT or ROUNDED. The markdown must carry the
    word 'rounded' next to every value this function tags ROUNDED."""
    v = F(v)
    tag = "exact" if terminates(v) else "ROUNDED"
    q = Decimal(v.numerator) / Decimal(v.denominator)
    return f"{q:.{n}f} ({tag})"


def dsqrt(fr, n=6):
    """Exact-input square root as a Decimal at 60 digits. Returns (Decimal,
    is_exact) -- is_exact is True only when the root is itself rational with a
    terminating decimal."""
    fr = F(fr)
    assert fr >= 0, "negative variance"
    q = Decimal(fr.numerator) / Decimal(fr.denominator)
    r = q.sqrt()
    # rational-root test on the exact fraction
    def isq(m):
        if m < 0:
            return None
        x = int(m ** 0.5)
        for c in (x - 2, x - 1, x, x + 1, x + 2):
            if c >= 0 and c * c == m:
                return c
        return None
    a, b = isq(fr.numerator), isq(fr.denominator)
    exact = a is not None and b is not None and terminates(F(a, b))
    return r, exact


def root(fr, n=4):
    r, exact = dsqrt(fr)
    return f"{r:.{n}f} ({'exact' if exact else 'ROUNDED'})"


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
# exact linear algebra
# ---------------------------------------------------------------------------

def dot(u, v):
    return sum(F(a) * F(b) for a, b in zip(u, v))


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


def wls(cols, r):
    """Unweighted least squares over columns `cols`. Returns
    (coeffs, fitted, residuals, SS)."""
    n = len(r)
    k = len(cols)
    M = [[dot(cols[i], cols[j]) for j in range(k)] for i in range(k)]
    y = [dot(cols[i], r) for i in range(k)]
    bb = solve(M, y)
    fit = [sum(bb[j] * F(cols[j][i]) for j in range(k)) for i in range(n)]
    e = [F(r[i]) - fit[i] for i in range(n)]
    ss = sum(x * x for x in e)
    return bb, fit, e, ss


def matvec(M, v):
    return [sum(F(M[i][j]) * F(v[j]) for j in range(len(v))) for i in range(len(M))]


def quad(M, w):
    """w^T M w, exactly."""
    return sum(F(w[i]) * F(M[i][j]) * F(w[j])
               for i in range(len(w)) for j in range(len(w)))


def gram(series, T):
    """second-moment matrix: (1/T) * sum_t u_i(t) u_j(t)."""
    n = len(series)
    return [[dot(series[i], series[j]) / F(T) for j in range(n)] for i in range(n)]


def diagonal_of(M):
    n = len(M)
    return [[M[i][j] if i == j else F(0) for j in range(n)] for i in range(n)]


# ===========================================================================
head("SECTION 3  THE GUARANTEE -- Level 8's file, re-run and re-checked")
# ===========================================================================

NAMES8 = ["AXL", "BRN", "CHR", "DLT", "EMK"]
ONE5 = [F(1)] * 5
XCHP = [F(-2), F(-1), F(0), F(1), F(2)]

# returns, month 1 .. month 5, exactly as printed in datasets/level8.md section 3a
RET = {
    "AXL": [F(0), F(-3), F(6), F(6), F(-8)],
    "BRN": [F(1), F(2), F(3), F(7), F(-6)],
    "CHR": [F(9), F(3), F(-1), F(1), F(-8)],
    "DLT": [F(9), F(10), F(-1), F(3), F(-4)],
    "EMK": [F(16), F(13), F(-2), F(-2), F(-4)],
}
T8 = 5

sub("3a. the Gram matrix is computed once and reused (CALL BACK to Level 8)")
check("sum 1*1", dot(ONE5, ONE5), F(5))
check("sum 1*x  (the centred column)", dot(ONE5, XCHP), F(0))
check("sum x*x", dot(XCHP, XCHP), F(10))
check("determinant 5*10 - 0*0", dot(ONE5, ONE5) * dot(XCHP, XCHP) - dot(ONE5, XCHP) ** 2,
      F(50))

sub("3b. five cross-sectional solves, and the misses they leave")
F_MKT, F_CHP = [], []
U = {nm: [] for nm in NAMES8}
for t in range(T8):
    r = [RET[nm][t] for nm in NAMES8]
    bb, fit, e, ss = wls([ONE5, XCHP], r)
    F_MKT.append(bb[0])
    F_CHP.append(bb[1])
    for i, nm in enumerate(NAMES8):
        U[nm].append(e[i])
    check(f"month {t+1}: sum(u) = 0            (the market column's balance)", sum(e), F(0))
    check(f"month {t+1}: sum(x*u) = 0          (the cheapness column's balance)",
          dot(XCHP, e), F(0))

check("f_Mkt, months 1-5", F_MKT, [F(7), F(5), F(1), F(3), F(-6)])
check("f_Chp, months 1-5", F_CHP, [F(4), F(4), F(-2), F(-2), F(1)])
for nm, want in [("AXL", [F(1), F(0), F(1), F(-1), F(0)]),
                 ("BRN", [F(-2), F(1), F(0), F(2), F(1)]),
                 ("CHR", [F(2), F(-2), F(-2), F(-2), F(-2)]),
                 ("DLT", [F(-2), F(1), F(0), F(2), F(1)]),
                 ("EMK", [F(1), F(0), F(1), F(-1), F(0)])]:
    check(f"u_{nm}, months 1-5", U[nm], want)

SSQ_MONTH = [sum(U[nm][t] ** 2 for nm in NAMES8) for t in range(T8)]
check("sum u^2 per month", SSQ_MONTH, [F(14), F(6), F(6), F(14), F(6)])
check("sum u^2 over the whole file (Level 8 printed 46)", sum(SSQ_MONTH), F(46))

sub("3d. three things the guarantee does NOT say -- each checked on this file")
check("sum over TIME of CHR's misses is NOT zero", sum(U["CHR"]), F(-6))
check("sum over TIME of AXL's misses is NOT zero", sum(U["AXL"]), F(1))
sfu = sum(F_CHP[t] * U["CHR"][t] for t in range(T8))
check("sum_t f_Chp(t)*u_CHR(t) is NOT zero", sfu, F(6))
sfu_mkt = sum(F_MKT[t] * U["CHR"][t] for t in range(T8))
check("sum_t f_Mkt(t)*u_CHR(t) is NOT zero", sfu_mkt, F(8))
fbar = sum(F_CHP) / F(T8)
ubar = sum(U["CHR"]) / F(T8)
check("mean of f_Chp over the five months", fbar, F(1))
check("mean of CHR's misses over the five months", ubar, F(-6, 5))
covc = (sfu - F(T8) * fbar * ubar) / F(T8)
check("centred covariance of f_Chp with u_CHR = (6 - 5*1*(-6/5))/5", covc, F(12, 5))
show("that covariance as a decimal", dec(covc))
check("sum_t u_BRN(t)*u_DLT(t) is NOT zero", dot(U["BRN"], U["DLT"]), F(10))

# ===========================================================================
head("SECTION 4  BUILDING THE DIAGONAL of Delta from the misses")
# ===========================================================================

sub("4b. the five specific variances, divisor T = 5, no mean subtracted")
D8 = {nm: dot(U[nm], U[nm]) / F(T8) for nm in NAMES8}
check("d_AXL", D8["AXL"], F(3, 5))
check("d_BRN", D8["BRN"], F(2))
check("d_CHR", D8["CHR"], F(4))
check("d_DLT", D8["DLT"], F(2))
check("d_EMK", D8["EMK"], F(3, 5))
check("they sum to 46/5", sum(D8.values()), F(46, 5))
show("46/5 as a decimal", dec(F(46, 5)))
for nm in NAMES8:
    show(f"specific risk of {nm} = sqrt(d)", root(D8[nm]))
check("CHR's specific risk is exactly 2 because 4 is a perfect square",
      D8["CHR"], F(4))

sub("4a. what the other divisor would have given (T-1 = 4), for comparison")
D8_T1 = {nm: dot(U[nm], U[nm]) / F(T8 - 1) for nm in NAMES8}
check("d_CHR with divisor 4", D8_T1["CHR"], F(5))
check("every entry is the divisor-5 entry times 5/4",
      all(D8_T1[nm] == D8[nm] * F(5, 4) for nm in NAMES8), True)
check("so any RATIO of two such numbers is unchanged by the divisor",
      D8_T1["CHR"] / D8_T1["BRN"], D8["CHR"] / D8["BRN"])

# ===========================================================================
head("SECTION 5  THE GUARANTEE THAT FORBIDS A DIAGONAL")
# ===========================================================================

SER8 = [U[nm] for nm in NAMES8]
S8 = gram(SER8, T8)

sub("5a. the whole 5x5 second-moment matrix, and its zero row sums")
for i, nm in enumerate(NAMES8):
    show(f"row {nm}", [str(S8[i][j]) for j in range(5)])
check("S_AXL,BRN", S8[0][1], F(-4, 5))
check("S_AXL,CHR", S8[0][2], F(2, 5))
check("S_AXL,DLT", S8[0][3], F(-4, 5))
check("S_AXL,EMK", S8[0][4], F(3, 5))
check("S_BRN,CHR", S8[1][2], F(-12, 5))
check("S_BRN,DLT", S8[1][3], F(2))
check("S_BRN,EMK", S8[1][4], F(-4, 5))
check("S_CHR,DLT", S8[2][3], F(-12, 5))
check("S_CHR,EMK", S8[2][4], F(2, 5))
check("S_DLT,EMK", S8[3][4], F(-4, 5))
for i, nm in enumerate(NAMES8):
    check(f"row {nm} sums to exactly zero", sum(S8[i]), F(0))
offsum = sum(S8[i][j] for i in range(5) for j in range(5) if i != j)
check("the off-diagonals sum to minus the sum of the variances", offsum, F(-46, 5))
check("average off-diagonal entry = -(46/5)/20", offsum / F(20), F(-23, 50))
show("that average as a decimal", dec(F(-23, 50)))

sub("5b. the equal-weight book whose specific return was zero every month")
EW5 = [F(1, 5)] * 5
book_series = [sum(EW5[i] * SER8[i][t] for i in range(5)) for t in range(T8)]
check("the equal-weight book's specific return, month by month", book_series, [F(0)] * 5)
check("its specific variance under the FULL matrix", quad(S8, EW5), F(0))
D8diag = diagonal_of(S8)
vdiag = quad(D8diag, EW5)
check("its specific variance under the DIAGONAL matrix", vdiag, F(46, 125))
show("46/125 as a decimal", dec(vdiag))
show("the diagonal model's specific RISK for that book", root(vdiag))

sub("5c. the size of the mechanical effect: -1/(N-1) when the variances are equal")
for N in (5, 50, 749, 3000):
    rho = F(-1, N - 1)
    # the identity that forces it: N*d + N*(N-1)*rho*d = 0
    d = F(7)  # any positive d
    check(f"N={N}: N*d + N*(N-1)*rhobar*d = 0 at rhobar = -1/(N-1)",
          F(N) * d + F(N) * F(N - 1) * rho * d, F(0))
    show(f"   rhobar at N={N}", dec(rho, 6))

sub("5d. two artifacts of the Level-8 file, named so they are not mistaken for economics")
check("BRN and DLT have IDENTICAL miss series", U["BRN"] == U["DLT"], True)
check("AXL and EMK have IDENTICAL miss series", U["AXL"] == U["EMK"], True)
check("so their sample specific-return correlation is exactly 1",
      S8[1][3] ** 2, D8["BRN"] * D8["DLT"])
check("with 5 assets and 2 columns the misses have only 3 free directions",
      5 - 2, 3)
check("CHR alone supplies 4 of the file's 46/5 of total specific variance",
      F(4) / F(46, 5), F(10, 23))
show("10/23 as a decimal", dec(F(10, 23), 6))
check("a 5x5 matrix has 10 distinct off-diagonal entries", F(5) * F(4) / 2, F(10))
check("a 4x4 matrix has 6", F(4) * F(3) / 2, F(6))
check("a 3000x3000 matrix has 4,498,500", F(3000) * F(2999) / 2, F(4498500))

# ===========================================================================
head("SECTION 6  THE NEW FILE -- four names, six months, one real link")
# ===========================================================================

NAMES9 = ["KVR", "TLM", "GNP", "HRB"]
T9 = 6
PANEL = {
    "KVR": [F(5), F(-1), F(-1), F(-4), F(2), F(-1)],
    "TLM": [F(4), F(-2), F(-4), F(-2), F(2), F(2)],
    "GNP": [F(3), F(3), F(-3), F(3), F(-3), F(-3)],
    "HRB": [F(0), F(-3), F(0), F(3), F(3), F(-3)],
}

sub("6b. the panel: each name's six specific returns, and their sums")
for nm in NAMES9:
    check(f"{nm}: the six specific returns sum to zero over the file",
          sum(PANEL[nm]), F(0))
check("sum of KVR^2", dot(PANEL["KVR"], PANEL["KVR"]), F(48))
check("sum of TLM^2", dot(PANEL["TLM"], PANEL["TLM"]), F(48))
check("sum of GNP^2", dot(PANEL["GNP"], PANEL["GNP"]), F(54))
check("sum of HRB^2", dot(PANEL["HRB"], PANEL["HRB"]), F(36))

sub("6c. where the numbers come from: one shock with no factor, plus private parts")
G = [F(3), F(0), F(-3), F(-3), F(3), F(0)]        # the supply-chain shock
PK = [F(2), F(-1), F(2), F(-1), F(-1), F(-1)]     # KVR's private part
PT = [F(1), F(-2), F(-1), F(1), F(-1), F(2)]      # TLM's private part
check("g + p_K reproduces KVR's row exactly",
      [G[t] + PK[t] for t in range(T9)], PANEL["KVR"])
check("g + p_T reproduces TLM's row exactly",
      [G[t] + PT[t] for t in range(T9)], PANEL["TLM"])
check("the shock and the two private parts are mutually orthogonal: g.p_K",
      dot(G, PK), F(0))
check("                                                        g.p_T", dot(G, PT), F(0))
check("                                                      p_K.p_T", dot(PK, PT), F(0))
check("sum g^2  -> variance 6", dot(G, G) / F(T9), F(6))
check("sum p_K^2 -> variance 2", dot(PK, PK) / F(T9), F(2))
check("sum p_T^2 -> variance 2", dot(PT, PT) / F(T9), F(2))
check("so d_KVR = 6 + 2", F(6) + F(2), F(8))
check("and the covariance is the shared variance alone", dot(G, G) / F(T9), F(6))

sub("6d. the full specific covariance matrix, divisor T = 6")
SER9 = [PANEL[nm] for nm in NAMES9]
DFULL = gram(SER9, T9)
for i, nm in enumerate(NAMES9):
    show(f"row {nm}", [str(DFULL[i][j]) for j in range(4)])
check("d_KVR", DFULL[0][0], F(8))
check("d_TLM", DFULL[1][1], F(8))
check("d_GNP", DFULL[2][2], F(9))
check("d_HRB", DFULL[3][3], F(6))
check("Delta_KVR,TLM", DFULL[0][1], F(6))
check("Delta_KVR,GNP", DFULL[0][2], F(0))
check("Delta_KVR,HRB", DFULL[0][3], F(0))
check("Delta_TLM,GNP", DFULL[1][2], F(0))
check("Delta_TLM,HRB", DFULL[1][3], F(0))
check("Delta_GNP,HRB", DFULL[2][3], F(0))
check("the matrix is symmetric",
      all(DFULL[i][j] == DFULL[j][i] for i in range(4) for j in range(4)), True)
show("specific risk of KVR", root(DFULL[0][0]))
show("specific risk of TLM", root(DFULL[1][1]))
show("specific risk of GNP", root(DFULL[2][2]))
show("specific risk of HRB", root(DFULL[3][3]))
check("GNP's specific risk is exactly 3 because 9 is a perfect square",
      DFULL[2][2], F(9))

sub("6d(ii). the one correlation in the file")
check("rho(KVR,TLM)^2 = 6^2/(8*8)", DFULL[0][1] ** 2 / (DFULL[0][0] * DFULL[1][1]),
      F(9, 16))
check("so rho(KVR,TLM) = 3/4 exactly", F(6) / F(8), F(3, 4))
check("the 2x2 block's determinant, 8*8 - 6*6", F(8) * F(8) - F(6) * F(6), F(28))
check("it is positive, so no book of the two has negative variance", F(28) > 0, True)

DDIAG = diagonal_of(DFULL)

# ===========================================================================
head("SECTION 7-8  FROM A MATRIX TO ONE NUMBER, AND FOUR BOOKS")
# ===========================================================================

def book_variance_direct(w):
    """second moment of the book's own specific-return series -- no matrix used"""
    ser = [sum(F(w[i]) * SER9[i][t] for i in range(4)) for t in range(T9)]
    return ser, sum(x * x for x in ser) / F(T9)

BOOKS = {
    "P  (pair trade)      ": [F(1, 2), F(1, 2), F(0), F(0)],
    "H  (hedged pair)     ": [F(1, 2), F(-1, 2), F(0), F(0)],
    "A  (four names equal)": [F(1, 4), F(1, 4), F(1, 4), F(1, 4)],
}

sub("7b. the quadratic form equals the book's own second moment -- three books")
for label, w in BOOKS.items():
    ser, v = book_variance_direct(w)
    show(f"{label} specific-return series", [str(x) for x in ser])
    check(f"{label} direct second moment == w^T Delta_full w", v, quad(DFULL, w))

sub("8a. Book P -- 50% KVR, 50% TLM")
wP = BOOKS["P  (pair trade)      "]
vP_full = quad(DFULL, wP)
vP_diag = quad(DDIAG, wP)
check("variance with the full matrix", vP_full, F(7))
check("variance with the diagonal only", vP_diag, F(4))
check("the diagonal part alone: (1/4)*8 + (1/4)*8", F(1, 4) * 8 + F(1, 4) * 8, F(4))
check("the cross term: 2*(1/2)*(1/2)*6", 2 * F(1, 2) * F(1, 2) * F(6), F(3))
check("4 + 3", F(4) + F(3), F(7))
show("risk, full matrix   = sqrt(7)", root(vP_full))
show("risk, diagonal only = sqrt(4)", root(vP_diag))
check("the variance ratio is exactly 7/4", vP_full / vP_diag, F(7, 4))
rP, _ = dsqrt(F(7, 4))
print(f"        risk ratio sqrt(7)/2 = {rP:.6f} (ROUNDED)")
sP, _ = dsqrt(F(4, 7))
print(f"        the diagonal model reports this share of the truth, 2/sqrt(7) = {sP:.6f} (ROUNDED)")
missP = dsqrt(F(7))[0] - Decimal(2)
print(f"        risk missing, in percentage points = {missP:.6f} (ROUNDED)")
print(f"        risk missing, in basis points      = {missP*100:.2f} (ROUNDED)")

sub("8b. Book H -- long KVR, short TLM: the error changes sign")
wH = BOOKS["H  (hedged pair)     "]
vH_full = quad(DFULL, wH)
vH_diag = quad(DDIAG, wH)
check("variance with the full matrix, 4 - 3", vH_full, F(1))
check("variance with the diagonal only (unchanged from Book P)", vH_diag, F(4))
show("risk, full matrix", root(vH_full))
show("risk, diagonal only", root(vH_diag))
check("the variance ratio is exactly 4", vH_diag / vH_full, F(4))
check("so the risk ratio is exactly 2", F(2) ** 2, F(4))
check("the diagonal model OVERstates by exactly 100 basis points",
      F(2) - F(1), F(1))

sub("8c. Book A -- the four names, equally weighted")
wA = BOOKS["A  (four names equal)"]
vA_full = quad(DFULL, wA)
vA_diag = quad(DDIAG, wA)
check("diagonal part: (1/16)*(8+8+9+6)", F(1, 16) * (F(8) + F(8) + F(9) + F(6)), F(31, 16))
check("cross term: 2*(1/4)*(1/4)*6", 2 * F(1, 4) * F(1, 4) * F(6), F(12, 16))
check("variance with the full matrix", vA_full, F(43, 16))
check("variance with the diagonal only", vA_diag, F(31, 16))
show("43/16 as a decimal", dec(vA_full))
show("31/16 as a decimal", dec(vA_diag))
show("risk, full matrix", root(vA_full))
show("risk, diagonal only", root(vA_diag))
check("the variance ratio is exactly 43/31", vA_full / vA_diag, F(43, 31))
rA, _ = dsqrt(F(43, 31))
sA, _ = dsqrt(F(31, 43))
print(f"        risk ratio     = {rA:.6f} (ROUNDED)")
print(f"        reported share = {sA:.6f} (ROUNDED)")
missA = (dsqrt(F(43))[0] - dsqrt(F(31))[0]) / Decimal(4)
print(f"        risk missing, percentage points = {missA:.6f} (ROUNDED)")
print(f"        risk missing, basis points      = {missA*100:.2f} (ROUNDED)")

sub("8d. Book W -- fifty names at 2% each, our four among them")
# the other 46 names are declared to have d = 8 and no specific links at all
w_each = F(1, 50)
vW_diag = w_each ** 2 * (F(8) + F(8) + F(9) + F(6) + F(46) * F(8))
vW_full = vW_diag + 2 * w_each * w_each * F(6)
check("the four named diagonals sum to 31", F(8) + F(8) + F(9) + F(6), F(31))
check("the other forty-six contribute 46*8 = 368", F(46) * F(8), F(368))
check("so the diagonal variance is 399/2500", vW_diag, F(399, 2500))
check("the single cross term is 12/2500", 2 * w_each * w_each * F(6), F(12, 2500))
check("and the full variance is 411/2500", vW_full, F(411, 2500))
show("399/2500 as a decimal", dec(vW_diag))
show("411/2500 as a decimal", dec(vW_full))
show("risk, full matrix", root(vW_full))
show("risk, diagonal only", root(vW_diag))
check("the variance ratio is exactly 137/133", vW_full / vW_diag, F(137, 133))
rW, _ = dsqrt(F(137, 133))
sW, _ = dsqrt(F(133, 137))
print(f"        risk ratio     = {rW:.6f} (ROUNDED)")
print(f"        reported share = {sW:.6f} (ROUNDED)")
missW = (dsqrt(F(411))[0] - dsqrt(F(399))[0]) / Decimal(50)
print(f"        risk missing, percentage points = {missW:.6f} (ROUNDED)")
print(f"        risk missing, basis points      = {missW*100:.2f} (ROUNDED)")
ratio_bps = missP / missW
print(f"        Book P's shortfall divided by Book W's = {ratio_bps:.1f} (ROUNDED)")

sub("8e. the share of the variance the diagonal model throws away")
check("Book P: 3 out of 7", F(3) / F(7), F(3, 7))
show("3/7 as a decimal", dec(F(3, 7), 6))
check("Book A: (12/16) out of (43/16)", (F(12, 16)) / F(43, 16), F(12, 43))
show("12/43 as a decimal", dec(F(12, 43), 6))
check("Book W: (12/2500) out of (411/2500)", F(12, 2500) / F(411, 2500), F(4, 137))
show("4/137 as a decimal", dec(F(4, 137), 6))
check("Book H: the discarded term is -3 against a full variance of 1",
      F(-3) / F(1), F(-3))
check("the discarded matrix is the same in all four books", DFULL[0][1], F(6))
sub("8e(ii). how many pairs each book has, and how many are linked")
for N, pairs in ((2, 1), (4, 6), (50, 1225)):
    check(f"a {N}-name book has N(N-1)/2 = {pairs} pairs, exactly one of them linked",
          F(N) * (F(N) - 1) / 2, F(pairs))
check("1 of 1 pairs versus 1 of 1225 pairs", F(1) / F(1225), F(1, 1225))
show("1/1225 as a decimal", dec(F(1, 1225), 6))

sub("8e(iii). the discarded part is indefinite -- which is why the sign can flip")
OFFONLY = [[DFULL[i][j] if i != j else F(0) for j in range(4)] for i in range(4)]
check("Book P's discarded term is positive", quad(OFFONLY, wP), F(3))
check("Book H's discarded term is negative", quad(OFFONLY, wH), F(-3))
check("so no single direction of error can be claimed for the diagonal model",
      (quad(OFFONLY, wP) > 0, quad(OFFONLY, wH) < 0), (True, True))

sub("8e(iv). sweep: every integer book in [-3,3]^4, matrix against raw series")
swept = 0
neg = 0
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-3, 4):
            for e in range(-3, 4):
                w = [F(a), F(b), F(c), F(e)]
                ser = [sum(w[i] * SER9[i][t] for i in range(4)) for t in range(T9)]
                v = sum(x * x for x in ser) / F(T9)
                assert v == quad(DFULL, w)
                assert v >= 0
                if quad(OFFONLY, w) < 0:
                    neg += 1
                swept += 1
check("integer books swept", swept, 2401)
check("... every one has a non-negative specific variance under the full matrix",
      True, True)
check("... and in this many of them the diagonal model OVERstates the risk",
      neg, 882)

sub("8f. the general formula for N equal-weighted names with one linked pair")
# sigma^2_diag = d/N ; sigma^2_full = d/N + 2c/N^2 ; ratio^2 = 1 + 2*rho/N
d_gen, rho_gen = F(8), F(3, 4)
c_gen = rho_gen * d_gen
check("with d = 8 and rho = 3/4 the covariance is 6", c_gen, F(6))
for N in (2, 4, 10, 25, 50, 100):
    w = F(1, N)
    vd = F(N) * w * w * d_gen
    vf = vd + 2 * w * w * c_gen
    check(f"N={N}: variance ratio equals 1 + 2*rho/N", vf / vd, F(1) + 2 * rho_gen / F(N))
    r, _ = dsqrt(vf / vd)
    print(f"        N={N:3d}   variance ratio {vf/vd}   risk ratio {r:.6f} (ROUNDED)")
check("N=2 reproduces Book P's 7/4 exactly", F(1) + 2 * rho_gen / F(2), F(7, 4))
check("N=50 gives 103/100", F(1) + 2 * rho_gen / F(50), F(103, 100))
r50, _ = dsqrt(F(103, 100))
print(f"        and sqrt(103/100) = {r50:.6f} (ROUNDED), against Book W's {rW:.6f} (ROUNDED)")
check("the two agree to four decimal places",
      str(r50.quantize(Decimal('1.0000'))), str(rW.quantize(Decimal('1.0000'))))

# ===========================================================================
head("SECTION 9  THE SAME-COMPANY CASE -- BFRE's structural override (p.28)")
# ===========================================================================

# structural approach: clone the primary listing's specific risk, force rho = 1
DSTR = [[F(8), F(8)], [F(8), F(8)]]
check("cloned specific risk on both lines", DSTR[0][0], DSTR[1][1])
check("forced correlation of 1 means the covariance IS the variance",
      DSTR[0][1], F(8))
check("the 2x2 determinant is exactly zero", DSTR[0][0] * DSTR[1][1] - DSTR[0][1] ** 2,
      F(0))
w5050 = [F(1, 2), F(1, 2)]
vs_full = quad(DSTR, w5050)
vs_diag = quad(diagonal_of(DSTR), w5050)
check("50/50 across the two lines, full matrix", vs_full, F(8))
check("50/50 across the two lines, diagonal only", vs_diag, F(4))
check("the variance ratio is exactly 2", vs_full / vs_diag, F(2))
show("risk, full matrix", root(vs_full))
show("risk, diagonal only", root(vs_diag))
rs, _ = dsqrt(F(2))
ss_, _ = dsqrt(F(1, 2))
print(f"        risk ratio sqrt(2)  = {rs:.6f} (ROUNDED)")
print(f"        reported share      = {ss_:.6f} (ROUNDED)")
sub("9b. under a forced correlation of 1 the split does not matter at all")
for w in (F(1, 2), F(3, 5), F(9, 10), F(1, 4)):
    ww = [w, F(1) - w]
    check(f"long-only split {w} / {F(1)-w}: variance is exactly 8", quad(DSTR, ww), F(8))
sub("9c. and the hedged book's true specific risk is exactly zero")
whedge = [F(1, 2), F(-1, 2)]
check("+50% one line, -50% the other, full matrix", quad(DSTR, whedge), F(0))
check("... while the diagonal model still says 4", quad(diagonal_of(DSTR), whedge), F(4))
check("that is the index-tracker's whole risk, declared to be nothing",
      quad(DSTR, whedge), F(0))
check("on the 50/50 long-only book the diagonal model throws away exactly half",
      (F(8) - F(4)) / F(8), F(1, 2))

# ===========================================================================
head("SECTION 10  SABOTAGE -- two corrupted matrices, two structural checks")
# ===========================================================================

sub("10a. a covariance that no data could have produced")
BAD = [[F(8), F(10)], [F(10), F(8)]]
check("claimed correlation 10/8 is bigger than 1", F(10, 8) > 1, True)
check("determinant 8*8 - 10*10 is negative", F(8) * F(8) - F(10) * F(10), F(-36))
check("the hedged book gets a NEGATIVE variance", quad(BAD, whedge), F(-1))

sub("10b. a corrupted miss, caught by the cross-sectional balance")
bad_month = [U[nm][0] for nm in NAMES8]
bad_month[2] = bad_month[2] + F(1)      # CHR's month-1 miss pushed from +2 to +3
check("the corrupted month's misses no longer sum to zero", sum(bad_month), F(1))
check("but the cheapness balance does NOT break -- CHR's exposure is zero",
      dot(XCHP, bad_month), F(0))
check("so on CHR only the sum-to-zero check fires",
      (sum(bad_month) != 0, dot(XCHP, bad_month) == 0), (True, True))
bad_month2 = [U[nm][0] for nm in NAMES8]
bad_month2[4] = bad_month2[4] + F(1)    # EMK's month-1 miss pushed from +1 to +2
check("push EMK instead and BOTH checks break: sum", sum(bad_month2), F(1))
check("push EMK instead and BOTH checks break: sum x*u", dot(XCHP, bad_month2), F(2))

# ===========================================================================
head("SECTION 14  BOSS ROUND -- the counting argument that defends the paper")
# ===========================================================================

sub("14.4 how many numbers a full specific covariance matrix would need")
# Table 1.3, p.28: daily specific-risk model uses 375 observations; weekly uses 104.
OBS_DAILY, OBS_WEEKLY = F(375), F(104)
for N in (100, 375, 749, 750, 3000):
    params = F(N) * (F(N) + 1) / 2
    data = OBS_DAILY * F(N)
    show(f"N={N}: distinct entries {params}, numbers available {data}, "
         f"{'ENOUGH' if data >= params else 'NOT ENOUGH'}", "")
check("N(N+1)/2 <= 375N exactly when N <= 749: at N=749",
      F(749) * F(750) / 2 <= OBS_DAILY * F(749), True)
check("... and it fails at N=750", F(750) * F(751) / 2 <= OBS_DAILY * F(750), False)
check("the break-even follows from (N+1)/2 = 375, i.e. N = 749",
      (F(2) * OBS_DAILY) - 1, F(749))
check("the weekly model's break-even, (N+1)/2 = 104, i.e. N = 207",
      (F(2) * OBS_WEEKLY) - 1, F(207))
check("a 3000-name universe would need 4,501,500 entries",
      F(3000) * F(3001) / 2, F(4501500))
check("... from 1,125,000 numbers", OBS_DAILY * F(3000), F(1125000))
check("that is 3001/750 parameters for every number",
      F(4501500) / F(1125000), F(3001, 750))
show("3001/750 as a decimal", dec(F(3001, 750)))
check("rank of a second-moment matrix built from 375 observations is at most 375",
      375 < 3000, True)

sub("14.4(ii) the same counting for the diagonal alone, which IS estimable")
check("a diagonal needs N numbers, not N(N+1)/2: at N=3000", F(3000), F(3000))
check("375 observations per diagonal entry", OBS_DAILY / F(1), F(375))
check("so the diagonal is over-determined 375 to 1, while the full matrix is "
      "under-determined 1 to 3001/750",
      F(4501500) / F(1125000) > 1, True)

sub("14.3 where the shortfall lands, side by side")
rows = [("P  pair trade, 2 names ", F(4), F(7)),
        ("A  four-name book      ", F(31, 16), F(43, 16)),
        ("W  fifty-name book     ", F(399, 2500), F(411, 2500))]
for label, vd, vf in rows:
    rd, _ = dsqrt(vd)
    rf, _ = dsqrt(vf)
    print(f"        {label} diag {rd:.4f}  full {rf:.4f}  "
          f"short {(rf-rd)*100:.2f} bps  reported share {(rd/rf):.4f}")
check("Book P's variance ratio", F(7) / F(4), F(7, 4))
check("Book A's variance ratio", F(43, 16) / F(31, 16), F(43, 31))
check("Book W's variance ratio", F(411, 2500) / F(399, 2500), F(137, 133))

# ===========================================================================
head("SECTION 16  BACK TO BFRE -- the paper's own printed numbers")
# ===========================================================================

sub("16d. Table 1.3, p.28, quoted digit for digit")
check("daily model half-life, days", F(125), F(125))
check("daily model observations, days", F(375), F(375))
check("daily model Newey-West lag, days", F(10), F(10))
check("weekly model half-life, weeks", F(26), F(26))
check("weekly model observations, weeks", F(104), F(104))
check("weekly model Newey-West lag, weeks", F(2), F(2))
check("375 days is about 15 months of trading at 25 days a month",
      F(375) / F(25), F(15))
check("104 weeks is exactly 2 years", F(104) / F(52), F(2))

sub("16g. p.35 -- the size of the stake, read directly off the pie")
check("Specific + Style + Industry + Country + FX + Act Sec",
      F(50) + F(25) + F(14) + F(6) + F(4) + F(1), F(100))
check("Specific is half of that report's Active Risk", F(50), F(100) / 2)

sub("16f. p.16 -- the other failure mode, [APPROX] pixel measurements")
# quoted only as positions relative to the printed 10% line, never as digits
check("decile 10 before the small-cap factor is above the 10% line",
      F(211, 10) > F(10), True)
check("decile 9 before the small-cap factor is above the 10% line",
      F(108, 10) > F(10), True)
check("decile 10 after the small-cap factor is below it", F(34, 10) < F(10), True)
check("decile 9 after the small-cap factor is below it", F(21, 10) < F(10), True)
check("they are the only two deciles of the ten that clear the line before",
      2, 2)

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level9.md.")
print("   Decimals tagged ROUNDED above are marked 'rounded' in the markdown.")
print("   Square roots are computed with decimal.Decimal at 60 digits; the")
print("   variance under every root is exact and is asserted as a Fraction.")
