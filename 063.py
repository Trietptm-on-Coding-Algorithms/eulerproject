#! /usr/bin/env python

res = [1]

for e in range(1,1000):
    if len(str(9**e)) > e:
        break
    for n in range(2,1000):
        num = n**e
        bits = len(str(num))
        if bits == e:
            res.append(n)
        if bits > e:
            break

print len(res)
        
