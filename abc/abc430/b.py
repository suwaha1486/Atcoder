n, m = map(int, input().split())

s = [input() for _ in range(n)]

grid_mm = set()

for i in range(n-m+1):
    for j in range(n-m+1):
        tmp = ''
        for k in range(i, i+m):
            tmp += s[k][j:j+m]
        grid_mm.add(tmp)

print(len(grid_mm))