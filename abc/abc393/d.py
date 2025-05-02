n = int(input())
s = list(map(int, input()))

n1 = sum(s)

if n1 == 1:
    print(0)
    exit() 

one_pos = []

for i in range(n):
    if s[i] == 1:
        one_pos.append(i)

ans = 0
mid = n1 // 2

for i in range(n1):
    if i == mid:
        continue
    ans += abs(one_pos[mid] - one_pos[i]) - abs(mid - i)

print(ans)