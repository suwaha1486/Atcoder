n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


min_path_w = float('inf')
visited = [False] * (n + 1)

def dfs(v, visited, current_weight, n, graph):
    visited[v] = True
    global min_path_w

    if v == n:
        min_path_w = min(min_path_w, current_weight)

    for u, w in graph[v]:
        if not visited[u]:
            new_weight = w if v == 1 else current_weight ^ w
            dfs(u, visited, new_weight, n, graph)
    
    visited[v] = False

dfs(1, visited, 0, n, graph)

print(min_path_w)