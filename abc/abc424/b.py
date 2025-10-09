n, m, k = map(int, input().split())
person = [0] * n
ans = []

for i in range(k):
    a, b = map(int, input().split())
    person[a-1] += 1
    if person[a-1] == m:
        ans.append(a)

print(*ans, sep= ' ')