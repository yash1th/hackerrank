from itertools import permutations
i = input().split()
a = sorted(list(i[0]))
b = int(i[1])
r = list(permutations(a,b))
for i in r:
    print(''.join(i))
