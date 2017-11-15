flag = True
s = set(i for i in input().split())
for i in range(int(input())):
    a = set(i for i in input().split())
    if not s>a:
        flag = False
        break
print(flag)

#check the editorial
# flag = True
# s = set(i for i in input().split())
# l = len(s)
# for i in range(int(input())):
#     a = set(i for i in input().split())
#     la = len(a)
#     if not s.issuperset(a) :
#         flag = False
#         break
#     else:
#         if l == la:
#             flag = False
#             break
# print(flag)
