n = int(input())
arr = []
for i in range(n):
    arr.append(input())
nc = int(input())
comp = []
for i in range(nc):
    comp.append(input())
for i in comp:
    print(arr.count(i))
