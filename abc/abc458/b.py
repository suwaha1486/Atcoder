H, W = map(int, input().split())

ans_grid = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        # up
        if i > 0:
            ans_grid[i][j] += 1
        
        # down
        if i < H - 1:
            ans_grid[i][j] += 1

        # left
        if j > 0:
            ans_grid[i][j] += 1

        # right
        if j < W - 1:
            ans_grid[i][j] += 1

for i in range(H):
    print(*ans_grid[i])