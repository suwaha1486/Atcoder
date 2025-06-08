n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

wall = [0] * (n+2)
for i in range(m):
    wall[lr[i][0]] += 1
    wall[lr[i][1] + 1] -= 1

for i in range(1, n+1):
    wall[i] += wall[i-1]

print(min(wall[1:n+1]))