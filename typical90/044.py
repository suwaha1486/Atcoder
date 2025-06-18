# ★3
n, q = map(int, input().split())
a = list(map(int, input().split()))

diff = 0
for i in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        x = (x - diff - 1) % n
        y = (y - diff - 1) % n
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        diff += 1
    elif t == 3:
        x = (x - diff - 1) % n
        print(a[x])
