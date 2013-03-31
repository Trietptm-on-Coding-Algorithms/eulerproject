#! /usr/bin/env python

from math import factorial

def c(n,r):
    return factorial(n)/factorial(r)/factorial(n-r)

ns = [(n,r) for n in range(1,101) for r in range(n+1) if c(n,r)>1000000]

print ns
print len(ns)
