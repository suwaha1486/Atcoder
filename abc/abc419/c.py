import math
n = int(input())

r_list = []
c_list = []
for i in range(n):
    r, c = map(int, input().split())
    r_list. append(r)
    c_list.append(c)

r_max = max(r_list)
r_min = min(r_list)
c_max = max(c_list)
c_min = min(c_list)

r_range = math.ceil((r_max - r_min) / 2)
c_range = math.ceil((c_max - c_min) / 2)

print(max(r_range, c_range))