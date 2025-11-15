n, m, k = map(int, input().split())
h = list(map(int, input().split()))
b = list(map(int, input().split()))

h.sort()
b.sort()

b_pos = 0
cnt = 0

for i in range(n):
    while b_pos < m and b[b_pos] < h[i]:
        b_pos += 1
    if b_pos == m:
        break
    cnt += 1
    b_pos += 1
    if cnt == k:
        print('Yes')
        exit()

print('No')