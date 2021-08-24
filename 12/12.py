import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import triangleNumbersGenerator
from usefulfunctions import factors_of_N as factors

#This program solves Project Euler #12.
#Iterate through the triangle numbers and check how many factors each one has.
#If it has more than 500 print the result and stop.
triangleNumbers = triangleNumbersGenerator()
for triangleNumber in triangleNumbers:
    if len(factors(triangleNumber)) > 500:
        print(triangleNumber)
        break


