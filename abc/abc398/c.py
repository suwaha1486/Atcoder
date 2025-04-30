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
a.append((0, -1))
a_max = 1000000001

for i in range(n):
    if a[i][0] != a_max and a[i][0] != a[i+1][0]:
        print(a[i][1])
        exit()
    else:
        a_max = a[i][0]

print(-1)