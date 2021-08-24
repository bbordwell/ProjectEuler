import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program Solves Project Euler #10.
#Use the Sieve of Eratosthenes to generate all primes under two million, sum them
print(sum(sieve(2_000_000)))
