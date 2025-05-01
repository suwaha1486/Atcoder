n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_max = max(b)

score = [-1] * (b_max + 1)

r = b_max + 1

for i in range(n):
  while r > a[i]:
    r -= 1
    score[r] = i + 1

answers = []

for i in range(m):
  answers.append(score[b[i]])

for ans in answers:
  print(ans)
