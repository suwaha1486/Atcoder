import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1))

dist = [float('inf')] * (n + 1)
dist[1] = 0

while len(q) > 0:
    d, u = heapq.heappop(q)
    for v, c in graph[u]:
        if dist[v] > d + c:
            dist[v] = d + c
            heapq.heappush(q, (dist[v], v))

for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])