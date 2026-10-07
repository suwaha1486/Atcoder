N = int(input())
A = list(map(int, input().split()))

A.sort()

keta = [0] * (max(A) + 10)


pre_keta = 0
for i in range(N):
    for j in range(pre_keta, A[i]):
        keta[j] = N - i
    pre_keta = A[i]

for i in range(len(keta) - 1):
    keta[i + 1] += keta[i] // 10
    keta[i] %= 10

while len(keta) > 1 and keta[-1] == 0:
    keta.pop()

print(''.join(map(str, keta[::-1])))