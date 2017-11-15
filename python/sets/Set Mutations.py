if __name__ == '__main__':
        _ = input()
        a = set(input().strip().split())
        n = int(input())
        for _ in range(n):
            line = input()
            s = set(input().strip().split())
            if line.startswith('i'):
                a.intersection_update(s)
            elif line.startswith('u'):
                a.update(s)
            elif line.startswith('d'):
                a.difference_update(s)
            elif line.startswith('s'):
                a.symmetric_difference_update(s)
        print(sum([int(i) for i in a]))
