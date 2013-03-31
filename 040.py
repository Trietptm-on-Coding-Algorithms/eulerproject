#! /usr/bin/env python

s = ''

for i in xrange(0,1000000):
    s += str(i)
    if len(s) > 1000001:
        break

from operator import mul

print reduce(mul,[int(s[10**n]) for n in range(0,7)])

