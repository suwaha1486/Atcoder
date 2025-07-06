t = int(input())

for _ in range(t):
    # 等比数列かどうかを判定
    n = int(input())
    a = list(map(int, input().split()))

    # 公比が負になる場合 -> 正負が交互になる
    # 絶対値でsort
    a.sort(key=abs)

    # 公比rを割り算で求めると誤差が出るので，ai ** 2 == ai+1 * ai-1 で等比数列かを判別する

    # r == 1 or -1 の場合
    if abs(a[0]) == abs(a[1]):
        positive = 0
        negative = 0
        tmp = abs(a[0])
        for i in range(n):
            if a[i] > 0:
                positive += 1
            else:
                negative += 1
            if abs(a[i]) != tmp:
                print("No")
                break
        else:
            # 全部正 or 全部負
            if positive == n or negative == n:
                print("Yes")
            # 正負が交互になる
            elif abs(positive - negative) <= 1:
                print("Yes")
            else:
                print("No")

    # abs(r) != 1 の場合
    else:
        for i in range(1, n - 1):
            if a[i + 1] * a[i - 1] != a[i] ** 2:
                print("No")
                break
        else:
            print("Yes")
