k,m = (int(i) for i in input().split())
max_list = []
for _ in range(k):
    l = [int(i) for i in input().split()]
    del l[0]
    max_list.append(max(l))
total_max_square = sum((i**2 for i in max_list))
print(total_max_square%m)

#still needs work to be done
