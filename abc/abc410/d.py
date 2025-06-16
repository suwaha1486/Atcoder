# xor -> 1024種類
# n * xor -> 1000 * 1024 ~= 10^6
# visitの状態表現を工夫

import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited = defaultdict(set)
ans = 10**18

def dfs(v, w_bit, visited):
    global ans
    for u, w in graph[v]:
        if u == n:
            ans = min(ans, w_bit ^ w)
        if w_bit ^ w not in visited[u]:
            visited[u].add(w_bit ^ w)
            dfs(u, w_bit ^ w, visited)
    return

dfs(1, 0, visited)
if ans == 10**18:
    print(-1)
else:
    print(ans)
