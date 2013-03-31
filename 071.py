#! /usr/bin/env python

from eulerutils import gcd
from fractions import Fraction

def findorderfractions(d,a,b):
    x = d*a/b

    return Fraction(x,d) if Fraction(x,d) != Fraction(a,b) else Fraction(x-1,d)

print max([findorderfractions(d,3,7) for d in range(2,1000000)])

