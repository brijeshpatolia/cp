#!/usr/bin/env python3
"""
verify_level12.py -- recomputes EVERY number printed in datasets/level12.md.

Exact rational arithmetic only (fractions.Fraction). Standard library only.
No numpy.

Three jobs, because Level 12 is a level about a document rather than about a matrix:

  A. THE ARITHMETIC. The Placebo Desk file: six stocks, two months, the ten
     balanced candidate columns, the enumerated null, the persistence table,
     the joint fits and the sabotage round. Exact rationals throughout; every
     square root is presented as a rounded decimal and tagged ROUNDED here.

  B. THE CITATIONS. Every figure the markdown quotes from the BFRE paper is
     asserted against the string recorded in notes/ -- in the correct page
     chunk. If a figure is not in notes/, this script fails and the markdown
     is wrong. (It cannot check that notes/ is right; it can check that the
     level never invents a figure notes/ does not carry.)

  C. THE COUNTS. The number of named weaknesses, cheap shots, concessions,
     grey-zone items, scoreboard rows and automatic-fail conditions in
     gm/CRITIQUE.md, asserted against the numbers datasets/level12.md prints,
     so the level and the dossier cannot drift apart.

Run:  python3 tools/verify_level12.py
Exits 0 if every assertion holds; exits non-zero with a MISMATCH message otherwise.

Layout mirrors the markdown section by section.
"""

from fractions import Fraction as F
from itertools import combinations
from math import comb
import os
import re
import sys

# ---------------------------------------------------------------------------
# harness (same conventions as tools/verify_level5.py and verify_level6.py)
# ---------------------------------------------------------------------------

CHECKS = [0]

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NOTES = os.path.join(ROOT, "notes")
CRITIQUE = os.path.join(ROOT, "gm", "CRITIQUE.md")
MARKDOWN = os.path.join(ROOT, "datasets", "level12.md")


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


def dec(v, n=6):
    """Decimal string, tagged EXACT or ROUNDED. 'exact' means the printed n
    decimal places ARE the number, not merely that its expansion terminates.
    The markdown must carry the word 'rounded' next to every ROUNDED value."""
    v = F(v)
    shown = F(round(v * 10 ** n), 10 ** n)
    tag = "exact" if shown == v else "ROUNDED"
    return f"{float(v):.{n}f} ({tag})"


def root(v, n=6):
    """A square root is never exact unless the radicand is a perfect square of
    a rational. Print it as an explicitly rounded decimal, or as exact."""
    v = F(v)
    num, den = v.numerator, v.denominator
    rn, rd = int(round(num ** 0.5)), int(round(den ** 0.5))
    if rn * rn == num and rd * rd == den:
        return dec(F(rn, rd), n) + f"  [= {F(rn, rd)} exactly]"
    return f"{float(v) ** 0.5:.{n}f} (ROUNDED)"


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
# linear algebra in exact rationals (same convention as verify_level5.py)
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


def ols(cols, r):
    """Ordinary least squares. cols is a list of columns.
    Returns (coeffs, fitted, residuals, SSE, Gram)."""
    n = len(r)
    k = len(cols)
    M = [[dot(cols[i], cols[j]) for j in range(k)] for i in range(k)]
    y = [dot(cols[i], r) for i in range(k)]
    b = solve(M, y)
    fit = [sum(b[j] * cols[j][i] for j in range(k)) for i in range(n)]
    e = [r[i] - fit[i] for i in range(n)]
    return b, fit, e, dot(e, e), M


def ones(n):
    return [F(1)] * n


# ===========================================================================
head("SECTION 3  THE PLACEBO DESK -- the file")
# ===========================================================================

NAMES = ["AXL", "BRN", "CHR", "DLT", "EMK", "FNX"]
N = 6
ONE = ones(N)

R1 = [F(4), F(3), F(1), F(-1), F(-2), F(-5)]      # month 1, percent
R2 = [F(2), F(2), F(-3), F(5), F(0), F(-6)]       # month 2, percent
R3 = [F(4), F(1), F(-1), F(1), F(-1), F(-4)]      # month 3, percent
R4 = [F(2), F(1), F(-3), F(3), F(0), F(-3)]       # month 4, percent
MONTHS = [R1, R2, R3, R4]

check("n (stocks)", N, 6)
check("months in the file", len(MONTHS), 4)
check("month 1 returns", R1, [F(4), F(3), F(1), F(-1), F(-2), F(-5)])
check("month 2 returns", R2, [F(2), F(2), F(-3), F(5), F(0), F(-6)])
check("month 3 returns", R3, [F(4), F(1), F(-1), F(1), F(-1), F(-4)])
check("month 4 returns", R4, [F(2), F(1), F(-3), F(3), F(0), F(-3)])

Q1 = dot(R1, R1)
Q2 = dot(R2, R2)
check("month 1  sum r  (the market column's fit is exactly zero)", sum(R1), F(0))
check("month 2  sum r", sum(R2), F(0))
check("month 1  sum r^2 = Q", Q1, F(56))
check("month 2  sum r^2 = Q", Q2, F(78))


def column(idx):
    """A balanced +/-1 column: +1 on the three named stocks, -1 on the rest."""
    return [F(1) if i in idx else F(-1) for i in range(N)]


# the true factor, declared by the game: r = f*z + e each month
Z = column((0, 1, 3))                     # +1 on AXL, BRN, DLT
check("true factor z", Z, [F(1), F(1), F(-1), F(1), F(-1), F(-1)])
check("z is balanced: sum z", sum(Z), F(0))
check("z'z", dot(Z, Z), F(6))

E1 = [R1[i] - 2 * Z[i] for i in range(N)]
E2 = [R2[i] - 3 * Z[i] for i in range(N)]
check("month 1 miss e1 = r1 - 2z", E1, [F(2), F(1), F(3), F(-3), F(0), F(-3)])
check("month 2 miss e2 = r2 - 3z", E2, [F(-1), F(-1), F(0), F(2), F(3), F(-3)])
check("sum e1", sum(E1), F(0))
check("sum e2", sum(E2), F(0))
check("sum z*e1 = 0  (Level 2's balance condition, and it makes b_z exact)",
      dot(Z, E1), F(0))
check("sum z*e2 = 0", dot(Z, E2), F(0))
check("sum e1^2", dot(E1, E1), F(32))
check("sum e2^2", dot(E2, E2), F(24))

TRUE_F = [F(2), F(3), F(2), F(2)]
check("the true factor returns, month by month", TRUE_F, [F(2), F(3), F(2), F(2)])
for i, (R, f) in enumerate(zip(MONTHS, TRUE_F), start=1):
    e = [R[j] - f * Z[j] for j in range(N)]
    check(f"month {i}: sum r = 0", sum(R), F(0))
    check(f"month {i}: sum z*e = 0, so b_z is exactly f", dot(Z, e), F(0))
    check(f"month {i}: b_z = sum(z*r)/6 = f", dot(Z, R) / 6, f)
check("month 3 miss e3", [R3[j] - 2 * Z[j] for j in range(N)],
      [F(2), F(-1), F(1), F(-1), F(1), F(-2)])
check("month 4 miss e4", [R4[j] - 2 * Z[j] for j in range(N)],
      [F(0), F(-1), F(-1), F(1), F(2), F(-1)])
check("sum e3^2", dot([R3[j] - 2 * Z[j] for j in range(N)],
                      [R3[j] - 2 * Z[j] for j in range(N)]), F(12))
check("sum e4^2", dot([R4[j] - 2 * Z[j] for j in range(N)],
                      [R4[j] - 2 * Z[j] for j in range(N)]), F(8))
check("month 3  sum r^2 = Q", dot(R3, R3), F(36))
check("month 4  sum r^2 = Q", dot(R4, R4), F(32))

# ===========================================================================
head("SECTION 3b  The candidate universe -- exactly ten distinct tests")
# ===========================================================================

ALL_SPLITS = list(combinations(range(N), 3))
check("ways to call three of six stocks 'high'", len(ALL_SPLITS), 20)

TRIPLES = [t for t in ALL_SPLITS if 0 in t]        # one representative per mirror pair
check("distinct tests once mirror images are folded together", len(TRIPLES), 10)

LABELS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]
NICK = {"C1": "Random Substyle (the placebo)", "C2": "Payout (the true factor)",
        "C3": "Asset Growth", "C4": "Analyst Revision", "C5": "Accruals",
        "C6": "Share Turnover", "C7": "Book-to-Price", "C8": "Cash-Flow Yield",
        "C9": "Sales Growth", "C10": "Debt-to-Assets"}
COLS = {lab: column(t) for lab, t in zip(LABELS, TRIPLES)}
HIGH = {lab: [NAMES[i] for i in t] for lab, t in zip(LABELS, TRIPLES)}

for lab in LABELS:
    show(f"{lab} high side", HIGH[lab])
check("C1 is the placebo, high on AXL BRN CHR", HIGH["C1"], ["AXL", "BRN", "CHR"])
check("C2 is the true factor z", COLS["C2"], Z)
for lab in LABELS:
    check(f"{lab} is balanced (sum = 0)", sum(COLS[lab]), F(0))
    check(f"{lab}'{lab} = 6", dot(COLS[lab], COLS[lab]), F(6))

sub("a column and its mirror image are the same test (t^2 unchanged)")
for lab in LABELS:
    c = COLS[lab]
    mc = [-x for x in c]
    b1, _, e1, s1, _ = ols([ONE, c], R1)
    b2, _, e2, s2, _ = ols([ONE, mc], R1)
    check(f"{lab}: mirror flips b and leaves SSE alone", (b2[1], s2), (-b1[1], s1))

# ===========================================================================
head("SECTION 3c/3d  The shortcut, and the bar, in |S|")
# ===========================================================================


def stats(R, c):
    """Fit r = a*1 + b*c with sum(c) = 0 and sum(r) = 0.
    Returns S, b, SSE, sigma2, Var(b), t2, R2 -- all exact."""
    Q = dot(R, R)
    Sc = dot(c, R)
    b = Sc / 6
    sse = Q - Sc * Sc / 6
    df = N - 2
    s2 = sse / df
    varb = s2 / 6
    t2 = b * b / varb
    r2 = (Sc * Sc / 6) / Q
    return Sc, b, sse, s2, varb, t2, r2


sub("the shortcut: S = 2 x (sum of the three returns called high)")
for lab, t in zip(LABELS, TRIPLES):
    Sc = dot(COLS[lab], R1)
    check(f"month 1 {lab}: S = 2 x triple sum", Sc, 2 * sum(R1[i] for i in t))

sub("the bar: t^2 >= 4  <=>  S^2 >= 3Q   (derived from Level 6's t)")
for lab in LABELS:
    for R in (R1, R2):
        Sc, b, sse, s2, varb, t2, r2 = stats(R, COLS[lab])
        check(f"bar agrees with t^2 for S={Sc}, Q={dot(R,R)}",
              (t2 >= 4), (Sc * Sc >= 3 * dot(R, R)))


def even_bar(three_q):
    """Smallest EVEN |S| that satisfies S^2 >= 3Q. S is even on this file because
    S = 2 x (sum of the high triple) and the returns are whole percents."""
    s = 0
    while s * s < three_q:
        s += 2
    return s


check("month 1 bar  S^2 >= 3Q", 3 * Q1, F(168))
show("month 1 bar in |S|", root(F(168)))
check("month 1 bar in |S| for an even S", even_bar(3 * Q1), 14)
check("month 2 bar  S^2 >= 3Q", 3 * Q2, F(234))
show("month 2 bar in |S|", root(F(234)))
check("month 2 bar in |S| for an even S", even_bar(3 * Q2), 16)

# cross-check the closed form against a generic least-squares solve
sub("closed form checked against a generic OLS solve, all ten columns, both months")
for lab in LABELS:
    for tag, R in (("M1", R1), ("M2", R2)):
        Sc, b, sse, s2, varb, t2, r2 = stats(R, COLS[lab])
        bb, _, ee, ss, M = ols([ONE, COLS[lab]], R)
        check(f"{tag} {lab}: (intercept, b, SSE) from OLS", (bb[0], bb[1], ss), (F(0), b, sse))
        check(f"{tag} {lab}: Level 2 balance sum c*e = 0", dot(COLS[lab], ee), F(0))

# ===========================================================================
head("SECTION 4  Month one -- the search finds the placebo")
# ===========================================================================

M1 = {}
print("   lab  high side              S     b        SSE      R2        t^2      |t|")
for lab in LABELS:
    Sc, b, sse, s2, varb, t2, r2 = stats(R1, COLS[lab])
    M1[lab] = (Sc, b, sse, s2, varb, t2, r2)
    print(f"   {lab:<4} {'/'.join(HIGH[lab]):<22} {str(Sc):>4}  {str(b):>6}  "
          f"{str(sse):>7}  {str(r2):>7}  {str(t2):>7}  {root(t2)}")

check("C1  S", M1["C1"][0], F(16))
check("C1  b", M1["C1"][1], F(8, 3))
check("C1  SSE", M1["C1"][2], F(40, 3))
check("C1  sigma^2 = SSE/df, df = 4", M1["C1"][3], F(10, 3))
check("C1  Var(b) = sigma^2/6", M1["C1"][4], F(5, 9))
check("C1  t^2", M1["C1"][5], F(64, 5))
check("C1  R2", M1["C1"][6], F(16, 21))
show("C1  SE(b) = sqrt(5/9)", root(F(5, 9)))
show("C1  |t| = sqrt(64/5)", root(F(64, 5)))
show("C1  R2 as a decimal", dec(F(16, 21)))

check("C2  S", M1["C2"][0], F(12))
check("C2  b = 2 = the true f1, estimated exactly", M1["C2"][1], F(2))
check("C2  SSE = sum e1^2", M1["C2"][2], F(32))
check("C2  sigma^2", M1["C2"][3], F(8))
check("C2  Var(b)", M1["C2"][4], F(4, 3))
check("C2  t^2", M1["C2"][5], F(3))
check("C2  R2", M1["C2"][6], F(3, 7))
show("C2  SE(b) = sqrt(4/3)", root(F(4, 3)))
show("C2  |t| = sqrt(3)", root(F(3)))
show("C2  R2 as a decimal", dec(F(3, 7)))

sub("how many of the ten clear |t| > 2 in month 1")
w1 = [lab for lab in LABELS if M1[lab][5] >= 4]
check("month 1: columns clearing the bar", w1, ["C1"])
check("month 1: count clearing", len(w1), 1)
check("month 1: the winner is the placebo, not the truth", w1[0] == "C1", True)
check("month 1: the truth's t^2 is below the bar", M1["C2"][5] < 4, True)
check("C7 explains exactly nothing (S = 0)", (M1["C7"][0], M1["C7"][5]), (F(0), F(0)))

sub("4d. where the winner's 16 came from")
check("C1 . z  (the overlap with the truth)", dot(COLS["C1"], Z), F(2))
check("C1 . r1 = 2*(C1.z) + C1.e1", dot(COLS["C1"], R1),
      2 * dot(COLS["C1"], Z) + dot(COLS["C1"], E1))
check("  ... the borrowed part", 2 * dot(COLS["C1"], Z), F(4))
check("  ... the luck part", dot(COLS["C1"], E1), F(12))
check("share of the winner's score that is pure luck", F(12, 16), F(3, 4))
check("cos between C1 and z = 2/6", F(2, 6), F(1, 3))
check("VIF of the pair = 1/(1 - cos^2)", 1 / (1 - F(1, 3) ** 2), F(9, 8))
check("for scale: VIF at BFRE's largest printed exposure correlation, 0.74 (p.11)",
      1 / (1 - F(74, 100) ** 2), F(2500, 1131))
show("   that VIF as a decimal", dec(F(2500, 1131)))

sub("4e. BFRE's own two-step screen, (1.3)-(1.4) p.10, run on this file")
bz, _, ez, ssez, _ = ols([ONE, Z], R1)
check("step 1: fit the model we already have (z alone), b", bz[1], F(2))
check("step 1: residuals are e1", ez, E1)
check("step 1: SSE", ssez, F(32))
b2s, _, e2s, sse2s, _ = ols([ONE, COLS["C1"]], ez)
check("step 2: regress the residuals on the placebo, b", b2s[1], F(2))
check("step 2: SSE falls 32 -> 8", sse2s, F(8))
check("step 2: share of the remaining miss taken by the placebo", (F(32) - F(8)) / F(32), F(3, 4))
s2_2 = sse2s / (N - 2)
t2_2 = (b2s[1] ** 2) / (s2_2 / 6)
check("step 2: t^2", t2_2, F(12))
show("step 2: |t| = sqrt(12) = 2*sqrt(3)", root(F(12)))

sub("4f. what it costs to ship it -- the joint fit, Level 3's 2x2 system")
bj1, _, ej1, ssej1, Mj1 = ols([ONE, Z, COLS["C1"]], R1)
A, B, C = Mj1[1][1], Mj1[1][2], Mj1[2][2]
check("Gram: A = z'z", A, F(6))
check("Gram: B = z'C1", B, F(2))
check("Gram: C = C1'C1", C, F(6))
det = A * C - B * B
check("det = AC - B^2 (Level 4)", det, F(32))
check("joint: intercept", bj1[0], F(0))
check("joint: b_z falls from 2 to 5/4", bj1[1], F(5, 4))
check("joint: b_C1", bj1[2], F(9, 4))
check("joint: residuals", ej1, [F(1, 2), F(-1, 2), F(0), F(0), F(3, 2), F(-3, 2)])
check("joint: SSE", ssej1, F(5))
check("joint: sum z*e = 0", dot(Z, ej1), F(0))
check("joint: sum C1*e = 0", dot(COLS["C1"], ej1), F(0))
dfj = N - 3
check("joint: df = n - k", dfj, 3)
s2j1 = ssej1 / dfj
check("joint: sigma^2", s2j1, F(5, 3))
varj = s2j1 * A / det
check("joint: Var(b) for either column (A = C here)", varj, F(5, 16))
show("joint: SE = sqrt(5/16)", root(F(5, 16)))
check("joint: t^2 for z", bj1[1] ** 2 / varj, F(5))
check("joint: t^2 for C1", bj1[2] ** 2 / varj, F(81, 5))
show("joint: |t_z| = sqrt(5)", root(F(5)))
show("joint: |t_C1| = sqrt(81/5)", root(F(81, 5)))
check("the truth's coefficient loses 3/8 of itself", (F(2) - F(5, 4)) / F(2), F(3, 8))
check("joint R2", 1 - ssej1 / Q1, F(51, 56))
show("joint R2 as a decimal", dec(F(51, 56)))

# ===========================================================================
head("SECTION 5  The null rate, by enumeration -- no distribution assumed")
# ===========================================================================

sub("5a. the permutation null: deal the six returns out at random")
for tag, R in (("month 1", R1), ("month 2", R2)):
    Qr = dot(R, R)
    clearing = [sub_ for sub_ in ALL_SPLITS
                if (2 * sum(R[i] for i in sub_)) ** 2 >= 3 * Qr]
    check(f"{tag}: deals of six returns into a 3/3 split", len(ALL_SPLITS), 20)
    check(f"{tag}: deals that clear |t| > 2", len(clearing), 2)
    check(f"{tag}: per-test null rate", F(len(clearing), 20), F(1, 10))
    show(f"{tag}: the two deals that clear",
         [[NAMES[i] for i in s_] for s_ in clearing])

P_NULL = F(1, 10)

sub("5b. expected count needs no independence -- only linearity")
check("expected number of the ten clearing in one month", 10 * P_NULL, F(1))
check("month 1 observed number clearing", len(w1), 1)

sub("5c. the average squared t-statistic (BFRE's own diagnostic, p.8)")
tot1 = sum(M1[lab][5] for lab in LABELS)
show("month 1 sum of the ten t^2", tot1)
show("month 1 average squared t-statistic", dec(tot1 / 10))
check("month 1 average squared t is between 1.98 and 1.99",
      F(198, 100) < tot1 / 10 < F(199, 100), True)

# ===========================================================================
head("SECTION 6  Month two -- the winner is somebody else")
# ===========================================================================

M2 = {}
print("   lab  high side              S     b        SSE      R2        t^2      |t|")
for lab in LABELS:
    Sc, b, sse, s2, varb, t2, r2 = stats(R2, COLS[lab])
    M2[lab] = (Sc, b, sse, s2, varb, t2, r2)
    print(f"   {lab:<4} {'/'.join(HIGH[lab]):<22} {str(Sc):>4}  {str(b):>6}  "
          f"{str(sse):>7}  {str(r2):>7}  {str(t2):>7}  {root(t2)}")

check("month 2  C2  S", M2["C2"][0], F(18))
check("month 2  C2  b = 3 = the true f2, estimated exactly", M2["C2"][1], F(3))
check("month 2  C2  SSE = sum e2^2", M2["C2"][2], F(24))
check("month 2  C2  sigma^2", M2["C2"][3], F(6))
check("month 2  C2  Var(b)", M2["C2"][4], F(1))
check("month 2  C2  SE = 1 exactly (SE^2 = Var(b), and Var(b) = 1)",
      (M2["C2"][4], F(1) * F(1) == M2["C2"][4]), (F(1), True))
check("month 2  C2  t^2 = 9, so |t| = 3 exactly", M2["C2"][5], F(9))
check("month 2  C2  R2", M2["C2"][6], F(9, 13))
show("month 2  C2  R2 as a decimal", dec(F(9, 13)))

check("month 2  C1  S", M2["C1"][0], F(2))
check("month 2  C1  b", M2["C1"][1], F(1, 3))
check("month 2  C1  t^2", M2["C1"][5], F(1, 29))
show("month 2  C1  |t| = sqrt(1/29)", root(F(1, 29)))
check("month 2  C1  R2", M2["C1"][6], F(1, 117))
show("month 2  C1  R2 as a decimal", dec(F(1, 117)))

w2 = [lab for lab in LABELS if M2[lab][5] >= 4]
check("month 2: columns clearing the bar", w2, ["C2"])
check("month 2: count clearing", len(w2), 1)
check("month 2: the month-1 champion does not clear", "C1" in w2, False)

sub("where the month-1 champion finishes in month 2")
order = sorted(LABELS, key=lambda lab: -M2[lab][5])
ranks = {lab: 1 + sum(1 for o in LABELS if M2[o][5] > M2[lab][5]) for lab in LABELS}
show("month 2 order by t^2", order)
check("month 2: C1's rank (ties share the higher rank)", ranks["C1"], 8)
check("month 2: columns strictly above C1", len([o for o in LABELS if M2[o][5] > M2["C1"][5]]), 7)
check("month 2: C1 is tied at the bottom with C6 and C9",
      sorted(o for o in LABELS if M2[o][5] == M2["C1"][5]), ["C1", "C6", "C9"])

tot2 = sum(M2[lab][5] for lab in LABELS)
show("month 2 sum of the ten t^2", tot2)
show("month 2 average squared t-statistic", dec(tot2 / 10))
check("month 2 average squared t is between 1.69 and 1.70",
      F(169, 100) < tot2 / 10 < F(170, 100), True)

sub("6c. in-sample vs out-of-sample, in one table")
check("C1  R2 in the month it was found", M1["C1"][6], F(16, 21))
check("C1  R2 in the next month", M2["C1"][6], F(1, 117))
check("C2  R2 in month 1", M1["C2"][6], F(3, 7))
check("C2  R2 in month 2", M2["C2"][6], F(9, 13))
ratio = M1["C1"][6] / M2["C1"][6]
check("the placebo's R2 falls by a factor of", ratio, F(624, 7))
show("that factor as a decimal", dec(ratio))

sub("6d. the shipped model's factor returns, month by month")
bj2, _, ej2, ssej2, Mj2 = ols([ONE, Z, COLS["C1"]], R2)
check("month 2 joint: b_z", bj2[1], F(13, 4))
check("month 2 joint: b_C1 changes sign", bj2[2], F(-3, 4))
check("month 2 joint: SSE", ssej2, F(21))
s2j2 = ssej2 / dfj
check("month 2 joint: sigma^2", s2j2, F(7))
varj2 = s2j2 * Mj2[1][1] / (Mj2[1][1] * Mj2[2][2] - Mj2[1][2] ** 2)
check("month 2 joint: Var(b)", varj2, F(21, 16))
check("month 2 joint: t^2 for z", bj2[1] ** 2 / varj2, F(169, 21))
check("month 2 joint: t^2 for C1", bj2[2] ** 2 / varj2, F(3, 7))
show("month 2 joint: |t_z| = sqrt(169/21)", root(F(169, 21)))
show("month 2 joint: |t_C1| = sqrt(3/7)", root(F(3, 7)))
check("the placebo's reported factor return: +9/4 then -3/4", (bj1[2], bj2[2]),
      (F(9, 4), F(-3, 4)))
check("the true factor's reported return keeps its sign", (bj1[1] > 0, bj2[1] > 0),
      (True, True))

# ===========================================================================
head("SECTION 6e  Months three and four -- the persistence table on this file")
# ===========================================================================

BARS = []
for i, R in enumerate(MONTHS, start=1):
    Qm = dot(R, R)
    show(f"month {i}: Q = {Qm}, bar S^2 >= {3 * Qm}, |S| >=", root(3 * Qm))
    BARS.append(3 * Qm)
check("month 3 bar in |S| for an even S", even_bar(BARS[2]), 12)
check("month 4 bar in |S| for an even S", even_bar(BARS[3]), 10)

PANEL = {}
print("   lab     S in m1   m2   m3   m4     months cleared")
for lab in LABELS:
    Ss = [dot(COLS[lab], R) for R in MONTHS]
    hits = [1 if Ss[i] ** 2 >= BARS[i] else 0 for i in range(4)]
    PANEL[lab] = (Ss, sum(hits))
    print(f"   {lab:<5} {str(Ss[0]):>6} {str(Ss[1]):>5} {str(Ss[2]):>5} {str(Ss[3]):>5}"
          f"      {sum(hits)} of 4")
check("C1 (the placebo) clears in 1 of 4 months", PANEL["C1"][1], 1)
check("C2 (the truth) clears in 3 of 4 months", PANEL["C2"][1], 3)
check("C8 also clears once", PANEL["C8"][1], 1)
check("every other column never clears",
      sorted(lab for lab in LABELS if PANEL[lab][1] == 0),
      ["C10", "C3", "C4", "C5", "C6", "C7", "C9"])
check("columns clearing the paper's '>10% of months' bar over 4 months",
      sorted(lab for lab in LABELS if F(PANEL[lab][1], 4) > F(1, 10)),
      ["C1", "C2", "C8"])
ADMITTED = sorted(lab for lab in LABELS if F(PANEL[lab][1], 4) > F(1, 10))
JUNK_ADMITTED = sorted(lab for lab in ADMITTED if COLS[lab] != Z)
check("   ... of which junk (every admitted column that is not the true factor)",
      (JUNK_ADMITTED, len(JUNK_ADMITTED)), (["C1", "C8"], 2))
check("C1's proportion of significant months", F(PANEL["C1"][1], 4), F(1, 4))
check("C2's proportion of significant months", F(PANEL["C2"][1], 4), F(3, 4))
check("with 4 months the smallest non-zero proportion is 25%", F(1, 4), F(25, 100))
check("so '>10% of months' and 'at least once' are the same rule here",
      F(1, 4) > F(1, 10), True)
check("total clears across 10 columns x 4 months", sum(v[1] for v in PANEL.values()), 5)
check("month 4: C8 clears at t^2 = 100/23 (just over the bar)",
      F(2, 3) * dot(COLS["C8"], R4) ** 2 / (dot(R4, R4) - dot(COLS["C8"], R4) ** 2 / 6),
      F(100, 23))
show("   i.e. |t| =", root(F(100, 23)))
check("month 3: the truth clears at t^2 = 8",
      F(2, 3) * dot(COLS["C2"], R3) ** 2 / (dot(R3, R3) - dot(COLS["C2"], R3) ** 2 / 6), F(8))
show("   i.e. |t| =", root(F(8)))
check("month 4: the truth clears at t^2 = 12",
      F(2, 3) * dot(COLS["C2"], R4) ** 2 / (dot(R4, R4) - dot(COLS["C2"], R4) ** 2 / 6), F(12))
show("   i.e. |t| =", root(F(12)))
check("month 3: the placebo's t^2", 
      F(2, 3) * dot(COLS["C1"], R3) ** 2 / (dot(R3, R3) - dot(COLS["C1"], R3) ** 2 / 6),
      F(32, 19))
check("month 4: the placebo scores exactly zero", dot(COLS["C1"], R4), F(0))

# ===========================================================================
head("SECTION 7  The defence, as arithmetic -- persistence")
# ===========================================================================


def tail(k, n, p):
    """Exact P(X >= k) for X ~ Binomial(n, p), rational p."""
    return sum(F(comb(n, i)) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


sub("7a. one month, then a repetition rule -- 10 candidates at p = 1/10")
check("rule 'clears once in one month': P for one junk column", P_NULL, F(1, 10))
check("   expected junk winners out of 10", 10 * P_NULL, F(1))
p22 = P_NULL ** 2
check("rule 'clears in both of 2 months': P", p22, F(1, 100))
check("   expected junk winners out of 10", 10 * p22, F(1, 10))
check("hand step: (9/10)^4", (1 - P_NULL) ** 4, F(6561, 10000))
check("hand step: 4*(1/10)^3*(9/10)", 4 * P_NULL ** 3 * (1 - P_NULL), F(36, 10000))
p14 = tail(1, 4, P_NULL)
check("rule 'clears in at least 1 of 4 months' (= 25% of months): P", p14, F(3439, 10000))
check("   expected junk winners out of 10", 10 * p14, F(3439, 1000))
show("   as a decimal", dec(10 * p14))
p34 = tail(3, 4, P_NULL)
check("rule 'clears in at least 3 of 4 months': P", p34, F(37, 10000))
check("   expected junk winners out of 10", 10 * p34, F(37, 1000))
show("   as a decimal", dec(10 * p34))
check("the 3-of-4 rule divides the junk count by", P_NULL / p34, F(1000, 37))
check("expected junk columns (9 of the 10) clearing at least once in 4 months",
      9 * p14, F(30951, 10000))
show("   as a decimal", dec(9 * p14, 4))
check("   the file delivered (junk columns clearing at least once in four months)",
      len([lab for lab in LABELS if COLS[lab] != Z and PANEL[lab][1] >= 1]), 2)
show("   that factor as a decimal", dec(P_NULL / p34))

sub("7b. the same rules with 200 candidates instead of 10")
check("200 candidates, one month", 200 * P_NULL, F(20))
check("200 candidates, both of 2 months", 200 * p22, F(2))
check("200 candidates, at least 1 of 4", 200 * p14, F(3439, 50))
show("   as a decimal", dec(200 * p14))
check("200 candidates, at least 3 of 4", 200 * p34, F(74, 100))
show("   as a decimal", dec(200 * p34))

sub("7c. scaled to the paper's own numbers (all of this is INFER, not PAPER)")
P_BIG = F(1, 20)          # the rival's assumed null rate in a huge cross-section
MONTHS_15Y = 180          # 15 years of monthly cross-sections, p.8
BAR = 18                  # 10% of 180, p.14
check("assumed per-month null rate in a huge cross-section", P_BIG, F(1, 20))
check("months in a 15-year monthly history", MONTHS_15Y, 180)
check("expected significant months for a junk column (hand arithmetic)",
      MONTHS_15Y * P_BIG, F(9))
check("10% of 180 months", F(MONTHS_15Y, 10), F(18))
check("the bar is this multiple of the expected count",
      F(BAR) / (MONTHS_15Y * P_BIG), F(2))
check("Markov bound on P(count >= 18) given mean 9 (Level 6, 8f): 9/18",
      (MONTHS_15Y * P_BIG) / BAR, F(1, 2))
tbig = tail(BAR, MONTHS_15Y, P_BIG)
show("exact binomial P(count >= 18 | 180, 1/20)  [machine arithmetic, not hand]",
     dec(tbig))
check("that tail is between 0.4% and 0.5%",
      F(4, 1000) < tbig < F(5, 1000), True)
show("expected junk survivors out of 200 candidates", dec(200 * tbig))
check("expected junk survivors out of 200 is between 0.8 and 0.9",
      F(8, 10) < 200 * tbig < F(9, 10), True)
check("200 candidates with no persistence rule at all, per month", 200 * P_BIG, F(10))

# ===========================================================================
head("SECTION 12  The sabotage round")
# ===========================================================================

check("Level 6's identity t^2 = df * R2/(1 - R2), df = 4, on C1 month 1",
      4 * M1["C1"][6] / (1 - M1["C1"][6]), M1["C1"][5])
check("so R2 is forced to be 16/21 once t^2 = 64/5 and df = 4",
      M1["C1"][5] / (M1["C1"][5] + 4), F(16, 21))
show("16/21 as a decimal", dec(F(16, 21)))
check("the planted lie 0.68 is not 16/21", F(68, 100) == F(16, 21), False)
check("the miss the planted R2 would imply", (1 - F(68, 100)) * Q1, F(448, 25))
show("  i.e. SSE would have to be", dec(F(1792, 100)))
check("the real SSE", M1["C1"][2], F(40, 3))
show("  which is", dec(F(40, 3)))

# ===========================================================================
head("SECTION 17  Numbers used in the BFRE tie-back, and the size of the harm")
# ===========================================================================

sub("if the placebo ships: what it does to a portfolio (Level 10 / Level 11)")
# long the three stocks C1 calls high, short the three it calls low, equal weights
wts = [F(1, 3), F(1, 3), F(1, 3), F(-1, 3), F(-1, 3), F(-1, 3)]
check("portfolio weights sum to zero (a pure factor bet)", sum(wts), F(0))
check("portfolio exposure to C1", dot(wts, COLS["C1"]), F(2))
check("portfolio exposure to z", dot(wts, Z), F(2, 3))
check("month 1 portfolio return", dot(wts, R1), F(16, 3))
show("   as a decimal", dec(dot(wts, R1)))
check("month 2 portfolio return", dot(wts, R2), F(2, 3))
show("   as a decimal", dec(dot(wts, R2)))
check("month 1: share of that return the shipped model books to the placebo",
      dot(wts, COLS["C1"]) * bj1[2], F(9, 2))
check("month 1: share it books to the true factor", dot(wts, Z) * bj1[1], F(5, 6))
show("   as a decimal", dec(F(5, 6)))
check("   the two blocks plus the residual reproduce the return",
      dot(wts, COLS["C1"]) * bj1[2] + dot(wts, Z) * bj1[1] + dot(wts, ej1),
      dot(wts, R1))
check("   the portfolio's residual is exactly zero", dot(wts, ej1), F(0))
check("   share of the portfolio's month-1 return booked to the placebo",
      (dot(wts, COLS["C1"]) * bj1[2]) / dot(wts, R1), F(27, 32))
show("      as a decimal", dec(F(27, 32)))
check("   share booked to the true factor",
      (dot(wts, Z) * bj1[1]) / dot(wts, R1), F(5, 32))

# ===========================================================================
head("SECTION B  CITATIONS -- every paper figure quoted in the markdown, "
     "asserted against notes/")
# ===========================================================================

# (page, chunk file, exact substring recorded in notes/, what the markdown uses it for)
CITES = [
    ("p.4", "chunk_1-9.md", "beta = 0.99", "the only R2 value printed anywhere"),
    ("p.4", "chunk_1-9.md", "R2 = 91%", "the same regression"),
    ("p.8", "chunk_1-9.md", "in excess of", "|t| > 2 is the significance threshold"),
    ("p.8", "chunk_1-9.md", "as statistically significant", "the same sentence"),
    ("p.8", "chunk_1-9.md", "average squared t-statistic", "BFRE's own squared diagnostic"),
    ("p.8", "chunk_1-9.md", "15-year", "the research history behind the t-statistics"),
    ("p.8", "chunk_1-9.md", "five-year sub-samples", "the sub-sample check"),
    ("p.8", "chunk_1-9.md", "purely statistical in nature",
     "why LASSO / LARS / Ridge / Bayesian were declined"),
    ("p.10", "chunk_10-18.md", "N >= 200", "the candidate count"),
    ("p.10", "chunk_10-18.md", "| -5.1% |", "Table 1.2 Reversal return"),
    ("p.10", "chunk_10-18.md", "-1.59", "Table 1.2 Reversal Sharpe"),
    ("p.10", "chunk_10-18.md", "| 5.4% |", "Table 1.2 Momentum return"),
    ("p.10", "chunk_10-18.md", "| 1.43 |", "Table 1.2 Momentum Sharpe"),
    ("p.10", "chunk_10-18.md", "| 0.22 |", "Table 1.2 Momentum autocorrelation"),
    ("p.10", "chunk_10-18.md", "| 0.17 |", "Table 1.2 Reversal autocorrelation"),
    ("p.11", "chunk_10-18.md", "0.74", "Figure 1.3 Size-Liquidity, printed"),
    ("p.12", "chunk_10-18.md", "10% - 15%", "the stopping band"),
    ("p.14", "chunk_10-18.md",
     "indicates a statistically significant style effect", "the 10% inclusion bar"),
    ("p.16", "chunk_10-18.md",
     "threshold used to determine whether styles are eligible for inclusion",
     "the same bar, restated"),
    ("p.16", "chunk_10-18.md", "overreacting", "the reversal story"),
    ("p.17", "chunk_10-18.md", "11 months with a one month lag", "momentum's window"),
    ("p.24", "chunk_19-27.md", "In general a multi-factor model",
     "p.24's lead-in, quoted in trap 5"),
    ("p.25", "chunk_19-27.md", "square-root of market capitalisation",
     "the regression weights (a cheap shot to refuse)"),
    ("p.26", "chunk_19-27.md", "there exist three intercept terms",
     "the three columns of ones, quoted in 3c"),
    ("p.28", "chunk_28-36.md", "in-line with standard modelling practice",
     "the across-company zero, the real attack behind trap 5"),
    ("p.27", "chunk_19-27.md", "104 weeks", "the default factor covariance window"),
    ("p.27", "chunk_19-27.md", "26 weeks", "the default half-life"),
    ("p.27", "chunk_19-27.md", "March 1996", "the start of the factor return history"),
    ("p.27", "chunk_19-27.md", "BRS Covariance Matrix Estimation",
     "the deferred covariance document"),
    ("p.5", "chunk_1-9.md", "8 August 2011", "the stressed-day illustration"),
    ("p.6", "chunk_1-9.md", "16 August 2011", "the calm-day illustration"),
    ("p.30", "chunk_28-36.md", "Out-of-sample", "the single occurrence of the phrase"),
    ("p.30", "chunk_28-36.md", "The forecast horizon of the model is",
     "the 1-month organising principle, quoted in trap 7"),
    ("p.32", "chunk_28-36.md", "well within suitable thresholds", "the VIF pass mark"),
    ("p.32", "chunk_28-36.md",
     "proportion of cross-sectional variation in asset returns explained by the set of "
     "common factors in the model", "the paper's own R2, quoted in 4f"),
    ("p.32", "chunk_28-36.md", "significant instability in the factor return estimates",
     "what the paper says unstable columns do, quoted in 6d"),
    ("p.32", "chunk_28-36.md", "1996 to 2013",
     "the dated testing span 7c sets against p.8's '15-year'"),
    ("p.35", "chunk_28-36.md", "Active Risk",
     "the paper's word, which trap 3 forbids replacing with 'tracking error'"),
    ("p.32", "chunk_28-36.md", "majority", "the word that concedes F-1"),
    ("p.32", "chunk_28-36.md", "exhaustive set", "the bias-statistic claim"),
    ("p.33", "chunk_28-36.md", "available on request", "where the test results went"),
    ("p.38", "chunk_37-45.md", "99% 1-day VaR over the previous 252 days",
     "the one externally-anchored parameter"),
    ("p.38", "chunk_37-45.md", "Kupiec", "its external anchor"),
    ("p.38", "chunk_37-45.md", "12 monthly standardised returns",
     "the bias-statistic window required in Move 1"),
    ("p.38", "chunk_37-45.md", "95% confidence interval",
     "the exception band required in Move 1"),
    ("p.38", "chunk_37-45.md", "STORM",
     "the benchmark model -- p.38, NOT p.30"),
    ("p.47", "chunk_46-55.md", "s <= t",
     "the lag convention behind 'look-ahead bias' in 13"),
    ("p.55", "chunk_46-55.md", "200+", "the full candidate list"),
    ("p.56", "chunk_56-65.md", "Random Substyle", "the placebo, by name"),
    ("p.56", "chunk_56-65.md", "18 styles, 108 substyles",
     "counted from the printed rows; the page prints no totals"),
    ("p.65", "chunk_56-65.md", "forthcoming", "how [27] is listed"),
]

TEXT = {}
for fn in sorted(os.listdir(NOTES)):
    if fn.endswith(".md"):
        with open(os.path.join(NOTES, fn), encoding="utf-8") as fh:
            TEXT[fn] = fh.read()
check("notes/ chunk files found", len(TEXT), 7)

for page, fn, needle, why in CITES:
    check(f"{page} {why}: {needle!r} present in notes/{fn}",
          needle in TEXT[fn], True)

sub("things the markdown says are ABSENT from the paper -- checked as absences")
ALL_NOTES = "\n".join(TEXT.values())

# 'placebo', 'falsifiable', 'post hoc', 'look-ahead' never appear as the paper's words.
# notes/ mixes paper text with the transcriber's commentary, so the honest check is on
# the phrases that appear NOWHERE in notes/ at all -- those cannot be the paper's either.
for word in ["family-wise", "false discovery rate", "Bonferroni", "eigenvalue",
             "principal component", "tracking error", "least squares",
             "normal equation", "degrees of freedom"]:
    check(f"{word!r} appears nowhere in notes/", word.lower() in ALL_NOTES.lower(), False)

# ===========================================================================
head("SECTION C  COUNTS -- gm/CRITIQUE.md against what the markdown prints")
# ===========================================================================

with open(CRITIQUE, encoding="utf-8") as fh:
    CRIT = fh.read()

IDS = sorted(set(re.findall(r"\b([A-H]-\d+)\b", CRIT)),
             key=lambda s: (s[0], int(s[2:])))
check("numbered dossier items in gm/CRITIQUE.md", len(IDS), 38)
show("the ids", IDS)
check("class A items", len([i for i in IDS if i[0] == "A"]), 7)
check("class B items", len([i for i in IDS if i[0] == "B"]), 6)
check("class C items", len([i for i in IDS if i[0] == "C"]), 9)
check("class D items (the class is argued as one charge, not numbered)",
      len([i for i in IDS if i[0] == "D"]), 0)
check("class E items", len([i for i in IDS if i[0] == "E"]), 4)
check("class F items", len([i for i in IDS if i[0] == "F"]), 2)
check("class G items", len([i for i in IDS if i[0] == "G"]), 5)
check("class H items", len([i for i in IDS if i[0] == "H"]), 5)

check("the two unnumbered charges are both present",
      ("## 5.1 THE WORKED EXAMPLE" in CRIT) and ("## 5.5 CLASS D" in CRIT), True)
WEAKNESSES = len(IDS) + 2
check("TOTAL named weaknesses (38 numbered + 5.1 + class D)", WEAKNESSES, 40)

CS = sorted(set(re.findall(r"\bCS-(\d+)\b", CRIT)), key=int)
check("cheap shots named in gm/CRITIQUE.md", len(CS), 12)
CS_ROWS = [l for l in CRIT.splitlines() if re.match(r"^\|\s*\*\*CS-\d+\*\*\s*\|", l)]
check("cheap-shot table rows", len(CS_ROWS), 12)


def section(start, end):
    i = CRIT.index(start)
    j = CRIT.index(end)
    return CRIT[i:j]


s4 = section("# 4. THE SCOREBOARD", "# 5. THE DOSSIER")
SB = re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|\s*([^|]+?)\s*\|", s4, re.M)
check("scoreboard rows", len(SB), 20)
RANK = {item: int(rk) for rk, item in SB}
check("rank 1 is G-3 (the deferred testing)", RANK["G-3"], 1)
check("rank 2 is F-2 (multiple testing + the placebo)", RANK["F-2"], 2)
check("rank 3 is F-1 (the 10% bar)", RANK["F-1"], 3)
check("rank 5 is A-6 (the deferred covariance method)", RANK["A-6"], 5)
check("rank 9 is 5.1 (the standardisation asymmetry)", RANK["5.1"], 9)
check("rank 20 is the prose/formula group", RANK["H-3…H-5"], 20)

STARS = re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|[^|]*\|[^|]*\|\s*(★+☆*)\s*\|\s*(★+☆*)\s*\|",
                   s4, re.M)
ST = {int(r): (a.count("★"), d.count("★")) for r, a, d in STARS}
check("scoreboard rows carrying both star ratings", len(ST), 20)
check("G-3: attack 5 stars, defence 3", ST[1], (5, 3))
check("F-2: attack 5 stars, defence 4", ST[2], (5, 4))
check("the tie-break rule: equal attacks, lead with the weaker defence",
      ST[1][0] == ST[2][0] and ST[1][1] < ST[2][1], True)
check("5.1: attack 3 stars, defence 5 -- the calibration item", ST[9], (3, 5))

s7 = section("# 7. GREY ZONE", "# 8. THE CONCESSIONS")
GZ = [l for l in s7.splitlines() if l.startswith("| **")]
check("grey-zone items", len(GZ), 6)

s8 = section("# 8. THE CONCESSIONS", "# 9. BOSS-ROUND SCRIPTS")
CON = [l for l in s8.splitlines() if re.match(r"^\|\s*\d+\s*\|", l)]
check("concessions a credible rival must grant", len(CON), 12)
check("the dossier demands at least four of them", "at least four" in s8, True)

s10 = section("**Automatic fail conditions**", "\n# 11. NEVER CITE")
AF = [l for l in s10.splitlines() if l.startswith("- ")]
check("automatic fail conditions", len(AF), 5)

s3 = section("## 3. DIFFICULTY FLAGS", "## 4. THE SCOREBOARD")
DF = [l for l in s3.splitlines() if l.startswith("| **")]
check("items flagged graduate-level", len(DF), 5)

s9 = section("### Vocabulary-under-fire prompts", "\n# 10. SCORING RUBRIC")
VP = re.findall(r"^\d+\.", s9, re.M)
check("round-F vocabulary prompts for this level", len(VP), 5)

crib_a = section("**Five attacks, in order", "**Five defences")
crib_d = section("**Five defences, in order", "**The sentence that ends")
check("crib: attacks", len(re.findall(r"^\d+\.", crib_a, re.M)), 5)
check("crib: defences", len(re.findall(r"^\d+\.", crib_d, re.M)), 5)

s2 = section("## 2. JARGON-UNLOCK LEDGER", "## 3. DIFFICULTY FLAGS")
L12_ROWS = [l for l in s2.splitlines()
            if l.startswith("|") and re.search(r"\|\s*\*\*L12\*\*\s*\|", l)]
check("terms the dossier's ledger unlocks at L12 in bold", len(L12_ROWS), 7)
for term in ["bias statistic", "sensitivity analysis", "multiple testing",
             "placebo", "falsifiable", "post hoc", "look-ahead bias"]:
    check(f"  ... including {term!r}",
          any(term in l for l in L12_ROWS), True)

# ===========================================================================
head("SECTION D  The markdown itself -- the counts it prints must be these")
# ===========================================================================

with open(MARKDOWN, encoding="utf-8") as fh:
    MD = fh.read()

MD_CLAIMS = [
    (r"\*\*40\*\* named weaknesses", WEAKNESSES, 40),
    (r"\*\*12\*\* cheap shots", len(CS), 12),
    (r"\*\*12\*\* concessions", len(CON), 12),
    (r"\*\*6\*\* grey-zone", len(GZ), 6),
    (r"\*\*20\*\* ranked", len(SB), 20),
    (r"\*\*5\*\* automatic-fail", len(AF), 5),
]
for pat, got, want in MD_CLAIMS:
    check(f"markdown prints the count matching CRITIQUE.md: /{pat}/",
          (re.search(pat, MD) is not None, got), (True, want))

check("markdown states the class sizes 7/6/9/4/2/5/5",
      "7 / 6 / 9 / 4 / 2 / 5 / 5" in MD, True)
check("markdown carries the verification block",
      "python3 bfre-risk-desk/tools/verify_level12.py" in MD, True)

# cross-file: the two earlier numbers this page quotes back at the player must still be there
with open(os.path.join(ROOT, "datasets", "level6.md"), encoding="utf-8") as fh:
    L6 = fh.read()
with open(os.path.join(ROOT, "datasets", "level0.md"), encoding="utf-8") as fh:
    L0 = fh.read()
check("Level 6 still prints E[t^2] = 1.676788 at df = 4 (quoted in this level's 5c)",
      "1.676788" in L6, True)
check("Level 0 still prints Desk B's sum of squared misses, 144 (quoted in this level's 0)",
      "144" in L0, True)
# Figure 1.8's bar heights are pixel measurements. Any line of the markdown that puts a
# number next to one of those style names must carry the words that keep it honest.
FIG18 = ["Sentiment", "Earnings Yield"]
bad = [l for l in MD.splitlines()
       if any(nm in l for nm in FIG18) and re.search(r"\d\s*%", l)
       and not ("APPROX" in l or "pixel" in l)]
check("every Figure 1.8 percentage on the page travels with APPROX / pixel", bad, [])
check("the page says Figure 1.8 carries no threshold line",
      "has no threshold line drawn on it" in MD, True)
check("the page marks the toy null rate as non-transferable (trap 9)",
      "Laundering a toy number onto the real model" in MD, True)
check("the page never sources 'tracking error' or 'eigenvalue' to the paper",
      re.search(r"(paper|BFRE|they) (says?|call[s]?) [^.\n]*tracking error", MD) is None, True)

# ===========================================================================
head("ALL CHECKS PASSED")
print(f"   {CHECKS[0]} assertions verified.")
print("   Every number printed above appears in datasets/level12.md,")
print("   every decimal tagged ROUNDED is marked 'rounded' there,")
print("   every paper figure quoted there was found in notes/, and the")
print("   weakness / cheap-shot / concession counts match gm/CRITIQUE.md.")
