#This program solves Project Euler #71.

def fareyNeighbor(a,b,c,d,maxd):
    """
    Given two farey neightbors a/b and b/c return the fraction just to the
     left of b/c that has a denominator of under max d.
    """
    #https://en.wikipedia.org/wiki/Farey_sequence#Farey_neighbours

    while True:
        if b+d > maxd:
            return (a,b)
        a, b = a+c, b+d

print(fareyNeighbor(2,5,3,7,1_000_000))