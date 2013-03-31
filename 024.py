#! /usr/bin/env python

from itertools import permutations

print ''.join([str(n) for n in list(permutations(range(10)))[1000000-1]])
