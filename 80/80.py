#This program solves Project Euler #80.

from decimal import *
getcontext().prec = 110

def digitalSum(n):
    """
    Return the sum of the first one hundred decimal digits of the square
    root of the inputed number.
    """
    decimalDigits = str(Decimal(n).sqrt())
    decimalDigits = decimalDigits.replace('.','')
    decimalDigits = [int(x) for x in decimalDigits[:100]]
    return sum(decimalDigits)

ans = 0    
for n in range(2,101):
    if n**.5 % 1 != 0: #skip perfect squares.
        ans += digitalSum(n)
print(ans)
