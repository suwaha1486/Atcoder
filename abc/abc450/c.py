from collections import deque

H, W = map(int, input().split())
S = list(input() for _ in range(H))

visited = [[False] * W for _ in range(H)]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    touch_border = False

    while q:
        x, y = q.popleft()
        if x == 0 or x == H - 1 or y == 0 or y == W - 1:
            touch_border = True

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (0 <= nx < H) and (0 <= ny < W) and (S[nx][ny] == '.') and (not visited[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny))

    return not touch_border

ans = 0
for x in range(H):
    for y in range(W):
        if S[x][y] == '.' and not visited[x][y]:
            if bfs(x, y):
                ans += 1

print(ans)
