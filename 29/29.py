#This program solves Project Euler #29

ans = set()
for a in range(2,101):
    for b in range(2,101):
        ans.add(a**b)
print(len(ans))