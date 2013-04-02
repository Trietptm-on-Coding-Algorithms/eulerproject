#! /usr/bin/env python

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

print 'inited'

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
