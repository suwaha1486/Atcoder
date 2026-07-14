N, M = map(int, input().split())
color_ball_max = [-1] * (M)

for _ in range(N):
    C, S = map(int, input().split())
    color_ball_max[C - 1] = max(color_ball_max[C - 1], S)

print(*color_ball_max)