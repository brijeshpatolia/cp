from fractions import Fraction as F

# LEVEL 0 BOSS: three desks, same factor return b = 2, IDENTICAL raw sum of misses (= 0),
# wildly different quality. Built residual-first so every number is exact.
b = F(2)
x = [F(-2), F(-1), F(1), F(2)]

desks = {
    "Desk A (tight)":     [F('1/2'), F('-1/2'), F('-1/2'), F('1/2')],
    "Desk B (blown out)": [F(6),     F(-6),     F(-6),     F(6)],
    "Desk C (perfect)":   [F(0),     F(0),      F(0),      F(0)],
}
for name, e in desks.items():
    r = [b*xi + ei for xi, ei in zip(x, e)]
    raw   = sum(e)
    absS  = sum(abs(ei) for ei in e)
    sq    = sum(ei*ei for ei in e)
    bal   = sum(xi*ei for xi, ei in zip(x, e))
    refit = sum(xi*ri for xi, ri in zip(x, r)) / sum(xi*xi for xi in x)
    print(f"{name}")
    print(f"   x         = {[str(v) for v in x]}")
    print(f"   r         = {[str(v) for v in r]}")
    print(f"   misses    = {[str(v) for v in e]}")
    print(f"   RAW SUM   = {raw}      <-- identical across all three desks")
    print(f"   sum |e|   = {absS}")
    print(f"   sum e^2   = {sq}")
    print(f"   sum x*e   = {bal}   (balance holds -> b=2 really is the least-squares fit)")
    print(f"   refit b   = {refit}")
    print()

# Why squares and not absolute values: absolute value has no unique/stable minimum here.
xs = [F(1), F(1), F(1)]
rs = [F(1), F(2), F(9)]
print("Squares vs absolutes, x = [1,1,1], r = [1,2,9]:")
for cand in [F(1), F(2), F(3), F(4), F(9), F(12,3)]:
    sa = sum(abs(ri - cand*xi) for xi, ri in zip(xs, rs))
    ss = sum((ri - cand*xi)**2 for xi, ri in zip(xs, rs))
    print(f"   b={str(cand):>4}  sum|e| = {str(sa):>4}   sum e^2 = {str(ss):>5} ({float(ss):.3f})")
print("   least-squares b = ", sum(xi*ri for xi,ri in zip(xs,rs))/sum(xi*xi for xi in xs), "(the mean)")
print("   least-absolutes b =  2  (the median) -- ignores the 9 entirely")
