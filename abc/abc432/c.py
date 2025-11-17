n, x, y = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

b = [ai * x for ai in a]

# w_total = A_i * x + cnt_y_i * (y - x)
# cnt_y_i を調整することで任意のi に対して w_total が同じになるようにする

# 1. A_i * x が y - x の余りが全て等しい
# 2. 0 <= cnt_y_i <= A_iより，min_A_i に関して A_i * (y - x) >= max_A_i * x
# 3. w_total = b[0] + d * a[0] とし，cnt_y_i = (w_total - b[i]) // d とする

d = y - x
d_mod = b[0] % d

for i in range(n):
    if b[i] % d != d_mod:
        print('-1')
        exit()

if b[0] + a[0] * d < b[n-1]:
    print('-1')
    exit()

w_total = b[0] + d * a[0]

ans = a[0]

for i in range(1, n):
    ans += (w_total - b[i]) // d

print(ans)