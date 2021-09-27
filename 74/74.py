from math import factorial

#This program solves Project Euler #74.

#Create a dictionary of factorials so they are not recomputed millions of times.
#Saves ~2 seconds of run time.
facts = dict()
for n in range(10):
    facts[n] = factorial(n)

def digitsFactorial(n):
    """Returns the sum of the factorials of the digits of the input."""
    n = str(n)
    digits = [facts[int(x)] for x in n]
    return sum(digits)

def digitFactorialChainLen(n):
    """Returns the length of the factorial chain for the input."""
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