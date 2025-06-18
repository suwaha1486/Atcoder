# ★4
h, w = map(int, input().split())
c = []
for i in range(h):
    c.append(list(input()))

graph = [[] for _ in range(h * w)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            continue
        if i > 0 and c[i - 1][j] == ".":
            graph[i * w + j].append((i - 1) * w + j)
        if i < h - 1 and c[i + 1][j] == ".":
            graph[i * w + j].append((i + 1) * w + j)
        if j > 0 and c[i][j - 1] == ".":
            graph[i * w + j].append(i * w + j - 1)
        if j < w - 1 and c[i][j + 1] == ".":
            graph[i * w + j].append(i * w + j + 1)

# 孤立したノードを削除
for i in range(h * w):
    if len(graph[i]) < 2:
        for neighbor in graph[i]:
            graph[neighbor].remove(i)
        graph[i] = []

def dfs(v, visited, dist_list):
    visited[v] = True
    for u in graph[v]:
        # startから始まるパスを探索するときに、startより小さいノードは探索しない
        if v == start and u < start:
            continue
        # 探索済みのノードは探索しない
        if not visited[u]:
            dfs(u, visited, dist_list)
            visited[u] = False
        # スタートに戻ったら距離を記録
        # 3回以上訪れたら記録
        if u == start and sum(visited) > 3:
            dist_list.append(sum(visited))

# DFSで探索
ans = -1
for start in range(h * w):
    if graph[start] == []:
        continue
    visited = [False] * (h * w)
    visited[start] = True
    dist_list = []
    dfs(start, visited, dist_list)
    if dist_list:
        ans = max(ans, max(dist_list))

print(ans)
