#This program solves Project Euler #30

ans = []
for n in range(2,354295):
    digits = [int(x) for x in str(n)]
    digits = [x**5 for x in digits]
    if sum(digits) == n:
        ans.append(n)
print(sum(ans))