import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve
    
#This Program solves Project Euler #49.

primes = sieve(10000)
primes = {x for x in primes if x >1000}

arithmeticSequences = []
for prime in primes:
    for x in range(1,3334):
        if prime + x in primes and prime + x*2 in primes:
            arithmeticSequences.append((prime,prime+x,prime+x+x))

for sequence in arithmeticSequences:
    if set(str(sequence[0])) == set(str(sequence[1])) == set(str(sequence[2])):
        print(str(sequence[0])+str(sequence[1])+str(sequence[1]))