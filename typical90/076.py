import bisect

n = int(input())
a = list(map(int, input().split()))

whole = sum(a)
if whole % 10 != 0:
    print('No')
    exit()

a += a
cumsum = [0] * (n * 2 + 1)
for i in range(n * 2):
    cumsum[i + 1] = cumsum[i] + a[i]

for i in range(n):
    pos = bisect.bisect_left(cumsum, cumsum[i] + whole / 10)
    if pos < n * 2 and cumsum[pos] - cumsum[i] == whole / 10:
        print('Yes')
        exit()

print('No')
