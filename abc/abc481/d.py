from collections import deque

N, M, S, T = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

dist = [float('inf')] * (N + 1)
queue = deque([S])
dist[S] = 0

for g in graph:
    g.sort()

while queue:
    u = queue.popleft()
    for i in range(len(graph[u])):
        v = graph[u][i]
        if i == 0:
            cost = 0
        else:
            cost = 1
        if dist[v] > dist[u] + cost:
            dist[v] = dist[u] + cost
            
            if cost == 0:
                queue.appendleft(v)
            else:
                queue.append(v)

if dist[T] == float('inf'):
    print(-1)
else:
    print(dist[T])
