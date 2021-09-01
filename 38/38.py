#This program solves Project Euler #38

maxAns = 0
for x in range(1,10000):  #5 digit number *2 is too long, so check all numbers with 4 or less digits.
    if not len(set(str(x))) == len(str(x)):
        continue
    digits = set(str(x))
    for n in range(2,6):    #multiply by two, three, ... until it is pandigital or fails
        if not len(set(str(x*n))) == len(str(x*n)):
            break
        if not digits.isdisjoint(set(str(x*n))):
            break
        digits = digits.union(set(str(x*n)))
        if len(digits) == 9:
            ans = str(x)
            for i in range(n-1):
                ans += str(x*(i+2))
            if int(ans) > maxAns and '0' not in ans:    #Make sure the number does not include 0
                maxAns = int(ans) 
print(maxAns)