import re

N = int(input().strip())
l = []
for _ in range(N):
    l.append(input())
st1 = '\n'.join(l)
T = int(input().strip())
total = 0
for _ in range(T):
    st2 = input().strip()
    my_regex = re.escape(st2[:-2]) + r'(s|z)e'
    result = re.findall(my_regex, st1)
    print(len(result))