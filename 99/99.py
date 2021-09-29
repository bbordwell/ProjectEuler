#This program Solves Project Euler #99.

file = open('base_exp.txt')
nums = []
for line in file:
    nums.append([int(line.split(',')[0]),int(line.split(',')[1])])

largest = 0
for i,num in enumerate(nums):
    result = num[0]**(num[1]/10000) #dividing preserves relative size, but reduces calculation time.
    if result > largest:
        largest = result
        ans = i+1 #Count from 1 instead of 0.
print(ans)