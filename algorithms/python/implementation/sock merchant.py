#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    pairs = {i:ar.count(i) for i in set(ar)}
    total = 0
    for k,v in pairs.items():
        total+=(v//2)
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
