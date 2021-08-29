import sys      #Do this so I can import usefulfuntions from parent directory. There must be a better way to do this?
sys.path.append("/home/bbordwell/Documents/SRC/ProjectEuler")   #Edit this to fit your device

from usefulfunctions import factors_of_N, isprime

#This program solves Project Euler #32

def isPandigitalProduct(n):
    """Input an integer (n) and output True if is is a pandigital product, else False"""
    digits = str(n)
    if len(set(digits)) != len(digits) or '0' in digits:
        return False    #return False if n contains duplicate digits
    factors = factors_of_N(n,include_N=False,include_One=False)
    while len(factors) > 1:
        a = factors.pop()
        b = factors.pop(0)
        digits = str(a) + str(b) + str(n)
        if '0' in digits:
            continue
        if len(digits) == 9 and len(set(digits)) == len(digits):
            return True
    return False


if __name__ == "__main__":
    pandigitals = []
    for n in range(1,10000):
        if isPandigitalProduct(n):
            pandigitals.append(n)
    print(sum(pandigitals))

