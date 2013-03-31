#! /usr/bin/env python

with open(r'./data/059.txt','r') as f:
    encrypted = [int(s) for s in f.readline().strip().split(',')]

#print encrypted

def isp(l):
    return ord('a') <= l <= ord('z')

def decrypt(en,pw):
    res = en[:]
    for i in range(len(res)):
        res[i] = res[i]^pw[i%len(pw)]
    return res

indicate = set()

def findindicate(numlist):
    comm = [ord(s) for s in ' the ']
    passphr = [numlist[i]^comm[i] for i in range(len(comm))]
    if all([ isp(n) for n in passphr ]):
        return passphr
    return []

for i in range(len(encrypted)-5):
    passphr = findindicate(encrypted[i:i+5])
    if passphr:
        pw = tuple(passphr[:3]*2)
        indicate.add(pw[i%3:i%3+3])

for pw in sorted(indicate):
    print ''.join([chr(c) for c in decrypt(encrypted,pw)])
    print sum(decrypt(encrypted,pw))
    print ''

