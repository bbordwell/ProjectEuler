#This program solves Euler #28

nums = [1,]     #First square is one
for n in range(2,1001,2):   #Distance between corners increments by 2 per level
    for i in range(4):      #Each level has 4 corners
        nums.append(nums[-1]+n)     #Record all corners.
print(sum(nums))        #Display the sum of all corners.