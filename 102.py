#! /usr/bin/env python

def area(x1,y1,x2,y2,x3,y3):
    return abs(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/2.

def ispassthrough(x1,y1,x2,y2):
    return (y1-y2)*x1-(x1-x2)*y1 == 0

def ispassorigin(x1,y1,x2,y2,x3,y3):
    if ispassthrough(x1,y1,x2,y2) or ispassthrough(x1,y1,x3,y3) or ispassthrough(x3,y3,x2,y2):
        return True
    return area(x1,y1,x2,y2,0,0)+\
           area(x1,y1,0,0,x3,y3)+\
           area(0,0,x2,y2,x3,y3) ==\
           area(x1,y1,x2,y2,x3,y3)

with open(r'./data/102.txt','r') as f:
    count = 0
    for line in f:
        arg = [int(s) for s in line.strip().split(',')]
        if ispassorigin(*arg):
            count+=1
    print count

