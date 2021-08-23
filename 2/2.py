import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import fibonacci

print(sum([fib for fib in fibonacci(maxValue=4_000_000) if fib%2 == 0])) #create all fibonaccis below 4 million and filter out the odds. Print the sum.