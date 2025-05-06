def f(x):
    return x ** 3 + x

n = int(input())

error_cap = 0.001

l = 0.0
r = n

while l < r:                             
    m = (l + r) / 2
    if abs(f(m) - n) < error_cap:
        break
    if f(m) < n:
        l = m
    else:
        r = m

print(m)