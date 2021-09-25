from itertools import permutations
from copy import deepcopy

class Ring:
    
    def __init__(self,line):
        self.rings = [line,]
        self.ns = line
        
    def __add__(self,other):
        self = deepcopy(self)
        if len(self.rings) == 4:
            if self.rings[0][1] != other.rings[0][2]:
                raise ValueError
            other.ns = list(other.ns)
            other.ns.remove(other.rings[0][2])
            other.ns = tuple(other.ns)
        if self.rings[0][0] > other.rings[0][0]:
            raise ValueError
        if not self.rings[-1][2] == other.rings[0][1]:
            raise ValueError
        other.ns = list(other.ns)
        other.ns.remove(other.rings[0][1])
        other.ns = tuple(other.ns)
        if not set(self.ns).isdisjoint(other.ns):
            raise ValueError
        self.rings.append(other.rings[0])
        self.ns += other.ns
        return self
        
def allLines(total):
    lines = permutations((1,2,3,4,5,6,7,8,9,10),3)
    lines = tuple(line for line in lines if sum(line) == total)
    lines = tuple(line for line in lines if not line[1] == 10 or line[2] == 10)
    return lines
    
def appendRings(rings,total):
    newRings = []
    for ring in rings:
        for attempt in allLines(total):
            try: 
                newRings.append(ring+Ring(attempt))
            except ValueError:
                pass
    return newRings
 
 

for total in range(6,28):
    rings = [Ring(x) for x in allLines(total)]
    for i in range(4):
        rings = appendRings(rings,total)
    for ring in rings:
        print(ring.rings)

        

