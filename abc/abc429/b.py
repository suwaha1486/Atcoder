n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = sum(a)

for i in range(n):
    if a_sum - a[i] == m:
        print('Yes')
        exit()

print('No')