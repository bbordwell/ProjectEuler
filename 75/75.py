import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import pythagoreanTriples

#This program solves Project Euler #75.

triples = pythagoreanTriples(750_000)

wireLengths = dict()
for triple in triples:
    try:
        wireLengths[sum(triple)] += 1
    except KeyError:
        wireLengths[sum(triple)] = 1

ans = 0
for perimiter,count in wireLengths.items():
    if perimiter <= 1_500_000 and count == 1:
        ans += 1
print(ans)