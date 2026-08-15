import heapq

Q, V = map(int, input().split())

battery = []
heapq.heapify(battery)

# wq - tqの最大値を管理

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        tq = query[1]
        wq = query[2]
        heapq.heappush(battery, -(wq - tq))
    elif query[0] == 2:
        tq = query[1]
        if battery:
            max_value = -heapq.heappop(battery)
            print(min(max_value + tq, V))
        else:
            print(-1)