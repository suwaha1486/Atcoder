# MA Answer

k = int(input())
mod = 10**9 + 7

# 9の倍数条件 -> 各位の数字の和が9の倍数

if k % 9 != 0:
    print(0)
    exit()

dp = [0] * (k+1)
dp[0] = 1

for i in range(1, k+1):
    for j in range(1, 10):
        if i - j >= 0:
            dp[i] += dp[i-j]
            dp[i] %= mod

print(dp[k])