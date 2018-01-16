import re

n = int(input().strip())
my_regex = r'^(_|\.)\d+[a-zA-Z]*_?$'
pattern = re.compile(my_regex)
for _ in range(n):
    s = input()
    if pattern.match(s):
        print('VALID')
    else:
        print('INVALID')