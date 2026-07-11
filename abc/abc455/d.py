N, Q = map(int, input().split())
up = [-1] * (N + 1)
down = [-1] * (N + 1)
for _ in range(Q):
    c, p = map(int, input().split())
    # 動かされていなくなった
    if down[c] != -1:
        up[down[c]] = -1
    # 動かしたカードの下
    down[c] = p
    # 動かされてきたカード
    up[p] = c
    
ans = [0] * (N + 1)
for i in range(1, N + 1):
    if down[i] == -1:
        idx = i
        cnt = 1
        while up[idx] != -1:
            idx = up[idx]
            cnt += 1
        ans[i] = cnt

print(*ans[1:])