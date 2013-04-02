#! /usr/bin/env python

from eulerutils import genprime

def totient_sieve(L):
    ''' return list of totient(i) for i from 0 to n-1.
 
    >>> totient_sieve(12)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10]
    '''     
    t = range(L+1)
    for i in xrange(2,L+1):
        if i == t[i]:
            for j in xrange(i,L+1,i): t[j]-=t[j]/i
    return t

def findR(a,b,start=2):
    tots = totient_sieve(b**2)
    d = start
    while True:
        if tots[d]* b < a*(d-1):
            return d
        if d%1000000==0:
            print d
        d+=1
       
#print findR(15499,94744,5000000)
#failed 10**8 out of mem

def findR2(a,b):
    # phi = pi(n*(1-1/p))
    gp = genprime()
    r,l = b,a
    d = 1
    while True:
        p = gp.next()
        rn = r*(p-1)
        ln = l*p
        dn = d*p
        # find the most 2*3*5*...value
        if rn*dn<ln*(dn-1):
            #test small values
            for i in xrange(2,p):
                if r*d*i < l*(d*i-1):
                    return d*i
        r = rn
        l = ln
        d = dn

    return 0

print findR2(4,10)
print findR2(15499,94744)

