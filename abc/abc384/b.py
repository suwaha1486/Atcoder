n, r = map(int, input().split())

for i in range(n):
    d, a = map(int, input().split())
    if d == 1 and 1600 <= r < 2800:
        r += a
    elif d == 2 and 1200 <= r < 2400:
        r += a

print(r)