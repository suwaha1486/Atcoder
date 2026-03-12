N, Q = map(int, input().split())
A = list([int(x), i + 1] for i, x in enumerate(input().split()))
A.sort()

for i in range(Q):
    K = int(input())
    B = set(map(int, input().split()))
    for i in range(N):
        if A[i][1] not in B:
            print(A[i][0])
            break
