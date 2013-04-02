#! /usr/bin/env python

from eulerutils import gcd,PrimesUtils

pu = PrimesUtils(1100000)
print 'initial done'

isprime = pu.isPrime
primefactors = pu.primefactors

def phi1(x):
    #phi function implenment 1
    if isprime(x):
        return x-1
    count = 0
    for i in xrange(x):
        if gcd(i,x) == 1:
            count += 1
    return count

def phi2(x):
    #phi function implenment 2
    if isprime(x):
        return x-1

    factors = primefactors(x,True)

    #phi(x) = pi(p**(a-1)*(p-1))
    count = 1
    for item in factors:
        count *= (item[0]-1)*(item[0]**(item[1]-1))
    return count

def findFrac(n,func):
    res = 0
    for x in xrange(2,n+1):
        f = func(x)
        res += f
        if x%10**5 == 0:
            print x
    return res

#print findFrac(3000,phi1)
print findFrac(10**6,phi2)
