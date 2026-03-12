N, M = map(int, input().split())
C = list(map(int, input().split()))

ans = 0

for i in range(N):
    A, B = map(int, input().split())
    ans += min(C[A-1], B)
    C[A-1] = max(C[A-1]-B, 0)

print(ans)
