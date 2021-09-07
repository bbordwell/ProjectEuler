from math import factorial

#This program solve Project Euler #53

ans = 0
for n in range(101):
    for r in range(n):
        if factorial(n) / (factorial(r)*factorial(n-r)) > 1_000_000:
            ans += 1
print(ans)