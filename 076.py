#! /usr/bin/env python

from eulerutils import memo
from math import factorial as f

@memo
def part(num,p):
    if p == 1:
        return [[num]]
    if p == num:
        return [[1]*p]
    res = []
    for i in range(1,num-p+1):
        for numlist in part(num-i,p-1):
            res.append([i] + numlist)
    res = [tuple(sorted(r)) for r in res]
    res = set(res)
    res = [list(r) for r in res]
    return res
        

def cal(n):
    s = 0
    for i in range(2,n+1):
        p = len(part(n,i))
        s+= p
    return s

@memo
def part2(num,p,maxnum):
    #print 'process',(num,p,maxnum)
    if num <= 0:
        return 0
    if maxnum <= 0:
        return 0
    if p == 0:
        return 0
    if maxnum*p < num:
        return 0
    if maxnum*p == num:
        #print 'hit'
        return 1
    res = 0
    res += part2(num,p,maxnum-1)
    for i in xrange(num/maxnum,0,-1):
        res += part2(num - i*maxnum, p-i, maxnum -1)
    return res

def cal2(n):
    s = 0
    for p in range(2,n+1):
        g = part2(n,p,n)
        #print 'Parted for',n,p,g
        s += g
    return s

print cal2(100)
#print cal(10)

print '-------------'
#print part2(5,3,5)
#print part2(3,3,2)
#print part2(1,1,1)
