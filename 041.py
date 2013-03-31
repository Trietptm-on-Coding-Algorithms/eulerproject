#! /usr/bin/env python

from itertools import permutations
from eulerutils import isprime,genprime

def ispandigital(n):
    s = str(n)
    return sorted([int(i) for i in s]) == sorted(range(1,len(s)+1))

#print ispandigital(2143),ispandigital(2123)

def find1():
    # take so long
    for n in genprime():
        if ispandigital(n):
            print n
        if n > 987654321:
            break

def find2():
    for n in range(9,0,-1):
        for numlist in permutations([str(i) for i in range(n,0,-1)]):
            if isprime(int(''.join(numlist))):
                return int(''.join(numlist))
    return 0

print find2()
