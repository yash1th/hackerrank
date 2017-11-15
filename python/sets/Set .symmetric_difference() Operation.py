if __name__ == '__main__':
        _ = input()
        a = set(input().strip().split())
        _ = input()
        b = set(input().strip().split())
        print(len(a.symmetric_difference(b)))
