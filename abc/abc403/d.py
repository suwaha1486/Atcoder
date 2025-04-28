n, d = map(int, input().split())
a = list(map(int, input().split()))

a_max = 10 ** 6 + 1
cnt = [0] * a_max

for i in range(n):
    cnt[a[i]] += 1

ans = 0

if d == 0:
    for i in range(a_max):
        ans += max(cnt[i] - 1, 0)
    print(ans)
    exit()

for i in range(d):
    x = cnt[i::d]
    if not x:
        continue
    x = [0] + x
    dp = [0] * (len(x) + 1)
    for j in range(1, len(x)):
        dp[j + 1] = min(dp[j] + x[j], dp[j - 1] + x[j - 1])
    ans += dp[-1]

print(ans)