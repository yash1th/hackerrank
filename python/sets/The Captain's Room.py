k = int(input())
arr = [int(i) for i in input().strip().split()]
s1 = set() #all unique room number
s2 = set() #all unique room number occur more than once
for i in arr:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print(list(s3)[0])

#valid solution as well (editorial)
# k = int(input())
# a = [int(i) for i in input().strip().split()]
# d = set(a)
# print((sum(d)*k - sum(a))//(k-1))

# k = int(input())
# a = input().strip().split()
# d = set(a)
# for i in d:
#     if a.count(i)==1:
#         print(int(i))
#         break
#better solution passed - 5 test cases


# k = int(input())
# a = input().strip().split()
# d = (i for i in a if a.count(i)==1)
# print(type(d))
# print(int(next(iter(d))))


# k = int(input())
# a = input().strip().split()
# for i in range(len(a)):
#     if a.count(a[i]) != k:
#         print(int(a[i]))
#         break
#

# k = int(input())
# a = input().strip().split()
# d = {i for i in a if a.count(i)==1}
# print(int(next(iter(d))))




# k = int(input())
# a = input().strip().split()
# step = len(a)//k
# d = {i:a.count(i) for i in a}
# for key in d:
#      if d[key]!=k:
#          print(int(key))
#          break

# k = int(input())
# a = input().strip().split()
# a.sort()
# step = len(a)//k
# for i in range(0,len(a),step-1):
#     if a.count(a[i]) != k:
#         break
# print(int(a[i]))
# #1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
