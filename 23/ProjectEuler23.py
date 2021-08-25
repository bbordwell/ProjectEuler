import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import factors_of_N as factors
from itertools import combinations_with_replacement as combinations

abundants = []
for x in range(1,28123):
    if sum(factors(x,include_N=False)) > x:
        abundants.append(x)
answer = {x for x in range(1,28124)}
sums = combinations(abundants,2)
for x in sums:
    try:
        answer.remove(sum(x))
    except KeyError:
        pass
print(sum(answer))
