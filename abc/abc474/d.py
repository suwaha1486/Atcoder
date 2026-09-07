N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

MAX = 10**18

diff = [[i, A[i] - B[i]] for i in range(N)]

diff.sort(key=lambda x: x[1])

ans = [0] * N
tmp_sum = 0
for i in range(N):
    if diff[i][1] < 0:
        ans[diff[i][0]] = 1
        tmp_sum += diff[i][1]
    else:
        ans[diff[i][0]] = MAX
        tmp_sum += diff[i][1] * MAX

if tmp_sum <= 0:
    print("No")
else:
    print("Yes")
    print(*ans)