#! /usr/bin/env python

from eulerutils import genprime,ispermutation
from sys import exit

primes = []
# for sqrt(10**7) ~ 50%
for p in genprime():
    if p > 5000:
        break
    if p > 2000:
        primes.append(p)

print 'initial done'

primes.reverse()

res = []
for i in xrange(len(primes)):
    for j in xrange(i,len(primes)):
        p = primes[i]
        q = primes[j]
        if p*q > 10**7:
            continue
        if p!=q:
            phi = (p-1)*(q-1)
        else:
            phi = p*(p-1)
        if ispermutation(p*q,phi):
            res.append((float(p*q)/phi,p*q))

print min(res)
