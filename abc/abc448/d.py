from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(v, parent, has_dup, visited_num_dict):
    x = A[v]
    visited_num_dict[x] += 1

    if has_dup or visited_num_dict[x] >= 2:
        now_dup = True
    else:
        now_dup = False
        
    ans[v] = now_dup

    for u in graph[v]:
        if u == parent:
            continue
        dfs(u, v, now_dup, visited_num_dict)

    visited_num_dict[x] -= 1


visited_num_dict = defaultdict(int)
ans = [False] * N

dfs(0, -1, False, visited_num_dict)

for i in range(N):
    print("Yes" if ans[i] else "No")