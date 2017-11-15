from itertools import product
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
l = list(product(a,b))
for i in l:
    print(i,end=' ')
