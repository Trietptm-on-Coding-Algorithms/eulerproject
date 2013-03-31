#! /usr/bin/env python

def divisors(n):
    return [i for i in range(1,n//2+1) if n%i==0]

def isabundant(n):
    return sum(divisors(n)) > n

allabundants = [ n for n in range(1,28124) if isabundant(n) ]

res = set(range(1,28124)) - {a+b for a in allabundants for b in allabundants}

print sum(res)
