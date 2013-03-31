#! /usr/bin/env python

from eulerutils import ispalindrome

print max(((x*y,x,y) for x in xrange(100,1000) for y in xrange(100,1000) if ispalindrome(x*y)))

