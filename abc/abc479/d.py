N, Q = map(int, input().split())
L = list(map(int, input().split()))
R = list(map(int, input().split()))

R_min = [0] * (N - 1)
R_min[0] = R[0]

for i in range(1, N - 1):
    R_min[i] = min(R_min[i - 1], R[i])

L_min = [0] * (N - 1)
L_min[-1] = L[-1]

for i in range(N - 3, -1, -1):
    L_min[i] = min(L_min[i + 1], L[i])

for _ in range(Q):
    s, t = map(int, input().split())

    if s < t:
        ans = R[s - 1]
        if s > 1:
            ans = min(ans, L[s - 2] + R_min[s - 2])

    else:
        ans = L[s - 2]
        if s < N:
            ans = min(ans, R[s - 1] + L_min[s - 1])

    print(ans)