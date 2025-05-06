import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a
for i in range(1, n + 1):
    a[i] += a[i - 1]

ans = 0
for i in range(n + 1):
    idx = bisect.bisect_right(a, a[i] + k)
    ans += idx - i - 1

print(ans)