N, Q = map(int, input().split())
P = list(map(int, input().split()))

tmp = [0] * N
for i, p in enumerate(P):
    tmp[p - 1] = i + 1

A = [tmp, P]

row = 1

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        y = query[2] - 1

        tmp_x = A[row][x]
        tmp_y = A[row][y]

        A[row][x] = tmp_y
        A[row][y] = tmp_x

        A[row ^ 1][tmp_x - 1] = y + 1
        A[row ^ 1][tmp_y - 1] = x + 1
    
    elif query[0] == 2:
        row ^= 1

print(*A[row])
