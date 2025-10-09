n, m = map(int, input().split())

vote = [[None] * n for _ in range(m)]

for i in range(n):
    s = input()
    for j in range(m):
        vote[j][i] = int(s[j])

point = [0] * n

for i in range(m):
    result = sum(vote[i])

    if result == n or result == 0:
        for j in range(n):
            point[j] += 1
    
    elif result < n // 2 + 1:
        for j in range(n):
            if vote[i][j] == 1:
                point[j] += 1
    
    elif result > n // 2:
        for j in range(n):
            if vote[i][j] == 0:
                point[j] += 1
    
max_point = max(point)
max_point_index = []

for i in range(n):
    if point[i] == max_point:
        max_point_index.append(i + 1)

print(*max_point_index, sep=' ')