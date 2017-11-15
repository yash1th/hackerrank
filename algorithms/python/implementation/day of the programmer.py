#!/bin/python3

import sys

def solve(year):
    # Complete this function
    if year == 1918:
        return '26.09.1918'
    elif ((year<1918) and (year%4==0)) or ((year>1918) and ((year%400==0) or (year%4 == 0 and year%100 != 0))):
        return '12.09.%s'%year
    else:
        return '13.09.%s'%year


year = int(input().strip())
result = solve(year)
print(result)


#if year>1918:

#     number_of_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if year%4 == 0:
#         number_of_days[1] = 29
#     total = 0
#     for month in range(len(number_of_days)):
#         if total+number_of_days[month]>=256:
#             break
#         else:
#             total += number_of_days[month]
#     month += 1
#     if month < 10:
#         month = '0'+str(month)
#     else:
#         month = str(month)
# return '{}.{}.{}'.format(256-total,month,year)
