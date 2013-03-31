#! /usr/bin/env python

digitn = []

for i in range(2,6*9**5):
    n=i
    s=0
    while n>0:
        s += (n%10)**5
        n = n//10

    if i == s:
        digitn.append(i)

print digitn
print sum(digitn)
        
