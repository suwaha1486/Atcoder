from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = deque()
q.append(1)

dist = [-1] * (n + 1)
dist[1] = 0

while len(q) > 0:
    v = q.popleft()
    for u in graph[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)

for i in range(1, n + 1):
    print(dist[i])