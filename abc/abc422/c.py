t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    # 2種類のボトルネックを満たす最大の整数
    ans = min(min(a, c), (a + b + c) // 3)
    print(ans)