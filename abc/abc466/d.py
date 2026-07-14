N, M = map(int, input().split())
rc = [list(map(int, input().split())) for _ in range(M)]
rc.reverse()

row_set = set()
col_set = set()

ans = 0
for r, c in rc:
    if not (r in row_set) and not (c in col_set):
        ans += 1
    row_set.add(r)
    col_set.add(c)

print(ans)