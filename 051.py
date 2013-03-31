#! /usr/bin/env python

from eulerutils import genprime,isprime
from itertools import permutations

pd = {}

def cl(num,mask):
    bits = len(str(num))
    bm = mask
    nu = num
    if len(mask)<bits:
        mask = '0'*(bits-len(mask)-1)+mask+'0'
    for b in range(bits):
        if mask[b]=='1':
            nb = 10**(bits-b-1)
            num -= ((num/nb)%10)*nb

    #return [int(bm)*i*10 + num for i in range(10)]

    return len([1 for i in range(10) if (int(bm)*i*10 + num)>= nu and isprime(int(bm)*i*10 + num)])
    
for p in genprime():
    if p > 1000000:
        break
    if p > 100000:
        lb = p%10
        if lb not in pd:
            pd[lb] = []
        pd[lb].append(p)

res = []
for ss in pd:
    for mask in range(1,32):
        m = bin(mask)[2:]
        for num in pd[ss]:
            if  cl(num,m) == 8:
                res.append((num,m))
                print num,m

print min(res)
