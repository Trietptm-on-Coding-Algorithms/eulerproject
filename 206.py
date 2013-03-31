#! /usr/bin/env python

def isright(n):
    s = str(n)
    for i in range(9):
        if int(s[2*i]) != i+1:
            return False
    return True

def find1():
    for i in xrange(10**8):
        if i % 1000000 == 0:
            print i
        s = format(i,'08d')
        sqrt = int(''.join([str(n+1)+s[n] for n in range(8)]) + '900') 
        n = int(sqrt**.5)
        if n**2 == sqrt:
            return n
            print 'find',n
            break

def find2():
    for i in xrange(int(1020304050607080900**.5)/100,int(2000000000000000000**.5)/100,1):
        p3 = i*100+30
        if isright(p3**2):
            print 'find',p3
            return p3
        p7 = p3+40
        if isright(p7**2):
            print 'find',p7
            return p7

print find2()
