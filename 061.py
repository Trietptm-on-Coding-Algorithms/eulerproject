#! /usr/bin/env python

from eulerutils import seqmaker

def triangle(n):
    return n*(n+1)/2

def square(n):
    return n*n

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return n*(5*n-3)/2

def octagonal(n):
    return n*(3*n-2)

def searchcli(n,numlist):
    req = []
    for i in numlist:
        if n%100 == i/100:
            req.append(i)
    return req

octs = seqmaker(999,9999,octagonal)
heps = seqmaker(999,9999,heptagonal)
hexs = seqmaker(999,9999,hexagonal)
pens = seqmaker(999,9999,pentagonal)
squs = seqmaker(999,9999,square)
tris = seqmaker(999,9999,triangle)    

res = []   
for octn in octs:

    setlist = [heps,hexs,pens,squs,tris]
    setviewed = [octs]
    cyclic = [octn]
    pplist = [(octn,setviewed[:],cyclic[:])]
    
    for i in range(5):
        ppplist = pplist[:]
        pplist =[]
        for p in ppplist:
            setviewed = p[1]
            cyclic = p[2]
            for lists in setlist:
                if lists in setviewed:
                    continue
                for pt in searchcli(p[0],lists):
                    pplist.append((pt,setviewed[:]+[lists],cyclic[:]+[pt]))
                    
                 
    for p in pplist:
        if p[0]%100 == octn/100:
            res.append(p[2])

for l in res:
    print l,sum(l)
        
