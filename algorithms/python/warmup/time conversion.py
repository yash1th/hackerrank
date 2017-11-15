#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    tarr = s[:-2].split(':')
    if 'PM' in s and tarr[0] != '12':
        tarr[0] = str(12 + int(tarr[0]))
    if 'AM' in s and tarr[0] == '12':
        tarr[0] = '00'
    return tarr

s = input().strip()
result = timeConversion(s)
print(':'.join(result))
