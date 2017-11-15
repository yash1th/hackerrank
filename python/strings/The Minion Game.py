def minion_game(string):
    # your code goes here
    v = 'AEIOU'
    l = len(string)
    ss, ks = 0, 0
    for i in range(l):
        if string[i] in v:
            ks += (l-i)
        else:
            ss += (l-i)
    if ss>ks:
        print('Stuart',ss)
    elif ss<ks:
        print('Kevin',ks)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
