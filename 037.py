#! /usr/bin/env python


def memo(func):
    c={}
    def f(*arg):
        if arg not in c:
            c[arg] = func(*arg)
        return c[arg]
    return f

@memo
def isprime(x):
    if x < 2:
        return False
    for i in range(2,int(x**.5)+1):
        if x % i == 0:
            return False
    return True

def isTruncatable(n):
    s = str(n)
    for i in range(len(s)):
        if not ( isprime(int(s[i:])) and isprime(int(s[:len(s)-i])) ):
            return False
    return True

#print isTruncatable(3797)

tru = []
n = 10
while len(tru) < 11:
    if isTruncatable(n):
        tru.append(n)
        print len(tru),n
    n+=1

print tru
print sum(tru)
        

