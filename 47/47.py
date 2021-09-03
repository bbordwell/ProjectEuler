#This program solves Project Euler #47.

primes = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,
179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,
383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,
607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809)

def numberOfPrimeFactors(n):
    """Given an integer, n, return how many prime factors it has """
    ans = ()
    for prime in primes:
        if prime > n:
            break
        if n % prime == 0:
            ans += (prime,)
    return len(ans)

ans = (0,1,1)
i = 600
while i < 140_000:
    i += 1
    ans += (numberOfPrimeFactors(i),)
    if ans[-4] > 3 and ans[-3] > 3 and ans[-2] > 3 and ans[-1] > 3:
        print(i-3)
        break