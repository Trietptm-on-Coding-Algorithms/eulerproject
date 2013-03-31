#! /usr/bin/env python

from operator import mul

with open(r'./data/008.txt','r') as f:
    s = ''
    for line in f:
        s+=line.strip()

def pofxc(s,x):
    return reduce(mul,[int(c) for c in s[:x]])

maxp = 0
for i in xrange(len(s)-5):
    p = pofxc(s[i:i+5],5)
    maxp = max(p,maxp)

print maxp
