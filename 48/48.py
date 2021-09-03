#This program solves Project Euler #48.

ans = 0
for x in range(1,1001):
    ans += x**x
print(str(ans)[-10:])