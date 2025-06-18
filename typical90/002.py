# ★3
from collections import defaultdict

n = int(input())

if n % 2 == 1:
    exit()

if n == 2:
    print('()')
    exit()

parentheses = defaultdict(set)

parentheses[0] = {''}
parentheses[2] = {'()'}

for i in range(4, n+1, 2):
    for p in parentheses[i-2]:
        parentheses[i].add('(' + p + ')')

    for j in range(2, i-1, 2):
        for p1 in parentheses[j]:
            for p2 in parentheses[i-j]:
                parentheses[i].add(p1 + p2)


for i in sorted(parentheses[n]):
    print(i)
