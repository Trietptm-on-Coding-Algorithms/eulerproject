#! /usr/bin/env python

def genpentagon():
    n=0
    while True:
       n+=1
       yield n*(3*n-1)/2

gp = genpentagon()

pens = [ gp.next() for i in range(1000000) ]
ss = set(pens)

print 'G'

def g(n):
    return n*(3*n-1)/2

def findD():
    for i in xrange(1,len(pens)-1):
        for j in xrange(1,i):
            if g(i) - g(j) in ss and g(i)+g(j) in ss:
                return g(i) - g(j)

print findD()
