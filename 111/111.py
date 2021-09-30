import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from itertools import combinations
from itertools import product

from  usefulfunctions import isprime

def euler(digits,d):
    """Given the number of digits and d, return (M,N,S)."""
    referenceNumber = list(str(d)*digits)
    numbers = []

    for n in range(10): #Try replacing only 1 digit.
        for change in range(digits):
            number = referenceNumber[:]
            number[change] = str(n)
            if number[0] != '0':
                numbers.append(''.join(number))
    numbers = [int(number) for number in numbers if isprime(int(number))]
    if numbers:
        return (digits-1,len(numbers),sum(numbers))
    
    #One digit replacement found no primes, so try 2 digit replacement. 
    for ns in product(range(10),repeat=2):
        changes = combinations(range(digits),2)
        for change in changes:
            number = referenceNumber[:]
            number[change[0]] = str(ns[0])
            number[change[1]] = str(ns[1])
            if number[0] != '0':
                numbers.append(''.join(number))     
    numbers = [int(number) for number in numbers if isprime(int(number))]
    return (digits-2,len(numbers),sum(numbers))

        
ans = 0
for x in range(10):
    result = euler(10,x)
    print(result)
    ans += result[-1]
print(ans)
