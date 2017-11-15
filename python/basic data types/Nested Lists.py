if __name__ == '__main__':
    nm = [[input(),float(input())] for i in range(int(input()))]
    s = sorted(set([x[1] for x in nm] ))
    for name in sorted(x[0] for x in nm if x[1] == s[1]):
        print(name)
        
# n = int(input())
# li = [[input(), float(input())]for _ in range(n)]
# marks = set()
# for x in range(len(li)):
#     marks.add(li[x][1])
# secondHighest = sorted(marks)[1]
# names = []
# for x in range(len(li)):
#     if secondHighest == li[x][1]:
#         names.append(li[x][0])
# names.sort()
# for name in names:
#     print(name)

#above program is a basic version using the builtin functions used in the list

# shortened version by - gkeswani92 (hackerrank handle)
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])
# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))


#another try
# if __name__ == '__main__':
#     marksheet = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         marksheet.append([score,name])
#     marksheet.sort()
#     mi = min(marksheet)[0]
#     while min(marksheet)[0] == mi:
#         marksheet.remove(min(marksheet))
#     mi = min(marksheet)[0]
#     names = []
#     while min(marksheet)[0] == mi:
#         names.append(min(marksheet)[1])
#     names.sort()
#     print('\n'.names)
