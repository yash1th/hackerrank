import re

n = int(input().strip())
my_regex = r'hackerrank'
total = 0
for _ in range(n):
    s = input().strip()
    if re.search(my_regex,s,re.IGNORECASE):
        total += 1
print(total)