#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    t = list(range(1,6))
    c = [ar.count(i) for i in t]
    return t[c.index(max(c))]


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
