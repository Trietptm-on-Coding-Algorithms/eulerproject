#! /usr/bin/env python

def isdbpalindromic(n):
    s = str(n)
    b = bin(n)[2:]
    #print s,b
    return (s == ''.join(reversed(s))) and (b == ''.join(reversed(b)))

#print isdbpalindromic(585)

print sum([x for x in range(1,1000001) if isdbpalindromic(x)])
