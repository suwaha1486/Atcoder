n, m = map(int, input().split())
s = list(input())
t = list(input())

change_pos = [0] * (n + 1)

for i in range(m):
    l, r = map(int, input().split())
    change_pos[l-1] += 1
    change_pos[r] -= 1

for i in range(n):
    change_pos[i+1] += change_pos[i]
    if change_pos[i] % 2 == 0:
        t[i] = s[i]

print(*t, sep='')