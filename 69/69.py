import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import phi

#This program solves Project Euler #69.

maxPhi = 0
for n in range(2,1_000_001):
    p = phi(n)
    if n/p > maxPhi:
        maxPhi = n/p
        maxN = n
print(maxN)