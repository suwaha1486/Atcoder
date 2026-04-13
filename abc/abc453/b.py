T, X = map(int, input().split())
A = list(map(int, input().split()))

pre_score = A[0]

print(0, pre_score)

for i in range(1, T+1):
    if abs(A[i] - pre_score) >= X:
        print(i, A[i])
        pre_score = A[i]