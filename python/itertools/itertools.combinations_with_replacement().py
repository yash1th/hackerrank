from itertools import combinations_with_replacement
i = input().split()
a = sorted(list(i[0]))
b = int(i[1])
r = list(combinations_with_replacement(a,b))
for i in r:
    print(''.join(i))
