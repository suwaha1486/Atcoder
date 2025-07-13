n, m = map(int, input().split())
x = list(map(int, input().split()))

if n == m:
    print(0)
    exit()

x.sort()
if m == 1:
    print(x[-1] - x[0])
    exit()

x = set(x)
x = list(x)
n = len(x)

# m-1個の間隔を選ぶ
space = []
for i in range(n-1):
    space.append(x[i+1] - x[i])
space.sort(reverse=True)
ans = (x[-1] - x[0]) - sum(space[:m-1])
print(ans)
