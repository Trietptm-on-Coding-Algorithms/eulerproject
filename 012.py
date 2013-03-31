#! /usr/bin/env python

from eulerutils import divisors

n=1
s=0
while True:
    s+=n
    n+=1
    if len(divisors(s))+1 > 500:
        print s
        break

