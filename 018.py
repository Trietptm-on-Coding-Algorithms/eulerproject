#! /usr/bin/env python

tri = []

with open(r'./data/018.txt','r') as f:
    for line in f:
        tri.append([int(n) for n in line.split()])

tri.reverse()

for line in tri:
    print line

for i in xrange(len(tri)):
    if len(tri[i]) > 1:
        for j in xrange(len(tri[i+1])):
            tri[i+1][j] += max(tri[i][j],tri[i][j+1])

print tri[-1][0]

