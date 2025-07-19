# ★5
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

import heapq

def dijkstra(start):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        d, v = heapq.heappop(hq)
        if dist[v] < d:
            continue
        for nv, cost in graph[v]:
            if dist[nv] > dist[v] + cost:
                dist[nv] = dist[v] + cost
                heapq.heappush(hq, (dist[nv], nv))
    return dist

forward_dist = dijkstra(1)
backward_dist = dijkstra(n)

for i in range(1, n+1):
    print(forward_dist[i] + backward_dist[i])
