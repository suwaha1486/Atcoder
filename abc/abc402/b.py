from collections import deque

q = int(input())

order = deque()

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        order.append(query[1])
    elif query[0] == 2:
        print(order.popleft())