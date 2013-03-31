#! /usr/bin/env python

from fractions import Fraction
from math import e,floor

def getConvergentslist(num,iters):
    res = []
    for i in xrange(iters):
        res.append(int(floor(num)))
        p = num - floor(num)
        if p == 0:
            return res
        num = 1./p
    return res

def getConv(convlist):
    p = 0
    for x in reversed(convlist):
        p = Fraction(1,p+x)
    return 1/p

sl = getConvergentslist(e,10)

print sl

s = getConv(sl)

print sum([int(c) for c in str(s).split('/')[0]])

def another():
    d = 1
    n = 2
    for i in range(2,101):
        temp = d
        c = 2*(i/3) if i%3 == 0 else 1
        d = n
        n = c*d + temp
    return n
print sum([int(c) for c in str(another())])
