from math import factorial

ans = 0
for n in range(3,2540161): #Sum of the factorial of 9999999 is 2540160
    digits = [int(digit) for digit in str(n)]
    digits = [factorial(digit) for digit in digits]
    if sum(digits) == n:
        ans += n
print(ans)