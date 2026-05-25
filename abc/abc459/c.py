N, Q = map(int, input().split())

A = [0] * N
B = [0] * (Q + 1)
k = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        A[x] += 1
        h = A[x]
        B[h] += 1
        if B[h] == N:
            k = h
    else:
        y = query[1]
        t = k + y
        if t > Q:
            print(0)
        else:
            print(B[t])
