n = int(input())

if n == 1:
    print(1)
    exit()

a = [1] * (n + 1)

for i in range(2, n+1):
    tmp = 0
    for j in range(len(str(a[i-1]))):
        tmp += int(str(a[i-1])[j])
    a[i] = a[i-1] + tmp

print(a[n])