#! /usr/bin/env python

p = {}
for i in range(2,10):
    p[str(i)] = i
p['T'] = 10
p['J'] = 11
p['Q'] = 12
p['K'] = 13
p['A'] = 14

def pval(hands):
    cards = sorted([ (p[s[0]],s[1]) for s in hands],reverse = True)
    cd = {}
    for card in cards:
        if card[0] not in cd:
            cd[card[0]] = 0
        cd[card[0]] += 1
    cardvs = sorted([(i,v) for v,i in cd.items()],reverse = True)
    
    cardv = tuple([c[1] for c in cardvs])

    def isSame(cards):
        return 1 == len(set([s[1] for s in cards]))

    def isConse(cardv):
        return cardv == tuple(range(cardv[0],cardv[0]-5,-1))

    if cardvs[0][0] == 4:
        return (7,)+cardv
    elif cardvs[0][0] == 3:
        if cardvs[1][0] == 2:
            return (6,)+cardv
        else:
            return (3,)+cardv
    elif cardvs[0][0] == 2:
        if cardvs[1][0] == 2:
            return (2,)+cardv
        else:
            return (1,)+cardv
    else:
        if isConse(cardv):
            if isSame(cards):
                return (9,)+cardv
            else:
                return (4,)+cardv
        elif isSame(cards):
            return (5,)+cardv
        else:
            return(0,)+cardv

def cmp(a,b):
    #print a, ' vs ',b
    #print pval(a),' vs ',pval(b), 'p1: ' ,pval(a) > pval(b)
    return pval(a) > pval(b)

with open(r'./data/054.txt','r') as f:
    p1w = 0
    for line in f:
        hands = line.split()
        if cmp(hands[:5],hands[5:]):
            p1w += 1

print p1w
