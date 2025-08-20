# TLE submission

import sys 
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(v, path, visited, y):
    if v == y:
        return True
    visited[v] = True
    for u in graph[v]:
        if visited[u]:
            continue
        path.append(u)
        if dfs(u, path, visited, y):
            return True
        path.pop()
    visited[v] = False
    return False

for _ in range(t):
    n, m, x, y = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        graph[i].sort()

    visited = [False] * (n + 1)
    path = [x]
    dfs(x, path, visited, y)
    print(*path)
