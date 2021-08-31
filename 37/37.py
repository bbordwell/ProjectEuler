import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve
from usefulfunctions import isprime

#This program solves Project Euler #37

primes = sieve(1_000_000)[4:]     #Generate primes up to 1 million, exclude 2,3,5,7
ans = 0

for prime in primes:
    lToR = str(prime)
    rToL = str(prime)
    for digit in range(len(lToR)-1):
        lToR = lToR[1:] #Remove the leftmost digit and check if the new number is prime.
        if not isprime(int(lToR)):
            break
        rToL =rToL[:-1] #Remove the rightmost digit and check if the new number is prime.
        if not isprime(int(rToL)):
            break
    else:   #If all checks pass the number is a truncatable prime so sum it.
        ans += prime
print(ans)