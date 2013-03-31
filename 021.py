#! /usr/bin/env python

def memo(func):
    cache={}
    def f(*arg):
        if arg not in cache:
            cache[arg] = func(*arg)
        return cache[arg]
    return f

@memo
def divisors(n):
    return [x for x in range(1,n//2+1) if n%x == 0]

def d(n):
    return sum(divisors(n))

#print d(284),d(220) #220,284
    
res = []
for i in range(1,10000):
    if i in res: continue

    j = d(i)
    if i!=j and d(j) == i:
        res.append(i)
        res.append(j)

print sum(res)

