from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num_count = defaultdict(int)
for i in range(N):
    num_count[A[i]] += 1

ans = 0
for key, value in num_count.items():
    if value % 2 == 1:
        ans += key

print(ans)
