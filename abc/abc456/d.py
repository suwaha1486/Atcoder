S = input()
MOD = 998244353

# dp[i]: 最後の文字がiの文字列の個数
dp = [0] * 3

for i in range(len(S)):
    if S[i] == 'a':
        dp[0] += (dp[1] + dp[2] + 1) % MOD
    elif S[i] == 'b':
        dp[1] += (dp[0] + dp[2] + 1) % MOD
    elif S[i] == 'c':
        dp[2] += (dp[0] + dp[1] + 1) % MOD

print(sum(dp) % MOD)