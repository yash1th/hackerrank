if __name__ == '__main__':
    n = int(input())
    result = set()
    for i in range(n):
        a = input()
        if a not in result:
            result.add(a)
    print(len(result)) 
