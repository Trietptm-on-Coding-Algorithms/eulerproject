#! /usr/bin/env python

from math import factorial as f
from eulerutils import memo

f = memo(f)

@memo
def digitalfact(n):
    res = 0
    while n!=0:
        res += f(n%10)
        n/=10
    return res

def chains(n):
    res = {n}
    nxt = digitalfact(n)
    while nxt not in res:
        res.add(nxt)
        nxt = digitalfact(nxt)
    return len(res)

def findchains(m,ch):
    res = 0
    for i in range(1,m+1):
        if i%10000 == 0:
            print i
        if chains(i) == ch:
            res += 1
    return res

print findchains(1000000,60)

