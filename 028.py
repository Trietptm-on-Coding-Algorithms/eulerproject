#! /usr/bin/env python

k = 1001
print sum([4*(x**2)-6*(x-1) for x in range(3,k+1,2)]) + 1
