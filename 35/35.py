import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import isprime
from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program solves Euler #35

primes = sieve(1_000_000)   #Generate all primes < 1 million
ans = 0
for prime in primes:
    if prime < 10:  #Single digit primes are always circular
        ans += 1
        continue
    #The following block creates a string version of the prime and multiplies it by 2
    #It then slices out an equal length number shifted one digit to the right
    #repeat until all rotations have been checked, if they were all prime record it.
    for rotation in range(1,len(str(prime))):   
        rotatedPrime = int((str(prime)*2)[rotation:rotation+len(str(prime))])
        if not isprime(rotatedPrime):
            break
    else:
        ans += 1
print(ans)
