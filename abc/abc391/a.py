d = input()

ans = ''
for i in range(len(d)):
    if d[i] == 'N':
        ans += 'S'
    elif d[i] == 'S':
        ans += 'N'
    elif d[i] == 'E':
        ans += 'W'
    elif d[i] == 'W':
        ans += 'E'

print(ans)