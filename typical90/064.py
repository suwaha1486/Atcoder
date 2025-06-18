# ★3
n, q = map(int, input().split())
a = list(map(int, input().split()))

diff = []
for i in range(n-1):
    diff.append(a[i+1] - a[i])
diff.append(0)

ans = sum(abs(diff[i]) for i in range(n-1))

for i in range(q):
    l, r, v = map(int, input().split())
    l, r = l-1, r-1

    before = abs(diff[l-1]) + abs(diff[r])

    if l != 0:
        diff[l-1] += v
    if r != n-1:
        diff[r] -= v

    after = abs(diff[l-1]) + abs(diff[r])
    ans += after - before
    
    print(ans)
