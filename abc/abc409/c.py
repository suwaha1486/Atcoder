n, l = map(int, input().split())
d = list(map(int, input().split()))
d.insert(0, 0)
position = [0] * l

if l % 3 != 0:
    print(0)
    exit()

position[0] = 1
for i in range(1, n):
    d[i] += d[i - 1]
    d[i] %= l
    position[d[i]] += 1

ans = 0
side = l // 3   
for i in range(side):
    ans += position[i] * position[i+side] * position[i+side*2]

print(ans)
