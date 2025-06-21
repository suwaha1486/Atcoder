n, m = map(int, input().split())
xyc = []

for i in range(m):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    xyc.append([x, y, c])

xyc.sort()

white_min_x = n+1
white_min_y = n+1

for x, y, c in xyc:
    if c == 'W':
        white_min_x = min(white_min_x, x)
        white_min_y = min(white_min_y, y)
    else:
        if x >= white_min_x and y >= white_min_y:
            print('No')
            exit()
print('Yes')
