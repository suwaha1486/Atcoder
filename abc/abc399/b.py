n = int(input())
p = list(map(int, input().split()))

p_idx = []

for i in range(n):
    p_idx.append((p[i], i))

p_idx.sort(reverse=True)

ranking = [[p_idx[0][1], 1]]
for i in range(1, n):
    if p_idx[i][0] == p_idx[i-1][0]:
        ranking.append([p_idx[i][1], ranking[-1][1]])
    else:
        ranking.append([p_idx[i][1], i+1])

ranking.sort()

for i in range(n):
    print(ranking[i][1])