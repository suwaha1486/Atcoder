n = int(input())
a = list(map(int, input().split()))

print(-1)

for i in range(1, n):
    for j in range(i, -1, -1):
        if a[j] > a[i]:
            print(j+1)
            break
    else:
        print(-1)