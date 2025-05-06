n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

ab = set()
cd = set()

for i in range(n):
    for j in range(n):
        ab.add(a[i] + b[j])
        cd.add(c[i] + d[j])

for x in ab:
    if k - x in cd:
        print("Yes")
        exit()

print("No")