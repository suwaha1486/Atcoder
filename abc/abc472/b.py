N = int(input())
L = list(map(int, input().split()))

for i in range(1, N):
    L[i] = L[i-1] + L[i]

L_len = L[-1]

ans_len = L_len
for i in range(N):
    ans_len = min(ans_len, abs(L_len - 2 * L[i]))

print(ans_len)