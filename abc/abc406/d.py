h, w, n = map(int, input().split())

x = [set() for _ in range(h)]
y = [set() for _ in range(w)]
for i in range(n):
    a, b = map(int, input().split())
    x[a-1].add(b-1)
    y[b-1].add(a-1)

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    b -= 1

    if a == 1:
        print(len(x[b]))
        for j in x[b]:
            y[j].remove(b)
        x[b].clear()
    else:
        print(len(y[b]))
        for j in y[b]:
            x[j].remove(b)
        y[b].clear()
