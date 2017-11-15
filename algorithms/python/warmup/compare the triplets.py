#!/bin/python3

import sys

def solve(a,b):
    ar = 0
    br = 0
    for i in range(len(a)):
        if a[i]>b[i]:
            ar += 1
        elif a[i]<b[i]:
            br += 1
        else:
            pass
    return ar,br

a = tuple(int(i) for i in input().split())
b = tuple(int(i) for i in input().split())
print(' '.join([str(i) for i in solve(a,b)]))

# def solve(a0, a1, a2, b0, b1, b2):
#     # Complete this function
#
# a0, a1, a2 = input().strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = input().strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]
# result = solve(a0, a1, a2, b0, b1, b2)
# print (" ".join(map(str, result)))
