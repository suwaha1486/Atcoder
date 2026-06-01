N, M = map(int, input().split())
cnt = 0
while M > 0:
    cnt += 1
    M = N % M

print(cnt)
