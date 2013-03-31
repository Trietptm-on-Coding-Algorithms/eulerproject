#! /usr/bin/env python

def isluar(year):
    return year%400 == 0 or (year%100!=0 and year%4==0)

def md(year):
    m = {}
    for i in [9,4,6,11]: m[i] = 30
    for i in [1,3,5,7,8,10,12]: m[i] = 31
    m[2] = 29 if isluar(year) else 28

    return m

def days(now,old):
    if now < old :
        return 0
    day = 0
    for year in range(old[0]+1,now[0]):
        day += 366 if isluar(year) else 365
    if now[0] == old[0]:
        cal = md(now[0])
        for month in range(old[1],now[1]):
            day += cal[month]
        day += now[2]-old[2]
    else:
        cal = md(old[0])
        for month in range(old[1],13):
            day += cal[month]
        day -= old[2]
        cal = md(now[0])
        for month in range(1,now[1]):
            day += cal[month]
        day += now[2]

    return day

sun = 0
for y in range(1901,2001):
    for m in range(1,13):
       if (days((y,m,1),(1900,1,1)) + 1) % 7 == 0:
          sun += 1
print sun

