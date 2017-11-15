#!/bin/python3

import sys


n = int(input().strip())
li = 0
ri = n-1
ls = 0
rs = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    ls += ae[li]
    rs += ae[ri]
    li += 1
    ri -= 1
print(abs(ls-rs))

#above code is slightly improved code

#the following code worked
# #!/bin/python3
#
# import sys
#
#
# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)
# li = 0
# ri = n-1
# ls = 0
# rs = 0
# for ae in a:
#     ls += ae[li]
#     rs += ae[ri]
#     li += 1
#     ri -= 1
# print(abs(ls-rs))
