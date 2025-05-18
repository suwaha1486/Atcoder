n = int(input())
coin = list(map(int, input().split()))

coin.sort(reverse=True)

ans = 10000
for i in range(n // coin[0], -1, -1):
    for j in range((n - i * coin[0]) // coin[1], -1, -1):
        if (n - i * coin[0] - j * coin[1]) % coin[2] == 0:
            ans = min(ans, i + j + (n - i * coin[0] - j * coin[1]) // coin[2])

print(ans)
