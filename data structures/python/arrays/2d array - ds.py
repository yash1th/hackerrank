#!/bin/python3
arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
max_array = []
for row in range(4):
    for col in range(4):
        tl = arr[row][col]
        tc = arr[row][col+1]
        tr = arr[row][col+2]
        mc = arr[row+1][col+1]
        bl = arr[row+2][col]
        bc = arr[row+2][col+1]
        br = arr[row+2][col+2]
        max_array.append(tl+tc+tr+mc+bl+bc+br)
print(max(max_array))
