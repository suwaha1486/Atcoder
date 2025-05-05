n = int(input())

num = dict()

for i in range(n):
    a = int(input())
    if a in num:
        num[a] += 1
    else:
        num[a] = 1

ans = 0
for cnt in num.values():
    if cnt >= 2:
        ans += cnt * (cnt - 1) // 2

print(ans)