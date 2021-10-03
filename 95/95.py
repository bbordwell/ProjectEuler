import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import factors_of_N  
    
divisorSums = {x:sum(factors_of_N(x,include_N=False)) for x in range(1,1_000_000)}

longestChain = 0
for n in range(1,200_000):
    i = 1
    chainEnd = n
    while True:
        try:
            chainEnd = divisorSums[chainEnd]
            if chainEnd == n:
                if i > longestChain:
                    longestChain = i
                    longestN = n
                break
        except KeyError:
            break
        i += 1
        if i > 30:
            break
print(longestN)