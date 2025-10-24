s, a, b, x = map(int, input().split())

cnt = x // (a + b)

time = cnt * (s * a) + s * (min(x - cnt * (a + b), a))

print(time)