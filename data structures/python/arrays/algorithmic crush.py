#using concept of prefix sum - remember it
n, o = (int(i) for i in input().split())
arr = [0]*(n+1)
for _ in range(o):
    p, q, m = (int(i) for i in input().split())
    arr[p]+=m
    if (q+1) <= n:
        arr[q+1] -= m
max , x = 0, 0
for i in arr:
    x += i
    if max<x:
        max = x
print(max)

# n, o = (int(i) for i in input().split())
# arr = [0]*n
# for j in range(o):
#     a, b, m = (int(i) for i in input().split())
#     a -= 1
#     b -= 1
#     # for k in range(a,b+1):
#     #     arr[k] += m
#     arr = arr[:a]+list(i+=m for i in range(a,b+1))+arr[b+1:] # does not work, because we have to add existing value to the new one
# print(max(arr))
