n, m = map(int, input().split())
S = [list(input()) for _ in range(n)]
T = [list(input()) for _ in range(m)]

for a in range(n-m+1):
    for b in range(n-m+1):
        flg = True
        for i in range(m):
            for j in range(m):
                if S[a+i][b+j] != T[i][j]:
                    flg = False
                    break
            if not flg:
                break
        if flg:
            print(a + 1, b + 1)
            exit()