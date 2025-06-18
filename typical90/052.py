# ★3
n = int(input())

mod = 10**9 + 7
ans = 1

for i in range(n):
    a = list(map(int, input().split()))
    ans *= sum(a)
    ans %= mod

print(ans)
