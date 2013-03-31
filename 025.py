#! /usr/bin/env python

def memo(func):
    cache = {}
    def f(*arg):
        if arg not in cache:
            cache[arg] = func(*arg)
        return cache[arg]
    return f

@memo
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,10000000):
    k = fib(i)
    if len(str(k)) >=1000:
        print i
        break
