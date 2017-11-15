#slightly modified
def count_substring(string, sub_string):
    count = 0
    ssl = len(sub_string)
    for i in range(len(string)):
        if string[i:i+ssl] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# count = 0
# st1 = input()
# st2 = input()
# for i in range(len(st1)):
#     if st1[i:i+len(st2)] == st2:
#         count+=1
# print(count)
