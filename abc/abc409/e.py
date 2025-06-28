import sys
sys.setrecursionlimit(10 ** 7)

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

# 部分木の電荷の合計を計算し、親子間の移動コストを累積する
ans = 0
def dfs(u, parent=-1):
    global ans
    total = x[u]
    for v, w in graph[u]:
        if v == parent:
            continue
        child = dfs(v, u)
        ans += abs(child) * w
        total += child
    return total

dfs(0)
print(ans)
