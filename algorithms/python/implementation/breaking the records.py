#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    mini = maxi = s[0]
    maxiChange, miniChange = 0, 0
    for i in range(1,len(s)):
        if mini>s[i]:
            mini = s[i]
            miniChange += 1
        elif maxi < s[i]:
            maxi = s[i]
            maxiChange += 1
        else:
            pass
    return maxiChange, miniChange
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
