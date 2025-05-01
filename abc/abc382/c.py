n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 解けてない

for i in range(m):
  for j in range(n):
    if b[i] >= a[j]:
      print(j+1)
      break
    if j == n-1:
      print(-1)
