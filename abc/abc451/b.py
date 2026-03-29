N, M = map(int, input().split())

busyo_before = [0] * M
busyo_after = [0] * M

for _ in range(N):
    a, b = map(int, input().split())
    busyo_before[a - 1] += 1
    busyo_after[b - 1] += 1

for i in range(M):
    print(busyo_after[i] - busyo_before[i])