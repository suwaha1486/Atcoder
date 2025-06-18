# ★4
from collections import defaultdict

h, w = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for i in range(1, 2 ** h):
    use_num = [j for j in range(h) if i & (1 << j)]
    cnt = defaultdict(int)
    for j in range(w):
        value = p[use_num[0]][j]
        for k in use_num:
            if p[k][j] != value:
                break
        else:
            cnt[value] += 1
    max_cnt = max(cnt.values(), default=0)
    ans = max(ans, max_cnt * len(use_num))

print(ans)
