import heapq

q = int(input())
heap = []

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        heapq.heappush(heap, x)
    elif query[0] == 2:
        print(heapq.heappop(heap))
