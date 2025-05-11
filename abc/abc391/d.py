n, w = map(int, input().split())

x = []
y = []
x_block = [[] for _ in range(w + 1)]

for i in range(n):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)
    x_block[x_tmp].append((y_tmp, i+1))

cnt = [0] * n
disappear = [-1] * (n + 1)
for i in range(1, w + 1):
    x_block[i].sort()
    for j in range(len(x_block[i])):
        cnt[x_block[i][j][1]] = j
        disappear[j] = max(disappear[j], x_block[i][j][0])
    disappear[len(x_block[i])] = 10 ** 10

for i in range(n):
    disappear[i + 1] = max(disappear[i + 1], disappear[i] + 1)

q = int(input())
query = []
for _ in range(q):
    t, a = map(int, input().split())
    if t < disappear[cnt[a - 1]]:
        print('Yes')
    else:
        print('No')