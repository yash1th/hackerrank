#!/bin/python3

import sys


s, t = [int(i) for i in input().strip().split(' ')]
a, b = [int(i) for i in input().strip().split(' ')]
m, n = [int(i) for i in input().strip().split(' ')]
apple = [int(i) for i in input().strip().split(' ')]
orange = [int(i) for i in input().strip().split(' ')]
Total_apples, Total_oranges = 0, 0
for d in apple:
    if a+d >= s and a+d <= t:
        Total_apples += 1
for d in orange:
    if b+d >= s and b+d <= t:
        Total_oranges += 1
print(Total_apples,Total_oranges,sep='\n')
