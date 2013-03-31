#! /usr/bin/env python

def memo(func):
    c={}
    def f(*arg):
        if arg not in c:
            c[arg] = func(*arg)
        return c[arg]
    return f

@memo
def fact(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)


def iscurnum(n):
    i = n
    s = 0
    while n>0:
        s+= fact(n%10)
        n = n//10
    return True if s == i else False

print sum([x for x in range(3,fact(9)) if iscurnum(x)])
