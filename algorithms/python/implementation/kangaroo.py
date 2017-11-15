#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    while True:
        if (x1>x2 and v1>v2) or (x2>x1 and v2>v1) or (v1 == v2):
            return 'NO'
            break
        x1 += v1
        x2 += v2
        if x1 == x2:
            return 'YES'
            break


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
