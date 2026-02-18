N = int(input())
S = []
m = 0
for i in range(N):
    S.append(input())
    m = max(m, len(S[i]))

for i in range(N):
    S[i] = '.' * ((m - len(S[i])) // 2) + S[i] + '.' * ((m - len(S[i])) // 2)
    print(S[i])
