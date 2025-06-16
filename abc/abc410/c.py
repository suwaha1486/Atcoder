n, q = map(int, input().split())

a = [i + 1 for i in range(n)]
diff = 0

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1], query[2]
        idx = (diff + p - 1) % n
        a[idx] = x
    elif query[0] == 2:
        p = query[1]
        idx = (diff + p - 1) % n
        print(a[idx])
    elif query[0] == 3:
        k = query[1]
        diff += k
