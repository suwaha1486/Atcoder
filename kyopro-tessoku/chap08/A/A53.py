import heapq

q = int(input())

item = []

for i in range(q):
    query = list(map(int, input().split()))
    a = query[0]
    if a == 1:
        heapq.heappush(item, query[1])
    elif a == 2:
        print(item[0])
    elif a == 3:
        heapq.heappop(item)