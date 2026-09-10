from fractions import Fraction as F

def frac(*a): return [F(v) for v in a]

x  = frac('-3/2','-1/2','0','1','2')
r  = frac('-2','-2','1/2','4','7/2')
S2 = sum(xi*xi for xi in x)
Sxr= sum(xi*ri for xi,ri in zip(x,r))
b  = Sxr/S2
print("x  =", [str(v) for v in x])
print("r  =", [str(v) for v in r])
print("sum x   =", sum(x))
print("sum x^2 =", S2)
print("sum x*r =", Sxr)
print("b_ols   =", b, "=", float(b))
naive_total = sum(r)/sum(x)
ratios = [ri/xi for xi,ri in zip(x,r) if xi!=0]
naive_avg = sum(ratios)/len(ratios)
print("sum r   =", sum(r))
print("naive total-r/total-x =", naive_total, "=", float(naive_total))
print("ratios r/x            =", [f'{float(v):.4f}' for v in ratios])
print("naive average ratio   =", naive_avg, "=", float(naive_avg))
e = [ri - b*xi for xi,ri in zip(x,r)]
print("residuals =", [str(v) for v in e])
print("  sum e   =", sum(e), "(not zero: no-intercept fit)")
print("  sum x*e =", sum(xi*ei for xi,ei in zip(x,e)), "(zero: balance condition)")
print("  sum e^2 =", sum(ei*ei for ei in e), "=", float(sum(ei*ei for ei in e)))
for cand in [F(2), naive_total, naive_avg, F(3,2), F(5,2)]:
    ss = sum((ri-cand*xi)**2 for xi,ri in zip(x,r))
    print(f"  SS at b={float(cand):.4f} -> {float(ss):.4f}")
