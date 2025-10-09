n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 最初にsum(min(ai, bi))を計算

sum_min = 0
for i in range(n):
    sum_min += min(a[i], b[i])

for i in range(q):
    c, x, v = input().split()
    x = int(x)
    v = int(v)

    if c == 'A':
        sum_min -= min(a[x - 1], b[x - 1])
        a[x - 1] = v
        sum_min += min(a[x - 1], b[x - 1])
    
    elif c == 'B':
        sum_min -= min(a[x - 1], b[x - 1])
        b[x - 1] = v
        sum_min += min(a[x - 1], b[x - 1])
    
    print(sum_min)

