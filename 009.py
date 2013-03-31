#! /usr/bin/env python

from sys import exit

def ispt(a,b,c):
    return a**2+b**2 == c**2

for a in xrange(1,1000/3):
    for b in xrange(a,(1000-a)/2):
        c = 1000-a-b
        if ispt(a,b,c):
            print a*b*c,a,b,c
            exit(0)
