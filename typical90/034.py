# ★4
'''
〇〇を満たす区間の内，最小or最大の長さ
〇〇を満たす区間を数え上げよ
-> 尺取り法
'''
from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

number = defaultdict(int)
ans = 0
right = 0

for left in range(n):
    # rightを可能な限り右に伸ばす
    while right < n and (len(number) < k or a[right] in number):
        number[a[right]] += 1
        right += 1
    ans = max(ans, right - left)
    number[a[left]] -= 1
    if number[a[left]] == 0:
        del number[a[left]]

print(ans)
        
