n = int(input())

s = []
t = []

for i in range(n):
    s.append(list(input()))

for i in range(n):
    t.append(list(input()))

sousa = []
for i in range(4):
    sousa.append(i)

    if i > 0:
        s = [list(row) for row in zip(*s[::-1])]

    for j in range(n):
        for k in range(n):
            if s[j][k] != t[j][k]:
                sousa[i] += 1

print(min(sousa))