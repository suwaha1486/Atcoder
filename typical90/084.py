# ★3
n = int(input())
s = input()

first_o = [n] * n
first_x = [n] * n

last_o = n
last_x = n
for i in range(n-1, -1, -1):
    if s[i] == 'o':
        last_o = i
    else:
        last_x = i
    first_o[i] = last_o
    first_x[i] = last_x

ans = 0
for i in range(n):
    min_len = max(first_o[i], first_x[i])
    if min_len < n:
        ans += n - min_len

print(ans)
