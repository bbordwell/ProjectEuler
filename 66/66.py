from decimal import *
getcontext().prec = 100

#This program solves Project Euler #66

def convergentsGenerator(d):
    """Generate convergents of a given non perfect square int."""
    #https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
    r = Decimal(d).sqrt()
    remainders = []
    h,k,a = [0,1],[1,0],[]
    while True:
        a.append(int(r))
        r -= a[-1]
        remainders.append(float(r))
        r = 1/r
        h.append((a[-1]*h[-1])+h[-2])
        k.append((a[-1]*k[-1])+k[-2])
        yield (h[-1],k[-1])
    

def solvePells(d):
    """Find the fundamental solution of for a Pell's equation given D."""
    #https://en.wikipedia.org/wiki/Pell%27s_equation#Example
    convergents = convergentsGenerator(d)
    while True:
        convergant = next(convergents)
        if convergant[0]**2 - d*convergant[1]**2 == 1:
            return convergant

ds = [x for x in range(2,1_001) if x**.5 % 1 != 0]

maxD = 0
maxX = 0
for d in ds:
    solution = solvePells(d)
    if solution[0] > maxX:
        maxX = solution[0]
        maxD = d
print(maxD)
    
test = convergentsGenerator(2)
while True:
    next(test)