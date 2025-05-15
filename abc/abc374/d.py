from math import sqrt
from itertools import permutations

n, s_speed, t_speed = map(int, input().split())
ab = [] 
cd = []
line_len = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    ab.append((a, b))
    cd.append((c, d))
    line_len += sqrt((a - c)**2 + (b - d)**2)

def dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

move_len = 10**18
for order in permutations(range(n)):
    for i in range(2 ** n):
        tmp_move_len = 0
        pre_pos = (0, 0)
        for j in range(n):
            if i & (1 << j):
                tmp_move_len += dist(pre_pos, ab[order[j]])
                pre_pos = cd[order[j]]
            else:
                tmp_move_len += dist(pre_pos, cd[order[j]])
                pre_pos = ab[order[j]]
        move_len = min(move_len, tmp_move_len)

ans = move_len / s_speed + line_len / t_speed
print(ans)