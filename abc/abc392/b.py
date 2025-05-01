n, m = map(int, input().split())

a = set(map(int, input().split()))

ans = []
for i in range(n):
    if not (i+1 in a):
        ans.append(i+1)

print(len(ans))
print(*ans, sep=' ')