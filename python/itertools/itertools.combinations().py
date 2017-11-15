from itertools import combinations
i = input().split()
a = sorted(list(i[0]))
b = int(i[1])
for k in range(1,b+1):
    r = list(combinations(a,k))
    for i in r:
        print(''.join(i))
