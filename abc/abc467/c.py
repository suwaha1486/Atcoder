N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10 ** 18
dp = [[INF] * 2 for _ in range(N)]

# dp[i][v]: A[i]をvにするための最小コスト

if A[0] == 0:
    dp[0][0] = 0
else:
    dp[0][0] = 1

if A[0] == 1:
    dp[0][1] = 0
else:
    dp[0][1] = 1
    

for i in range(1, N):
    for cur_val in (0, 1):
        for prev_val in (0, 1):
            if (prev_val + cur_val) % 2 != B[i - 1]:
                continue

            if A[i] == cur_val:
                add_cost = 0
            else:
                add_cost = 1

            dp[i][cur_val] = min(dp[i - 1][prev_val] + add_cost, dp[i][cur_val])

print(min(dp[N - 1][0], dp[N - 1][1]))