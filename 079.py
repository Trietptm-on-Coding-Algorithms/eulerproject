#! /usr/bin/env python

numstrings = set()

with open('./data/079.txt','r') as f:
    for line in f:
        numstrings.add(line.strip())

numlist = [ list(s) for s in sorted(numstrings) ]

allnum = { n for l in  numlist for n in l }

res = []
while allnum:
    firsts = { l[0] for l in numlist if l }
    others = { l[i] for l in numlist for i in range(len(l)) if i }
    
    num = firsts-others

    for i in sorted(num):
        for l in numlist:
            if i in l:
                l.remove(i)
        allnum.remove(i)
        res.append(i)

print ''.join(res)
