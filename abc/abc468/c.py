from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i in range(N):
    P[i] = P[i] - 1
    Q[i] = Q[i] - 1
P_num = int("".join(map(str, P)))
Q_num = int("".join(map(str, Q)))

ans = 0
# (1, 2, ..., N) の順列を全探索
for perm in permutations(range(N)):
    perm_num = int("".join(map(str, perm)))
    if P_num < perm_num < Q_num:
        ans += 1

print(ans)