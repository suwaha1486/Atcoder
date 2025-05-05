from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c, d = map(int, input().split())
    c *= 10 ** 7
    c -= d
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heappush(q, (0, 1))

dist = [float('inf')] * (n + 1)
dist[1] = 0

while len(q) > 0:
    d, u = heappop(q)
    for v, c in graph[u]:
        if dist[v] > d + c:
            dist[v] = d + c
            heappush(q, (dist[v], v))

ans_dist = dist[n] // 10 ** 7 + 1
ans_tree = ans_dist * (10 ** 7) - dist[n]

print(ans_dist, ans_tree, sep=' ')