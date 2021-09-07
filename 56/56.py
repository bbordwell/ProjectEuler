#This program solves Project Euler #56.

ans = 0
for a in range(1,100):
    for b in range(1,100): 
        digits = [int(x) for x in str(a**b)]
        digitsSum = sum(digits)
        if digitsSum > ans:
            ans = digitsSum
print(ans)