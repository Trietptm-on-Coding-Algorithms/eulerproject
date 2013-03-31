#! /usr/bin/env python

from itertools import permutations

res = set()

def ismul(numlist,mi,ei):
    md = int(''.join(numlist[:mi]))
    m = int(''.join(numlist[mi:mi+ei]))
    p = int(''.join(numlist[mi+ei:]))
    return True if md*m==p else False

for numlist in permutations('123456789'):
    if ismul(numlist,1,4):
        res.add(int(''.join(numlist[5:])))
    if ismul(numlist,2,3):
        res.add(int(''.join(numlist[5:])))

#print ismul(list(str(391867254)),2,3)
print sum(list(res))
