n = int(input())
a = list(map(int, input().split()))

'''
方針
理想状態：a[i] = a[i] + i - (n - i - 1)
本来の増加幅 - 自分がもらう段階で自分より前の成人で０になっている人数
減少により途中で０未満になる人→０になるタイミングを記録
'''
cnt0 = 0
when0 = [0] * n
for i in range(n):
    cnt0 += when0[i]

    a[i] = a[i] + (i - cnt0)

    if a[i] - (n - i - 1) < 0:
        when0[i + a[i] + 1] += 1
        a[i] = 0
    else:
        a[i] -= n - i - 1

print(*a)