from collections import defaultdict
n,m = map(int, input().strip().split(' '))
d = defaultdict(list)
for _ in range(n):
    d['A'].append(input().strip())
for _ in range(m):
    d['B'].append(input().strip())
for b in d['B']:
    if d['A'].count(b) == 0:
            print('-1')
            continue
    for i in range(n):
        if d['A'][i] == b:
            print(i+1,end=' ')
    print()