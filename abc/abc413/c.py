q = int(input())

a = []
idx = 0

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        x = query[2]
        a.append([c, x])

    elif query[0] == 2:
        k = query[1]
        cnt = 0
        sum_x = 0
        while cnt < k:
            c = a[idx][0]
            x = a[idx][1]
            # 同じ整数を全て削除できる場合
            if cnt + c <= k:
                cnt += c
                idx += 1
                sum_x += x * c
            # 同じ整数を全て削除できない場合
            else:
                sum_x += x * (k - cnt)
                a[idx][0] -= k - cnt
                break
        print(sum_x)

