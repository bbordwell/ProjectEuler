#This program sovles Project Euler #97.

n = 2
for i in range(7830456):
    n = (n*2) % 10000000000 #Only track the last 10 digits to improve execution speed.
n *= 28433
n += 1
print(n%10000000000)