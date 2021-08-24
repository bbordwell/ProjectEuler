#This program solves Project Euler #14

def collatzSequenceLen(n):
    """Input a starting number and return the length of it's collatz sequence. """
    sequence = [n,]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            sequence.append(n)
        else:
            n = 3*n + 1
            sequence.append(n)
    return len(sequence)

#Check the length of every Collatz sequence under 1 million
#Store the starting number and length if it is the longest found yet
#Display the longest one found
longest = 0
for n in range(1_000_000,1,-1):
    length = collatzSequenceLen(n)
    if length > longest:
        longest = length 
        ans = n
print(ans)