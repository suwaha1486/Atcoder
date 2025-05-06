n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(max(a))
    exit()

dp = [[0] * (n + 1) for _ in range(2)]

dp[0][1] = a[0]
dp[1][2] = a[1]

for i in range(3, n + 1):
    dp[0][i] = max(dp[0][i - 2] + a[i - 1], dp[1][i - 3] + a[i - 1])
    dp[1][i] = max(dp[1][i - 2] + a[i - 1], dp[0][i - 3] + a[i - 1])

print(max(max(dp[0]), max(dp[1])))