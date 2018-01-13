#replace all occurences of our in input to or
import re

N = int(input().strip())
l = []
for _ in range(N):
    l.append(input())
st1 = '\n'.join(l)
st1 = st1.replace('our','or')
T = int(input().strip())
total = 0
for _ in range(T):
    st2 = input().strip()
    st3 = st2.replace('our','or')
    my_regex = r'\b'+re.escape(st2)+r'\b'
    result = len(re.findall(my_regex, st1))
    print(result)


#without replacing 

# import re

# N = int(input().strip())
# l = []
# for _ in range(N):
#     l.append(input())
# st1 = '\n'.join(l)
# T = int(input().strip())
# total = 0
# for _ in range(T):
#     st2 = input().strip()
#     st3 = st2.replace('our','or')
#     my_regex = r'\b'+re.escape(st2)+r'\b'
#     result = len(re.findall(my_regex, st1))
#     #print('result 1 :',result)
#     my_regex = r'\b'+re.escape(st3)+r'\b'
#     result += len(re.findall(my_regex, st1))
#     #print('result 2 :',result)
#     print(result)