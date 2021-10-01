#This program solves Project Euler #92.

def sqaureOfDigits(n):
    """Input an integer (n) and output the sum of the square of its digits."""
    return sum([int(x)**2 for x in str(n)])


#Create a table of results for 1-567 because the maximum possilbe value for the 
# first iteration of squareOfDigits With input under 10,000,000 is 9**2 * 7 == 567.
ans = 1
table = dict()
for n in range(1,568):
    chainEnd = n
    while True:
        if chainEnd == 89:
            table[n] = True
            ans += 1
            break
        elif chainEnd == 1:
            table[n] = False
            break
        chainEnd = sqaureOfDigits(chainEnd)

#for the rest of the numbers find first iteration of squareOfDigits and look up the result.
for n in range(568,10_000_000):
    n = sqaureOfDigits(n)
    if table[n]:
        ans += 1
print(ans)
