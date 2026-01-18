N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

drink_sum = 0

for i in range(K):
    drink_sum += A[i]

if drink_sum < X:
    print(-1)
    exit()

removed = 0
for i in range(K):
    if drink_sum - A[i] >= X:
        drink_sum -= A[i]
        removed += 1
    else:
        break

print(N - removed)
