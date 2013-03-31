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

def rotation(n):
    s = str(n)
    c = len(s)
    p = s+s
    return [int(p[k:k+c]) for k in range(c)]
    
primes = [i for i in xrange(3,1000000,2)
              if all([c in ['1','3','5','7','9'] for c in str(i)]) and isprime(i)]
primes.append(2)

print 'prmed'

processed = set()
res = set()
for n in primes:
    if n in processed:
        continue
    allp = rotation(n)
    processed.update(allp)
    if all([ i in primes for i in allp]):
        res.update(allp)    

print res
print len(res)
