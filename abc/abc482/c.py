import bisect

H, W, N, Q = map(int, input().split())

# 累積でやるとメモリ溢れるから二分探索で
row = []
col = []

for _ in range(N):
    r, c = map(int, input().split())
    row.append(r)
    col.append(c)

row.sort()
col.sort()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, d = query[1], query[2]
        row_cnt = bisect.bisect_right(row, d) - bisect.bisect_left(row, u)
        print(row_cnt)

    else:
        l, r = query[1], query[2]
        col_cnt = bisect.bisect_right(col, r) - bisect.bisect_left(col, l)
        print(col_cnt)