if __name__ == '__main__':
        n = int(input())
        a = set(map(int, input().split()))
        op = int(input())
        for _ in range(op):
            line = input().strip().split()
            if 'pop' in line:
                a.pop()
            elif 'remove' in line:
                a.remove(int(line[1]))
            elif 'discard' in line:
                a.discard(int(line[1]))
            else:
                pass
        print(sum(a))
