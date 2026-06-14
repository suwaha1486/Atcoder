N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY.sort(key=lambda x: x[0])

Y_min = XY[0][1]
ans = 1

for i in range(1, N):
    if XY[i][1] < Y_min:
        ans += 1
        Y_min = XY[i][1]

print(ans)