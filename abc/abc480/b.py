N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

ans = [0] * N

for i in range(M):
    much_cnt = 0
    for j in range(N):
        t_len = len(T[i])
        if t_len != len(S[j]):
            continue
            
        diff = 0
        for k in range(t_len):
            if S[j][k] != T[i][k]:
                diff += 1
                if diff > 1:
                    break
        if diff == 0:
            much_cnt = 1
            ans_idx = j
            break
            ans_i
        if diff == 1:
            much_cnt += 1
            ans_idx = j

    if much_cnt == 1:
        ans[ans_idx] += 1

for i in range(N):
    print(ans[i])