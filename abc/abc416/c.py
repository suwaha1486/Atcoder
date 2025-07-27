from itertools import product

n, k, x = map(int, input().split())

s = []

for i in range(n):
    s.append(input())

f_list = [''.join(t) for t in product(s, repeat=k)]

f_list.sort()

print(f_list[x-1])
