import re

N = int(input())
for _ in range(N):
    s = input().strip()
    r = re.split(r'(\s|-)',s)
    print('CountryCode={},LocalAreaCode={},Number={}'.format(r[0],r[2],r[4]))