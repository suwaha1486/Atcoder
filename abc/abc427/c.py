# 各ノードが｛0, 1｝を取るものとして，n個のノードの全ての組み合わせを求める
# 全組合せに対して，同じ値を持つノードがあればエッジを削除して二部グラフにする
# 全組合せ中，最小の削除数の組合せを求める

from itertools import combinations

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))  # 0-indexed

# n個のノードの全ての組み合わせを求める
min_delete_count = m
set_comb = set(range(n))
for i in range(0, n+1):
    for whitelist in combinations(set_comb, i):
        whitelist = set(whitelist)
        blacklist = set_comb - whitelist
        delete_count = 0
        for u, v in edges:
            if (u in whitelist and v in whitelist) or (u in blacklist and v in blacklist):
                delete_count += 1
        min_delete_count = min(min_delete_count, delete_count)

print(min_delete_count)
