#This program solves Project Euler #73.

#Use a modified farey sequence generator to find the conditions at 1/3
def fareyConditionsAtFraction(n,d,maxD):
    """Output the conditions of the farey algorithm at a given fraction"""
    x1,y1,x2,y2,x,y = 0,1,1,maxD,0,0
    while y != 1.0:
        x = int((y1 + maxD) / y2) * x2 - x1
        y = int((y1 + maxD) / y2) * y2 - y1
        x1,x2,y1,y2 = x2,x,y2,y
        if y == d and x == n:
            return(x1,x2,y1,y2)

#Starting from the conditions at 1/3 continue the algorithm while counting the number of fractions generated. Stop at 1/2.    
def fareyFromConditionToCondition(x1,x2,y1,y2,maxD,endN,endD,startN,startD):
    """Count the number of fractions from a given start point to a given end point."""
    ans = 0
    x = startN
    y = startD
    while y != 1.0:
        x = int((y1 + maxD) / y2) * x2 - x1
        y = int((y1 + maxD) / y2) * y2 - y1
        x1,x2,y1,y2 = x2,x,y2,y
        ans += 1
        if y == 2 and x == 1:
            return ans-1

initials = fareyConditionsAtFraction(1,3,12_000)
print(fareyFromConditionToCondition(initials[0],initials[1],initials[2],initials[3],12000,1,2,1,3))