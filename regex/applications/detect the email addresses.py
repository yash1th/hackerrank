import re

n = int(input().strip())
s1 = []
for _ in range(n):
    s1.append(input())
s = '\n'.join(s1)
email_regex = r'[a-zA-Z_\.]+@([A-Za-z]+\.){1,5}[a-zA-Z]+'
p = re.compile(email_regex)
l = set()
for i in re.finditer(p,s):
    l.add(i.group(0))
print(*sorted(list(l)),sep=';')