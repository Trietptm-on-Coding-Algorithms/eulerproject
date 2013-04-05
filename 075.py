#! /usr/bin/env python

# use Pythagorean triple Euclid's formula

def findPythagoreanTriple(L):
    l = [0]*(L+1)
    A = set()
    # a = m*m - n*n
    # b = 2*m*n
    # c = m*m + n*n
    
    for m in xrange(2,int(L**.5)+1):
        for n in xrange(1,m):
            b = m*n
            if b%2!=0:
                a = m*m - n*n
                if a%2!=0:
                    break
                a = a/2
                c = (m*m + n*n)/2
            else:
                b *=2
                a = m*m - n*n
                c = m*m + n*n
            s,sa,sb,sc = a+b+c,a,b,c
            if a<=b<=c:
                while s<L+1:
                    if (sa,sb,sc) not in A:
                        #print s,sa,sb,sc
                        A.add((sa,sb,sc))
                        l[s]+=1
                    sa+=a
                    sb+=b
                    sc+=c
                    s+=a+b+c

    return len([1 for i in l if i==1])

print findPythagoreanTriple(1500000)


