# ★3
from itertools import permutations
from collections import defaultdict

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
m = int(input())
bad_pair = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    bad_pair[x].append(y)
    bad_pair[y].append(x)

ans = 10**10
for order in permutations(range(1, n+1)):
    valid = True
    tmp = 0
    for j in range(n):
        if j < n-1 and order[j+1] in bad_pair[order[j]]:
            valid = False
            break
        tmp += a[order[j]-1][j]
    if valid:
        ans = min(ans, tmp)

if ans == 10**10:
    print(-1)
else:
    print(ans)
