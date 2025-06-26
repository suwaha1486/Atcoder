from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

a_start0 = []
a_start1 = []
if n % 2 == 0:
    for i in range(n//2):
        if a[i*2] == a[i*2+1]:
            a_start0.append(a[i*2])
        else:
            a_start0.append(-1)

        if i > 0:
            if a[i*2-1] == a[i*2]:
                a_start1.append(a[i*2-1])
            else:
                a_start1.append(-1)
else:
    for i in range(n//2):
        if a[i*2] == a[i*2+1]:
            a_start0.append(a[i*2])
        else:
            a_start0.append(-1)

        if a[i*2+1] == a[i*2+2]:
            a_start1.append(a[i*2+1])
        else:
            a_start1.append(-1)

num_pos = defaultdict(int)

ans = 0
start_pos = 0

for i in range(len(a_start0)):
    if a_start0[i] == -1:
        ans = max(ans, i - start_pos)
        start_pos = i + 1
        continue

    if a_start0[i] in num_pos and num_pos[a_start0[i]] >= start_pos:
        ans = max(ans, i - start_pos)
        start_pos = num_pos[a_start0[i]] + 1
    num_pos[a_start0[i]] = i

ans = max(ans, len(a_start0) - start_pos)

num_pos = defaultdict(int)
start_pos = 0

for i in range(len(a_start1)):
    if a_start1[i] == -1:
        ans = max(ans, i - start_pos)
        start_pos = i + 1
        continue

    if a_start1[i] in num_pos and num_pos[a_start1[i]] >= start_pos:
        ans = max(ans, i - start_pos)
        start_pos = num_pos[a_start1[i]] + 1
    num_pos[a_start1[i]] = i

ans = max(ans, len(a_start1) - start_pos)

print(ans * 2)