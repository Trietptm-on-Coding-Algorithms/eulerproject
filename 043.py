#! /usr/bin/env python

from itertools import permutations

subdiv = [1,2,3,5,7,11,13,17]

res = []

for numlist in permutations('1234567890'):
    flag = 1
    for i in range(len(subdiv)):
        subnum = int(''.join((numlist[i:i+3])))
        if subnum % subdiv[i] != 0:
            flag = 0
            break
    if flag == 1:
        res.append(int(''.join(numlist)))

print sum(res)
