if __name__ == '__main__':
    n = int(input())
    integer_list = [int(i) for i in input().split()]
    print(hash(tuple(integer_list)))
