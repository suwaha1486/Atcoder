N, W = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for bit in range(1 << N):
    a_sum = 0
    b_sum = 0

    for i in range(N):
        if bit & (1 << i):
            a_sum += AB[i][0]
            b_sum += AB[i][1]

    if b_sum <= W:
        ans = max(ans, a_sum)

print(ans)