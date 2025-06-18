# ★4
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
d = [-1] * (n + 1)
d[1] = 0

while q:
    v = q.popleft()
    for u in graph[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)

even = []
odd = []
for i in range(1, n + 1):
    if d[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

if len(even) >= n // 2:
    print(*even[:n//2])
else:
    print(*odd[:n//2])
