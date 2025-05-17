n, k = map(int, input().split())
a = list(map(int, input().split()))

max_keta = 10 ** k

num = 1
for i in range(n):
    num *= a[i]
    if num >= max_keta:
        num = 1

print(num)
