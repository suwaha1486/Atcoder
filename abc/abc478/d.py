N, Q = map(int, input().split())

X_list = [[] for _ in range(Q + 1)]

for _ in range(Q):
    L, R, X = map(int, input().split())
    X_list[X].append((L, R))

diff = [0] * (N + 2)

for x in range(1, Q + 1):
    if len(X_list[x]) == 0:
        continue

    X_list[x].sort()
    cur_L, cur_R = X_list[x][0]

    for L, R in X_list[x][1:]:
        if L > cur_R + 1:
            diff[cur_L] += 1
            diff[cur_R + 1] -= 1
            cur_L, cur_R = L, R
        else:
            cur_R = max(cur_R, R)

    diff[cur_L] += 1
    diff[cur_R + 1] -= 1

for i in range(1, N + 2):
    diff[i] += diff[i - 1]

print(*diff[1:N + 1])