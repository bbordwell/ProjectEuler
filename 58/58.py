import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import isprime

primes = 0
nums = [1,]     #First square is one
for n in range(2,1000000,2):   #Distance between corners increments by 2 per level
    for i in range(4):      #Each level has 4 corners
        nums.append(nums[-1]+n)     #Record all corners.
        if isprime(nums[-1]):
            primes += 1
    if primes / len(nums) < 0.1:
        print(n+1)
        break