m,n = input().strip().split()
h = input().strip().split()
a = set(input().strip().split())
b = set(input().strip().split())
totalHappiness = 0
for i in h:
    if i in a:
        totalHappiness+=1
    elif i in b:
        totalHappiness-=1
    else:
        pass
print(totalHappiness)
