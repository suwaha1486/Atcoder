S = input()
M = 998244353

L = 1
ans = 0
for i in range(1, len(S)):
    if S[i - 1] != S[i]:
        L += 1
    else:
        ans = (ans + L * (L + 1) // 2) % M
        L = 1
ans = (ans + L * (L + 1) // 2) % M
print(ans % M)