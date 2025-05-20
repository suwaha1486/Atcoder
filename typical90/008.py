n = int(input())
s = input()
mod = 10**9 + 7

dp = [[0] * 8 for _ in range(n + 1)]

target = "0atcoder"

for i in range(1, n + 1):
    for j in range(8):
        dp[i][j] = dp[i - 1][j]
        if s[i - 1] == target[j]:
            if j == 1:
                dp[i][j] = (dp[i - 1][j] + 1) % mod
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod

print(dp[n][7])
