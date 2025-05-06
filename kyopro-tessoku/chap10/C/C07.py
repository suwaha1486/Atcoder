import bisect
n = int(input())
c = list(map(int, input().split()))
c.sort()
c = [0] + c

for i in range(1, n + 1):
    c[i] += c[i - 1]

q = int(input())

for i in range(q):
    x = int(input())
    idx = bisect.bisect_right(c, x)
    print(idx - 1)