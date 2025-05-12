n, k = map(int, input().split())

a = [1] * (n+1)
s = k
for i in range(k, n+1):
    a[i] = s
    s += a[i]
    s -= a[i-k]
    s %= 1000000000

print(a[n])