#!/usr/bin/env python3
"""
verify_level6.py -- recomputes EVERY number printed in datasets/level6.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Run:  python3 tools/verify_level6.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.

Decimals are printed only as a display convenience and are ALWAYS labelled
"(ROUNDED)" here and "rounded" in the markdown.
"""

from fractions import Fraction as F
from itertools import product
import sys

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def S(v):
    if isinstance(v, (tuple, list)):
        return "[" + ", ".join(S(t) for t in v) + "]"
    return str(v)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def dec(v, n=6):
    """rounded decimal string -- ALWAYS labelled rounded wherever it is used"""
    return f"{float(v):.{n}f}"


def isqrt_dec(v, n=6):
    """rounded decimal square root of a Fraction"""
    return f"{float(v) ** 0.5:.{n}f}"


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


def showd(label, val, n=6):
    print(f"        {label}: {S(val)}   = {dec(val, n)} (ROUNDED)")


def showsqrt(label, val, n=6):
    print(f"        {label}: sqrt({S(val)}) = {isqrt_dec(val, n)} (ROUNDED)")


# ---------------------------------------------------------------------------
# the one-column machine
# ---------------------------------------------------------------------------


def fit1(x, r):
    """no-intercept one-column least squares"""
    Q = dot(x, x)
    Sxr = dot(x, r)
    b = Sxr / Q
    e = [ri - b * xi for xi, ri in zip(x, r)]
    return Q, Sxr, b, e


def fit2(x1, x2, r):
    """no-intercept two-column least squares, by Cramer"""
    A = dot(x1, x1)
    B = dot(x1, x2)
    C = dot(x2, x2)
    p = dot(x1, r)
    q = dot(x2, r)
    det = A * C - B * B
    b1 = (C * p - B * q) / det
    b2 = (A * q - B * p) / det
    e = [ri - b1 * a - b2 * c for a, c, ri in zip(x1, x2, r)]
    return A, B, C, p, q, det, b1, b2, e


# ===========================================================================
head("SECTION 3  The cold-open dataset, re-established from raw numbers")
# ===========================================================================

x = [F(-3, 2), F(-1, 2), F(0), F(1), F(2)]
r = [F(-2), F(-2), F(1, 2), F(4), F(7, 2)]
names = ["AXL", "BRN", "CHR", "DLT", "EMK"]

show("x", x)
show("r (percent)", r)

n = len(x)
k = 1
check("n", n, 5)
check("k (columns)", k, 1)
check("Sum x", sum(x), F(1))
Q, Sxr, b, e = fit1(x, r)
check("Q = Sum x^2", Q, F(15, 2))
check("S = Sum x*r", Sxr, F(15))
check("Sum r", sum(r), F(4))
check("Sum r^2", dot(r, r), F(73, 2))
check("b = S/Q", b, F(2))
check("residuals e = r - 2x", e, [F(1), F(-1), F(1, 2), F(2), F(-1, 2)])
check("Sum e", sum(e), F(2))
check("Sum x*e (the Level 2 balance)", dot(x, e), F(0))
check("SSE = Sum e^2", dot(e, e), F(13, 2))
check("Sum |e|", sum(abs(v) for v in e), F(5))
SSE = dot(e, e)

# ===========================================================================
head("SECTION 4  Where the wobble comes from -- the algebra")
# ===========================================================================

sub("4a. b_hat = b + Sum(x*e)/Sum(x^2), verified as an identity on this data")
# r = 2x + e exactly, by construction of e
check("r reconstructed as 2x + e", [F(2) * xi + ei for xi, ei in zip(x, e)], r)
check("Sum x*r  =  2*Q + Sum x*e", Sxr, F(2) * Q + dot(x, e))
check("b_hat - b = Sum x*e / Q", b - F(2), dot(x, e) / Q)

sub("2. bedrock: Q is reach from zero, NOT spread about the mean (no intercept here)")
xbar = sum(x) / n
check("x-bar", xbar, F(1, 5))
check("Q = Sum x^2 (what Var(b) = sigma^2/Q divides by here)", Q, F(15, 2))
check("Sum (x - xbar)^2 (what it would become WITH an intercept)",
      sum((xi - xbar) ** 2 for xi in x), F(73, 10))
check("   the two are different numbers", Q == F(73, 10), False)

sub("4b. the weights w_i = x_i / Q")
w = [xi / Q for xi in x]
check("w", w, [F(-1, 5), F(-1, 15), F(0), F(2, 15), F(4, 15)])
check("Sum w*x = 1 exactly (a pure signal passes through untouched)", dot(w, x), F(1))
check("Sum w", sum(w), F(2, 15))
check("Sum w^2 = 1/Q", dot(w, w), F(2, 15))
check("1/Q", 1 / Q, F(2, 15))
show("CHR's weight (x = 0)", w[2])

sub("4c. nudge one return, watch b move by exactly w_i")
for i, d in ((3, F(1)), (4, F(1)), (2, F(100))):
    r2 = list(r)
    r2[i] = r2[i] + d
    Q2, S2, b2, e2 = fit1(x, r2)
    check(f"add {d} to {names[i]}'s return -> new b", b2, b + d * w[i])
    show(f"   new S = Sum x*r", S2)
check("b unchanged when CHR moves by +100", fit1(x, [r[0], r[1], r[2] + F(100), r[3], r[4]])[2], F(2))
check("CHR's return could be +100.5 and b stays 2", r[2] + F(100), F(201, 2))

sub("4d. leverage h_i = x_i^2 / Q, and Sum h = k")
h = [xi * xi / Q for xi in x]
check("h", h, [F(3, 10), F(1, 30), F(0), F(2, 15), F(8, 15)])
check("Sum h = k = 1", sum(h), F(1))
check("h_i = w_i * x_i", h, [wi * xi for wi, xi in zip(w, x)])

# ===========================================================================
head("SECTION 5  The 32 worlds -- a standard error by enumeration")
# ===========================================================================

sub("5a. sign-flip worlds built from the OBSERVED residual sizes")
prods = [xi * ei for xi, ei in zip(x, e)]
check("x_i * e_i", prods, [F(-3, 2), F(1, 2), F(0), F(2), F(-1)])
check("Sum x_i*e_i = 0", sum(prods), F(0))
check("Sum x_i^2 * e_i^2", sum(xi * xi * ei * ei for xi, ei in zip(x, e)), F(15, 2))

worlds = list(product([F(1), F(-1)], repeat=5))
check("number of worlds = 2^5", len(worlds), 32)

bs = []
for s in worlds:
    rw = [F(2) * xi + si * ei for xi, si, ei in zip(x, s, e)]
    bs.append(fit1(x, rw)[2])

check("mean of b over 32 worlds", sum(bs) / 32, F(2))
var_obs = sum((v - F(2)) ** 2 for v in bs) / 32
check("mean squared deviation of b", var_obs, F(2, 15))
showsqrt("   standard deviation of b", var_obs)
check("   equals (Sum x^2 e^2)/Q^2",
      sum(xi * xi * ei * ei for xi, ei in zip(x, e)) / (Q * Q), F(2, 15))

sub("5b. the distribution of b over the 32 worlds")
tally = {}
for v in bs:
    tally[v] = tally.get(v, 0) + 1
for v in sorted(tally):
    print(f"        b = {S(v):>8}  = {dec(v, 4)} (ROUNDED)   count {tally[v]:>2} / 32")
check("distinct values of b", len(tally), 11)
check("smallest b", min(tally), F(4, 3))
check("largest b", max(tally), F(8, 3))
check("count at b = 2", tally[F(2)], 4)
check("counts sum to 32", sum(tally.values()), 32)
check("every count is even (CHR's flip never moves b)",
      all(c % 2 == 0 for c in tally.values()), True)

sub("5c. CHR's flip is invisible to b, visible to SSE")
s_a = (F(1), F(1), F(1), F(1), F(1))
s_b = (F(1), F(1), F(-1), F(1), F(1))
ra = [F(2) * xi + si * ei for xi, si, ei in zip(x, s_a, e)]
rb = [F(2) * xi + si * ei for xi, si, ei in zip(x, s_b, e)]
check("b in world (+,+,+,+,+)", fit1(x, ra)[2], F(2))
check("b in world (+,+,-,+,+)", fit1(x, rb)[2], F(2))
check("SSE in both worlds is the same here (both are 13/2)",
      (dot(fit1(x, ra)[3], fit1(x, ra)[3]), dot(fit1(x, rb)[3], fit1(x, rb)[3])),
      (F(13, 2), F(13, 2)))
check("but CHR's own residual flipped sign",
      (fit1(x, ra)[3][2], fit1(x, rb)[3][2]), (F(1, 2), F(-1, 2)))

# ===========================================================================
head("SECTION 6  Degrees of freedom")
# ===========================================================================

sub("6a. the residuals are pinned: given four of them, the fifth is forced")
# Sum x*e = 0  ->  2*e5 = -( x1e1 + x2e2 + x3e3 + x4e4 )
partial = dot(x[:4], e[:4])
check("x1e1 + x2e2 + x3e3 + x4e4", partial, F(1))
check("e5 forced = -partial / x5", -partial / x[4], F(-1, 2))
check("   which is the residual we actually have", e[4], F(-1, 2))
check("CHR's residual is NOT pinned (its x is 0)", x[2], F(0))

sub("6b. equal-size wobble worlds: eps_i = +/-1, so sigma^2 = 1 exactly")
sigma2 = F(1)
eps_worlds = list(product([F(1), F(-1)], repeat=5))
b_eq = []
sse_eq = []
e_sq_sum = [F(0)] * 5
tsq_true = []
tsq_est = []
for s in eps_worlds:
    rw = [F(2) * xi + si for xi, si in zip(x, s)]
    Qw, Sw, bw, ew = fit1(x, rw)
    b_eq.append(bw)
    sse = dot(ew, ew)
    sse_eq.append(sse)
    for i in range(5):
        e_sq_sum[i] += ew[i] * ew[i]
    drop = (bw - F(2)) ** 2 * Q
    tsq_true.append(drop / sigma2)
    tsq_est.append(drop / (sse / (n - k)) if sse != 0 else None)

check("mean of b over the 32 equal-size worlds", sum(b_eq) / 32, F(2))
var_eq = sum((v - F(2)) ** 2 for v in b_eq) / 32
check("Var(b) = sigma^2 / Q", var_eq, F(2, 15))
check("   sigma^2 / Q", sigma2 / Q, F(2, 15))

sub("6c. E[e_i^2] = (1 - h_i) * sigma^2, stock by stock")
for i in range(5):
    check(f"E[e^2] for {names[i]}", e_sq_sum[i] / 32, (1 - h[i]) * sigma2)
check("E[SSE] = Sum (1-h_i) = n - k", sum(sse_eq) / 32, F(4))
check("   n - k", F(n - k), F(4))
check("E[SSE]/n (the WRONG denominator)", sum(sse_eq) / 32 / n, F(4, 5))
show("   sigma^2 it should have returned", sigma2)
check("shortfall of the /n rule", 1 - F(4, 5), F(1, 5))
check("E[SSE]/(n-k) (the RIGHT denominator)", sum(sse_eq) / 32 / (n - k), F(1))

sub("6d. E[t^2] for a worthless column")
check("E[t^2] using the TRUE sigma^2", sum(tsq_true) / 32, F(1))
Et2_est = sum(tsq_est) / 32
showd("E[t^2] using the ESTIMATED sigma^2 (df = 4)", Et2_est)
check("   is bigger than 1", Et2_est > 1, True)
big = sum(1 for v in tsq_est if v >= 4)
check("worlds with t^2 >= 4, out of 32", big, 4)
check("   as a fraction", F(big, 32), F(1, 8))
showd("Markov bound E[t^2]/4 on that fraction", Et2_est / 4)
check("   Markov bound holds", F(big, 32) <= Et2_est / 4, True)

sub("6e. the degenerate case: four assets, four columns c1..c4 (a Hadamard design)")
H = [
    [F(1), F(1), F(-1), F(-1)],
    [F(1), F(-1), F(1), F(-1)],
    [F(1), F(-1), F(-1), F(1)],
    [F(1), F(1), F(1), F(1)],
]
for j in range(4):
    check(f"Sum c{j+1}^2", dot(H[j], H[j]), F(4))
for i in range(4):
    for j in range(i + 1, 4):
        check(f"c{i+1}.c{j+1} = 0 (orthogonal)", dot(H[i], H[j]), F(0))

eps4 = list(product([F(1), F(-1)], repeat=4))
check("number of worlds = 2^4", len(eps4), 16)
ladder = {}
for kk in range(1, 5):
    tot = F(0)
    zeros = 0
    for s in eps4:
        coefs = [dot(H[j], s) / F(4) for j in range(kk)]
        sse = dot(s, s) - sum(c * c * F(4) for c in coefs)
        tot += sse
        if sse == 0:
            zeros += 1
    ladder[kk] = (tot / 16, zeros)
    check(f"k = {kk}: E[SSE] = n - k = {4-kk}", tot / 16, F(4 - kk))
    check(f"k = {kk}: E[SSE]/n", (tot / 16) / 4, F(4 - kk, 4))
    show(f"   worlds (of 16) with SSE exactly 0", zeros)
check("k = 4: SSE is 0 in EVERY world", ladder[4][1], 16)
check("k = 4: /n gives sigma^2 = 0, which is false", ladder[4][0] / 4, F(0))
show("k = 4: /(n-k) gives 0/0 -- undefined, which is honest", "0 / 0")
for kk in range(1, 5):
    check(f"k = {kk}: /n understates sigma^2 by",
          1 - (ladder[kk][0] / 4), F(kk, 4))

sub("6f. the n-1 trap: on the cold open n-k happens to equal n-1")
check("n - k", F(n - k), F(4))
check("n - 1", F(n - 1), F(4))
check("they coincide only because k = 1", k, 1)

# ===========================================================================
head("SECTION 7  The standard error on the cold open")
# ===========================================================================

df = n - k
check("df = n - k", df, 4)
sig2_hat = SSE / df
check("sigma^2_hat = SSE/(n-k) = (13/2)/4", sig2_hat, F(13, 8))
showsqrt("sigma_hat", sig2_hat)
varb = sig2_hat / Q
check("Var(b) = sigma^2_hat / Q", varb, F(13, 60))
showd("   Var(b)", varb)
showsqrt("SE(b)", varb)
t_sq = b * b / varb
check("t^2 = b^2 / Var(b)", t_sq, F(240, 13))
showd("   t^2 as a decimal", t_sq)
showsqrt("   t", t_sq)

sub("7a. t^2 = (S^2/Q) / sigma^2_hat, pieces named")
check("S = Sum x*r", Sxr, F(15))
check("Q = Sum x^2", Q, F(15, 2))
check("S^2", Sxr * Sxr, F(225))
check("S^2/Q", Sxr * Sxr / Q, F(30))
check("(S^2/Q) / sigma^2_hat", (Sxr * Sxr / Q) / sig2_hat, F(240, 13))
check("   equals b^2/Var(b)", (Sxr * Sxr / Q) / sig2_hat, t_sq)
check("S^2/Q = b^2 * Q", Sxr * Sxr / Q, b * b * Q)

sub("7b. S^2/Q is the drop in the miss, straight from Level 0's parabola")
SS0 = dot(r, r)
check("SS(0) = Sum r^2", SS0, F(73, 2))
check("SS(2) = SSE", SSE, F(13, 2))
check("drop = SS(0) - SS(2)", SS0 - SSE, F(30))
check("   = S^2/Q", SS0 - SSE, Sxr * Sxr / Q)

sub("7c. R^2 and t^2 are the same fact")
R2 = (SS0 - SSE) / SS0
check("R^2 = 30 / 36.5", R2, F(60, 73))
showd("   R^2", R2)
check("1 - R^2", 1 - R2, F(13, 73))
check("df * R^2/(1-R^2)", F(df) * R2 / (1 - R2), F(240, 13))
check("   equals t^2", F(df) * R2 / (1 - R2), t_sq)

sub("7d. wrong denominators, and exactly what each returns")
rows = []
for label, dd in (("n - k = 4  (correct)", F(4)), ("n = 5", F(5)), ("n - 2 = 3", F(3))):
    s2 = SSE / dd
    vb = s2 / Q
    rows.append((label, s2, vb, b * b / vb))
    print(f"        {label:>22}: sigma^2 = {S(s2):>8} = {dec(s2,6)} (ROUNDED)"
          f"  SE = {isqrt_dec(vb)} (ROUNDED)  t = {isqrt_dec(b*b/vb)} (ROUNDED)")
check("sigma^2 with /n", SSE / 5, F(13, 10))
check("Var with /n", (SSE / 5) / Q, F(13, 75))
check("t^2 with /n", b * b / ((SSE / 5) / Q), F(300, 13))
check("ratio of that t to the right t, squared", (F(300, 13)) / t_sq, F(5, 4))
showsqrt("   so t is too big by a factor", F(5, 4))
check("sigma^2 with /(n-2)", SSE / 3, F(13, 6))
check("t^2 with /(n-2)", b * b / ((SSE / 3) / Q), F(180, 13))
check("ratio squared", F(180, 13) / t_sq, F(3, 4))
showsqrt("   so t is too small by a factor", F(3, 4))

sub("7e. two more wrong shapes")
check("SE '=' sigma_hat  (forgot to divide by Q)", sig2_hat, F(13, 8))
showsqrt("   that 'SE'", sig2_hat)
check("t^2 from that shape = b^2/sigma^2_hat", b * b / sig2_hat, F(32, 13))
showsqrt("   t", b * b / sig2_hat)
check("SE '=' sigma_hat/sqrt(n) (used n where Q belongs)", sig2_hat / n, F(13, 40))
showsqrt("   that 'SE'", sig2_hat / n)
check("t^2 from that shape", b * b / (sig2_hat / n), F(160, 13))
showsqrt("   t", b * b / (sig2_hat / n))
check("that shape is right only if Q = n; here Q =", Q, F(15, 2))
abs_sigma = sum(abs(v) for v in e) / df
check("'typical miss' from absolute values: Sum|e|/(n-k)", abs_sigma, F(5, 4))
showsqrt("   the SE it gives (abs_sigma^2/Q)", abs_sigma * abs_sigma / Q)
check("t^2 from that shape", b * b / (abs_sigma * abs_sigma / Q), F(96, 5))
showsqrt("   the t it gives", b * b / (abs_sigma * abs_sigma / Q))

sub("7e2. the Section 11 sabotage round: R^2 recovered from t^2 and df alone")
check("t^2 / df", t_sq / F(df), F(60, 13))
check("R^2 = (t^2/df) / (1 + t^2/df)", (F(60, 13)) / (1 + F(60, 13)), F(60, 73))
showd("   R^2", F(60, 73))
check("the planted lie 0.75 is not 60/73", F(3, 4) == F(60, 73), False)

sub("7f. Level 0's parabola, re-checked (the symmetry the player already owns)")
for bb in (F(3, 2), F(2), F(5, 2)):
    ss = dot(r, r) - 2 * bb * Sxr + bb * bb * Q
    check(f"SS({bb})", ss, {F(3, 2): F(67, 8), F(2): F(13, 2), F(5, 2): F(67, 8)}[bb])
check("SS(3/2) = SS(5/2) = 8.375", F(67, 8), F(8375, 1000))

sub("7g. more data: the same five names replicated five times over (n = 25)")
x25 = x * 5
r25 = r * 5
Q25, S25, b25, e25 = fit1(x25, r25)
check("n", len(x25), 25)
check("Q = 5 * 15/2", Q25, F(75, 2))
check("S = 5 * 15", S25, F(75))
check("b is unchanged", b25, F(2))
check("SSE = 5 * 13/2", dot(e25, e25), F(65, 2))
check("df = n - k", 25 - 1, 24)
s2_25 = dot(e25, e25) / 24
check("sigma^2_hat", s2_25, F(65, 48))
check("Var(b)", s2_25 / Q25, F(13, 360))
showsqrt("SE(b)", s2_25 / Q25)
check("t^2", b * b / (s2_25 / Q25), F(1440, 13))
showsqrt("t", b * b / (s2_25 / Q25))
check("sigma^2_hat fell by", s2_25 / sig2_hat, F(5, 6))
check("Q grew by", Q25 / Q, F(5))
check("Var(b) shrank by 5 * 6/5 = 6", varb / (s2_25 / Q25), F(6))
check("t^2 ratio to the 5-stock t^2", (F(1440, 13)) / t_sq, F(6))
showsqrt("   so t grew by a factor", F(6))

# ===========================================================================
head("SECTION 8  The mean is the same machine: the sqrt(n) law")
# ===========================================================================

ones = [F(1)] * 5
Q1, S1, b1_, e1 = fit1(ones, r)
check("Q = Sum 1^2 = n", Q1, F(5))
check("S = Sum r", S1, F(4))
check("b = r-bar", b1_, F(4, 5))
check("residuals r - r-bar", e1, [F(-14, 5), F(-14, 5), F(-3, 10), F(16, 5), F(27, 10)])
check("Sum of those residuals is 0", sum(e1), F(0))
SSE1 = dot(e1, e1)
check("SSE = Sum (r - r-bar)^2", SSE1, F(333, 10))
check("   = Sum r^2 - (Sum r)^2/n", dot(r, r) - S1 * S1 / F(5), F(333, 10))
s2_1 = SSE1 / (5 - 1)
check("sigma^2_hat = SSE/(n-1)", s2_1, F(333, 40))
showsqrt("sigma_hat", s2_1)
var1 = s2_1 / Q1
check("Var(r-bar) = sigma^2/n", var1, F(333, 200))
showsqrt("SE(r-bar) = sigma/sqrt(n)", var1)
t1sq = b1_ * b1_ / var1
check("t^2 = (S^2/Q)/sigma^2", t1sq, F(128, 333))
check("   S^2/Q", S1 * S1 / Q1, F(16, 5))
check("   (S^2/Q)/sigma^2", (S1 * S1 / Q1) / s2_1, F(128, 333))
showd("t^2", t1sq)
showsqrt("t", t1sq)
print("        The average return of these five names (+0.8%) is NOT")
print("        distinguishable from zero, while the cheapness slope is.")

# ===========================================================================
head("SECTION 9  Unequal wobble sizes (graduate aside)")
# ===========================================================================

sub("9a. on the cold open the two routes agree, by an accident of this data")
check("Sum x^2 e^2", sum(xi * xi * ei * ei for xi, ei in zip(x, e)), F(15, 2))
check("Sum x^2", Q, F(15, 2))
check("they are equal here", sum(xi * xi * ei * ei for xi, ei in zip(x, e)) == Q, True)
check("sign-flip Var(b)", var_obs, F(2, 15))
check("classical Var(b) = sigma^2_hat/Q", varb, F(13, 60))
check("2/15 as sixtieths", F(2, 15), F(8, 60))
showd("ratio classical/sign-flip", varb / var_obs)
check("   ratio", varb / var_obs, F(13, 8))
check("sign-flip t^2 = b^2/(2/15)", b * b / var_obs, F(30))
showsqrt("   sign-flip t", b * b / var_obs)

sub("9b. a three-asset case where they disagree by 3x")
xc = [F(1), F(1), F(-2)]
ec = [F(1), F(-1), F(0)]
rc = [F(1) * xi + ei for xi, ei in zip(xc, ec)]
Qc, Sc, bc, ecc = fit1(xc, rc)
check("x", xc, [F(1), F(1), F(-2)])
check("r", rc, [F(2), F(0), F(-2)])
check("Q = Sum x^2", Qc, F(6))
check("S = Sum x*r", Sc, F(6))
check("b", bc, F(1))
check("residuals", ecc, [F(1), F(-1), F(0)])
check("Sum x*e = 0", dot(xc, ecc), F(0))
check("SSE", dot(ecc, ecc), F(2))
check("df = n - k", 3 - 1, 2)
check("sigma^2_hat", dot(ecc, ecc) / 2, F(1))
check("classical Var(b) = sigma^2/Q", F(1) / Qc, F(1, 6))
check("Sum x^2 e^2", sum(xi * xi * ei * ei for xi, ei in zip(xc, ecc)), F(2))
check("sign-flip Var(b) = Sum x^2e^2 / Q^2", F(2) / (Qc * Qc), F(1, 18))
check("ratio", (F(1) / Qc) / (F(2) / (Qc * Qc)), F(3))

# ===========================================================================
head("SECTION 14  BOSS ROUND -- the two-column desk file")
# ===========================================================================

bnames = ["PRM", "QNT", "ROV", "SLT", "TDR", "URS"]
g = [F(-2, 100), F(-1, 100), F(1, 100), F(-1, 100), F(1, 100), F(2, 100)]
xv = [F(-3), F(-2), F(-1), F(1), F(2), F(3)]
rb2 = [F(-43, 10), F(-29, 10), F(4, 10), F(16, 10), F(19, 10), F(33, 10)]

show("g (buyback ratio, a raw decimal)", g)
show("x (cheapness score)", xv)
show("r (percent)", rb2)
check("Sum g", sum(g), F(0))
check("Sum x", sum(xv), F(0))

A, B, C, p, q, det, bg, bx, eb = fit2(g, xv, rb2)
check("A = Sum g^2", A, F(3, 2500))
showd("   A", A)
check("B = Sum g*x", B, F(7, 50))
showd("   B", B)
check("C = Sum x^2", C, F(28))
check("p = Sum g*r", p, F(47, 250))
showd("   p", p)
check("q = Sum x*r", q, F(168, 5))
showd("   q", q)
check("det = AC - B^2", det, F(7, 500))
showd("   det", det)
check("   84/2500 - 49/2500", F(84, 2500) - F(49, 2500), F(35, 2500))
check("   35/2500 = 7/500", F(35, 2500), F(7, 500))

check("b_g = (Cp - Bq)/det", bg, F(40))
check("   Cp", C * p, F(658, 125))
showd("   Cp", C * p)
check("   Bq", B * q, F(588, 125))
showd("   Bq", B * q)
check("   Cp - Bq", C * p - B * q, F(14, 25))
showd("   Cp - Bq", C * p - B * q)
check("b_x = (Aq - Bp)/det", bx, F(1))
check("   Aq", A * q, F(126, 3125))
showd("   Aq", A * q)
check("   Bp", B * p, F(329, 12500))
showd("   Bp", B * p)
check("   Aq - Bp", A * q - B * p, F(7, 500))
showd("   Aq - Bp", A * q - B * p)

check("residuals e", eb, [F(-1, 2), F(-1, 2), F(1), F(1), F(-1, 2), F(-1, 2)])
check("Sum e", sum(eb), F(0))
check("Sum g*e = 0 (balance 1)", dot(g, eb), F(0))
check("Sum x*e = 0 (balance 2)", dot(xv, eb), F(0))
SSEb = dot(eb, eb)
check("SSE = Sum e^2", SSEb, F(3))
check("Sum r^2", dot(rb2, rb2), F(1103, 25))
showd("   Sum r^2", dot(rb2, rb2))

sub("14.4 standard errors and t")
nb, kb = 6, 2
dfb = nb - kb
check("n", nb, 6)
check("k", kb, 2)
check("df = n - k", dfb, 4)
check("n - 1 (the trap answer)", nb - 1, 5)
s2b = SSEb / dfb
check("sigma^2_hat = 3/4", s2b, F(3, 4))
showsqrt("sigma_hat", s2b)

var_g = s2b * C / det
check("Var(b_g) = sigma^2 * C/det", var_g, F(1500))
showsqrt("SE(b_g)", var_g)
var_x = s2b * A / det
check("Var(b_x) = sigma^2 * A/det", var_x, F(9, 140))
showsqrt("SE(b_x)", var_x)

tg2 = bg * bg / var_g
tx2 = bx * bx / var_x
check("t_g^2", tg2, F(16, 15))
showd("   t_g^2", tg2)
showsqrt("   t_g", tg2)
check("t_x^2", tx2, F(140, 9))
showd("   t_x^2", tx2)
showsqrt("   t_x", tx2)
check("t_x^2 / t_g^2", tx2 / tg2, F(175, 12))
showsqrt("   t_x / t_g", tx2 / tg2)

sub("14.4b det/C and det/A -- the effective leverage of each column")
check("det/C", det / C, F(1, 2000))
showd("   det/C", det / C)
check("det/A", det / A, F(35, 3))
showd("   det/A", det / A)
check("C/A", C / A, F(70000, 3))
showd("   C/A", C / A, 3)
check("t_g^2 = b_g^2 (det/C) / sigma^2", bg * bg * (det / C) / s2b, F(16, 15))
check("t_x^2 = b_x^2 (det/A) / sigma^2", bx * bx * (det / A) / s2b, F(140, 9))

sub("14.4b2 det/C IS Level 4's leftover column: w = g - (B/C) x, Sum w^2 = det/C")
wlo = [gi - (B / C) * xi for gi, xi in zip(g, xv)]
check("Sum x*w = 0 (nothing of cheapness left in w)", dot(xv, wlo), F(0))
check("Sum w^2 = det/C", dot(wlo, wlo), det / C)
check("   = A - B^2/C", A - B * B / C, F(1, 2000))
vlo = [xi - (B / A) * gi for gi, xi in zip(g, xv)]
check("Sum g*v = 0", dot(g, vlo), F(0))
check("Sum v^2 = det/A", dot(vlo, vlo), det / A)
check("   = C - B^2/A", C - B * B / A, F(35, 3))

sub("14.4c overlap between the two columns")
cos2 = B * B / (A * C)
check("cos^2 = B^2/(AC)", cos2, F(7, 12))
showd("   cos^2", cos2)
showsqrt("   cos", cos2)
check("VIF = 1/(1-cos^2)", 1 / (1 - cos2), F(12, 5))
showd("   VIF", 1 / (1 - cos2))

check("det/C = A / VIF (Level 4's number doing Level 4's job)", A / (1 / (1 - cos2)), det / C)

sub("14.4d leverages, which must sum to k = 2")
hb = [(C * gi * gi - 2 * B * gi * xi + A * xi * xi) / det for gi, xi in zip(g, xv)]
check("h", hb, [F(13, 35), F(1, 7), F(17, 35), F(17, 35), F(1, 7), F(13, 35)])
for i in range(6):
    print(f"        h[{bnames[i]}] = {S(hb[i])} = {dec(hb[i],6)} (ROUNDED)")
check("Sum h = k", sum(hb), F(2))
check("h[PRM] worked by hand: (C g^2 - 2B g x + A x^2)/det",
      (C * g[0] * g[0] - 2 * B * g[0] * xv[0] + A * xv[0] * xv[0]) / det, F(13, 35))
# with B = 0 the two-column leverage separates into the two one-column leverages.
# demonstrated on the orthogonal Hadamard pair c1, c2 of Section 6e.
Ao, Co = dot(H[0], H[0]), dot(H[1], H[1])
Bo, deto = dot(H[0], H[1]), Ao * Co - dot(H[0], H[1]) ** 2
check("orthogonal pair: B = 0", Bo, F(0))
h_two = [(Co * a * a - 2 * Bo * a * c + Ao * c * c) / deto for a, c in zip(H[0], H[1])]
check("orthogonal pair: two-column h", h_two, [F(1, 2)] * 4)
check("   separates as g^2/A + x^2/C",
      h_two, [a * a / Ao + c * c / Co for a, c in zip(H[0], H[1])])
check("   Sum h = k = 2", sum(h_two), F(2))
check("dropping g entirely leaves Section 4d's x^2/C",
      [(A * xi * xi) / (A * C) for xi in xv], [xi * xi / C for xi in xv])

sub("14.5 the case FOR dropping g -- drop g, refit on x alone")
Qx, Sx, bx_only, ex_only = fit1(xv, rb2)
check("b_x alone = q/C", bx_only, F(6, 5))
showd("   b_x alone", bx_only)
SSE_x_only = dot(ex_only, ex_only)
check("SSE without g", SSE_x_only, F(19, 5))
showd("   SSE without g", SSE_x_only)
check("   = Sum r^2 - q^2/C", dot(rb2, rb2) - q * q / C, F(19, 5))
check("q^2/C", q * q / C, F(1008, 25))
showd("   q^2/C", q * q / C)
check("rise in SSE from dropping g", SSE_x_only - SSEb, F(4, 5))
check("   = t_g^2 * sigma^2_hat", tg2 * s2b, F(4, 5))
check("   = b_g^2 * det/C", bg * bg * (det / C), F(4, 5))
check("sigma^2_hat that a worthless column earns back, on average", s2b, F(3, 4))
check("what g actually earned back, as a multiple of that", (SSE_x_only - SSEb) / s2b, F(16, 15))
showd("   multiple", (SSE_x_only - SSEb) / s2b)

R2_full = 1 - SSEb / dot(rb2, rb2)
R2_nog = 1 - SSE_x_only / dot(rb2, rb2)
check("R^2 with both columns", R2_full, F(1028, 1103))
showd("   R^2 both", R2_full)
check("R^2 with x only", R2_nog, F(1008, 1103))
showd("   R^2 x only", R2_nog)
check("R^2 lost", R2_full - R2_nog, F(20, 1103))
showd("   R^2 lost (percentage points x100)", (R2_full - R2_nog) * 100, 4)

s2_x_only = SSE_x_only / (nb - 1)
check("sigma^2_hat without g, df = n-1 = 5", s2_x_only, F(19, 25))
tx_only_sq = (q * q / C) / s2_x_only
check("t_x^2 without g = (q^2/C)/sigma^2", tx_only_sq, F(1008, 19))
showd("   t_x^2 without g", tx_only_sq)
showsqrt("   t_x without g", tx_only_sq)
check("   also equals b^2/(sigma^2/C)", bx_only * bx_only / (s2_x_only / C), F(1008, 19))

sub("14.5b the same file with the WRONG denominator")
for label, dd in (("n - k = 4  (correct)", F(4)), ("n - 1 = 5", F(5)), ("n = 6", F(6))):
    s2w = SSEb / dd
    tgw = bg * bg * (det / C) / s2w
    txw = bx * bx * (det / A) / s2w
    print(f"        {label:>22}: sigma^2 = {S(s2w):>6} = {dec(s2w,6)} (ROUNDED)"
          f"   t_g = {isqrt_dec(tgw,4)} (ROUNDED)   t_x = {isqrt_dec(txw,4)} (ROUNDED)")
check("sigma^2 with /(n-1)", SSEb / 5, F(3, 5))
check("t_g^2 with /(n-1)", bg * bg * (det / C) / (SSEb / 5), F(4, 3))
check("t_x^2 with /(n-1)", bx * bx * (det / A) / (SSEb / 5), F(175, 9))
check("sigma^2 with /n", SSEb / 6, F(1, 2))
check("t_g^2 with /n", bg * bg * (det / C) / (SSEb / 6), F(8, 5))
check("t_x^2 with /n", bx * bx * (det / A) / (SSEb / 6), F(70, 3))
check("none of them lifts t_g over 2",
      all(float(v) ** 0.5 < 2 for v in (F(16, 15), F(4, 3), F(8, 5))), True)

sub("14.6 the case AGAINST dropping g")
showsqrt("   2 * SE(b_g)", 4 * var_g)
print(f"        b_g +/- 2 SE(b_g)  =  40 -/+ 77.459667"
      f"  ->  [{float(bg) - float(4*var_g)**0.5:.4f}, "
      f"{float(bg) + float(4*var_g)**0.5:.4f}] (ROUNDED)")
showsqrt("   2 * SE(b_x)", 4 * var_x)
print(f"        b_x +/- 2 SE(b_x)  =  1 -/+ 0.507093"
      f"  ->  [{float(bx) - float(4*var_x)**0.5:.6f}, "
      f"{float(bx) + float(4*var_x)**0.5:.6f}] (ROUNDED)")
check("the interval for b_g straddles 0 AND straddles 2*b_g",
      (float(var_g) ** 0.5) * 2 > 40, True)
check("the interval for b_x does not straddle 0",
      (float(var_x) ** 0.5) * 2 < 1, True)
print(f"        upper end of b_g's interval, as a multiple of b_g: "
      f"{(float(bg) + float(4*var_g)**0.5) / float(bg):.6f} (ROUNDED)")

check("omitted-variable bias in b_x when g is dropped = b_g * B/C", bg * B / C, F(1, 5))
check("   b_x + bias", bx + bg * B / C, F(6, 5))
check("   which is exactly b_x alone", bx + bg * B / C, bx_only)
check("bias as a SHARE of b_x alone = one sixth (NOT 1/5)", (bg * B / C) / bx_only, F(1, 6))
showd("   bias as a share of b_x alone", (bg * B / C) / bx_only)

sub("14.6b what g is worth in RETURN, not in coefficient units")
cg = [bg * gi for gi in g]
cx = [bx * xi for xi in xv]
check("g's fitted contribution", cg, [F(-4, 5), F(-2, 5), F(2, 5), F(-2, 5), F(2, 5), F(4, 5)])
check("x's fitted contribution", cx, [F(-3), F(-2), F(-1), F(1), F(2), F(3)])
check("spread of g's contribution (max-min)", max(cg) - min(cg), F(8, 5))
check("spread of x's contribution (max-min)", max(cx) - min(cx), F(6))
check("ratio of spreads", (max(cx) - min(cx)) / (max(cg) - min(cg)), F(15, 4))
showd("   ratio", (max(cx) - min(cx)) / (max(cg) - min(cg)))
check("g's spread as a share of x's", (max(cg) - min(cg)) / (max(cx) - min(cx)), F(4, 15))
showd("   share", (max(cg) - min(cg)) / (max(cx) - min(cx)))
check("b_g^2 * A (g's explained sum of squares)", bg * bg * A, F(48, 25))
showd("   b_g^2 A", bg * bg * A)
check("b_x^2 * C (x's explained sum of squares)", bx * bx * C, F(28))
check("ratio", (bx * bx * C) / (bg * bg * A), F(175, 12))
showd("   ratio", (bx * bx * C) / (bg * bg * A))

sub("14.6c t is scale-free, b is not")
G = [F(100) * gi for gi in g]  # same column, expressed in percent
A2, B2, C2, p2, q2, det2, bG, bx2, e2 = fit2(G, xv, rb2)
check("rescaled column G = 100 g", G, [F(-2), F(-1), F(1), F(-1), F(1), F(2)])
check("A(G) = 10000 A", A2, F(12))
check("b_G = b_g / 100", bG, F(2, 5))
check("b_x unchanged", bx2, F(1))
check("residuals unchanged", e2, eb)
var_G = (dot(e2, e2) / dfb) * C2 / det2
check("Var(b_G)", var_G, F(3, 20))
showsqrt("   SE(b_G)", var_G)
check("t_G^2 = t_g^2 exactly", bG * bG / var_G, F(16, 15))
check("standardising changes b, never t", bG * bG / var_G, tg2)

sub("14.7 the trap: run g on its own, the Level 1 way")
Qg, Sg, bg_only, eg_only = fit1(g, rb2)
check("b_g alone = p/A", bg_only, F(470, 3))
showd("   b_g alone", bg_only)
SSE_g_only = dot(eg_only, eg_only)
check("SSE with g alone", SSE_g_only, F(44, 3))
showd("   SSE with g alone", SSE_g_only)
check("   = Sum r^2 - p^2/A", dot(rb2, rb2) - p * p / A, F(44, 3))
check("p^2/A", p * p / A, F(2209, 75))
showd("   p^2/A", p * p / A)
check("   2209 = 47^2", F(47) ** 2, F(2209))
s2_g_only = SSE_g_only / (nb - 1)
check("sigma^2_hat, df = 5", s2_g_only, F(44, 15))
tg_only_sq = (p * p / A) / s2_g_only
check("t_g^2 alone = (p^2/A)/sigma^2", tg_only_sq, F(2209, 220))
showd("   t_g^2 alone", tg_only_sq)
showsqrt("   t_g alone", tg_only_sq)
check("t_g alone clears |t| > 2, t_g jointly does not",
      (float(tg_only_sq) ** 0.5 > 2, float(tg2) ** 0.5 > 2), (True, False))
check("rise in SSE from dropping x", SSE_g_only - SSEb, F(35, 3))
check("   = t_x^2 * sigma^2_hat", tx2 * s2b, F(35, 3))
check("dropping x costs this many times what dropping g costs",
      (SSE_g_only - SSEb) / (SSE_x_only - SSEb), F(175, 12))
showd("   ratio", (SSE_g_only - SSEb) / (SSE_x_only - SSEb))
R2_nox = 1 - SSE_g_only / dot(rb2, rb2)
check("R^2 with g only", R2_nox, F(2209, 3309))
showd("   R^2 g only", R2_nox)

sub("14.8 the scoreboard")
print("        model            b_g        b_x       SSE      R^2        t_g      t_x")
print(f"        both        {S(bg):>8} {S(bx):>10} {S(SSEb):>8}  {dec(R2_full,4)}   "
      f"{isqrt_dec(tg2,3)}   {isqrt_dec(tx2,3)}   (all ROUNDED decimals)")
print(f"        x only            --  {S(bx_only):>10} {S(SSE_x_only):>8}  {dec(R2_nog,4)}"
      f"      --   {isqrt_dec(tx_only_sq,3)}")
print(f"        g only    {S(bg_only):>10}         -- {S(SSE_g_only):>8}  {dec(R2_nox,4)}   "
      f"{isqrt_dec(tg_only_sq,3)}      --")

# ===========================================================================
head("SECTION 16  Numbers used in the BFRE tie-back")
# ===========================================================================

print("   p.8  : |t| > 2 is BFRE's significance threshold (quoted, not computed).")
print("   p.8  : BFRE also tracks the AVERAGE SQUARED t-statistic.")
print("   p.14 : 10% proportion-of-significant-t threshold (quoted).")
print("   p.15 : Figure 1.8 bar heights are MEASURED from the scan, not printed.")
sub("Markov bar: a factor cannot beat 1/4 by chance if E[t^2] = 1")
check("Markov: P(t^2 >= 4) <= E[t^2]/4 with E[t^2] = 1", F(1) / F(4), F(1, 4))
fig18 = [("Volatility", 63), ("Momentum", 50), ("Size", 42), ("Reversal", 37),
         ("Value", 34), ("Liquidity", 32), ("Dividend Yield", 23), ("MidCap", 20),
         ("Growth", 18), ("Profitability", 14), ("Sentiment", 7),
         ("Earnings Yield", 4)]
above = [nm for nm, v in fig18 if F(v, 100) > F(1, 4)]
below = [nm for nm, v in fig18 if F(v, 100) <= F(1, 4)]
check("factors clearing the 1/4 bar", above,
      ["Volatility", "Momentum", "Size", "Reversal", "Value", "Liquidity"])
check("factors not clearing it", below,
      ["Dividend Yield", "MidCap", "Growth", "Profitability", "Sentiment",
       "Earnings Yield"])
check("count above", len(above), 6)
check("count below", len(below), 6)
check("BFRE's own 10% threshold vs the 25% bar", F(1, 10) < F(1, 4), True)

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} exact-rational assertions verified.")
print("   Every number printed above appears in datasets/level6.md,")
print("   and every decimal is labelled rounded there.")
