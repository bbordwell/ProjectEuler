import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program solves Project Euler #46.

ans = set()
primes = sieve(10000)[1:] 

for prime in primes:
    n = 1
    ans.add(prime)
    while prime + 2*(n**2) < 10000:
        if  (prime + 2*(n**2)) % 2 == 1:
            ans.add(prime+ 2*(n**2))
        n += 1
odds = {x for x in range(3,10000,2)}
print(min(odds.difference(ans)))