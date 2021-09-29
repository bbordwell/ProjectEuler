from itertools import combinations, product

#This program solves Project Euler #90.

dice = product(combinations('0123456789',6),repeat=2)
squares = set(['01','04','09','16','25','36','49','64','81'])

ans = 0
for die1,die2 in dice:
    foundSqaures = set()
    if '6' in die1 and '9' not in die1:
        die1 += ('9',)
    if '9' in die1 and '6' not in die1:
        die1 += ('6',)
    if '6' in die2 and '9' not in die2:
        die2 += ('9',)
    if '9' in die2 and '6' not in die2:
        die2 += ('6',)
    for digit1 in die1:
        for digit2 in die2:
            if digit1+digit2 in squares:
                foundSqaures.update([digit1+digit2,])
    for digit1 in die2:
        for digit2 in die1:
            if digit1+digit2 in squares:
                foundSqaures.update([digit1+digit2,])
    if foundSqaures == squares:
        ans += 1
print(ans//2) #Each set of dice shows up twice as die1,die2 and die2,die1.
    