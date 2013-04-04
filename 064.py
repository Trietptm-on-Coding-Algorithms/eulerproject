#! /usr/bin/env python

from math import sqrt

def nextC(n,d,m):
    # (sqrt(n)+d)/m
    a = int((sqrt(n)+d)/m)
    d = a*m -d
    m = (n-d*d)/m
    return (a,n,d,m)

def confraction(num):
    a = int(sqrt(num))
    if a**2 == num:
        return [a]

    n = nextC(num,0,1)
    res = [n]
    while True:
        n = nextC(*n[1:])
        if n in res:
            break
        res.append(n)
    
    return [i[0] for i in res]

cnt = 0
for i in range(1,10**4+1):
    if len(confraction(i))%2==0:
        cnt+=1
print cnt

