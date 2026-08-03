N = int(input())
S = input()

cumsum = [0] * (N + 1)

for i in range(N):
    if S[i] == 'o':
        cumsum[i + 1] = cumsum[i] + 1
    else:
        cumsum[i + 1] = cumsum[i]

cumsum_idx = 1

for k in range(1, N + 1):
    while cumsum_idx <= N and cumsum_idx - cumsum[cumsum_idx] < k:
        cumsum_idx += 1

    if cumsum_idx <= N:
        print(cumsum_idx)
    else:
        print(N)