import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

if n != m:
    print('No')
    exit()

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if len(graph[i]) != 2:
        print('No')
        exit()

def dfs(v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)

visited = [False] * (n + 1)
dfs(1, visited)

if all(visited[1:]):
    print('Yes')
else:
    print('No')