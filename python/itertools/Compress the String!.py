from itertools import groupby
a = []
for group, items in groupby(input().strip()):
    a.append((len(list(items)), int(group)))
print(*a)