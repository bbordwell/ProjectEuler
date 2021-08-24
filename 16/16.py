#This program Solves Euler #16

ans = 0
for digit in str(2**1000):
    ans += int(digit)
print(ans)