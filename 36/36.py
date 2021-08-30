#This program solves Project Euler #36.

ans = 0
for n in range(1,1_000_000):
    if "{0:b}".format(n) == "{0:b}".format(n)[::-1] and str(n) == str(n)[::-1]:
        ans += n
print(ans)