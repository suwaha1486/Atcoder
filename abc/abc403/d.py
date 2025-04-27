from collections import Counter

n, d = map(int, input().split())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0

for x in sorted(cnt):
    if cnt[x] <= cnt[x + d]:
        ans += cnt[x]
        cnt[x] = 0
    else:
        ans += cnt[x + d]
        cnt[x + d] = 0

print(ans)