t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    dp = [0] * (2 ** n)
    for i in range(len(s)):
        if s[i] == '1':
            dp[i + 1] = -1

    dp[0] = 1
    
    for i in range(2 ** n):
        if dp[i] != 1:
            continue
        for j in range(n):
            if not (i >> j & 1):
                idx = i | (1 << j)
                if dp[idx] != -1:
                    dp[idx] = 1
    
    if dp[2 ** n - 1] == 1:
        print("Yes")
    else:
        print("No")
        