from collections import defaultdict

N, M = map(int, input().split())
color_dict = defaultdict(int)

DAB = []

for i in range(N):
    a, d, b = map(int, input().split())
    color_dict[a] += 1
    DAB.append((d, a, b))

DAB.sort(key=lambda x: x[0])

color_set_num = len(color_dict.keys())

t = 1
i = 0
while t < M + 1:
    while i < N and DAB[i][0] <= t:
        d, a, b = DAB[i]
        color_dict[a] -= 1
        if color_dict[a] == 0:
            color_set_num -= 1
        color_dict[b] += 1
        if color_dict[b] == 1:
            color_set_num += 1
        i += 1
        
    print(color_set_num)
    t += 1
