N, D = map(int, input().split())
ST = []
max_t = 0
for _ in range(N):
    s, t = map(int, input().split())
    if s > t - D:
        continue
    ST.append((s, t - D))
    max_t = max(max_t, t)

max_t += 1
A = [0] * max_t

for s, t in ST:
    A[s] += 1
    A[t + 1] -= 1

for i in range(1, max_t):
    A[i] += A[i - 1]

ans = 0
for i in range(max_t):
    ans += A[i] * (A[i] - 1) // 2

print(ans)