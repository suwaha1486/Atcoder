# ★3
h, w = map(int, input().split())
a = []
b = []
for _ in range(h):
    a.append(list(map(int, input().split())))
for _ in range(h):
    b.append(list(map(int, input().split())))

diff = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        diff[i][j] = a[i][j] - b[i][j]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        if diff[i][j] != 0:
            change_num = 0 - diff[i][j]
            diff[i][j] = 0
            diff[i+1][j] += change_num
            diff[i][j+1] += change_num
            diff[i+1][j+1] += change_num
            ans += abs(change_num)

for i in range(h):
    for j in range(w):
        if diff[i][j] != 0:
            print('No')
            exit()

print('Yes')
print(ans)
