if __name__ == '__main__':
        n = int(input())
        marks={}
        for i in range(n):
            line = input()
            words = line.split()
            marks[words[0]] = (float(words[1])+float(words[2])+float(words[3]))/3
        result = format(marks[input()],'.2f')
        print(result)
