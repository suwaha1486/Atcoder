n, m = map(int, input().split())

x = 0

inf = 1000000000

for i in range(m + 1):
    x += n ** i
    if x > inf:
        print('inf')
        exit()

print(x)