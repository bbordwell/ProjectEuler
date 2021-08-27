import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import isprime

#This program Solves Project Euler #27
#Try all possible combinations of a and b, record which one finds the most primes

maxPrimes = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n = 0
        while isprime(n**2 + (a*n) + b):
            n += 1
        if n > maxPrimes:
            maxPrimes = n
            aAndb = (a,b)
print(aAndb[0]*aAndb[1])