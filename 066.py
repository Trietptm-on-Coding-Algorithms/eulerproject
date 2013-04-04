#! /usr/bin/env python

def findmaxD1(p):
    # impossible to find solution ...
    n = 1
    sqlist = [0,1]
    D = {i for i in xrange(2,p+1) if int(i**.5)**2 != i}

    while True:
        n+=1
        sq = n*n
        sqlist.append(sq)
        for i in xrange(n-1):
            if sq % sqlist[n-i-1] == 1:
                d = sq // sqlist[n-i-1]
            if sqlist[n-i-1] == 1:
                d = sq-1
            if d in D:
                D.remove(d)
                if len(D) == 0:
                    return d
    return 0

from math import sqrt
from eulerutils import gcd

def nextC(n,d,m):
    # (sqrt(n)+d)/m
    a = int((sqrt(n)+d)/m)
    d = a*m -d
    m = (n-d*d)/m
    return (a,n,d,m)

def nextCN(n):
    p0 = nextC(n,0,1)
    a0 = p0[0]
    n0,d0 = a0,1
    yield n0,d0
    p1 = nextC(*p0[1:])
    a1 = p1[0]
    n1,d1 = a1*a0+1,a1
    g = gcd(n1,d1)
    n1,d1 = n1/g,d1/g
    yield n1,d1
    while True:
        p2 = nextC(*p1[1:])
        p1,p0 = p2,p1
        n2 = p2[0]*n1+n0
        d2 = p2[0]*d1+d0
        g = gcd(n2,d2)
        n2,d2 = n2/g,d2/g
        d1,d0 = d2,d1
        n1,n0 = n2,n1
        yield n2,d2

def findmaxD2(p):
    D = [i for i in xrange(2,p+1) if int(i**.5)**2 != i]
    res = []
    for d in D:
        for x,y in nextCN(d):
            if x*x - d*y*y == 1:
                res.append((x,y,d))
                break
    return max(res)[2]

print findmaxD2(1000)

