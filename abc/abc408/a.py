n, s = map(int, input().split())
t = list(map(int, input().split()))
t.insert(0, 0)
for i in range(n):
    if t[i+1] - t[i] > s:
        print('No')
        exit()
print('Yes')
