#! /usr/bin/env python

from eulerutils import gcd,isprime,primefactors

def findonly(x):
    if isprime(x):
        return x-1
    count = 0
    for i in xrange(x):
        if gcd(i,x) == 1:
            count += 1
    return count

def findFrac(n):
    res = 0
    for x in xrange(2,n+1):
        f = findonly(x)
        res += f
        if x%10**4 == 0:
            print x
    return res

#print findFrac(10**6)
