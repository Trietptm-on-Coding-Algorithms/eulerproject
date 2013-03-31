#! /usr/bin/env python

from eulerutils import memo

@memo
def fib(n):
    if n<2:
        return 1
    return fib(n-2) + fib(n-1)

n = 1
f=fib(n)
s=0
while f<=4*10**6:
    if f%2==0:
        s+=f
    n+=1
    f=fib(n)

print s

