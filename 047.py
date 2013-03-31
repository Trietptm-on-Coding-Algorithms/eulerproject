#! /usr/bin/env python

Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in xrange(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print i-3 # First number
            break
    else:
        count = 0
#from eulerutils import genprime,isprime,memo
#
##@memo
##def isdistinct(n,i):
##    res = set()
##    gp = genprime()
##    p = gp.next()
##    l = int(n**.5)+1
##    while p < l:
##        if n%p == 0:
##            n/=p
##            res.add(p)
##        if len(res)>i:
##            return False
##        p = gp.next()
##    return len(res)==i
#
#@memo
#def distinct(n):
#    if isprime(n):
#        return [n]
#    if n==1:
#        return []
#    gp = genprime()
#    p = gp.next()
#    l = int(n**.5)+1
#    while p < l:
#        if n%p == 0:
#            while n%p ==0:
#                n/=p
#            return [p] + distinct(n)
#        p = gp.next()
#    return [n]
#
##print distinct(644),distinct(2),distinct(14),distinct(15)
#
#@memo
#def isdistinct(n,i):
#    return len(distinct(n)) == i
#
#def findCIP(n):
#    i = 1
#    found = 0
#    while True:
#        for c in range(i,i+n):
#            if not isdistinct(c,n):
#                found = c-i+1
#                break
#        if found == 0:
#            return i
#        i+=found
#        found = 0
#        if i%1000 == 0: print i
#
#print findCIP(3)
