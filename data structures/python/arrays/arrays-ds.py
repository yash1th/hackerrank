#!/bin/python3
_ = int(input().strip())
arr = [int(i) for i in input().split()]
for i in reversed(arr):
    print(i,end=' ')
