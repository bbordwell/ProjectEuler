#This program solves Project Euler #104.

def fibs():
    """Generator for fibonacci numbers"""
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

panset = {str(x) for x in range(1,10)}

for n,fib in enumerate(fibs()):
    if set(str(fib%1000000000)) == panset:
        fibsetbegin = set(str(fib)[:9])
        if fibsetbegin == panset:
            print(n)
            break