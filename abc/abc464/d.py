T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    # S: {s, r}で構成される文字列
    # 任意の位置の文字を入れ替えられる（s -> r or r -> s）が，嬉しさがX_iだけ減少
    # i = r and i+1 = s の場合，嬉しさがY_iだけ増加
    # 嬉しさ最大を目指す

    # dp[i][j]: i日目がs(j=0) or r(j=1)の時の，i日目までの嬉しさの最大値
    # 遷移の仕方

    # i日目をsにする場合
    # - i-1日目がs → ボーナスなし
    # - i-1日目がr → Y[i-1]ボーナス加算
    # + 元の天気と違う場合は -X[i] のコスト

    # i日目をrにする場合
    # - ボーナスなし（ボーナスはi+1日目の遷移で加算される）
    # + 元の天気と違う場合は -X[i] のコスト

    # 基底: dp[0][0], dp[0][1] はそれぞれ元の天気との差分だけコスト
    # 答え: max(dp[N-1][0], dp[N-1][1])

    dp = [[0] * 2 for _ in range(N)]
    if S[0] == 'S':
        dp[0][0] = 0
    else:
        dp[0][0] = -X[0]

    if S[0] == 'R':
        dp[0][1] = 0
    else:
        dp[0][1] = -X[0]

    for i in range(1, N):
        if S[i] == 'S':
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + Y[i - 1])
        else:
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + Y[i - 1]) - X[i]

        if S[i] == 'R':
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) - X[i]
    
    print(max(dp[N - 1][0], dp[N - 1][1]))