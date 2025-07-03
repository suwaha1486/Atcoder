# 制約に注目：N ≤ 8 なので全探索で最適解を求める
from itertools import permutations

n, m = map(int, input().split())

# 1. {u,v}(u<v) -> bit index を割り当てる
edge_idx = {}
idx = 0
for u in range(n):
    for v in range(u + 1, n):
        edge_idx[(u, v)] = idx
        idx += 1

# 2. 入力グラフをビットマスク化
original_graph = 0
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    original_graph |= 1 << edge_idx[(a, b)]

ans = 10 ** 9

# 3. 順列を全探索
vertices = list(range(n))   # 順列の要素を格納するリスト

# index u -> perm[u] のエッジ
for perm in permutations(vertices):
    # 3-1. 自己ループがあるか判定
    self_loop = False
    for i in range(n):
        if perm[i] == i:
            self_loop = True
            break
    if self_loop:
        continue

    # 3-2. 多重辺があるか判定
    visited = [False] * n
    ok = True
    for s in vertices:
        if visited[s]:
            continue
        v = s
        length = 0
        while not visited[v]:
            visited[v] = True
            v = perm[v]
            length += 1
        if length < 3:
            ok = False
            break
    if not ok:
        continue

    # 4. 順列から無向辺集合を作る
    mask = 0
    for u in vertices:
        v = perm[u]
        if u > v:
            u, v = v, u
        mask |= 1 << edge_idx[(u, v)]

    ans = min(ans, (original_graph ^ mask).bit_count())

print(ans)
