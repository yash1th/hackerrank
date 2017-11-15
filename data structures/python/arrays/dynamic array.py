def findSequence(x, lastAnswer, n):
    return ((x^lastAnswer)%n)
s = []
n, q = (int(i) for i in input().split())
lastAnswer = 0
for i in range(n):
    s.append([])
for i in range(q):
    qn, x, y = (int(i) for i in input().split())
    if qn == 1:
        s[findSequence(x, lastAnswer, n)].append(y)
    if qn == 2:
        index = findSequence(x, lastAnswer, n)
        lastAnswer = s[index][y%len(s[index])]
        print(lastAnswer)
