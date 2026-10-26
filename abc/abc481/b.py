N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
if A[0] == K:
    cnt += 1

pre_pos = A[0]

for i in range(1, N):
    if A[i] == K:
        cnt += 1
    elif (A[i] - K) * (pre_pos - K) < 0:
        cnt += 1
    pre_pos = A[i]

print(cnt)