size = int(input())
alphabets = [chr(i) for i in range(97,123)]
result = []
for i in range(size):
    row = alphabets[size-1:size-1-i:-1]+alphabets[size-i-1:size]
    result.append("-".join(row).center(4*size-3,"-"))
if size>1:
    for i in result:
            print(i)
    for i in result[len(result)-2::-1]:
            print(i)
else:
     print('a')

#the above is a hard coding


#the below is a better one

# for i in range(size):
#     s = "-".join(alphabets[i:size])
#     result.append((s[::-1]+s[1:]).center(4*size-3,"-"))
# print('\n'.join(result[:0:-1]+result))
