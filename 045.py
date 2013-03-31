#! /usr/bin/env python

def tri():
    n = 0
    while True:
        n += 1
        yield n*(n+1)/2

def pen():
    n = 0
    while True:
        n += 1
        yield n*(3*n-1)/2

def hexa():
    n = 0
    while True:
        n += 1
        yield n*(2*n-1)

t,p,h = tri(),pen(),hexa()
a,b,c = t.next(),p.next(),h.next()
print a,b,c

s = 1
while s <= 3:
    if a==b==c:
        print s,a
        s += 1
    if a == min(a,b,c):
        a = t.next()
    elif b == min(a,b,c):
        b = p.next()
    else:
        c = h.next()
