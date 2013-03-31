#! /usr/bin/env python

from eulerutils import ispandigital

res = []
for n in range(2,6):
    exp = 9//n
    for md in xrange(10**(exp-1),10**(exp+1)):
        s = ''.join([str(md*i) for i in range(1,n+1)])
        if len(s) == 9 and ispandigital(int(s)):
            res.append(int(s))


print res
print max(res)
