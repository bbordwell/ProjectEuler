from itertools import combinations, repeat

#This program solves Project Euler #44.


pentagonsSet = {n*(3*n - 1)//2 for n in range(1,100_000)} #A set for quick lookup
pentagons = [n*(3*n - 1)//2 for n in range(1,3000)] #first 2999 pentagonal numbers

pentagonPairs = [x for x in combinations(pentagons,2) if sum(x) in pentagonsSet]    #Pairs of pentagonal numbers where their sums are also pentagonal
pentagonPairs = [x for x in pentagonPairs if x[1]-x[0] in pentagonsSet] #Of those pairs find any that the difference is also pentagonal
pentagonPairsD = [x[1]-x[0] for x in pentagonPairs]     #Calculate the difference of valid pairs
print(min(pentagonPairsD))  #display the lowest difference

