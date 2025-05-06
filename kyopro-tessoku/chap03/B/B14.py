n, k = map(int, input().split())
a = list(map(int, input().split()))

a1 = a[:n // 2]
a2 = a[n // 2:]

a1_set = set()
a2_set = set()

for i in range(1 << len(a1)):
    sum1 = 0
    for j in range(len(a1)):
        if i & (1 << j):
            sum1 += a1[j]
    a1_set.add(sum1)
for i in range(1 << len(a2)):
    sum2 = 0
    for j in range(len(a2)):
        if i & (1 << j):
            sum2 += a2[j]
    a2_set.add(sum2)

for x in a1_set:
    if k - x in a2_set:
        print("Yes")
        exit()

print("No")