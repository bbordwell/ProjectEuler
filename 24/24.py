from itertools import permutations

#This program sovles Project Euler #24
#Generate all permutations and print the millionth element
print(str().join(list(permutations('0123456789',10))[999_999]))