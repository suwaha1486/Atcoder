from collections import deque

q = int(input())

p = deque()

for i in range(q):
    query = list(input().split())
    if query[0] == "1":
        p.append(query[1])
    elif query[0] == "2":
        print(p[0])
    elif query[0] == "3":
        p.popleft()