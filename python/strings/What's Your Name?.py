def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# print("Hello "+input()+" "+input()+"! You just delved into python.")
# the above version is not a good practice
# http://programmers.stackexchange.com/questions/304445/why-is-s-better-than-for-concatenation

# print("Hello %s %s! You just delved into python." %(input(),input()))
