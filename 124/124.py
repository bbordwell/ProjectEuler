import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import primeFactorsOfRange

#This program solves Project Euler #124.

def rad(factors):
    """Given a list of factors, return the radical."""
    ans = 1
    for factor in factors:
        ans *= factor
    return ans
        
    
rads = primeFactorsOfRange(100_000) 
for n,factors in rads.items():
    if not factors:
        rads[n] = n
    else:
        rads[n] = rad(factors)
rads = {k: v for k, v in sorted(rads.items(), key=lambda item: item[1])}
print(list(rads.keys())[9_998])