#! /usr/bin/env python

def sumdigital(n):
    return sum([int(d) for d in str(n)])

print max([sumdigital(a**b) for a in range(1,100) for b in range(1,100)])
