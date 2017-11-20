from collections import deque
d = deque()
for _ in range(int(input())):
    command = input().split()
    if 'append' in command:
        d.append(int(command[1]))
    elif 'appendleft' in command:
        d.appendleft(int(command[1]))
    elif 'pop' in command:
        d.pop()
    elif 'popleft' in command:
        d.popleft()
print(*list(d))