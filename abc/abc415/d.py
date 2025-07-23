import bisect

n, m = map(int, input().split())
abc = []
for _ in range(m):
    a, b = map(int, input().split())
    abc.append((a, b, b / a))

# 今持っている瓶入りコーラで最も効率よく交換できる行動をとる（貪欲法）
# ci =  bi / ai
# ai <= n_bottleの中で最大のciを選択

# 更新式
# diff = ai - bi
# change_count = (n_bottle - a) // diff + 1 回交換できる
# n_bottle -=change_count * diffとなる

n_bottle = n
total_change_count = 0

abc.sort()
a = [a for a, b, c in abc]

while n_bottle > 0:
    idx = bisect.bisect_right(a, n_bottle)
    if idx == 0:
        break
    
    possible_action = abc[0:idx]
    max_c = max(possible_action, key=lambda x: x[2])
    # print(max_c)

    diff = max_c[0] - max_c[1]
    change_count = (n_bottle - max_c[0]) // diff + 1
    n_bottle -= change_count * diff
    # print(n_bottle, change_count, diff)

    total_change_count += change_count

print(total_change_count)
