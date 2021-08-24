for num in range(20,999999999,20):  #check numbers from 20 until an answer. Since the number must be divisible by 20 count by 20.
    for divisor in range(19,1,-1):  #don't check 20 since we know it is divisible by 20 since we are counting by 20s. Don't check 1 because all nums are divisible by 1
        if num%divisor != 0:        #Stop cheking as soon as one of the numbers does not divide
            break
    else:                           #If all nums 2-19 were divisors then this is our answer
        print(num)
        break
