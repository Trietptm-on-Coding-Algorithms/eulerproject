#! /usr/bin/env python

def memo(func):
    c = {}
    def f(*arg):
        if arg not in c:
            c[arg] = func(*arg)
        return c[arg]
    return f

@memo
def count(cost,coins):
    if cost == 0:
        return 1
    if len(coins) == 0:
        return 0
    res = 0
    for n in range(cost//coins[0]+1):
        c = cost - n*coins[0]
        res += count(c,coins[1:])

    return res

coins = (200,100,50,20,10,5,2,1)

print count(200,coins)
