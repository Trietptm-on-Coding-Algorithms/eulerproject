#! /usr/bin/env python

from eulerutils import ispalindrome,memo

@memo
def islychrelnumber(n):
    p = n
    for i in range(50):
        rp = int(''.join(reversed(str(p))))
        p = p+rp
        if ispalindrome(p):
            return False
    return True

print len([i for i in range(1,10000) if islychrelnumber(i)])
