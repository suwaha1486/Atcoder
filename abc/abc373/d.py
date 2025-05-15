from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, -w))

x = [0] * (n + 1)
visited = [False] * (n + 1)

for start in range(1, n + 1):
    if visited[start]:
        continue
    
    q = deque()
    q.append(start)
    x[start] = 0
    visited[start] = True

    while q:
        now = q.popleft()
        for v, w in graph[now]:
            if not visited[v]:
                x[v] = x[now] + w
                visited[v] = True
                q.append(v)

print(*x[1:])