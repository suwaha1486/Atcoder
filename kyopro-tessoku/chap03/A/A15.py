n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = [a[i], i]

a.sort()

b = []
b.append((a[0][1], 1))

pos = 1
for i in range(1, n):
    if a[i][0] > a[i - 1][0]:
        pos += 1
    b.append((a[i][1], pos))

b.sort()
print(*[item[1] for item in b], sep=" ")