#! /usr/bin/env python

from eulerutils import genprime,isprime,memo
from itertools import combinations
from sys import exit

@memo
def isnotcp(a,b):
    a,b = str(a),str(b)
    return not (isprime(int(a+b)) and isprime(int(b+a)))


gp = genprime()

primes = [ gp.next() for i in xrange(5000) ]

print 'initial done'

for i in xrange(4,len(primes)):
    for j in xrange(3,i):
        if isnotcp(primes[i],primes[j]):
            continue
        for k in xrange(2,j):
            if isnotcp(primes[i],primes[k]):
                continue
            if isnotcp(primes[j],primes[k]):
                continue
            for m in xrange(1,k):
                if isnotcp(primes[i],primes[m]):
                    continue
                if isnotcp(primes[j],primes[m]):
                    continue
                if isnotcp(primes[k],primes[m]):
                    continue
                for n in xrange(m):
                    if isnotcp(primes[i],primes[n]):
                        continue
                    if isnotcp(primes[j],primes[n]):
                        continue
                    if isnotcp(primes[k],primes[n]):
                        continue
                    if isnotcp(primes[m],primes[n]):
                        continue
                    #found
                    print sum([primes[i],primes[j],primes[k],primes[m],primes[n]]),[primes[i],primes[j],primes[k],primes[m],primes[n]]
                    exit(0)

# a bit timewasty and ugly ...
# maybe sieve can be a nice solution

