def levenshtein_distance(s, t):
    '''
    編集距離
    O(mn) -> TLE
    '''
    m = len(s)
    n = len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m][n]

k = int(input())
s = list(input())
t = list(input())

# insert
if len(s) + k == len(t):
    s_idx = 0
    t_idx = 0
    diff_cnt = 0
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] != t[t_idx]:
            t_idx += 1
            diff_cnt += 1
        else:
            s_idx += 1
            t_idx += 1
    if diff_cnt <= k:
        print('Yes')
    else:
        print('No')

# delete
elif len(s) - k== len(t):
    s_idx = 0
    t_idx = 0
    diff_cnt = 0
    while s_idx < len(s) and t_idx < len(t):
        if s[s_idx] != t[t_idx]:
            s_idx += 1
            diff_cnt += 1
        else:
            s_idx += 1
            t_idx += 1
    if diff_cnt <= k:
        print('Yes')
    else:
        print('No')

# replace
elif len(s) == len(t):
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    if cnt <= k:
        print('Yes')
    else:
        print('No')

else:
    print('No')