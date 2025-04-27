from collections import deque

q = int(input())
query = [None] * q

card = deque()

for i in range(q):
    query[i] = list(map(int, input().split()))

for i in range(q):
    if query[i][0] == 1:
        card.append(query[i][1])
    else:
        if len(card) == 0:
            print(0)
        else:
            print(card.pop())