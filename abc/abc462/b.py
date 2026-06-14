N = int(input())

ans_list = [list() for _ in range(N)]

for i in range(N):
    ka = list(map(int, input().split()))
    K = ka[0]
    A = ka[1:]
    for j in range(K):
        ans_list[A[j] - 1].append(i + 1)

for i in range(N):
    x = len(ans_list[i])
    b = sorted(ans_list[i])
    print(x, *b)