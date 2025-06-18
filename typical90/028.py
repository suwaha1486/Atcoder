# ★4
n = int(input())

square = [[0] * 1001 for _ in range(1001)]

for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    square[lx][ly] += 1
    square[lx][ry] -= 1
    square[rx][ly] -= 1
    square[rx][ry] += 1

cumsum = [[0] * 1001 for _ in range(1001)]
for i in range(1001):
    for j in range(1001):
        if j > 0:
            cumsum[i][j] = cumsum[i][j - 1] + square[i][j]
        else:
            cumsum[i][j] = square[i][j]

for i in range(1001):
    for j in range(1001):
        if i > 0:
            cumsum[i][j] += cumsum[i - 1][j]

cluttered = [0] * (n + 1)
for i in range(1001):
    for j in range(1001):
        cluttered[cumsum[i][j]] += 1

for i in range(1, n + 1):
    print(cluttered[i])
