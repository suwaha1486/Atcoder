N = int(input())
A = list(map(int, input().split()))

# 目標：max(最大到達点座標 - 最小到達座標 + 1)とする高々一点の符号反転を考える

up_down = [[0, 0] for _ in range(N + 1)]  # i~N-1で[最大上昇量，最大下降量]

prev, prev_max, prev_min = 0, 0, 0

for i in range(N - 1, -1, -1):
    if A[i] > 0:
        prev_min = min(prev_min, prev - A[i])
        prev = prev - A[i]

    elif A[i] < 0:
        prev_max = max(prev_max, prev - A[i])
        prev = prev - A[i]
    
    up_down[i][0] = prev_max - prev
    up_down[i][1] = prev_min - prev

band_upper, band_lower = 0, 0
prev = 0
max_band_len = 0

for i in range(N):
    # A[i]の符号を入れ替える
    rev_prev = prev - A[i]
    rev_band_upper = max(band_upper, rev_prev)
    rev_band_lower = min(band_lower, rev_prev)
    rev_band_max = max(rev_band_upper, rev_prev + up_down[i + 1][0])
    rev_band_min = min(rev_band_lower, rev_prev + up_down[i + 1][1])
    rev_band_len = rev_band_max - rev_band_min + 1
    max_band_len = max(max_band_len, rev_band_len)

    prev = prev + A[i]
    band_upper = max(band_upper, prev)
    band_lower = min(band_lower, prev)

jun_band_len = band_upper - band_lower + 1
print(max(max_band_len, jun_band_len))