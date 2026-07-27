S = input()

n = len(S)

ans = 0

for i in range(n):
    wrong_cnt = 0
    for j in range(min(i, n - i - 1) + 1):
        if S[i - j] == S[i + j]:
            ans += 1
        elif wrong_cnt == 0:
            ans += 1
            wrong_cnt += 1
        else:
            break

for i in range(n - 1):
    wrong_cnt = 0
    for j in range(min(i + 1, n - 1 - i)):
        if S[i - j] == S[i + j + 1]:
            ans += 1
        elif wrong_cnt == 0:
            ans += 1
            wrong_cnt = 1
        else:
            break

print(ans)