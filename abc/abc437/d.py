N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

TMP = 998244353

A.sort()
B.sort()

cumsum_A = [0] * (N+1)

for i in range(N):
    cumsum_A[i+1] = cumsum_A[i] + A[i]

# A[i] <= B[j]となる最小のiに関して， 
# ( (i + 1) * B[j] - cumsum_A[i + 1] ) + ( (cumsum_A[N] - cumsum_A[i + 1] ) - (N - i - 1) * B[j] ) を最小化する

# 尺取り法でB[j]を固定して，A[i] <= B[j]となる最小のiを探す

ans = 0
right = 0
for i in range(M):
    while right < N and A[right] <= B[i]:
        right += 1

    tmp = right * B[i] % TMP - cumsum_A[right] % TMP + (cumsum_A[N] - cumsum_A[right]) % TMP - (N - right) * B[i] % TMP
    ans = (ans + tmp) % TMP

print(ans)