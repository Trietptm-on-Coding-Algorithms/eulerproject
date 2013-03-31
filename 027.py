#! /usr/bin/env python

def memo(func):
    c={}
    def f(*arg):
        if arg not in c:
            c[arg] = func(*arg)
        return c[arg]
    return f
    
@memo
def isprime(x):
    for i in range(2,int(x**.5)+1):
        if x % i == 0:
            return False
    return True

def qp(n,a,b):
    return n**2 + a*n + b

mn,ma,mb = 0,0,0

for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        while (qp(n,a,b)>1 and isprime(qp(n,a,b))):
            n+=1
        if n > mn:
            mn = n
            ma,mb = a,b


print ma*mb
