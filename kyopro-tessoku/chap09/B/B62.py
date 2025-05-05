import sys 
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited, path):
    visited[v] = True
    for u in graph[v]:
        if u == n:
            path.append(u)
            print(*path, sep=' ')
            exit()

        if not visited[u]:
            path.append(u)
            dfs(u, visited, path)
            path.pop()

visited = [False] * (n + 1)
path = [1]
dfs(1, visited, path)