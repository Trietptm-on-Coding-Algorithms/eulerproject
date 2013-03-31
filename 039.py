#! /usr/bin/env python

def isrtri(a,b,c):
    return a**2+b**2 == c**2

def findallrtri(p):
    if p < 12:
        return []
    allt = []
    for a in range(1,p//3+1):
        for b in range(a, (p-a)//2+1):
            if isrtri(a,b,p-a-b):
                allt.append((a,b,p-a-b))
                break

    return allt

#print findallrtri(120)

print max([ (len(findallrtri(p)),p) for p in range(1,1001) ])

