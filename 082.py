#! /usr/bin/env python

matrix = []
with open(r'./data/082.txt','r') as f:
    for line in f:
        matrix.append([int(n) for n in line.split(',')])
#matrix = [
#[131,673,234,103,18],
#[201,96 ,342,965,150],
#[630,803,746,422,111],
#[537,699,497,121,956],
#[805,732,524,37 ,331]]
#print matrix[0][0],len(matrix[0]),len(matrix)

matrix.insert(0,[9999999]*len(matrix[0]))
matrix.append([9999999]*len(matrix[0]))
for line in matrix:
    line.append(0)

#print matrix[0][0],len(matrix[0]),len(matrix)

for j in xrange(len(matrix[0])-2,-1,-1):
    temp = [matrix[i][j]+matrix[i][j+1] for i in xrange(len(matrix))]
    #for line in matrix:
    #    print line
    #print temp
    #raw_input()
    for i in xrange(1,len(matrix)-1):
        ind = temp.index(min(temp))
        matrix[ind][j] = temp[ind]
        if temp[ind-1]<9999999:
            temp[ind-1] = min(temp[ind-1],matrix[ind-1][j]+temp[ind])
        if temp[ind+1]<9999999:
            temp[ind+1] = min(temp[ind+1],matrix[ind+1][j]+temp[ind])
        temp[ind] = 9999999

print min([m[0] for m in matrix])
