n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n-2, -1, -1):
    dp[a[i]] += dp[i + 2] + 1

print(*dp[1:], sep=' ')