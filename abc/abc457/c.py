N, K = map(int, input().split())
A = []
L = []

for i in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    A.append(tmp[1:])

C = list(map(int, input().split()))

# total_len += L[i] * C[i] 
# total_len <= K
total_len = 0
i = 0

while i < N and total_len + L[i] * C[i] < K:
    total_len += L[i] * C[i]
    i += 1

# i 番目ブロック内での 0-index 位置を求める
pos = (K - total_len - 1) % L[i]

print(A[i][pos])
