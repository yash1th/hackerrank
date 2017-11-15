def print_formatted(number):
    # your code goes here
    width = len(bin(n).split('b')[1]) #newbies might get an error here, as it should be length
    for i in range(1,number+1):
         print("%s %s %s %s"%(str(i).rjust(width), oct(i).split('o')[1].rjust(width),hex(i).split('x')[1].upper().rjust(width),bin(i).split('b')[1].rjust(width)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
