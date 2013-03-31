#! /usr/bin/env python

with open(r'./data/022.txt','r') as f:
    words = f.readline()
    words = eval('['+words+']')

    words.sort()

def count(s):
    return sum([ ord(x) - ord('A') + 1 for x in s])

#print count('COLIN')

print sum([(i+1)*count(words[i]) for i in range(len(words))])

