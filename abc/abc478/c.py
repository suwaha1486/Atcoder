N, K = map(int, input().split())
A = list(map(int, input().split()))

sorted_A = sorted(A)

diff = []
for i in range(N):
    if A[i] != sorted_A[i]:
        diff.append(i)

if len(diff) == 0:
    print("Yes")
elif diff[-1] - diff[0] + 1 <= K:
    print("Yes")
else:
    print("No")