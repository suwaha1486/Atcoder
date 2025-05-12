from collections import deque

h, w, d = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

graph = [[] for _ in range(h * w)]
dist = [float("inf")] * (h * w)
humidifier_pos = []

for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
            if i + 1 < h and s[i + 1][j] != "#":
                graph[i * w + j].append((i + 1) * w + j)
            if i - 1 >= 0 and s[i - 1][j] != "#":
                graph[i * w + j].append((i - 1) * w + j)
            if j + 1 < w and s[i][j + 1] != "#":
                graph[i * w + j].append(i * w + j + 1)
            if j - 1 >= 0 and s[i][j - 1] != "#":
                graph[i * w + j].append(i * w + j - 1)

        if s[i][j] == "H":
            humidifier_pos.append(i * w + j)
            dist[i * w + j] = 0

q = deque(humidifier_pos)

while q:
    v = q.popleft()
    for u in graph[v]:
        if dist[v] + 1 < dist[u]:
            dist[u] = dist[v] + 1
            q.append(u)

ans = 0
for i in range(h):
    for j in range(w):
        if dist[i * w + j] <= d:
            ans += 1

print(ans)