from math import factorial

#This program solves Project Euler #15
#See https://en.wikipedia.org/wiki/lattice_path
#The number of NE (This question is about SE, but they are equivalent)
#lattice paths from (0,0) to (A,B) counts the number of combinations of A
#objects out of a set of A+B objects
#The formula for combinations is n!/(r!(n-r)!) n=A+B r = A

print(factorial(40)/(factorial(20)*factorial(20)))