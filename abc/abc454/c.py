N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 有向グラフ上で1から始まって，到達できるノードを列挙する
visited = [False] * (N + 1)

def dfs(v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)

dfs(1, visited)

print(visited.count(True))