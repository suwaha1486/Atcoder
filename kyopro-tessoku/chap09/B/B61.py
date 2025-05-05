n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans_idx = 1
for i in range(2, n + 1):
    if len(graph[i]) > len(graph[ans_idx]):
        ans_idx = i

print(ans_idx)