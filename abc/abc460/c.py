N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

A_pos = 0
cnt = 0

# B[i] <= A[j] * 2 となる組合せの最大個数を探す

for i in range(M):
    while A_pos < N and B[i] > A[A_pos] * 2:
        A_pos += 1
    if A_pos == N:
        break
    cnt += 1
    A_pos += 1

print(cnt)