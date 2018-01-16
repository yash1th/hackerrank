import re

my_regex = r'^[A-Z]{5}\d{4}[A-Z]$'
p = re.compile(my_regex)
n = int(input().strip())
for _ in range(n):
    s = input().strip()
    if p.match(s):
        print('YES')
    else:
        print('NO')