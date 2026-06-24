N, K = map(int, input().split())
LR = list(list(map(int, input().split())) for _ in range(N))

LR.sort(key=lambda x: x[1])

def check(x):
    cnt = 0
    last = 0
    for l, r in LR:
        if last <= l:
            cnt += 1
            last = r + x + 1
    return cnt >= K

if not check(0):
    print(-1)
else:
    left = 0
    right = 10 ** 10
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid
    print(left + 1)
