n = int(input())
dt = []

d_max = 0
for i in range(n):
    t, d = map(int, input().split())
    dt.append((d, t))
    if d > d_max:
        d_max = d

dt.sort()

dp = [[-1] * (d_max + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n+1):
    for j in range(d_max + 1):
        if dp[i-1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j + dt[i-1][1] <= dt[i-1][0]:
                dp[i][j + dt[i-1][1]] = max(dp[i-1][j] + 1, dp[i][j + dt[i-1][1]])

print(max(dp[n]))