N, Q = map(int, input().split())
A = list(map(int, input().split()))

cum_sum = [0] * (N+1)
for i in range(N):
    cum_sum[i+1] = cum_sum[i] + A[i]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        cum_sum[x + 1] = cum_sum[x] + A[x + 1]
        A[x], A[x + 1] = A[x + 1], A[x]
        
    elif query[0] == 2:
        l = query[1] - 1
        r = query[2]
        print(cum_sum[r] - cum_sum[l])
