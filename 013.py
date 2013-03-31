#! /usr/bin/env python

with open(r'./data/013.txt','r') as f:
    s = 0
    for line in f:
        s+= int(line.strip())
    print s
    print str(s)[:10]
