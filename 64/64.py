from decimal import *
getcontext().prec = 250

def squareRootPeriod(d):
    """Input and int and output a continued fraction representation of its sqrt"""
    r = Decimal(d).sqrt()
    remainders = []
    h,k,a = [0,1],[1,0],[]
    n = 0
    while True:
        a.append(int(r))
        r -= a[-1]
        if float(r) not in remainders:
            remainders.append(float(r))
        else:
            return len(a)-1
        r = 1/r
        h.append((a[-1]*h[-1])+h[-2])
        k.append((a[-1]*k[-1])+k[-2])
        n += 1

roots = [x for x in range(2,10_001) if x**.5 % 1 != 0]
ans = 0
for root in roots:
    if squareRootPeriod(root) % 2 != 0:
        ans += 1
print(ans)

