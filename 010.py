#! /usr/bin/env python

from eulerutils import genprime

def sum1(n):
    # a bit slow
    s=0
    for p in genprime():
        if p > n:
            break
        s+=p
    return s

def sum2(n):
    # python sieve 15x faster than sum1
    sieve = [0]*n
    p = 3
    s = 2
    while p<n:
        if sieve[p] == 0:
            s += p
            i = p
            while i < n:
                sieve[i] = 1
                i += p
        p += 2
    return s

print sum2(2*10**6)
