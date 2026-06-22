N = int(input())
HK = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 2, -1, -1):
    HK[i][0] = max(HK[i][0], HK[i + 1][0])

Q = int(input())
T = list(enumerate(map(int, input().split())))
T.sort(key=lambda x: x[1])

ans = [None] * Q
hk_pos = 0
for t_idx, t in T:
    while hk_pos < N and HK[hk_pos][1] <= t:
        hk_pos += 1

    ans[t_idx] = (HK[hk_pos][0])

for a in ans:
    print(a)