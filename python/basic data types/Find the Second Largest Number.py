if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
z = max(arr)
while max(arr) == z:
	arr.remove(z)#agj
print(max(arr))
