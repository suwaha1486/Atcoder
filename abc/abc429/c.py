from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

pos_dict = defaultdict(int)

for i in range(n):
    pos_dict[a[i]] += 1

cnt = 0

for key, value in pos_dict.items():
    if value >= 2:
        cnt += value * (value - 1) // 2 * (n - value)

print(cnt)