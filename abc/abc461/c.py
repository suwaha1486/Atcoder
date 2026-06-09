N, K, M = map(int, input().split())
VC = []

for _ in range(N):
    C, V = map(int, input().split())
    VC.append((V, C))

VC.sort(reverse=True)

surplus_num = K - M
sum_v = 0
color_set = set()
cnt = 0

for i in range(N):
    if cnt >= K:
        break

    if VC[i][1] in color_set and surplus_num > 0:
        surplus_num -= 1
        sum_v += VC[i][0]
        cnt += 1
    elif VC[i][1] not in color_set:
        color_set.add(VC[i][1])
        sum_v += VC[i][0]
        cnt += 1

print(sum_v)