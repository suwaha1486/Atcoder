n = int(input())

cnt = 0
at = 2

while at <= n:
    r = n // at
    l = 1
    while l+1 < r:
        mid = (l + r) // 2
        if at * (mid ** 2) > n:
            r = mid
        else:
            l = mid
    cnt += (l + 1) // 2
    at *= 2

print(cnt) 