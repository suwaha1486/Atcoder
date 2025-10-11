n, q = map(int, input().split())
a = list(map(int, input().split()))

prefix_sum = [0] * (2 * n + 1)
for i in range(2 * n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i % n]

head_pos = 0

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        head_pos = (head_pos + c) % n
    else:
        l, r = query[1], query[2]
        start = head_pos + l - 1
        end = head_pos + r - 1
        
        lr_sum = prefix_sum[end + 1] - prefix_sum[start]
        print(lr_sum)