def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# line = input()
# a = []
# for i in line:
#     if i.isupper():
#         a.append(i.lower())
#     else:
#         a.append(i.upper())
# print(''.join(a))
