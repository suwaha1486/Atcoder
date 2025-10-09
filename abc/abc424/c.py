from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
q = deque()

for i in range(1, n + 1):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        q.append(i)
    else:
        graph[a].append(i)
        graph[b].append(i)

visited = [False] * (n + 1)
while q:
    v = q.popleft()
    if visited[v]:
        continue
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            q.append(u)
    
print(visited.count(True))

'''
# TLE submission
# 模範解答でもTLEとなった
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    a, b = map(int, input().split())
    graph[a].append(i)
    graph[b].append(i)

visited = [False] * (n + 1)
visited[0] = True

def dfs(v, visited):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited)

dfs(0, visited)

print(visited.count(True) - 1)
'''