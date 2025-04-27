n = int(input())
a = list(map(int, input().split()))

tmp = a[0]
cnt = 1
for i in range(1, n):
  if a[i] == tmp:
    cnt += 1
    if cnt == 3:
      print('Yes')
      exit()
  else:
    tmp = a[i]
    cnt = 1
print('No')