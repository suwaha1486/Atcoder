from collections import defaultdict
n, m = map(int, input().split())

graph = defaultdict(list)

ans = 0
for i in range(m):
    u, v = map(int, input().split())
    if u == v:
        ans += 1
        continue
    
    if v in graph[u] or u in graph[v]:
        ans += 1
    else:
        graph[v].append(u)
        graph[u].append(v)

print(ans)