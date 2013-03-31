#! /usr/bin/env python

print sum((i for i in range(1000) if i%3==0 or i%5==0))

def sigma(m):
    return m*(m+1)/2

print 3*sigma(1000/3) + 5*sigma(1000/5-1) - 15*sigma(1000/15)



