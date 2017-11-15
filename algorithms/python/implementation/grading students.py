#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i,v in enumerate(grades):
        m = v//5
        v2 = (m+1)*5
        if v2 - v < 3 and v2 >= 40:
            grades[i] = v2
    return grades

grades = []
for i in range(int(input())):
    grades.append(int(input()))
result = solve(grades)
print('\n'.join([str(i) for i in result]))


# #!/bin/python3
#
# import sys
#
# def solve(grades):
#     # Complete this function
#
# n = int(input().strip())
# grades = []
# grades_i = 0
# for grades_i in range(n):
#    grades_t = int(input().strip())
#    grades.append(grades_t)
# result = solve(grades)
# print ("\n".join(map(str, result)))
