t = int(input())

for _ in range(t):
    # 等比数列かどうかを判定
    n = int(input())
    a = list(map(int, input().split()))
    # 公比が負になる場合 -> 正負が交互になる
    # 絶対値でsort
    a_abs = sorted(a, key=abs)
    
    r = a_abs[1] / a_abs[0]
    for i in range(1, n - 1):
        if a_abs[i + 1] / a_abs[i] != r:
            print("No")
            break
    else:
        print("Yes")

