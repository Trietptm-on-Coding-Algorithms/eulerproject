#! /usr/bin/env python

from eulerutils import memo

def cz(n):
    if n%2 == 0:
        return n/2
    return 3*n+1

@memo
def czchain(n):
    if n == 1:
        return 1
    return 1+czchain(cz(n))

maxc = 0
start = 0

for i in xrange(1,10**6):
    mc = czchain(i)
    if mc > maxc:
        maxc = mc
        start = i

print start,maxc
