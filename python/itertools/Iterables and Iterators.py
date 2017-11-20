from itertools import combinations
_ = input()
L = [i for i in input().strip().split(' ')]
K = int(input().strip())
C = list(combinations(L, K))
F = list(filter(lambda c: 'a' in c, C))
print(len(F)/len(C))