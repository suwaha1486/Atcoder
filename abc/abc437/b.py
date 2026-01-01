h, w, n = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]

b = []
for i in range(n):
    tmp = int(input())
    b.append(tmp)

ans = 0
for i in range(h):
    i_line = 0
    for j in range(w):
        for k in range(n):
            if a[i][j] == b[k]:
                i_line += 1
    ans = max(ans, i_line)

print(ans)