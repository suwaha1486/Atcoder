n = int(input())

s = []

for i in range(n):
    tmp = input()
    s.append([len(tmp), tmp])

s.sort()

ans = ''
for i in range(n):
    ans += s[i][1]

print(ans)