#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
negCount = 0
zeroCount = 0
posCount = 0
for i in arr:
    if i == 0:
        zeroCount += 1
    elif i<0:
        negCount += 1
    else:
        posCount += 1
print(posCount,negCount,zeroCount,sep='\n')
