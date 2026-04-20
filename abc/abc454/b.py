N, M = map(int, input().split())
F = list(map(int, input().split()))

cloth_list = [0] * M

for i in range(N):
    cloth_list[F[i] - 1] += 1

if all(x < 2 for x in cloth_list):
    print('Yes')
else:
    print('No')

if cloth_list.count(0) == 0:
    print('Yes')
else:
    print('No')