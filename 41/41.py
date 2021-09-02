import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from itertools import permutations

from usefulfunctions import isprime

#This program solves Project Euler #41

def maxPandigitalPrime():
    """Check primeness of all pandigital numbers from highest to lowest, return first result"""
    digits = '0987654321'
    while digits:
        digits = digits [1:]
        pandigitals = permutations(digits)
        for pandigital in pandigitals:
            pandigital = int(str().join(pandigital))
            if isprime(pandigital):
                return pandigital

print(maxPandigitalPrime())
