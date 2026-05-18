S = input()
N = len(S)

ans_cnt = 0

for i in range(N):
    if S[i] == 'C':
        ans_cnt += min(i + 1, N - i)

print(ans_cnt)