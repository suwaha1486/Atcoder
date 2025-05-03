n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)

visited = [False] * (n + 1)
dfs(1, visited)
if all(visited[1:]):
    print("The graph is connected.")
else:
    print("The graph is not connected.")