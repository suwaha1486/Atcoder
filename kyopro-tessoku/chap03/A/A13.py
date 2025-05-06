import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    idx = bisect.bisect_right(a, a[i] + k)
    ans += idx - i - 1

print(ans)

# 尺取り法でも可能