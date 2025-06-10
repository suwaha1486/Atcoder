n = int(input())
a = list(map(int, input().split()))

# x <= n
for x in range(n, -1, -1):
    cnt = 0
    for i in range(n):
        if a[i] >= x:
            cnt += 1
    if cnt >= x:
        print(x)
        exit()
        
print(0)
