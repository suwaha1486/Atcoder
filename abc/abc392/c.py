n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

qp = []
for i in range(n):
    qp.append([q[i], p[i]])

qp.sort()

ans = []
for i in range(n):
    ans.append(q[qp[i][1] - 1])

print(*ans, sep=' ')