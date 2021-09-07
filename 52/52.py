#This program solves Project Euler #52.

i = 0
while True:
    i += 1
    #If n*6 has more digits than n then it and all other numbers higher than n with that many digits are too high to be valid answers, so skip to the next number of digits.
    if len(str(i*6)) > len(str(i)):
        i = 10**(len(str(i)))
        continue
    if set(str(i)) == set(str(i*2)) and set(str(i)) == set(str(i*3)) and set(str(i)) == set(str(i*4)) and set(str(i)) == set(str(i*5)) and set(str(i)) == set(str(i*6)):
        print(i)
        break