#!/bin/python3

import sys

arr = [int(i) for i in input().split()]
#arr = list(map(int, input().strip().split(' ')))
arr.sort()
l = len(arr)
print(sum(arr[:l-1]),sum(arr[1:]),sep=' ')


#another way to do this is

#!/bin/python3

import sys

arr = [int(i) for i in input().split()]
s = sum(arr)
total = [s-i for i in arr]
print(min(total),max(total),sep=' ')
