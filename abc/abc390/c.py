h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

upper = h - 1
lower = 0
left = w - 1
right = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            upper = min(upper, i)
            lower = max(lower, i)
            left = min(left, j)
            right = max(right, j)

for i in range(upper, lower+1):
    for j in range(left, right+1):
        if s[i][j] == ".":
            print('No')
            exit()

print('Yes')