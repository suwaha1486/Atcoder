H, W, Q = map(int, input().split())

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        r = query[1]
        print(r * W)
        H -= r

    elif query[0] == 2:
        c = query[1]
        print(c * H)
        W -= c
