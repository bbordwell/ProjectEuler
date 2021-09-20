#This program solves Project Euler #57

fractions = [(3,2),(7,5)]

while len(fractions) < 1000:
    #The denominator of the next fraction is the sum of the current numerator and denominator.
    d = sum(fractions[-1])
    #The numerator of the next fraction is the current numerator *2 plus the previous numerator.
    n = (fractions[-1][0] * 2) + fractions[-2][0]
    fractions.append((n,d))

ans = 0
for fraction in fractions:
    if len(str(fraction[0])) > len(str(fraction[1])):
        ans += 1
print(ans)