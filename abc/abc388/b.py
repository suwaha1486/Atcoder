n, d = map(int, input().split())

tl = []

for i in range(n):
    tl.append(list(map(int, input().split())))

for k in range(d):
    maxl = 0
    for t, l in tl:
        maxl = max(maxl, t * (l + k + 1))
    print(maxl)