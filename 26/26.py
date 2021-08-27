#This program Solves Project Euler #26
#It works based on the idea that when generating more and more digits after the
#decimal point, if you see the same numerator/denominator twice then you are in
#an infinite loop. If you measure the distance between the first and second
#occurrence you know how long the pattern is.

longest = 0     
for d in range(2,1000):
    divs = []
    n = 10
    while n < d:
        n *= 10
    for x in range(1000):
        if (n,d) not in divs:
            divs.append((n,d))
            n = (n % d) * 10
        else:
            if len(divs)-divs.index((n,d)) > longest:
                longest = len(divs)-divs.index((n,d))
                ans = d
            break
print(ans)