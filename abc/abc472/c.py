N, M, K = map(int, input().split())
A = list(map(int, input().split()))

eat_flg = [False] * (N + 1)

calory_sum = 0

for i in range(1, N + 1):
    outrange_index = max(i - M, 0)
    if eat_flg[outrange_index]:
        calory_sum -= A[outrange_index - 1]

    if calory_sum + A[i - 1] <= K:
        calory_sum += A[i - 1]
        eat_flg[i] = True
        print('Yes')
    else:
        print('No')
