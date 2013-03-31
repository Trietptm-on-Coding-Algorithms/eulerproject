#! /usr/bin/env python
# -*- coding: utf-8 -*-

from operator import mul

print sum([int(s) for s in str(reduce(mul,xrange(1,101)))])


print sum([int(s) for s in str(2**1000)])

