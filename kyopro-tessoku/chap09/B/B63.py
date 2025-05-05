from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

meiro = []
for i in range(r):
    meiro.append(list(input()))

graph = [[] for _ in range(r * c)]

for i in range(r):
    for j in range(c):
        if meiro[i][j] == "#":
            continue
        # left
        if i > 0 and meiro[i - 1][j] == ".":
            graph[i * c + j].append((i - 1) * c + j)
            graph[(i - 1) * c + j].append(i * c + j)

        # up
        if j > 0 and meiro[i][j - 1] == ".":
            graph[i * c + j].append(i * c + j - 1)
            graph[i * c + j - 1].append(i * c + j)
            
q = deque()
q.append((sy - 1) * c + sx - 1)

dist = [-1] * (r * c)
dist[(sy - 1) * c + sx - 1] = 0

while len(q) > 0:
    v = q.popleft()
    for u in graph[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)

print(dist[(gy-1) * c + gx-1])