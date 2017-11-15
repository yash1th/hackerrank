#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    pfa = []
    total = 0
    result = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            total += 1
    return total



n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

#tried it, not working
# #!/bin/python3
#
# import sys
#
# def solve(n, s, d, m):
#     # Complete this function
#     psa = [0]*(n+1)
#     psa[0] = s[0]
#     result = 0
#     for i in range(n):
#         psa[i+1] = psa[i]+s[i]
#     print('psa = ',psa)
#     for i in range(n-m+1):
#         if (psa[i+m]-psa[i]) == d:
#             print('index j ={},index i = {}'.format(i+m,i))
#             result+=1
#     return result
#
#
# n = int(input().strip())
# s = list(map(int, input().strip().split(' ')))
# d, m = input().strip().split(' ')
# d, m = [int(d), int(m)]
# result = solve(n, s, d, m)
# print(result)
