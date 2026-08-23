from collections import deque

H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

# 1. 安全な行・列を特定
safe_rows = []
safe_columns = []

for i in range(H):
    if all(S[i][j] == '.' for j in range(W)):
        safe_rows.append(i)

for j in range(W):
    if all(S[i][j] == '.' for i in range(H)):
        safe_columns.append(j)


# 2. すべての安全な空マスを始点にしてBFS
dist = [[-1] * W for _ in range(H)]
q = deque()

# 安全な空マス = safe_rows × safe_columns
for i in safe_rows:
    for j in safe_columns:
        dist[i][j] = 0
        q.append((i, j))


# 3. BFS
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

while q:
    x, y = q.popleft()

    if dist[x][y] == K:
        continue

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < H and 0 <= ny < W):
            continue

        if S[nx][ny] == '#':
            continue

        if dist[nx][ny] != -1:
            continue

        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))


# 4. 到達可能なマスを数える
ans = 0

for i in range(H):
    for j in range(W):
        if dist[i][j] != -1:
            ans += 1

print(ans)