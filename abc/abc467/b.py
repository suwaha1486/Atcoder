N = int(input())

ans = 0
for i in range(N):
    a, b, s = input().split()
    a = int(a)
    b = int(b)
    if s == 'keep':
        ans += b - a

print(ans)