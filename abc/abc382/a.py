n, d = map(int, input().split())
s = input()

cnt = 0
for si in s:
  if si == ".":
    cnt += 1

print(cnt + d)