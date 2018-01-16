import re

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    if re.search(r'^hackerrank(.*hackerrank)?$',s):
        print('0')
    elif re.search(r'^hackerrank',s):
        print('1')
    elif re.search(r'hackerrank$',s):
        print('2')
    else:
        print('-1')