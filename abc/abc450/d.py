N, K = map(int, input().split())

A = list(map(int, input().split()))

for i in range(N):
    A[i] %= K

A.sort()

max_gap = A[0] + K - A[N - 1]

for i in range(N - 1):
    max_gap = max(max_gap, A[i + 1] - A[i])

print(K - max_gap)
