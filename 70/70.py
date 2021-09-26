import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from collections import Counter
from time import time

from usefulfunctions import phis

#This program solves Project Euler #70.

start = time()
 
minRatio = 100000000000   
for k,v in phis(10**7).items():
    if Counter(str(k)) == Counter(str(v)):
        if k/v < minRatio:
            minRatio = k/v
            ans = k
print(ans)
print(time()-start)