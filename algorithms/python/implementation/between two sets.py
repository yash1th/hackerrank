


# I understood the problem wrong on so many levels
# #!/bin/python3
#
# import sys
#
# def getTotalX(a, b):
#     # Complete this function
#     total = 0
#     aflag = True
#     bflag = True
#     for i in range(max(a),min(b)):
#         print('i = ',i)
#         for af in a:
#             print('af = ',af)
#             if i%af != 0:
#                 aflag = False
#                 break
#         for bf in b:
#             print('bf = ',bf)
#             if bf%i != 0:
#                 bflag = False
#                 break
#         print('aflag = {}, bflag = {}'.format(aflag,bflag))
#         if aflag and bflag:
#             total += 1
#         aflag, bflag = (True,)*2
#     return total
#
# n, m = [int(i) for i in input().strip().split(' ')]
# a = list(map(int, input().strip().split(' ')))
# b = list(map(int, input().strip().split(' ')))
# total = getTotalX(a, b)
# print(total)
