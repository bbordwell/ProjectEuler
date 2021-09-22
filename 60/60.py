import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from itertools import permutations
from itertools import combinations

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program sovles Project Euler #60

PrimesSet = set(sieve(100000000))
primes = sieve(10000)
del primes[0]   #remove 2 because it can never be concatenated and to the end and produce a prime

def validSet(nums):
    """"Input a list of numbers and output wether it is a prime pair set"""
    combos = permutations(nums,2)
    for combo in combos:
        if not (int(str(combo[0])+str(combo[1])) in PrimesSet and int(str(combo[1])+str(combo[0])) in PrimesSet):
            return False
    return True

def addToSets(sets):
    """Input prime pair sets and output a new list where each set has one more member"""
    newSets = []
    for prime in primes:
        for set in sets:
            if prime in set:
                break
            set = list(set)
            set.append(prime)
            set.sort()
            if validSet(set):
                newSets.append(set)
    return newSets


sets = combinations(primes,2)
sets = [x for x in sets if int(str(x[0])+str(x[1])) in PrimesSet and int(str(x[1])+str(x[0])) in PrimesSet]
sets = addToSets(sets)
sets = addToSets(sets)
sets = addToSets(sets)
print(sets)
print(sum(sets[0]))



