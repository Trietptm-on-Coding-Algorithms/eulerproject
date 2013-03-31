#! /usr/bin/env python

def countrec(x,y,m,n):
    return (m-x+1)*(n-y+1)

def countallrec(m,n):
    return sum((countrec(x+1,y+1,m,n) for x in xrange(m) for y in xrange(n)))

def findarea(num):
    m = 0
    minnum = 999999999
    rm = 0
    rn = 0
    sp = 99999999
    while True:
        m+=1
        if m%1000==0:
            print m
        for n in range(1,m+1):
            mp = m-1 if n==1 else m
            spold = sp
            sp = countallrec(m,n)
            if sp > num:
                if abs(sp-num) < abs(spold-num):
                    minnump = abs(sp-num)
                    rmp = m
                    rnp = n
                else:
                    minnump = abs(spold-num)
                    rmp = mp
                    rnp = np
                if minnump < minnum:
                    minnum = minnump
                    rm = rmp
                    rn = rnp
                if n==1:
                    return rm*rn,rm,rn,minnum
                break
            np = n

print findarea(2000000)
