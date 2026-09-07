N, Q = map(int, input().split())
P = list(map(int, input().split()))

num_idx = [0] * N
for i in range(N):
    num_idx[P[i] - 1] = i

latest_idx = N

for i in range(Q):
    a = int(input()) - 1
    num_idx[a] = latest_idx
    latest_idx += 1

ans = sorted(range(1, N + 1), key=lambda v: num_idx[v - 1])
print(*ans)