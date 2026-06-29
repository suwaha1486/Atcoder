H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

top = 0
down = H - 1
left = 0
right = W - 1

for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            top = max(top, i)
            down = min(down, i)
            left = max(left, j)
            right = min(right, j)

for i in range(down, top + 1):
    for j in range(right, left + 1):
        print(C[i][j], end="")
    print()