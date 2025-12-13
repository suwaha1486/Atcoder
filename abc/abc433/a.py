x, y, z = map(int, input().split())

a = x - y * z

if a >= 0 and a % (z - 1) == 0:
    print('Yes')
else:
    print('No')