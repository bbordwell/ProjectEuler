from decimal import Decimal
from typing import final

#This Program solves Euler #33

finalNumerator = 1
finalDenominator = 1

for denominator in range(11,100):
    for numerator in range(10,denominator):
        if str(numerator)[1] == str(denominator)[0]:
            if str(numerator)[0] != '0' and str(denominator)[1] != '0' and Decimal(int(str(numerator)[0])) / Decimal(int(str(denominator)[1])) == Decimal(numerator) / Decimal(denominator):
                #This case finds all 4 fractions, tests for other cases are not needed.
                finalNumerator *= numerator
                finalDenominator *= denominator
if finalDenominator % finalNumerator == 0:
    #The the numerator divides into the denominator evenly, you can find the simplified version of the fraction by dividing the denominator by the numerator.
    #In this case the answer fits this form so no more advanced simplification is needed
    print(finalDenominator//finalNumerator)