if __name__ == '__main__':
    _ = input()
    a = {int(i) for i in input().split()}
    _ = input()
    b = {int(i) for i in input().split()}
    c = list(a.symmetric_difference(b))
    for i in sorted(c):
        print(i)
