import bisect

n, m = map(int, input().split())
ad_list = []
for _ in range(m):
    a, b = map(int, input().split())
    ad_list.append((a, a-b))

# 今持っている瓶入りコーラで最も効率よく交換できる行動をとる（貪欲法）
# diff = ai - bi
# ai <= n_bottleの中で最大のdiffを選択

# 更新式
# change_count = (n_bottle - a) // diff + 1 回交換できる
# n_bottle -=change_count * diffとなる

ad_list.sort()

A = [a for a, _ in ad_list]

n_bottle = n

min_diff = 10**18
min_a = 0
min_ad_list = []

for i in range(m):
    if ad_list[i][1] < min_diff:
        min_diff = ad_list[i][1]
        min_a = ad_list[i][0]

    min_ad_list.append((min_a, min_diff))

ans = 0

while n_bottle > 0:
    idx = bisect.bisect_right(A, n_bottle) - 1
    if idx == -1:
        break

    diff = min_ad_list[idx][1]
    a = min_ad_list[idx][0]
    change_count = (n_bottle - a) // diff + 1
    n_bottle -= change_count * diff
    ans += change_count

print(ans)
