n, q = map(int, input().split())
a = list(map(int, input().split()))

masu = [0] * (n+2)
cnt = 0
for i in range(q):
    # 対象マスが白の場合
    if masu[a[i]] == 0:
        masu[a[i]] = 1
        # 両隣が黒の場合
        if masu[a[i]-1] == 1 and masu[a[i]+1] == 1:
            cnt -= 1
        # 両隣が白の場合
        elif masu[a[i]-1] == 0 and masu[a[i]+1] == 0:
            cnt += 1
        # 片方が黒の場合
        else:
            cnt += 0
    
    # 対象マスが黒の場合
    else:
        masu[a[i]] = 0
        # 両隣が黒の場合
        if masu[a[i]-1] == 1 and masu[a[i]+1] == 1:
            cnt += 1
        # 両隣が白の場合
        elif masu[a[i]-1] == 0 and masu[a[i]+1] == 0:
            cnt -= 1
        # 片方が黒の場合
        else:
            cnt += 0
    print(cnt)
