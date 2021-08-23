#This program solves Project Euler #1
print(sum([n for n in range(3,1000) if n%3 == 0 or n%5 == 0]))
#Check all numbers from 3 to 999, if they are divisible by 3 or 5 add them to the list
#Then sum all numbers in the list and dispaly the result