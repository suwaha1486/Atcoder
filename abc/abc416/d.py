# A+B >= Mを満たすペアを最大個数にする
# ペアの個数をcntとすると，sum(A) + sum(B) - cnt * M
# A降順ソート，B昇順ソート
# Aに対して，足してMを超える最小のBを探す尺取り法

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort()

    cnt = 0
    idx = 0
    for i in range(n):
        while idx < n and a[i] + b[idx] < m:
            idx += 1
        if idx == n:
            break
        cnt += 1
        idx += 1

    print(sum(a) + sum(b) - cnt * m)
