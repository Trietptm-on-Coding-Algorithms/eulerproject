#! /usr/bin/env python

from fractions import Fraction

def iterF():
    n= 1+Fraction('1/2')
    yield n
    while True:
        n = 1 + 1/(1+n)
        yield n

def isexceed(f):
    n,d = str(f).split('/')
    return len(str(n)) > len(str(d))

k = iterF()
count = 0
for i in xrange(1000):
    if isexceed(k.next()):
        count+=1
    
print count
