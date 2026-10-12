N = int(input())
S = input()

rain_max = 0
rain_count = 0

for i in range(N):
    if S[i] == 'R':
        rain_count += 1
    else:
        rain_max = max(rain_max, rain_count)
        rain_count = 0

rain_max = max(rain_max, rain_count)

print(rain_max)