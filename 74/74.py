from math import factorial
from time import time

start = time()

def digitsFactorial(n):
    n = str(n)
    digits = [factorial(int(x)) for x in n]
    return sum(digits)

def digitFactorialChainLen(n):
    chain = [n,]
    while True:
        nextTerm = digitsFactorial(chain[-1])
        if nextTerm not in chain:
            chain.append(nextTerm)
        else:
            return len(chain)

ans = 0
for n in range(1,1_000_000):
    if digitFactorialChainLen(n) == 60:
        ans += 1
print(ans)
print(time()-start)