import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program solves Project Euler #87.

seconds = [x**2 for x in sieve(7079)]
thirds = [x**3 for x in sieve(373)]
fourths = [x**4 for x in sieve(89)]

ans = set()

for x in seconds:
    for y in thirds:
        for z in fourths:
            if x+y+z < 50000000:
                ans.add(x+y+z)

print(len(ans))