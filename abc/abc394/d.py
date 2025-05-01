from collections import deque

S = list(input())

d = deque()

for s in S:
    if len(d) == 0:
        d.append(s)
        continue
    
    if s == '(' or s == '[' or s == '<':
        d.append(s)
    else:
        left = d.pop()
        if (left == '(' and s == ')') or (left == '[' and s == ']') or (left == '<' and s == '>'):
            continue
        else:
            print('No')
            exit()

if len(d) == 0:
    print('Yes')
else:
    print('No')