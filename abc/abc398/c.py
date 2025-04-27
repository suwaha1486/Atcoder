# 解けてない

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
if n == 2:
    if a[0] > a[1]:
        print(1)
    elif a[0] < a[1]:
        print(2)
    else:
        print(-1)
    exit()
    

for i in range(n):
    a[i] = [a[i], i+1]

a.sort(reverse=True)

for i in range(1, n-1):
    if a[i-1][0] != a[i][0] and a[i+1][0] != a[i][0]:
        print(a[i][1])
        exit()

print(-1)