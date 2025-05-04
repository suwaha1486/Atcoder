from collections import deque

n, x = map(int, input().split())
a = list(input())

que = deque()

que.append(x-1)

a[x-1] = '@'

while len(que) > 0:
    pos = que.popleft()
    if 0 <= pos - 1 and a[pos-1] == '.':
        a[pos-1] = '@'
        que.append(pos-1)
    if pos + 1 < n and a[pos+1] == '.':
        a[pos+1] = '@'
        que.append(pos+1)

print(*a, sep='')