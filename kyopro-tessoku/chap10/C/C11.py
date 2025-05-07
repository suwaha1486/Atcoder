n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 1.0
right = 10**9
border = 0.0

# whileだと上手く行かなかったのでfor文で60回回す
# 1e-9の精度で二分探索するために60回回す
for _ in range(60):
    mid = (left + right) / 2.0
    if sum(int(ai / mid) for ai in a) >= k:
        left = mid
        border = max(border, mid)
    else:
        right = mid

ans = [int(ai / border) for ai in a]
print(*ans)