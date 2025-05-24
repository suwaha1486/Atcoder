h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

xor_total = 0
for i in range(h):
    for j in range(w):
        xor_total ^= a[i][j]

ans = xor_total

def dfs(cell_idx, coverd_mask, current_xor):
    global ans
    if cell_idx == h * w:
        ans = max(ans, xor_total ^ current_xor)
        return
    
    # すでに覆われている場合はスキップ
    if (coverd_mask & (1 << cell_idx)):
        dfs(cell_idx + 1, coverd_mask, current_xor)
        return

    # 覆われていない場合

    # 1. 覆わない
    dfs(cell_idx + 1, coverd_mask, current_xor)

    # 座標を取得
    r, c = cell_idx // w, cell_idx % w

    # 2. 横に覆う
    if c + 1 < w and not (coverd_mask & (1 << (cell_idx + 1))):
        dfs(cell_idx + 1, coverd_mask | (1 << cell_idx) | (1 << (cell_idx + 1)), current_xor ^ a[r][c] ^ a[r][c + 1])

    # 3. 縦に覆う
    if r + 1 < h and not (coverd_mask & (1 << (cell_idx + w))):
        dfs(cell_idx + 1, coverd_mask | (1 << cell_idx) | (1 << (cell_idx + w)), current_xor ^ a[r][c] ^ a[r + 1][c])

dfs(0, 0, 0)

print(ans)
