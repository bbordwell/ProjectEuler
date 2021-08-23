import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import factors_of_N, isprime

factors = factors_of_N(600851475143,include_N=False)
factors.reverse()       #generate all factors of 60085147514 from highest to lowest
for factor in factors:
    if isprime(factor):     #The first one that is prime is the answer
        print(factor)
        break




