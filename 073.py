#! /usr/bin/env python

from eulerutils import gcd,isprime
from fractions import Fraction

def findorderfractions(x,a,b,c,d):
    lb = x*a/b+1
    ub = x*c/d

    res = [Fraction(i,x) for i in xrange(lb,ub)]

    if Fraction(ub,x)!=Fraction(c,d) and Fraction(ub,x)!=Fraction(a,b):
        res.append(Fraction(ub,x))
    return res

def findFrac(n,a,b,c,d):
    res = set()
    for x in range(2,n+1):
        for f in findorderfractions(x,a,b,c,d):
            res.add(f)
    return sorted(res)

#print len(findFrac(8,1,3,1,2))

def findorderfractions2(x,a,b,c,d):
    lb = x*a/b+1
    ub = x*c/d

    if isprime(x):
        return ub-lb+1

    res = [1 for i in xrange(lb,ub+1) if gcd(i,x) == 1]

    return len(res)

def findFrac2(n,a,b,c,d):
    res = 0
    for x in range(4,n+1):
        f = findorderfractions2(x,a,b,c,d)
        res += f
        #print x,f
    return res

print findFrac2(12000,1,3,1,2)
