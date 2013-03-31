#! /usr/bin/env python

from eulerutils import genprime,isprime

def findmostCP(LIMITS):
    primes = []
    sop = 0
    gp = genprime()

    while sop < LIMITS:
        p = gp.next()
        primes.append(p)
        sop += p

    for n in range(1,len(primes)):
        for i in range(n+1):
            s = sum(primes[i:len(primes)-n+i])
            if s < LIMITS and isprime(s):
                return s

print findmostCP(1000000)
