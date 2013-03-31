#! /usr/bin/env python

from eulerutils import genprime
from itertools import combinations

def isacc(l):
    if len(l) < 3:
        return False
    d = l[1] - l[0]
    s = l[0]
    for n in l[1:]:
        s += d
        if n!=s:
            return False
    return True

def isperm(l):
    if len(l) < 1:
        return False
    k = [sorted(str(i)) for i in l]
    d = k[0]
    for p in k:
        if p != k:
            return False
    return True
    

primedic = {}
for n in genprime():
    if n > 10000:
        break
    if n > 1000:
        s = int(''.join(sorted(str(n))))
        if s not in primedic:
            primedic[s] = []
        primedic[s].append(n)

for numsl in primedic.values():
    for nums in combinations(numsl,3):
        if isacc(nums):
            print nums

