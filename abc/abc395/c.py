n = int(input())
a = list(map(int, input().split()))

num_pos = dict()
shortest_len = n + 1

for i in range(n):
    preb_pos = num_pos.get(a[i])
    if preb_pos == None:
        num_pos[a[i]] = i
    else:
        shortest_len = min(shortest_len, i - preb_pos)
        num_pos[a[i]] = i

if shortest_len == n + 1:
    print(-1)
else:
    print(shortest_len + 1)