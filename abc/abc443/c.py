N, T = map(int, input().split())
A = list(map(int, input().split()))

Watch_time = 0
Start_time = 0

for a in A:
    if Start_time < a:
        Watch_time += a - Start_time
        Start_time = a + 100
        if Start_time > T:
            break

if Start_time <= T:
    Watch_time += T - Start_time

print(Watch_time)