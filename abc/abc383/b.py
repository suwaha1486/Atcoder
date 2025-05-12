from itertools import combinations

h, w, d = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

floor_pos = []
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            floor_pos.append((i, j))

ans = 0
for pos1, pos2 in combinations(floor_pos, 2):
    t = [[0] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                dist1 = abs(i - pos1[0]) + abs(j - pos1[1])
                dist2 = abs(i - pos2[0]) + abs(j - pos2[1])
                
                if dist1 <= d or dist2 <= d:
                    t[i][j] = 1

    cnt = sum(map(sum, t))
    ans = max(ans, cnt)

print(ans)