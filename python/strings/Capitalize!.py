def capitalize(string):
    return ' '.join([i.capitalize() for i in string.split(' ')])

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)


# s = input().split(" ") #if i use default .split() it will strip the whitespace otherwise it will only consider single space
# for i in range(len(s)):
#     s[i] = s[i].capitalize()
# print(" ".join(s))
