from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

element_sum = defaultdict(int)

for i in range(N):
    element_sum[A[i]] += A[i]

element_sum = sorted(element_sum.items(), key=lambda x: x[1])

ans = 0
for i in range(len(element_sum) - K):
    ans += element_sum[i][1]

print(ans)