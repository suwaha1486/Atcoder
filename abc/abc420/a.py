x, y = map(int, input().split())

z = (x + y) % 12

if z == 0:
    print(12)
else:
    print(z)
    