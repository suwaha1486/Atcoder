x, y = map(int, input().split())

cnt = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= x or abs(i - j) >= y:
            cnt += 1

print(cnt / 36)
