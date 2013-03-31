#! /usr/bin/env python

def addn(n):
    # if use str: run for double time -_-b
    #return sum([ int(s)**2 for s in str(n)])

    sum = 0
    while n > 0:
        sum += (n%10)**2
        n = n/10
    return sum

def find1():
    # run for 57s
    s89 = set([89])
    s1 = set([1])

    for n in xrange(1,10000000):
        i = n
        chains = [i]
        while True:
            if i in s89:
                s89.update(chains)
                break
            if i in s1:
                s1.update(chains)
                break
            i = addn(i)
            chains.append(i)
    
    return len(s89)

def find2():
    # run for 49s
    count = 0
    arr = [0]*10000002
    arr[1]=2
    arr[89]=1
    for n in xrange(1,10000000):
        i = n
        c = [i]
        while True:
            if arr[i] == 1:
                for p in c:
                    arr[p] = 1
                count +=1
                break
            if arr[i] == 2:
                for p in c:
                    arr[p] = 2
                break
            i = addn(i)
            c.append(i)
    
    return count

print find2()
