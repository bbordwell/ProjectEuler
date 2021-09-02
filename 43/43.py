#This program solves Project Euler #43.

#Generate all possible last three digit endings.
nums = [str(x) for x in range(17,1000,17)]
nums = [x for x in nums if len(x) == len(set(x))]

#Add a leading 0 the two digit numbers.
for index,num in enumerate(nums):
    if len(num) == 2:
        nums[index] = '0'+num
    else:
        break

def addDigit(nums,divisor):
    """Given a list of valid number endings, adds all valid new first digits for the given divisor."""
    digits = set('0123456789')
    newNums = []
    for num in nums:
        for digit in digits.difference(set(num)):
            if int((digit+num)[:3]) % divisor == 0:
                newNums.append(digit+num)
    return newNums

#Using all posible endings, find all possible endings with one more first digit for each divisor indicated in the problem.
for i in (13,11,7,5,3,2):
    nums = addDigit(nums,i)

#For each ending the first digit will be be the remaining digit that has not yet been used, find that digit and add it to the beginning.    
ans = []
for i, num in enumerate(nums):
    nums[i] = set('0123456789').difference(set(num)).pop() + num
 
#Find and display the sum of all the valid answers.   
nums = [int(x) for x in nums]
print(sum(nums))