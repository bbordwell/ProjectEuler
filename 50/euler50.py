import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import sieve_of_Eratosthenes as sieve

#This program solves Project Euler #50.

primes = sieve(1_000_000)
primesSet = set(primes)

def consecutivePrimeSums(terms,limit):
    """
    Input the number of consecutive terms and the max prime.
    Output a list of all prime sums that can me made with those criteria.
    """
    #This depends on primes and primesSet which are precomputed so it does not
    #have to be recomputed every function call. To generalize remove this optimization.
    consecutivePrimes = []
    i = 0
    while i < len(primes) - terms:
        if sum(primes[i:i+terms]) > limit:
            break
        if sum(primes[i:i+terms]) in primesSet:
            consecutivePrimes.append(sum(primes[i:i+terms]))
        i += 1
    return consecutivePrimes

if __name__ == '__main__':
    #The sum of the first 547 primes > 1,000,00 so check up to 546 terms.
    for terms in range(21,547):
        tempAns = consecutivePrimeSums(terms,1_000_000)
        if tempAns:
            ans = tempAns
    print(ans)