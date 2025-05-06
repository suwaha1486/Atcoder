import bisect

n = int(input())
a = list(map(int, input().split()))

a.sort()

q = int(input())

for _ in range(q):
    x = int(input())
    ans = bisect.bisect_left(a, x)
    print(ans)