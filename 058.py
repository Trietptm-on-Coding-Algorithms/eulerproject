#! /usr/bin/env python

from eulerutils import isprime

def d(n):
    if n == 1:
        return (0,1)
    w = [ n*n - (n-1)*k for k in range(1,4)]
    return (len([p for p in w if isprime(p)]),4)

p = 0.0
a = 1.0
n = 3

while True:
    p1,a1 = d(n)
    p+=p1
    a+=a1

    if p/a < .1:
        print n
        break
    n+=2

