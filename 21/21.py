import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import factors_of_N as factors

#This program solves Project Euler #21. Variable names follow the question
def d(n):
    """Input an integer and return the sum of its factors"""
    return sum(factors(n,include_N=False))

amicables = set()

for a in range(1,10_000):
    b = d(a)
    if d(b) == a and a != b:
        amicables.add(a)
        amicables.add(b)
print(sum(amicables))
