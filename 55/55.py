#This program solvers Project Euler #55

ans = 0
for number in range(1,10_001):
    for iteration in range(50):
        number = number + int(str(number)[::-1])
        if str(number) == str(number)[::-1]:
            break
    else:
        ans += 1
print(ans)