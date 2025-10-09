n = int(input())
s = []

for i in range(n):
    s.append(input())

x, y = input().split()
x = int(x)

if s[x-1] == y:
    print('Yes')
else:
    print('No')
    