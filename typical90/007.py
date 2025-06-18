# ★3
from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())

for i in range(q):
    b = int(input())
    idx = bisect_left(a, b)
    if idx == 0:
        print(abs(a[idx] - b))
    elif idx == n:
        print(abs(a[idx - 1] - b))
    else:
        print(min(abs(a[idx] - b), abs(a[idx - 1] - b)))
