#! /usr/bin/env python

i = 1

for e in xrange(7830457):
    i*=2
    i%=10**10

i = (28433*i + 1) % (10**10)

print i
