N, K = map(int, input().split())

ans = 0

for num in range(1, N + 1):
    sum_num = 0
    for j in str(num):
        sum_num += int(j)
    if sum_num == K:
        ans += 1

print(ans)