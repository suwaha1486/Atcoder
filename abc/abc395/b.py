n = int(input())

a = [['#'] * n for _ in range(n)]
for i in range(1, n//2+1):
    for j in range(i, n-i):
        for k in range(i, n-i):
                if i % 2 == 1:
                    a[j][k] = '.'
                else:
                    a[j][k] = '#'

for i in range(n):
    print(*a[i], sep='')