#! /usr/bin/env python

def isbounce(n):
    s = str(n)
    if len(s) < 3:
        return False
    if isincre(s):
        return False
    else:
        return not isdecre(s)

def isincre(s):
    for i in xrange(len(s)-1):
        if s[i+1] < s[i]:
            return False
    return True

def isdecre(s):
    for i in xrange(len(s)-1):
        if s[i+1] > s[i]:
            return False
    return True

def countforb(limit,start=0,count=0,por=0):
    n = start
    cnt=count
    p = por
    while p < limit:
        n+=1
        if isbounce(n):
            cnt+=1
        p = float(cnt)/n
        if n % 100000 == 0:
            print n,round(p,3)
    return n,cnt,round(p,3)

print countforb(.99)

