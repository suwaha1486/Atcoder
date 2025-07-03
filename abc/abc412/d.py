# 制約に注目：N ≤ 8 なので全探索で最適解を求める
from itertools import permutations

n, m = map(int, input().split())
edges_bitmask = 0

# 入力グラフをビットマスク化
for _ in range(m):
    a, b = map(int, input().split())
    edges_bitmask |= 1 << (a - 1) << (b - 1)

ans = 10**9
# 全ての頂点の順列を生成
for perm in permutations(range(n)):
    # 閉路を作るために最初の頂点を最後に追加
    perm = list(perm) + [perm[0]]
    edges_bitmask_perm = 0
    # 順列からグラフを作成
    for i in range(len(perm) - 1):
        edges_bitmask_perm |= 1 << (perm[i]) << (perm[i + 1])
    
    # 入力グラフと順列から作成したグラフの差分を計算
    diff = edges_bitmask ^ edges_bitmask_perm
    # 差分のビット数を計算
    diff_count = bin(diff).count("1")
    ans = min(ans, diff_count)

print(ans)
