h, w, x, y = map(int, input().split())
s = [list(input()) for _ in range(h)]
action = input()

x -= 1
y -= 1
visit = 0

for t in action:
    if t == 'U':
        if s[x-1][y] == '#':
            continue
        if s[x-1][y] == '@':
            visit += 1
            s[x-1][y] = '.'
        x -= 1

    elif t == 'D':
        if s[x+1][y] == '#':
            continue
        if s[x+1][y] == '@':
            visit += 1
            s[x+1][y] = '.'
        x += 1
    elif t == 'L':
        if s[x][y-1] == '#':
            continue
        if s[x][y-1] == '@':
            visit += 1
            s[x][y-1] = '.'
        y -= 1
    elif t == 'R':
        if s[x][y+1] == '#':
            continue
        if s[x][y+1] == '@':
            visit += 1
            s[x][y+1] = '.'
        y += 1

print(x+1, y+1, visit)