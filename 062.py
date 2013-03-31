#! /usr/bin/env python


def findCube(perms):
    d = {}

    n = 1
    l = 10

    while True:
        cube = n**3
        if cube < l:
            s = tuple(sorted(str(cube)))
            if s not in d:
                d[s] = []
            d[s].append(cube)
            n+=1
        else:
            l*=10
            per = [min(d[s]) for s in sorted(d.keys()) if len(d[s]) == perms]
            if per:
                return min(per)
            d.clear()

print findCube(5)

