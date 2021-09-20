import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from itertools import combinations

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program Solves Project Euler #51

primes = sieve(1_000_000)
primesSet = set(primes)

def digitReplacementCombos(n):
    """Given an integer, n, output all valid digit replacements."""
    replacements = tuple()
    for y in range(1,len(str(n))):
        indices = [x for x in range(len(str(n))-1)] #Last digit of a prime must be 1,3,7, or 9 so don't try to check digit changes on the last digit since there are not enough options.
        replacements += tuple(combinations(indices,y))
    replacements = [x for x in replacements if isValidReplacementCombo(n,x)]
    return replacements

def isValidReplacementCombo(n,combo):
    """Given an integer and a combination of indexes, return wether it is a valid replacement strategy."""
    n = str(n)
    digits = []
    for digit in combo:
        digits.append(n[digit])
    for digit in digits:
        if digit != digits[0]:
            return False
    return True

def numberOfPrimeDigitReplacements(n,replacement):
    """Given an integer, n, and a digit replacement combo, return the number of primes created"""
    primes = []
    n = str(n)
    for x in '0123456789':
        newN = ''
        for index, digit in enumerate(n):
            if index not in replacement:
                newN += n[index]
            else:
                newN += x
        if newN[0] != '0' and int(newN) in primesSet:
            primes.append(newN)
    return len(primes)

def checkPrimes():
    """Check all primes and return the first one with a digit replacement strategy that produces 8 primes."""
    for prime in primes:
        for combo in digitReplacementCombos(prime):
            if numberOfPrimeDigitReplacements(prime,combo) == 8:
                return prime

print(checkPrimes())







