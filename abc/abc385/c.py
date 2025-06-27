n = int(input())
h = list(map(int, input().split()))

ans = 1
for step_size in range(1, n):
    dp = [1] * n
    for j in range(n):
        if j - step_size >= 0:
            if h[j] == h[j - step_size]:
                dp[j] = dp[j - step_size] + 1
                ans = max(ans, dp[j])

print(ans)