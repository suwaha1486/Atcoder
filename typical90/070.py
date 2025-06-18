# ★4
n = int(input())
x = [None] * n
y = [None] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

x.sort()
y.sort()

if n % 2 == 0:
    x_mid = (x[n//2-1] + x[n//2]) / 2
    y_mid = (y[n//2-1] + y[n//2]) / 2
else:
    x_mid = x[n//2]
    y_mid = y[n//2]

ans = 0
for i in range(n):
    ans += abs(x[i] - x_mid) + abs(y[i] - y_mid)

print(int(ans))
