#! /usr/bin/env python

from eulerutils import genprime

m = 1
for p in genprime():
    m*=p
    if m>1000000:
        m/=p
        print m
        break
