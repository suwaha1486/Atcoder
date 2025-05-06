from bisect import bisect_left, bisect_right

n, w, l, r = map(int, input().split())
x = [0]
x += list(map(int, input().split()))
x.append(w)

DIV = 10 ** 9 + 7

cum_sum = [0] * (n + 3)
cum_sum[1] = 1
dp = [0] * (n + 2)

for i in range(1, n + 2):
    right_idx = bisect_right(x, x[i] - l)
    left_idx = bisect_left(x, x[i] - r)
    dp[i] = (cum_sum[right_idx] - cum_sum[left_idx]) % DIV
    cum_sum[i + 1] = (cum_sum[i] + dp[i]) % DIV

print(dp[-1])