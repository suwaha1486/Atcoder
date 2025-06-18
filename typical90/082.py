# ★3
l, r = input().split()
mod = 10**9 + 7

l_len = len(l)
r_len = len(r)
l = int(l)
r = int(r)

if l_len == r_len:
    ans = ((r * (r + 1) // 2) % mod - (l * (l - 1) // 2) % mod) * l_len % mod
    print(ans)
    exit()

ans = 0
for i in range(l_len, r_len + 1):
    if i == l_len:
        max_num = 10 ** i - 1
        sum_max = (max_num * (max_num + 1) // 2) % mod
        sum_min = (l * (l - 1) // 2) % mod
        ans += (sum_max - sum_min) * i % mod
    elif i == r_len:
        min_num = 10 ** (i - 1)
        sum_max = (r * (r + 1) // 2) % mod
        sum_min = (min_num * (min_num - 1) // 2) % mod
        ans += (sum_max - sum_min) * i % mod
    else:
        max_num = 10 ** i - 1
        min_num = 10 ** (i - 1)
        sum_max = (max_num * (max_num + 1) // 2) % mod
        sum_min = (min_num * (min_num - 1) // 2) % mod
        ans += (sum_max - sum_min) * i % mod

print(ans % mod)
