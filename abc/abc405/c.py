n = int(input())
a = list(map(int, input().split()))

cumsum = [0] * (n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + a[i]

ans = 0
for i in range(n):
    ans += a[i] * (cumsum[n] - cumsum[i+1])

print(ans)