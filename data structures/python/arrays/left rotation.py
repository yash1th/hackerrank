import sys
def print_array(p):
    for i in p:
        print(i,end=' ')
    print('\n')
_, r = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
l = len(arr)
if r%l == 0:
    print_array(arr)
    sys.exit()
if r>l:
    r = r%l
result = arr[r:]+arr[:r]
print_array(result)
