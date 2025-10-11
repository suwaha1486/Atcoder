n = int(input())

ans = 0
for i in range(1, n+1):
    sign = 1 if i % 2 == 0 else -1
    ans += i * i * i * sign

print(ans)