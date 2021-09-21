from collections import Counter

#This program solves Project Euler #62.

#Create a tuple of all cubes from 1**3 to 10000**3 represented as a sorted string of their digits.
cubes = tuple()
for cube in range(1,10000):
    cubes += (''.join(sorted(str(cube**3))),)

#Count how many times each sorted set of digits appears, store the most common one.
digits = Counter(cubes).most_common()[0][0]

#Find the lowest cube that has the most common digits which will be the answer.
for cube in range(1,10000):
    if ''.join(sorted(str(cube**3))) == digits:
        print(cube**3)
        break