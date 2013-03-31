#! /usr/bin/env python

from eulerutils import genprime

gp = genprime()

for i in xrange(10001):
    p = gp.next()

print p
