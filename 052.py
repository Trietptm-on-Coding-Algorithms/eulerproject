#! /usr/bin/env python

def samed(a,b):
    return  sorted(list(str(a))) == sorted(list(str(b)))

def isnxsame(x,n):
    return all([ samed(x,a) for a in [ (i+1)*x for i in range(1,n) ]])

#print isnxsame(125874,2)

n = 1
while True:
    if isnxsame(n,6):
        print n
        break
    n+=1
