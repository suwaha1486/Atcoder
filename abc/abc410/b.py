n, q = map(int, input().split())
x = list(map(int, input().split()))

box = [0] * n
b = []
for i in range(q):
    if x[i] >= 1:
        b.append(x[i])
        box[x[i] - 1] += 1
    else:
        box_idx = -1
        box_balls = 10**9
        for i in range(n):
            if box_balls > box[i]:
                box_balls = box[i]
                box_idx = i
        b.append(box_idx + 1)
        box[box_idx] += 1

print(*b)