N, S, L = map(int, input().split())
A = list(map(int, input().split()))

# 累積和？

P = [0] * N
for i in range(N - 1):
    P[i + 1] = P[i] + A[i]

ans = 1
S -= 1

# 尺取り法
r = S
for l in range(S + 1):
    while r + 1 < N:
        x = P[S] - P[l]
        y = P[r + 1] - P[S]

        if x + y + min(x, y)<= L:
            r += 1
        else:
            break
    x = P[S] - P[l]
    y = P[r] - P[S]
    
    if x + y + min(x, y)<= L:
        ans = max(ans, r - l + 1)
print(ans)