# AI helped me to write this code

from collections import defaultdict
from bisect import bisect_left, bisect_right

N, M, sx, sy = map(int, input().split())

# coordinate -> sorted list of (other_axis_coord, id)
x_map = defaultdict(list)  # x = const (vertical line)
y_map = defaultdict(list)  # y = const (horizontal line)

for idx in range(N):
    xi, yi = map(int, input().split())
    x_map[xi].append((yi, idx))
    y_map[yi].append((xi, idx))

# sort lists for binary search
for lst in x_map.values():
    lst.sort(key=lambda t: t[0])
for lst in y_map.values():
    lst.sort(key=lambda t: t[0])

visited = [False] * N
ans = 0

cur_x, cur_y = sx, sy

NEG_INF = -10 ** 20
POS_INF = 10 ** 20

for _ in range(M):
    d, c_str = input().split()
    c = int(c_str)

    if d == 'U':
        new_y = cur_y + c
        low, high = (cur_y, new_y) if cur_y <= new_y else (new_y, cur_y)
        lst = x_map.get(cur_x, [])
        l = bisect_left(lst, (low, NEG_INF))
        r = bisect_right(lst, (high, POS_INF))
        for _, hid in lst[l:r]:
            if not visited[hid]:
                visited[hid] = True
                ans += 1
        cur_y = new_y

    elif d == 'D':
        new_y = cur_y - c
        low, high = (new_y, cur_y) if new_y <= cur_y else (cur_y, new_y)
        lst = x_map.get(cur_x, [])
        l = bisect_left(lst, (low, NEG_INF))
        r = bisect_right(lst, (high, POS_INF))
        for _, hid in lst[l:r]:
            if not visited[hid]:
                visited[hid] = True
                ans += 1
        cur_y = new_y

    elif d == 'L':
        new_x = cur_x - c
        low, high = (new_x, cur_x) if new_x <= cur_x else (cur_x, new_x)
        lst = y_map.get(cur_y, [])
        l = bisect_left(lst, (low, NEG_INF))
        r = bisect_right(lst, (high, POS_INF))
        for _, hid in lst[l:r]:
            if not visited[hid]:
                visited[hid] = True
                ans += 1
        cur_x = new_x

    elif d == 'R':
        new_x = cur_x + c
        low, high = (cur_x, new_x) if cur_x <= new_x else (new_x, cur_x)
        lst = y_map.get(cur_y, [])
        l = bisect_left(lst, (low, NEG_INF))
        r = bisect_right(lst, (high, POS_INF))
        for _, hid in lst[l:r]:
            if not visited[hid]:
                visited[hid] = True
                ans += 1
        cur_x = new_x

print(cur_x, cur_y, ans)
