n = int(input())

a = [[0] * n for _ in range(n)]

a[0][(n-1)//2] = 1
r = 0
c = (n-1)//2
k = 1

for t in range(n * n - 1):
    if a[(r - 1) % n][(c + 1) % n] == 0:
        a[(r - 1) % n][(c + 1) % n] = k + 1
        r = (r - 1) % n
        c = (c + 1) % n
    else:
        a[(r + 1) % n][c] = k + 1
        r = (r + 1) % n
        c = c
    
    k += 1

for i in range(n):
    print(*a[i], sep=' ')