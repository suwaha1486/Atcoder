N = int(input())
X = list(map(int, input().split()))

for i in range(N):
    if i == 0 or i == N - 1:
        print((X[N - 1] - X[0]) // 2)
    else:
        left_time = (X[i] - X[i - 1]) // 2 + max((X[i - 1] - X[0]) // 2,  (X[N - 1] - X[i]) // 2)
        right_time = (X[i + 1] - X[i]) // 2 + max((X[i] - X[0]) // 2, (X[N - 1] - X[i + 1]) // 2)
        print(min(left_time, right_time))
