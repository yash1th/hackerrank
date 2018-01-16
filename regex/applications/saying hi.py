import re

n = int(input().strip())
my_regex = r'^[hH][iI]\s[^dD]'
for _ in range(n):
    s = input().strip()
    if re.search(my_regex, s):
        print(s)