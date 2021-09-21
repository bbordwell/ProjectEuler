#This program solves Project Euler #63

ans = 0
for exp in range(1,22): #9**22 is only 21 digits long, so 21 is the highest possible exponent.
    i = 1
    while i**exp < 10**exp:
        if len(str(i**exp)) == exp:
            ans +=1
        i += 1
print(ans)