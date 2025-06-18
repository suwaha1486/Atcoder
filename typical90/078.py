# ★2
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[max(a, b)].append(min(a, b))

cnt = 0
for i in range(2, n + 1):
    if len(graph[i]) == 1:
        cnt += 1

print(cnt)
