#! /usr/bin/env python

def sigma1to(n):
    return n*(n+1)/2

def sigma1dto(n):
    return n*(n+1)*(2*n+1)/6

print sigma1to(100)**2-sigma1dto(100)
