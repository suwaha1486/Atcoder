# ★2
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]


row = [0] * h
col = [0] * w

for i in range(h):
    for j in range(w):
        row[i] += a[i][j]
        col[j] += a[i][j]

ans = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        ans[i][j] = row[i] + col[j] - a[i][j]

for i in range(h):
    print(*ans[i])
