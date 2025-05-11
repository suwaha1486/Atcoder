from collections import deque

h, w = map(int, input().split())

s = []
for i in range(h):
    s.append(list(input()))

graph = [[] for _ in range(h * w)]
exit_point = []
dist = [float("inf")] * (h * w)

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        # up
        if i > 0 and s[i - 1][j] != "#":
            graph[i * w + j].append((i - 1) * w + j)
        # down
        if i < h - 1 and s[i + 1][j] != "#":
            graph[i * w + j].append((i + 1) * w + j)
        # left
        if j > 0 and s[i][j - 1] != "#":
            graph[i * w + j].append(i * w + j - 1)
        # right
        if j < w - 1 and s[i][j + 1] != "#":
            graph[i * w + j].append(i * w + j + 1)
        
        if s[i][j] == "E":
            dist[i * w + j] = 0
            exit_point.append(i * w + j)

pre_pos = [-1] * (h * w)

q = deque(exit_point)

while len(q) > 0:
    v = q.popleft()
    for u in graph[v]:
        if dist[v] + 1 < dist[u]:
            dist[u] = dist[v] + 1
            pre_pos[u] = v
            q.append(u)

for i in range(h):
    for j in range(w):
        if s[i][j] == "#" or s[i][j] == "E":
            continue
        if pre_pos[i * w + j] == (i - 1) * w + j:
            s[i][j] = "^"
        elif pre_pos[i * w + j] == (i + 1) * w + j:
            s[i][j] = "v"
        elif pre_pos[i * w + j] == i * w + j - 1:
            s[i][j] = "<"
        elif pre_pos[i * w + j] == i * w + j + 1:
            s[i][j] = ">"

for i in range(h):
    print("".join(s[i]))
