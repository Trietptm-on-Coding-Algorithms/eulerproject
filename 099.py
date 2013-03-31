#! /usr/bin/env python

from math import log

with open(r'./data/099.txt','r') as f:
    nums = []
    l = 0
    for line in f:
        # count log(base)*exp
        l+=1
        s = line.split(',')
        nums.append((log(int(s[0]))*int(s[1]),l))

print max(nums)
