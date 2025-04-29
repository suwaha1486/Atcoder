n, s = map(int, input().split())
a = list(map(int, input().split()))

# 1周期分の合計で余りを取る
sum_a = sum(a)
s %= sum_a

# 配列を2周期分に拡張
a = a + a

# 尺取り法で解く
right = 0
current_sum = 0

for left in range(n):
    # rightを進められるだけ進める
    while right < 2*n and current_sum < s:
        current_sum += a[right]
        right += 1
    
    # 合計がsと等しければYes
    if current_sum == s:
        print('Yes')
        exit()
    
    # leftを進める前に、左端の値を引く
    current_sum -= a[left]

print('No')