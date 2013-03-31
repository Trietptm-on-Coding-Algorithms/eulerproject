#! /usr/bin/env python


with open(r'./data/011.txt','r') as f:
    grid = []
    for line in f:
        grid.append([int(s.strip()) for s in line.split()])

from operator import mul

def mulx(l):
    return reduce(mul,l)

maxp = 0

for line in grid:
    maxp = max([ mulx(line[i:i+4]) for i in range(len(line)-4)]+[maxp])

for line in [ [grid[i][j] for i in range(len(grid))] for j in range(len(grid[0])) ]:
    maxp = max([ mulx(line[i:i+4]) for i in range(len(line)-4)]+[maxp])

for i in range(len(grid)-4):
    for j in range(len(grid[0])-4):
        maxp = max(maxp,mulx([grid[i+k][j+k] for k in range(4)]))

for i in range(len(grid)-4):
    for j in range(4,len(grid[0])):
        maxp = max(maxp,mulx([grid[i+k][j-k] for k in range(4)]))

print maxp
