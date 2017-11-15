if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N) :
        inp = input().strip().split(' ')
        for i in range(1, len(inp)):
            inp[i] = int(inp[i])
        if inp[0] == 'insert' :
            l.insert(inp[1],inp[2])
        if inp[0] == 'print' :
            print(l)
        if inp[0] == 'remove' :
            try:
                l.remove(inp[1])
            except ValueError:
                pass
        if inp[0] == 'append' :
            l.append(inp[1])
        if inp[0] == 'sort' :
            l.sort()
        if inp[0] == 'pop' :
            l.pop()
        if inp[0] == 'reverse' :
            l.reverse()
