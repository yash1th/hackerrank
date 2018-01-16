import re

n = int(input().strip())
my_regex = r'^\((\+|-)?(90(\.0+)?|[1-8]?[0-9](\.[0-9]+)?), (\+|-)?(180(\.0+)?|(1[0-7][0-9]|[1-9]?[0-9])(\.[0-9]+)?)\)$'
pattern = re.compile(my_regex)
for _ in range(n):
    s = input()
    if pattern.fullmatch(s):
        print('Valid')
    else:
        print('Invalid')