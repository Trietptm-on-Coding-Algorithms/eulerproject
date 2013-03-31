#! /usr/bin/env python

def repeated(s):
    for i in xrange(len(s)):
        index = s.find(s[i:i+500],i+1)
        if index != -1:
            return index - i
    return 0

from decimal import *

getcontext().prec = 3000

md = 0
mn = 1

for d in range(2,1000):
    s = str(Decimal(1)/Decimal(d))
    #print d,s
    r = repeated(s)
    if r > md:
        md = r
        mn = d

print mn,md
