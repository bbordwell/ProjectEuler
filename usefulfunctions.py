#A collection of useful function for Project Euler

def sieve_of_Eratosthenes(n):
    """Returns a list of all prime numbers below the input 'n'."""
    from math import sqrt
    prime = [True for x in range(n+1)]
    p = 2
    while(p*p <= n):
        if prime[p] == True:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2,n) if prime[p]]
    return primes


def writtennumber(number,withand=False,withspaces=False,withhyphen=False):
    """This function takes an integer as an input, and outputs the word written out as a string. Use withand, withspaces, and withhyphen to include those characters where appropriate."""
    if withand == True and withspaces == True:
        withand = 'and '
        withspaces = ' '
    else:
        if withand == False:
            withand = ''
        else:
            withand = 'and'
        if withspaces == False:
            withspaces = ''
        else:
            withspaces = ' '
    if withhyphen == True:
        withhyphen = '-'
    else:
        withhyphen = ''

    FIRST_TEN = ["","one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
    SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
    OTHER_TENS = ["zero","ten","twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
    HUNDRED = "hundred"
    THOUSAND = "thousand"
    if number < 10:
        return FIRST_TEN[number]
    elif number < 20:
        seconddigit = str(number)[1]
        return SECOND_TEN[int(seconddigit)]
    elif number < 100:
        firstdigit = int(str(number)[0])
        seconddigit = int(str(number)[1])
        if seconddigit == 0:
            return OTHER_TENS[firstdigit]
        else:
            return OTHER_TENS[firstdigit] + withhyphen + FIRST_TEN[seconddigit]
    elif number < 1000:
        firstdigit = int(str(number)[0])
        seconddigit = int(str(number)[1])
        thirddigit = int(str(number)[2])
        lasttwodigits = int(str(seconddigit)+str(thirddigit))
        if seconddigit == 0 and thirddigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + HUNDRED
        elif lasttwodigits < 10:
            return FIRST_TEN[firstdigit] + withspaces + HUNDRED + withspaces + withand + FIRST_TEN[thirddigit]
        elif lasttwodigits < 20:
            return FIRST_TEN[firstdigit] + withspaces + HUNDRED + withspaces + withand + SECOND_TEN[thirddigit]
        elif thirddigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + HUNDRED + withspaces + withand + OTHER_TENS[seconddigit]
        else:
            return FIRST_TEN[firstdigit] + withspaces + HUNDRED + withspaces + withand + OTHER_TENS[seconddigit] + withhyphen + FIRST_TEN[thirddigit]
    elif number < 10000:
        firstdigit = int(str(number)[0])
        seconddigit = int(str(number)[1])
        thirddigit = int(str(number)[2])
        fourthdigit = int(str(number)[3])
        lasttwodigits = int(str(thirddigit)+str(fourthdigit))
        if seconddigit == 0 and thirddigit == 0 and fourthdigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND
        elif thirddigit == 0 and fourthdigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + FIRST_TEN[seconddigit] + withspaces + HUNDRED
        elif fourthdigit == 0 and seconddigit != 0:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + FIRST_TEN[seconddigit] + withspaces + HUNDRED + withspaces + withand + OTHER_TENS[thirddigit] 
        elif lasttwodigits < 10:
            if seconddigit == 0 and thirddigit == 0:
                return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + withand + FIRST_TEN[fourthdigit]
            else:
                return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + FIRST_TEN[seconddigit] + withspaces + HUNDRED + withspaces + withand + FIRST_TEN[fourthdigit]
        elif lasttwodigits < 20:
            if seconddigit == 0:
                return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + withand + SECOND_TEN[fourthdigit]
            else:
                return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + FIRST_TEN[seconddigit] + withspaces + HUNDRED + withspaces + withand + SECOND_TEN[fourthdigit]
        elif seconddigit == 0 and fourthdigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + withand + OTHER_TENS[thirddigit]
        elif seconddigit == 0:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + withand + OTHER_TENS[thirddigit] + withhyphen + FIRST_TEN[fourthdigit]
        else:
            return FIRST_TEN[firstdigit] + withspaces + THOUSAND + withspaces + FIRST_TEN[seconddigit] + withspaces + HUNDRED + withspaces + withand + OTHER_TENS[thirddigit] + withhyphen + FIRST_TEN[fourthdigit]


def factors_of_N(n,include_One=True,include_N=True):
    """ Takes an integer and returns a list of factors."""
    if n == 1:
        if include_One == True:
            if include_N == False:
                return [1]
            else:
                return [1,n]
        else:
            return []
    factors = set()
    for x in range(1,int(n**.5)+1):
        if n%x == 0:
            factors.add(x)
            factors.add(n//x)
    if not include_N:
        factors.remove(n)
    if include_One == False:
        factors.remove(1)
    return sorted(factors)


def isprime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i += 6
  
    return True


def arecoprime(x,y):
    """ Takes two integers as input and returns True if they are coprime, otherwise False."""
    xfactors = set(factors_of_N(x,include_One=False,include_N=True))
    yfactors = set(factors_of_N(y,include_One=False,include_N=True))
    if xfactors.isdisjoint(yfactors):
        return True
    return False

def phi(n):
    """Takes an int (n) and returns the number of positive ints thare are coprime to n."""
    if isprime(n):
        return n-1
    primefactors = [x for x in factors_of_N(n,include_N=True) if isprime(x)]
    for x in primefactors:
        n *= 1-(1/x)
    return int(n)


def farey(n):
    """Input an int (n) and output all fractions from 0 to 1, with a max denominator of n"""
    x1,y1,x2,y2,x,y,ans = 0,1,1,n,0,0,[]
    ans.append('0/1')
    ans.append(f'1/{n}')
    while y != 1.0:
        x = int((y1 + n) / y2) * x2 - x1
        y = int((y1 + n) / y2) * y2 - y1
        ans.append(f'{x}/{y}')
        x1,x2,y1,y2 = x2,x,y2,y
    return ans


def ordinal_number(num):
    """This function accepts an integer and returns that number as an ordinal number string"""
    oddballs = {'one':'first','two':'second', 'three':'third','five':'fifth','eight':'eighth','nine':'ninth','twelve':'twelfth'}
    
    wr = writtennumber(num)
    for oddball in oddballs:
        if oddball == wr[-len(oddball):]:
            wr = wr[:-len(oddball)] + oddballs[oddball]
            return wr
    if wr[-1] != 'y':
        wr += 'th'
    else:
        wr = wr[:-1] + 'ieth'
    return wr


def romanToInteger(s):
    '''Accepts a roman numeral as a string and returns and integer. '''
    ans = 0
    if 'IV' in s:
        ans += 4
        s = s.replace('IV','')

    if 'IX' in s:
        ans += 9
        s = s.replace('IX','')

    if 'XL' in s:
        ans += 40
        s = s.replace('XL','')
    
    if 'XC' in s:
        ans += 90
        s = s.replace('XC','')

    if 'CD' in s:
        ans += 400
        s = s.replace('CD','')

    if 'CM' in s:
        ans += 900
        s = s.replace('CM','')

    for digit in s:
        if digit == 'I':
            ans += 1
        elif digit == 'V':
            ans += 5
        elif digit == 'X':
            ans += 10
        elif digit =='L':
            ans += 50
        elif digit == 'C':
            ans += 100
        elif digit == 'D':
            ans += 500
        elif digit == 'M':
            ans += 1000

    return ans


def fibonacci(n=False,maxValue=False):
    """If given n return the first n values from the Fibonacci sequence.
       If given maxValue return the sequence with all numbers below that value"""
    fib = [1,2]
    if n:
        if n == 1: return [1]
        while len(fib) < n:
            fib.append(sum(fib[-2:]))
        return fib

    if maxValue:
        if maxValue == 1: return [1]
        if maxValue == 2: return fib
        while sum(fib[-2:]) <= maxValue:
            fib.append(sum(fib[-2:]))
        return fib


def pythagoreanTriples(maxSide):
    """Input an Integer and output all pythagorean triples with all sides smaller than that number"""
    #Euclid's formula, implemented by me.
    triples = set()
    for m in range(2,maxSide+1):
        for n in range(1,m):
            if not arecoprime(m,n):
                continue
            else:
                k = 1
                while k * (m**2 + n**2) <= maxSide:
                    a = k * (m**2 - n**2)
                    b = k * (2*m*n)
                    c = k * (m**2 + n**2)
                    triples.add(tuple(sorted([a,b,c])))
                    k += 1
    return sorted(tuple(triples))


def triangleNumbersGenerator(limit=float('inf')):
    """This generator produces triangle numbers"""
    tNumber = 0
    i = 1
    while i <= limit:
        tNumber += i
        i += 1
        yield tNumber
