from collections import namedtuple
n = int(input())
student_record = namedtuple('whatsmypurpose',input().split())
total_marks = 0
for _ in range(n):
    values = tuple(input().split())
    sr = student_record(*values)
    total_marks += int(sr.MARKS)
print(total_marks/n)
