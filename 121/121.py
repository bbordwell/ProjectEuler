from itertools import product
from fractions import Fraction

#This program solves Project Euler #121.

pickslist = list(product([0,1],repeat=15))  #All combinations of wins and losses
pickslist = [x for x in pickslist if sum(x) > 7]    #Remove losses

totalChances = []
for picks in pickslist:
    chances = []
    for i,pick in enumerate(picks):
        if pick:    #If blue was picked, calculate odds.
            chance = Fraction(1)/Fraction(i+2)
            chances.append(chance)
        else:   #If red is picked, calculate odds.
            chance = Fraction(i+1)/Fraction(i+2)
            chances.append(chance)
    chance = Fraction(1)
    for x in chances:   #Calculate total odds for the current game.
        chance *= x
    totalChances.append(chance) #Track odds for each possible game.
print(int(1/float(sum(totalChances))))   #Sum the odds for each way too win for a total chance of winning.