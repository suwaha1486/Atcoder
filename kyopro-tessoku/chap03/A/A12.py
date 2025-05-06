n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = 10 ** 9

while left + 1 < right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(n):
        cnt += mid // a[i]
    if cnt < k:
        left = mid
    else:
        right = mid

print(right)