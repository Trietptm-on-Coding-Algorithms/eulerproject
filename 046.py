#! /usr/bin/env python

from eulerutils import genprime,isprime

def goldbach():
    gp = genprime()
    p = gp.next()
    q = gp.next()

    while True:
        for com in xrange(p+2,q,2):
            if not isop(com):
                return com
        p = q
        q = gp.next()
                

def isop(com):
    for n in range(1,int(com**.5)+1):
        if isprime(com - 2*n**2):
            return True
    return False

print goldbach()
