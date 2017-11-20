from itertools import *
K, M = (int(i) for i in input().strip().split(' '))
L = []
for _ in range(K):
    L.append([int(i) for i in input().strip().split(' ',1)[1].split(' ')])
results = max(map(lambda x: sum(i**2 for i in x)%M, product(*L)))
print(results)

#we need to find the maximum of all possible values of S, that's the key