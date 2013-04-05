#! /usr/bin/env python

from itertools import permutations,combinations

def findgonring(n):
    numlist = range(1,n+1)
    res = []
    l = n/2

    for nul in combinations(numlist,l):
        sumofinner = sum(nul)
        sumofall = sum(numlist) + sumofinner
        nuo = [i for i in numlist if i not in nul]
        sumofoutter = sum(nuo)
        avge = sumofall/l
        if avge*l != sumofall:
            continue
        nul = sorted(nul)
        for nup in permutations(nul[:-1]):
            nup = list(nup)
            nup.append(nul[-1])
            nuq = []
            nuop = set(nuo)
            for i in range(l):
                p = avge-nup[i]-nup[(i+1)%l]
                if p in nuop:
                    nuop.remove(p)
                    nuq.append(p)
                else:
                    break
            if sum(nuq) != sumofoutter or len(nuq) != l:
                continue
            leader = nuq.index(min(nuq))
            s = []
            for i in range(l):
                s.append(nuq[(leader+i)%l])
                s.append(nup[(leader+i)%l])
                s.append(nup[(leader+i+1)%l])
            res.append(''.join([str(c) for c in s]))
    return res

def findmaxr(l,bits):
    return max([int(s) for s in l if len(s)<=bits])

print findmaxr(findgonring(10),16)
