# give up
from collections import deque

h, w = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs, cs, rt, ct = rs - 1, cs - 1, rt - 1, ct - 1

s = []
for _ in range(h):
    s.append(input())

# 4方向の移動ベクトル
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 各頂点の各方向での最小方向転換回数を保持
dist = [[float('inf')] * 4 for _ in range(h * w)]

q = deque()

# 初期状態を4方向すべてキューに追加
for i in range(4):
    dist[rs * w + cs][i] = 0
    q.append((rs * w + cs, i))

while q:
    v, d = q.popleft()
    i, j = v // w, v % w
    
    # 現在の方向に進む
    ni, nj = i + dx[d], j + dy[d]
    if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.':
        nv = ni * w + nj
        if dist[nv][d] > dist[v][d]:
            dist[nv][d] = dist[v][d]
            q.appendleft((nv, d))
    
    # 方向転換
    for nd in range(4):
        if nd != d:
            if dist[v][nd] > dist[v][d] + 1:
                dist[v][nd] = dist[v][d] + 1
                q.append((v, nd))

# 目標地点の4方向の最小値が答え
print(min(dist[rt * w + ct]))
