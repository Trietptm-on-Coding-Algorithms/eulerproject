#! /usr/bin/env python

matrix = []
with open(r'./data/081.txt','r') as f:
    for line in f:
        matrix.append([int(n) for n in line.split(',')])

#print matrix[0][0],len(matrix[0]),len(matrix)

matrix.append([9999999]*len(matrix[0]))
for line in matrix:
    line.append(9999999)
matrix[-1][-2] = 0
matrix[-2][-1] = 0
#print matrix[0][0],len(matrix[0]),len(matrix)

for i in xrange(len(matrix)-2,-1,-1):
    for j in xrange(i,-1,-1):
        matrix[i][j] += min(matrix[i][j+1],matrix[i+1][j])
        if i!=j:
            matrix[j][i] += min(matrix[j][i+1],matrix[j+1][i])

print matrix[0][0]
