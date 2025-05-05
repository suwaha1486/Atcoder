import sys 
sys.setrecursionlimit(10**6)

n, t = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)
            buka[v] = max(buka[v], buka[u] + 1)

visited = [False] * (n + 1)
buka = [0] * (n + 1)

dfs(t, visited)
print(*buka[1:], sep=' ')