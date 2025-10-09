n, r = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0

open_door_flg = False
for i in range(r):
    if l[i] == 0:
        open_door_flg = True
        cnt += 1
    if l[i] == 1 and open_door_flg:
        cnt += 2

open_door_flg = False
for i in range(n-1, r-1, -1):
    if l[i] == 0:
        open_door_flg = True
        cnt += 1
    if l[i] == 1 and open_door_flg:
        cnt += 2

print(cnt)