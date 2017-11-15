def merge_the_tools(string, k):
    l = []
    for i in range(0,len(string),k):
        l.append(string[i:i+k])
    result = []
    for i,v in enumerate(l):
        temp = []
        for k in v:
            if k not in temp:
                temp.append(k)
        result.append(''.join(temp))
    print('\n'.join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
