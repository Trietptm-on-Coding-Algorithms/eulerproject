#! /usr/bin/env python

dic = {}
with open(r'./data/017.txt','r') as f:
    flip = 0
    for line in f:
        if flip == 0:
            n = int(line.strip())
            flip = 1
        else:
            dic[n] = line.strip()
            flip = 0

for x in range(21,100):
    if x not in dic:
        dic[x] = dic[x//10*10] + dic[x%10]

for x in range (1,10):
    if 100*x not in dic:
        dic[100*x] = dic[x] + 'hundred'

dic[1000] = 'onethousand'

for x in range(101,1000):
    if x not in dic:
        dic[x] = dic[x//100*100] + 'and' + dic[x%100]

def search(num):
    return(dic[num],len(dic[num]))

print sum([ search(x)[1] for x in range(1,1001) ])

