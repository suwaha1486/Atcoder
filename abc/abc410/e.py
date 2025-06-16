n, h, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

dp = [-1] * (h + 1)
dp[h] = m

for i in range(n):
    next_dp = [-1] * (h + 1)
    ai, bi = a[i], b[i]

    for hp in range(h + 1):
        mp = dp[hp]
        if mp < 0:
            continue

        # use hp
        if hp >= ai:
            next_dp[hp - ai] = max(next_dp[hp - ai], mp)

        # use mp
        if mp >= bi:
            next_dp[hp] = max(next_dp[hp], mp - bi)

    if all(v < 0 for v in next_dp):
        print(i)
        break

    dp = next_dp
else:
    print(n)        