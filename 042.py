#! /usr/bin/env python

with open(r'./data/042.txt','r') as f:
    words = eval('['+f.readline()+']')

tri = {n*(n+1)/2 for n in range(1,101)}

tw = [sum([ ord(c)-ord("A")+1 for c in w ]) for w in words] 

print len([ x for x in tw if x in tri])
