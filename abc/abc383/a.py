n = int(input())

pre_t = 0
water = 0
for i in range(n):
    t, v = map(int, input().split())
    if i > 0:
        water = max(0, water - (t - pre_t))
    water += v
    pre_t = t

print(water)