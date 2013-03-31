#! /usr/bin/env python

def memo(func):
    cache = {}
    def f(*arg):
        if arg not in cache:
            cache[arg] = func(*arg)
        return cache[arg]
    return f

@memo
def route(x,y):
    if x == 0 or y == 0:
        return 1
    else:
        return route(x-1,y) + route(x,y-1)


print route(20,20)
