n = int(input())
a = list(map(int, input().split()))
x = int(input())

for i in range(n):
    if a[i] == x:
        print('Yes')
        break
else:
    print("No")
