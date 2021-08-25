from math import factorial

#This program solves Project Euler #20
num = factorial(100)
num = str(num)
nums = [int(x) for x in num]
print(sum(nums))