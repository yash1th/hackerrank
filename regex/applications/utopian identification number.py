import re

n = int(input().strip())
my_regex = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'
c = re.compile(my_regex)
for _ in range(n):
    s = input().strip()
    if c.match(s):
        print('VALID')
    else:
        print('INVALID')