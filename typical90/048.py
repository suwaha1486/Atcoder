n, k = map(int, input().split())
ab = []

for i in range(n):
    a, b = map(int, input().split())
    ab.append(b)
    ab.append(a - b)

ab.sort(reverse=True)

print(sum(ab[:k]))
