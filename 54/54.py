file = open('hands.txt')
hands = []
p1score, p2score,tie = 0,0,0
for line in file:
    hands.append(line.split())


def cardsort(n):
    if n == 'T':return '91'
    elif n == 'J':return '92'
    elif n == 'Q':return '93'
    elif n == 'K': return '94'
    elif n == 'A': return '95'
    else: return n


def pairbreaker(one,two):
    for x in '23456789TJQKA':
        if one.count(x) == 2:
            onepair = x
        if two.count(x) == 2:
            twopair = x
    one.remove(onepair)
    one.remove(onepair)
    two.remove(twopair)
    two.remove(twopair)
    if onepair == 'T':
        onepair = '91'
    if onepair == 'J':
        onepair = '92'
    if onepair == 'Q':
        onepair == '93'
    if onepair == 'Q':
        onepair = '94'
    if onepair == 'K':
        onepair = '95'
    if onepair == 'A':
        onepair = '96'
    if twopair == 'T':
        twopair = '91'
    if twopair == 'J':
        twopair = '92'
    if twopair == 'Q':
        twopair == '93'
    if twopair == 'Q':
        twopair = '94'
    if twopair == 'K':
        twopair = '95'
    if twopair == 'A':
        twopair = '96'
    if onepair > twopair:
        return 1
    if twopair > onepair:
        return 2
    else:
        if one[0] > two[0]:
            return 1
        elif two[0] > one[0]:
            return 2


def flushbreaker(one,two):
    for x in 'AKQJT98765432':
        if x in one and x not in two:
            return 1
        if x in two and x not in one:
            return 2


def handscore(ns,suits):
    ns = ''.join(ns)
    flush,straight,royal = False,False,False
    if ns == 'TJQKA':
            royal = True
    if ns in 'A23456789TJQKA':
            straight = True
    if suits == ['H','H','H','H','H'] or p1suits == ['C','C','C','C','C'] or p1suits == ['S','S','S','S','S'] or p1suits == ['D','D','D','D','D']:
        flush = True
    if royal == True and flush == True:
        return 23
    if straight == True and flush == True:
        return 22
    for x in '23456789TJQKA':
        if ns.count(x) == 4:
            return 21
    count = 0
    for x in '23456789TJQKA':
        if x in ns:
            count += 1
    if count == 2:
        return 20
    if flush == True:
        return 19
    if straight == True:
        return 18
    for x in '23456789TJQKA':
        if ns.count(x) == 3:
            return 17
    count = 0
    for x in '23456789TJQKA':
        if ns.count(x) == 2:
            count += 1
    if count == 2:
        return 16
    if count == 1:
        return 15
    if 'A' in ns: return 14
    if 'K' in ns: return 13
    if 'Q' in ns: return 12
    if 'J' in ns: return 11
    if 'T' in ns: return 10
    if '9' in ns: return 9
    if '8' in ns: return 8
    if '7' in ns: return 7
    if '6' in ns: return 6
    if '5' in ns: return 5
    if '4' in ns: return 4
    if '3' in ns: return 3
    if '2' in ns: return 2
    

for hand in hands:
    p1 = hand[0:5]
    p2 = hand[5:10]
    p1ns = [x[0] for x in p1]
    p1suits = [x[1] for x in p1]
    p2ns = [x[0] for x in p2]
    p2suits = [x[1] for x in p2]
    p1ns.sort(key=cardsort)
    p2ns.sort(key=cardsort)
    p1handscore = handscore(p1ns,p1suits)
    p2handscore = handscore(p2ns,p2suits)
    if p1handscore > p2handscore:
        p1score += 1
    elif p2handscore > p1handscore:
        p2score += 1
    elif p1handscore == 15:
        if pairbreaker(list(p1ns),list(p2ns)) == 1:
            p1score += 1
        elif pairbreaker(list(p1ns),list(p2ns)) == 2:
            p2score += 1
    elif p1handscore == 19:
        if flushbreaker(p1ns,p2ns) == 1:
            p1score += 1
        if flushbreaker(p1ns,p2ns) == 2:
            p2score += 1
    else:
        print([p1handscore,p2handscore])
        tie += 1

print([p1score,p2score,tie])