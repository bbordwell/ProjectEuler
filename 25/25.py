import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from  usefulfunctions import fibonacci

#This program solves Project Euler #25.

#+1 to the answer for off by one error due to the fibbonacci function 
#not including the first 1
#+1 more because I generate all values with less than 1000 digits, so the first
#number to contain 1000 digits is the next one
print(len(fibonacci(maxValue=10**999))+2) 