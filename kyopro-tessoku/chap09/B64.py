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
prev = [-1] * (n + 1)
dist[1] = 0

while q:
    d, u = heapq.heappop(q)
    if d > dist[u]:
        continue
    for v, c in graph[u]:
        if dist[v] > d + c:
            dist[v] = d + c
            prev[v] = u
            heapq.heappush(q, (dist[v], v))

ans = []
pos = n
while pos != -1:
    ans.append(pos)
    pos = prev[pos]
    
ans.reverse()

print(*ans, sep=' ')