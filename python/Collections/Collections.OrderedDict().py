from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    fieldname, price = input().rsplit(' ',1)
    d[fieldname] = d.get(fieldname, 0)+int(price)
for k,v in d.items():
    print(k,v,sep=' ')