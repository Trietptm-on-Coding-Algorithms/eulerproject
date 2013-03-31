#! /usr/bin/env python

from fractions import Fraction

for a in range(1,9):
    for b in range(a+1,10):
        if a==b:
            continue
        n = range(1,10)
        n.remove(a)
        n.remove(b)
        for i in n:
            l = [ Fraction(a*10+i)/Fraction(b*10+i),
                  Fraction(i*10+a)/Fraction(b*10+i),
                  Fraction(a*10+i)/Fraction(i*10+b),
                  Fraction(i*10+a)/Fraction(i*10+b) 
                ]
            for f in l:
                if f == Fraction(a)/Fraction(b):
                    print f


